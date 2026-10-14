# TMC Content Workflow

The content engine for **The Modern Classroom (TMC)**, an educational school-travel operator. This repo holds the instructions, brand rules, job records and a few local tools that let Claude (and ChatGPT) plan, draft, review and render TMC's non-video marketing and tour content in a consistent way.

Most of the repo is Markdown that an AI assistant reads, not application code. The Python scripts build a distributable instruction pack and render branded photo carousels offline.

> **Status:** Release `0.1.0`. The instruction pack is built. Behaviour has been checked in a single Claude Code session but not yet in both target desktop apps (ChatGPT Desktop and Claude Desktop). Nothing in this repo publishes, schedules or sends content. See [`docs/PROJECT_STATUS.md`](docs/PROJECT_STATUS.md).

## What it covers

| Format | Skill |
|---|---|
| Content planning, calendars, campaign themes | `tmc-content-strategist` |
| Marketing carousels (positioning, lead gen) | `tmc-marketing-carousel` |
| Tour photo dumps (real trip documentation) | `tmc-tour-photo-dump` |
| Photo selection, ranking and sequencing | `tmc-photo-selector` |
| LinkedIn (company page and founder, Yasin) | `tmc-linkedin` |
| Blogs and SEO articles | `tmc-blog` |
| Newsletters and nurture emails | `tmc-newsletter` |
| Case studies | `tmc-case-study` |
| Reels (deferred in release 0.1) | `tmc-reel` |
| Pre-publication review and QA | `tmc-editorial-qa` |
| Monthly performance review and planning | `tmc-monthly-strategist` |
| Rendering via open-carrusel (optional, legacy) | `tmc-carousel-pipeline` |

Every job loads `tmc-core-context` first. It holds the brand context, content taxonomy, Marketing Template mapping and a claims-register template.

## Core rules

- **Every job is TOUR or MARKETING.** In TOUR content the photos tell the real trip story. In MARKETING content a school audience's problem drives the argument.
- **Never invent facts.** That covers claims, student outcomes, safety records, prices, testimonials, founder anecdotes, links and media permissions. If evidence is missing, the affected claim is blocked. Unrelated work can still go ahead.
- **Consent is explicit.** Media permission is `APPROVED`, `DENIED`, `UNKNOWN` or `NOT_APPLICABLE`. `UNKNOWN` never counts as approved, and having a photo file is not consent.
- **AI QA and human approval are separate.** QA returns `PASS`, `REVISE` or `BLOCK`. Approval needs a human decision tied to a specific version. Changing an approved version sends it back to review.
- **States:** `INTAKE → DRAFT → REVIEW → APPROVED → EXPORTED → PUBLISHED`, plus `NEEDS_INPUT`, `CHANGES_REQUESTED` and `RENDERING_PENDING`.

The full rules are in [`system/WORKFLOW.md`](system/WORKFLOW.md) and [`system/PROJECT_INSTRUCTIONS.md`](system/PROJECT_INSTRUCTIONS.md).

## Repository layout

```
brand-brief.md          Colours, fonts, logo rules, photo selection, caption voice, export sizes
START_HERE.md           Short orientation note
GETTING_STARTED.md      Older open-carrusel carousel route (optional renderer)
THIRD_PARTY_NOTICES.md  Attribution for adapted upstream skills

system/                 Source for the packaged desktop workflow
  PROJECT_INSTRUCTIONS.md, WORKFLOW.md, FORMAT_EXTENSIONS.md,
  SKILL.md, SMOKE_TESTS.md, job-template.md

skills/                 Canonical TMC skills (one SKILL.md each)
  tmc-core-context/references/   Brand context, taxonomy, template framework, claims register
  _examples/                     Sample brief and tour context
  TEST_PROMPTS.md                Prompts for exercising the skills

jobs/<content-id>/      Portable job records: job.md, sources.md, draft-vNNN.md, review-vNNN.md
uploads/<Trip>/Post N/  Hand-picked source trip photos
output/                 Rendered carousels, previews and PDFs
logos/                  TMC primary and dark-mode logos
scripts/                Build, render and test scripts, plus the shared font locator (below)
vendor/                 Pinned upstream skill snapshots and licences (not auto-activated)
dist/                   Generated releases (project files + native skill ZIP)
docs/                   Setup, renderer guide, skill research, status, smoke-test results
tmp/                    Rendered QA page images
```

Job IDs look like `TMC-YYYYMMDD-<FORMAT>-NNN`, where the format is `LI`, `FB`, `CAR`, `BLOG`, `NEWS` or `CASE`.

## Using the workflow in a desktop app

The full guide is [`docs/DESKTOP_SETUP.md`](docs/DESKTOP_SETUP.md). In short:

