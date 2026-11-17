---
name: tmc-social-post
description: Use this skill whenever the user asks for a TMC Instagram post or caption, single-image post, infographic, quote card, poll or question post, Facebook post or adaptation, WhatsApp broadcast or status message, Google Business Profile post, X post, or a short social adaptation of an existing TMC asset. Use tmc-linkedin for LinkedIn and tmc-marketing-carousel for multi-slide carousels.
---

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
