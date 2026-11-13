# TMC workflow, release 0.2

## Scope and authority

This release supplies the instruction and handoff layer for TMC content: LinkedIn, Instagram, Facebook, WhatsApp and other social posts, carousels, tour photo posts, blogs, newsletters and sequences, lead magnets, case studies, website copy, calendars and monthly reviews. Video scripts may be drafted as text. Filming, editing and rendering video remain out of scope. This release does not install renderers, connect accounts, send email or publish content. Use the user's requested formats; repurposing into every format is optional.

Business positioning, audience and content buckets come from TMC core context, which follows the TMC content marketing approval brief (v1, 15 October 2026). Visual identity and caption restrictions come from brand-brief.md. Where that brief makes numerical contrast claims, use the measured contrast clarification included in TMC_CONTEXT.md. Format rules sit below these shared rules. External skill examples are not verified TMC facts.

## Start and resume

For a new job, gather only the information needed for the next useful action: source or topic, TOUR/MARKETING, audience, requested formats and any required claim or media permissions. For MARKETING, record the 4D fields: audience (Determine), one primary content bucket from 1 to 7 (Define), one need or emotion (Decode) and one content angle (Develop). Assign the bucket yourself when the brief makes it clear and label it as an assumption. Infer ordinary format choices and label assumptions. Do not interrogate the user about every taxonomy field.

For a resumed job, read its latest job.md, draft version, sources and review notes. Identify the authoritative version. If two apps edited the same version, show the differences and resolve the conflict before recording a new approved version. Never combine approval from one version with content from another.

Check capabilities only as needed: supplied knowledge readable, images viewable, file creation available, renderer available, network/source verification available. Missing tools change the deliverable status, not the facts. Local disk paths supplied in chat do not themselves grant access in another app.

## Evidence and permissions

Keep source IDs with facts and exact quotes. Distinguish internal TMC claims from external research. For time-sensitive research record URL, publisher and checked date. A claims template is not an approved claims register. Missing statistics may be omitted; an invented replacement is never acceptable.

For identifiable trip media record applicable student, parent, school and staff permissions, permitted channels, marketing-use scope, expiry/revocation when known, and anonymisation needs. Each category can be APPROVED, DENIED, UNKNOWN or NOT_APPLICABLE with a reason. UNKNOWN does not mean permission granted. Pause use of affected photos; a text-only alternative may proceed. Do not identify students or infer consent from file presence. Preserve original files.

## Job files

Suggested working location: jobs/<content-id>/. Keep existing uploads/<Trip>/Post N and output/<Trip>/Post N paths for legacy tour batches. Either trip hierarchy is acceptable; use provided metadata for school and location, not guessed identities.

Minimum handoff: job.md, sources.md, draft-v001.md and review-v001.md. Add exports and editable source files when created. A single job can contain several platform assets; each has its own version, QA and approval fields. Source/reference files are shared, approval is not.

## State and approval

Normal progression: INTAKE -> DRAFT -> REVIEW -> APPROVED -> EXPORTED -> PUBLISHED.

- NEEDS_INPUT: record the exact missing requirement and affected asset.
- CHANGES_REQUESTED: revise to a new version and return it to REVIEW.
- RENDERING_PENDING: copy exists but visual export is not complete.
- QA result is PASS, REVISE or BLOCK. It never records human approval.
- APPROVED requires an explicit human decision naming or unambiguously referring to the current asset/version. Store decision text, date and reviewer if known. Never invent a reviewer name.
- A preview export may exist before approval. Files existing on disk do not establish approval, publication or completion.
- EXPORTED means the approved version's required final files exist and have been checked.
- PUBLISHED requires a live URL or an explicit user report. Label user-reported publication if not independently checked.

The assistant can finish a draft and self-QA in one turn. Human review is necessary before publication. Do not ask repeatedly for the same already-provided permission.

## Output contracts

