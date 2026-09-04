# Git Push in Concurrent Pipeline Window

**Problem**: When multiple pipelines (blog-ingest, newsletter-ingest, sitemap-monitor, raw-backlog-ingest) run concurrently in the 07:00–07:50 UTC window, `git pull --rebase` can fail with:

```
error: cannot pull with rebase: You have unstaged changes.
error: Please commit or stash them.
```

The "unstaged changes" are typically from OTHER directories (config/hermes/skills/, inbox/, raw/) modified by concurrent Hermes agents and not by your current pipeline.

## Resolution

### Case 1: Commit already done, no upstream divergence
If you've already committed your wiki changes and `git status --short` shows only non-wiki dirty files:

```bash
cd ~/ai-topics && git push
```

Skip `git pull --rebase` entirely — there is no upstream divergence since your commit is local-only. The dirty working tree is from concurrent processes, not from changes you need to reconcile.

### Case 2: Need to pull before committing
If you need to integrate upstream changes before committing your own:

```bash
cd ~/ai-topics
git stash -- include/          # or stash individual non-wiki paths
git pull --rebase
git stash pop
```

Stash only the specific paths that are dirty, not all files. This avoids accidentally stashing your own wiki changes.

### Case 3: Clean commit first, won't worry about dirty tree
If your wiki commit is clean and you're the only one making wiki changes:

```bash
cd ~/ai-topics && git commit -m 'wiki: ...' && git push
```

Skip pull entirely — in the 07:00-07:50 parallel window, no other pipeline is pushing wiki changes that would conflict.

## Root Cause
The working tree at `/opt/data/ai-topics/` is shared among multiple cron pipelines running on the same host. Files modified by different processes (skill updates from the curator, newsletter ingest inbox files, raw article archives) create an "unclean" tree that blocks `git pull --rebase` even when those files are not wiki files.

## Validated
- Jul 25, 2026: newsletter-wiki-ingest hit this after parallel enrichment. Commit was done. Simply ran `git push` — worked.
- Aug 2, 2026: newsletter-wiki-ingest again — `git pull --rebase` failed with unstaged changes from sibling pipelines (skill updates, hierarchy_report.json), but `git push` succeeded (`7827c6e2..f98e117d`). Confirmed: when your commit is local-only and the dirty tree is non-wiki files from concurrent processes, skip pull entirely. Also: **stage only your own files** (`git add wiki/entities/... wiki/log.md`), not blanket `git add wiki/`, to avoid sweeping sibling pipelines' unrelated staged changes into your commit.
