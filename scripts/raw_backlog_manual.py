#!/usr/bin/env python3
"""Manual runner for Lucy raw-backlog-ingest.

Run from the host via:
  bin/hermes-lucy-raw-backlog dry-run --count 5
  bin/hermes-lucy-raw-backlog run --count 2
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import textwrap
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.request import urlopen

JOB_ID = "4e63c6f0d140"
JOB_NAME = "raw-backlog-ingest"
DEFAULT_COUNT = 5
DEFAULT_MIN_SIZE = 500
DEFAULT_SORT = "ai-hint"
GATE_BUSY_URL = "http://hermes-llm-serial-gate:8080/busy"

HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
PROFILE_ROOT = Path(os.environ.get("HERMES_PROFILE_ROOT", Path.home()))
AI_TOPICS = PROFILE_ROOT / "ai-topics"
COLLECTOR = AI_TOPICS / "scripts" / "raw_backlog_collect.py"
JOBS_FILE = HERMES_HOME / "cron" / "jobs.json"
MANUAL_OUTPUT_DIR = HERMES_HOME / "cron" / "manual" / JOB_NAME


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Manual raw-backlog-ingest runner")
    sub = parser.add_subparsers(dest="command", required=True)

    def add_common(p: argparse.ArgumentParser) -> None:
        p.add_argument("--count", type=int, default=DEFAULT_COUNT, help="articles to select for this batch")
        p.add_argument("--min-size", type=int, default=DEFAULT_MIN_SIZE, help="minimum raw article size in bytes")
        p.add_argument("--sort", choices=["ai-hint", "recent", "size"], default=DEFAULT_SORT)
        p.add_argument("--json", action="store_true", help="print raw collector/run JSON")

    add_common(sub.add_parser("dry-run", help="show selected articles and estimated runtime only"))
    run = sub.add_parser("run", help="run one manual batch synchronously")
    add_common(run)
    run.add_argument("--max-tokens", type=int, default=None, help="override job max_tokens for this manual run")
    run.add_argument("--force", action="store_true", help="run even when the serial LLM gate reports busy")
    return parser.parse_args(argv)


def fmt_duration(seconds: float | int | None) -> str:
    if seconds is None:
        return "unknown"
    seconds = int(round(float(seconds)))
    hours, rem = divmod(seconds, 3600)
    minutes, sec = divmod(rem, 60)
    if hours:
        return f"{hours}h {minutes}m"
    if minutes:
        return f"{minutes}m {sec}s"
    return f"{sec}s"


def run_collector(args: argparse.Namespace, *, dry_run: bool) -> dict[str, Any]:
    cmd = [
        sys.executable,
        str(COLLECTOR),
        "--count", str(args.count),
        "--min-size", str(args.min_size),
        "--sort", args.sort,
        "--estimate",
    ]
    if dry_run:
        cmd.append("--dry-run")
    proc = subprocess.run(cmd, cwd=AI_TOPICS, text=True, capture_output=True, check=False)
    if proc.returncode != 0:
        raise RuntimeError(f"collector failed with exit {proc.returncode}\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}")
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"collector did not return JSON: {exc}\n{proc.stdout[:2000]}") from exc


def print_plan(data: dict[str, Any]) -> None:
    estimate = data.get("estimate") if isinstance(data.get("estimate"), dict) else {}
    print(f"raw-backlog-ingest dry-run ({data.get('collected_at')})")
    print(f"selected: {data.get('candidates_selected')} / requested {data.get('selection', {}).get('requested_count')}")
    print(f"remaining candidates after this batch: {data.get('candidates_remaining')}")
    print(f"candidate count total: {data.get('candidate_count')}")
    print(f"selected bytes: {data.get('selected_bytes_total')}")
    if estimate.get("available"):
        print("estimate basis: successful raw-backlog-ingest o11y traces")
        print(f"history samples: {estimate.get('history_samples')}")
        print(f"median per article: {fmt_duration(estimate.get('median_per_article_seconds'))}")
        print(f"this batch median: {fmt_duration(estimate.get('estimated_selected_seconds_median'))}")
        print(f"this batch p80: {fmt_duration(estimate.get('estimated_selected_seconds_p80'))}")
        print(f"all current candidates median: {fmt_duration(estimate.get('estimated_all_candidates_seconds_median'))}")
    else:
        print(f"estimate unavailable: {estimate.get('basis')}")
    print("\nselected articles:")
    for idx, article in enumerate(data.get("articles", []), 1):
        print(f"{idx}. {article.get('filename')} ({article.get('size_bytes')} bytes)")
        if article.get("url"):
            print(f"   {article.get('url')}")


def load_job() -> dict[str, Any]:
    jobs = json.loads(JOBS_FILE.read_text(encoding="utf-8"))
    for job in jobs.get("jobs", []):
        if job.get("id") == JOB_ID or job.get("name") == JOB_NAME:
            return dict(job)
    raise RuntimeError(f"job not found: {JOB_ID}")


def serial_gate_busy() -> dict[str, Any] | None:
    try:
        with urlopen(GATE_BUSY_URL, timeout=5) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception:
        return None


def gate_is_busy(status: dict[str, Any] | None) -> bool:
    if not status:
        return False
    for info in status.values():
        if isinstance(info, dict) and info.get("busy"):
            return True
    return False


def save_manual_output(full_output: str, final_response: str, error: str | None, plan: dict[str, Any]) -> Path:
    MANUAL_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = MANUAL_OUTPUT_DIR / f"{stamp}.md"
    doc = [
        f"# Manual {JOB_NAME} {stamp}",
        "",
        "## Plan",
        "```json",
        json.dumps(plan, ensure_ascii=False, indent=2),
        "```",
        "",
        "## Error" if error else "## Result",
        error or final_response or "",
        "",
        "## Full Output",
        full_output or "",
    ]
    path.write_text("\n".join(doc), encoding="utf-8")
    return path


def run_manual(args: argparse.Namespace) -> int:
    plan = run_collector(args, dry_run=True)
    print_plan(plan)
    if int(plan.get("candidates_selected") or 0) == 0:
        print("\nNo candidates selected; nothing to run.")
        return 0

    gate = serial_gate_busy()
    if gate_is_busy(gate) and not args.force:
        print("\nSerial LLM gate is busy; not starting a manual batch. Re-run with --force to override.", file=sys.stderr)
        print(json.dumps(gate, ensure_ascii=False, indent=2), file=sys.stderr)
        return 2

    os.environ["RAW_BACKLOG_COUNT"] = str(args.count)
    os.environ["RAW_BACKLOG_MIN_SIZE"] = str(args.min_size)
    os.environ["RAW_BACKLOG_SORT"] = args.sort

    job = load_job()
    if args.max_tokens is not None:
        if args.max_tokens <= 0:
            raise RuntimeError("--max-tokens must be positive")
        job["max_tokens"] = args.max_tokens

    print("\nStarting manual raw-backlog-ingest batch...", flush=True)
    sys.path.insert(0, "/opt/hermes")
    from cron.scheduler import run_job  # type: ignore

    success, full_output, final_response, error = run_job(job)
    output_path = save_manual_output(full_output, final_response, error, plan)

    print(f"\nmanual output: {output_path}")
    if final_response:
        print("\nfinal response:\n")
        print(final_response)
    if not success:
        print("\nmanual run failed:", file=sys.stderr)
        print(error or "unknown error", file=sys.stderr)
        return 1
    return 0


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.command == "dry-run":
        data = run_collector(args, dry_run=True)
        if args.json:
            print(json.dumps(data, ensure_ascii=False, indent=2))
        else:
            print_plan(data)
        return 0
    if args.command == "run":
        if args.json:
            data = run_collector(args, dry_run=True)
            print(json.dumps(data, ensure_ascii=False, indent=2))
        return run_manual(args)
    raise RuntimeError(f"unknown command: {args.command}")


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        raise SystemExit(130)
    except Exception as exc:
        print(textwrap.dedent(f"""
        raw-backlog manual runner failed:
        {exc}
        """).strip(), file=sys.stderr)
        raise SystemExit(1)
