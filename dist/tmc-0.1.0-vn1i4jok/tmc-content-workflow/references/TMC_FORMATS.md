# TMC Formats

Pack version: 0.1.0

Read only the relevant sections. The extensions at the end adapt external guidance and add Facebook, static posts, document carousels and nurture sequences. Video is deferred. TMC_WORKFLOW.md controls job state, permissions and tool availability. Repository-relative paths in source sections are provenance; use this pack's context and workflow equivalents. No other skill installation is required.


---

Source: skills/tmc-content-strategist/SKILL.md

# TMC Content Strategist

## Goal
Turn TMC strategy into controlled, audience-specific content ideas rather than generic travel content.

## Workflow
1. Confirm content category: TOUR or MARKETING.
2. For MARKETING, define:
   - audience
   - school segment if known
   - content pillar
   - customer emotion/problem
   - content angle
   - funnel stage
   - objective
3. Generate ideas only after those fields are set.
4. Check every idea against TMC positioning.
5. Flag proof or source requirements.
6. Recommend the best format: carousel, LinkedIn, blog, newsletter, reel, case study or lead magnet.
7. Avoid repeating recently used topics if content history is available.

## Idea quality gate
Reject or rewrite an idea if:
- it is only destination inspiration,
- it could be posted unchanged by any tour operator,
- it has no clear school decision-maker relevance,
- it depends on an unsupported claim,
- it is purely promotional,
- it has no meaningful audience problem or insight.

## Preferred idea output
Return structured records:

- Idea ID
- Working title
- Audience
- Pillar
- Emotion/problem
- Content angle
- Funnel stage
- Objective
- Hook
- Core message
- Proof needed
- Best format
- Suggested CTA
- Photo direction

## Repurposing
One master idea may become multiple formats, but keep one central argument and rewrite natively for each platform.


---

Source: skills/tmc-linkedin/SKILL.md

# TMC LinkedIn

## First choose account voice
### Yasin
- first person
- reflective
- story-led
- experienced
- warm authority

### TMC Company
- proof-led
- professional but warm
- practical
- portfolio, not brochure

## Default post structure
1. Hook
2. Problem / observation
3. Reframe
4. Value
5. TMC perspective / proof
6. Conversation CTA or takeaway

## Hook types
Use Marketing Template angles such as:
- truth
- observation
- mistake
- question
- case study
- comparison
- process
- founder lesson
- myth
- buyer guide

## Rules
- Write for one primary audience.
- Keep paragraphs short.
- Teach before selling.
- No generic "travel changes lives" writing.
- No unsupported story details.
- No invented Yasin memories or quotes.
- Do not add a CTA to every post.
- If the post is built from a voice note, preserve the speaker's actual point of view rather than polishing it into corporate copy.

## Output
Provide:
- post copy
- hook alternatives (optional)
- CTA
- recommended visual type
- claim/source flags


---

Source: skills/tmc-marketing-carousel/SKILL.md

# TMC Marketing Carousel

## Purpose
Create a strategic carousel where the copy carries the marketing argument and approved tour photos support the message.

## Required brief
Define:
- audience
- pillar
- customer problem/emotion
- funnel stage
- objective
- content angle
- core message
- CTA
- proof/source requirements

## Narrative structure
Default:
1. Hook
2. Problem / tension
3. Reframe
4. Explanation
5. Proof / practical detail
6. TMC difference or perspective
7. Takeaway
8. Optional CTA

Use 6–9 slides when suitable. Do not force a fixed count if the story needs fewer slides.

## Slide rules
- One job per slide.
- Keep copy concise enough for image-led design.
- Do not literally describe the photo unless that helps the argument.
- Avoid turning every slide into a slogan.
- Use specific language.
- Do not overuse TMC branding in the copy.
- CTA is optional and should usually appear only at the end.

## Photo logic
Provide a visual requirement for each slide:
- subject
- scene
- emotion
- composition / text-space requirement
- destination flexibility
Then pass to the photo-selection workflow.

## Claims
Any safety, educational, statistical, school, price, testimonial or outcome claim must be verified before rendering.

## Output
Produce:
- carousel metadata
- slide-by-slide copy
- visual direction for each slide
- caption brief
- claim checklist


---

Source: skills/tmc-tour-photo-dump/SKILL.md

# TMC Tour Photo Dump

## Purpose
Turn real TMC trip photos into a branded, human, candid tour carousel.

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

Do not force an educational or sales claim onto every photo.

## Hard rule
Never infer or publish school/student identity, permissions, activity details, location facts or trip facts that are not supported by folder context or approved metadata.

## Desktop production
Use `system/WORKFLOW.md` (or bundled TMC_WORKFLOW.md) for output contracts, versions and approval. Use an available renderer only after checking its capabilities. `tmc-carousel-pipeline` is an optional adapter for an existing open-carrusel installation, not a required desktop service. If rendering is unavailable, return copy and a design brief with RENDERING_PENDING. Existing rendered files do not establish human approval or publication.


---

Source: skills/tmc-photo-selector/SKILL.md

# TMC Photo Selector

## Two selection modes
### TOUR
Choose photos that best tell the actual trip story.

### MARKETING
Start from the marketing message, then find photos that support each narrative role.

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
- themes
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
Create useful long-form content for school decision-makers that builds trust, search visibility and due-diligence credibility.

## Marketing Template structure
Preserve this logic:
1. Speak about the problem / hook
2. Make the problem personal
3. Discovery / reframe
4. Solve the problem
5. CTA

For TMC, add verified proof/perspective before the conclusion where useful.

## Supported blog types
- Listicle
- Detailed explanation
- Step-by-step guide
- Case study
- Comparison
- Pillar page
- FAQ / knowledge base
- Thought leadership