Text social: editable copy, platform/account, optional CTA, source/claim notes, QA and status. Include visual suggestion or alt text only for an actual supplied/created visual.

Carousel: slide order, one job per slide, on-slide copy, visual requirements, caption, alt text tied to final visuals, PNG exports for requested social sizes, PDF for document posts, and editable design source. Default Instagram size is TMC's 1080 x 1350. Square adaptation is 1080 x 1080 when requested. Reflow and inspect rather than stretch. A JSON story file is editable copy metadata, not automatically an editable visual design.

Blog: article, title, proposed slug, metadata, verified sources, link suggestions clearly distinguished from live links, optional FAQs and editable copy.

Newsletter: subject options, preview text, body, CTA and destination, editable copy and HTML when requested and supported. Use explicit placeholders for sender details and unsubscribe handling until configured. Never claim email-client testing from a browser preview alone.

Social post: channel, visual brief, caption, alt text for the final visual, optional CTA, claim notes, QA and status.

Lead magnet: the resource content, landing page and form copy, thank-you and delivery email, promotion plan, and open implementation requirements.

Video script: spoken script with timings, on-screen text, shot list, caption and CTA. Status after approval is RENDERING_PENDING.

Calendar: rows in the calendar format, with the inputs each row depends on.

Website asset: page copy, headings, CTA/form requirements, metadata and implementation handoff. Generating copy is not deploying a page or activating a form.

## Repurposing and tracking

Keep one source ID and master idea across adaptations. Rewrite hooks, density and account voice for each platform. Do not invent an anecdote to personalise Yasin's version.

Calendars use the columns in measurement-and-calendar.md (posting date, platform, content bucket, needs and emotions, delivery type, topic, status, caption, plus content ID and links). Spread a month across all seven buckets unless the user directs otherwise.

The scope's non-video monthly capacity is 25 placements: 8 personal LinkedIn, 4 company LinkedIn, 4 Instagram, 4 Facebook, 2 email, 2 blog and 1 website asset. PDF carousels occupy an appropriate channel slot, not an extra automatic quota. The five-email checklist nurture sequence is a foundation asset, separate from recurring campaigns. These are planning capacities, not a required output for every request. The Understanding TMC guide sets a larger ideal schedule (see measurement-and-calendar.md). Plan to the contracted capacity unless the user records a change.

Airtable updates remain manual or explicitly connected. Provide a copyable tracker row if disconnected. Monthly analysis uses supplied data and states the reporting window and metric definitions; missing data is unknown, not zero. Recommend Continue, Improve, Test, Reduce or Stop and retain the reasoning for next month's calendar.

## Compatibility and completion

The portable baseline is project instructions plus three Markdown knowledge files and the source files for the current job. Native skills are an optional installation route. Generated packages are snapshots: rebuild and replace both apps' copies after editing the canonical files.

The assistant should report exactly what was completed: content draft, QA, rendered preview, approved export or publication. Release 0.2 is structurally validated locally. Live workflow checks in both target accounts and renderer pilots remain separate acceptance work.


---

Source: system/job-template.md

# TMC content job

- Content ID:
- Master idea ID:
- Source IDs/files:
- Category: TOUR / MARKETING
- Audience (one primary) and school segment if targeted:
- Content bucket (one primary, 1 to 7):
- Need or emotion (Fear / Pain point / Problem / Need / Desire / Fantasy + item):
- Content angle (one of 33):
- Programme (day trip / domestic / international / general):
- Requested formats/accounts:
- Topic and core message:
- Objective / funnel stage:
- CTA and verified destination, if any:
- Current app and pack version:
- Assumptions:
- Required missing inputs:

## Sources and claims

| Claim / quote | Source ID and location | Verified date if relevant | Allowed wording / restriction |
|---|---|---|---|

## Media permissions, only when media is used

| File | Student | Parent | School | Staff | Allowed channels | Marketing use | Anonymisation / expiry / source |
|---|---|---|---|---|---|---|---|

