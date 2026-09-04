# Dominant-Publication Batch Yield Pattern

## When One Publication Dominates the Batch

When a single publication (measured by `publication_id` in the inbox summary) accounts for ≥50% of newsletters in a single triage batch, the standard yield estimates from `semantic-article-grouping` SKILL.md are too optimistic.

## Concrete Pattern (Validated July 2026)

**Scenario**: 8 newsletters in one batch, of which 4 are from swyx's pub_id=1084089 (AINews daily bulletin, Latent Space podcast Q&A, AIEWF FDE article, AIEWF Daily Dispatch).

**Actual yield**: 4 takes, 3 references, 2 skips — well below the 5-9 takes / 5-8 references / 5-10 skips estimate for 8-9 newsletter batches.

**Why the yield drops**:
- The daily bulletin (AINews) covers the widest range but at shallow depth — most topics are skim-level and many duplicate content from other newsletters in the same batch.
- Podcast/standalone articles (Latent Space, AIEWF articles) cover deep single-topic content — these are the primary takes.
- Conference dispatches (AIEWF Daily Dispatch) overlap with the bulletin's topics but frame them differently — may produce one additional take.
- Multiple newsletters from the same newsroom mean fewer truly independent editorial perspectives → fewer unique gap-finding opportunities.

## What to Expect

| Batch composition | Typical yield |
|---|---|
| 8 newsletters, 0-1 dominant pub | 5-9 takes, 5-8 refs, 5-10 skips |
| 8 newsletters, 1 dominant pub (50%+) | 4-6 takes, 2-4 refs, 2-4 skips |

## Terminal Pitfall: `&` in `find -name` Commands

When checking existing wiki pages with multiple patterns, avoid shell `&` (background operator) in `find` invocations:

```bash
# WRONG — triggers Hermes background detection and blocks the command
find ~/wiki/concepts -name "*sonnet*" -o -name "*claude*" &
find ~/wiki/concepts -name "*fable*" &

# CORRECT — one command, no &
find ~/wiki/concepts \( -name "*sonnet*" -o -name "*claude*" -o -name "*fable*" \) 2>/dev/null | head -20
```

The `&` at end of line is interpreted by the Hermes terminal security layer as a request to background the process, which is blocked for non-daemon commands. Use explicit `\( ... \)` grouping in `find` instead of multiple `&`-joined commands.
