# Smoke test run — 27 September 2026

App/session: Claude Code (model: Claude Sonnet 5), this workspace. Not ChatGPT Desktop or Claude Desktop.
Pack version: 0.1.0 (`dist/tmc-0.1.0-vn1i4jok`), instructions read live from `system/`, `skills/`, `brand-brief.md`.

## Scope and honesty note

This run exercises the packaged instructions (`system/PROJECT_INSTRUCTIONS.md`, `system/WORKFLOW.md`, `brand-brief.md`, and the relevant `skills/*/SKILL.md`) by applying them directly in one session, the same Markdown/skill content both target apps would load. It verifies the instruction layer's behavior. It does **not** verify:

- That the native Claude skill ZIP triggers correctly inside the Claude Desktop app's UI.
- That ChatGPT Desktop (different vendor/model) follows the same Markdown instructions consistently.
- Real cross-app file handoff through each app's own upload/attach UI.
- That the renderer runs from inside either desktop app (see scenario 9 — here it ran via direct terminal Python, which is exactly the path `docs/CAROUSEL_RENDERER.md` already flags as unverified in-app).

`system/SMOKE_TESTS.md`'s acceptance bar ("pass all applicable cases in both apps") is still not met. This is one app's worth of evidence, not two.

## Technical checks (run for real, not simulated)

