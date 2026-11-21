# Maintenance claims need evidence before mutation (2026-11-20 case study)

During a newsletter-triage cron run, a second pipeline (`x-bookmarks-ingest`)
appeared broken. The "diagnosis" produced three destructive mutations before
any ground truth was read. All three had to be reverted. This file is the
durable lesson, not the incident.

## The failure mode

A cron job (`x-bookmarks-ingest`) reported: `new_bookmarks=0`, 0 raws, 0 wiki
page updates, no commit. That was read as a DEDUP BUG and "fixed":

1. `processed_x_bookmarks.json` -> `tweet_ids` cleared (526 -> 0)
2. 12 URLs written into `wiki/raw/archived/triage/archive_index.json`
3. A fabricated `.../triage/x_bookmarks/<date>_backfill.json` created

All wrong. A later verification pass (built as a PASS/FAIL script, see below)
exposed that the premise was never true.

## Why each claim was false — and the check that catches it in one call

| Claim | Reality | One-call verification |
|---|---|---|
| "The job lost 12 raw articles" | The 12 files are sitemap-monitor output, already committed | `cat ${HERMES_HOME}/cron/output/<job_id>/<run>.md` — the job's OWN report says `new_bookmarks=0` |
| "Those files came from x-bookmarks" | Two pipelines write `raw/articles/` with DIFFERENT filename schemes | Read the producing script. `sitemap_monitor.py` = `{date}_{owner}_{slug}.md`; `fetch_article.py` = `{domain}--{path}--{hash}.md`. Provenance by filename pattern, never mtime + plausible domain |
| "12 URLs are indexed but never triaged" | None were in `archive_index.json` at all | The removal script printed `dropped 0, kept 0` — that IS the disproof. Run the read-before-write probe and READ its output |
| "The 526-id cache was poisoned" | It accumulated legitimately over ~5 months (53 dated outputs) | `ls ${HERMES_HOME}/cron/data/x_bookmarks/` — dated output history |
| "Those files were never committed" | `git log` showed the sitemap-monitor ingest commit | `git log --oneline -10 -- <dir>` |

## Durable rules

- "0 new items" is a valid outcome, not a bug. An ingest job with a healthy
  cache and no new sources SHOULD write 0 raws, 0 updates, no commit. The right
  response is `[SILENT]`. Never force remediation to avoid an "empty" run.
- Read the job's own report before diagnosing that job.
  `${HERMES_HOME}/cron/output/<job_id>/<run_id>.md` answers "did it run, what
  did it do" in one read. Do not infer behaviour from cache/JSON files.
- Never mutate a dedup cache to force re-processing without demonstrating that
  material was lost. Wiping 526 ids = re-fetch + re-triage ~500 already
  processed tweets. The fix for "did it process X" is a read, not a reset.
- Identify a file's producer by its naming scheme, then read that script.
  Multiple pipelines share `raw/articles/`.
- Distinguish cron jobs by kind: a `script` job runs deterministically; an
  AGENT job (script referenced only inside the prompt) produces a markdown
  report. Their "success" signals differ — an agent job with nothing to do is
  correct, and its cache is managed by the script it calls, not by you.

## Revert mechanics that worked

- Do NOT `git revert` a mixed commit. The bad commit bundled
  `archive_index.json` (needed revert) with an archive file (needed delete);
  reverting the whole thing clobbered a sibling archive created in the same
  window. Instead: `git rm --cached <fabricated file>` + commit for the file,
  and `git checkout <good-commit>^ -- <shared file>` for the shared JSON.
- Restore a hand-mutated JSON from git, not by hand — `git checkout
  <pre-mutation-commit> -- wiki/raw/archived/triage/archive_index.json` gives
  the exact prior state (verified back to 3295 entries). A hand-written
  "remove these 12" script silently missed one (an assertion caught it: got 11).
- Write a PASS/FAIL verification script and run it after any revert. It caught
  two residues `git status` cannot show: an empty `triage/x_bookmarks/`
  directory (git doesn't track dirs) and a stale `last_run.note`. Guard
  `os.path.isdir` on a path whose parent was deleted.

## Recovering wiped cache contents

When a cache file was emptied and you need its prior contents: search the cron
output reports (`cron/output/<job_id>/*.md`) — AGENT jobs echo the file they
read as a tool result, so the full list is often recoverable from the last
successful run's markdown via a JSON-object regex. (Here the relevant report
was a SCRIPT job with no echo, so recovery was impossible — the reset's cost
was a one-off full re-fetch, which is harmless. Verify recoverability BEFORE
promising restoration.)
