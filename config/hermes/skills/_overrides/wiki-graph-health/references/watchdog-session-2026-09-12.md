# Watchdog Session — 2026-09-12

## Context delivered by pre-run script was partly useless
- `wiki_health: null` (no report) → ran `~/ai-topics/scripts/wiki_health_json.py` directly (0.3s, works from any cwd when invoked with explicit path). Output keys: `overview`, `page_name_policy`, `orphan_count`, `orphans`. All 23 orphans were `_index.md` hubs + `concepts/gpt/_archive/` files — known false positives, no action.
- `wiki_graph_analysis` context "sample_issues" were just llm-wiki skill boilerplate — the weekly graph job itself had FAILED (HTTP 503). Don't mine a FAILED job's response preview for real findings; check `last_status` first.

## Authoritative job-failure source when `hermes` CLI is unavailable
`hermes` was not on PATH in the cron session (`command not found`). Do NOT waste turns hunting for the binary. The canonical fallback:
```bash
python3 -c "
import json
d=json.load(open('/opt/data/.hermes/cron/jobs.json'))
for j in d['jobs']:
    print(j.get('name'), '| enabled:', j.get('enabled'), '| last_status:', j.get('last_status'),
          '| last_run:', j.get('last_run_at'), '| err:', str(j.get('last_error'))[:150])
"
```
File shape: `{"jobs": [...], "updated_at": ...}`. Each job has `name`, `enabled`, `last_status` (ok|error), `last_run_at`, `last_error`. This gives per-job error messages the pipeline_watchdog summary truncates.

## Two systemic failure classes seen 2026-09-12 (report, do NOT auto-fix)
1. **Context-length-exceeded** — `RuntimeError: Context length exceeded (48K–79K tokens). Cannot compress further.` hit 6 ingest-class jobs in one day: newsletter-triage, newsletter-wiki-ingest, blog-wiki-ingest, x-bookmarks-ingest, active-crawl, dreaming-wiki-ingest. Root cause is oversized checkpoint payloads vs the configured model window — a config/payload-size problem (model budget or checkpoint script trimming), never a watchdog auto-fix. When newsletter-ingest is `ok` but newsletter-triage is `error`, that IS the `ingest_ok_but_triage_failed` chain-break alert.
2. **HTTP 503 "Local LLM server is busy; Hermes should fall back to the external provider"** — hit wiki-health-fix, wiki-graph-analysis, x-accounts-scan. The fallback apparently doesn't engage; failures cascade (a failed wiki-health-fix means the watchdog's expected upstream fix pass didn't happen — do the verification yourself, which was already the rule).

Both classes: report to human with the per-job table; do not retry jobs, do not edit cron config autonomously.

## Index header recompute (worked example)
Header counts decayed: `Total pages: 3039` and `## Concepts (2041 pages)` while the index actually had concepts=2046. Recompute per namespace from index lines, NOT filesystem:
```python
import re
idx = open('wiki/index.md').read()
for ns in ['entities','concepts','comparisons','events','queries']:
    print(ns, len(re.findall(r'^- \[\[%s/' % ns, idx, re.M)))
```
Total pages = sum of the five counts (3042 here). Fix headers, run `python3 scripts/validate_index.py`, log, commit only index.md + log.md.

## Concurrent sibling agent in same worktree
A sibling ingest session had uncommitted changes (new concept pages + edits to 5 pages) in `~/ai-topics` while the watchdog ran. Rules that worked:
- Stage ONLY your own files (`git add wiki/index.md wiki/log.md`), never `git add wiki/` or `-A`.
- `git pull --rebase` fails with "You have unstaged changes" when siblings dirty the tree — plain `git push` is fine if it fast-forwards (it did). Don't stash other agents' work.
- Expect the `patch` tool "modified by sibling subagent" warning on index.md; verify your edit landed with a follow-up read/grep rather than rewriting the file.
