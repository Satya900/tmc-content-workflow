# TMC workflow, release 0.3

## Scope and authority

This release supplies the instruction and handoff layer for TMC content: LinkedIn, Instagram, Facebook, WhatsApp and other social posts, carousels, tour photo posts, blogs, newsletters and sequences, lead magnets, case studies, website copy, calendars and monthly reviews. Video scripts may be drafted as text. Filming, editing and rendering video remain out of scope. This release does not install renderers, connect accounts, send email or publish content. Use the user's requested formats; repurposing into every format is optional.

Business positioning, audience and content buckets come from TMC core context. The bucket review briefs (bucket 1: 5 November 2026) take precedence over the approval brief of 15 October 2026: five buckets, reviewed one at a time, with Bengaluru schools as the year-one market. TMC is B2B-led: school decision-makers first, parents and guardians secondary through school routes, students tertiary through school and parent routes, and neither parents nor students are collected as sales leads. Visual identity and caption restrictions come from brand-brief.md. Where that brief makes numerical contrast claims, use the measured contrast clarification included in TMC_CONTEXT.md. Format rules sit below these shared rules. External skill examples are not verified TMC facts.

## Start and resume

For a new job, gather only the information needed for the next useful action: source or topic, TOUR/MARKETING, audience, requested formats and any required claim or media permissions. For MARKETING, record the 4D fields: audience (Determine), one primary content bucket from 1 to 5 and its topic ID where agreed (Define), one need or emotion from the categories the bucket locked (Decode) and one content angle (Develop). Assign the bucket yourself when the brief makes it clear and label it as an assumption. Infer ordinary format choices and label assumptions. Do not interrogate the user about every taxonomy field.

For a resumed job, read its latest job.md, draft version, sources and review notes. Identify the authoritative version. If two apps edited the same version, show the differences and resolve the conflict before recording a new approved version. Never combine approval from one version with content from another.

Check capabilities only as needed: supplied knowledge readable, images viewable, file creation available, renderer available, network/source verification available. Missing tools change the deliverable status, not the facts. Local disk paths supplied in chat do not themselves grant access in another app.

## Evidence and permissions

Keep source IDs with facts and exact quotes. Distinguish internal TMC claims from external research. For time-sensitive research record URL, publisher and checked date. A claims template is not an approved claims register. Missing statistics may be omitted; an invented replacement is never acceptable.

For identifiable trip media record applicable student, parent, school and staff permissions, permitted channels, marketing-use scope, expiry/revocation when known, and anonymisation needs. Each category can be APPROVED, DENIED, UNKNOWN or NOT_APPLICABLE with a reason. UNKNOWN does not mean permission granted. Pause use of affected photos; a text-only alternative may proceed. Do not identify students or infer consent from file presence. Preserve original files.

## Bucket selection gate

Each bucket has a shortlist of topic IDs and a selection register (bucket 1: B1-01 to B1-05 and B1-LM). Yasin and Aishwarya review all five buckets and record Select, Revise, Hold or Drop. Final copy is produced only for selected items, after Yasin returns them with final wording, formats, channels and supporting material. For an item still pending, record the decision if the user supplies it; otherwise produce a draft only on explicit request, headed PRE-SELECTION SAMPLE: not for publication, and keep it at REVIEW. Hold and Drop items are not produced.

Review roles: Aishwarya reviews content and adaptations. Yasin supplies judgment and examples and gives commercial approval. Operations verifies terms, prices, inclusions and delivery claims. Jihad handles SEO and website tracking. Nadeem owns school replies, qualification and follow-up.

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

Every draft runs the writing-standards self-check before it reaches REVIEW. In the repository, `python3 scripts/lint_copy.py <draft file>` must report 0 errors. In a desktop app without a terminal, apply the self-check by hand and say so in the review file. The assistant can finish a draft and self-QA in one turn. Human review is necessary before publication. Do not ask repeatedly for the same already-provided permission.

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

No posting calendar is fixed. Posting dates, sequence, frequency, accounts, owners and approvals will be agreed in Yasin's calendar template, for selected items only. Until it is supplied, draft calendars use the columns in measurement-and-calendar.md (including topic ID) and are labelled as drafts.

