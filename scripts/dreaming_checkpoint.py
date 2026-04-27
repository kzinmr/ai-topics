#!/usr/bin/env python3
"""Load the latest dreaming checkpoint for replay."""

from __future__ import annotations

import json
import os
from pathlib import Path


def get_hermes_home() -> Path:
    hermes_home = os.environ.get("HERMES_HOME")
    if hermes_home:
        return Path(hermes_home)
    return Path.home() / ".hermes"


def main() -> int:
    checkpoint_path = get_hermes_home() / "cron" / "data" / "dreaming" / "latest.json"
    if not checkpoint_path.exists():
        print(json.dumps({
            "ok": False,
            "error": "dreaming checkpoint not found",
            "checkpoint_path": str(checkpoint_path),
        }, ensure_ascii=False, indent=2))
        return 0

    checkpoint = json.loads(checkpoint_path.read_text(encoding="utf-8"))
    payload = checkpoint.get("payload", {})
    payload["_checkpoint"] = {
        "ok": True,
        "run_id": checkpoint.get("run_id"),
        "generated_at": checkpoint.get("generated_at"),
        "checkpoint_path": str(checkpoint_path),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
