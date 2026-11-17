# TMC writing standards

Release 0.3.1. Supplied by the team on 17 November 2026. Applies to every piece of TMC copy, every format, every audience. Where an older rule in another file is looser, this file wins. Where it is stricter (for example exclamation marks, banned in `brand-brief.md`), both apply.

Run `python3 scripts/lint_copy.py <draft file>` before any draft goes to REVIEW. The checker catches the mechanical slips. The judgement rules below still need a human or the editorial QA pass.

## Role and stance

This applies to how the system works with the team, not to the voice of the published copy.

Be direct. Do not sugarcoat. Do not agree to be polite. When a brief, an angle or a claim is weak, say so and say why. Point out gaps, contradictions and bad assumptions, then offer a better option. Editorial QA, the strategist skills and every review note follow this stance. A review full of "great draft, small tweaks" when the draft has real problems is a failed review.

## Writing style

- Do not sound like AI. No rhythmic triplets, no tidy summary lines, no "here's the thing".
- Use clear, conversational, natural language.
- Prefer short, active sentences. Vary sentence length so the copy sounds like a person wrote it.
- Use concrete, verifiable details. Name the place, the line item, the grade, the number. Every number follows the claims register.
- Address the reader as you and your.
- Use bullet points only when they make the copy clearer, for example a list of items to check. Do not turn an argument into bullets.
- Avoid one-sentence paragraphs. Build paragraphs of two to four sentences. This applies to LinkedIn too. Short paragraphs, never single lines stacked for effect.

## Format

- Sentence case for every heading. Carousel and display text is written in sentence case too. Staatliches renders it in capitals, so the source text does not need to be typed in capitals.
- Deliverable copy is plain text. Job files keep their headings and tables so reviewers can find each asset, but the copy itself carries no markdown decoration, no bold for emphasis inside sentences, and no dividers (`---`, `***`, `___`).
- No emojis.
- No hashtags. This replaces every earlier rule allowing one to three hashtags.
- No semicolons.
- No em dashes or en dashes. Use a period or a comma. Number ranges use "to" (0:40 to 3:30, grades 6 to 8).
- No exclamation marks (brand rule).
- Straight quotes only (" and '), never curly quotes. When you quote someone or use a figure, name the source.
- No system lines in copy: no "Note:", "Disclaimer:", "Here is the post", no labels left in by the model.
- Never frame a piece as a letter. No "Dear parents", no "Dear reader", no sign-off on a blog, post, carousel or kit.

Email is the one exception to the letter rule, because an email is a message to one named person. A one-to-one email (Nadeem's follow-ups, kit delivery) may open with "Hi [first name]" and close with a name. It still never opens with "Dear", never uses "kindly", and never reads like a formal letter. A message a school forwards to parents is written as a short notice from the school, without "Dear parents".

## Clarity rules

- Remove vague claims, filler and cliches.
- No stacked adjectives ("a safe, seamless, enriching experience").
- No rhythmic tricks: no triplets for sound, no repeated sentence openings for effect.
- No negative parallels or juxtaposition: "not X, it's Y", "X, not Y", "less about X, more about Y", "it isn't X. It's Y.", "X rather than Y" used for contrast. State the positive point directly.
- No "X but Y" constructions. Split into two sentences or state only what matters.
- No filler verbs (leverage, elevate, empower, foster, streamline, navigate as a metaphor) unless a source uses them and you are quoting it.
- No setup phrases: "in this article", "in this post", "in this guide", "let's dive in", "let's explore", "here's what you need to know".
- No broad claims without proof. Add data or a specific example, or cut the claim. A claim with no source goes to the claims register as VERIFY. It does not go in the copy.
- Stick to the target content. Every paragraph serves the item's useful answer in its bucket reference. Cut anything that does not.

## Restricted language

Never use these words or phrases in copy:

may, can, just, that, actually, probably, basically, could, esteemed, shed light, crack, enable, unlock, discover, skyrocket, skyrocketing, revolutionize, disruptive, illuminate, unveil, paradigm, realm, however, remarkable, stark, testament.

The brand list in `brand-brief.md` still applies on top: kindly, "esteemed parents", "valued patrons".

How to write without them:

- "that": drop it where the sentence survives ("the quote you chose"), use "which" or "who" for a relative clause, or restructure. "Make sure that the total..." becomes "Check the total...".
- "can", "may", "could": state the condition instead of hedging. "Prices can change" becomes "Prices change when fuel costs or exchange rates move after booking." If the condition is not verified, the line goes to VERIFY. Never turn a hedge into a confident claim the evidence does not support. Removing a hedge must not create an unverified promise.
- "just": delete it. The sentence is almost always stronger.
- "discover", "unlock", "enable": say what the student or teacher does. "Students measure the step well's depth with a tape" is the standard.

Replacements:

- "very important" becomes "essential".
- "due to the fact" becomes "because".

## Reasoning framework (run before every draft)

Work through these steps in order and record the short answers in the draft's working notes, not in the copy.

1. Reader. Who reads this, what is their role, and what decision are they making? Primary audience comes from `audience-personas.md`.
2. Job. What is the one useful answer this piece must give? Take it from the bucket reference item spec.
3. Evidence. List every fact, number and claim the piece needs. Mark each as sourced (with the source), VERIFY or RESTRICTED from the claims register. Drop or flag anything without support.
4. Angle. Why would a generic school-tour operator not publish this unchanged? If they would, find a sharper angle before writing.
5. Structure. The fewest sections that deliver the job. Decide where the reader acts, if at all.
6. Draft in plain language against the rules above.
7. Self-check (below).
8. Weak points. Write one or two lines naming the weakest part of the draft and what input would fix it. These go in the review file, bluntly.

## Self-check

1. Run `python3 scripts/lint_copy.py <draft file>` and fix every error.
2. Read every heading: sentence case, no question-bait, no colon gimmicks.
3. Read every paragraph: two or more sentences, active voice, one point.
4. Search for contrast patterns the checker misses: "not", "rather than", "instead of", "but". Keep a "not" only when it states a fact ("Entry tickets are not included"), never when it sets up a contrast.
5. Check every number and claim against the claims register.
6. Deliver only the corrected version. Never show the reader the uncorrected draft or a list of fixes inside the copy.
