# Pilot review

Result: PASS in AI self-QA. Status: awaiting human review.

Reviewed copy v001 and render v001-preview-02 on 27 September 2026.

- Strategy: one principal audience, school planning needs and educational purpose.
- Structure: six slides, one task per slide, three explicit planning questions.
- Differentiation: school-specific considerations including reflection, walking, rest, family information and uncertain arrangements. No invented TMC proof is added to force differentiation.
- Evidence: general advice only, no claims about TMC results.
- CTA: none. Final advice completes the topic rather than requesting engagement.
- Permissions: no student media, supplied TMC logo only.
- Style: no prohibited vocabulary or punctuation. Arial Black and Arial use the documented offline fallback.
- Visual QA: all six PDF pages rendered and inspected. Portrait and square layouts checked. No clipping or footer collisions observed. Logo enlarged after first layout review, without redrawing or cropping.
- Technical QA: five automated tests passed, checking file dimensions, page count, hashes, overwrite refusal, approval reset, overflow rejection, unsupported media, style rejection and SVG XML escaping.

Limitations: this is not independent editorial approval. The renderer has not been executed in either external desktop account. SVG layouts require compatible fonts and an SVG-capable editor. The PDF contains rasterized slide images. No publishing connection exists. The primary Google Fonts are not bundled.

Next decision: human review of the current copy and visual preview, with any changes recorded as a new copy or render version.

## Render revision — v001-preview-03 (27 September 2026)

Same copy (`carousel-v001.json`, unchanged). The renderer previously laid out each slide's text top-down from a fixed y-coordinate and stopped wherever the copy ended, leaving a visibly empty bottom half on every slide in v001-preview-02. `scripts/render_marketing_carousel.py` was changed to measure each slide's actual content height first, then center that block within the available space above the footer. Re-ran the 5 automated renderer tests after the change: all passed. Visually inspected all 6 portrait slides and one square slide in the new render: content is balanced top-to-bottom, no clipping or footer collisions, footer/logo/page-number position unchanged. AI self-QA remains PASS; human approval remains unrecorded and applies only to a specific named version, so v001-preview-03 still needs its own review even though the copy hasn't changed.
