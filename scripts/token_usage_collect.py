#!/usr/bin/env python3
"""Token usage monitor — persistent DuckDB-based storage with time-bucketed queries.

Architecture:
  1. COST_REPORT lines from cron outputs are parsed into DuckDB on ingest
  2. All historical entries persist in a single .db file
  3. Reports (daily/weekly/monthly/trend) query the DB with SQL
  4. Future: trend analysis, anomaly detection, alerts

Usage:
  python3 token_usage_collect.py          # daily report (default)
  python3 token_usage_collect.py weekly   # weekly report
  python3 token_usage_collect.py monthly  # monthly report
  python3 token_usage_collect.py trend    # daily cost trend (7d)
  python3 token_usage_collect.py all      # all reports at once

Output: ~/.hermes/cron/data/token_usage/summary.json
DB:     ~/.hermes/cron/data/token_usage/token_usage.db
"""

import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

HERMES_HOME = Path(os.environ.get("HERMES_HOME", Path.home() / ".hermes"))
OUTPUT_DIR = HERMES_HOME / "cron" / "output"
DATA_DIR = HERMES_HOME / "cron" / "data" / "token_usage"
SUMMARY_PATH = DATA_DIR / "summary.json"
DB_PATH = DATA_DIR / "token_usage.db"
JOBS_PATH = HERMES_HOME / "cron" / "jobs.json"

# COST_REPORT parsing moved to parse_cost_report() with flexible handling
# (regex-based approach replaced by key-value extraction)

PROVIDER_COSTS = {
    "deepseek":  {"input": 0.002, "output": 0.008},
    "fireworks.ai": {"input": 0.003, "output": 0.015},
}


def _parse_token_val(s):
    """Parse token values: handles ~prefix, K/M suffixes."""
    s = s.strip().lstrip('~').lstrip('≈').lstrip('*')
    multiplier = 1
    up = s.upper()
    if up.endswith('K'):
        multiplier = 1000
        s = s[:-1]
    elif up.endswith('M'):
        multiplier = 1_000_000
        s = s[:-1]
    try:
        return int(float(s) * multiplier)
    except (ValueError, TypeError):
        return 0


def parse_cost_report(line: str):
    """Parse COST_REPORT lines in two formats:
    Format A (space-sep, legacy): COST_REPORT: job=NAME [status=S] input_tokens=N output_tokens=N [cost=C]
    Format B (pipe-sep, current): COST_REPORT: job=NAME | field=val | field=val | ...
    """
    line = line.strip().strip('*')
    if 'COST_REPORT:' not in line:
        return None

    idx = line.index('COST_REPORT:')
    rest = line[idx + len('COST_REPORT:'):].strip()

    entry = {
        'job': None,
        'status': '',
        'input_tokens': 0,
        'output_tokens': 0,
        'cost': 0.0,
        'provider': None,
        'model': None,
    }

    if ' | ' in rest:
        # Format B: pipe-delimited key=value pairs
        parts = [p.strip() for p in rest.split('|')]
        kv_pairs = {}
        for p in parts:
            if '=' in p:
                k, v = p.split('=', 1)
                kv_pairs[k.strip()] = v.strip()
        entry['job'] = kv_pairs.get('job', '')
        entry['status'] = kv_pairs.get('status', '')
        entry['provider'] = kv_pairs.get('provider')
        entry['model'] = kv_pairs.get('model', '')

        # Try multiple field names for tokens
        input_raw = kv_pairs.get('input_tokens') or kv_pairs.get('input') or ''
        output_raw = kv_pairs.get('output_tokens') or kv_pairs.get('output') or ''
        entry['input_tokens'] = _parse_token_val(input_raw) if input_raw else 0
        entry['output_tokens'] = _parse_token_val(output_raw) if output_raw else 0

        # Cost from line or compute later
        cost_raw = kv_pairs.get('cost', '')
        try:
            entry['cost'] = float(cost_raw) if cost_raw else 0.0
        except ValueError:
            entry['cost'] = 0.0

        # Skip if no meaningful token data and this isn't a known format
        if not entry['job']:
            return None

    else:
        # Format A: space-separated key=value pairs
        m = re.search(r'job=(\S+)', rest)
        if not m:
            return None
        entry['job'] = m.group(1)
        # Validate job name: skip if it looks like a regex pattern
        if not all(c.isalnum() or c in '-_.' for c in entry['job']):
            return None

        m_status = re.search(r'status=(\S+)', rest)
        if m_status:
            entry['status'] = m_status.group(1)

        m_in = re.search(r'input_tokens=(\S+)', rest)
        if m_in:
            entry['input_tokens'] = _parse_token_val(m_in.group(1))

        m_out = re.search(r'output_tokens=(\S+)', rest)
        if m_out:
            entry['output_tokens'] = _parse_token_val(m_out.group(1))

        m_cost = re.search(r'cost=(\S+)', rest)
        if m_cost:
            try:
                entry['cost'] = float(m_cost.group(1))
            except ValueError:
                entry['cost'] = 0.0

        m_provider = re.search(r'provider=(\S+)', rest)
        if m_provider:
            entry['provider'] = m_provider.group(1)

        m_model = re.search(r'model=(\S+)', rest)
        if m_model:
            entry['model'] = m_model.group(1)

    return entry