1. **Project-file route (ChatGPT or Claude).** Create a project. Paste `PROJECT_INSTRUCTIONS.md` into its instructions, then add `TMC_CONTEXT.md`, `TMC_FORMATS.md` and `TMC_WORKFLOW.md` from `dist/<release>/project-files/` as knowledge.
2. **Claude native skill route.** Go to Customize → Skills → Upload a skill and upload `dist/<release>/tmc-content-workflow.zip`.
3. Run the acceptance prompts in [`system/SMOKE_TESTS.md`](system/SMOKE_TESTS.md) and write down the results.

To move a job between apps, take its latest `job.md`, sources, draft and review files with it. Copies in different apps do not sync.

## Scripts

All scripts are Python 3.9 or newer and resolve paths relative to the repo root. One-time setup:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

The renderer and the cost proposal use Arial and Arial Black as offline fallbacks for DM Sans and Staatliches. `scripts/tmc_fonts.py` finds them in the standard Windows, macOS and Linux font folders. On Linux, install them first (for example `ttf-mscorefonts-installer` on Debian or Ubuntu).

### Build the desktop pack

```bash
python scripts/build_desktop_pack.py [--output-dir dist]
```

Uses only the standard library and makes no network calls. It compiles `system/`, `skills/` and `brand-brief.md` into a new `dist/tmc-<version>-<suffix>/` release containing project files, a native skill ZIP and a `manifest.json` with SHA-256 hashes. Before building, it checks vendor files against `vendor/sources.lock.json`, and afterwards it validates the release. Older releases are kept.

### Render a photo carousel

```bash
python scripts/render_photo_carousel.py story.json \
  --photos-dir "uploads/<Trip>/Post N" \
  --output "output/<job>/<version>" \
  [--fonts-dir <folder with Arial and Arial Black>]
```

Needs Pillow, reportlab and numpy. Works offline. It puts brand-styled hook and caption text over trip photos, with a vignette, logo, page counter and swipe indicator. Text is capped at 10 words per slide. Outputs:

- `instagram_4x5/` (1080×1350) and `square_1x1/` (1080×1080) PNGs
- a PDF, a contact sheet, `caption.txt`, `alt-text.md` and `story.json`
- `manifest.json` with file hashes, `status: REVIEW` and `human_approval: null`

Rendering stops before any file is written if `consent_status` is anything other than `APPROVED` or `NOT_APPLICABLE`, or if the copy contains banned words or punctuation from the brand brief. It also refuses to overwrite an existing output folder. Fonts are found automatically. Pass `--fonts-dir` only if they're installed somewhere non-standard. See [`docs/PHOTO_CAROUSEL_RENDERER.md`](docs/PHOTO_CAROUSEL_RENDERER.md) for the input schema.

### Test the renderer

```bash
python scripts/test_photo_carousel_renderer.py
```

Also needs `pypdf`. Covers the export contract, the consent gate (`UNKNOWN` and `DENIED`), missing photos, banned-copy rejection and the 10-word cap. It reads photos from `uploads/Europe Batch 3/Post 1`.

### Other scripts

- `scripts/fetch_vendor_notices.py` fetches licences and notices for the pinned upstream skills from GitHub and rewrites `vendor/sources.lock.json`. This is the only script that uses the network, and it never runs vendor code.
- `scripts/build_costing_proposal.py` generates the TMC Content Platform cost proposal PDF in `output/pdf/`. Needs reportlab and pypdfium2. Running it overwrites the existing proposal PDF and its QA images in `tmp/pdfs/costing/`.

## Brand essentials

From [`brand-brief.md`](brand-brief.md):

- **Colours:** Classroom Cyan `#1AAFE0` (large text only), Cyan Deep `#0E7FA6`, Modern Charcoal `#3F3F3F`, Anchor Black `#0E0E0E`, Mist Grey `#F2F4F6`, Paper White `#FFFFFF`. Aim for roughly 70% white, 20% neutrals and 10% cyan.
- **Fonts:** Staatliches for display (all caps, 18pt and up). DM Sans for everything else.
- **Tagline:** `TRAVEL. EXPERIENCE. LEARN.`, always in that order and never reworded.
- **Voice:** direct, specific and warm. No em dashes, semicolons, exclamation marks or hype words such as "unlock" or "remarkable".

## Third-party content

`vendor/` holds pinned snapshots of selected skills from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT) and [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) (Apache-2.0). Adapted methods live in `system/FORMAT_EXTENSIONS.md`. See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and [`docs/SKILL_RESEARCH.md`](docs/SKILL_RESEARCH.md).

## Out of scope for release 0.1

Video and reels production, Ready for Umrah content, automatic publishing, scheduling, email sending, analytics collection, and the proposed TMC Content Platform web app (costed, not built).
