# Cron-Mode Git Conflict from Sibling Pipeline Modifications

When multiple cron pipelines run concurrently in the 07:00-07:50 UTC window (blog-ingest, newsletter-ingest, etc.), sibling agents may modify non-wiki files (e.g., `config/hermes/cron/jobs.json`, skill files under `config/hermes/skills/`) **without committing them**.

## Symptom

The standard git workflow from AGENTS.md fails:

```bash
cd ~/ai-topics && git pull --rebase && git add wiki/ && git commit -m 'wiki: ...' && git push
# → error: cannot pull with rebase: You have unstaged changes.
#   Please commit or stash them.
```

## Cause

`git pull --rebase` requires a clean working tree. Sibling pipelines' uncommitted modifications to non-wiki files block the operation.

## Solution

Use `git stash` to temporarily shelve the sibling's changes, then restore after the rebase:

```bash
# 1. Stage only your wiki changes first
git add wiki/
# 2. Stash everything else (sibling's uncommitted changes)
git stash
# 3. Pull and rebase
git pull --rebase
# 4. Restore sibling's changes
git stash pop
# 5. Commit your wiki changes (sibling's unstaged changes are back)
git commit -m 'wiki: ...'
git push
```

Note: If `git stash` returns a warning about sibling subagent modification (e.g., `"warning: /tmp/log_entry.md was modified by sibling subagent"`), re-read wiki files before committing to confirm your content is intact.

## Why This Works

- `git stash` only affects the staging area and working tree — it does not touch committed history
- `git pull --rebase` operates on committed history only
- After the rebase, `git stash pop` restores the exact working tree state including sibling's uncommitted modifications
- Your wiki changes were already staged via `git add wiki/` before the stash, so they survive the stash/pop cycle

## Validated

July 2026: newsletter-wiki-ingest encountered this after blog-ingest sibling left `config/hermes/cron/jobs.json` and skill files modified. The stash → pull → stash pop → commit sequence resolved cleanly without merge conflicts.
