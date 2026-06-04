# Wiki-Health Pipeline Race Condition — 2026-05-13 Session

## Timeline

| Job | Schedule (UTC) | Actual Start | Actual Finish | Duration |
|-----|---------------|-------------|--------------|----------|
| wiki-health (07d1ccf7541a) | 0 17 * * * | 17:00 | 18:14:32 | **74 min** |
| wiki-health-plan (ac70e197fc75) | 10 17 * * * | 17:10 | 18:18:04 | **68 min** |
| wiki-health-fix (6f3525ec4d9a) | 25 17 * * * | 17:25 | 18:17:03 | 52 min |
| wiki-watchdog-fix (459ec1a09b8d) | 35 17 * * * | 17:35 | 18:21:37 | 46 min |

Normal run times (May 9-12): ~15-20 min per job. May 13 anomaly: 60-75 min due to wiki growth (1,800+ pages, 5,800+ raw articles).

## What Happened

1. `wiki_health_plan_checkpoint.py` looked for latest output in `~/.hermes/cron/output/ac70e197fc75/`
2. At 17:25, today's output hadn't been written yet (wiki-health-plan still running)
3. Latest file was `2026-05-12_17-16-42.md` — 24 hours old
4. `max_age_hours=6` check triggered → `"ok": false, "error": "latest wiki-health-plan output is stale"`
5. `wiki-health-fix` agent received `ok: false` → reported error, applied zero fixes

## Missed Fixes

wiki-health-plan (May 13, completed at 18:18) produced 16 auto-apply orphan_index actions. None were applied because wiki-health-fix had already skipped.

Manual application (this session):
- `entities/dex-horthy` — added to index.md
- `entities/merge-dev` — added to index.md (alphabetical position corrected after initial misplacement)
- `concepts/agentic-rag` — added to index.md
- `concepts/agentic-retrieval` — added to index.md
- `concepts/claude-opus-4-7` — added to index.md
- `concepts/death-of-browser` — added to index.md
- Section counts updated: Entities 582→584, Concepts 1249→1253

## Fix Applied

- `wiki-health-fix` schedule: `25 17 * * *` → `50 17 * * *` (40 min margin)
- `cronjob(action='update', job_id='6f3525ec4d9a', schedule='50 17 * * *')`

## Key Files

- `~/.hermes/scripts/wiki_health_plan_checkpoint.py` — pre-run script for wiki-health-fix
  - `find_plan_job_id()` — looks up job named "wiki-health-plan" in jobs.json
  - `is_fresh()` — checks mtime against MAX_AGE_HOURS (default 6)
- `~/.hermes/cron/jobs.json` — all cron job definitions
- `~/.hermes/cron/output/ac70e197fc75/` — wiki-health-plan output directory
- `~/.hermes/cron/data/wiki_health/plan_latest.json` — checkpoint written by successful runs
