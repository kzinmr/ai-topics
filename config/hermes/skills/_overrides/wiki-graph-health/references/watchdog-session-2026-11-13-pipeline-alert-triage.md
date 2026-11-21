# Watchdog session 2026-11-13 — pipeline alert triage (stale x-accounts, newsletter 503 chain)

Two pipeline-alert classes the watchdog handled that the SKILL.md watchdog section didn't cover.

## Class 1: `x_accounts: stale(Nh)` — REAL, not false positive. The `*/2` schedule trap.

The existing `watchdog-session-2026-09-28.md` note says `stale(Nh)` with an every-2-days schedule is a false positive **if `last_status: ok`**. That rule is incomplete: it assumes the schedule actually fires every 2 days.

**This run it was REAL**: last successful scan 2026-11-11 22:30 UTC, ~43h stale at report time (context said 26h, it had grown). Two compounding causes:
1. The job's cron expr was `30 22 */2 * *` — `*/2` in the **day-of-month** field means "days 1,3,5,...,31", which SKIPS runs at each month boundary (31→1 transition can land on an even day). It does NOT mean "every 2 days".
2. The 2026-11-13 22:30 window was missed outright (scheduler/skip behavior).

**Triage procedure** (follow before touching anything):
1. `cat ~/.hermes/cron/data/x_accounts_scan_state.json` → `updated_at` is the ground-truth last success. Compare with `date -u`.
2. Read the job's schedule + state from `~/.hermes/cron/jobs.json`:
   ```bash
   python3 -c "
   import json; d=json.load(open('/opt/data/.hermes/cron/jobs.json'))
   jobs=d if isinstance(d,list) else d.get('jobs',[])
   for j in jobs:
       if 'x-accounts' in j.get('name',''): print(j['id'], j['schedule']['expr'], j.get('state'), j.get('last_status'))"
   ```
3. Verify the data source is healthy: `xurl /2/users/me` (quick auth probe; a 200 response = credential/API fine, so staleness is scheduling, not auth).
4. If genuinely missed: change schedule to daily `30 22 * * *` — this also **aligns with the staleness detector's every-2-days expectation**, eliminating future ambiguity. Day-of-month `*/N` expressions should be treated as a latent bug, not the intended cadence.

**Safe jobs.json edit recipe** (cron jobs live OUTSIDE git — backup first):
```bash
cp ~/.hermes/cron/jobs.json ~/.hermes/cron/jobs.json.bak-watchdog-$(date +%F)
python3 - <<'EOF'
import json, os
p = os.path.expanduser('~/.hermes/cron/jobs.json')
d = json.load(open(p))
jobs = d if isinstance(d, list) else d.get('jobs', [])
for j in jobs:
    if j['id'] == '<job-id>':
        j['schedule']['expr'] = '30 22 * * *'
        j['schedule']['display'] = '30 22 * * *'
json.dump(d, open(p,'w'), indent=2, ensure_ascii=False)
EOF
```
Verify by re-reading expr + `state: scheduled`. (`hermes cron list` may output nothing useful — jobs.json is the authoritative source.)

## Class 2: newsletter chain `ingest_ok_but_triage_failed` — HTTP 503, fallback not engaging

**Signature**: `RuntimeError: HTTP 503: Local LLM server is busy; Hermes should fall back to the external provider.` at the bottom of `~/.hermes/cron/output/<job-id>/<date>.md` (under `## Error`). Repeats daily while `last_status: error`.

**Triage path**:
1. `cat ~/.hermes/cron/data/newsletter/latest.json` — if `ok: true` with fresh `collected_at`, ingest is healthy; only downstream stages are down. The chain-break alert is then accurate.
2. Read the 2–4 newest outputs in `~/.hermes/cron/output/<triage-id>/` and `<wiki-ingest-id>/` — check whether the 503 is a one-off or consecutive-day failure (this run: 4 consecutive days, both `newsletter-triage` AND `newsletter-wiki-ingest`).
3. Check model config in jobs.json: both jobs had `model: null, provider: null` (inherit defaults) — which is why the promised external-provider fallback never engaged.

**Watchdog decision rule**: this is NEEDS-HUMAN, not auto-fix.
- Do NOT force-rerun the chain (the failure is provider infra; a rerun at the same time just 503s again).
- Do NOT auto-set `provider`/`model` on jobs — cron model config is a config-safety boundary (see `cron-job-management`).
- The checkpoint (`latest.json`) is NOT consumed until wiki-ingest succeeds → **no data loss**, backlog self-heals on recovery. Report the accumulated unprocessed `processed_count` so the human sees the backlog size.
- Suggest the human either fix local LLM health at the job's scheduled hour (10:30–10:55 UTC here) or set explicit external provider/model on the two jobs.

## Misc verified this run
- When `wiki_health` context is `null` and live grep confirms index clean (pipe/line-number/triple = 0, `validate_index.py` exit 0), there are no lint auto-fixes due — report and move on; don't invent work.
- The 2.5h-old weekly graph report (460 orphans tracking new pages 1:1, 0 actionable dups, 149 bare→namespaced links) needed no watchdog action — the weekly run already routed those to its own queue. Check the report's own "actions/routing" section before duplicating fixes.
- log.md prepend via `python3 - <<'EOF'` heredoc through terminal worked cleanly (execute_code blocked in cron mode; the heredoc has no backticks in content, so no bash substitution risk — keep backticks out of heredoc payloads or use write_file + python3 /tmp/script.py).
