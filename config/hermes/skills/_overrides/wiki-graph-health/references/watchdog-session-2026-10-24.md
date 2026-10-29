# Watchdog session 2026-10-24 — clean-corruption run, two real gaps fixed

Digest: 955 entities / 2231 concepts / 35 comparisons, 10,750 raw, 6,742 unprocessed, 2,931 stale, 0 skeleton, orphans "all indexed ✅".

## Verified clean (no action)
- index.md: pipe_prefix=0, line_number=0, triple_bracket=0, space_prefix=0, `||- `=0 (Python regex counts — the authoritative method per skill).
- Ghost entries: 0 (recursive check incl. `<dir>/_index.md` dir-slug form).
- Top-level not-indexed pages: 0 (filter `'/' not in relpath`, skip `_`-prefixed — nested pages served by hubs are by design).
- L2 pipe bullets (`|- [` in entities/ + concepts/ only): 0. Quadruple brackets: 0.
- `validate_index.py` exit 0.

## Real fixes applied
1. **Frontmatter missing on hot-post query page**: `queries/2026-10-24-morning-hotpost-oracle-routing.md` created by the morning hot-post pipeline with NO YAML frontmatter (started with `# 🔥 ...`). The daily digest does NOT flag this class — only the recursive no-frontmatter scan (Section 5 Sub-pattern A) catches it. Fixed by prepending:
   ```yaml
   ---
   title: "Morning Hot-Post 2026-10-24 — Oracle Routing の経済学"
   created: 2026-10-24
   updated: 2026-10-24
   type: query
   tags: [query, model-routing, oracle-routing, ai-economics, agent-economics]
   sources: []
   status: active
   ---
   ```
   All tags SCHEMA-valid → pre-commit tag validator passed, no `--no-verify` needed.
   - Date sourcing: `git log --diff-filter=A --follow --format='%ai %h' -- <path>` worked fine for the date-prefixed query filename.
   - Recipe tags for hot-post pages: `query` + topical SCHEMA tags (`model-routing`, `oracle-routing`, `ai-economics`, `agent-economics` are all in SCHEMA.md Meta/Models lines as of 2026-10-24).
2. **Index header count recount**: headers had drifted from actual list-line counts (Entities 955→959, Concepts 2228→2227, Events 45→44, Queries 37→39, Total 3277→3304). Recompute via per-section count of `- [[<dir>/` lines and rewrite with `str.replace()` — then `validate_index.py` must still pass. Digest concept count (2231) > index top-level count (2227) is NORMAL: nested hub-subpages are intentionally not top-level entries.

Commit `544d9242` pushed; hooks (validate_index + tag validator) passed normally.

## Cost profile
~11 tool calls, one `patch`, one Python recount script, one commit. Cheap run — when corruption classes are 0, the highest-value checks are the no-frontmatter scan and header recount, since the digest under-reports both.

## Note on SKILL.md size
SKILL.md hit the 100,000-char limit this session (100,817) — patches to it will fail until it is trimmed. Put new session learnings in references/ files; if SKILL.md needs a pointer, replace an older pointer line rather than adding.
