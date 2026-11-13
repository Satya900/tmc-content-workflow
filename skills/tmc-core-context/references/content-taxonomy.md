# TMC Content Taxonomy

Every asset carries these fields where practical. MARKETING assets need all fields marked required. TOUR assets need the fields marked T.

| Field | Values | Required |
|---|---|---|
| content_id | `TMC-YYYYMMDD-<FORMAT>-NNN`. Formats: LI, FB, IG, CAR, BLOG, NEWS, CASE, LM (lead magnet), WA (WhatsApp), WEB, VID (script) | yes, T |
| master_idea_id | Shared ID across repurposed versions of one idea | if repurposed |
| content_category | TOUR, MARKETING | yes, T |
| target_audience | owner_trustee, management, principal, academic_coordinator, teacher (B2B: always a school role; parents and students are voices, recorded in `voice_source`) | yes, T |
| voice_source | Parent, student, teacher or educator whose words or work appear, with consent reference, or "none" | if voices used |
| school_segment | A, B, C (`audience-personas.md`) or unknown | if targeted |
| content_bucket | 1 to 7 (`content-buckets.md`). One primary only | yes, T |
| customer_emotion | fear, pain_point, problem, need, desire, fantasy + the specific item | yes |
| content_angle | One of the 33 angles (`marketing-template-framework.md`) | yes |
| funnel_stage | awareness, consideration, proof, conversion, nurture | yes |
| programme | day_trip, domestic_tour, international_tour, general | if relevant |
| objective | What this asset should cause | yes |
| topic | Working title | yes, T |
| hook | First line | yes |
| core_message | One sentence | yes |
| proof_required | Claim IDs from the claims register, or "none" | yes, T |
| claim_risk | low, medium, high | yes |
| delivery_type | infographic, carousel, text_post, blog, email, case_study, lead_magnet, video_script, photo_dump | yes, T |
| platform | linkedin_yasin, linkedin_company, instagram, facebook, email, blog, website, whatsapp, youtube, x | yes, T |
| account_voice | yasin, company | for LinkedIn |
| photo_requirement | Brief or "none" | yes, T |
| media_permission | APPROVED, DENIED, UNKNOWN, NOT_APPLICABLE per category | if media, T |
| CTA | One action and its verified destination, or "none" | yes |
| source_materials | Files, notes, URLs | yes, T |
| approval_status | Workflow state | yes, T |

## Funnel stages
- **Awareness:** insight, problem recognition, founder perspective. Usual buckets: 1, 6.
- **Consideration:** frameworks, safety and governance, buyer guides, parent confidence, curriculum fit. Usual buckets: 2, 3, 4, 7.
- **Proof:** case studies, testimonials, evidenced outcomes, process evidence. Usual bucket: 5.
- **Conversion:** planner, consultation, resource, conversation. Usual bucket: 7.
- **Nurture:** newsletters, follow-up content, deeper proof.

## Idea quality gate
Reject or rewrite an idea if any answer is yes:
1. Could any generic school-tour company publish this unchanged?
2. Is it only destination inspiration?
3. Does it lack a clear decision-maker (or, for TOUR, a real trip moment)?
4. Does it depend on an unsupported claim?
5. Is it purely promotional?
6. Does it speak to more than one primary audience?
7. Does it fit no bucket, or need two buckets to make sense?
8. Is it written to sell to parents or students (B2C) rather than to help a school role decide?
9. Does its CTA ask a family, rather than a school, to act?

If question 1 is yes, rewrite until the piece contains a distinct TMC point of view, verified proof, or school-specific usefulness.
