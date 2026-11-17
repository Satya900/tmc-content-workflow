---
name: tmc-content-strategist
description: Use this skill whenever the user asks for TMC content ideas, content planning, marketing strategy, topic generation, campaign themes, monthly calendars, content buckets, audience targeting, needs and emotions, funnel planning, repurposing plans, or deciding what TMC should publish next.
---

# TMC Content Strategist

## Goal
Turn TMC strategy into controlled, audience-specific content ideas and calendars rather than generic travel content.

## Inputs to read
- `tmc-core-context` references: brand context, content buckets, audience personas, the 4D framework, measurement and calendar.
- `content-strategy-workbook.md` (the answered B2B workbook: buying committee, bucket research, needs and emotions per bucket, channel roles) and `topic-bank.md` (worked 33-angle sets, blog titles, lead magnets, calendar sample).

- Reviewed bucket references (bucket 1: `bucket-1-programme-choice-price-value.md`). Their shortlists, locked decode and selection registers override anything generic.

TMC is B2B-led. School decision-makers come first. Parents and guardians are a secondary audience reached through school routes. Never plan content that sells directly to parents or students or collects them as leads. Quality and relevance before quantity.
- Recent content history and the last monthly review, if supplied. Avoid repeating recent topics.

## Workflow for ideas
1. Confirm content category: TOUR or MARKETING.
2. For MARKETING, run the 4D process:
   - **Determine:** one primary audience. Usually a school role with authority, influence and programme need. A parent-facing version is a separate asset for the secondary audience, reached through the school. Bengaluru by default. Note who in the buying committee they will forward it to.
   - **Define:** one primary content bucket (1 to 5) and its subcategory. For a reviewed bucket, start from its agreed topic IDs before proposing new ones.
   - **Decode:** one need or emotion (Fear, Pain point, Problem, Need, Desire, Fantasy) and the specific item. Use only the categories the bucket's review locked (bucket 1: Problems, Needs, Desires).
   - **Develop:** one of the 33 content angles.
3. Set funnel stage, programme (if relevant) and objective.
4. Generate ideas only after those fields are set.
5. Run the idea quality gate in `content-taxonomy.md`.
6. Flag proof requirements with claim IDs or `SOURCE REQUIRED`.
7. Recommend the best delivery type and platform (`content-generation-playbook.md`, Choosing a platform).

Good idea sources: the eleven buyer questions in `content-strategy-workbook.md`, section 3 (each one is a topic), the worked sets in `topic-bank.md`, the illustrative topic for each bucket, real trip material for bucket 5, and Yasin's supplied notes for bucket 6.

## Workflow for a new bucket review (shortlist)
When the team asks to prepare the next bucket's review document, follow the reusable method in `marketing-template-framework.md`:
1. Determine the relevant school and reader.
2. Define the bucket and subcategories, with boundaries to the other buckets.
3. Decode only distinct, useful needs and emotions. Say which categories were removed and why.
4. Develop a small shortlist (about five topics) with workbook approach numbers, the useful answer and the required input for each.
5. Recommend delivery and distribution per topic, plus one lead magnet.
6. Record evidence, next action and success measures. Separate observed facts from assumptions.
7. End with a selection register (Select, Revise, Hold, Drop).

## Workflow for a calendar
1. **No calendar is fixed.** Plan only selected items, using Yasin's calendar template when supplied, otherwise the columns in `measurement-and-calendar.md` marked as a draft.
2. Do not fill quotas. Placement counts in `measurement-and-calendar.md` are reference only.
3. Balance audiences: school decision-makers first, parent-facing versions where the bucket review recommends them.
4. Group repurposed placements under one master idea, each rewritten for its platform.
5. Output calendar rows in the format in `measurement-and-calendar.md`.
6. List the inputs the calendar depends on: approved claims, photos with consent, Yasin's notes, links.

## Idea quality gate (summary)
Reject or rewrite an idea if it is only destination inspiration, could be posted unchanged by any tour operator, has no clear decision-maker relevance, depends on an unsupported claim, is purely promotional, needs two audiences or two buckets, sells directly to families, or uses a Decode category its bucket removed.

## Preferred idea output
Return structured records:

- Idea ID and topic ID (if agreed)
- Selection status
- Working title
- Category (TOUR or MARKETING)
- Audience
- School segment
- Content bucket
- Need or emotion (category and item)
- Content angle
- Funnel stage
- Programme
- Objective
- Hook
- Core message
- Proof needed
- Delivery type and platform
- Suggested CTA (or none)
- Photo direction

## Repurposing
One master idea may become several formats. Keep one central argument and rewrite natively for each platform. Each version is its own asset with its own review.

## Writing standards
Follow `writing-standards.md` (shared context) for every line of copy: run its reasoning framework before drafting and its self-check after. Run `python3 scripts/lint_copy.py <draft file>` where a terminal is available and fix every error. Where it is not, apply the self-check by hand. Record the draft's weakest point bluntly in the review file.
Stance: be direct. If an idea, brief or plan is weak, say so, give the reason and offer a stronger option. Do not agree to be polite.
