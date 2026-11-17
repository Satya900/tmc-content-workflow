# TMC Formats

Pack version: 0.3.1

Read only the relevant sections. The extensions at the end adapt external guidance and add Facebook, static posts, document carousels and nurture sequences. Video scripts are covered by tmc-reel; video production is deferred. TMC_WORKFLOW.md controls job state, permissions and tool availability. Repository-relative paths in source sections are provenance; use this pack's context and workflow equivalents. No other skill installation is required.


---

Source: skills/tmc-content-strategist/SKILL.md

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


---

Source: skills/tmc-linkedin/SKILL.md

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


---

Source: skills/tmc-social-post/SKILL.md

# TMC Social Post

## Channel roles
| Channel | Main audience | Role | Capacity (reference only) |
|---|---|---|---|
| Instagram | Coordinators, teachers, principals, and parents for parent-friendly carousels (secondary, questions directed to the school coordinator) | Understanding: process explainers, parent-friendly carousels, trip evidence | reference |
| Facebook | Parents and school communities, school leaders | Reuses parent-facing carousels (bucket 1: B1-02, B1-03). No separate production initially | reference |
| WhatsApp | Opted-in school contacts. Parent groups only via school-led sharing | Agreed follow-up, resource sharing, mobile-readable versions for schools to forward | as needed |
| Google Business Profile | Anyone searching for TMC | Updates and review responses | as needed |
| X | Education conversations | Not in current scope. Brand building only | 0 |

## Infographic types
| Type | Content | Rule |
|---|---|---|
| Educational | Tips, do's and don'ts, facts, checklists | Default for TMC |
| Inspirational | Quotes | Real, sourced quotes with permission only |
| Promotional | Programme announcements | Approved details only. No unapproved discounts |
| Conversational | Polls, questions, fill in the blank, caption this | Good for teachers and coordinators. No consumer contests or giveaways |
| Entertainment | Puzzles, comics, memes | Rare. Never with identifiable students |

Design: brand colours (70 / 20 / 10), logo, blank space, one message per graphic, readable on a phone.

## Brief
Audience, content bucket, need or emotion, angle, objective, core message, visual source (approved photo or graphic), CTA (optional), proof needed.

## Instagram
- First line carries the hook. Caption explains, the visual stops the scroll.
- Name the actual place, task or decision. Keep captions short for TOUR posts.
- No hashtags (writing standards).
- Feed size 1080 × 1350. Alt text after the visual is final.

## Facebook
Follow the Facebook adaptation rules in `system/FORMAT_EXTENSIONS.md`: start from approved source content, make it standalone, one practical takeaway or trip moment, at most one action, no forced engagement question. It is a separate asset with its own review.

## WhatsApp
- Broadcast: 3 to 6 short lines, one link, sent only to contacts who opted in.
- Status: one image (1080 × 1080) plus one line.
- Trip-time parent groups are operational channels. Do not use them for marketing.
- Mobile-readable parent versions (for example the B1-03 checklist) are supplied to the school, which shares them in its own groups or email. Square 1080 × 1080, large text, one idea per image, ends with "Questions? Ask your school's programme coordinator."

## Google Business Profile
Short update with one photo and one link. For reviews: thank the reviewer by role, respond to the specific point, never argue, never disclose student details.

## X
Only if the team adds it to scope. One idea per post, no hashtags, link to the blog.

## Rules
- One audience, one bucket, one message.
- Writing standards apply (`writing-standards.md`): restricted words, no em dashes, semicolons, exclamation marks, emojis or hashtags.
- Consent rules apply to every photo.
- Never invent testimonials, quotes or numbers.

## Output
- Channel, audience and bucket
- Visual brief (headline, optional support line, image or graphic direction)
- Caption
- Alt text (after the visual is final)
- CTA or none
- Claim and permission flags

## Bucket review items
If the request names a topic ID (for example B1-01) or falls inside a reviewed bucket, follow that bucket's reference: item spec, required inputs, production guide and selection register. Produce final copy only for selected items. For an unselected item, produce a draft only on explicit request, headed `PRE-SELECTION SAMPLE: not for publication`.

## Writing standards
Follow `writing-standards.md` (shared context) for every line of copy: run its reasoning framework before drafting and its self-check after. Run `python3 scripts/lint_copy.py <draft file>` where a terminal is available and fix every error. Where it is not, apply the self-check by hand. Record the draft's weakest point bluntly in the review file.


---

Source: skills/tmc-marketing-carousel/SKILL.md

# TMC Marketing Carousel

