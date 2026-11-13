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
