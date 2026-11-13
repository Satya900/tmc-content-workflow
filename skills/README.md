# TMC Claude Skills Pack

Purpose: make Claude follow The Modern Classroom (TMC) strategy consistently across content planning, marketing carousels, tour photo dumps, LinkedIn, social posts, blogs, newsletters, lead magnets, video scripts, case studies, image selection, QA and monthly recommendations.

## Source documents
The skills are built from three TMC documents (provenance and open decisions in `../docs/SOURCE_DOCUMENTS.md`):
- **TMC content marketing approval brief** (v1, 15 October 2026): objective, positioning, audience roles and the seven content buckets.
- **Understanding The Modern Classroom**: mission, vision, personas, needs and emotions, buyer questions, keywords, school segments, programmes, SEL values, posting schedule and metrics.
- **Content Generation workbook**: the 4D content strategy process, 33 content angles, delivery templates (infographics, blogs, video, case studies, lead magnets, email) and channel playbooks.

## Recommended installation
Copy the skill folders into the skills directory used by your Claude environment. Each skill has a `SKILL.md`. For desktop apps, use the compiled pack in `../dist/` instead (see `../docs/DESKTOP_SETUP.md`).

## Operating model
- TMC strategy is the source of truth. The approval brief governs positioning, audience and buckets.
- The Marketing Template (4D process) provides the content-generation mechanics.
- External SEO and marketing skills may assist research and editing but never override TMC rules or facts.
- Human review is mandatory before publishing.
- Never invent TMC claims, student outcomes, safety records, prices, testimonials, school permissions or trip facts.

## Skill order
1. `tmc-core-context` (always)
2. `tmc-content-strategist` (ideas, calendars)
3. Format skill: `tmc-linkedin`, `tmc-social-post`, `tmc-marketing-carousel`, `tmc-tour-photo-dump`, `tmc-blog`, `tmc-newsletter`, `tmc-lead-magnet`, `tmc-case-study`, `tmc-reel`
4. `tmc-photo-selector` where images are needed
5. `tmc-editorial-qa` (final gate)
6. `tmc-monthly-strategist` for performance-led planning

`tmc-carousel-pipeline` is an optional adapter for an open-carrusel installation.

## Pipeline at a glance
```
Brief or source material
  -> core context (positioning, bucket, persona)
  -> strategist: 4D (Determine audience, Define bucket, Decode emotion, Develop angle) + quality gate
  -> format skill drafts the asset (+ photo selector for visuals)
  -> editorial QA (PASS / REVISE / BLOCK)
  -> human review and approval of a named version
  -> render / export -> manual publication -> monthly review -> next calendar
```

## Content categories
### Tour content
Real TMC trip documentation. Experience-led. Photos determine the story. Usually bucket 5.

### Marketing content
Positioning and qualified school conversations. Strategy determines the story. Approved tour photos support it.

## Audience
- Decision-makers: school owners, trustees, management, principals
- Influencers: academic coordinators, HODs, teachers
- Voices: parents and students

## Seven content buckets (one primary per asset)
1. Experiential learning and SEL
2. Safety, governance and parent confidence
3. Educators and partnerships
4. Curriculum integration and pedagogy
5. Evidence of learning and stories from the road
6. Leadership and vision (Yasin)
7. School programme planning and decisions

## Core context references
| File | Holds |
|---|---|
| `tmc-brand-context.md` | Business, mission, vision, positioning, objective, audience roles, programmes, SEL values, voice, internal targets |
| `content-buckets.md` | The seven buckets with boundaries, evidence rules, and the mapping from earlier themes |
| `audience-personas.md` | Demographic and psychographic profiles, needs and emotions, buyer questions, keywords, school segments |
| `content-strategy-workbook.md` | The workbook's exercises answered for TMC as B2B: customer focus, buying committee, personas, bucket research, needs and emotions for all seven buckets, channel roles |
| `topic-bank.md` | Three worked 33-angle topic sets, 15 blog titles, interview guests, testimonial questions, lead magnets per bucket, calendar sample |
| `marketing-template-framework.md` | Content marketing principles, the 4D process, the 33 angles with TMC examples |
| `content-generation-playbook.md` | Delivery templates and channel playbooks |
| `content-taxonomy.md` | Asset fields, funnel stages, idea quality gate |
| `measurement-and-calendar.md` | Cadence, calendar columns, metrics, KPIs |
| `claims-register-template.md` | Claim statuses and seeded VERIFY rows |
