# Parallel-Cron Git Push: Rebase Blocked by Sibling Unstaged Changes

Validated 2026-08-07 (newsletter-wiki-ingest, 10:40 UTC run).

## Symptom

In the parallel pipeline window (07:00-11:00 UTC), after committing wiki changes:

```
$ git pull --rebase
error: cannot pull with rebase: You have unstaged changes.
error: Please commit or stash them.
```

The unstaged changes are **sibling agents' edits** (typically `config/hermes/skills/` skill maintenance from blog-wiki-ingest, raw-backlog-ingest, or the skill curator) — NOT your wiki changes.

## Correct action

1. **Commit your wiki changes first** (`git add wiki/ && git commit`).
2. **Do NOT stash or commit the siblings' changes** — they belong to other pipeline runs and will be committed by their own agents.
3. **Run `git push` directly** — it succeeds if your local HEAD is based on the latest origin. The rebase was only needed to merge remote commits; if origin hasn't moved since your branch point, push works without it.
4. **Verify sync**:
   ```bash
   git log --oneline -1          # local HEAD
   git log --oneline origin/main -1   # remote HEAD — must match
   git status                     # "up to date with 'origin/main'" + sibling changes listed as unstaged
   ```
5. Leave the sibling unstaged changes in place — they are not yours to commit.

## Observed result

Pushed `ddca2b21..c6b8f0ef main -> main` after the blocked rebase; `git status` confirmed "up to date with 'origin/main'" with the skill-file changes still unstaged (correctly untouched).

## Related
- This is the *commit-side* variant of the sibling `/tmp/` race documented in the main SKILL.md (unique filenames for `/tmp/` scripts). Same root cause: concurrent agents in one repo.
- If push DOES fail (non-fast-forward), then origin moved and you must rebase: `git stash push -u config/ && git pull --rebase && git stash pop` — but only do this if push actually failed; most parallel-window pushes succeed without it.