## Required brief
- audience
- search intent
- pillar
- customer problem/emotion
- content angle
- primary keyword if SEO-led
- secondary topics
- objective
- proof/sources
- CTA

## Research
Use authoritative external research when needed.
Keep TMC internal claims separate from external evidence.
Do not let external research override TMC's approved positioning or facts.

## SEO workflow
If Claude SEO or an equivalent SEO skill is available:
1. Research search intent / gaps.
2. Build brief.
3. Write.
4. Run fact check.
5. Run SEO check.
6. Generate metadata/schema.
7. Run TMC editorial QA.

## Blog structure
- Title
- Opening problem/hook
- Why this matters to the reader
- Reframe
- Main solution sections
- Practical examples / proof
- TMC perspective where appropriate
- Conclusion
- One CTA
- Meta title
- Meta description
- Suggested internal links
- FAQ opportunities

## Rules
- Search usefulness beats keyword stuffing.
- Do not invent data, curriculum alignment, safety facts or student outcomes.
- Mark unsupported claims.
- Make the article useful even if the reader never buys from TMC.


---

Source: skills/tmc-newsletter/SKILL.md

# TMC Newsletter

## Core structure from the Marketing Template
1. Clear goal
2. Subject line
3. Layout
4. Introduction / hook
5. Core content
6. Conclusion + CTA

## TMC rule
One newsletter should have one clear focus. Do not turn it into a generic monthly roundup unless explicitly requested.

## Email types
- Value add
- Quick win
- Free resource
- Case study
- Tip of the iceberg
- Promotional
- Engagement / feedback

## Workflow
1. Define audience segment.
2. Define one goal.
3. Choose email type.
4. Write 3–5 subject-line options.
5. Write a short hook.
6. Deliver one useful idea.
7. Add TMC proof/perspective only where supported.
8. End with one action.

## Tone
- direct
- useful
- personal
- brief
- calm
- no brochure language

## CTA examples
- read the full guide
- download a checklist/toolkit
- reply with a planning question
- view a case study
- book a conversation when commercially appropriate

## Output
- goal
- audience
- subject lines
- preview text
- email body
- CTA
- links/resources needed
- claim flags


---

Source: skills/tmc-case-study/SKILL.md

# TMC Case Study

## Framework
Use the Marketing Template's case-study logic:
1. Situation
2. Complication
3. Question / challenge
4. Answer / TMC intervention
5. Impact / outcome

## Required evidence
Do not create a case study until the following are known or explicitly marked missing:
- school/client permission
- trip/programme
- objective
- challenge
- TMC intervention
- actual outcome
- testimonial source if used
- photo/media permission if visual
- any quantitative proof source

## Strong case studies show
- what the school needed
- why the usual approach was insufficient
- what TMC changed or designed
- what happened afterward
- what can be learned by another school

## Output variants
A single verified case study can be repurposed into:
- full blog
- LinkedIn post
- marketing carousel
- newsletter
- Reel script
- short proof card

## Rules
- Never invent a before/after.
- Never convert satisfaction into measurable impact without evidence.
- Anonymise when permission does not allow naming.
- Preserve quotes accurately.
- Flag every quantitative claim.


---

Source: skills/tmc-editorial-qa/SKILL.md

# TMC Editorial QA

## Review order
1. Strategy fit
2. Audience fit
3. Factual support
4. TMC differentiation
5. Structure
6. Voice
7. CTA
8. Media/permission risk
9. Formatting/platform fit

## Checks
### Strategy
- TOUR or MARKETING correctly classified?
- Clear objective?
- Correct pillar?
- Correct funnel stage?

### Audience
- One primary reader?
- Is the problem meaningful to that reader?

### Differentiation
Ask:
"Could a generic school-tour operator publish this unchanged?"
If yes, rewrite.

### Voice
Reject:
- generic inspiration
- brochure copy
- hard-selling language
- empty superlatives
- jargon-heavy academic phrasing
- fake founder voice

Prefer:
- warm authority
- specific examples
- practical usefulness
- honest complexity

### Claims
Flag:
- numbers
- years
- safety records
- prices
- visa/travel rules
- educational outcomes
- testimonials
- named schools
- incidents
- curriculum claims

### CTA
- one clear action maximum
- CTA not required on every piece

## Output
Return:
- PASS / REVISE / BLOCK
- issues by severity
- exact lines or sections to change
- corrected version when appropriate
- claims requiring verification
- permission/media concerns


---

Source: skills/tmc-monthly-strategist/SKILL.md

# TMC Monthly Strategist

## Purpose
Use performance data to improve the next month's content plan. Do not optimise only for vanity metrics.

## Inputs
Use whatever is available:
- content ID
- format/platform
- audience
- pillar
- topic
- impressions/reach
- engagement
- clicks
- saves/shares
- profile visits
- DMs
- lead magnet downloads
- qualified school conversations
- proposals
- wins/losses
- qualitative feedback

## Analysis
1. Validate data completeness.
2. Separate reach metrics from business metrics.
3. Identify top themes by qualified engagement.
4. Identify content that caused conversations.
5. Identify weak or repetitive themes.
6. Identify audience gaps.
7. Identify funnel gaps.
8. Recommend what to double down on, test, reduce or stop.
9. Produce next-month topic recommendations.
10. Preserve strategic consistency unless data strongly justifies a change.

## Output
- executive summary
- what worked
- what did not
- content-to-conversation insights
- audience insights
- pillar mix recommendation
- next-month experiments
- recommended master ideas
- proposed format distribution
- data caveats

## Rule
Low reach does not automatically mean bad content, and high reach does not automatically mean useful content.
Prioritise qualified school conversations and downstream pipeline.


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
