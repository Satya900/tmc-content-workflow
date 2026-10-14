"""Offline TMC photo carousel renderer: brand-overlay text on trip photos.

Implements the "Overlay style for photo carousels" section of brand-brief.md:
Staatliches-style bold hook line (Arial Black offline fallback), DM Sans
(Arial) supporting captions, a dark top-and-bottom vignette for legibility,
text anchored left or right per a calm region of each photo chosen by
actual image content, TMC logo and tagline, page counter and swipe
indicator. On-photo text (title/caption) is capped at 10 words.

Requires Pillow, reportlab and numpy. No network or paid API is used.

Consent gate: every input file must declare consent_status. Rendering is
refused unless it is APPROVED or NOT_APPLICABLE. UNKNOWN or DENIED never
produce an export -- presence of a photo file is never treated as consent.
"""
import argparse
import base64
import hashlib
import json
import re
import shutil
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageStat
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

from tmc_fonts import find_fonts

ROOT = Path(__file__).resolve().parents[1]
CYAN = (26, 175, 224)
DEEP = (14, 127, 166)
WHITE = (255, 255, 255)
BAN = r'\b(skyrocket|revolutionize|unlock|unveil|illuminate|paradigm|realm|esteemed|remarkable|testament|stark|however|kindly)\b|[—;!]'
CONSENT_OK = {'APPROVED', 'NOT_APPLICABLE'}
MAX_OVERLAY_WORDS = 10


def validate(data, photos_dir):
    if not isinstance(data, dict):
        raise ValueError('Input must be a JSON object')
    for key in ('id', 'version', 'title', 'post_caption', 'consent_status'):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f'Missing text field: {key}')
    if data.get('category') not in ('MARKETING', 'TOUR'):
        raise ValueError('category must be MARKETING or TOUR')
    if data['consent_status'] not in CONSENT_OK:
        raise ValueError(
            f"Render blocked: consent_status is '{data['consent_status']}'. "
            "A photo carousel needs APPROVED (identifiable people, permission on file) "
            "or NOT_APPLICABLE (no identifiable people) before it renders. "
            "UNKNOWN or DENIED must not produce an export."
        )
    if not re.fullmatch(r'[A-Za-z0-9_-]+', data['id'] + data['version']):
        raise ValueError('ID and version must be filename-safe')
    if len(data['title'].split()) > MAX_OVERLAY_WORDS:
        raise ValueError(f'Title is on-photo overlay text: max {MAX_OVERLAY_WORDS} words')
    slides = data.get('slides')
    if not isinstance(slides, list) or not 2 <= len(slides) <= 12:
        raise ValueError('Supply 2 to 12 slides')
    copy = [data['title'], data['post_caption']]
    for i, s in enumerate(slides, 1):
        if not isinstance(s, dict) or not isinstance(s.get('file'), str):
            raise ValueError(f'Slide {i}: expected an object with a file name')
        if not (Path(photos_dir) / s['file']).is_file():
            raise ValueError(f"Slide {i}: photo not found: {s['file']}")
        for key in ('caption', 'label'):
            if key in s and not isinstance(s[key], str):
                raise ValueError(f'Slide {i}: {key} must be text')
        if len(s.get('caption', '').split()) > MAX_OVERLAY_WORDS:
            raise ValueError(f'Slide {i}: caption is on-photo overlay text: max {MAX_OVERLAY_WORDS} words')
        copy.extend([s.get('caption', ''), s.get('label', '')])
    if re.search(BAN, '\n'.join(copy), re.I):
        raise ValueError('Copy contains a prohibited TMC word or punctuation mark')


def cover_fit(image, w, h):
    src_ratio, dst_ratio = image.width / image.height, w / h
    if src_ratio > dst_ratio:
        new_h = h; new_w = round(h * src_ratio)
    else:
        new_w = w; new_h = round(w / src_ratio)
    image = image.resize((new_w, new_h), Image.Resampling.LANCZOS)
    x = (new_w - w) // 2; y = (new_h - h) // 2
    return image.crop((x, y, x + w, y + h))


