---
title: Weekly Wiki Graph Analysis 2026-09-18
created: 2026-09-18
updated: 2026-09-18
type: query
tags: [knowledge-management, wiki]
sources: []
---

# Weekly Wiki Graph Analysis — 2026-09-18

Full-corpus graph scan (recursive, 3,079 pages), verified with `scripts/wiki_graph_analysis_verified.py`. The stock `wiki_graph_analysis_weekly.py` under-scans (2,486 pages — flat directories only) and its broken-link stats are inflated by double-wrapping targets in its output; numbers below are from the corrected recursive walk.

## Summary

| Metric | Count | Notes |
|---|---|---|
| Total pages | 3,079 | entities 926, concepts 2,080 (587 in subdirs), comparisons 35, events 33, queries 6 |
| Orphans (no inbound links) | 446 | content-rich (≥50 lines): 303 |
| Broken wikilinks | 2,810 refs / 1,758 targets | classified below |
| Real duplicate groups | 8 | 16 flagged → 8 already redirects / by-design pairs |
| Index gaps | 0 ghosts / 22 unindexed | all 22 are `_index` hub pages (by-design) |
| Stale pages (>90d) | 1,661 | bulk: April-10 entity batch |
| Tag violations | 0 | clean |
| Oversized (>200 lines) | 243 | candidates for splitting |

## 1. Broken links (2,810 refs) — dominant structural debt

| Category | Refs | Meaning / fix |
|---|---|---|
| namespaced-missing | 1,280 | `[[concepts/foo]]` with no `foo.md` anywhere — wrong-namespace guesses (e.g. `[[entities/drata]]`, `[[concepts/autonomous-agents]]`) |
| raw-ref-as-wikilink | 919 | `[[raw/...]]`/`[[transcripts/...]]` — valid provenance pointers, not navigable pages; consider converting to inline links |
| bare-missing | 432 | bare links to non-existent pages (`[[windsurf]]`, `[[julia-evans]]`) |
| deep-path-drift | 121 | moved/renamed targets, some with trailing `\` artifacts |
| dir-hub-missing-index | 58 | links to category dirs lacking `_index.md` (e.g. `concepts/context-engineering` — top offender: ~130 refs) |

Top single fix: create `concepts/context-engineering/_index.md` plus ~15 other hub `_index.md` pages — kills the largest broken-link cluster.

## 2. Orphans (446; 303 content-rich)

Worst content-rich orphans (rich outbound links, zero inbound): `concepts/ai-energy` (284L), `concepts/multi-objective-policy-distillation` (279L), `entities/openenv` (234L), `concepts/claude/system-card-milestones` (231L), `entities/ibrahim-diallo` (227L), `concepts/symphony` (208L). Fix by adding inbound links from sibling pages in the same subdirectory categories (subdir pages rarely get linked from flat pages).

## 3. Duplicates (8 real groups to consolidate)

1. `entities/eugeneyan` (220L) vs `entities/eugene-yan` (352L) — merge → eugene-yan
2. `entities/lilianweng` (156L) vs `entities/lilian-weng` (202L) — merge → lilian-weng
3. `entities/gilesthomas` (228L) vs `entities/giles-thomas` (92L) — merge → giles-thomas (keep richer)
4. `entities/deliberate-coder` vs `entities/deliberatecoder` (both ~130-139L, same person) — merge
5. `concepts/deerflow` (51L) vs `concepts/deer-flow` (92L) — merge → deer-flow
6. `concepts/alphaproof-nexus` (52L) vs `concepts/alpha-proof-nexus` (142L) — merge (stub → redirect)
7. `concepts/dspyrlm` (25L stub) vs `concepts/dspy-rlm` (697L) — stub → redirect
8. `concepts/open-claw-ecosystem` (25L) vs `concepts/openclaw-ecosystem` (138L) — stub → redirect

Already resolved (no action): samuelcolvin, martin-fowler (redirects). By-design splits: cline, qwen (entity+concept), agent-harnesses / evals-skills / llm-integration-patterns (concept + comparison; consider cross-linking).

## 4. Stale (1,661) & oversized (243)

Staleness is dominated by the 2026-04-10 blog-entity batch — mostly long-tail blogger pages where infrequent updates are expected; recommend a policy note rather than batch touching. Oversized top: agentic-search (1,191L), simon-willison (974L), harvey (960L).

## Recommended actions (priority)

- [HIGH] Consolidate the 8 duplicate groups above (merge rich → thin becomes redirect, alias preserved)
- [HIGH] Create missing `_index.md` hubs (~15 dirs; context-engineering first — ~130 refs)
- [MEDIUM] Convert `[[raw/...]]`/`[[transcripts/...]]` wikilinks (919 refs) to inline markdown links, or register them as lint-exempt
- [MEDIUM] Fix 1,280 wrong-namespace links via batch resolver (basename-match where unique)
- [MEDIUM] Add inbound links to top 20 content-rich orphans from sibling subdir pages
- [LOW] Split 5 largest oversized pages (>600 lines)
- [LOW] Script fix: `wiki_graph_analysis_weekly.py` should use `os.walk` (recursive) — verified version saved as `scripts/wiki_graph_analysis_verified.py`
