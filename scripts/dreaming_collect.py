#!/usr/bin/env python3
"""Collect and checkpoint dreaming input for later processing."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def get_hermes_home() -> Path:
    hermes_home = os.environ.get("HERMES_HOME")
    if hermes_home:
        return Path(hermes_home)
    return Path.home() / ".hermes"


def main() -> int:
    hermes_home = get_hermes_home()
    profile_root = hermes_home.parent
    ai_topics_repo = Path(os.environ.get("AI_TOPICS_REPO", str(profile_root / "ai-topics")))
    checkpoint_dir = hermes_home / "cron" / "data" / "dreaming"
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    source_script = ai_topics_repo / "scripts" / "dreaming.py"
    proc = subprocess.run(
        [sys.executable, str(source_script)],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if proc.stderr:
        print(proc.stderr, file=sys.stderr, end="")
    if proc.returncode != 0:
        print(json.dumps({
            "ok": False,
            "error": f"dreaming.py exited with code {proc.returncode}",
            "script": str(source_script),
        }, ensure_ascii=False))
        return 0

    payload = json.loads(proc.stdout)
    generated_at = datetime.now(timezone.utc).isoformat()
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    archive_path = checkpoint_dir / f"dreaming_checkpoint_{run_id}.json"
    latest_path = checkpoint_dir / "latest.json"

    checkpoint = {
        "run_id": run_id,
        "generated_at": generated_at,
        "source_script": str(source_script),
        "payload": payload,
    }
    archive_path.write_text(json.dumps(checkpoint, ensure_ascii=False, indent=2), encoding="utf-8")
    latest_path.write_text(json.dumps(checkpoint, ensure_ascii=False, indent=2), encoding="utf-8")

    summary = {
        "ok": True,
        "run_id": run_id,
        "generated_at": generated_at,
        "checkpoint_path": str(latest_path),
        "archive_path": str(archive_path),
        "collected_articles": payload.get("collected_articles", payload.get("total_articles")),
        "triage_articles": payload.get("total_articles"),
        "filtered_out_articles": payload.get("filtered_out_articles", 0),
        "truncated": payload.get("truncated", False),
        "existing_wiki_pages_count": payload.get("existing_wiki_pages_count", 0),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
