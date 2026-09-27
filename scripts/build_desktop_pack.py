"""Build portable TMC project files and a native skill ZIP from one source set.

Uses only Python's standard library. No network, AI API or global installation.
Each run writes a fresh release folder, preserving existing releases.
"""
import argparse
import hashlib
import json
import re
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.1.0"
FORMAT_SKILLS = [
    "tmc-content-strategist", "tmc-linkedin", "tmc-marketing-carousel",
    "tmc-tour-photo-dump", "tmc-photo-selector", "tmc-blog", "tmc-newsletter",
    "tmc-case-study", "tmc-editorial-qa", "tmc-monthly-strategist",
]
CONTEXT_FILES = [
    "skills/tmc-core-context/references/tmc-brand-context.md",
    "brand-brief.md",
    "skills/tmc-core-context/references/marketing-template-framework.md",
    "skills/tmc-core-context/references/content-taxonomy.md",
    "skills/tmc-core-context/references/claims-register-template.md",
]


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8-sig")


def body(text):
    return re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, count=1, flags=re.S)


def contrast_on_white(hex_color):
    values = [int(hex_color[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    linear = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in values]
    luminance = sum(a * b for a, b in zip(linear, (0.2126, 0.7152, 0.0722)))
    return 1.05 / (luminance + 0.05)


def verify_vendor():
    records = json.loads(read("vendor/sources.lock.json"))
    for record in records:
        for filename, expected in record["files_sha256"].items():
            actual = hashlib.sha256((ROOT / filename).read_bytes()).hexdigest()
            if actual != expected:
                raise ValueError(f"Vendor source changed: {filename}")


def section(filename, content):
    return f"\n\n---\n\nSource: {filename}\n\n{content.strip()}\n"


def make_documents():
    context = f"# TMC Context\n\nPack version: {VERSION}\n\n"
    context += "Business positioning, visual brand and evidence rules. Historical mentions of video are deferred in this release. Source filenames below identify provenance; all their text is included here.\n"
    context += "\n## Visual clarification\n\n"
    context += (f"Computed sRGB contrast against white: Classroom Cyan #1AAFE0 = {contrast_on_white('1AAFE0'):.2f}:1; "
                f"Cyan Deep #0E7FA6 = {contrast_on_white('0E7FA6'):.2f}:1. "
                "These measured values supersede the source brief's approximate numerical claims. "
                "Do not assume cyan becomes legible simply because text is large. Check the actual foreground/background pair, especially on photo scrims. "
                "Use charcoal or black on light surfaces where contrast is insufficient. The brand's letter-spacing value has no unit specified; do not interpret it as 30-60 CSS pixels.\n")
    context += "".join(section(p, read(p)) for p in CONTEXT_FILES)
    formats = f"# TMC Formats\n\nPack version: {VERSION}\n\n"
    formats += "Read only the relevant sections. The extensions at the end adapt external guidance and add Facebook, static posts, document carousels and nurture sequences. Video is deferred. TMC_WORKFLOW.md controls job state, permissions and tool availability. Repository-relative paths in source sections are provenance; use this pack's context and workflow equivalents. No other skill installation is required.\n"
    for name in FORMAT_SKILLS:
        path = f"skills/{name}/SKILL.md"
        formats += section(path, body(read(path)))
    formats += section("system/FORMAT_EXTENSIONS.md", read("system/FORMAT_EXTENSIONS.md"))
    workflow = read("system/WORKFLOW.md")
    workflow += section("system/job-template.md", read("system/job-template.md"))
    workflow += section("system/SMOKE_TESTS.md", read("system/SMOKE_TESTS.md"))
    return {"TMC_CONTEXT.md": context, "TMC_FORMATS.md": formats, "TMC_WORKFLOW.md": workflow}


def validate_release(release):
    skill = release / "tmc-content-workflow"
    entry = (skill / "SKILL.md").read_text(encoding="utf-8")
    assert "name: tmc-content-workflow" in entry
    for target in re.findall(r"\]\(([^)]+)\)", entry):
        assert (skill / target).is_file(), f"Broken skill reference: {target}"
    for filename in ("TMC_CONTEXT.md", "TMC_FORMATS.md", "TMC_WORKFLOW.md"):
        assert (release / "project-files" / filename).read_bytes() == (skill / "references" / filename).read_bytes()
    for container in (release / "project-files", skill):
        assert (container / "licenses/coreyhaines31-MIT.txt").is_file()
        assert (container / "licenses/anthropic-Apache-2.0.txt").is_file()
    with zipfile.ZipFile(release / "tmc-content-workflow.zip") as archive:
        assert archive.testzip() is None
        assert "tmc-content-workflow/SKILL.md" in archive.namelist()
        assert all(p.startswith("tmc-content-workflow/") for p in archive.namelist())
        assert not any(p.endswith((".py", ".exe", ".ps1")) for p in archive.namelist())
    manifest = json.loads((release / "manifest.json").read_text(encoding="utf-8"))
    for name, digest in manifest["files_sha256"].items():
        assert hashlib.sha256((release / name).read_bytes()).hexdigest() == digest


def build(parent):
    verify_vendor()
    parent.mkdir(parents=True, exist_ok=True)
    release = Path(tempfile.mkdtemp(prefix=f"tmc-{VERSION}-", dir=parent))
    docs = make_documents()
    skill = release / "tmc-content-workflow"
    project = release / "project-files"

    def write(path, content):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")

    for filename, content in docs.items():
        write(project / filename, content)
        write(skill / "references" / filename, content)
    write(project / "PROJECT_INSTRUCTIONS.md", read("system/PROJECT_INSTRUCTIONS.md"))
    write(skill / "SKILL.md", read("system/SKILL.md"))
    write(skill / "assets/job-template.md", read("system/job-template.md"))
    for base in (skill, project):
        write(base / "THIRD_PARTY_NOTICES.md", read("THIRD_PARTY_NOTICES.md"))
        write(base / "licenses/coreyhaines31-MIT.txt", read("vendor/coreyhaines31/LICENSE"))
        write(base / "licenses/anthropic-Apache-2.0.txt", read("vendor/anthropic/marketing-LICENSE"))
        for notice in sorted((ROOT / "vendor/anthropic").glob("*NOTICE*")):
            write(base / "licenses" / notice.name, notice.read_text(encoding="utf-8"))
        for logo in sorted((ROOT / "logos").glob("*.png")):
            target = base / "assets" / logo.name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(logo.read_bytes())
    with zipfile.ZipFile(release / "tmc-content-workflow.zip", "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(skill.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(release).as_posix())
    write(release / "SETUP.md", read("docs/DESKTOP_SETUP.md"))
    write(release / "SKILL_RESEARCH.md", read("docs/SKILL_RESEARCH.md"))
    write(release / "sources.lock.json", read("vendor/sources.lock.json"))
    hashes = {p.relative_to(release).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted(release.rglob("*")) if p.is_file()}
    manifest = {"version": VERSION, "built_utc": datetime.now(timezone.utc).isoformat(),
                "app_validation": {"chatgpt": "NOT_RUN", "claude": "NOT_RUN"},
                "files_sha256": hashes}
    write(release / "manifest.json", json.dumps(manifest, indent=2) + "\n")
    validate_release(release)
    return release


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    release = build(args.output_dir.resolve())
    print(f"Built and validated: {release}")
    print("Matching project/native knowledge, license inclusion, links, ZIP integrity and file hashes passed.")
    print("Live ChatGPT and Claude acceptance tests: NOT RUN.")
