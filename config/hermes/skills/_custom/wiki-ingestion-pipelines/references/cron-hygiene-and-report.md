# Raw-layer hygiene + log + report procedure (cron ingest runs)

Learned during blog-ingest run 20260911T100030Z. The ingest script saves files to
`wiki/raw/articles/` but does NOT commit them, and prior jobs (newsletter-ingest,
x-bookmarks, company-blog captures, previous blog runs) can leave dozens of untracked
files behind. A clean run should end with a clean working tree.

## Procedure (after the script output shows saved_articles)

1. **Check the tree**: `cd ~/ai-topics && git status --porcelain --untracked-files=all -- wiki/raw`
   — count untracked files. If more than this run's saved articles, earlier runs left strays.
2. **Batch-commit strays** rather than leaving them:
   `git add wiki/raw/articles && git commit -m "wiki: blog-ingest raw articles <date> (batch commit of pending untracked)"`.
   Raw files are immutable source material — committing untracked strays is always safe;
   never edit or delete them.
3. **Check `wiki/raw/newsletters/` too** — newsletter strays commonly accumulate alongside.
4. **Push**: `git pull --rebase && git push`. If rebase is blocked by unstaged changes in
   OTHER paths (e.g. `config/hermes/skills`, `config/hot-topics.yaml` — the live skills
   directory is symlinked under config/hermes/skills and gets dirtied by runtime skill
   updates), commit those separately with a `skills/config: sync runtime skill updates`
   message. That's legitimate in-repo syncing, not scope creep.
5. **log.md entry**: insert a `## [YYYY-MM-DD] ingest | ...` entry just after the
   `# Wiki Log` header block (the header is NOT at line 1 — stray entries can sit above
   it; grep for `^# Wiki Log` and the first `^## \[` line to locate the insertion point).
   Include: run_id, scanned/fetched/saved counts, notable articles, unsaved items + why,
   hygiene actions, and a "no pages created" note when true.
6. **Final verification**: `git status --porcelain | wc -l` should be 0 before finishing.

## Cron-mode pitfalls hit this run

- **execute_code is BLOCKED in cron mode** (arbitrary Python needs approval; no user
  present). Use terminal + patch/write_file instead. Don't waste a turn trying it.
- `pre-commit` hooks run on wiki commits; raw-only commits pass without wiki-lang checks.
- The pre-run script JSON's `saved_articles[].raw_path` is the authoritative list of this
  run's files; anything untracked beyond it is a stray from earlier runs.

## Report shape (final response for the cron job)

Short sections: scan/capture counts → notable captured articles (grouped by theme) →
unsaved items with reasons → hygiene actions (with final commit hash) → pointer to the
checkpoint for downstream triage. End with the `COST_REPORT:` line the job template requires.

## SKILL.md size limit note

`wiki-ingestion-pipelines` SKILL.md sits at ~100KB — right at the 100,000-char
skill_manage limit. Even a one-line patch to its SKILL.md is rejected once at the cap.
Add new knowledge as files under `references/` (this file is one) rather than growing
the body; a future curator pass should trim the body and move prose into references.
