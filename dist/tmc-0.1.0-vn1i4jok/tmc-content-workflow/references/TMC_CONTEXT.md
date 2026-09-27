# TMC Context

Pack version: 0.1.0

Business positioning, visual brand and evidence rules. Historical mentions of video are deferred in this release. Source filenames below identify provenance; all their text is included here.

## Visual clarification

Computed sRGB contrast against white: Classroom Cyan #1AAFE0 = 2.54:1; Cyan Deep #0E7FA6 = 4.56:1. These measured values supersede the source brief's approximate numerical claims. Do not assume cyan becomes legible simply because text is large. Check the actual foreground/background pair, especially on photo scrims. Use charcoal or black on light surfaces where contrast is insufficient. The brand's letter-spacing value has no unit specified; do not interpret it as 30-60 CSS pixels.


---

Source: skills/tmc-core-context/references/tmc-brand-context.md

# TMC Brand Context

## Business
The Modern Classroom (TMC) is an experiential education company that works primarily with schools through day trips, domestic educational tours, and international educational tours.

## Core positioning
TMC must not sound like a generic tour operator. The brand should be presented as an educational-travel partner that understands school goals, student development, safety, parent confidence, logistics, and educational value.

## Commercial objective
Year-1 content should build enough credibility and visibility that relevant school contacts:
1. reach out to TMC, or
2. feel confident responding positively when TMC reaches out.

## Audience hierarchy
Prioritise:
1. Principals / Heads of School
2. Academic Coordinators / HODs
3. Management / Trustees
4. Parents as indirect influencers

## Marketing themes
1. Parent Confidence
2. Safety & Operational Excellence
3. Student Outcomes & SEL
4. School Competitive Edge
5. Yasin's Perspective
6. Educational travel design / customisation
7. Proof, case studies and real trip evidence

## Voice
- Warm authority
- Specific over abstract
- Practical rather than academic
- Honest rather than promotional
- Experienced, calm and useful
- Educational partner, not travel agent

## Avoid
- "Book now", "best prices", package-selling language
- Generic phrases like "broaden horizons" unless made concrete
- Unsupported superlatives
- Inflated educational claims
- Academic jargon for its own sake
- Defensive replies to objections
- Frequent CTAs
- Generic travel photography with no context in marketing content

## Two content modes
### TOUR
Purpose: document a real TMC trip.
Photos determine the story.
Copy may be light, candid, location-based and experience-led.

### MARKETING
Purpose: build positioning, trust, authority, demand and qualified school conversations.
Strategy determines the story.
Tour photos are visual evidence and emotional support; the copy carries the argument.

## Positioning sequence
Early-stage content should lead with capabilities, proof, safety, parent confidence, student outcomes and case studies. Introduce deeper customisation/diagnostic language only when appropriate to the campaign phase and audience.

## Rule
Never invent facts about TMC, a school, a student, a parent, a trip, a safety incident, prices, outcomes, testimonials, approvals or permissions.


---

Source: brand-brief.md

# TMC Brand Brief — for carousel generation

Condensed from `TMC_Design_Elements.docx` v1.0 (06 May 2026). Full doc
has print/web/motion rules too; this file keeps only what matters for
generating Instagram/LinkedIn carousels. Feed this to open-carrusel's
Brand Setup wizard, or to Claude Code when it's designing slides.

## Colors

| Name | Hex | Use for | Notes |
|---|---|---|---|
| Classroom Cyan | `#1AAFE0` | Headlines, day numbers/chips, CTAs, icon strokes, links | **Fails AA contrast on white below 18pt** — large display text only, never small captions |
| Cyan Deep | `#0E7FA6` | Cyan text under 18pt, button hover/pressed states | Passes AA (4.7:1) — use this for small cyan text instead of Classroom Cyan |
| Cyan Wash | `#E6F6FB` | Callout/quote backgrounds, soft panel tints | |
| Modern Charcoal | `#3F3F3F` | H1/H2 headings on white | |
| Anchor Black | `#0E0E0E` | Body text, captions, outlines, logo mark | |
| Mist Grey | `#F2F4F6` | Card backgrounds, alternating panels | |
| Paper White | `#FFFFFF` | Dominant background — always the largest area | |

