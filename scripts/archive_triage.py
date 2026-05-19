#!/usr/bin/env python3
"""Archive triage decisions (skip/reference items) to wiki/raw/archived/triage/.

Reads triage_latest.json from blog/newsletter/dreaming pipelines and saves
skip+reference decisions to the archive, preserving article body excerpts.

Usage:
    python3 scripts/archive_triage.py blog       # archive latest blog triage
    python3 scripts/archive_triage.py newsletter  # archive latest newsletter triage
    python3 scripts/archive_triage.py dreaming    # archive latest dreaming triage
    python3 scripts/archive_triage.py --all       # archive all three
    python3 scripts/archive_triage.py blog --keep-reference  # also archive reference items
"""

from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path


HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
WIKI_ROOT = Path(os.environ.get("WIKI_ROOT", Path.home() / "ai-topics" / "wiki"))
ARCHIVE_ROOT = WIKI_ROOT / "raw" / "archived" / "triage"
ARCHIVE_INDEX = ARCHIVE_ROOT / "archive_index.json"

# Pipeline → (triage_job_id, checkpoint_dir, archive_subdir)
PIPELINES = {
    "blog": {
        "triage_job_id": "58c2f4a7e1bd",
        "checkpoint_dir": HERMES_HOME / "cron" / "data" / "blog_ingest",
        "subdir": "blog",
    },
    "newsletter": {
        "triage_job_id": "4e8b0d92c6a1",
        "checkpoint_dir": HERMES_HOME / "cron" / "data" / "newsletter",
        "subdir": "newsletter",
    },
    "dreaming": {
        "triage_job_id": "c4a9e8d2f671",
        "checkpoint_dir": HERMES_HOME / "cron" / "data" / "dreaming",
        "subdir": "dreaming",
    },
}

BODY_EXCERPT_LENGTH = 300  # chars from article body opening


def load_archive_index() -> set[str]:
    """Return set of archived URLs for dedup."""
    if not ARCHIVE_INDEX.exists():
        return set()
    try:
        data = json.loads(ARCHIVE_INDEX.read_text(encoding="utf-8"))
        return set(data.get("urls", []))
    except Exception:
        return set()


def save_archive_index(urls: set[str]) -> None:
    ARCHIVE_INDEX.write_text(
        json.dumps({"urls": sorted(urls), "updated": datetime.now(timezone.utc).isoformat()},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def extract_body_excerpt(raw_path: str, length: int = BODY_EXCERPT_LENGTH) -> str:
    """Extract opening body text from a raw article file."""
    p = Path(raw_path)
    if not p.exists():
        return ""

    try:
        text = p.read_text(encoding="utf-8", errors="replace")
        # Skip YAML frontmatter if present
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
            if stripped:  # non-empty lines for body
                body_lines.append(line)
                if sum(len(l) for l in body_lines) >= length:
                    break
        return "\n".join(body_lines)[:length]
    except Exception:
        return ""


def archive_pipeline(pipeline: str, keep_reference: bool = False) -> dict:
    """Archive skip (and optionally reference) decisions from a pipeline."""
    cfg = PIPELINES[pipeline]
    triage_path = cfg["checkpoint_dir"] / "triage_latest.json"

    if not triage_path.exists():
        return {"ok": False, "error": f"triage_latest.json not found at {triage_path}"}

    try:
        triage = json.loads(triage_path.read_text(encoding="utf-8"))
    except Exception as e:
        return {"ok": False, "error": f"Failed to parse triage JSON: {e}"}

    decisions = triage.get("decisions", [])
    if not decisions:
        return {"ok": True, "message": "No decisions in triage output", "archived": 0}

    # Filter: keep skip + optionally reference
    actions = {"skip"}
    if keep_reference:
        actions.add("reference")

    to_archive = [d for d in decisions if d.get("recommended_action") in actions]

    if not to_archive:
        return {"ok": True, "message": "No skip/reference items to archive", "archived": 0}

    # Dedup against archive index
    archive_index = load_archive_index()
    new_items = []
    for d in to_archive:
        url = d.get("url", "")
        if url and url in archive_index:
            continue
        if url:
            archive_index.add(url)
        # Add body excerpt
        raw_path = d.get("raw_path", "")
        if raw_path:
            d["body_excerpt"] = extract_body_excerpt(raw_path)
        new_items.append(d)

    if not new_items:
        return {"ok": True, "message": "All items already archived (dedup)", "archived": 0}

    # Build archive payload
    run_id = triage.get("checkpoint_run_id", datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"))
    archive_payload = {
        "archived_at": datetime.now(timezone.utc).isoformat(),
        "triage_run_id": run_id,
        "source": pipeline,
        "summary_ja": triage.get("summary_ja", ""),
        "decisions": new_items,
    }

    # Save to archive file
    archive_dir = ARCHIVE_ROOT / cfg["subdir"]
    archive_dir.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    archive_path = archive_dir / f"{date_str}_{run_id}.json"
    archive_path.write_text(json.dumps(archive_payload, ensure_ascii=False, indent=2), encoding="utf-8")

    # Update index
    save_archive_index(archive_index)

    return {
        "ok": True,
        "pipeline": pipeline,
        "candidates": len(to_archive),
        "new_archived": len(new_items),
        "dedup_skipped": len(to_archive) - len(new_items),
        "archive_path": str(archive_path),
        "total_archive_urls": len(archive_index),
    }


def main() -> int:
    targets = []
    keep_reference = False
    args = sys.argv[1:]

    if "--keep-reference" in args:
        keep_reference = True
        args.remove("--keep-reference")

    if "--all" in args:
        targets = list(PIPELINES.keys())
    elif args:
        targets = [a for a in args if a in PIPELINES]
        unknown = [a for a in args if a not in PIPELINES and not a.startswith("--")]
        if unknown:
            print(f"Unknown pipelines: {unknown}. Valid: {list(PIPELINES.keys())}", file=sys.stderr)
            return 1
    else:
        print("Usage: archive_triage.py [--all] [--keep-reference] <pipeline> [...]", file=sys.stderr)
        return 1

    results = {}
    for t in targets:
        result = archive_pipeline(t, keep_reference=keep_reference)
        results[t] = result

    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