def load_jobs_map():
    """Read cron config to map job_id → {name, model, provider}."""
    if not JOBS_PATH.exists():
        return {}
    with open(JOBS_PATH) as f:
        jobs_data = json.load(f)
    return {
        job["job_id"]: {
            "name": job.get("name", job["job_id"]),
            "model": job.get("model"),
            "provider": job.get("provider"),
        }
        for job in jobs_data.get("jobs", [])
        if job.get("job_id")
    }


def init_db():
    """Initialize SQLite with the tokens table."""
    import sqlite3
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH))
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tokens (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            job          TEXT,
            status       TEXT,
            provider     TEXT,
            model        TEXT,
            input_tokens INTEGER,
            output_tokens INTEGER,
            cost         REAL,
            input_cost   REAL,
            output_cost  REAL,
            source_file  TEXT,
            run_ts       TEXT,
            line_hash    TEXT  -- MD5 of raw COST_REPORT line (for dedup)
        )
    """)
    # Index for fast time-range queries
    conn.execute("CREATE INDEX IF NOT EXISTS idx_run_ts ON tokens(run_ts)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_job ON tokens(job)")
    conn.execute("CREATE INDEX IF NOT EXISTS idx_provider ON tokens(provider)")
    conn.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_line_hash ON tokens(source_file, line_hash)")
    conn.commit()
    return conn


def ingest_from_output_dir(conn, output_dir, jobs_map):
    """Scan cron output files, parse COST_REPORT, insert into DB.
    Uses (job, source_file) as dedup key.
    """
    cur = conn.cursor()
    ingested = 0

    for job_dir in output_dir.iterdir():
        job_id = job_dir.name
        job_info = jobs_map.get(job_id, {})
        provider = job_info.get("provider", "deepseek")
        model = job_info.get("model", "")

        if not job_dir.is_dir():
            continue

        for output_file in sorted(job_dir.iterdir()):
            try:
                content = output_file.read_text(errors="replace")
                for line in content.split("\n"):
                    entry = parse_cost_report(line)
                    if not entry:
                        continue

                    # Use provider/model from COST_REPORT line if available, else job config
                    eff_provider = entry.get("provider") or provider
                    eff_model = entry.get("model") or model

                    input_cost = output_cost = 0.0
                    if eff_provider in PROVIDER_COSTS:
                        pc = PROVIDER_COSTS[eff_provider]
                        input_cost = entry["input_tokens"] * pc["input"] / 1_000_000
                        output_cost = entry["output_tokens"] * pc["output"] / 1_000_000

                    run_ts = datetime.now(timezone.utc).isoformat()
                    line_hash = hashlib.md5(line.strip().encode()).hexdigest()
                    try:
                        cur.execute(
                            """INSERT INTO tokens
                               (job, status, provider, model, input_tokens, output_tokens,
                                cost, input_cost, output_cost, source_file, run_ts, line_hash)
                               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                            (
                                entry["job"],
                                entry["status"],
                                eff_provider,
                                eff_model,
                                entry["input_tokens"],
                                entry["output_tokens"],
                                input_cost + output_cost,  # computed from provider rates
                                input_cost,
                                output_cost,
                                output_file.name,
                                run_ts,
                                line_hash,
                            ),
                        )
                        ingested += 1
                    except Exception:
                        # Duplicate (source_file, line_hash) - skip silently
                        pass
            except Exception:
                continue

    conn.commit()
    return ingested


