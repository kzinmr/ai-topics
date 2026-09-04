# Parallel Subagent Index/Log Trap (Jul 2026)

## The Problem

When spawning 3+ parallel subagents for wiki-enrichment takes, each subagent independently writes to `wiki/index.md` and `wiki/log.md`. This causes:

1. **Log.md overwrite**: Each subagent uses prepend (cat new + old → mv), but only the *last* subagent's prepend survives. Earlier subagents' log entries are silently dropped because the later subagent read the intermediate (already-appended) file, appended its own entry, and wrote — but the earlier entry was already in its input, so the ordering is wrong or entries are lost entirely.

2. **Index.md corruption**: Multiple subagents increment section counts independently (e.g., both AX concept and Grok-4-5 subagents increment `Events` or `Concepts` from different baselines), producing wrong totals.

3. **False success reports**: Subagents report "log.md updated" via their summary, but verification shows the entry never made it to disk. This happened in Jul 2026: the modal-labs subagent claimed log.md update, but the entry was absent.

## Symptoms

- `grep "2026-XX-XX" log.md` shows only N-1 of N expected entries
- Index.md section counts are off (e.g., Concepts count is actual+1 or actual-1)
- Log.md entries are in wrong order (newest entry buried mid-file instead of first)

## Root Cause

Parallel subagents with shared mutable state (log.md, index.md) cannot independently update those files without coordination. Each subagent does:
```python
# Read current log.md → prepend new entry → write
# If two subagents do this simultaneously, one overwrites the other's changes
```

## The Fix: Centralized Index/Log Management

**Subagents should NOT update index.md or log.md.** Subagents only:
- Create new pages (write_file)
- Enrich existing pages (patch)
- Report back what they did via their summary

The **parent agent** collects all results after subagents finish and performs ONE centralized update to index.md and log.md.

### Implementation Pattern

```python
# After all parallel subagents complete:
# 1. Collect all changes from subagent summaries
# 2. Read index.md ONCE, apply all additions, increment counts correctly
# 3. Build ONE log entry covering all changes
# 4. Prepend log entry once (not N times)
# 5. Verify by re-reading both files
```

### Subagent Context Instructions

Add this to every parallel subagent's context:

```
IMPORTANT: Do NOT update wiki/index.md or wiki/log.md. Only create/enrich 
the page file itself. The parent agent will handle index and log updates 
centrally after all subagents complete.
```

### Verification After Parallel Block

After all subagents finish and centralized index/log update:

```bash
# Count entries by date
grep "2026-07-09" wiki/log.md | wc -l
# Should match number of subagents + any other same-day entries

# Check index section counts
grep -c "^\- \[\[concepts" wiki/index.md  # Concepts count
grep -c "^\- \[\[events" wiki/index.md    # Events count

# Spot-check first log entry date
head -3 wiki/log.md
```

## Validated

- Jul 2026: Newsletter-wiki-ingest with 3 parallel subagents. 2 of 3 subagents' log entries survived (the grok-4-5 and agent-experience entries). The modal-labs entry was missing despite subagent reporting success. Index counts were correct by coincidence (subagents modified different sections).

- Aug 2026: X bookmarks ingest with 3 parallel subagents creating 3 new pages (1 concept + 2 entities). Reconciliation bugs encountered:
  - Subagent A (varick-agents) updated `entities/_index.md` but forgot `wiki/index.md`
  - Subagent B (vasuman) updated `wiki/index.md` but didn't create a `log.md` entry
  - Subagent C (ai-adoption-barbell) added to both `index.md` and `log.md` but referenced sibling entities as "not yet created" / "created by sibling subagent"
  - Log.md header was displaced during the follow-up vasuman log prepend (fixed with Python reorder script)

## Reconciliation Checklist (When Subagents Modified Shared Files)

When subagents DID independently modify `index.md` and `log.md` despite the recommendation:

### 1. Missing `index.md` entries
```bash
# For each new page created, verify it appears in index.md
grep "varick-agents\|vasuman\|ai-adoption-barbell" wiki/index.md
```
If a subagent forgot to add its entry to `wiki/index.md` (but added to `_index.md`), add it manually with `patch` at the alphabetically correct position.

### 2. Stale cross-references in `log.md`
Subagents may reference sibling creations as "not yet created" or "created by sibling subagent" because they run in parallel and don't see each other's output. After all subagents complete:
```bash
grep -n "not yet created\|created by sibling" wiki/log.md
```
Replace stale references with actual status ("created").

### 3. Missing `log.md` entries
```bash
# After all subagents, each created page should have a log entry
grep -c "entities/varick-agents\|entities/vasuman\|concepts/ai-adoption-barbell" wiki/log.md
```
If a subagent didn't create a log entry (common — some only update index), prepend one manually using the Python prepend pattern (see `references/log-prepend-header-repair.md`).

### 4. Log.md header displacement
The follow-up log prepend may push the "# Wiki Log" header down. Verify:
```bash
head -1 wiki/log.md | grep -c "^# Wiki Log"
```
If displaced, use the strip-all-variants rebuild pattern from `references/log-prepend-header-repair.md`.

### 5. Index section header counts
```bash
# After all entries are in place, verify section counts match
grep "^## Concepts (" wiki/index.md     # Should reflect actual concept count
grep "^## Entities (" wiki/index.md     # Should reflect actual entity count
```
Increment each section header count by the number of new pages in that section. The Concepts count was bumped by subagent C (1956→1957) but the Entities count (884) needed manual update to 886.
