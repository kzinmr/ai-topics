#!/usr/bin/env python3
"""Collect unprocessed raw articles for the raw-backlog-ingest pipeline.

Picks N articles that haven't been triaged yet, cross-references against
the archive index for comparison context, and outputs JSON for the agent.

Usage:
    python3 scripts/raw_backlog_collect.py          # default: 5 articles, 500B+ min
    python3 scripts/raw_backlog_collect.py --count 10 --min-size 1000
    python3 scripts/raw_backlog_collect.py --dry-run  # don't update tracking
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path


HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
WIKI_ROOT = Path(os.environ.get("WIKI_ROOT", Path.home() / "ai-topics" / "wiki"))
RAW_ARTICLES = WIKI_ROOT / "raw" / "articles"
ARCHIVE_INDEX = WIKI_ROOT / "raw" / "archived" / "triage" / "archive_index.json"
TRACKING_FILE = HERMES_HOME / "processed_raw_articles.json"

DEFAULT_COUNT = 5
DEFAULT_MIN_SIZE = 500  # bytes
BODY_EXCERPT_LENGTH = 400


def load_tracking() -> dict:
    """Return {filename: {processed_at, status, ...}}."""
    if not TRACKING_FILE.exists():
        return {}
    try:
        return json.loads(TRACKING_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_tracking(data: dict) -> None:
    TRACKING_FILE.parent.mkdir(parents=True, exist_ok=True)
    TRACKING_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def load_archive_index() -> dict:
    """Return {url: archived_item_info} or {}."""
    if not ARCHIVE_INDEX.exists():
        return {"urls": []}
    try:
        return json.loads(ARCHIVE_INDEX.read_text(encoding="utf-8"))
    except Exception:
        return {"urls": []}


def extract_url_from_article(path: Path) -> str | None:
    """Try to extract the canonical URL from a raw article's frontmatter."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        for line in text.split("\n")[:30]:
            line = line.strip()
            if line.startswith("url:") or line.startswith("**URL:**"):
                url = line.split(":", 1)[1].strip().strip('"').strip("'")
                if url.startswith("http"):
                    return url
            if line.startswith("- **Source:**"):
                # Format: - **Source:** [text](url) or - **Source:** url
                import re
                match = re.search(r"\(?(https?://[^\s\)]+)\)?", line)
                if match:
                    return match.group(1)
    except Exception:
        pass
    return None


