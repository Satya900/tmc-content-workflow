# TMC Brand Brief — for carousel generation

Condensed from `TMC_Design_Elements.docx` v1.0 (06 May 2026). Full doc
has print/web/motion rules too; this file keeps only what matters for
generating Instagram/LinkedIn carousels. Feed this to open-carrusel's
Brand Setup wizard, or to Claude Code when it's designing slides.

## Colors

| Name | Hex | Use for | Notes |
|---|---|---|---|
| Classroom Cyan | `#1AAFE0` | Headlines, day numbers/chips, CTAs, icon strokes, links | **Fails AA contrast on white below 18pt** — large display text only, never small captions |
| Cyan Deep | `#0E7FA6` | Cyan text under 18pt, button hover/pressed states | Passes AA (4.7:1) — use this for small cyan text instead of Classroom Cyan |
| Cyan Wash | `#E6F6FB` | Callout/quote backgrounds, soft panel tints | |
| Modern Charcoal | `#3F3F3F` | H1/H2 headings on white | |
| Anchor Black | `#0E0E0E` | Body text, captions, outlines, logo mark | |
| Mist Grey | `#F2F4F6` | Card backgrounds, alternating panels | |
| Paper White | `#FFFFFF` | Dominant background — always the largest area | |

**Ratio: 70% white surface, 20% neutrals, 10% cyan.** If cyan is everywhere, nothing stands out.

## Fonts

- **Display — Staatliches** (free, Google Fonts): tagline, hero headlines, day chips/numbers, short destination-sign phrases. ALL CAPS only, letter-spacing 30–60. Never for body or anything under 18pt.
- **Body — DM Sans** (free, Google Fonts): everything else. Regular (400) for body, Bold (700) for subheads, Medium (500) for captions/labels.
- Two families max, two weights each. Sentence case for headings — all caps is reserved for Staatliches/tagline.
- Office fallback (no internet): Arial Black or Bebas Neue for display, Arial or Calibri for body.

## Logo

- Files: `TMC_Logo_Primary_CRM.png` (full color, use on white/light) and `TMC_Logo_Dark_Mode_CRM.png` (reverse, use on Cyan Deep/Anchor Black/photos).
- The hand-drawn circle is intentional — never redraw as a perfect ring, never add drop shadows/glows/gradients.
- Clear space on all sides = height of the lowercase "t" in "classroom." Minimum size: 96px digital.
- On reels/video: reverse logo, bottom-right corner, 6–8% of frame width, static (don't animate after intro).
- Tagline "TRAVEL. EXPERIENCE. LEARN." — always this order, all caps, two spaces between words, periods included. Never move it above the wordmark or reword it.

## Photo selection (what to pick when curating a day's folder)

**Prefer:** students reacting (not posing), wide environmental shots that place students in the location, honest moments (tired feet, group hugs, full plates), at least one teacher visible in group shots, one clean establishing shot of the destination alone.

**Avoid using as hero/cover shots:** stiff lined-up group photos, peace-sign/selfie-stick poses, anything shot in Full HDR, wide shots of no people at all.

**Reminder:** written consent required before publishing any student's face — flag if unsure a shot has clearance.

## Caption voice

Direct, specific, warm — like a class teacher talking to a parent. Name the actual place/dish/museum. If a day was long, say so; trust comes from accuracy, not hype.

- **Do:** "Day 3. A waffle stop at Grand Place, then the Atomium."
- **Don't:** "Embark on an unforgettable journey of cultural awakening."

**Never use:** skyrocket, revolutionize, unlock, unveil, illuminate, paradigm, realm, esteemed, remarkable, testament, stark, however, kindly, "esteemed parents," "valued patrons."

**Never use:** em dashes, semicolons, exclamation points.

## Export sizes (from the brand doc's channel table)

- Instagram feed carousel: **1080×1350** (matches open-carrusel's recommended 4:5)
- Instagram/Facebook Reel: 1080×1920, keep bottom 200px / top 250px clear of text (UI overlays)
- WhatsApp share image: 1080×1080

## Overlay style for photo carousels (dynamic, on-brand)

Goal: scroll-stopping text-on-photo carousels, without breaking the
brand system above. This is a deliberate blend — TMC's real
typography and colors, arranged with the energy of a handwritten
carousel, but without adopting the handwritten look itself.

- **Typography stays TMC's.** Staatliches for the hook line — short,
  punchy, one sentence max. Its tall condensed all-caps form already
  reads as bold and dynamic without needing a script font. DM Sans
  Medium for any supporting line. No handwritten/cursive fonts — none
  exist in the TMC system, and the brand doc caps type families at two.
- **Placement is dynamic, not dead-center.** Put the hook line in the
  photo's calm negative space (rule of thirds, away from faces) —
  upper-left on one slide, lower-right on the next, wherever the photo
  actually has room. Vary it slide to slide so the carousel doesn't
  feel like a repeated template. This is where the "scroll-stopping"
  energy comes from — not from the font.
- **Always sit text on a soft scrim**, gradient not solid block, per
  the brand doc's "don't place type on a busy photo without a scrim."
  The photo should still read through.
- **Color:** Classroom Cyan is fine for the hook line since it's large
  display text (18pt+ passes contrast). Any smaller supporting line
  uses Cyan Deep or Paper White with a text shadow — never small
  Classroom Cyan text.
- **Skip generic doodles** (hearts, sparkles, scroll banners) — those
  belong to the reference account's identity, not TMC's. If a slide
  wants a small graphic accent, reuse TMC's actual icon language: a
  single 1.5px-stroke line icon, or a short hand-drawn underline
  echoing the logo's own imperfect line quality.
- **Cover slide carries the boldest placement** — large Staatliches
  hook, off-center. Body slides keep captions shorter and quieter so
  the carousel has rhythm instead of every slide shouting equally.

Don't feed the reference screenshots into open-carrusel's own
"reference image" style-matching feature — that would pull in the
handwritten font and doodles directly. Point Claude Code at this
section instead.

## Approval gate (from the brand doc — worth keeping as a final check)

Before anything ships: does it follow this brand doc (color/type/logo), does it read aloud like a class teacher talking to a parent, and could a parent understand it on a phone in poor light in five seconds? If not, simplify.
