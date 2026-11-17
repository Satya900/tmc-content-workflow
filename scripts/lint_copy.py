"""Check TMC draft copy against skills/tmc-core-context/references/writing-standards.md.

Uses only Python's standard library. Catches the mechanical slips: restricted
words, banned punctuation, emojis, hashtags, curly quotes, dividers, setup
phrases and letter framing (errors), plus contrast patterns, title-case
headings and one-sentence paragraphs (warnings). Judgement rules still need
editorial QA.

Ignored: YAML front matter, inline code, square-bracket placeholders such as
[NEEDS INPUT: ...], table separator rows, and any region between
<!-- lint: off --> and <!-- lint: on -->.

Exit status is 1 when any error is found.
"""
import argparse
import re
import sys
from pathlib import Path

RESTRICTED = [
    "may", "can", "just", "that", "actually", "probably", "basically", "could",
    "esteemed", "shed light", "crack", "enable", "unlock", "discover",
    "skyrocket", "skyrocketing", "revolutionize", "disruptive", "illuminate",
    "unveil", "paradigm", "realm", "however", "remarkable", "stark", "testament",
    "kindly", "valued patrons",
]
RESTRICTED_RE = re.compile(r"\b(" + "|".join(re.escape(w) for w in RESTRICTED) + r")\b", re.I)
PHRASES = {
    r"\bin this (article|post|guide|blog|piece|video)\b": "setup phrase",
    r"\blet'?s (dive|explore|take a look)\b": "setup phrase",
    r"\bhere'?s what you need to know\b": "setup phrase",
    r"\bvery important\b": 'use "essential"',
    r"\bdue to the fact\b": 'use "because"',
    r"^\s*dear\b": "letter framing",
}
EMOJI_RE = re.compile("[\U0001F000-\U0001FAFF☀-➿⬀-⯿️]")
PUNCTUATION = {
    "—": "em dash", "–": "en dash", ";": "semicolon",
    "“": "curly quote", "”": "curly quote", "‘": "curly quote", "’": "curly quote",
}
CONTRAST = [
    r"\bnot\b[^.]{0,60},\s*(but|it'?s|it is)\b",
    r"\b(isn'?t|is not|aren'?t|are not)\b[^.]{0,60}\.\s+(it'?s|they'?re|it is)\b",
    r",\s+not\s+(a|an|the)?\s*[\w-]+[.,]",
    r"\brather than\b",
    r"\bless about\b.*\bmore about\b",
    r"\bbut\b",
]
LABEL_RE = re.compile(r"^\s*(\*\*[^*]+:\*\*|[A-Z][\w ()/-]{0,40}:\s)")


def clean(line):
    line = re.sub(r"`[^`]*`", "", line)
    return re.sub(r"\[[^\]]*\]", "", line)


def copy_lines(text):
    lines = text.splitlines()
    start, active = 0, True
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                start = i + 1
                break
    for number, line in enumerate(lines[start:], start + 1):
        if "<!-- lint: off -->" in line:
            active = False
        elif "<!-- lint: on -->" in line:
            active = True
        elif active:
            yield number, line


def check(text):
    findings = []

    def add(number, level, message):
        findings.append((number, level, message))

    paragraph = []

    def close_paragraph():
        if paragraph:
            joined = " ".join(clean(l) for _, l in paragraph).strip()
            sentences = [s for s in re.split(r"(?<=[.?])\s+", joined) if s.strip()]
            if len(sentences) == 1 and len(joined.split()) > 3 and not LABEL_RE.match(paragraph[0][1]):
                add(paragraph[0][0], "WARN", "one-sentence paragraph")
            paragraph.clear()

    for number, raw in copy_lines(text):
        stripped = raw.strip()
        if re.fullmatch(r"\|?[\s:|-]+\|?", stripped) and "|" in stripped:
            continue
        if re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", stripped):
            add(number, "ERROR", "markdown divider")
            close_paragraph()
            continue
        line = clean(raw)
        for word in RESTRICTED_RE.findall(line):
            add(number, "ERROR", f'restricted word "{word.lower()}"')
        for pattern, label in PHRASES.items():
            if re.search(pattern, line, re.I):
                add(number, "ERROR", label)
        for char, label in PUNCTUATION.items():
            if char in line:
                add(number, "ERROR", label)
        if re.search(r"!(?!\[)", line):
            add(number, "ERROR", "exclamation mark")
        if EMOJI_RE.search(line):
            add(number, "ERROR", "emoji")
        if re.search(r"(?<![\w&/#])#[A-Za-z]\w*", line):
            add(number, "ERROR", "hashtag")
        for pattern in CONTRAST:
            if re.search(pattern, line, re.I):
                add(number, "WARN", "contrast pattern (X not Y, X but Y, rather than)")
                break
        heading = re.match(r"^#{1,6}\s+(.*)", stripped)
        if heading:
            close_paragraph()
            words = re.findall(r"[A-Za-z][\w'-]*", heading.group(1))[1:]
            capped = [w for w in words if w[0].isupper() and not w.isupper()]
            if len(words) >= 3 and len(capped) * 2 > len(words):
                add(number, "WARN", "heading not in sentence case")
            continue
        if not stripped or stripped.startswith(("|", "-", "*", "+", ">")) or re.match(r"\d+\.\s", stripped):
            close_paragraph()
            continue
        paragraph.append((number, raw))
    close_paragraph()
    return sorted(findings)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--errors-only", action="store_true")
    args = parser.parse_args()
    errors = 0
    for path in args.files:
        for number, level, message in check(path.read_text(encoding="utf-8")):
            if level == "ERROR":
                errors += 1
            elif args.errors_only:
                continue
            print(f"{path}:{number}: {level} {message}")
    print(f"{errors} error(s)", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
