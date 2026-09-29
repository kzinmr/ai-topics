# Watchdog / wiki-health-fix session — 2026-09-28

## Context
Daily `wiki-health-fix` cron. Digest: entities 932, concepts 2098, comparisons 35, raw 9973, stale 2885, unprocessed raw 6118, orphans 3.

## Verified clean (no action)
- index corruption 4 patterns (pipe prefix, line-number, triple-bracket, space-prefix): live grep all 0.
- Ghost entries: 0.

## Orphan triage (3 reported)
1. `concepts/authors-guild-v-openai` — REAL orphan. File existed but was **uncommitted in the working tree** (`git status` showed `?? wiki/concepts/authors-guild-v-openai.md` plus several raw articles). Upstream ingest wrote the page but never committed it.
   - Action: added to index.md alphabetically, registered page + raw source in the same commit, recomputed Total pages / Last updated.
   - **Tag violation caught by pre-commit**: page used `training-data`, which is NOT in the SCHEMA taxonomy (despite SCHEMA listing 957 tags). Fixed to `datasets`.
2. `concepts/gpt/_archive/2026-04-24-ainews`, `-news-aggregation` — false positives; `_archive/` is intentionally not indexed. Skip.

## Index header facts
- Mid-session a sibling bumped `## Concepts (2095 pages)` → `(2103 pages)` while adding files. Recompute header counts from actual `- [[concepts/` line counts right before the final write; don't trust the digest or your earlier count.
- `validate_index.py` exit 0 before and after commit.

## Lessons
- **Digest orphan + `git status ??` for the same file ⇒ commit it, don't just index it.** An unindexed page that is also untracked means the ingest pipeline forgot its commit step. Adding it to index.md without committing reproduces the same orphan in tomorrow's digest. Batch the page + its raw sources + index/log edits into one scoped `git add`.
- **`training-data` is a recurring pipeline-invented tag** — map to `datasets`, never add to SCHEMA.
- Pre-dry-run `.githooks/pre-commit` after `git add`, before the real commit — it caught the tag violation on the new page pre-flight, avoiding the stash dance.
