# Blog-Ingest Stage Execution Notes (2026-08-28 session)

> Referenced from SKILL.md's "Blog ingest" pipeline section: read this file when running or debugging the blog-ingest cron agent stage. (SKILL.md itself could not carry the pointer — it is at the 100K char cap and needs a size-reduction pass first.)

## execute_code is BLOCKED in this cron profile
`execute_code` returns "BLOCKED: ... Cron jobs run without a user present to approve it" (approvals gate). Do not attempt it — use plain `terminal`, `read_file`, `patch` calls instead. The system prompt suggests execute_code but the runtime denies it here.

## Triage heuristics that worked (2026-08-28)
Saved 16/20 articles; wiki updates on 3 pages only. Priority filter:
- UPDATE existing pages, never create new pages for a single daily batch:
  - security incident vs. product capability page → patch the capability section with a **Contested (date):** bullet, keep original claims (AGENTS.md "矛盾を消さない" rule)
  - same-author follow-up article → new bold sub-paragraph in the person's Core Ideas section + add raw path to frontmatter `sources:` + bump `updated`
  - concept page → add a dated `## Case Study:` section near the end, before Open Problems/See Also
- Skip-as-raw-only: consumer/politics items from aggregator blogs (daringfireball relays), book reviews, math trivia, non-AI tooling posts, foreign-language policy posts.

## Git commit pattern for the batch
The script output lists `raw_path`s; commit exactly those + the edited Layer-2 pages + `wiki/log.md`. Untracked files from OTHER pipelines (e.g. `2026-08-28_<source>_*.md` from x-bookmarks/newsletter) also sit under `?? wiki/raw/articles/` — do NOT sweep them into this commit; enumerate paths explicitly (the `-- wiki/` pathspec with explicit file list works). pre-commit hook runs index.md validate + tag validator; commit succeeded without index.md changes when only existing pages were patched.

## Log line format
One bullet in wiki/log.md: `- YYYY-MM-DD HH:MM UTC — blog-ingest: N new articles; M saved, K unsaved (<reasons>). **Priority wiki ingest (X)**: per-page what/why. **Skip as raw-only**: list.`

## Link style inside wiki pages
Cite raw sources inline as `[[raw/articles/<filename>.md]]` wikilinks; cross-link related entities/concepts (`[[entities/micahflee]]`, `[[concepts/prompt-injection]]`) — the case-study section should triangulate person ↔ concept ↔ product pages.
