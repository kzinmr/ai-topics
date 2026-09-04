# Blog-Wiki-Ingest Recovery — 2026-07-31 (archive-already-run sub-variant)

Validated in the blog-wiki-ingest cron job on 2026-07-31. Extends the
"Triage Agent Saves JSON Before Response Render Failure" pattern with the
finding that the upstream triage agent may ALSO have completed the archive
step before its response render failed.

## Trace

- blog-triage cron output failed: `{"ok": false, "error": "failed to parse JSON response from blog-triage output", "output_path": "/opt/data/.hermes/cron/output/<job-id>/2026-07-31_10-29-22.md"}`
- Checkpoint at `/opt/data/.hermes/cron/data/blog_ingest/triage_latest.json` was valid JSON:
  `checkpoint_run_id: 20260731T102328Z`, `triage_timestamp: 2026-07-31T10:30:00Z`, 20 decisions
  (1 take, 9 references, 10 skips).
- Archive at `wiki/raw/archived/triage/blog/2026-07-31_20260731T102328Z.json` ALSO existed:
  `archived_at: 2026-07-31T10:28:39Z` — 59 seconds BEFORE the render failure — with 19
  decisions (the skip+reference subset).

## Action in recovery path

1. Read `triage_latest.json` directly (no extraction, no re-run) — as per the main pattern.
2. Before re-running `archive_triage.py {pipeline} --keep-reference`, check whether
   `wiki/raw/archived/triage/{pipeline}/{date}_{checkpoint_run_id}.json` already exists.
   If present, verify it (decisions count) and SKIP re-running — the archive script would
   dedup-skip everything anyway, and re-running risks touching `archive_index.json` a second time.
3. Verification snippet (no pipe-to-interpreter):
   `python3 -c "import json; d=json.load(open('wiki/raw/archived/triage/blog/2026-07-31_20260731T102328Z.json')); print(d.get('triage_run_id'), len(d.get('decisions',[])))"`

## Post-recovery verification (unchanged from skill)

- All 6 candidate pages existed → every decision was an enrichment, zero creations.
- Confirmed genuine gaps by reading each page's relevant sections, not just frontmatter:
  e.g. `concepts/gpt/gpt-5-6.md` pricing table was launch-only (Jul 15 update, no Jul 30 price
  cut); `entities/simon-willison.md` July 2026 Updates section ended Jul 28.
- Enriched rich pages with `patch()` (never `write_file` for >40-line pages).

## Git staging discipline in parallel pipeline windows

- Worktree contained pre-existing dirty files from sibling processes
  (`config/hermes/skills/_custom/...` modified/deleted) plus ~255 untracked files
  (raw articles, newsletters, archives).
- Staged ONLY `wiki/`: `git add wiki/` → verify `git diff --cached --name-only | wc -l`
  and eyeball the list contains only wiki paths → commit → push.
- Do NOT use `git add .` / `git add -A` in the 07:00–07:50 pipeline window; sibling
  skill-config changes would be swept into the wiki commit and may trip pre-commit hooks.
- Result: 35 files staged (6 pages + log.md + 2 archives + today's raw articles/newsletters),
  commit pushed cleanly (pre-commit hooks passed: tag taxonomy + index validation).

## Sibling-subagent patch warning (benign)

- `patch()` on `entities/seangoedecke-com.md` warned: "was modified by sibling subagent
  ... but this agent never read it." The patch still applied correctly because old_string
  was a unique, grep-verified anchor.
- Rule for parallel pipeline windows: verify old_string uniqueness with grep before
  patching; read the sibling warning but proceed if the applied diff is correct.
