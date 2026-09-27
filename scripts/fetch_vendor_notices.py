"""Fetch notices for pinned, already downloaded skills; never execute vendor code."""
import base64
import hashlib
import json
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ("coreyhaines31", "coreyhaines31/marketingskills", "5b2c0007766c6a1cf1d53fd8fc73e979e0821022", ["LICENSE"], ["social", "copy-editing"]),
    ("anthropic", "anthropics/knowledge-work-plugins", "bdf7160f2b33598fb0cb3860027e033cbaec7ce6", ["marketing/LICENSE", "marketing/CONNECTORS.md"], ["content-creation", "email-sequence"]),
]


def get_json(url):
    with urlopen(Request(url, headers={"User-Agent": "TMC-skill-source-review"}), timeout=30) as response:
        return json.load(response)


def main():
    records = []
    for owner, repo, commit, extra_paths, skills in SOURCES:
        tree = get_json(f"https://api.github.com/repos/{repo}/git/trees/{commit}?recursive=1")
        paths = {item["path"] for item in tree["tree"] if item["type"] == "blob"}
        notices = [p for p in ("NOTICE", "marketing/NOTICE") if p in paths]
        for source_path in extra_paths + notices:
            data = get_json(f"https://api.github.com/repos/{repo}/contents/{source_path}?ref={commit}")
            payload = base64.b64decode(data["content"])
            filename = source_path.replace("/", "-")
            destination = ROOT / "vendor" / owner / filename
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(payload)
        hashes = {}
        for path in sorted((ROOT / "vendor" / owner).rglob("*")):
            if path.is_file():
                hashes[path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
        records.append({"repository": repo, "commit": commit, "skills": skills,
                        "retrieved_on": "2026-09-17", "files_sha256": hashes})
    (ROOT / "vendor" / "sources.lock.json").write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
    print("Saved licenses, connector reference, and pinned source hashes for four skills.")


if __name__ == "__main__":
    main()
