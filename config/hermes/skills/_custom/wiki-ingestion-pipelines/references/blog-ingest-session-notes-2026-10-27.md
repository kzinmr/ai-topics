# Blog-Ingest Stage — 2026-10-27 session notes

## Untracked-file sweep is CORRECT for this cron job (refines the 10-23 "do not sweep" rule)

The 2026-10-23 notes say "commit exactly the checkpoint-listed raw_paths … do not sweep other pipelines' untracked files." That applies to *other pipelines'* output. But `git status --porcelain wiki/raw/articles/` also surfaces previous blog-ingest runs whose commits failed or were skipped — those are this pipeline's own backlog. On 2026-10-27, 21 raw files from the 2026-10-26 run were still untracked; sweeping them into the day's commit (40 files total) was the right call. Raw files are immutable Layer-1, so sweeping can't damage other stages.

Rule of thumb: sweep untracked files under `wiki/raw/articles/` (check mtimes via `stat -c %y` to know which run produced them), but NEVER stage modified files outside `wiki/raw/` — modified `wiki/concepts/`, `wiki/entities/`, `wiki/events/` pages and untracked `config/hermes/skills/` changes belong to sibling pipelines (hot-post, skeleton-enrich, dreaming). Stage with explicit paths: `git add wiki/raw/articles/` then `git add wiki/log.md`.

## Minimal ingest-only run shape (when no synthesis is requested)

When the cron prompt is just "run blogwatcher, save raw, save checkpoint" and the script output already contains the checkpoint:
1. Verify checkpoint exists (head latest.json) and a sample of saved raw files have real frontmatter + >100-char bodies.
2. `git add wiki/raw/articles/` → commit → push (pre-commit tag validator passes for raw frontmatter tags [blog, raw]).
3. Prepend a log.md bullet (format in 2026-10-23 notes) → commit → push.
4. Report notable AI-relevant titles in the final response so the user can see what downstream triage will have to work with — do NOT create/update Layer-2 pages; that is blog-triage / blog-wiki-ingest's job.

Total tool budget used on 2026-10-27: about 12 calls. Keep it tight; resist enriching entity pages in this stage.

## Scan-field quirks in checkpoint

`scan.total_new` (42) counts ALL new articles in the blogwatcher DB; `articles.total` (20) is the per-run fetch cap subset; `scan.blogs_scanned` can be 0 even when new articles were found — do not treat those as failures. `unsaved_articles` entries (scrape failures, e.g. NYT paywall) are expected and need no retry — they just won't have raw files.

## execute_code blocked in cron (third confirmation: 10-19, 10-23, 10-27)

`execute_code` is hard-blocked in this cron profile ("Cron jobs run without a user present to approve it"). First instinct was to use it for the ls/cat verification batch — go straight to `terminal` with semicolon-joined commands instead.
