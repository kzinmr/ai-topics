# Blog Wiki Ingest — Duplicate-Invocation Recovery Reference Gap (2026-08-12)

## Scenario
- blog-wiki-ingest cron run failed upstream: `failed to parse JSON response from blog-triage output`
- Checkpoint recovery per standard pattern: `triage_latest.json` was valid (20 decisions, run 20260812T101753Z)
- Triage summary stated a prior run (commit 5fd460f3, same day 10:24) already processed the same checkpoint ("実行済み決定をミラーリング")

## The trap
The prior run DID execute the take + housekeeping:
- Take: `entities/ryan-greenblatt.md` + `entities/redwood-research.md` created; `concepts/recursive-self-improvement.md` (+35 lines, RSI debate, median 2031); `entities/dwarkesh-patel.md` updated; `index.md` updated
- Raw articles (20) + archive committed in f1b3d539

**BUT the sole REFERENCE decision was silently dropped.** blog-8 ("There are no lossless transformations of natural-language text", Simon Willison) → `entities/simon-willison.md` was absent from the prior commit. `grep lossless wiki/entities/simon-willison.md` → no match, even though the triage summary claimed "Reference 1件" was handled.

## Decisive verification
```bash
git log --oneline -5          # find the prior run's commit
git show --stat 5fd460f3      # does EVERY non-skip candidate_wiki_path appear in the diff?
grep -n "keyword" wiki/entities/<target>.md   # confirm the specific content is present in-page
```
Check **takes AND references** — the prior run may have executed one and dropped the other. The commit diff is evidence; the triage summary text is not.

## Resolution performed
- Added the reference entry to `entities/simon-willison.md` **August 2026 Updates** section (Sophie Alpert's AI-writing policy: "You must stand behind every idea and every sentence in your docs"; no-lossless-transformations thesis; cross-links to the Meat Proxy and Technical Blogging entries; `[[concepts/agentic-engineering]]` link)
- Added the raw article filename to the frontmatter `sources` array by patching the **tail** of the long single-line sources array. Pitfall: the filename also appears in the body as a wikilink ending `]]` — the plain `]` matches both. Include the preceding `, ` in `old_string` for uniqueness
- Prepended a log.md recovery entry (newest-first, insert after the `_Log of all wiki changes...` header line)
- Commit + push succeeded (e10052e5)

## Git: pull --rebase blocked by pre-existing unstaged tracked changes
- After committing, `git pull --rebase` failed: `cannot pull with rebase: You have unstaged changes`
- Cause: other pipelines/processes share the repo and leave tracked files dirty (here: `config/hermes/skills/*` modified by skill-drift / concurrent jobs) — not files touched by this run
- Fix (pathspec-limited stash):
```bash
git stash push -m "temp stash for rebase" -- config/hermes/
git pull --rebase
git stash pop
git push
```
- If the remote is not ahead, the rebase is a no-op and `git push` succeeds as a fast-forward regardless of the pull failure
- Do NOT commit other pipelines' dirty files into your wiki commit — use targeted `git add wiki/<files>` only
- Untracked files (inbox/, raw/newsletters from sibling pipelines) do NOT block `pull --rebase`; only modified **tracked** files do