def query_aggregates(conn, since, group_by="job"):
    """Generic aggregate query. Returns list of dicts."""
    cur = conn.cursor()
    cur.execute(f"""
        SELECT
            job,
            status,
            provider,
            model,
            COUNT(*) as runs,
            SUM(input_tokens) as total_input,
            SUM(output_tokens) as total_output,
            SUM(cost) as total_cost,
            SUM(input_cost) as total_input_cost,
            SUM(output_cost) as total_output_cost
        FROM tokens
        WHERE run_ts >= ?
        GROUP BY {group_by}
        ORDER BY total_cost DESC
    """, (since,))
    cols = [d[0] for d in cur.description]
    rows = cur.fetchall()
    return [dict(zip(cols, r)) for r in rows]

def query_trend(conn, days=7):
    """Daily cost trend. Returns list of {day, total_cost, runs}."""
    since = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()
    cur = conn.cursor()
    cur.execute("""
        SELECT
            DATE(run_ts) as day,
            SUM(cost) as total_cost,
            SUM(input_cost) as total_input_cost,
            SUM(output_cost) as total_output_cost,
            COUNT(*) as runs
        FROM tokens
        WHERE run_ts >= ?
        GROUP BY DATE(run_ts)
        ORDER BY day
    """, (since,))
    return [{"day": r[0], "cost": r[1] or 0, "input_cost": r[2] or 0,
             "output_cost": r[3] or 0, "runs": r[4]} for r in cur.fetchall()]


def format_report(report_type, rows, total_runs, total_cost, **extra):
    """Format as JSON with consistent structure."""
    return {
        "report_type": report_type,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_runs": total_runs,
        "total_cost": total_cost,
        **extra,
        "rows": rows,
    }


def main():
    import sqlite3

    jobs_map = load_jobs_map()

    # Allow CLI arg: daily | weekly | monthly | trend | all
    mode = sys.argv[1] if len(sys.argv) > 1 else "daily"

    conn = init_db()
    ingested = ingest_from_output_dir(conn, OUTPUT_DIR, jobs_map)

    now = datetime.now(timezone.utc)

    results = {}

    if mode in ("daily", "all"):
        since = (now - timedelta(hours=24)).isoformat()
        rows = query_aggregates(conn, since, "job")
        total_runs = sum(r.get("runs", 0) for r in rows)
        total_cost = sum(r.get("total_cost", 0) or 0 for r in rows)
        results["daily"] = format_report("daily", rows, total_runs, total_cost)

    if mode in ("weekly", "all"):
        since = (now - timedelta(days=7)).isoformat()
        rows = query_aggregates(conn, since, "job")
        total_runs = sum(r.get("runs", 0) for r in rows)
        total_cost = sum(r.get("total_cost", 0) or 0 for r in rows)
        results["weekly"] = format_report("weekly", rows, total_runs, total_cost)

    if mode in ("monthly", "all"):
        since = (now - timedelta(days=30)).isoformat()
        rows = query_aggregates(conn, since, "job")
        total_runs = sum(r.get("runs", 0) for r in rows)
        total_cost = sum(r.get("total_cost", 0) or 0 for r in rows)
        results["monthly"] = format_report("monthly", rows, total_runs, total_cost)

    if mode in ("trend", "all"):
        since = (now - timedelta(days=7)).isoformat()
        trend_rows = query_trend(conn, 7)
        results["trend"] = {
            "report_type": "trend",
            "days": 7,
            "data": trend_rows,
        }

    # Write summary.json
    summary = {
        "mode": "sqlite",
        "ingested": ingested,
        **results,
    }
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(SUMMARY_PATH, "w") as f:
        json.dump(summary, f, indent=2, default=str)

    # Print one-line summary
    if "daily" in results:
        r = results["daily"]
        print(json.dumps({
            "summary": f"token_usage: {r['total_runs']} runs, ${r['total_cost']:.3f} total "
                       f"(DB: {len(r['rows'])} jobs, ingested={ingested})",
        }, indent=2))
    elif "weekly" in results:
        r = results["weekly"]
        print(json.dumps({
            "summary": f"token_usage (weekly): {r['total_runs']} runs, ${r['total_cost']:.3f} total",
        }, indent=2))
    elif "monthly" in results:
        r = results["monthly"]
        print(json.dumps({
            "summary": f"token_usage (monthly): {r['total_runs']} runs, ${r['total_cost']:.3f} total",
        }, indent=2))
    elif "trend" in results:
        print(json.dumps({
            "summary": f"token_usage (trend): {len(results['trend']['data'])} days",
        }, indent=2))

    conn.close()


if __name__ == "__main__":
    main()
