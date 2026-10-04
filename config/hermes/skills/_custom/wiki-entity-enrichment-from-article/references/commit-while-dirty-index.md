# Committing Wiki Changes in a Shared-Repo, Cron-Concurrent Environment

The ai-topics wiki repo is edited concurrently by Hermes sessions and cron
ingestion pipelines. Mass `git add wiki/` during a manual ingest will sweep
hundreds of unrelated in-flight cron changes into your commit, and pre-commit
gates may then BLOCK your legitimate commit for reasons you can't control.
This file records the recovery/avoidance recipes (verified 2026-10-02).

## Rule 1: Never `git add wiki/` blindly

Check `git status --short | grep -v "^ M" ` and stage ONLY your own files by
explicit path. If the pre-commit hook fails due to files you never touched:

```bash
git reset -q                      # unstage everything
git add <your files, explicit>    # stage only your own
git commit -m "..."
```

## Rule 2: Pre-commit gates and how to satisfy them

- **Tag taxonomy** (`.githooks/pre-commit-tag-validator.py`): every frontmatter
  tag must be in SCHEMA.md's `## Tag Taxonomy`. If unrelated staged pages carry
  non-canonical tags (e.g. `ai-agent` vs canonical `ai-agents`, `devtools` vs
  `developer-tools`, `genai` vs `generative-ai`, `ai-coding-tools` vs
  `ai-coding`, `ai-timeline` vs `timeline`), either unstage those files or fix
  them: dedup-normalize the `tags:` block in Python, canonical mapping from
  SCHEMA.md, then re-add.
- **Content regression guard**: blocks any staged change shrinking an existing
  page >50% or >50 lines. Usually a legit cron merge-to-redirect (e.g.
  `eugeneyan.md` → `eugene-yan.md`) that just isn't yours to commit. Unstage it
  and leave it in the working tree for the cron that owns it — but REPORT it to
  the user, since they may not realize an ingestion pipeline staged page
  overwrites.
- **Index validation** (`scripts/validate_index.py`): runs when index.md is
  staged; check corruption patterns before committing.

## Rule 3: Recovering your own work if it got swept into a stash

Cron pipelines sometimes `git stash push -u` to clean the tree. If your new
files suddenly vanish (`ls` fails, files gone), the stash may hold them:

1. `git stash show --name-only stash@{0}` — confirm your files appear (both
   tracked mods and new untracked files land there after `-u`).
2. `git stash pop` — restores everything, including the cron junk.
3. `git reset -q` + explicit `git add <your files>` — separate yours.
4. Commit; leave the cron's files unstaged in the working tree.

If you stashed yourself to escape a blocked commit, `git stash pop` later and
follow the separation recipe above — do NOT leave the stash sitting (see
wiki-ingestion-pipelines/references/stale-stash-supersession.md).

## Rule 4: Index bookkeeping on new pages

- Add one entry in the alphabetically-plausible cluster near the page's first
  letter — do NOT guess a different section by prefix (`comprehension-interface`
  belongs under `c`, not near `ai-output-format-progression`).
- Bump `> Total pages:` in the header AND the `## Concepts (N pages)` /
  `## Entities (N pages)` section counts.
- Append a dated log.md entry (ingest template).
