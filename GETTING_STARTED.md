# TMC Content Engine — Getting Started (Carousel Pipeline)

Consolidated setup guide. Covers install through your first published
carousel. Video/reel pipeline (HyperFrames) comes after this is
running smoothly.

## Phase 0 — Prerequisites
- Node.js 20+ and git installed
- Claude Code set up in your local project (same one `video-analysis` lives in)

## Phase 1 — Install open-carrusel
```
git clone https://github.com/Hainrixz/open-carrusel
cd open-carrusel
npm run setup      # downloads Puppeteer's Chromium (~300MB), first run only
npm audit fix      # patches known dependency vulnerabilities
npm run dev
```
Runs at `http://localhost:3000` — keep it running in a terminal tab whenever building carousels.

## Phase 2 — Brand Setup wizard
Enter, from `brand-brief.md`:
- Colors: `#1AAFE0` Classroom Cyan, `#0E7FA6` Cyan Deep, `#3F3F3F` Modern Charcoal, `#0E0E0E` Anchor Black, `#F2F4F6` Mist Grey, `#FFFFFF` Paper White
- Fonts: Staatliches (display), DM Sans (body)
- Logos: `TMC_Logo_Primary_CRM.png`, `TMC_Logo_Dark_Mode_CRM.png`
- Tagline: `TRAVEL. EXPERIENCE. LEARN.`

## Phase 3 — Install skill files
```
your-project/
  skills/
    video-analysis/
    tmc-carousel-pipeline/
      SKILL.md
  brand-brief.md
  logos/
    TMC_Logo_Primary_CRM.png
    TMC_Logo_Dark_Mode_CRM.png
```
Delete any earlier `carousel-generator` skill folder — it conflicts with this pipeline.

## Phase 4 — Set up a trip's folders
```
uploads/<Trip Name>/Post 1/
uploads/<Trip Name>/Post 2/
output/<Trip Name>/            <- fills in as posts render
```

## Phase 5 — Hand-pick photos (manual step)
Copy your best ≤10 shots per post into each `uploads/<Trip Name>/Post N/`. Selection always happens by hand before the pipeline runs. Double-check student-face consent while picking.

## Phase 6 — Run the pipeline
With open-carrusel running, tell Claude Code to run the carousel pipeline on the trip folder. It works through each `Post N`: view photos → check against brand rules → draft `story.json` → build slides in open-carrusel → export into the matching output folder.

## Phase 7 — Review and publish
Open `output/<Trip Name>/Post N/story.json` for the hook line and captions, check the rendered PNGs, then post manually. Repeat per post.

## Reference files from this project
- `brand-brief.md` — colors, fonts, logo rules, photo-selection rules, caption voice, overlay style
- `tmc-carousel-pipeline/SKILL.md` — the per-post workflow Claude Code follows
- `TMC_Logo_Primary_CRM.png` / `TMC_Logo_Dark_Mode_CRM.png` — brand logos

## What's next
Once carousels are running smoothly, move to the video/reel pipeline (HyperFrames) using the same trip/post folder convention.
