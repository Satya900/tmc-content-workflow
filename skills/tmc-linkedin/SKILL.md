---
name: tmc-linkedin
description: Use this skill whenever the user asks for a TMC LinkedIn post, Yasin LinkedIn post, company-page post, founder thought-leadership post, LinkedIn poll, LinkedIn document carousel caption, LinkedIn content series, or a repurposed TMC insight for LinkedIn.
---

# TMC LinkedIn

LinkedIn is TMC's primary B2B channel for school owners, trustees, management, principals and academic leaders. Original contracted capacity (reference only, no quota is fixed): 8 Yasin posts and 4 company posts a month.

## First choose account voice
### Yasin (founder)
- First person, reflective, story-led, experienced, warm authority.
- His voice can carry any bucket. In bucket 1 he gives short native extracts (B1-01) and explains one budget trade-off (B1-04), always from his own judgment and examples.
- Uses only his supplied notes, voice notes or approved past statements. No invented memories, anecdotes, quotes or opinions. With no notes, offer a non-anecdotal draft marked `NEEDS INPUT: Yasin's own example`.

### TMC company
- Proof-led, professional but warm, practical.
- Portfolio, not brochure. Shows process, evidence and useful frameworks.

## Brief
Audience, content bucket, need or emotion, angle, funnel stage, objective, core message, proof needed, CTA (optional).

## Default post structure
1. Hook (first two lines decide whether the post is read)
2. Problem or observation
3. Reframe
4. Value
5. TMC perspective or proof
6. Conversation CTA or takeaway

## Strong angles for LinkedIn
Truths, observations, mistakes, questions to ask before, parameters to consider, options to choose between, process, behind the scenes, case study (verified), experiences and lessons (Yasin's notes only), myths, beliefs, person A vs person B, cheat sheet. Avoid memes and humour for school leaders.

## Formats
- Text post (default).
- Document carousel (PDF): use `tmc-marketing-carousel`, then write the post that accompanies it.
- Poll: one question for teachers or leaders, 2 to 4 options, a short framing paragraph. Use the result in a later post.
- Single image: use `tmc-social-post` for the visual brief.

## Rules
- Write for one primary audience.
- Paragraphs of two to four sentences. No single-line paragraphs stacked for effect.
- Teach before selling.
- No generic "travel changes lives" writing.
- No unsupported story details.
- Do not add a CTA to every post.
- If the post is built from a voice note, preserve the speaker's actual point of view rather than polishing it into corporate copy.
- Writing standards apply (`writing-standards.md`): restricted words, no em dashes, semicolons, exclamation marks, emojis or hashtags.

## Output
- Account and bucket
- Post copy
- Hook alternatives (optional)
- CTA or none
- Recommended visual type
- Claim and source flags

## Bucket review items
If the request names a topic ID (for example B1-01) or falls inside a reviewed bucket, follow that bucket's reference: item spec, required inputs, production guide and selection register. Produce final copy only for selected items. For an unselected item, produce a draft only on explicit request, headed `PRE-SELECTION SAMPLE: not for publication`.

## Writing standards
Follow `writing-standards.md` (shared context) for every line of copy: run its reasoning framework before drafting and its self-check after. Run `python3 scripts/lint_copy.py <draft file>` where a terminal is available and fix every error. Where it is not, apply the self-check by hand. Record the draft's weakest point bluntly in the review file.
