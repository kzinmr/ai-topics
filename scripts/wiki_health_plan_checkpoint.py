#!/usr/bin/env python3
"""Load the latest wiki-health-plan output for the follow-up fix job."""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path


PLAN_JOB_NAME = os.environ.get("WIKI_HEALTH_PLAN_JOB_NAME", "wiki-health-plan")
MAX_AGE_HOURS = float(os.environ.get("WIKI_HEALTH_PLAN_MAX_AGE_HOURS", "6"))
MAX_AUTO_ORPHAN_INDEX = int(os.environ.get("WIKI_HEALTH_MAX_AUTO_ORPHAN_INDEX", "20"))


def get_hermes_home() -> Path:
    hermes_home = os.environ.get("HERMES_HOME")
    if hermes_home:
        return Path(hermes_home)
    return Path.home() / ".hermes"


def find_plan_job_id(hermes_home: Path) -> str | None:
    jobs_path = hermes_home / "cron" / "jobs.json"
    if not jobs_path.exists():
        return None
    try:
        data = json.loads(jobs_path.read_text(encoding="utf-8"))
    except Exception:
        return None

    matches = [
        job
        for job in data.get("jobs", [])
        if job.get("name") == PLAN_JOB_NAME and job.get("enabled", True)
    ]
    if not matches:
        return None

    matches.sort(key=lambda job: job.get("created_at") or "", reverse=True)
    return matches[0].get("id")


def extract_response_text(output_path: Path) -> str:
    text = output_path.read_text(encoding="utf-8", errors="replace")
    marker = "## Response"
    if marker not in text:
        return ""
    return text.split(marker, 1)[1].strip()


def strip_fence(text: str) -> str:
    text = text.strip()
    if text.startswith("```json"):
        text = text[len("```json"):].strip()
    elif text.startswith("```"):
        text = text[len("```"):].strip()
    if text.endswith("```"):
        text = text[:-3].strip()
    return text


def extract_json_blob(response_text: str) -> dict | None:
    response_text = strip_fence(response_text)
    try:
        payload = json.loads(response_text)
        return payload if isinstance(payload, dict) else None
    except Exception:
        return None


def sanitize_auto_apply(payload: dict) -> dict:
    """Keep auto-apply limited to deterministic index maintenance."""
    blocked: list[dict] = []
    for action in payload.get("actions", []):
        if not isinstance(action, dict) or not action.get("auto_apply"):
            continue
        category = str(action.get("category", ""))
        target_path = str(action.get("target_path", ""))
        action_text = " ".join(
            str(action.get(key, ""))
            for key in ("id", "diagnosis_ja", "fix_ja")
        )
        counts = [int(value) for value in re.findall(r"\d+", action_text)]
        max_count = max(counts, default=0)
        allowed = (
            category == "orphan_index"
            and target_path == "~/wiki/index.md"
            and max_count <= MAX_AUTO_ORPHAN_INDEX
        )
        if allowed:
            continue
        action["auto_apply"] = False
        if category == "orphan_index" and target_path == "~/wiki/index.md":
            reason = f"orphan index auto-apply is limited to <= {MAX_AUTO_ORPHAN_INDEX} pages"
        else:
            reason = "auto_apply is limited to orphan_index actions targeting ~/wiki/index.md"
        blocked.append({
            "id": action.get("id"),
            "category": category,
            "target_path": target_path,
            "reason": reason,
        })

    payload["_auto_apply_filter"] = {
        "allowed_categories": ["orphan_index"],
        "allowed_targets": ["~/wiki/index.md"],
        "max_auto_orphan_index": MAX_AUTO_ORPHAN_INDEX,
        "blocked": blocked,
    }
    return payload


def is_fresh(output_path: Path) -> bool:
    if MAX_AGE_HOURS <= 0:
        return True
    modified = datetime.fromtimestamp(output_path.stat().st_mtime, tz=timezone.utc)
    age_hours = (datetime.now(timezone.utc) - modified).total_seconds() / 3600
    return age_hours <= MAX_AGE_HOURS


def main() -> int:
    hermes_home = get_hermes_home()
    plan_job_id = find_plan_job_id(hermes_home)
    if not plan_job_id:
        print(json.dumps({
            "ok": False,
            "error": "wiki-health-plan job not found",
            "job_name": PLAN_JOB_NAME,
            "jobs_path": str(hermes_home / "cron" / "jobs.json"),
        }, ensure_ascii=False, indent=2))
        return 0

    output_dir = hermes_home / "cron" / "output" / plan_job_id
    checkpoint_dir = hermes_home / "cron" / "data" / "wiki_health"
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    files = sorted(output_dir.glob("*.md"), key=lambda path: path.stat().st_mtime, reverse=True)
    if not files:
        print(json.dumps({
            "ok": False,
            "error": "wiki-health-plan output not found",
            "plan_job_id": plan_job_id,
            "output_dir": str(output_dir),
        }, ensure_ascii=False, indent=2))
        return 0

    latest_output = files[0]
    if not is_fresh(latest_output):
        print(json.dumps({
            "ok": False,
            "error": "latest wiki-health-plan output is stale",
            "plan_job_id": plan_job_id,
            "output_path": str(latest_output),
            "max_age_hours": MAX_AGE_HOURS,
        }, ensure_ascii=False, indent=2))
        return 0

    payload = extract_json_blob(extract_response_text(latest_output))
    if not payload:
        print(json.dumps({
            "ok": False,
            "error": "failed to parse JSON response from wiki-health-plan output",
            "plan_job_id": plan_job_id,
            "output_path": str(latest_output),
        }, ensure_ascii=False, indent=2))
        return 0

    payload = sanitize_auto_apply(payload)
    latest_path = checkpoint_dir / "plan_latest.json"
    latest_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    payload["_wiki_health_plan_checkpoint"] = {
        "ok": True,
        "plan_job_id": plan_job_id,
        "output_path": str(latest_output),
        "checkpoint_path": str(latest_path),
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
