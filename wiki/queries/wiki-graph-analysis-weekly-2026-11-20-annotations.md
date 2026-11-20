---
title: Weekly Wiki Graph Analysis — Adjudicated Annotations 2026-11-20
created: 2026-11-20
updated: 2026-11-20
type: query
tags: [wiki]
sources: []
---

# Weekly Graph Analysis — Adjudicated Annotations (2026-11-20)

Companion to `[[queries/wiki-graph-analysis-weekly-2026-11-20]]`. The raw report is noisy;
these are the adjudicated verdicts after reading every page in doubt.

## Week-over-week trend

| Metric | 2026-11-13 | 2026-11-20 | Δ |
|---|---|---|---|
| Pages (scanner) | 3,456 | 3,495 | +39 |
| L2 pages (deep audit) | ~3,456 | 3,501 | +45 |
| True orphans (deep audit, ≥20L) | 460 | 462 | +2 |
| True broken links (deep audit) | 2,581 | 2,627 | +46 |
| Duplicate groups (report) | 17 | 17 | 0 |
| Real merge actions needed | 0 | 0 | 0 |
| Index gap (real) | 1 | 1 | 0 |
| Oversized (>200L) | 330 | 335 | +5 |
| Stale (>90d) | 2,558 | 2,563 | +5 |
| Tag violations (real) | 0 | 0 | 0 |

## 1. Duplicate groups — verdict table (17/17 adjudicated)

| Group | Verdict | Evidence |
|---|---|---|
| entities/_index vs concepts/_index | FALSE POSITIVE | Different namespaces, intentional hub pair |
| entities/cline vs concepts/cline | KEEP (intentional split) | entity = product page (129L), concept = "Autonomous Coding Agent Paradigm" essay (98L). Cross-link both. |
| entities/deliberate-coder vs entities/deliberatecoder | FALSE POSITIVE | Different people — Ben Ilegbodu (Deliberate Coder) vs Steve Shogren (Deliberate Software). Confirmed via titles. |
| entities/eugene-yan vs entities/eugeneyan | ALREADY HANDLED | `eugeneyan` (11L) has `status: redirect` → `eugene-yan` (352L) |
| entities/giles-thomas vs entities/gilesthomas | ALREADY HANDLED | `giles-thomas` (11L) has `status: redirect` → `gilesthomas` (228L) |
| entities/lilian-weng vs entities/lilianweng | ALREADY HANDLED | `lilianweng` (11L) has `status: redirect` → `lilian-weng` (202L) |
| entities/martin-fowler vs entities/martinfowler | ALREADY HANDLED | `martin-fowler` (17L) has `redirect:` frontmatter → `martinfowler` (171L) |
| entities/nvidia-openshell vs concepts/nvidia-openshell | KEEP (intentional split) | entity = NVIDIA product (128L, complete), concept (43L) has `redirect:` frontmatter pointing back. Already correct. |
| entities/omnara vs concepts/omnara | KEEP (intentional split) | entity = company/product (51L), concept = "Open-Source Managed Agent Platform" essay (114L). Cross-link both. |
| entities/qwen vs concepts/qwen | KEEP (intentional split) | entity = product/company (162L), concept = "Qwen Model Family" (89L) |
| entities/samuel-colvin vs entities/samuelcolvin | ALREADY HANDLED | `samuelcolvin` (14L) has `redirect:` → `samuel-colvin` (233L) |
| concepts/agent-harnesses vs comparisons/agent-harnesses | KEEP (intentional split) | concept = overview (158L), comparison = 9-way table (412L). Cross-link both. |
| concepts/alpha-proof-nexus vs concepts/alphaproof-nexus | ALREADY HANDLED | `alphaproof-nexus` (39L) has `redirect:` → `alpha-proof-nexus` (142L) |
| concepts/deer-flow vs concepts/deerflow | ALREADY HANDLED | `deerflow` (45L) has `redirect:` → `deer-flow` (92L) |
| concepts/dspy-rlm vs concepts/dspyrlm | ALREADY HANDLED | `dspyrlm` (18L) has `status: redirect` → `dspy-rlm` (697L, complete) |
| concepts/llm-integration-patterns vs comparisons/llm-integration-patterns | ALREADY HANDLED | concept side (18L) has `status: redirect` → comparison side (275L) |
| concepts/open-claw-ecosystem vs concepts/openclaw-ecosystem | ALREADY HANDLED | `open-claw-ecosystem` (18L) has `status: redirect` → `openclaw-ecosystem` (138L, complete) |

**Action**: 0 merges needed. 4 pairs (cline, omnara, qwen, agent-harnesses) are intentional namespace splits; verify they cross-link each other as a low-priority cleanup.

## 2. Index gap — ground truth

Independent resolver (recursive walk, `dir/index.md` + `dir/_index.md` resolution):
- Report says: 29 "stale index entries" + 18 "not indexed".
- Reality: **1 real gap**. The 29 are the 2 prior-week reports (auto-deleted by the generator) plus 27 dir-hub false positives. The 18 "not indexed" are 13 dir-hub slugs, 3 log-2026* archives, the prior-week's skeleton-enrich query (tracked but unindexed — last week's leftover), and today's report.
- The one genuine tracked gap: `queries/2026-11-13-skeleton-enrich-stub-action` — index it now (low priority).

Action: replace the 2 dangling `[[queries/wiki-graph-analysis-weekly-2026-11-13*]]` index lines with today's report + annotations entries.

