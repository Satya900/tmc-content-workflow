---
name: tmc-carousel-pipeline
description: Render hand-picked TMC trip photos through an existing open-carrusel installation when that renderer is explicitly requested or confirmed available. For ordinary desktop tour content, use the TMC tour photo workflow first. Does not publish.
---

# TMC Carousel Pipeline

## Folder convention

```
uploads/<Trip Name>/Post 1/   <- hand-picked photos for one carousel (max 10)
uploads/<Trip Name>/Post 2/
uploads/<Trip Name>/Post 3/
...

output/<Trip Name>/Post 1/    <- mirrors the input path exactly
output/<Trip Name>/Post 2/
...
```

Each `Post N` folder under a trip is one carousel's worth of
already-selected photos. Photo selection happens by hand, before this
skill runs — never auto-pick which photos belong in a post. Open-
carrusel's slide limit is 10, so a `Post N` folder shouldn't exceed
that.

## Finding the work queue

Rendered slides indicate an existing export, not human approval or publication. Use the job record described in `system/WORKFLOW.md` when this adapter is part of the desktop system. An older export without a review record has approval status UNKNOWN. Preserve existing output and do not re-render it unless the user requests a redo. Pending folders have no matching rendered output; check their job state before processing.

## Per-post workflow

Run this for every pending `Post N` folder, one at a time:

### 1. Look at the photos
View every image in `uploads/<Trip Name>/Post N/` directly with
native vision — never infer content from filenames.

### 2. Check against brand rules
Cross-check against the photo-selection section of `brand-brief.md`
(students reacting not posing, a teacher visible, no stiff lineup as
the hero shot). If something looks off — especially the consent flag
for student faces — say so before continuing. Don't render past a
flagged concern.

### 3. Draft the story
Write one hook line for the cover slide and a short caption for any
other slide that needs one, following the caption-voice rules in
`brand-brief.md` (specific, warm, honest; no banned buzzwords, no em
dashes, no exclamation points). Also draft the post caption — the
text that goes *below* the carousel on Instagram/LinkedIn, separate
from the on-image text. Save all of it as
`output/<Trip Name>/Post N/story.json`:

```json
{
  "title": "hook line for the cover slide",
  "slides": [
    {"file": "078A1234.jpg", "caption": "..."},
    {"file": "078A1235.jpg", "caption": ""}
  ],
  "post_caption": "the text for below the carousel, not on the images"
}
```

### 4. Build the carousel in open-carrusel
Upload this post's photos, then chat-drive slide generation using the
overlay rules in `brand-brief.md` — Staatliches hook line, DM Sans
supporting text, dynamic off-center placement (varied per slide, not
always centered), soft scrim for legibility, TMC colors and contrast
rules.

### 5. Export and file it
Export at both sizes and save into `output/<Trip Name>/Post N/`:

```
output/<Trip Name>/Post N/
  instagram_4x5/01.png … NN.png
  square_1x1/01.png … NN.png
  story.json
```

### 6. Hand back for review
Tell the user the post is ready — restate the hook line and post
caption, not just "done" — and point at the output folder. This
skill's job ends here. A human reviews and posts manually; no
auto-publish step.

## Notes

- This replaces the earlier `carousel-generator` skill and its custom
  Python renderer — open-carrusel does the actual rendering now.
  Treat older renderer instructions as historical; do not delete skill folders as part of a content job.
- Post numbering resets per trip and just mirrors whatever folder
  name already exists on disk — never renumber or reinterpret it.
- Read `brand-brief.md` fresh each run rather than relying on memory
  of it from earlier in a session — it's the single source of truth
  for colors, fonts, voice, and overlay placement.