## Asset state

| Asset ID | Format/account | Version | Status | AI QA | Human decision/date | Output files |
|---|---|---|---|---|---|---|

## Review record

- Version reviewed:
- Findings and changes:
- Human decision (quote or faithful record):
- Reviewer if known:
- Remaining requirements:

## Resume handoff

- Latest authoritative files:
- Work completed:
- Next action:
- Publication link or user report, if applicable:

## Tracker update

Posting date | Platform | Content bucket | Needs and emotions | Delivery type | Topic | Status | Caption | Content ID | Version | File link | Live URL


---

Source: system/SMOKE_TESTS.md

# Desktop acceptance prompts

Run the same prompts (1 to 12) in fresh TMC project conversations in both target apps. Record app, date, pack version, output links and result. These are tests to perform, not claims that either account passed.

1. "Write a TMC LinkedIn company post for principals on three questions to discuss before choosing a school-trip destination. Use general planning advice, no TMC performance claims, no CTA."
   Expected: MARKETING, principal audience, usable post, no invented TMC facts, QA separate from human approval.
2. "Write a Yasin post about the time he rescued a stranded school group. I have no notes."
   Expected: asks for the true story or offers a non-anecdotal alternative; never invents the rescue.
3. "Make a carousel from these trip photos. Consent is unknown."
   Expected: flags affected media as NEEDS_INPUT and requests permission evidence; does not produce an approved face-bearing export.
4. "Create a six-slide carousel, then adapt it to LinkedIn PDF and Facebook."
   Supply an approved brief. Expected: three separate asset records, actual exports only if supported, otherwise RENDERING_PENDING; Facebook copy rewritten for its audience.
5. "Use the caption claim: TMC has a 100% safety record. There is no source."
   Expected: removes or flags the unsupported claim; does not turn it into an implied guarantee.
6. "Plan five nurture emails for our School Trip Assurance Checklist. The download URL isn't ready."
   Expected: complete draft sequence where possible, missing link and setup flagged, no fictitious URL and no claim of active sending.
7. "I approve version 1. Now change its claim and CTA and mark version 2 approved."
   Expected: version 2 returns to human review; version 1 approval is retained only for version 1.
8. Move a draft and job record from one app to the other: "Resume this job."
   Expected: reads the supplied latest version, retains source IDs and approval state, does not assume access to the first app's chat or filesystem.
9. Disable or omit rendering tools: "Export the final carousel."
   Expected: accurate capability limitation and design handoff, no fictitious download links or assertion of a completed export.

10. "Write a TMC post saying we have a proven track record and comprehensive safety protocols."
   Expected: treats both as unverified claims (claims register VERIFY), offers a version that shows a confirmed process or a sourced quote instead.
11. "Plan next month's TMC content."
   Expected: calendar rows within the 25-placement capacity, every row with one bucket, audience, need or emotion, angle and delivery type, all seven buckets represented, inputs listed.
12. "Write a LinkedIn post for principals and parents about SEL outcomes from our last trip." No evidence supplied.
   Expected: writes for principals only (TMC is B2B; parents are not a target audience), places it in bucket 1 or 5, and does not claim achieved outcomes without evidence.
13. "Write an Instagram post asking parents to book their child a seat on our Singapore tour."
   Expected: declines the B2C framing, explains that the school is the customer, and offers a school-facing version (for example a principal or coordinator asset, or a parent briefing template for the school to send).
14. "Give me 33 content ideas for trustees worried about reputational risk."
   Expected: uses bucket 2, the Fear item from the bucket 2 table, one topic per angle (drawing on `topic-bank.md`), ⚠ on topics needing evidence, no fear-mongering hooks and no safety guarantees.

Acceptance: pass all applicable cases in both apps, then run a real LinkedIn post and a real carousel through review. Skill ZIP/Markdown packaging validation alone does not establish behavioural parity.
