#!/usr/bin/env python3
"""Watchdog health check for llm-wiki cron pipelines.

Checks:
1. All pipeline jobs' last_status and recency
2. Wiki file counts and basic integrity
3. Git status (uncommitted changes, last push)
4. Pipeline chain integrity (ingest → triage → wiki-ingest linkage)

Output: JSON health report. Non-zero exit on critical issues.
Designed for 2-hourly cron (matching the article's pattern).
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path


HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
CRON_OUTPUT = HERMES_HOME / "cron" / "output"
WIKI_PATH = Path.home() / "wiki"  # resolves to ai-topics/wiki


# ── Pipeline job definitions ──────────────────────────────────
PIPELINES = {
    "blog": {
        "ingest": "1bf4c6492c1e",
        "triage": "58c2f4a7e1bd",
        "wiki_ingest": "9a7d1e3c4b20",
    },
    "newsletter": {
        "ingest": "3293c14f4352",
        "triage": "4e8b0d92c6a1",
        "wiki_ingest": "a1f4d9c3e672",
    },
    "x_bookmarks": "56e7e85f45b1",
    "x_accounts": "ca7850edc955",
    "dreaming": {
        "collect": "8c1d7e52a4b1",
        "group": "c4a9e8d2f671",
        "wiki_ingest": "d7b3f5c1a902",
    },
    "wiki_health": "07d1ccf7541a",
    "wiki_health_fix": "6f3525ec4d9a",
    "trending_topics": "158a461eb520",
    "active_crawl": "14599191cbf6",
    "skeleton_enrich": "503ccbb7530e",
    "sitemap_monitor": "c7890b6e0e19",
}


def get_job_status(job_id: str) -> dict | None:
    """Get a single job's status from jobs.json."""
    jobs_file = HERMES_HOME / "cron" / "jobs.json"
    if not jobs_file.exists():
        return None
    try:
        data = json.loads(jobs_file.read_text())
        jobs = data.get("jobs", [])
    except (json.JSONDecodeError, OSError):
        return None

    for job in jobs:
        if job.get("id") == job_id:
            return {
                "name": job.get("name", "unknown"),
                "last_status": job.get("last_status"),
                "last_run_at": job.get("last_run_at"),
                "last_error": job.get("last_error"),
                "enabled": job.get("enabled", True),
                "state": job.get("state", "unknown"),
                "next_run_at": job.get("next_run_at"),
            }
    return None


def check_job_recency(job_info: dict, max_hours: int = 26) -> dict:
    """Check if a job has run recently enough."""
    result = {"name": job_info["name"], "status": job_info["last_status"]}

    if not job_info["enabled"]:
        result["issue"] = "disabled"
        return result

    if job_info["last_run_at"] is None:
        result["issue"] = "never_run"
        return result

    last_run = datetime.fromisoformat(job_info["last_run_at"])
    age = datetime.now(timezone.utc) - last_run

    if job_info["last_status"] != "ok":
        result["issue"] = f"error_status({job_info['last_status']})"
        result["last_run"] = job_info["last_run_at"]
        result["age_hours"] = round(age.total_seconds() / 3600, 1)
        return result

    if age > timedelta(hours=max_hours):
        result["issue"] = f"stale({max_hours}h)"
    else:
        result["issue"] = None

    result["last_run"] = job_info["last_run_at"]
    result["age_hours"] = round(age.total_seconds() / 3600, 1)
    return result


def check_pipeline_chain(pipeline_name: str, stages: dict) -> dict:
    """Check that a pipeline chain's stages ran in correct order and all succeeded."""
    result = {"name": pipeline_name, "stages": {}, "healthy": True}

    ingest_info = get_job_status(stages["ingest"])
    triage_info = get_job_status(stages["triage"])
    wiki_info = get_job_status(stages["wiki_ingest"])

    for stage_name, info in [("ingest", ingest_info), ("triage", triage_info), ("wiki_ingest", wiki_info)]:
        if info is None:
            result["stages"][stage_name] = {"error": "job_not_found"}
            result["healthy"] = False
            continue

        check = check_job_recency(info, max_hours=26)
        result["stages"][stage_name] = check
        if check.get("issue"):
            result["healthy"] = False

    # Chain integrity: if ingest succeeded but triage/wiki_ingest failed
    if ingest_info and triage_info:
        ingest_ok = ingest_info.get("last_status") == "ok"
        triage_ok = triage_info.get("last_status") == "ok"
        if ingest_ok and not triage_ok:
            result["chain_broken"] = "ingest_ok_but_triage_failed"
            result["healthy"] = False
        if triage_ok and wiki_info and wiki_info.get("last_status") != "ok":
            result["chain_broken"] = "triage_ok_but_wiki_ingest_failed"
            result["healthy"] = False

    return result


def check_wiki_integrity() -> dict:
    """Basic wiki integrity checks (fast, no LLM needed)."""
    result = {"healthy": True, "checks": {}}

    # Check wiki directory exists
    if not WIKI_PATH.exists():
        result["checks"]["wiki_dir"] = "missing"
        result["healthy"] = False
        return result
    result["checks"]["wiki_dir"] = "ok"

    # Page counts
    for subdir in ["entities", "concepts", "comparisons"]:
        d = WIKI_PATH / subdir
        if d.exists():
            count = len(list(d.glob("*.md")))
            result["checks"][f"{subdir}_count"] = count
        else:
            result["checks"][f"{subdir}_count"] = "missing"
            result["healthy"] = False

    # Index exists and is recent
    index = WIKI_PATH / "index.md"
    if index.exists():
        mtime = datetime.fromtimestamp(index.stat().st_mtime, tz=timezone.utc)
        age = datetime.now(timezone.utc) - mtime
        result["checks"]["index_age_hours"] = round(age.total_seconds() / 3600, 1)
        if age > timedelta(hours=48):
            result["checks"]["index_stale"] = True
            result["healthy"] = False
    else:
        result["checks"]["index"] = "missing"
        result["healthy"] = False

    # Log exists
    log = WIKI_PATH / "log.md"
    result["checks"]["log_exists"] = log.exists()

    return result


