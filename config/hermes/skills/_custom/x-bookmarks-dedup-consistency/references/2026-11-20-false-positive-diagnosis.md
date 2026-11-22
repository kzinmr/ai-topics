# Case study: false-positive x-bookmarks dedup diagnosis (2026-11-20)

## What was believed

A second cron job (wiki-watchdog) was told that the 2026-11-20 05:14 UTC
`x-bookmarks-ingest` run "saved 0 raw articles, 0 wiki page updates, no wiki
commit" and that 12 specific blog URLs (Harvey x4, Pinecone x3, Warp x2, Hex,
ElevenLabs x2) existed on disk but were never triaged.

## Why the belief was plausible

- `last_run` in `processed_x_bookmarks.json` showed
  `new_bookmarks: 0, x_articles_fetched: 0, stop_reason: already_processed_page,
  processed_cache_size: 526` - looks exactly like over-aggressive dedup.
- `wiki/log.md` had no `x-bookmarks-ingest` entry for 2026-11-20.
- The 12 filenames matched the `YYYY-MM-DD_owner_slug.md` convention used by
  `fetch_x_bookmarks.py` / `fetch_article.py`, and all 12 sat in
  `wiki/raw/articles/` with 06:00 mtimes.
- AGENTS.md's PATH TRAP warns that `$HOME=/opt/data/.hermes/home` writes are
  invisible to the wiki, which explains "raws written but never committed".
- `processed_x_bookmarks.json` exists at BOTH `/opt/data/.hermes/` and
  `/opt/data/home/.hermes/` (14622 bytes, mtime Nov 19 23:30 - the 23:30 UTC
  run). One is a decoy.

## What was actually true

- The 12 files are **sitemap-monitor** output, not bookmarks. Proof:
  `scripts/sitemap_monitor.py` line 214
  `filename = f"{date_str}_{owner_slug}_{title_slug}.md"` - the exact naming
  pattern of all 12 files (`harvey`, `pinecone`, `warp`, `hex-technologies`,
  `elevenlabs` are all monitored company blogs). `fetch_article.py` uses
  `{domain}--{path}--{hash}.md` instead.
- The sitemap-monitor pipeline genuinely ran at 06:00 and genuinely committed:
  `git log` shows `192c283a wiki: sitemap-monitor ingest - 12 new articles from harvey.ai, pinecone.io, warp.dev, hex.tech, elevenlabs.io`.
- The x-bookmarks job is an **agent** job (`fetch_x_bookmarks.py` has no cron
  `script` field - it is referenced only inside the prompt). Its own report at
  `/opt/data/.hermes/cron/output/56e7e85f45b1/2026-11-20_05-14-04.md` states
  verbatim: 526/526 tweet_ids cached, 0 new bookmarks, 0 raw articles, 0 page
  updates, "0 件のブックマークを処理しました（全件キャッシュ済み・新規なし）".
  `last_run.x_articles_fetched` also equals 0, consistent with nothing new.
- The 526-entry cache legitimately accumulated from 2026-05-14 through
  2026-11-19 (53 dated files under
  `/opt/data/.hermes/cron/data/x_bookmarks/`, latest 2026-11-19_23-30-03).
  Nothing was recorded "without matching raw articles".
- The "archive_index contained un-triaged URLs" claim also failed: a removal
  script reported `dropped 0, kept 0` because none of the 12 URLs were in the
  index at all.

## Actions taken that had to be undone

1. `processed_x_bookmarks.json` `tweet_ids` cleared 526 -> 0. Undone by
   restoring the `tweet_ids` list verbatim from the transcript's tool-result
   echo (526 ids, `20261119...` last entry, `last_run` dict preserved intact).
2. `archive_index.json` gained 12 fabricated skip entries (3295 -> 3307).
   Undone by `git revert --no-commit e68ca685` + commit, then
   `git checkout origin/main -- <reverted file>` to restore the 3295-entry
   state exactly (a plain revert would have clobbered a sibling
   `newsletter/2026-11-20_20261120T101025Z.json` created in the same window).
3. `wiki/raw/archived/triage/x_bookmarks/` (fabricated backfill dir) deleted.
4. The log.md entry's trailing cross-run-fix paragraph removed via a
   guarded Python line-anchored patch.

## Lessons

- **Read the job's own report before diagnosing it.**
  `cat ${HERMES_HOME}/cron/output/<job_id>/<run_id>.md` settles "did it run,
  what did it do" in one read and costs nothing. Do not infer from cache files.
- **Identify the producer of a file by its naming scheme**, then read the
  producing script. Two pipelines write into `raw/articles/` with different
  patterns; assuming provenance from "recently modified + plausible domain"
  produced the whole false diagnosis.
- **Treat "0 new items" as a valid outcome, not a bug.** An ingest job with a
  healthy cache and no new sources SHOULD produce 0 raws, 0 updates and no
  commit. `[SILENT]` is the correct response, per the skill's own rule.
- **Never mutate a dedup cache to force re-processing without first
  demonstrating that material was lost.** Wiping 526 ids would have re-fetched
  and re-triaged ~500 already-processed tweets.
- When undoing, prefer `git revert --no-commit` + `git checkout origin/main --`
  over hand-editing JSON, and always `grep` for the specific tokens you claim
  to have removed afterwards.
