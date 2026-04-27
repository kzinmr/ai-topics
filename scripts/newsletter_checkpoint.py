#!/usr/bin/env python3
"""Load the latest newsletter-ingest checkpoint for triage."""

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
    for message in checkpoint.get("processed_messages", []):
        raw_path = message.get("raw_path")
        if not raw_path:
            continue
        for index, article in enumerate(message.get("articles", []), start=1):
            url = article.get("url", "").strip()
            if not url:
                continue
            candidates.append({
                "item_id": f"{message.get('message_id', 'message')}-{index}",
                "source": "newsletter",
                "source_name": message.get("subject"),
                "title": article.get("title") or message.get("subject"),
                "url": url,
                "raw_path": raw_path,
                "message_id": message.get("message_id"),
                "date": message.get("date"),
            })
    return candidates


def main() -> int:
    checkpoint_path = get_hermes_home() / "cron" / "data" / "newsletter" / "latest.json"
    if not checkpoint_path.exists():
        print(json.dumps({
            "ok": False,
            "error": "newsletter checkpoint not found",
            "checkpoint_path": str(checkpoint_path),
        }, ensure_ascii=False, indent=2))
        return 0

    checkpoint = json.loads(checkpoint_path.read_text(encoding="utf-8"))
    payload = {
        "run_id": checkpoint.get("run_id"),
        "collected_at": checkpoint.get("collected_at"),
        "processed_count": checkpoint.get("processed_count", 0),
        "candidates": build_candidates(checkpoint),
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