## 3. Broken-link triage (top targets)

The deep audit reports 2,627 broken links. Resolving top targets by basename-match against nested pages:

| Target | Refs | Verdict |
|---|---|---|
| agent-evaluation | 24 | RESOLVES → `concepts/evaluation/agent-evaluation-methodology` |
| entities/cursor | 14 | RESOLVES → `concepts/coding-agents/cursor-ide` (or create entity) |
| concepts/enterprise-ai | 13 | RESOLVES → `concepts/enterprise-ai-scaling-patterns` (or hub) |
| concepts/ai-governance | 13 | RESOLVES → `concepts/security-and-governance/agentic-ai-governance` |
| concepts/ai-adoption | 11 | RESOLVES → `concepts/ai-adoption-barbell` |
| concepts/agent-architecture | 10 | RESOLVES → `concepts/ai-agent-architecture` |
| concepts/inference-optimization | 10 | RESOLVES → `concepts/llm-inference-optimization-performance` |
| concepts/bitter-lesson | 10 | RESOLVES → `concepts/rich-suttons-bitter-lesson` |
| entities/huggingface | 10 | GENUINE GAP → create `entities/huggingface` stub |
| concepts/claude-opus-4-7 | 10 | GENUINE GAP → create or alias to `entities/claude` |
| concepts/agent-framework | 9 | RESOLVES → `entities/microsoft-agent-framework` (context-check) |
| concepts/ai-coding | 9 | RESOLVES → `concepts/ai-coding-effectiveness-debate` (or hub) |
| entities/ben-clavie | 9 | GENUINE GAP → create `entities/ben-clavie` stub |
| concepts/agent-harness-comparison | 8 | GENUINE GAP → alias to `comparisons/agent-harnesses` |
| (empty `[[]]`) | 53 | Report artifact only — 0 real empty links outside the report itself |

**Genuine creation queue (≥8 refs, not nested-resolvable)**: `entities/huggingface`, `entities/ben-clavie`, `concepts/claude-opus-4-7`, alias `concepts/agent-harness-comparison` → `comparisons/agent-harnesses`.

## 4. Tag violations — report false positive

Report claims 1 tag-violating page. `tag_audit.py` reports **0 not in taxonomy** (1,144 canonical tags cover all 1,038 in-use). The "1" is a generator artifact (likely the report page itself). No action; the `tag-audit-weekly` job covers taxonomy drift.

## 5. Orphans — top linking candidates

Deep audit: 462 true orphans (292 concepts, 128 entities, 24 queries, 13 events, 5 comparisons). Most are recent pipeline output reachable via `index.md` only — not a real discoverability crisis. Prioritize for manual inbound linking:
1. `concepts/multi-objective-policy-distillation` (279L) — link from `concepts/post-training/` siblings + `concepts/knowledge-distillation`
2. `entities/ibrahim-diallo` (237L) — link from related people + projects
3. `entities/openenv` (234L) — link from RL/agent-environment concepts
4. `concepts/claude/system-card-milestones` (231L) — link from `concepts/claude/_index` + safety concepts
5. `concepts/symphony` (208L), `concepts/ai-benchmarks/skillspector` (188L), `concepts/hegel-property-based-testing` (187L), `concepts/spine-swarm-agents` (187L)
6. The two `comparisons/*` entries (codex-app-server-vs-claude-agent-sdk, openclaw-pi-hermes-state-management) should be linked from their subject pages.

`queries/2026-10-04-uncommitted-wip-snapshot-query` (3,680L) is a one-off WIP snapshot — leave as-is or move to `_archive`.

## 6. Stale pages

2,563 (>90 days) — dominated by bulk-import `updated` dates from April–August. Counts are stable week-over-week (+5); no degradation. No action beyond selective size-prioritized review.

## 7. Oversized pages

335 (>200L). Stable vs last week (+5). Top split candidates unchanged: `agentic-search` (1,212L), `entities/harvey` (1,133L), `entities/simon-willison` (1,121L), `entities/anthropic` (982L). Defer to dedicated splitting passes.

## 8. Sibling WIP

`git status --short -- wiki/` shows only the prior-week's deleted report files (this job's diff) + today's new report. No sibling pipeline interference. Safe to commit the full wiki/ tree.

## Action list (prioritized)

| Priority | Action | Owner |
|---|---|---|
| MEDIUM | Add 4 genuine missing pages: `entities/huggingface`, `entities/ben-clavie`, `concepts/claude-opus-4-7`, alias `concepts/agent-harness-comparison` | wiki-entity-enrichment |
| MEDIUM | Link top-10 content-rich orphans from their natural hubs | manual / skeleton-enrich |
| LOW | Cross-link the 4 intentional entity/concept split pairs (cline, omnara, qwen, agent-harnesses) | manual |
| LOW | Add `queries/2026-11-13-skeleton-enrich-stub-action` to index.md | manual |
| LOW | Fix 150 bare/cross-namespace wikilinks (auto-fixable) | health-fix cron |
| NONE | Tag violations (0 real), stale index entries (0 real), duplicates (0 merges) | — |

## Notes

- Generator bug backlog (unchanged): index reconciliation should resolve `dir/_index.md`; dup detector should skip `redirect:` stubs; report rotation should rewrite its own index entry.
- `llm-wiki` skill skip is a name collision (research/ vs _overrides/), not an absence; not needed for this run.