**Ratio: 70% white surface, 20% neutrals, 10% cyan.** If cyan is everywhere, nothing stands out.

## Fonts

- **Display — Staatliches** (free, Google Fonts): tagline, hero headlines, day chips/numbers, short destination-sign phrases. ALL CAPS only, letter-spacing 30–60. Never for body or anything under 18pt.
- **Body — DM Sans** (free, Google Fonts): everything else. Regular (400) for body, Bold (700) for subheads, Medium (500) for captions/labels.
- Two families max, two weights each. Sentence case for headings — all caps is reserved for Staatliches/tagline.
- Office fallback (no internet): Arial Black or Bebas Neue for display, Arial or Calibri for body.

## Logo

- Files: `TMC_Logo_Primary_CRM.png` (full color, use on white/light) and `TMC_Logo_Dark_Mode_CRM.png` (reverse, use on Cyan Deep/Anchor Black/photos).
- The hand-drawn circle is intentional — never redraw as a perfect ring, never add drop shadows/glows/gradients.
- Clear space on all sides = height of the lowercase "t" in "classroom." Minimum size: 96px digital.
- On reels/video: reverse logo, bottom-right corner, 6–8% of frame width, static (don't animate after intro).
- Tagline "TRAVEL. EXPERIENCE. LEARN." — always this order, all caps, two spaces between words, periods included. Never move it above the wordmark or reword it.

## Photo selection (what to pick when curating a day's folder)

**Prefer:** students reacting (not posing), wide environmental shots that place students in the location, honest moments (tired feet, group hugs, full plates), at least one teacher visible in group shots, one clean establishing shot of the destination alone.

**Avoid using as hero/cover shots:** stiff lined-up group photos, peace-sign/selfie-stick poses, anything shot in Full HDR, wide shots of no people at all.

**Reminder:** written consent required before publishing any student's face — flag if unsure a shot has clearance.

## Caption voice

Direct, specific, warm — like a class teacher talking to a parent. Name the actual place/dish/museum. If a day was long, say so; trust comes from accuracy, not hype.

- **Do:** "Day 3. A waffle stop at Grand Place, then the Atomium."
- **Don't:** "Embark on an unforgettable journey of cultural awakening."

**Never use:** skyrocket, revolutionize, unlock, unveil, illuminate, paradigm, realm, esteemed, remarkable, testament, stark, however, kindly, "esteemed parents," "valued patrons."

**Never use:** em dashes, semicolons, exclamation points.

## Export sizes (from the brand doc's channel table)

- Instagram feed carousel: **1080×1350** (matches open-carrusel's recommended 4:5)
- Instagram/Facebook Reel: 1080×1920, keep bottom 200px / top 250px clear of text (UI overlays)
- WhatsApp share image: 1080×1080

## Overlay style for photo carousels (dynamic, on-brand)

Goal: scroll-stopping text-on-photo carousels, without breaking the
brand system above. This is a deliberate blend — TMC's real
typography and colors, arranged with the energy of a handwritten
carousel, but without adopting the handwritten look itself.

- **Typography stays TMC's.** Staatliches for the hook line — short,
  punchy, one sentence max. Its tall condensed all-caps form already
  reads as bold and dynamic without needing a script font. DM Sans
  Medium for any supporting line. No handwritten/cursive fonts — none
  exist in the TMC system, and the brand doc caps type families at two.
- **Placement is dynamic, not dead-center.** Put the hook line in the
  photo's calm negative space (rule of thirds, away from faces) —
  upper-left on one slide, lower-right on the next, wherever the photo
  actually has room. Vary it slide to slide so the carousel doesn't
  feel like a repeated template. This is where the "scroll-stopping"
  energy comes from — not from the font.
- **Always sit text on a soft scrim**, gradient not solid block, per
  the brand doc's "don't place type on a busy photo without a scrim."
  The photo should still read through.
- **Color:** Classroom Cyan is fine for the hook line since it's large
  display text (18pt+ passes contrast). Any smaller supporting line
  uses Cyan Deep or Paper White with a text shadow — never small
  Classroom Cyan text.
- **Skip generic doodles** (hearts, sparkles, scroll banners) — those
  belong to the reference account's identity, not TMC's. If a slide
  wants a small graphic accent, reuse TMC's actual icon language: a
  single 1.5px-stroke line icon, or a short hand-drawn underline
  echoing the logo's own imperfect line quality.
- **Cover slide carries the boldest placement** — large Staatliches
  hook, off-center. Body slides keep captions shorter and quieter so
  the carousel has rhythm instead of every slide shouting equally.

Don't feed the reference screenshots into open-carrusel's own
"reference image" style-matching feature — that would pull in the
handwritten font and doodles directly. Point Claude Code at this
section instead.

## Approval gate (from the brand doc — worth keeping as a final check)

Before anything ships: does it follow this brand doc (color/type/logo), does it read aloud like a class teacher talking to a parent, and could a parent understand it on a phone in poor light in five seconds? If not, simplify.


---

Source: skills/tmc-core-context/references/marketing-template-framework.md

# Marketing Template Framework Applied to TMC

Use the 4D framework to build content.

## 1. Determine
Identify the target customer:
- Principal / Head
- Coordinator / HOD
- Management / Trustee
- Parent
Then note school segment if known.

## 2. Define
Choose a content bucket / TMC theme.

## 3. Decode
Choose the customer emotion:
- Fear
- Pain Point
- Problem
- Need
- Desire
- Aspiration

## 4. Develop
Choose a content angle:
1. Direct answer
2. Mindset
3. Truth
4. Tips
5. Things to follow
6. Mistakes
7. Myths
8. Secrets
9. Experience / lessons
10. Case study
11. Testimonial
12. Observation
13. Review / appreciation
14. Process
15. Tools
16. Step-by-step guide
17. Do / don't
18. Cheat sheet
19. FAQ
20. Options to choose between
21. Questions to ask before
22. Comparison
23. Parameters to consider
24. Live example
25. Research / study
26. Report / statistic / infographic
27. Behind the scenes
28. Belief
29. Trend
30. Expectations vs reality
31. Humour
32. Affirmation
33. Meme

## Delivery
After the idea is valid, route it to:
- Blog
- Newsletter
- LinkedIn
- Reel
- Marketing carousel
- Case study
- Lead magnet

## Distribution rule
The same master idea may be repurposed into several formats, but each format must be rewritten for its native consumption pattern. Do not paste identical copy across channels.


---

Source: skills/tmc-core-context/references/content-taxonomy.md

# TMC Content Taxonomy

Every marketing asset should carry these fields where practical:

- content_id
- content_category: TOUR | MARKETING
- target_audience
- school_segment
- content_pillar
- customer_emotion
- content_angle
- funnel_stage: awareness | consideration | proof | conversion | nurture
- objective
- topic
- hook
- core_message
- proof_required
- claim_risk: low | medium | high
- photo_requirement
- platform
- CTA
- source_materials
- approval_status

## Recommended funnel interpretation
Awareness: insight, problem recognition, founder perspective.
Consideration: frameworks, safety, buyer guides, parent confidence.
Proof: case studies, testimonials, real outcomes, process evidence.
Conversion: planner, consultation, resource, conversation.
Nurture: newsletters, follow-up content, deeper proof.

## Content quality question
Ask: "Could any generic school-tour company publish this unchanged?"
If yes, rewrite until it contains a distinct TMC point of view, verified proof, or school-specific usefulness.


---

Source: skills/tmc-core-context/references/claims-register-template.md

# TMC Claims Register Template

Maintain this outside the generation prompt as the authority for factual claims.

| Claim ID | Claim | Status | Source | Approved wording | Restrictions | Last verified |
|---|---|---|---|---|---|---|
| CLM-001 | Example only | VERIFY |  |  | Do not publish until approved |  |

## Status
- APPROVED: may be used exactly or conservatively paraphrased
- VERIFY: do not publish until checked
- RESTRICTED: only use in specified contexts
- PROHIBITED: do not use

## High-risk claim classes
Always verify:
- years in operation
- number of schools/students/trips
- safety records
- medical/emergency performance
- prices/packages
- visa/travel rules
- curriculum alignment claims
- measurable student outcomes
- school/client names
- testimonials
- parent feedback
- performance percentages