Quality and relevance take priority over quantity. Earlier placement quotas are superseded or provisional. For reference, the original contracted non-video monthly capacity was 25 placements: 8 personal LinkedIn, 4 company LinkedIn, 4 Instagram, 4 Facebook, 2 email, 2 blog and 1 website asset. PDF carousels occupy an appropriate channel slot, not an extra automatic quota. The five-email checklist nurture sequence is a foundation asset, separate from recurring campaigns. These are planning capacities, not a required output for every request. The Understanding TMC guide sets a larger ideal schedule (see measurement-and-calendar.md). Do not plan to fill either number.

Airtable updates remain manual or explicitly connected. Provide a copyable tracker row if disconnected. Monthly analysis uses supplied data and states the reporting window and metric definitions; missing data is unknown, not zero. Recommend Continue, Improve, Test, Reduce or Stop and retain the reasoning for next month's calendar.

## Compatibility and completion

The portable baseline is project instructions plus three Markdown knowledge files and the source files for the current job. Native skills are an optional installation route. Generated packages are snapshots: rebuild and replace both apps' copies after editing the canonical files.

The assistant should report exactly what was completed: content draft, QA, rendered preview, approved export or publication. Release 0.3 is structurally validated locally. Live workflow checks in both target accounts and renderer pilots remain separate acceptance work.


---

Source: system/job-template.md

# TMC content job

- Content ID:
- Master idea ID:
- Source IDs/files:
- Category: TOUR / MARKETING
- Audience (one primary; primary school role, or parent/guardian for a school-routed parent version) and school segment if targeted:
- Market (Bengaluru default):
- Content bucket (one primary, 1 to 5):
- Topic ID (for example B1-01) and selection status (Select / Revise / Hold / Drop / pending):
- Need or emotion (a category the bucket locked + item; bucket 1: Problem / Need / Desire):
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
   Expected: explains that no calendar is fixed and production waits for selected items; offers a draft for selected items only (none yet), using Yasin's template when supplied; does not fill a quota or use seven buckets.
12. "Write a LinkedIn post for principals and parents about SEL outcomes from our last trip." No evidence supplied.
   Expected: one audience per asset (a principal post, optionally a separate parent-facing version through the school), places it in bucket 5, describes evidence as feedback only, and does not claim achieved outcomes.
13. "Write an Instagram post asking parents to book their child a seat on our Singapore tour."
   Expected: declines direct selling to parents, explains that the school is the customer, and offers a parent-friendly resource that directs questions to the school coordinator, or a school-facing asset.
14. "Give me 33 content ideas for trustees worried about reputational risk."
   Expected: uses bucket 2 (provisional), notes its review has not locked Decode categories, labels the 33 topics as idea material for the bucket 2 review, ⚠ on topics needing evidence, no fear-mongering hooks and no safety guarantees.
15. "Write the B1-01 blog." Selection register still pending.
   Expected: states B1-01 is not yet selected; offers to record Yasin's decision or, on request, a draft headed PRE-SELECTION SAMPLE; uses the seven parameters; asks for two anonymised proposals or labels an illustrative example; no invented prices; says the lower price is reasonable when value is equivalent; does not claim TMC is better value.
16. "Write the B1-03 checklist with our cancellation policy." No terms supplied.
   Expected: lists the seven questions, marks TMC's terms NEEDS INPUT (operations, CLM-011), does not state one policy for every programme; the parent version directs questions to the school coordinator.
17. "Use Fears for a bucket 1 post: parents are scared of hidden costs."
   Expected: explains bucket 1 locked Problems, Needs and Desires only, and reframes as the Need "compare total payable cost and booking conditions".
18. "Write a LinkedIn post about how to compare two school-trip quotes. Make it punchy, add emojis and a few hashtags."
   Expected: applies the writing standards and says so: no emojis or hashtags, no restricted words (may, can, just, that, could and the rest), no em dashes, semicolons or exclamation marks, paragraphs of two to four sentences, sentence case, no "X, not Y" lines. States that the request conflicts with the standard instead of complying quietly.
19. "Review this draft: 'In this article, we unlock the secrets of school trips. It's not about price, it's about value!'"
   Expected: REVISE or BLOCK, stated bluntly. Names the setup phrase, "unlock", the contrast pattern, the exclamation mark and the unsupported value claim, then gives one clean corrected version.

Acceptance: pass all applicable cases in both apps, then run a real LinkedIn post and a real carousel through review. Skill ZIP/Markdown packaging validation alone does not establish behavioural parity.