def extract_body_excerpt(path: Path, length: int = BODY_EXCERPT_LENGTH) -> str:
    """Extract opening body text from a raw article file."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.split("\n")
        in_frontmatter = False
        body_lines = []
        for line in lines:
            stripped = line.strip()
            if stripped == "---" and not in_frontmatter:
                in_frontmatter = True
                continue
            if stripped == "---" and in_frontmatter:
                in_frontmatter = False
                continue
            if in_frontmatter:
                continue
            if stripped:
                body_lines.append(line)
                if sum(len(l) for l in body_lines) >= length:
                    break
        result = "\n".join(body_lines)[:length]
        # Clean up common scraper noise
        result = result.replace("\n\n", "\n").strip()
        return result
    except Exception:
        return ""


def get_article_hash(path: Path) -> str:
    """Content-based hash for dedup (first 8KB)."""
    try:
        return hashlib.md5(path.read_bytes()[:8192]).hexdigest()[:12]
    except Exception:
        return path.name[:12]


def collect(args: list[str]) -> dict:
    """Main collection logic. Returns JSON-serializable result."""
    count = DEFAULT_COUNT
    min_size = DEFAULT_MIN_SIZE
    dry_run = False

    for a in args:
        if a == "--dry-run":
            dry_run = True
        elif a.startswith("--count="):
            count = int(a.split("=")[1])
        elif a == "--count":
            pass  # handled below
        elif a.startswith("--min-size="):
            min_size = int(a.split("=")[1])

    # Parse --count N (positional after flag)
    i = 0
    while i < len(args):
        if args[i] == "--count" and i + 1 < len(args):
            count = int(args[i + 1])
            break
        i += 1

    # 1. Load tracking data
    tracking = load_tracking()
    processed_filenames = set(tracking.keys())

    # 2. Load archive index for cross-reference
    archive = load_archive_index()
    archived_urls = set(archive.get("urls", []))

    # 3. List raw articles, filter unprocessed — pre-compute mtime
    now_ts = datetime.now(timezone.utc).timestamp()
    all_articles = []
    for f in RAW_ARTICLES.iterdir():
        if not f.is_file() or not f.name.endswith(".md"):
            continue
        st = f.stat()
        size = st.st_size
        if size < min_size:
            continue
        mtime = st.st_mtime
        all_articles.append((f.name, size, f, mtime))

    # Parse --sort flag
    sort_mode = "size"  # default
    for a in args:
        if a.startswith("--sort="):
            sort_mode = a.split("=")[1]

    # Sort based on mode
    if sort_mode == "recent":
        all_articles.sort(key=lambda x: (-x[3], -x[1]))  # x[3] = mtime
    elif sort_mode == "ai-hint":
        ai_terms = ["agent", "llm", "gpt", "claude", "openai", "ai-", "model",
                     "deepseek", "anthropic", "mistral", "gemini", "huggingface",
                     "transformer", "fine-tun", "rag", "prompt", "inference",
                     "coding-agent", "harness", "language-model", "rlhf"]
        def ai_score(item):
            name = item[0].lower()
            return sum(1 for t in ai_terms if t in name)
        all_articles.sort(key=lambda x: (-ai_score(x), -x[3], -x[1]))  # x[3] = mtime
    else:
        all_articles.sort(key=lambda x: (-x[1], x[0]))

    # Filter: exclude already processed (skip "processing" stuck >1hr)
    candidates = []
    for name, size, path, mtime in all_articles:
        if name in processed_filenames:
            entry = tracking[name]
            status = entry.get("status", "")
            if status == "processing":
                # Check if stuck
                collected_at = entry.get("collected_at", "")
                if collected_at:
                    try:
                        ts = datetime.fromisoformat(collected_at).timestamp()
                        if now_ts - ts > 3600:  # 1 hour timeout
                            pass  # fall through: re-collect
                        else:
                            continue  # still processing, skip
                    except Exception:
                        continue
                else:
                    continue
            elif status in ("done", "skipped", "error"):
                continue  # already finished
            else:
                continue  # unknown status, skip
        candidates.append((name, size, path, mtime))

    # 4. Select top-N candidates
    selected = candidates[:count]

    # 5. Build output
    output = {
        "collect_run_id": datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"),
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "total_raw_articles": len(all_articles),
        "already_processed": len(processed_filenames),
        "archived_urls_count": len(archived_urls),
        "candidates_selected": len(selected),
        "candidates_remaining": len(candidates) - len(selected),
        "articles": [],
    }

    for name, size, path, mtime in selected:
        url = extract_url_from_article(path)
        body_excerpt = extract_body_excerpt(path)
        content_hash = get_article_hash(path)

        # Cross-reference with archive
        archive_status = None
        if url and url in archived_urls:
            archive_status = "already_archived"
        elif url:
            archive_status = "not_archived"

        article_info = {
            "filename": name,
            "raw_path": str(path),
            "size_bytes": size,
            "url": url,
            "content_hash": content_hash,
            "archive_status": archive_status,
            "body_excerpt": body_excerpt,
        }
        output["articles"].append(article_info)

        # Mark as "processing" in tracking (unless dry-run)
        if not dry_run:
            tracking[name] = {
                "status": "processing",
                "collected_at": datetime.now(timezone.utc).isoformat(),
                "size_bytes": size,
                "url": url,
            }

    if not dry_run:
        save_tracking(tracking)

    return output


def main() -> int:
    output = collect(sys.argv[1:])
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
