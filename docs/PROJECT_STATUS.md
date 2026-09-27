# TMC project status

Checked 27 September 2026. Scope: TMC non-video desktop workflow.

## Current conclusion

The knowledge and instruction package is built. End-to-end automation is not complete. The web application has been costed but has not been implemented in this workspace.

## Verified evidence

- Release 0.1.0 exists at `dist/tmc-0.1.0-vn1i4jok` with shared context, formats, workflow, logos and skill ZIP.
- Vendor integrity, release validation and source-to-package consistency passed on this check.
- The user previously reported desktop setup complete. Independent behavioral test results from ChatGPT and Claude are not recorded. The release manifest still records NOT_RUN for both.
- One saved LinkedIn pilot exists at `jobs/TMC-20260921-LI-001`. Its AI self-QA passed. It remains awaiting human review and has not been published.
- The earlier Brussels carousel export (`output/Europe Batch 3/Post 1`, made by the external open-carrusel tool) was lost on 27 September 2026: a backup `mv` into a sibling folder emptied the destination instead of transferring the files, apparently a OneDrive Files-on-Demand interaction with a raw filesystem rename. The user confirmed treating it as deleted rather than pursuing recovery. The source trip photos in `uploads/Europe Batch 3/Post 1` were unaffected and remain intact. The post was rebuilt from the same story content and photos using the new photo-overlay renderer (see item 3).
- The costing proposal is a planning artifact, not evidence of a deployed application or connected accounts.

## Remaining work in delivery order

1. Run and record the nine scenarios in `system/SMOKE_TESTS.md` in both target apps. Include one cross-app job handoff. Keep installation reported by the user distinct from observed behavior. Partial evidence: all nine scenarios were run and passed in a single Claude Code session on 27 September 2026 (see `docs/SMOKE_TEST_RESULTS_20260927.md`), including a real resume test against `TMC-20260921-LI-001` and a real fresh renderer run with inspected output. This verifies the instruction layer's behavior but is not the two-app acceptance run this item requires — ChatGPT Desktop and Claude Desktop remain untested.
2. The text-only marketing carousel renderer was retired on 27 September 2026 at the user's request, in favor of the photo-overlay renderer (item 3). Its code, tests and doc (`render_marketing_carousel.py`, `test_marketing_renderer.py`, `CAROUSEL_RENDERER.md`) were deleted. The `TMC-20260927-CAR-001` pilot's existing job files and rendered previews (`v001`, `v001-preview-02`, `v001-preview-03`) are left in place as historical record, but that content has no photos of its own and currently has no renderer in this repo that can re-render or extend it.
3. Photo-overlay carousel renderer built and locally tested on 27 September 2026 (`scripts/render_photo_carousel.py`, see `docs/PHOTO_CAROUSEL_RENDERER.md`): applies the brand's bold-overlay-on-photo style (Staatliches-fallback hook/caption, a dark top-and-bottom vignette for legibility, dynamic calm-quadrant text placement, logo, page counter, swipe arrow) to a folder of supplied photos, caps on-photo title/caption text at 10 words, and mechanically refuses to render unless `consent_status` is `APPROVED` or `NOT_APPLICABLE` — `UNKNOWN`/`DENIED` produce no files. `output/Europe Batch 3/Post 1` was fully deleted and re-rendered (version v003) after the vignette/word-cap changes, reusing the same `uploads/Europe Batch 3/Post 1` photos and story content as the lost original export. That rebuild's `consent_status: APPROVED` was carried forward from the fact this exact content was already published from this workspace before — it is not a freshly verified permission record for this specific render, and the rebuilt post itself is unreviewed and unapproved (status REVIEW). Still needed: human visual review of this rebuild, and a genuinely new tour job run through this renderer with its own recorded source metadata and permission evidence, not carried forward from prior content.
4. Facebook adaptation (`jobs/TMC-20260927-FB-001`) and blog article (`jobs/TMC-20260927-BLOG-001`) drafted and self-QA'd on 27 September 2026, both REVIEW / unapproved. Founder (Yasin) LinkedIn still has no real drafted example — the only demonstrated behavior is the correct refusal to invent a founder anecdote without real notes. A case study (`jobs/TMC-20260927-CASE-001`) cannot be drafted for real: no verified school outcome, permission or quote exists anywhere in this workspace, and `skills/tmc-case-study/SKILL.md` explicitly forbids inventing one. What exists instead is a complete structural template with every factual field marked as a required input — correct behavior per the skill, not a finished asset. Website copy remains not started.
5. The School Trip Assurance Checklist's 5-email nurture sequence is drafted and self-QA'd (`jobs/TMC-20260927-NEWS-001`), REVIEW / unapproved, with explicit placeholders for the download URL, sender identity, booking link and enrolment trigger. The checklist itself, its landing-page copy, form requirements and thank-you copy remain unbuilt. Deployment and sending remain separate acceptance steps.
6. Establish the shared calendar/tracker and authoritative job storage. Test revision, rejection, approval and handoff behavior. Desktop copies do not synchronize themselves.
7. Demonstrate monthly analysis using supplied historical data or clearly labelled sample data, then revise the next calendar.
8. Complete operating instructions and team handover after pilots pass.

## Separate automation expansion

API generation, automatic intake, persistent background jobs, scheduling, publishing, email delivery and analytics collection require implementation and account connections beyond the original manual desktop handoffs. No such working connections were verified in this workspace.

The proposed web app also requires login/roles, database/media storage, content editor, review screens, renderer integration, deployment and acceptance testing. Its development has not started here.

## Immediate next build

The photo-overlay carousel renderer is complete as a local preview workflow. See `docs/PHOTO_CAROUSEL_RENDERER.md` for operation. Next work is human visual review of the rebuilt Europe Batch 3 Post 1 carousel, cross-app acceptance, and a real tour job with genuinely recorded permission evidence (not the carried-forward assumption used for the rebuild). Human review of the existing LinkedIn draft remains pending.
