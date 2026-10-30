# Watchdog session 2026-10-30 — transient-failure triage pattern

Context alert: `newsletter chain broken: triage_ok_but_wiki_ingest_failed`. jobs.json showed
7 jobs with `last_status: error` (blog-ingest/triage/wiki-ingest, newsletter-ingest/wiki-ingest,
x-bookmarks-ingest, dreaming-wiki-ingest).

## Root cause classification (all transient infra, NO action taken)

| Job | Error | Classification |
|---|---|---|
| blog-ingest, blog-triage, newsletter-ingest, x-bookmarks (11:30), dreaming-wiki-ingest | `HTTP 503: Local LLM server is busy; Hermes should fall back to the external provider.` | Transient — local LLM outage at ~10:20–11:31 UTC window |
| newsletter-wiki-ingest | `RuntimeError: Response truncated due to output length limit` (agent wrote a huge knowledge dump before COST_REPORT) | Transient output-length failure |
| pipeline-watchdog `triage_ok_but_wiki_ingest_failed` | chain check compares stage `last_status` | FALSE-POSITIVE for work-done purposes — see below |

## Key insight: triage_ok_but_wiki_ingest_failed ≠ lost data

The 10:30 newsletter-triage run **completed its own work** despite last_status ambiguity:
- triage checkpoint fresh: `/opt/data/.hermes/cron/data/newsletter/triage_latest.json` (10:37, 20 decisions / 2 take / 6 ref / 12 skip)
- its outputs committed & pushed: `64054ff1` (triage report), `a2c0d4d8` (raw digests + archive)
- the 2 "take" targets were later handled: `entities/dianne-na-penn.md` (5.7 KB, full content)
  created by the 15:06 wiki-graph-analysis session (commit `d8756c5f`), registered in index.

So the broken-chain alert reflected a *stage-status bookkeeping* gap, not data loss. **Before
re-running or escalating a broken-chain alert: check (a) triage checkpoint mtime, (b) today's git
log for the chain's commits, (c) whether take-target files exist on disk.**

## Verified clean (no fixes needed)

- validate_index.py exit 0 (3,375 lines); pipe/line-number/triple-bracket/double-pipe/space-prefix = 0
- L2 `|- [` scan (entities+concepts only) = 0
- log.md: exactly 1 `# Wiki Log`, 0 orphan `###` timestamps
- no-frontmatter scan across entities/concepts/comparisons/events/queries = 0
- empty-wikilink residual stable at 278 (baseline 279; 0 auto-fixable — leave it)
- xurl working (live API call OK), hooksPath = .githooks, working tree clean under wiki/

## Guidance for future runs

- A 503 "Local LLM server is busy" cluster in the 10:00–11:45 UTC window = local-model outage;
  jobs self-heal on next scheduled run. Do not restart pipelines for a single occurrence.
- 2 consecutive x-bookmarks errors would be the escalation threshold (1st was 503, prior run SILENT/ok).
- dreaming-wiki-ingest's error is also `failed to parse JSON response from dreaming-group output`
  wrapping a valid "# Dreaming Report" — same known JSON-parse-wrapper class as newsletter chain.
