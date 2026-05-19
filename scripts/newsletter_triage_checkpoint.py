#!/usr/bin/env python3
"""Load the latest newsletter-triage output for wiki ingestion."""

from __future__ import annotations

import json
import os
from pathlib import Path


TRIAGE_JOB_ID = "4e8b0d92c6a1"


def get_hermes_home() -> Path:
    hermes_home = os.environ.get("HERMES_HOME")
    if hermes_home:
        return Path(hermes_home)
    return Path.home() / ".hermes"


def extract_response_text(output_path: Path) -> str:
    text = output_path.read_text(encoding="utf-8", errors="replace")
    marker = "## Response"
    if marker not in text:
        return ""
    return text.split(marker, 1)[1].strip()


def extract_json_blob(response_text: str) -> dict | None:
    response_text = response_text.strip()
    if response_text.startswith("```json"):
        response_text = response_text[len("```json"):].strip()
    if response_text.startswith("```"):
        response_text = response_text[len("```"):].strip()
    if response_text.endswith("```"):
        response_text = response_text[:-3].strip()
    try:
        return json.loads(response_text)
    except Exception:
        return None


def main() -> int:
    hermes_home = get_hermes_home()
    output_dir = hermes_home / "cron" / "output" / TRIAGE_JOB_ID
    checkpoint_dir = hermes_home / "cron" / "data" / "newsletter"
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(output_dir.glob("*.md"), key=lambda p: p.stat().st_mtime, reverse=True)
    if not files:
        print(json.dumps({
            "ok": False,
            "error": "newsletter-triage output not found",
            "output_dir": str(output_dir),
        }, ensure_ascii=False, indent=2))
        return 0

    latest_output = files[0]
    payload = extract_json_blob(extract_response_text(latest_output))
    if not payload:
        print(json.dumps({
            "ok": False,
            "error": "failed to parse JSON response from newsletter-triage output",
            "output_path": str(latest_output),
        }, ensure_ascii=False, indent=2))
        return 0

    latest_path = checkpoint_dir / "triage_latest.json"
    latest_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    payload["_triage_checkpoint"] = {
        "ok": True,
        "output_path": str(latest_output),
        "checkpoint_path": str(latest_path),
    }

    # --- Archive skip/reference items ---
    import subprocess
    archive_script = Path(__file__).resolve().parent / "archive_triage.py"
    if archive_script.exists():
        try:
            result = subprocess.run(
                [str(archive_script), "newsletter", "--keep-reference"],
                capture_output=True, text=True, timeout=30,
            )
            archive_data = json.loads(result.stdout) if result.stdout else {}
            payload["_archive"] = archive_data.get("newsletter", {"error": "no newsletter key"})
        except Exception as exc:
            payload["_archive"] = {"ok": False, "error": str(exc)}
    # --- end archive ---

    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
