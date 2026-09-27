# TMC workflow, release 0.1

## Scope and authority

This release supplies the instruction and handoff layer for non-video TMC content. It does not install renderers, connect accounts, send email or publish content. Use the user's requested formats; repurposing into every format is optional.

Business positioning comes from TMC core context. Visual identity and caption restrictions come from brand-brief.md. Where that brief makes numerical contrast claims, use the measured contrast clarification included in TMC_CONTEXT.md. Format rules sit below these shared rules. External skill examples are not verified TMC facts.

## Start and resume

For a new job, gather only the information needed for the next useful action: source or topic, TOUR/MARKETING, audience, requested formats and any required claim or media permissions. Infer ordinary format choices and label assumptions. Do not interrogate the user about every taxonomy field.

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

Website asset: page copy, headings, CTA/form requirements, metadata and implementation handoff. Generating copy is not deploying a page or activating a form.

## Repurposing and tracking

Keep one source ID and master idea across adaptations. Rewrite hooks, density and account voice for each platform. Do not invent an anecdote to personalise Yasin's version.

The scope's non-video monthly capacity is 25 placements: 8 personal LinkedIn, 4 company LinkedIn, 4 Instagram, 4 Facebook, 2 email, 2 blog and 1 website asset. PDF carousels occupy an appropriate channel slot, not an extra automatic quota. The five-email checklist nurture sequence is a foundation asset, separate from recurring campaigns. These are planning capacities, not a required output for every request.

Airtable updates remain manual or explicitly connected. Provide a copyable tracker row if disconnected. Monthly analysis uses supplied data and states the reporting window and metric definitions; missing data is unknown, not zero. Recommend Continue, Improve, Test, Reduce or Stop and retain the reasoning for next month's calendar.

## Compatibility and completion

The portable baseline is project instructions plus three Markdown knowledge files and the source files for the current job. Native skills are an optional installation route. Generated packages are snapshots: rebuild and replace both apps' copies after editing the canonical files.

The assistant should report exactly what was completed: content draft, QA, rendered preview, approved export or publication. Release 0.1 is structurally validated locally. Live workflow checks in both target accounts and renderer pilots remain separate acceptance work.
