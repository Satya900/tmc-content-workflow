"""Locates the approved offline fallback fonts (Arial Black and Arial) on Windows, macOS or Linux.

Arial Black stands in for Staatliches and Arial for DM Sans, per brand-brief.md.
The same fonts ship under different file names per OS, so each role lists every
known spelling. Pass fonts_dir to search only that folder.
"""
import os
from pathlib import Path

FONT_FILES = {
    'display': ['ariblk.ttf', 'Arial Black.ttf', 'Arial_Black.ttf'],
    'body': ['arial.ttf', 'Arial.ttf'],
    'bold': ['arialbd.ttf', 'Arial Bold.ttf', 'Arial_Bold.ttf'],
}


def default_dirs():
    dirs = [Path(os.environ.get('WINDIR', 'C:/Windows')) / 'Fonts',
            Path.home() / 'Library' / 'Fonts', Path('/Library/Fonts'),
            Path('/System/Library/Fonts/Supplemental'), Path('/System/Library/Fonts'),
            Path.home() / '.local' / 'share' / 'fonts', Path.home() / '.fonts',
            Path('/usr/share/fonts/truetype/msttcorefonts'), Path('/usr/share/fonts')]
    if os.environ.get('LOCALAPPDATA'):
        dirs.insert(1, Path(os.environ['LOCALAPPDATA']) / 'Microsoft' / 'Windows' / 'Fonts')
    return dirs


def find_fonts(fonts_dir=None):
    """Return {'display', 'body', 'bold'} -> Path, or raise ValueError naming what is missing."""
    dirs = [Path(fonts_dir)] if fonts_dir else default_dirs()
    found, missing = {}, []
    for role, names in FONT_FILES.items():
        for d in dirs:
            hit = next((d / n for n in names if (d / n).is_file()), None)
            if hit:
                found[role] = hit
                break
        else:
            missing.append(f"{role} ({' or '.join(names)})")
    if missing:
        where = ', '.join(str(d) for d in dirs)
        raise ValueError(f"Required offline fallback font missing: {'; '.join(missing)}. Searched: {where}. "
                         'Install Arial and Arial Black or pass --fonts-dir.')
    return found
