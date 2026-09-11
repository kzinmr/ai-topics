# Watchdog session 2026-09-07 — concurrent-writer scoping + index count sync

## What ran clean (baseline behavior confirmed)
- Pipeline watchdog: 0 alerts, report 5.6h old → normal. wiki-graph-analysis 74h old is NOT stale — the job runs weekly (Fri), so age up to ~168h is expected cadence. Don't flag it as stale.
- Index corruption live re-verify: line-number/pipe/triple-bracket prefixes = 0, validate_index.py passed. (Report claims must always be re-verified live — upstream wiki-health-fix may have repaired them.)

## Index count drift pattern (reconfirmed)
- index.md header said 3031 / Entities 920 / Concepts 2038; filesystem had 3033 / 922 / 2040.
- Root cause: morning trending-topics commits added pages and registered SOME in index.md but skipped the header counts and skipped one page entirely (`concepts/agent-platform-capability-composition`, created after the 12:00 index commit).
- Fix recipe: recompute counts from filesystem (find-verified), verify HEAD snapshot truly lacked the entry (`git show HEAD:wiki/index.md | grep -c <slug>` returns 0) before registering, insert alphabetically, run validate_index.py, commit only index.md + log.md.

## Concurrent-writer git hygiene (the key lesson)
- Working tree had 8 modified + ~40 untracked wiki files owned by ingestion pipelines RUNNING CONCURRENTLY. Do NOT stage them.
- Scoped staging: `git add wiki/index.md wiki/log.md` (explicit paths, never `git add -A` or `git add wiki/`).
- `git stash push -- <paths>` + pop is a safe way to test HEAD state of only your files while leaving others' work untouched.
- `git pull --rebase` fails with unstaged changes elsewhere in the tree — that's fine: plain `git push` still succeeds when remote hasn't moved (fast-forward). Don't stash-everything just to pull; try push first.
- Pre-commit hooks (validate_index + tag validator) pass when only clean staged files are involved.

## Tag-validation false-positive trap
An upstream review step reported new pages' tags as BAD against a "valid tag count: 666" list. Direct re-check against freshly-parsed SCHEMA.md showed the tags were valid — the reviewer's taxonomy list was stale. When judging tag validity of uncommitted pages, parse SCHEMA.md yourself (both backtick and bold-category formats) rather than trusting a checkpoint's tag list.

## Scope discipline honored
- 2,683 broken wikilinks: fix requires CREATING hub pages (agent-evaluation, rag, gemini, cursor) — watchdog must not create pages; report as recommendation (creating the top 5 hubs resolves ~140 links).
- 117 dup groups / 468 orphans: assigned to weekly wiki-graph-analysis, not watchdog.
- Missing-`sources` pages: needs-human class, leave flagged.
