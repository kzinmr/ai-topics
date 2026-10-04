# Git staging pitfalls when other cron jobs dirty the repo — learned 2026-10-03

## Partial staging: git pull --rebase aborts; commit first, push second

When the ai-topics working tree is dirty from OTHER jobs (sibling subagents, concurrent cron pipelines writing `config/hermes/skills/...`, other wiki pages), `git pull --rebase` aborts with:

```
error: additionally, your index contains uncommitted changes.
error: Please commit or stash them.
```

Do NOT try to stash or clean other jobs' files. The working sequence:

1. Stage ONLY the files this scan touched (explicit paths, never `git add wiki/` broadly):
   ```bash
   cd ~/ai-topics
   git add wiki/entities/<touched>.md wiki/concepts/<new>.md wiki/index.md wiki/log.md
   ```
2. `git commit -m "wiki: <summary>"` — the pre-commit hooks run here (tag taxonomy, Japanese-content, index checks).
3. `git push`. If it is rejected non-fast-forward (another job pushed meanwhile), then `git pull --rebase` NOW succeeds because your own changes are committed — and push again.

Committing before syncing is safe in this repo: the pre-commit hooks are local-only, and a rejected push is recoverable. Fighting for a clean tree first is the trap.

## `~/wiki` and `~/ai-topics/wiki` are the SAME directory — never "sync copy"

In this deployment `~/wiki` is a symlink into the git repo:

```bash
readlink -f ~/wiki   # → /opt/data/ai-topics/wiki
```

Edits made through either path land directly in the canonical repo. Attempts to "copy/sync" wiki files from `~/wiki` to `~/ai-topics/wiki` (e.g. `ln -f` or `cp`) fail with "are the same file" or are pointless no-ops. If a previous session or skill text suggests a dual-directory copy step, skip it — verify with `readlink -f ~/wiki` once per environment and edit the canonical path. This also means `git status` inside `~/ai-topics` immediately shows every edit you made via `~/wiki/...` — no intermediate sync state to reconcile.
