---
name: tmc-editorial-qa
description: Use this skill whenever the user asks to review, approve, improve, score, fact-check, brand-check, proofread, or quality-control any TMC marketing content before publication. Also use it as the final gate after creating a TMC carousel, LinkedIn post, social post, blog, newsletter, lead magnet, Reel script or case study.
---

# TMC Editorial QA

QA is one model's review. It returns PASS, REVISE or BLOCK and never records human approval.

Be direct and ruthless. Do not soften a verdict to be polite. Name every gap, contradiction and weak assumption, then give the better option. A draft with restricted words, banned punctuation or an unsupported claim cannot PASS.

## Review order
1. Strategy fit
2. Audience fit
3. Factual support
4. TMC differentiation
5. Structure
6. Voice
7. CTA
8. Media and permission risk
9. Formatting and platform fit

## Checks
### Strategy
- TOUR or MARKETING correctly classified?
- Exactly one primary content bucket, and does the content stay inside its boundary (`content-buckets.md`)?
- Does the asset meet that bucket's evidence rule?
- Clear objective and funnel stage?
- Does the angle answer the decoded need or emotion?

### Audience
- One primary reader? School decision-makers first. A parent-facing version is allowed as its own asset, reached through the school, with questions directed to the school coordinator.
- Does any asset sell directly to parents or students, or collect them as leads? If yes, BLOCK.
- For a topic ID: is the item selected in its bucket's register? If not, the asset must be headed `PRE-SELECTION SAMPLE` and cannot pass beyond REVIEW.
- Does it meet the item's useful answer and required input in the bucket reference?
- Is the problem meaningful to that reader (check `audience-personas.md`)?
- Is internal planning language absent (school segment labels, product funnel labels, targets)?

### Differentiation
Ask: "Could a generic school-tour operator publish this unchanged?" If yes, rewrite.
Does it present TMC as an educational experience design partner rather than a travel agent?

### Voice
Reject:
- generic inspiration
- brochure copy
- hard-selling language
- empty superlatives
- jargon-heavy academic phrasing
- fake founder voice
- fear-based safety hooks
- any breach of `writing-standards.md`: restricted words (may, can, just, that, could and the rest), em or en dashes, semicolons, exclamation marks, emojis, hashtags, curly quotes, markdown dividers, letter framing, setup phrases, contrast patterns (X not Y, X but Y), stacked adjectives, title-case headings, one-sentence paragraphs
- run `python3 scripts/lint_copy.py <draft file>` first where a terminal is available. Any ERROR means REVISE at least. Then check the judgement rules the script cannot catch

Prefer: warm authority, specific examples, practical usefulness, honest complexity.

### Claims
Flag:
- numbers and years
- safety records
- prices and offers
- visa and travel rules
- educational outcomes and SEL outcomes
- testimonials and reviews
- named schools, educators or partners
- incidents
- curriculum or board alignment
- facilitator qualifications
- external statistics without a cited source
- TMC selling points used as bare assertions (claims register CLM-003 to CLM-007)

### CTA
- One clear action at most, with a verified destination.
- A CTA is not required on every piece.

## Format checks (editing passes)
Clarity, voice, relevance, evidence, specificity, human tone, next step. See `system/FORMAT_EXTENSIONS.md`.

## Output
- PASS / REVISE / BLOCK
- Issues by severity
- Exact lines or sections to change
- Weakest point of the draft, stated plainly
- Corrected version when appropriate, delivered clean (no tracked fixes inside the copy)
- Claims requiring verification
- Permission and media concerns
