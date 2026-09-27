# Photo carousel renderer

This local renderer applies the brand's "Overlay style for photo carousels"
(see `brand-brief.md`) to a folder of already-selected trip photos: bold
Staatliches-style hook and caption text over the photo, a dark top-and-bottom
vignette for guaranteed legibility regardless of the photo's own brightness,
TMC logo, page counter and swipe indicator. On-photo title/caption text is
capped at 10 words per slide. It does not select photos, generate copy,
verify consent, approve claims or publish. It needs Python with Pillow,
reportlab and numpy, plus the approved Arial Black and Arial offline
fallback fonts. No network or paid API is used.

This is now the only carousel renderer in the repo: the earlier plain
typographic text-only renderer (`render_marketing_carousel.py`) was
retired on 27 September 2026 in favor of this one. Use this renderer for
photo-led TOUR posts and any MARKETING carousel that has its own approved
photos; a MARKETING carousel with no photo of its own still needs a
non-photo treatment, which is not currently covered by any renderer in
this repo.

## Consent gate

Every input file must declare `consent_status`: `APPROVED`, `DENIED`,
`UNKNOWN` or `NOT_APPLICABLE`. Rendering is refused — no files are
written — unless it is `APPROVED` (identifiable people, permission on
file for this specific use) or `NOT_APPLICABLE` (no identifiable people
in any slide). Presence of a photo file is never treated as consent;
`UNKNOWN` must not silently become `APPROVED`. This mirrors the rule in
`skills/tmc-photo-selector/SKILL.md` and `system/WORKFLOW.md`, enforced
mechanically instead of relying on someone remembering to check.

## Run

```powershell
& 'C:\Users\mohan\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts/render_photo_carousel.py path/to/story.json --photos-dir path/to/photos --output output/<job>/<version>
```

## Input

JSON with `id`, `version`, `title`, `category` (`MARKETING` or `TOUR`),
`consent_status`, `post_caption`, and 2–12 `slides`. Each slide has
`file` (must exist in `--photos-dir`), and optionally `caption` and
`label` (e.g. a place name shown above the caption). A slide with an
empty caption renders as photo-only (page counter, logo, swipe arrow,
no text block) rather than forcing text onto every slide.

Each slide's calmer bottom-left-vs-bottom-right quadrant is chosen
automatically (lower edge-detail = calmer) to decide which side the text
aligns to; the cover slide (first entry) always anchors bottom-left with
the largest type, matching the brand doc's "cover slide carries the
boldest placement" rule. A full-width dark vignette always sits at the
top of every slide (for the page counter and logo) and, whenever a slide
has text, a stronger dark vignette sits at the bottom spanning roughly
40–50% of the slide's height, so caption legibility never depends on
how bright or busy that particular photo is.

## Output

Each run produces `instagram_4x5/` (1080×1350) and `square_1x1/`
(1080×1080) PNGs, a rasterized PDF (one slide per page), a contact
sheet, `caption.txt`, `alt-text.md`, `story.json` (exact input), and
`manifest.json` with file hashes, the declared consent status, and
`status: REVIEW` / `human_approval: null` — set unconditionally,
regardless of what the input claims.

## Validation

```powershell
& 'C:\Users\mohan\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' scripts/test_photo_carousel_renderer.py
```

Seven tests cover the export contract (dimensions, PDF page count, file
hashes, overwrite refusal), the consent gate for both `UNKNOWN` and
`DENIED`, a missing photo file, prohibited-copy rejection, and the
10-word overlay cap for both the title and a slide caption.

## Known gap

No face detection exists — "calm quadrant" placement is edge-energy
based, not face-aware, so a human reviewer should still check that text
never sits over a face before approving. The renderer also cannot judge
whether photo *content* matches the brand's selection rules (reacting
not posing, teacher visible, no stiff lineups) — that's `tmc-photo-selector`'s
job, done before this renderer ever runs.
