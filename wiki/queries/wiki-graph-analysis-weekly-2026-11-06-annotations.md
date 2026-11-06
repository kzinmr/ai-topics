---
title: Weekly Wiki Graph Analysis — Adjudicated Annotations 2026-11-06
created: 2026-11-06
updated: 2026-11-06
type: query
tags: [wiki]
sources:
  - queries/wiki-graph-analysis-weekly-2026-11-06.md
  - /tmp/deep_audit_2026-11-06.txt (deep_link_audit.py run 2026-11-06)
---

# Weekly Graph Analysis — Adjudicated Annotations (2026-11-06)

Companion to `queries/wiki-graph-analysis-weekly-2026-11-06.md`. Ground truth via
`deep_link_audit.py` (recursive resolver) + manual page reads, per
`wiki-graph-health/references/weekly-graph-analysis.md`.

## Trend vs 2026-10-30

| Metric (raw report) | 2026-10-30 | 2026-11-06 | Δ |
|---|---|---|---|
| Pages | 3,351 | 3,404 | +53 |
| Orphans | 477 | 484 | +7 |
| Broken links | 3,378 | 3,447 | +69 |
| Dup groups | 18 | 17 | −1 |
| Oversized | 325 | 326 | +1 |
| Stale >90d | 2,420 | 2,491 | +71 |
| Tag violations (raw) | — | 1 | tag_audit.py: **0** (false positive) |

Deep-audit ground truth: **2,598 true broken links** (raw 3,447 inflated by bare/nested
links), **457 true orphans ≥20 lines** (raw 484).

## 1. Duplicate group verdicts (all 17 measured THIS session)

| Group | Verdict | Evidence |
|---|---|---|
| entities/_index vs concepts/_index | FALSE POSITIVE | meta pages, different namespaces |
| entities/deliberate-coder vs entities/deliberatecoder | FALSE POSITIVE | different people (Ben Ilegbodu vs Steve Shogren) — standing ground truth §11 |
| eugeneyan, gilesthomas, lilianweng, martinfowler, samuelcolvin, nvidia-openshell, alphaproof-nexus, deer-flow, dspy-rlm, llm-integration-patterns, open-claw-ecosystem | ALREADY HANDLED | thinner side has `redirect:` / `status: redirect` frontmatter (11 groups) |
| entities/cline vs concepts/cline | LEGIT split | both substantial (129/98 lines), cross-link each other, 5+4 inbound |
| entities/qwen vs concepts/qwen | LEGIT split, 1 gap | entity→concept links exist (6); **concepts/qwen has 0 links back to entities/qwen** — add cross-ref |
| entities/omnara vs concepts/omnara | LEGIT split | entities/omnara → concepts/omnara; but entities/omnara has only 1 inbound (orphan-adjacent) |
| concepts/agent-harnesses vs comparisons/agent-harnesses | LEGIT split, 1 gap | concepts (157L, 44 inbound) vs comparison (412L, 3 inbound); **concepts/agent-harnesses does NOT link comparisons/agent-harnesses** — add cross-ref |

**No merges needed. Zero destructive actions this week.** Two one-line cross-ref fixes:
`concepts/qwen` → add `[[entities/qwen]]`; `concepts/agent-harnesses` → add `[[comparisons/agent-harnesses]]`.

## 2. Index gaps (independent resolver)

- "27 stale index entries" → all but the deleted 10-30 report/annotations pair are dir-hub
  false positives (`[[concepts/foo/index]]` ↔ key `concepts/foo`). Fix = replace dangling
  10-30 entries with today's report + annotations (done in this commit).
- "25 not indexed" → mostly `_index`/dir-hub resolver mismatches + sibling-pipeline WIP
  (19 dirty wiki files from blog-ingest today: raw articles etc.). Defer sibling WIP to its pipeline.

## 3. Orphans (deep audit: 457 true ≥20-line)

Top content-rich orphans (indexed but no inbound wikilinks — link candidates, not deletions):
`queries/2026-10-04-uncommitted-wip-snapshot-query` (3,680L — consider archiving or linking from a hub),
`concepts/multi-objective-policy-distillation` (279L), `entities/openenv` (234L),
`concepts/claude/system-card-milestones` (231L), `entities/ibrahim-diallo` (227L),
`concepts/symphony` (208L), `concepts/ai-benchmarks/skillspector` (188L),
`comparisons/codex-app-server-vs-claude-agent-sdk` (185L), `comparisons/openclaw-pi-hermes-state-management` (183L).
By category: concepts 297, entities 131, queries 14, events 10, comparisons 5.

## 4. Missing-page creation queue (after nested resolution)

Resolved nested (link-fix, not creation): `agent-evaluation` → `concepts/evaluation/agent-evaluation-methodology`,
`bitter-lesson` → `concepts/rich-suttons-bitter-lesson`, `inference-optimization` → `concepts/llm-inference-optimization-performance`,
`agent-architecture` → `concepts/ai-agent-architecture`, `ai-coding` → `concepts/ai-coding-effectiveness-debate`,
`huggingface`-related → existing `concepts/huggingface-skills` / `entities/huggingface` (check exact target).

Genuine creation queue (≥8 inbound refs, nothing on disk):
1. `entities/cursor` (14 refs) — closest is `concepts/coding-agents/cursor-ide`; decide hub vs redirect
2. `concepts/claude-opus-4-7` (10 refs)
3. `entities/ben-clavie` (9 refs)
4. `concepts/enterprise-ai` (13 refs) — hub page candidate (children exist: scaling-patterns, deployment-jv)
5. `concepts/ai-governance` (13+9 bare refs) — hub candidate under security-and-governance
6. `concepts/ai-adoption` (11 refs)
7. `concepts/agent-harness-comparison` (8 refs) — likely should redirect to `comparisons/agent-harnesses`

Mechanical: 10× `[[concepts/ai-benchmarks/swe-bench\]]` stray-backslash malformed links.

## 5. Other

- Stale 2,491 dominated by bulk-import `updated` dates — not content degradation (standing interpretation).
- Tag violations: raw report says 1; `tag_audit.py` finds **0** non-taxonomy tags → false positive, no action.
- Generator bug backlog (unchanged): index `_index` resolution, dup detector should skip redirect stubs
  (would remove 11 of 17 "groups"), report rotation leaves dangling index entries.
