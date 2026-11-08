# Watchdog session — 2026-11-03 17:35 UTC (clean run, 0 fixes)

Outcome: fully healthy wiki, no auto-fixes. Only action = log.md prepend + commit `fde27f38`.
This file records the verification path and triage verdicts so future runs can shortcut.

## Alert triage (pre-run digest: 2 alerts)

1. `JOB x_accounts: stale(26h)` → **FALSE POSITIVE.** Schedule is `30 22 */2 * *`
   (every-2-days). jobs.json: `last_status: ok`, last run 2026-11-01 22:35 UTC; next due
   22:30 the evening of the watchdog run. Confirmed via
   `cron/data/x_accounts_scan_state.json` → `updated_at` matches last run.
   (Matches the documented every-2-days false-positive pattern, watchdog-session-2026-09-28.)
2. `blog chain broken: ingest_ok_but_triage_failed` → **TRANSIENT infra.**
   blog-triage (10:28) + blog-wiki-ingest (10:40) + dreaming-wiki-ingest (11-02 18:20) all
   carry the SAME `last_error`: `RuntimeError: HTTP 503: Local LLM server is busy; Hermes
   should fall back to the external provider.` One infra event, one diagnosis. 17 saved raw
   articles from blog-ingest run `20261103T100059Z` left untriaged; tomorrow's 10:20 run
   recovers them. Escalated to human ONLY as "inspect provider-fallback config" (fallback
   claimed in error text but job died). Did NOT self-ingest the backlog (that recipe is for
   failures NOT expected to self-recover next day; this one is).

## Verification commands that returned clean (use as the healthy-baseline probe set)

```bash
cd ~/ai-topics
grep -c '^|- \[\[' wiki/index.md                      # 0 (pipe)
grep -Pc '^\s*[0-9]+\|' wiki/index.md                 # 0 (line-number) — use -P, BRE parses \| as alternation
python3 -c "print(open('wiki/index.md').read().count('[[['))"   # 0 (triple bracket)
grep -c '^ - \[\[' wiki/index.md                      # 0 (space-prefix)
python3 scripts/validate_index.py                     # exit 0, 3409 lines
grep -c '^# Wiki Log' wiki/log.md                     # 1
grep -c '^### 2026-' wiki/log.md                      # 0 (orphan timestamp lines)
```

Plus a top-level-only index-coverage + frontmatter scan (filter `'/' not in relpath`,
per the 2026-08-13 nested-by-design lesson) → 0 unindexed, 0 missing-frontmatter against
953 entities / 1,694 concepts.

## New technique: jobs.json `last_error` batch query (primary chain-alert triage)

`hermes cron list` printed NOTHING with exit code 0 this run — silent empty, not an error.
Recovered by querying jobs.json directly:

```bash
python3 -c "
import json
d=json.load(open('/opt/data/.hermes/cron/jobs.json'))
jobs=d if isinstance(d,list) else d.get('jobs',[])
for j in jobs:
    n=j.get('name','?')
    if any(x in n for x in ('blog','x_accounts','x-accounts','wiki')):
        print(n,'| enabled:',j.get('enabled'),'| last_status:',j.get('last_status'),
              '| last_run:',str(j.get('last_run_at'))[:19],'| schedule:',j.get('schedule'))
"
```

- `last_error` field carries the full RuntimeError string per job — three identical 503s
  collapsed three alerts into one diagnosis without opening any cron output file.
- Per-job detailed output: `ls -t /opt/data/.hermes/cron/output/<hash-id>/ | head -1`
  then `head -6` (hash id = `id` in jobs.json; first lines show `# Cron Job: <name> (FAILED)`).
- `find ~/.hermes/cron/data -maxdepth 1 -type d` to learn actual checkpoint dir names —
  `newsletter-triage` (hyphen), `blog_ingest` (underscore), `triage_latest.json` lives
  INSIDE `blog_ingest/` (no separate blog-triage dir).

## Misc confirmations

- Snapshot counts (953/1,694) matched live filesystem and index coverage — no sibling
  index-recount race this run (`git log -1 -- wiki/index.md` showed reconciliation
  already done at `3410de36` earlier today).
- Staging hygiene: repo had 70+ dirty sibling files (skills dirs) — staged ONLY
  `wiki/log.md`; pre-commit tag validator passed normally (no tag/language blocks).
- Log prepend via /tmp script (write_file → `python3 /tmp/wd_log.py`) worked; the
  write_file `_warning: modified by sibling subagent` on /tmp/wd_log.py was a stale
  notice for a file I had just written myself — harmless, verified by read-back.
- `# Wiki Log` substring count said 2 (prose mention in an old entry) while
  `grep -c '^# Wiki Log'` said 1 — trust only the anchored grep (now in SKILL.md).
- Weekly graph analysis 98h old (Friday cadence, `0 15 * * 5`) — correctly deferred its
  172 auto-fixable links / 4 dup merges / 8 missing stubs to Friday's run and the
  17:50 wiki-health-fix, did not act on stale graph data.
