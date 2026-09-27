# TMC Content Engine

Current focus: non-video content in ChatGPT Desktop and Claude Desktop.

The working foundation is now in system/. Read docs/DESKTOP_SETUP.md for installation and docs/SKILL_RESEARCH.md for the selected online skills and source decisions. Generated releases are under dist/. Each includes matching project knowledge files and a Claude-compatible native skill ZIP.

The existing skills/ folder remains the canonical source of TMC format guidance. vendor/ holds four pinned upstream skill snapshots with their licenses; these are not automatically activated. scripts/build_desktop_pack.py compiles the shared release without network access or AI API keys.

The user has reported installation complete. Next acceptance step: run the LinkedIn pilot plus system/SMOKE_TESTS.md in both apps and record the results. The text-only marketing carousel renderer has been retired; the current carousel tool is the photo-overlay renderer at scripts/render_photo_carousel.py, which composites brand-styled hook/caption text onto supplied trip photos. See docs/PHOTO_CAROUSEL_RENDERER.md for commands and docs/PROJECT_STATUS.md for the remaining work. Cross-app execution is not yet validated.

GETTING_STARTED.md documents the older open-carrusel route. It remains useful for that optional renderer, but the current desktop workflow is defined by system/WORKFLOW.md. Existing uploads and exports are preserved.
