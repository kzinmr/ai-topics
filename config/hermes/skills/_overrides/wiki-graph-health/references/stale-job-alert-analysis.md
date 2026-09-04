# Stale Job Alert Analysis for Multi-Day Schedules

## Problem

The pipeline watchdog's stale alert threshold (typically 24h) does not account for multi-day schedule intervals. Jobs like `x-accounts-scan` (schedule: `30 22 */2 * *` — every 2 days) regularly appear "stale" 40+ hours after last run even though the next run is on schedule.

## Verification Procedure

When a stale alert fires:

1. **Read the job definition** from `~/.hermes/cron/jobs.json`:
   ```bash
   grep -B 2 -A 15 'job-name' ~/.hermes/cron/jobs.json
   ```
   Check: `schedule`, `state`, `last_run_at`, `next_run_at`, `enabled`, `paused_at`.

2. **Classify the alert**:
   | Condition | Classification | Action |
   |-----------|---------------|--------|
   | `enabled: true`, `state: scheduled`, `next_run_at` within 1 cycle | **False positive** | Job is on normal multi-day interval |
   | `paused_at` is non-null | **Genuine paused** | Check `paused_reason`; may need re-enabling |
   | `state: error` | **Genuine failure** | Investigate error logs |
   | `next_run_at` overdue by >1 full cycle | **Genuine stale** | Investigate root cause |

3. **Confirm schedule interval** from `schedule.expr` field. Common patterns:
   - `*/2 * *` = every 2 days (up to 48h between runs is normal)
   - `* * *` = daily (up to 26h between runs is normal)
   - `30 11,23 * * *` = twice daily (up to 13h between runs is normal)

## Pitfalls

- **`hermes` CLI not on PATH in cron context**: `hermes cron list` may fail with `command not found`. Read `~/.hermes/cron/jobs.json` directly with Python or grep instead.
- **Schema varies**: `jobs.json` may be a flat list or a dict with a `jobs` key. Check structure first:
  ```python
  import json, os
  data = json.load(open(os.path.expanduser('~/.hermes/cron/jobs.json')))
  if isinstance(data, dict):
      jobs = data.get('jobs', [])
  elif isinstance(data, list):
      jobs = data
  ```

## Recent Example

**2026-07-19**: `x-accounts-scan` reported stale(26h). Investigation showed:
- Last run: July 17T22:32, Next run: July 19T22:30 (schedule: every 2 days at 22:30 UTC)
- Enabled, scheduled, not paused
- Result: **False positive** — job was running on its normal 2-day interval