## Purpose
Create a strategic carousel where the copy carries the marketing argument and approved tour photos or brand graphics support the message.

## Required brief
- Audience
- Content bucket
- Need or emotion
- Content angle
- Funnel stage
- Objective
- Core message
- CTA (optional)
- Proof and source requirements

## Choose a carousel type
| Type | Best angles | Example |
|---|---|---|
| Educational infographic | Tips, do's and don'ts, cheat sheet, questions to ask before, parameters to consider | Five questions to ask before signing a tour proposal |
| Process walkthrough | Process, step-by-step guide, behind the scenes | From learning objective to field task in four steps |
| Problem, process, outcome story | Case study (verified), person A vs person B | How one school turned a history unit into a field day |
| Myth or truth | Myths, truths, beliefs, expectations vs reality | Four myths about overnight school trips |
| Conversational | Questions, fill in the blank | Which matters most when you pick a destination? |

## Narrative structure (default)
1. Hook
2. Problem or tension
3. Reframe
4. Explanation
5. Proof or practical detail
6. TMC difference or perspective
7. Takeaway
8. Optional CTA

Use 6 to 9 slides when suitable. Do not force a fixed count. A count in the hook must match the slides delivered.

## Slide rules
- One job per slide.
- Copy short enough to read on a phone in poor light.
- Do not describe the photo unless that helps the argument.
- Avoid turning every slide into a slogan.
- Specific language.
- Do not overuse TMC branding in the copy.
- CTA optional, usually only at the end.
- Writing standards apply (`writing-standards.md`). Write display text in sentence case. Staatliches renders it in capitals.

## Visual logic
For photo slides give: subject, scene, emotion, composition and text-space requirement, destination flexibility. Then pass to `tmc-photo-selector`. For graphic slides use brand colours, the logo, blank space and at most one line icon.

## Claims
Any safety, educational, statistical, school, price, testimonial or outcome claim must be verified before rendering.

## Output
- Carousel metadata (taxonomy fields)
- Slide-by-slide copy
- Visual direction for each slide
- Caption brief for each platform (Instagram, LinkedIn document post, Facebook)
- Alt text after visuals are final
- Claim checklist

## Bucket review items
If the request names a topic ID (for example B1-01) or falls inside a reviewed bucket, follow that bucket's reference: item spec, required inputs, production guide and selection register. Produce final copy only for selected items. For an unselected item, produce a draft only on explicit request, headed `PRE-SELECTION SAMPLE: not for publication`.

## Writing standards
Follow `writing-standards.md` (shared context) for every line of copy: run its reasoning framework before drafting and its self-check after. Run `python3 scripts/lint_copy.py <draft file>` where a terminal is available and fix every error. Where it is not, apply the self-check by hand. Record the draft's weakest point bluntly in the review file.


---

Source: skills/tmc-tour-photo-dump/SKILL.md

# TMC Tour Photo Dump

## Purpose
Turn real TMC trip photos into a branded, human, candid tour carousel.

Tour photo dumps usually sit in bucket 3 (service proof: how TMC runs a trip) or bucket 5 (student experience shown, not claimed). They serve the client school, which shares them with its own community (account care in a B2B relationship). Prospective schools' principals read them as evidence of how TMC runs a trip. Never write the caption as a sales pitch to parents. Any learning claim in a caption must match available evidence: an activity seen in the photos, student work or an educator's observation.

## Input convention
Accept the existing `uploads/<Trip Name>/Post N/` pattern or `school/destination/post_no/`. Preserve the user's hierarchy. Read school and destination from supplied context; folder labels alone do not establish school naming permission.

The post folder contains source photos and may optionally contain context metadata.

## Output convention
Mirror the same hierarchy under output:
`school/destination/post_no/`

Recommended outputs:
- `images/01.jpg ...`
- final PDF
- caption text
- generation metadata

## Workflow
1. Read folder path for school, destination and post number.
2. Read context file if present.
3. Inspect available photos.
4. Flag unusable or duplicate images for exclusion from the proposed sequence. Preserve source files and respect an explicitly hand-picked set.
5. Check media/consent status. Missing metadata means PERMISSION UNKNOWN, not approval. Pause use of affected media and request the missing information.
6. Build a visual sequence.
7. Write short tour-context copy.
8. Render in TMC visual template.
9. Export images + PDF.
10. Prepare caption and metadata.
11. Send for human approval.

## Copy style
Allowed:
- candid
- playful
- location/context-led
- human
- light
- memorable

