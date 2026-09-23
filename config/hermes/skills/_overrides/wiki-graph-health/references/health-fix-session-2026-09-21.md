# Watchdog / health-fix session — 2026-09-21

Run: `wiki-health-fix` cron, digest from `wiki_health.py --json` (timed out at 60s in a fresh foreground invocation; the JSON was already provided as cron script output — use the injected digest instead of re-running the slow script).

## Results
- Index corruption: all 0 (pipe / line-number / triple-bracket / space-prefix). `validate_index.py` exit 0 (3107 lines).
- Ghost entries: 0 (all index wikilinks verified against filesystem with recursive scan + `_index`→dir resolution).
- Orphan registration: digest reported 23 orphans, ALL were `_index.md` files:
  - 13 registered into index.md Concepts (ai-organization, claude-code, codex, coding-agents, evaluation, harness-engineering, harness-engineering/agentic-workflows, harness-engineering/system-architecture, inference, local-llm, multi-agents, openclaw, post-training).
  - 2 archived (`concepts/gpt/_archive/*`) — intentionally unindexed, skip.
  - 2 top-level (`concepts/_index`, `entities/_index`) — content IS the index, by-design exclusion.
  - Remaining hubs were already indexed as directory wikilinks (false positives, see below).
- Index header recount: Concepts 2067→2080, Entities 930→931, Total 3071→3086 (recomputed from section counts; header decay confirmed again — Total was 15 low). After fix, section counts sum equals header Total.
- Commit `7be01ff2` "wiki: auto-fix health issues (register 13 _index hubs, fix index counts)", pushed cleanly (`git reset -q` then add only index.md + log.md; no sibling-WIP stash needed).

## Key bug: `_index.md` directory-slug link resolution
index.md references hub pages as `[[concepts/inference]]` (directory form); the on-disk file is `concepts/inference/_index.md`. A naive filesystem-vs-index orphan scan flags every hub `_index.md` as "not indexed".

Fix for any orphan/ghost scanner — when building the existing-slugs set:

```python
rel = relpath_without_.md   # e.g. "concepts/inference/_index"
existing.add(rel)
if rel.endswith('/_index'):
    existing.add(rel.rsplit('/', 1)[0])   # also treat the DIRECTORY as indexed
```

Same trick already noted in the broken-link scanner pitfalls (`_index` dirs are valid wikilink targets). Expected healthy residual after this mapping: only archive files and top-level `concepts/_index` / `entities/_index`.

## Recipe: batch-registering hub `_index` pages into index.md
1. Dedup check first: check whether the wikilink pattern is already present in index.md — catches already-indexed hubs (8 of 21 were).
2. Insert the batch in one Python pass (read, insert alphabetically bottom-up, write) — safer than N patches.
3. Recompute section header counts AND the `Total pages:` line from actual counts.
4. Verify: `validate_index.py` + corruption regexes (pipe/lineno/triple/space) all 0.
5. log.md prepend via Python heredoc (open file, write entry + content) — avoid backticks in the entry so a plain terminal heredoc works.

## Notes
- `wiki_health.py --json` can exceed 60s when invoked fresh; if the digest is already injected by the cron pre-run script, do not re-run it.
- Report-only classes unchanged: stale 2818 (oldest 165d), unprocessed raw 5959 (raw-backlog-ingest cron still stopped).
