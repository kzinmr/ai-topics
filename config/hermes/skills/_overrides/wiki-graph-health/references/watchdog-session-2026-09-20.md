# Watchdog / health-fix session — 2026-09-20

## Outcome (baseline reference)
- Index corruption (pipe / line-number / triple-bracket / space-prefix): all 0, verified live with grep + Python count.
- Ghost entries (recursive scan): 0.
- Reported 26 orphan pages -> only 3 real gaps, all registered in index.md (commit `e41bbdf1`, pushed):
  - `entities/mario-zechner-badlogicgames`, `entities/sgnt-jev-article`, `entities/speakeasy-openapi-generation`
- Index counts bumped: Entities 927->930, Total pages 3068->3071. `validate_index.py` passed, pre-commit tag hook passed.

## Key lessons

### 1. Do NOT re-run `wiki_health.py --json` inside the agent run to verify/time it
The 0.28s optimization applies only to `load_l2_pages()`; the full run (unprocessed-raw scan across ~9,777 raw articles + orphan scan) exceeded 60s and timed out. Treat the pre-run script digest as the authoritative snapshot; verify claims with cheap targeted checks:
- Corruption: `grep -cP '^\s*\d+\|' wiki/index.md`, `grep -c '^|- \[\[' wiki/index.md`, Python `[[` sanity count, `grep -c '^ - \[\[' wiki/index.md`
- Ghosts: Python recursive wikilink-vs-filesystem scan (os.walk, `_index.md` handling)
- Orphans: per-candidate `[ -f wiki/<slug>.md ]` + in-index grep, not a full rescan

### 2. Orphan list triage — 26 reported -> 3 real
Composition of the daily orphan list (stable pattern):
- ~21 `_index.md` files (subdir hubs like `concepts/post-training/_index`, `entities/_index`, `concepts/_index`) — by design not in main index.md. SKIP.
- `_archive/` entries (`concepts/gpt/_archive/...`) — archived content, not indexed by design. SKIP.
- Pages already in index under the exact slug — check with an in-index substring probe before adding (e.g. `concepts/system-one-models`, `entities/typesafe-ai` were already indexed; the report flagged them falsely).
- Real gaps: top-level entity pages with a file on disk and 0 index hits -> register alphabetically.

### 3. Tag-only frontmatter fix before registering orphans
`entities/speakeasy-openapi-generation` had a non-SCHEMA tag (`philipp-schmid` — a person name used as tag). Remove person-name tags from `tags:` (person names belong in `related:`/wikilinks) before adding to index, or the pre-commit tag validator blocks the commit.

### 4. Stale sibling WIP in the working tree
Working tree had unrelated modified/untracked files from other pipelines (skills edits, raw articles, entity pages). Committed only `wiki/index.md` + `wiki/log.md` by explicit path — no stash needed because the pre-commit hook only validates staged files.

### 5. SKILL.md size gate
`wiki-graph-health/SKILL.md` is at the 100,000-char limit (100,445 when patching on 2026-09-20) — further SKILL.md patches will fail until it is trimmed/split. Put new lessons in `references/` files instead.

### 6. `/usr/bin/time` not installed on this host; use shell `time` builtin or omit.
