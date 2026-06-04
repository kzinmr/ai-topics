#!/usr/bin/env python3
"""Pre-run context collector for wiki-watchdog-fix agent.

Collects:
1. Latest pipeline_watchdog.py output
2. Latest wiki-health output (lint results)
3. Latest wiki-graph-analysis output
4. Current wiki state snapshot

Outputs JSON payload for the agent to analyze and auto-fix.
"""

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path


HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
CRON_OUTPUT = HERMES_HOME / "cron" / "output"
WIKI_PATH = Path.home() / "wiki"


def read_latest_job_output(job_id: str, max_age_hours: int = 30) -> dict | None:
    """Read the latest output file from a cron job."""
    job_dir = CRON_OUTPUT / job_id
    if not job_dir.exists():
        return None

    md_files = sorted(job_dir.glob("*.md"), reverse=True)
    for f in md_files:
        content = f.read_text(encoding="utf-8", errors="replace")
        if not content.strip():
            continue

        # Check age
        mtime = datetime.fromtimestamp(f.stat().st_mtime, tz=timezone.utc)
        age = datetime.now(timezone.utc) - mtime
        if age.total_seconds() > max_age_hours * 3600:
            continue

        # Extract the agent's Response section
        match = re.search(r"^## Response\s*\n(.*)", content, re.MULTILINE | re.DOTALL)
        if match:
            response_text = match.group(1).strip()
        else:
            response_text = content[:5000]  # fallback

        return {
            "file": f.name,
            "age_hours": round(age.total_seconds() / 3600, 1),
            "response": response_text[:8000],  # cap to save tokens
            "response_length": len(response_text),
        }

    return None


def extract_issues_from_wiki_health(response: str) -> list[str]:
    """Extract issue summaries from wiki-health lint output."""
    issues = []
    for line in response.split("\n"):
        line = line.strip()
        # Common patterns in lint output
        if any(kw in line.lower() for kw in [
            "broken", "orphan", "missing", "stale", "violation",
            "corruption", "duplicate", "inconsistency", "❌", "⚠️",
            "not found", "doesn't exist", "unreachable"
        ]):
            if len(line) > 10:
                issues.append(line[:200])
    return issues[:30]


def main():
    now = datetime.now(timezone.utc)

    payload = {
        "timestamp": now.isoformat(),
        "source": "wiki_watchdog_fix_context.py",
        "pipeline_watchdog": None,
        "wiki_health": None,
        "wiki_graph_analysis": None,
        "wiki_snapshot": {},
    }

    # 1. Pipeline watchdog output
    wd_job_id = "696ec6b0ecc7"
    wd = read_latest_job_output(wd_job_id)
    if wd:
        payload["pipeline_watchdog"] = {
            "file": wd["file"],
            "age_hours": wd["age_hours"],
            "alerts": extract_issues_from_wiki_health(wd["response"]),
        }

    # 2. Wiki health lint output
    health_job_id = "07d1ccf7541a"
    health = read_latest_job_output(health_job_id, max_age_hours=48)
    if health:
        issues = extract_issues_from_wiki_health(health["response"])
        payload["wiki_health"] = {
            "file": health["file"],
            "age_hours": health["age_hours"],
            "issues_found": len(issues),
            "sample_issues": issues[:20],
            "response_preview": health["response"][:3000],
        }

    # 3. Wiki graph analysis output
    graph_job_id = "ed6f00d28955"
    graph = read_latest_job_output(graph_job_id, max_age_hours=168)  # weekly
    if graph:
        issues = extract_issues_from_wiki_health(graph["response"])
        payload["wiki_graph_analysis"] = {
            "file": graph["file"],
            "age_hours": graph["age_hours"],
            "issues_found": len(issues),
            "sample_issues": issues[:15],
            "response_preview": graph["response"][:3000],
        }

    # 4. Wiki quick snapshot
    if WIKI_PATH.exists():
        payload["wiki_snapshot"] = {
            "index_mtime": None,
            "entities_count": 0,
            "concepts_count": 0,
        }
        index = WIKI_PATH / "index.md"
        if index.exists():
            payload["wiki_snapshot"]["index_mtime"] = datetime.fromtimestamp(
                index.stat().st_mtime, tz=timezone.utc
            ).isoformat()
        for subdir in ["entities", "concepts"]:
            d = WIKI_PATH / subdir
            if d.exists():
                payload["wiki_snapshot"][f"{subdir}_count"] = len(list(d.glob("*.md")))

    print(json.dumps(payload, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