Do not force an educational or sales claim onto every photo. Where a slide shows a learning task, name the task plainly (for example "Sketching the building before going inside") rather than claiming an outcome.

## Hard rule
Never infer or publish school/student identity, permissions, activity details, location facts or trip facts that are not supported by folder context or approved metadata.

## Desktop production
Use `system/WORKFLOW.md` (or bundled TMC_WORKFLOW.md) for output contracts, versions and approval. Use an available renderer only after checking its capabilities. `tmc-carousel-pipeline` is an optional adapter for an existing open-carrusel installation, not a required desktop service. If rendering is unavailable, return copy and a design brief with RENDERING_PENDING. Existing rendered files do not establish human approval or publication.

## Writing standards
Follow `writing-standards.md` (shared context) for every line of copy: run its reasoning framework before drafting and its self-check after. Run `python3 scripts/lint_copy.py <draft file>` where a terminal is available and fix every error. Where it is not, apply the self-check by hand. Record the draft's weakest point bluntly in the review file.


---

Source: skills/tmc-photo-selector/SKILL.md

# TMC Photo Selector

## Two selection modes
### TOUR
Choose photos that best tell the actual trip story.

### MARKETING
Start from the marketing message, then find photos that support each narrative role. Match the photo to the asset's content bucket: preparation and supervision for bucket 2, TMC running a trip well for bucket 3, school-relevant activities for bucket 4, students working on a task for bucket 5, and a clear sense of the programme type (day trip, domestic, international) for bucket 1. Natural photographs only. Published student faces need written permission.

## Required checks
Before selecting:
- media approval
- school permission
- student consent status
- allowed channels
- faces allowed
- school naming restrictions
- revocation/expiry if tracked

If these are unknown, flag `PERMISSION UNKNOWN`.

## Suggested metadata
- image_id
- school
- destination
- country
- trip/date
- subjects
- scene
- activity
- emotion
- content buckets the photo could support (1 to 5)
- programme (day trip, domestic, international)
- composition
- text-space
- visual_quality
- consent_status
- allowed_channels
- marketing_use
- notes

## Marketing matching
For each slide/content unit, define:
- desired subject
- desired scene
- emotion
- theme
- orientation
- text-space
- must-have / avoid

Then rank candidates.

## Rules
- Do not choose only the prettiest images.
- Prefer visual variety across a multi-slide asset.
- Avoid near-duplicates.
- Do not infer consent from the presence of a file.
- Do not identify students.


---

Source: skills/tmc-blog/SKILL.md

# TMC Blog

## Purpose
Create useful long-form content for school decision-makers that builds trust, search visibility and due-diligence credibility. Blogs boost SEO, keep readers updated, show expertise and build a loyal following through consistency.

## Marketing Template structure
1. **Speak about the problem.** Hook the reader.
2. **Make the problem personal.** What readers usually feel about it.
3. **Discovery of the solution.** The reframe or how the answer was found.
4. **Solve the problem.** The practical answer.
5. **Call to action.** One next step.

For TMC, add verified proof or TMC's perspective before the conclusion where useful.

## Blog types and title formulas
| Type | Formula | Example |
|---|---|---|
| Listicle | Number of items + benefit or statement of fact | 7 Questions to Ask Before Approving a School Trip |
| Detailed explanation | What is / What are + context | What Is Experiential Learning? A Guide for School Leaders |
| Step-by-step guide | How to + benefit + number of steps | How to Plan a Curriculum-Linked Domestic Tour in 6 Steps |

Bucket 1 agreed blog titles (pending selection): B1-01 detailed explanation "Two school-trip quotations, two prices: when is the higher fee worth paying?"; B1-04 listicle "Five budget decisions to review before reducing your school programme"; B1-05 step-by-step "How to shortlist a school programme in four steps". Keep agreed wording; offer alternatives only if asked.

