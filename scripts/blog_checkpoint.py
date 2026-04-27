#!/usr/bin/env python3
"""Load the latest blog-ingest checkpoint for blog triage."""

from __future__ import annotations

import json
import os
from pathlib import Path


def get_hermes_home() -> Path:
    hermes_home = os.environ.get("HERMES_HOME")
    if hermes_home:
        return Path(hermes_home)
    return Path.home() / ".hermes"


def build_candidates(checkpoint: dict) -> list[dict]:
    candidates = []
    for index, item in enumerate(checkpoint.get("saved_articles", []), start=1):
        url = item.get("url", "").strip()
        raw_path = item.get("raw_path")
        if not url or not raw_path:
            continue
        candidates.append({
            "item_id": f"blog-{index}",
            "source": "blog",
            "source_name": item.get("blog"),
            "title": item.get("title"),
            "url": url,
            "raw_path": raw_path,
        })
    return candidates


def main() -> int:
    checkpoint_path = get_hermes_home() / "cron" / "data" / "blog_ingest" / "latest.json"
    if not checkpoint_path.exists():
        print(json.dumps({
            "ok": False,
            "error": "blog-ingest checkpoint not found",
            "checkpoint_path": str(checkpoint_path),
        }, ensure_ascii=False, indent=2))
        return 0

    checkpoint = json.loads(checkpoint_path.read_text(encoding="utf-8"))
    payload = {
        "date": checkpoint.get("date"),
        "run_id": checkpoint.get("run_id"),
        "collected_at": checkpoint.get("collected_at"),
        "candidates": build_candidates(checkpoint),
        "unsaved_articles": checkpoint.get("unsaved_articles", []),
        "scan": checkpoint.get("scan", {}),
    }
    payload["_checkpoint"] = {
        "ok": True,
        "run_id": checkpoint.get("run_id"),
        "generated_at": checkpoint.get("collected_at"),
        "checkpoint_path": str(checkpoint_path),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
