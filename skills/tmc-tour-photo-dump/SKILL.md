---
name: tmc-tour-photo-dump
description: Use this skill whenever the user asks to create, generate, process, caption, sequence, or review a TMC tour photo dump from a real school trip folder, destination folder, post-number folder, or batch of tour photos. This is for experience-led trip documentation, not strategic marketing carousels.
---

# TMC Tour Photo Dump

## Purpose
Turn real TMC trip photos into a branded, human, candid tour carousel.

## Input convention
Accept the existing `uploads/<Trip Name>/Post N/` pattern or `school/destination/post_no/`. Preserve the user's hierarchy. Read school and destination from supplied context; folder labels alone do not establish school naming permission.

The post folder contains source photos and may optionally contain context metadata.

## Output convention
Mirror the same hierarchy under output:
`school/destination/post_no/`

Recommended outputs:
- `images/01.jpg ...`
- final PDF
- caption text
- generation metadata

## Workflow
1. Read folder path for school, destination and post number.
2. Read context file if present.
3. Inspect available photos.
4. Flag unusable or duplicate images for exclusion from the proposed sequence. Preserve source files and respect an explicitly hand-picked set.
5. Check media/consent status. Missing metadata means PERMISSION UNKNOWN, not approval. Pause use of affected media and request the missing information.
6. Build a visual sequence.
7. Write short tour-context copy.
8. Render in TMC visual template.
9. Export images + PDF.
10. Prepare caption and metadata.
11. Send for human approval.

## Copy style
Allowed:
- candid
- playful
- location/context-led
- human
- light
- memorable

Do not force an educational or sales claim onto every photo.

## Hard rule
Never infer or publish school/student identity, permissions, activity details, location facts or trip facts that are not supported by folder context or approved metadata.

## Desktop production
Use `system/WORKFLOW.md` (or bundled TMC_WORKFLOW.md) for output contracts, versions and approval. Use an available renderer only after checking its capabilities. `tmc-carousel-pipeline` is an optional adapter for an existing open-carrusel installation, not a required desktop service. If rendering is unavailable, return copy and a design brief with RENDERING_PENDING. Existing rendered files do not establish human approval or publication.