Also supported: case study (verified only), comparison, pillar page, FAQ, thought leadership (Yasin's views only). Offer 3 to 5 title options using the formula for the chosen type.

## Required brief
- Audience
- Content bucket
- Need or emotion
- Content angle
- Search intent
- Primary keyword if SEO-led (start from `audience-personas.md` keywords, confirm with search data when available)
- Secondary topics
- Objective
- Proof and sources
- CTA

## Research
Use authoritative external research when needed and cite it with URL, publisher and checked date. Keep TMC internal claims separate from external evidence. External research never overrides TMC's positioning or facts.

## SEO workflow
If an SEO skill or tool is available:
1. Research search intent and gaps.
2. Build the brief.
3. Write.
4. Fact check.
5. SEO check: keyword in title, H1, first paragraph, a subheading and meta description, used naturally.
6. Generate metadata and schema.
7. Run TMC editorial QA.

## Blog structure
- Title
- Opening problem or hook
- Why this matters to the reader
- Reframe
- Main solution sections
- Practical examples or proof
- TMC perspective where appropriate
- Conclusion
- One CTA
- Meta title (about 60 characters)
- Meta description (about 155 characters)
- Proposed slug
- Suggested internal links, marked as suggestions until the target page is live
- FAQ opportunities

## Rules
- Search usefulness beats keyword stuffing.
- Do not invent data, board or curriculum alignment, safety facts or student outcomes.
- Mark unsupported claims.
- Make the article useful even if the reader never buys from TMC.
- Title counts must match the content.

## Bucket review items
If the request names a topic ID (for example B1-01) or falls inside a reviewed bucket, follow that bucket's reference: item spec, required inputs, production guide and selection register. Produce final copy only for selected items. For an unselected item, produce a draft only on explicit request, headed `PRE-SELECTION SAMPLE: not for publication`.

## Writing standards
Follow `writing-standards.md` (shared context) for every line of copy: run its reasoning framework before drafting and its self-check after. Run `python3 scripts/lint_copy.py <draft file>` where a terminal is available and fix every error. Where it is not, apply the self-check by hand. Record the draft's weakest point bluntly in the review file.


---

Source: skills/tmc-newsletter/SKILL.md

# TMC Newsletter

## High-impact email in six steps
1. **Clear goal:** what this email should achieve and which content achieves it.
2. **Subject line:** the most important part of the content, with an action word.
3. **Layout:** placement of copy, images and links.
4. **Introduction:** a few sentences that hook and say what the email is about.
5. **Core content:** the value, with a visual (table, chart, image) where useful.
6. **Conclusion and CTA:** short summary, further resources, one action.

## TMC rule
One email, one focus. Do not turn it into a generic monthly roundup unless explicitly requested.

## Email types
| Type | Use |
|---|---|
| Value add | Address a need or emotion from the persona table and show expertise |
| Quick win | One small thing the reader can do this week |
| Free resource | Deliver a checklist, template or guide (`tmc-lead-magnet`) |
| Case study | A verified school story (`tmc-case-study` evidence rules) |
| Tip of the iceberg | Two points in the email, the rest in a blog post |
| Promotional | Programme announcement with approved details only. No false urgency or unapproved discounts |
| Engagement | Survey, feedback request, thank-you. Use testimonial questions from the playbook after programmes |

## Audiences and segments
TMC is B2B: marketing email goes to school contacts only. Segment by role (owner or trustee, management, principal, coordinator, teacher), school segment and interaction level. Parent emails during a trip are operational communication on the school's behalf, not marketing. Never add parents to a marketing list.

One-to-one sales emails from Nadeem (for example sharing the B1-01 article with a school evaluating proposals, or the B1-04 resource when a buyer raises budget limits) are short, personalised to the school, contact and stage, link one resource and ask one question. Qualification asks for grade, approximate group size, dates and budget. No pressure language.

## Workflow
1. Define the audience segment and content bucket.
2. Define one goal.
3. Choose the email type.
4. Write 3 to 5 subject-line options.
5. Write preview text.
6. Write a short hook.
7. Deliver one useful idea.
8. Add TMC proof or perspective only where supported.
9. End with one action and its verified destination.

## Sequences
For nurture sequences, define for each email: purpose, subject options, preview text, body, CTA and destination, relative timing and condition. Define the enrolment trigger, audience, sender, exit conditions and unsubscribe handling. The five-email School Trip Assurance Checklist sequence is in `system/FORMAT_EXTENSIONS.md`.

## Tone
Direct, useful, personal, brief, calm. No brochure language.

## CTA examples
- read the full guide
- download a checklist or toolkit
- reply with a planning question
- view a case study
- book a conversation when commercially appropriate

## Output
- Goal, audience, bucket and email type
- Subject lines and preview text
- Email body
- CTA and destination
- Links and resources needed (placeholders until verified)
- Claim flags

Drafting an email is not sending it. Never claim email-client testing from a browser preview.

## Bucket review items
If the request names a topic ID (for example B1-01) or falls inside a reviewed bucket, follow that bucket's reference: item spec, required inputs, production guide and selection register. Produce final copy only for selected items. For an unselected item, produce a draft only on explicit request, headed `PRE-SELECTION SAMPLE: not for publication`.

## Writing standards
Follow `writing-standards.md` (shared context) for every line of copy: run its reasoning framework before drafting and its self-check after. Run `python3 scripts/lint_copy.py <draft file>` where a terminal is available and fix every error. Where it is not, apply the self-check by hand. Record the draft's weakest point bluntly in the review file.


---

Source: skills/tmc-lead-magnet/SKILL.md

# TMC Lead Magnet

A lead magnet is something useful a school leader receives in exchange for contact details. It should solve a real planning problem even if the school never books with TMC.

## Choose the type
| Type | Examples | TMC fit |
|---|---|---|
| Solution-based | Checklist, toolkit, template | School Trip Assurance Checklist, proposal comparison template, parent briefing pack (a template the school sends to its parents), post-trip reflection sheet |
| Educational | Webinar, tutorial, short course | Webinar for principals on curriculum-linked trips |
| Entertaining | E-book, quiz, assessment, challenge | Readiness assessment for international programmes |
| Community | WhatsApp or Facebook group | Teacher community for trip leaders (needs moderation and consent rules) |
| Promotional | Free consultation, free design | Free programme design consultation (needs commercial approval) |

Prefer solution-based magnets for principals and management.

## Agreed: B1-LM programme selection and comparison kit (bucket 1)
Spec in `bucket-1-programme-choice-price-value.md`. Pending selection.
- Contents: a programme brief, a side-by-side quotation worksheet, the seven booking questions (B1-03).
- Form: name, school, role, work email. Offer an optional programme discussion separately, never as a required field.
- Parent resources stay freely accessible, never gated.
- Placement: website download page, linked from posts, articles, video descriptions and school emails.
- A download signals interest, not a qualified opportunity. Qualification (grade, approximate group size, dates, budget) happens in Nadeem's follow-up.
- Tracking and form setup: Jihad.

## Brief
- Audience and school segment
- Content bucket
- The problem it solves (persona need or emotion)
- Format and length
- What the reader gets and how it is delivered
- Linked content (blog, email sequence, posts) that promotes it
- Required approvals and claims

## Build
1. Title that states the outcome (for example "The School Trip Assurance Checklist: 20 checks before you approve a programme").
2. Who it is for and when to use it.
3. The core content, organised for use, not reading (sections, checkboxes, fill-in fields).
4. A short "how TMC approaches this" note only where supported by confirmed process.
5. One next step.

## Landing page and form
Deliver: who it is for, what it helps them check, what they receive, form fields (keep to name, school, role, email, phone if needed), one primary CTA, thank-you page copy and the delivery email. Privacy wording, delivery URL, form submission and email enrolment are implementation requirements until verified. A landing page draft is not a working funnel.

## Promotion
Plan the email sequence (`tmc-newsletter`), 2 to 4 social posts and any blog that links to it. For the agreed foundation asset, use the five-email sequence in `system/FORMAT_EXTENSIONS.md`.

## Rules
- No invented statistics, guarantees or urgency.
- No discounts or coupons without approval.
- Checklists describe what a school should verify. They do not claim TMC meets every item unless confirmed.
- Track: new contacts generated (`measurement-and-calendar.md`).

## Output
- Brief and taxonomy fields
- Full lead magnet content
- Landing page, form and thank-you copy
- Delivery email
- Promotion plan
- Open implementation requirements and claim flags

## Bucket review items
If the request names a topic ID (for example B1-01) or falls inside a reviewed bucket, follow that bucket's reference: item spec, required inputs, production guide and selection register. Produce final copy only for selected items. For an unselected item, produce a draft only on explicit request, headed `PRE-SELECTION SAMPLE: not for publication`.

## Writing standards
Follow `writing-standards.md` (shared context) for every line of copy: run its reasoning framework before drafting and its self-check after. Run `python3 scripts/lint_copy.py <draft file>` where a terminal is available and fix every error. Where it is not, apply the self-check by hand. Record the draft's weakest point bluntly in the review file.


---

Source: skills/tmc-case-study/SKILL.md

# TMC Case Study

Case studies provide social proof by showing a school's before and after, written by TMC. Testimonials are recommendations in the customer's own words. Most belong to bucket 3 (service proof) or bucket 5 (student development), depending on the angle. Bucket 1 has one deferred case study: "How one school chose its programme within a fixed budget", which needs the actual brief, options, decision, TMC's contribution, specific feedback and permission.

## Framework (SCAI)
1. **Situation:** who the school is and its context.
2. **Complication:** the specific problem or goal the school faced.
3. **Question:** what the school was trying to answer (optional, useful for video and long form).
4. **Answer:** what TMC designed or did.
5. **Impact:** the verified outcome.

## Draft template (adapted from the workbook's B2B template)
> **The school.** Meet [Name, Designation] of [School name or "a CBSE school in Bangalore" if anonymised]. The school has [verified context: size, grades, programme history].
>
> **The challenge.** When we met [Name or the school], they wanted to [school's goal]. But they faced [problem 1], [problem 2] and [problem 3].
>
> **What we designed.** We worked from [root cause] and designed [solution 1], [solution 2] and [solution 3].
>
> **The outcome.** As a result, [the school] was able to [verified result 1], [verified result 2] and [verified result 3].

Every bracket is a required input. Leave unknown brackets visible as `NEEDS INPUT` rather than filling them.

## Required evidence
Do not create a publishable case study until the following are known or explicitly marked missing:
- school permission to be named, or a decision to anonymise
- trip or programme
- objective
- challenge
- TMC intervention
- actual outcome and its source (records, educator observation, student work, feedback)
- testimonial source, date and permission scope if a quote is used
- photo and media permission if visual
- source for any number

## Collecting testimonials
TMC is B2B, so the testimonials that matter most come from the school: principals, coordinators, trip-lead teachers and management. Parent and student words are supporting voices, collected through the school with consent. Ask after a programme:
1. What problem were you trying to solve for your students or school when you chose this programme?
2. What made your school choose TMC over other options?
3. Which parts of the programme worked best for your students and teachers?
4. What, if anything, did you notice in your students afterwards?
5. What would be the main reason you would recommend TMC to another school?

Optional for management: "How did the planning and approval process compare with previous trips?"

Accepted forms: short quote (one to three sentences), unstructured messages (WhatsApp, comments), video, audio, public reviews. Store the original, the date, the person's role and their permission for marketing use. Never edit a quote's meaning.

## Strong case studies show
- what the school needed
- why the usual approach was insufficient
- what TMC changed or designed
- what happened afterwards
- what another school can learn

## Output variants
A single verified case study can be repurposed into: full blog, LinkedIn post, marketing carousel, newsletter (case study email), Reel or testimonial video script, short proof card.

## Rules
- Never invent a before and after.
- Never convert satisfaction into measurable impact without evidence.
- Anonymise when permission does not allow naming.
- Preserve quotes accurately.
- Flag every quantitative claim.

## Bucket review items
If the request names a topic ID (for example B1-01) or falls inside a reviewed bucket, follow that bucket's reference: item spec, required inputs, production guide and selection register. Produce final copy only for selected items. For an unselected item, produce a draft only on explicit request, headed `PRE-SELECTION SAMPLE: not for publication`.

## Writing standards
Follow `writing-standards.md` (shared context) for every line of copy: run its reasoning framework before drafting and its self-check after. Run `python3 scripts/lint_copy.py <draft file>` where a terminal is available and fix every error. Where it is not, apply the self-check by hand. Record the draft's weakest point bluntly in the review file.


---

Source: skills/tmc-reel/SKILL.md

# TMC Reel and Video Scripts

Scope: video scripts, on-screen text, shot lists and captions can be drafted as text assets. Filming, editing and rendering video are deferred in this release. Mark video assets `RENDERING_PENDING` after the script is approved.

Bucket 1 recommends two informational YouTube videos, embedded in their blogs: a comparison video (B1-01) and a trade-off video (B1-04). Interviews, live Q&A and promotional videos are deferred for bucket 1.

## Hook timing
1 second on Instagram Reels and YouTube Shorts. 3 seconds on YouTube, Facebook, LinkedIn and WhatsApp.

## Reel (20 to 60 seconds)
The workbook's informational video logic is opening, value, CTA. For Reels, drop the self-introduction and credibility seeding.

1. 1-second hook
2. Problem
3. 2 to 4 value points
4. TMC reframe or perspective
5. One CTA

Timing guide: hook 0 to 2 s, problem 2 to 7 s, value 7 to 30 s, reframe 30 to 40 s, CTA final 3 to 5 s. Adjust for length.

## Informational video (YouTube, LinkedIn, Facebook)
Opening (3 s) → introduction (who is speaking) → seeding (about 6 s, one verified instance that earns the right to speak) → value (bullets or story) → CTA (comment, share, DM, answer a question) → sign-off.

## Interview video
Edification of the guest → introduction → education or inspiration → CTA → sign-off. Guest consent and a review of their quotes before publishing.

## Programme or webinar promo
Press the pain point → programme intro and takeaways → speaker intro → invitation and CTA → sign-off. Programme details, dates and prices must be approved.

## Testimonial or case-study video
Hook (problem or verified result) → situation → complication → question → answer (TMC's intervention, before and after) → verified outcome → CTA. Follows `tmc-case-study` evidence rules.

## YouTube long form (8 to 12 minutes)
Hook 3 s → why me 3 s → why should you care 30 s → watch-to-the-end anchor seeding the lead magnet 5 s → expand the problem 2 min → solution 5 min → new reality 2 min → CTA to the lead magnet. Pair with a `tmc-lead-magnet` asset.

## Visual sourcing
Prefer approved TMC trip footage, B-roll, preparation and logistics, teachers, landmarks and student activities where permissions allow. Same consent rules as photos.

## Production brief notes
Thumbnail with title and image, brand guidelines, plain or appealing background, eye-level camera, speaker looks at the lens and talks to the viewer, light facing the speaker, a microphone, a tripod, subtitles.

## Rules
- Strong first line.
- No "Hi, my name is..." opening on Reels.
- Do not make factual claims to improve the hook.
- Concise on-screen text that works with audio muted.
- Never fabricate a student story.
- Subtitle-ready phrasing.

## Output
- Concept, bucket and audience
- Spoken script with timings
- On-screen text
- Shot and B-roll list
- Caption
- CTA
- Claim and permission flags

## Bucket review items
If the request names a topic ID (for example B1-01) or falls inside a reviewed bucket, follow that bucket's reference: item spec, required inputs, production guide and selection register. Produce final copy only for selected items. For an unselected item, produce a draft only on explicit request, headed `PRE-SELECTION SAMPLE: not for publication`.

## Writing standards
Follow `writing-standards.md` (shared context) for every line of copy: run its reasoning framework before drafting and its self-check after. Run `python3 scripts/lint_copy.py <draft file>` where a terminal is available and fix every error. Where it is not, apply the self-check by hand. Record the draft's weakest point bluntly in the review file.


---

Source: skills/tmc-editorial-qa/SKILL.md

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


---

Source: skills/tmc-monthly-strategist/SKILL.md

# TMC Monthly Strategist

## Purpose
Use performance data to improve next month's plan. Leads and qualified school conversations come first. Do not optimise for vanity metrics.

## Inputs
Use whatever is supplied. Platform metric lists are in `measurement-and-calendar.md`.
- Content ID, platform, delivery type, audience, content bucket, need or emotion, angle, topic
- Platform metrics (Instagram, Facebook, LinkedIn, YouTube, email, website, lead magnets, blog)
- Business KPIs: leads, qualified school conversations, proposals, conversion rate, wins and losses
- Qualitative feedback from schools, and parent and student feedback collected through them
- Last month's calendar and decisions

## Analysis
1. State the reporting window and metric definitions. Missing data is unknown, not zero.
2. Compare output against the agreed calendar for selected items. No quota is fixed, so do not judge a month by placement count.
3. Separate reach metrics from business KPIs.
4. Rank buckets, angles, audiences and formats by qualified engagement and conversations, not reach alone.
5. Count unique Bengaluru school enquiries, qualified conversations, meetings and programme opportunities. For each, record the source topic ID and channel, audience fit, need and next action. Parent and student engagement is supporting evidence. Downloads signal interest, not qualification.
6. Identify weak or repetitive buckets and topics.
7. Identify audience and funnel gaps. Recommend Continue, Revise or Stop per topic ID, reviewed together with Yasin and Aishwarya.
8. Recommend Continue, Improve, Test, Reduce or Stop for each bucket, platform and format, with evidence.
9. Produce next month's master ideas and a draft calendar (via `tmc-content-strategist` fields).
10. Preserve strategic consistency unless data strongly justifies a change.

## Output
- Executive summary
- Output vs capacity
- What worked and what did not
- Content-to-conversation insights
- Audience insights
- Bucket mix recommendation
- Next-month experiments
- Recommended master ideas
- Proposed format and platform distribution
- Data caveats

## Rules
Low reach does not automatically mean bad content. High reach does not automatically mean useful content. Prioritise qualified school conversations and pipeline. Never invent benchmark figures.

## Writing standards
Follow `writing-standards.md` (shared context) for every line of copy: run its reasoning framework before drafting and its self-check after. Run `python3 scripts/lint_copy.py <draft file>` where a terminal is available and fix every error. Where it is not, apply the self-check by hand. Record the draft's weakest point bluntly in the review file.
Stance: be direct. If an idea, brief or plan is weak, say so, give the reason and offer a stronger option. Do not agree to be polite.


---

Source: system/FORMAT_EXTENSIONS.md

# TMC format extensions and adapted external methods

Modification notice: this file adapts selected techniques from Corey Haines's marketingskills (MIT) and Anthropic's knowledge-work-plugins marketing skills (Apache-2.0). See THIRD_PARTY_NOTICES.md and licenses in the release. Wording, scope and defaults have been changed for TMC. Upstream example numbers, generic benchmarks and algorithm claims are not adopted.

## Social and carousel methods

Use the TMC master brief before choosing a structure. For marketing carousels, choose among a useful checklist, a documented problem/process/outcome story, or a practical walkthrough. Use outcomes as hooks only when the source proves them. A count in the headline must match the content delivered. Each slide should work at phone size and advance the argument.

Keep typography, palette and spacing coherent. TMC's photo-led layouts may vary text placement to fit negative space and avoid faces. External advice requiring identical interior layouts does not override that rule. Avoid manufactured controversy, fear-based hooks, viral guarantees, mandatory hashtags and unsupported claims about platform algorithms. Platform limits must be checked when needed; upstream tables are not permanent specifications.

For LinkedIn document posts, use the marketing-carousel or tour route according to purpose, then export a PDF with an accompanying post. Yasin's post uses only his supplied perspective; a company post uses an organisational voice. The PDF needs an editable visual source and a visual review, not just a script.

## Facebook adaptation

Start from approved source content. Preserve its facts and purpose while making it readable as a standalone Facebook post. Choose one practical takeaway or trip moment, add relevant context, and use at most one suitable action. Do not force an engagement question. Supply copy, visual selection/crop guidance, alt text for final media and link requirements. Log the adaptation as a separate asset/version. Source approval does not approve rewritten Facebook copy automatically.

## Single-image social post

Use one message per graphic. Deliver headline, optional short support line, photo or graphic brief, caption and alt text after visual review. Use an actual quote only with a source and permission. A quote-like design is not permission to fabricate a testimonial. Use the TMC logo asset and keep small text readable.

## Blog and website content

Use the existing TMC blog and case-study structures. External content-creation guidance helps organise headings, metadata, reader questions and CTA destinations. Specific length targets are editorial choices, not ranking guarantees. Do not add statistics, testimonials, client logos or outcome sections merely because an external template expects them.

For a checklist landing page: state who the resource is for, what it helps them check, what they receive, the form fields required, a single primary CTA, and the thank-you next step. Treat delivery URL, form submission, privacy wording and email enrolment as implementation requirements until verified. A landing-page draft is not a working funnel.

## Five-email School Trip Assurance Checklist sequence

Use tmc-newsletter for voice and per-email copy. Adapt the upstream email-sequence method to the agreed TMC foundation asset:

1. Deliver the checklist and explain how to use it.
2. Help the school prepare answers to parent questions.
3. Explain what evidence to request when evaluating a travel partner.
4. Offer a verified example or practical application. If case-study proof is absent, use a clearly framed planning exercise.
5. Invite a relevant planning question or conversation.

These are proposed content jobs, not claims about TMC's current operational processes. Recommend spacing as a hypothesis for team review. Define the enrolment trigger, intended audience, sender, destination links, conversion/exit conditions and unsubscribe suppression. Use reply, click or confirmed enquiry events where available; do not rely on opens alone as proof of interest. Never invent benchmark performance, discounts, urgency, guarantees or live download links. Drafting the sequence does not activate sending.

For each email deliver purpose, subject options, preview text, full body, CTA/destination, relative timing and condition. Keep missing implementation inputs outside the reader-facing body where possible and mark the asset accordingly.

## Editing passes

Adapt Corey Haines's focused editing passes to TMC:

1. Clarity: is the point immediately understandable?
2. Voice: does this sound like the correct TMC account and audience?
3. Relevance: does the reader know why this matters to their school?
4. Evidence: can each factual claim be traced to a source?
5. Specificity: replace vague language with supported details, never invented numbers.
6. Human tone: retain warmth without amplifying fear or promising transformation.
7. Next step: is any CTA accurate, optional where appropriate, and connected to a real destination?

For short posts, combine these into a brief review. For larger assets, report exact sections needing revision. Do not fabricate expert reviewers, customer feedback or independent evaluation. Self-QA is one model's review and is not human approval.