def calm_corner(image):
    """Pick the calmer (lower edge-energy) of the two bottom quadrants for text."""
    edges = image.convert('L').filter(ImageFilter.FIND_EDGES)
    w, h = edges.size
    left = ImageStat.Stat(edges.crop((0, h // 2, w // 2, h))).mean[0]
    right = ImageStat.Stat(edges.crop((w // 2, h // 2, w, h))).mean[0]
    return 'bottom-left' if left <= right else 'bottom-right'


def vignette(w, h, edge, strength, span_fraction):
    """Full-width dark gradient from `edge` ('top' or 'bottom'), fading over span_fraction of the height."""
    span = max(1, round(h * span_fraction))
    column = np.zeros(h, dtype=np.float32)
    fade = np.linspace(1, 0, span) ** 1.4
    if edge == 'top':
        column[:span] = fade
    else:
        column[h - span:] = fade[::-1]
    alpha = np.tile(column.reshape(h, 1), (1, w))
    layer = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    layer.putalpha(Image.fromarray((alpha * strength).astype(np.uint8)))
    return layer


def draw_shadowed(draw, xy, text, font, fill):
    x, y = xy
    draw.text((x + 2, y + 3), text, font=font, fill=(0, 0, 0, 150))
    draw.text((x, y), text, font=font, fill=fill)


def wrap(text, font, width):
    lines, current = [], ''
    for word in text.split():
        trial = f'{current} {word}'.strip()
        if current and font.getlength(trial) > width:
            lines.append(current); current = word
        else:
            current = trial
    if current: lines.append(current)
    return lines


def compose_slide(photo_path, s, index, total, height, fonts, logo, is_cover, title):
    w = 1080
    base = cover_fit(Image.open(photo_path).convert('RGB'), w, height).convert('RGBA')
    anchor = 'bottom-left' if is_cover else calm_corner(base)
    caption = s.get('caption', '').strip()
    has_text = is_cover or caption
    base = Image.alpha_composite(base, vignette(w, height, 'top', strength=210, span_fraction=0.22))
    if has_text:
        base = Image.alpha_composite(base, vignette(w, height, 'bottom', strength=240, span_fraction=0.5 if is_cover else 0.4))
    draw = ImageDraw.Draw(base)
    left = anchor == 'bottom-left'
    margin = 64
    text_width = w - margin * 2

    # page counter, top-left
    small = ImageFont.truetype(str(fonts['bold']), 26)
    draw_shadowed(draw, (margin, 48), f'{index:02d}/{total:02d}', small, WHITE)

    # logo (tagline is already part of the logo artwork), top-right
    logo_w = 148
    logo_h = round(logo_w * logo.height / logo.width)
    resized_logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
    base.paste(resized_logo, (w - margin - logo_w, 40), resized_logo)

    if has_text:
        y = height - 96
        if not is_cover:
            y -= 34  # room for swipe row
        lines = []
        if is_cover:
            font = ImageFont.truetype(str(fonts['display']), 92 if height > 1080 else 78)
            lines = [(l, font, CYAN) for l in wrap(title.upper(), font, text_width)]
        else:
            if s.get('label'):
                lf = ImageFont.truetype(str(fonts['bold']), 26)
                lines.append((s['label'].upper(), lf, DEEP))
            cf = ImageFont.truetype(str(fonts['bold']), 40)
            lines += [(l, cf, WHITE) for l in wrap(caption, cf, text_width)]
        block_h = sum(round(f.size * 1.25) for _, f, _ in lines)
        y -= block_h
        for text, font, color in lines:
            x = margin if left else w - margin - font.getlength(text)
            draw_shadowed(draw, (x, y), text, font, color)
            y += round(font.size * 1.25)

    if index < total:
        sf = ImageFont.truetype(str(fonts['bold']), 26)
        label = 'Swipe \u2192'
        draw_shadowed(draw, (w - margin - sf.getlength(label), height - 58), label, sf, WHITE)

    return base.convert('RGB')


def render(source, photos_dir, output, fonts_dir=None):
    source, photos_dir, output = Path(source), Path(photos_dir), Path(output)
    data = json.loads(source.read_text(encoding='utf-8-sig'))
    validate(data, photos_dir)
    if output.exists():
        raise ValueError('Output exists. Choose a new output directory to preserve reviewed versions.')
    fonts = find_fonts(fonts_dir)
    logo = Image.open(ROOT / 'logos' / 'TMC_Logo_Dark_Mode_CRM.png').convert('RGBA')
    output.parent.mkdir(parents=True, exist_ok=True)
    total = len(data['slides'])
    with tempfile.TemporaryDirectory(prefix='tmc-photo-render-') as scratch:
        stage = Path(scratch)
        for name, height in [('instagram_4x5', 1350), ('square_1x1', 1080)]:
            directory = stage / name; directory.mkdir()
            images = []
            for i, s in enumerate(data['slides'], 1):
                img = compose_slide(photos_dir / s['file'], s, i, total, height, fonts, logo, i == 1, data['title'])
                img.save(directory / f'{i:02d}.png', quality=92)
                images.append(img)
            if name == 'instagram_4x5':
                pdf_path = stage / f"{data['title'].replace(' ', '_')}.pdf"
                pdf = canvas.Canvas(str(pdf_path), pagesize=(540, 675))
                pdf.setTitle(data['title']); pdf.setSubject('Preview awaiting human review')
                for im in images:
                    pdf.drawImage(ImageReader(im), 0, 0, 540, 675); pdf.showPage()
                pdf.save()
                rows = (len(images) + 2) // 3
                contact = Image.new('RGB', (900, rows * 375), '#0E0E0E')
                for j, im in enumerate(images):
                    thumb = im.resize((280, 350), Image.Resampling.LANCZOS)
                    contact.paste(thumb, ((j % 3) * 300 + 10, (j // 3) * 375 + 10))
                contact.save(stage / 'contact-sheet.png')
        shutil.copyfile(source, stage / 'story.json')
        (stage / 'caption.txt').write_text(data['post_caption'] + '\n', encoding='utf-8')
        alt = ['# Alt text for preview visuals\n']
        for i, s in enumerate(data['slides'], 1):
            desc = s.get('caption') or s.get('label') or 'photo, no caption text on this slide'
            alt.append(f"{i}. TMC trip photo carousel slide. {desc}")
        (stage / 'alt-text.md').write_text('\n\n'.join(alt), encoding='utf-8')
        manifest = {
            'id': data['id'], 'version': data['version'], 'status': 'REVIEW',
            'human_approval': None, 'publication': None, 'renderer': 'photo-overlay-v1',
            'consent_status_declared': data['consent_status'],
            'font_mode': 'approved offline fallback: Arial Black and Arial',
            'dimensions': {'instagram_4x5': [1080, 1350], 'square_1x1': [1080, 1080]},
            'files_sha256': {str(p.relative_to(stage)).replace('\\', '/'): hashlib.sha256(p.read_bytes()).hexdigest() for p in stage.rglob('*') if p.is_file()},
        }
        (stage / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
        shutil.copytree(stage, output)
    return output


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('source'); ap.add_argument('--photos-dir', required=True)
    ap.add_argument('--output', required=True)
    ap.add_argument('--fonts-dir', help='Folder holding Arial and Arial Black (default: search the standard OS font folders)')
    args = ap.parse_args()
    try:
        print(render(args.source, args.photos_dir, args.output, args.fonts_dir))
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        ap.exit(1, f'Render blocked: {exc}\n')