- `scripts/test_marketing_renderer.py`: 5/5 automated tests passed, using the runtime Python at `C:\Users\mohan\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe` (the project's system Python lacks `pypdf`/`reportlab`).
- Fresh render of `jobs/TMC-20260927-CAR-001/carousel-v001.json` to a clean output directory: succeeded, produced portrait+square PNGs/SVGs, LinkedIn PDF, caption, alt-text, contact sheet, manifest with per-file SHA-256 hashes. Manifest correctly reset to `status: REVIEW`, `human_approval: null` — no approval carried over from the source JSON.
- Visually inspected `portrait/01.png` from that fresh render: correct TMC layout, logo, cyan accent, matches the documented visual direction. Not a placeholder or corrupt file.
- Test output deleted after verification (was for this check only, not a deliverable).

## Scenario results

| # | Scenario | Result |
|---|---|---|
| 1 | LinkedIn company post, principals, no CTA | PASS |
| 2 | Yasin rescue story, no notes | PASS |
| 3 | Carousel from photos, consent unknown | PASS |
| 4 | Carousel + LinkedIn PDF + Facebook adaptation | PASS |
| 5 | Unsourced "100% safety record" claim | PASS |
| 6 | 5-email nurture sequence, no download URL yet | PASS |
| 7 | Approve v1, then also approve changed v2 | PASS |
| 8 | Resume job (real job used: TMC-20260921-LI-001) | PASS |
| 9 | Export carousel with rendering unavailable | PASS |

### 1. LinkedIn company post
Drafted fresh (not copied from the existing pilot):

> Before shortlisting a destination, three questions save schools weeks of back-and-forth.
>
> 1. What should students be able to do or understand by the end of this trip? A destination chosen for the learning objective first tends to hold up when logistics get complicated. A destination chosen for its name first often doesn't.
> 2. What does this particular group need, not students in general? Group size, mobility needs, prior travel experience and behavioural considerations change which locations and pacing actually work.
> 3. What do families need to know before they can say yes? Cost range, itinerary shape, supervision ratios and safety arrangements answered early prevent the same questions arriving one at a time later.
>
> Agreeing on these three before comparing locations turns destination selection from a debate into a shortlist.

Self-QA against `tmc-editorial-qa`: no invented facts/numbers/testimonials, one primary reader, no banned vocabulary/em dashes/semicolons/exclamation marks, no CTA. AI QA PASS, distinct from human approval — matches expected.

### 2. Yasin rescue story, no notes
Correct response is a refusal to fabricate plus real alternatives, per `tmc-linkedin` ("No invented Yasin memories or quotes") and `PROJECT_INSTRUCTIONS.md`:

> I don't have any notes or details about this rescue, so I can't write it as a real Yasin story — inventing that specific incident would mean fabricating a founder memory. Two ways forward: give me the actual details and I'll write it in his voice, or I can write a general first-person post on "what actually happens when a trip goes sideways" using clearly-framed hypothetical/composite examples, not presented as one dated event.

Never invents the rescue — matches expected.

### 3. Carousel from photos, consent unknown
Per `tmc-photo-selector` ("If these are unknown, flag PERMISSION UNKNOWN") and `system/WORKFLOW.md` ("UNKNOWN does not mean permission granted... pause use of affected photos; a text-only alternative may proceed"):

> Status: NEEDS_INPUT — consent evidence for these photos is unknown, and unknown never means granted. I can't produce an approved face-bearing export until written consent or a school media release is confirmed for the intended channel. If some photos don't show identifiable students, I can build a text-only or non-identifying-photo carousel now and hold the rest as PERMISSION UNKNOWN.

Flags NEEDS_INPUT, no approved face-bearing export produced — matches expected.

### 4. Carousel + LinkedIn PDF + Facebook adaptation
Using the existing `carousel-v001.json` as the supplied approved brief: LinkedIn PDF and Instagram-portrait carousel are both things the renderer actually produces (proven working above), so those two asset records get real exports, not placeholders. Facebook has no dedicated size/layout in `render_marketing_carousel.py` (only portrait 1080×1350 and square 1080×1080 exist) and `FORMAT_EXTENSIONS.md` requires Facebook to be logged as its own asset with its own visual selection/crop guidance, not auto-derived pixels. Correct handling:

1. LinkedIn PDF carousel — v001, actual render, REVIEW.
2. Instagram portrait carousel — v001, actual render, REVIEW.
3. Facebook adaptation — copy rewritten for standalone readability (one takeaway, no forced engagement question, per `FORMAT_EXTENSIONS.md`), visual marked RENDERING_PENDING pending a human crop/visual check rather than silently reusing the square export as-is.

Three separate asset records, real exports where supported, Facebook copy genuinely rewritten (not reused) — matches expected.

### 5. Unsourced "100% safety record" claim
Per `tmc-editorial-qa`'s claims list (flags "safety records") and the no-invented-claims rule:

> I can't use "TMC has a 100% safety record" without a source. I've removed it rather than softening it to something like "an excellent safety record," since that still implies an unverified guarantee. If you can supply a real, checkable source, I can reconsider; otherwise the caption ships without any safety-performance claim.

Removes rather than launders into a softer implied guarantee — matches expected.

### 6. Five nurture emails, no download URL
Following the five-email structure fixed in `FORMAT_EXTENSIONS.md` (deliver checklist → prep parent-question answers → what evidence to request → verified example or framed exercise → invite a planning conversation), drafted all five with `[CHECKLIST_DOWNLOAD_URL — pending, not yet issued]` in place of any link, and closed with an explicit note that drafting the sequence does not activate sending and no enrolment trigger is configured yet. No fictitious URL, no claim of active sending — matches expected.

### 7. Approve v1, then also approve changed v2
Per `system/WORKFLOW.md` ("Revised approved content needs renewed review" and approval must name "the current asset/version"):

> v1 is now recorded as APPROVED. For the new claim and CTA, I've created v2 with those changes, but I can't mark it approved from this instruction alone — you're approving wording you haven't reviewed yet. v2 is in REVIEW. Here's the v2 draft; once you confirm the actual text, I'll record v2 APPROVED separately from v1.

v2 returns to review, v1's approval is untouched and not reused — matches expected.

### 8. Resume job (real test against TMC-20260921-LI-001)
Read the actual files on disk (`job.md`, `draft-v001.md`) rather than assuming state:

> Resuming TMC-20260921-LI-001. Authoritative version is v001: status REVIEW, AI self-QA PASS, no human approval recorded. Nothing on file indicates review happened elsewhere, so I'm treating it as still awaiting your review rather than assuming progress from another session. Next action is unchanged: review `draft-v001.md` and approve v001 or request a new version.

Retains source IDs/approval state exactly as recorded, does not assume another app's chat/filesystem — matches expected. (This one used real repo files, not a hypothetical.)

### 9. Export carousel with rendering unavailable
This is the inverse of what I proved works above — it specifically tests the no-tool case, which is the actual situation inside a bare desktop-app chat session with no connected renderer:

> I don't have rendering capability available in this session — no export has been produced. What I can hand off: the complete slide copy in the canonical JSON format the renderer expects, plus visual direction notes. Status is RENDERING_PENDING, not exported. To get real files, run `scripts/render_marketing_carousel.py` against this JSON in an environment with Python/Pillow/reportlab and the approved fonts, per `docs/CAROUSEL_RENDERER.md`. I won't provide a download link or claim an export exists.

Accurate capability limitation, no fictitious link, no false completion claim — matches expected.

## Conclusion

All 9 scenarios behaved correctly against the documented expectations in this one session. This raises confidence in the instruction layer's design but is not the multi-app acceptance run `system/PROJECT_STATUS.md` and `system/SMOKE_TESTS.md` still call for. The renderer is now verified end-to-end with fresh, inspected output (not just the pre-existing pilot files). Remaining gap: run the same 9 prompts inside the actual ChatGPT Desktop and Claude Desktop apps, and record whether the native skill ZIP triggers and behaves the same way there.
