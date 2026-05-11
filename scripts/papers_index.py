#!/usr/bin/env python3
"""
Paper deduplication checker and index builder for wiki/raw/papers/.

Two modes:
  --build   : Scan all paper files and rebuild the index
  --check   : Check if a given URL/arxiv ID already has a paper file
  --add     : Register a new paper in the index

The index maps canonical identifiers (arXiv ID or normalized URL) to filenames.
Before saving a new paper, run `--check` to detect duplicates.
"""

import json, os, re, sys
from pathlib import Path

INDEX_PATH = Path("/opt/data/ai-topics/wiki/raw/papers/.papers_index.json")
PAPERS_DIR = Path("/opt/data/ai-topics/wiki/raw/papers")

# --- ID extraction ---

ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})(?:v\d+)?", re.IGNORECASE)
ARXIV_FILENAME_RE = re.compile(r"(\d{4}\.\d{4,5})")
HF_RE = re.compile(r"huggingface\.co/papers/([^/\s]+)")
OPENREVIEW_RE = re.compile(r"openreview\.net/(?:forum\?id=|pdf\?id=)([^\s&]+)")

def extract_identifier_from_frontmatter(filepath: Path) -> list[str]:
    """Extract identifiers from a paper file's frontmatter and body."""
    try:
        text = filepath.read_text(encoding="utf-8")
    except Exception:
        return []

    ids = set()

    # Check for URL in frontmatter
    for m in re.finditer(r"url:\s*(https?://[^\s\n]+)", text[:2000]):
        url = m.group(1)
        ids.add(normalize_url(url))

    # Check for URL in body
    for m in re.finditer(r"https?://[^\s)]+", text):
        url = m.group(0)
        if any(domain in url for domain in ["arxiv.org", "openreview.net", "huggingface.co/papers"]) or "arXiv:" in url:
            ids.add(normalize_url(url))

    # Check for plain arXiv ID mentions (no URL)
    for m in re.finditer(r"arXiv:(\d{4}\.\d{4,5})", text[:2000]):
        ids.add(f"arxiv:{m.group(1)}")

    return list(ids)

def normalize_url(url: str) -> str:
    """Normalize a paper URL to a canonical identifier."""
    # arXiv ID embedded in URL
    m = re.search(r"arxiv\.org/(?:abs|pdf|html)/(\d{4}\.\d{4,5})", url, re.IGNORECASE)
    if m:
        return f"arxiv:{m.group(1)}"

    # Plain "arXiv:XXXX.XXXXX" format
    m = re.search(r"(?:^|\s|arXiv:)(\d{4}\.\d{4,5})", url, re.IGNORECASE)
    if m:
        return f"arxiv:{m.group(1)}"

    # HuggingFace papers
    m = HF_RE.search(url)
    if m:
        return f"hf:{m.group(1)}"

    # OpenReview
    m = OPENREVIEW_RE.search(url)
    if m:
        return f"openreview:{m.group(1)}"

    # Fallback: strip trailing slashes and fragments
    return url.rstrip("/").split("#")[0]

def extract_id_from_filename(filename: str) -> str | None:
    """Try to extract arXiv ID from filename (e.g., 2512.24601 from '2025-12-31_2512.24601_...')."""
    m = ARXIV_FILENAME_RE.search(filename)
    if m:
        return f"arxiv:{m.group(1)}"
    return None

# --- Index management ---

def load_index() -> dict:
    if INDEX_PATH.exists():
        try:
            return json.loads(INDEX_PATH.read_text())
        except json.JSONDecodeError:
            print(f"Warning: corrupt index at {INDEX_PATH}, rebuilding...", file=sys.stderr)
    return {}

def save_index(index: dict):
    INDEX_PATH.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n")

def build_index():
    """Scan all paper files and rebuild the index."""
    index: dict[str, str] = {}  # identifier -> filename
    conflicts = []

    for f in sorted(PAPERS_DIR.glob("*.md")):
        if f.name.startswith("."):
            continue

        found_ids = set()

        # From filename
        fid = extract_id_from_filename(f.name)
        if fid:
            found_ids.add(fid)

        # From frontmatter
        for id_ in extract_identifier_from_frontmatter(f):
            found_ids.add(id_)

        if not found_ids:
            print(f"  [WARN] No identifier found for: {f.name}")
            continue

        for id_ in found_ids:
            if id_ in index:
                conflicts.append((id_, index[id_], f.name))
            else:
                index[id_] = f.name

    if conflicts:
        print(f"  [WARN] {len(conflicts)} identifier conflict(s) found:")
        for id_, old, new in conflicts:
            print(f"    {id_}: {old}  <->  {new}")

    save_index(index)
    print(f"  Index built: {len(index)} papers indexed")
    return index

def check_paper(url_or_id: str) -> dict | None:
    """Check if a paper already exists. Returns {id, filename} or None."""
    index = load_index()
    key = normalize_url(url_or_id)

    if key in index:
        return {"id": key, "filename": index[key]}

    # Also try arXiv ID extraction from filename pattern
    if "/" not in url_or_id and not url_or_id.startswith("http"):
        # Might be a raw arXiv ID like "2512.24601"
        key2 = f"arxiv:{url_or_id}"
        if key2 in index:
            return {"id": key2, "filename": index[key2]}

    return None

def add_paper(filename: str, url: str):
    """Register a new paper in the index."""
    index = load_index()
    key = normalize_url(url)
    if key in index:
        print(f"  [WARN] Paper already indexed: {key} -> {index[key]}")
        return False
    index[key] = filename
    save_index(index)
    print(f"  Added: {key} -> {filename}")
    return True

# --- CLI ---

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: papers_index.py --build | --check <url|id> | --add <filename> <url>")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "--build":
        print("Building papers index...")
        build_index()

    elif cmd == "--check":
        if len(sys.argv) < 3:
            print("Usage: papers_index.py --check <url|arxiv-id>")
            sys.exit(1)
        result = check_paper(sys.argv[2])
        if result:
            print(f"DUPLICATE: {result['id']} -> {result['filename']}")
            sys.exit(1)
        else:
            print("OK: No duplicate found")
            sys.exit(0)

    elif cmd == "--add":
        if len(sys.argv) < 4:
            print("Usage: papers_index.py --add <filename> <url>")
            sys.exit(1)
        add_paper(sys.argv[2], sys.argv[3])

    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