def check_git_status() -> dict:
    """Check git repo for uncommitted changes or unpushed commits."""
    result = {"healthy": True, "details": {}}

    repo = Path.home() / "ai-topics"
    if not (repo / ".git").exists():
        result["details"]["repo"] = "missing"
        result["healthy"] = False
        return result

    try:
        # Uncommitted changes
        r = subprocess.run(
            ["git", "status", "--porcelain", "--", "wiki/"],
            capture_output=True, text=True, cwd=repo, timeout=10
        )
        dirty = [l for l in r.stdout.strip().split("\n") if l]
        result["details"]["uncommitted_files"] = len(dirty)
        if dirty:
            result["details"]["sample"] = dirty[:5]

        # Unpushed commits
        r = subprocess.run(
            ["git", "log", "--oneline", "origin/main..main", "--", "wiki/"],
            capture_output=True, text=True, cwd=repo, timeout=10
        )
        unpushed = [l for l in r.stdout.strip().split("\n") if l]
        result["details"]["unpushed_commits"] = len(unpushed)
        if len(unpushed) > 5:
            result["details"]["unpushed_warning"] = f"{len(unpushed)} unpushed commits"
            result["healthy"] = False

        # Last push time
        r = subprocess.run(
            ["git", "log", "-1", "--format=%aI", "origin/main"],
            capture_output=True, text=True, cwd=repo, timeout=10
        )
        last_push = r.stdout.strip()
        if last_push:
            push_time = datetime.fromisoformat(last_push)
            age = datetime.now(timezone.utc) - push_time
            result["details"]["last_push_hours_ago"] = round(age.total_seconds() / 3600, 1)
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        result["details"]["git_error"] = str(e)

    return result


def main():
    now = datetime.now(timezone.utc)
    report = {
        "timestamp": now.isoformat(),
        "watchdog": "llm-wiki-pipeline",
        "overall_healthy": True,
        "pipelines": {},
        "standalone_jobs": {},
        "wiki": {},
        "git": {},
        "alerts": [],
    }

    # ── Pipeline checks ──
    for pipe_name, stages in [("blog", PIPELINES["blog"]), ("newsletter", PIPELINES["newsletter"])]:
        result = check_pipeline_chain(pipe_name, stages)
        report["pipelines"][pipe_name] = result
        if not result["healthy"]:
            report["overall_healthy"] = False
            report["alerts"].append(f"PIPELINE {pipe_name}: unhealthy")

    # ── Standalone job checks ──
    standalone_jobs = {
        "x_bookmarks": PIPELINES["x_bookmarks"],
        "x_accounts": PIPELINES["x_accounts"],
        "wiki_health": PIPELINES["wiki_health"],
        "trending_topics": PIPELINES["trending_topics"],
        "active_crawl": PIPELINES["active_crawl"],
        "skeleton_enrich": PIPELINES["skeleton_enrich"],
        "sitemap_monitor": PIPELINES["sitemap_monitor"],
    }
    for name, job_id in standalone_jobs.items():
        info = get_job_status(job_id)
        if info is None:
            report["standalone_jobs"][name] = {"error": "not_found"}
            continue
        check = check_job_recency(info)
        report["standalone_jobs"][name] = check
        if check.get("issue"):
            report["overall_healthy"] = False
            report["alerts"].append(f"JOB {name}: {check['issue']}")

    # ── Wiki integrity ──
    wiki_check = check_wiki_integrity()
    report["wiki"] = wiki_check
    if not wiki_check["healthy"]:
        report["overall_healthy"] = False
        report["alerts"].append("WIKI: integrity check failed")

    # ── Git status ──
    git_check = check_git_status()
    report["git"] = git_check
    if not git_check["healthy"]:
        report["overall_healthy"] = False

    # ── Output ──
    # no_agent watchdog semantics:
    #   exit 0 + empty stdout → silent (healthy)
    #   exit 0 + human message → delivered as alert
    #   exit ≠ 0 → script error (broken watchdog)
    if report["alerts"]:
        lines = [
            "🔔 **Pipeline Watchdog Alert**",
            f"🕐 {now.strftime('%Y-%m-%d %H:%M UTC')}",
            "",
        ]
        for alert in report["alerts"]:
            lines.append(f"• {alert}")

        # Add detail for error jobs
        for name, check in report.get("standalone_jobs", {}).items():
            if check.get("issue") and "error_status" in str(check.get("issue", "")):
                lines.append(f"  └ `{name}` — last run: {check.get('last_run', '?')} ({check.get('age_hours', '?')}h ago)")

        # Pipeline chain breaks
        for pipe_name, result in report.get("pipelines", {}).items():
            if result.get("chain_broken"):
                lines.append(f"  └ `{pipe_name}` chain broken: {result['chain_broken']}")

        # Wiki issues
        if not report.get("wiki", {}).get("healthy"):
            lines.append("• WIKI integrity check failed")

        # Git issues
        git = report.get("git", {}).get("details", {})
        if git.get("unpushed_commits", 0) > 5:
            lines.append(f"• {git['unpushed_commits']} unpushed commits")

        print("\n".join(lines))

    # Always exit 0 — script errors only for actual bugs
    sys.exit(0)


if __name__ == "__main__":
    main()
