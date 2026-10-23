---
title: Weekly Wiki Graph Analysis
created: 2026-10-23
updated: 2026-10-23
type: query
tags: []
sources: []
---

# Weekly Wiki Graph Analysis

**Date**: 2026-10-23 15:00 UTC

## Summary

| Metric | Value |
|--------|-------|
| Total pages scanned | 3288 |
| Entities | 954 |
| Concepts | 2217 |
| Comparisons | 35 |
| Queries | 41 |
| Events | 41 |
| Orphans (no inbound links) | 491 |
| Content-rich orphans | 485 |
| Broken wikilinks | 4223 |
| Fixable wikilinks | 352 |
| Duplicate groups | 16 |
| Oversized pages (>200 lines) | 321 |
| Missing sources | 0 (0%) |
| Tag violations | 1 |
| Stale pages (>90 days) | 2385 |
| Skeleton pages | 0 |
| Not indexed in index.md | 22 |
| Stale index entries | 27 |

## 1. Orphan Pages

491 pages have zero inbound links from other wiki pages.

### Content-Rich Orphans (top 15)

- **queries/2026-10-04-uncommitted-wip-snapshot-query** — 3680 lines, 1297 outbound links
- **concepts/harness-engineering/system-architecture/claude-code-best-practices** — 385 lines, 19 outbound links
- **concepts/ai-energy** — 317 lines, 33 outbound links
- **concepts/multi-objective-policy-distillation** — 279 lines, 24 outbound links
- **entities/openenv** — 234 lines, 6 outbound links
- **concepts/claude/system-card-milestones** — 231 lines, 6 outbound links
- **entities/ibrahim-diallo** — 227 lines, 9 outbound links
- **concepts/symphony** — 208 lines, 9 outbound links
- **concepts/ai-benchmarks/skillspector** — 188 lines, 13 outbound links
- **concepts/mistral-ocr-4** — 188 lines, 11 outbound links
- **concepts/hegel-property-based-testing** — 187 lines, 14 outbound links
- **concepts/spine-swarm-agents** — 187 lines, 15 outbound links
- **concepts/nvidia-blackwell-architecture** — 186 lines, 15 outbound links
- **comparisons/codex-app-server-vs-claude-agent-sdk** — 185 lines, 1 outbound links
- **comparisons/openclaw-pi-hermes-state-management** — 183 lines, 8 outbound links

### All Orphans by Category
- content-rich: 485
- skeleton: 6

## 2. Broken Wikilinks

4223 total broken links.

| Issue Type | Count | Description |
|------------|-------|-------------|
| bare-wikilink-missing | 2072 | Bare name, target page does not exist |
| missing | 1799 | Namespaced link to a page that does not exist |
| bare-wikilink | 229 | Bare name without namespace prefix (auto-fixable) |
| cross-namespace | 123 | Entity ↔ concept namespace mismatch (auto-fixable) |

### Top Broken Targets (pages that need creating)

- [[]] — 38 references
- [[concepts/claude-code/claude-code]] — 36 references
- [[concepts/ai-safety]] — 35 references
- [[agent-evaluation]] — 26 references
- [[grpo]] — 22 references
- [[gaia-benchmark]] — 20 references
- [[reinforcement-learning]] — 19 references
- [[concepts/agent-evaluation]] — 19 references
- [[concepts/agent-memory]] — 16 references
- [[hal-leaderboard]] — 16 references
- [[concepts/rag]] — 15 references
- [[concepts/tau-knowledge]] — 14 references
- [[agentdojo]] — 14 references
- [[concepts/swe-bench]] — 14 references
- [[entities/cursor]] — 13 references

### Fixable Links (sample)

352 links can be auto-fixed (cross-namespace or bare → namespaced).

- `entities/alex-ellis`: [[concepts/opencode]] → [[entities/opencode]]
- `entities/alloomi-ai`: [[opencontext]] → [[entities/opencontext]]
- `entities/alloomi-ai`: [[self-evolving-agents]] → [[concepts/self-evolving-agents]]
- `entities/alloomi-ai`: [[self-learning-agents]] → [[concepts/self-learning-agents]]
- `entities/alloomi-ai`: [[context-engineering]] → [[concepts/context-engineering]]
- `entities/alloomi-ai`: [[opencontext]] → [[entities/opencontext]]
- `entities/apple-onnx-mlx-modelscope`: [[entities/mlx]] → [[concepts/mlx]]
- `entities/bill-gates`: [[gary-marcus]] → [[entities/gary-marcus]]
- `entities/bill-gates`: [[ai-employment-displacement]] → [[concepts/ai-employment-displacement]]
- `entities/bill-gates`: [[gary-marcus]] → [[entities/gary-marcus]]
- ... and 342 more

## 3. Duplicate / Similar Pages

16 potential duplicate groups detected by normalized name matching.

- `index`: entities/_index, concepts/_index
- `cline`: entities/cline, concepts/cline
- `deliberatecoder`: entities/deliberate-coder, entities/deliberatecoder
- `eugeneyan`: entities/eugene-yan, entities/eugeneyan
- `gilesthomas`: entities/giles-thomas, entities/gilesthomas
- `lilianweng`: entities/lilian-weng, entities/lilianweng
- `martinfowler`: entities/martin-fowler, entities/martinfowler
- `qwen`: entities/qwen, concepts/qwen
- `samuelcolvin`: entities/samuel-colvin, entities/samuelcolvin
- `agentharnesses`: concepts/agent-harnesses, comparisons/agent-harnesses
- `alphaproofnexus`: concepts/alpha-proof-nexus, concepts/alphaproof-nexus
- `deerflow`: concepts/deer-flow, concepts/deerflow
- `dspyrlm`: concepts/dspy-rlm, concepts/dspyrlm
- `evalsskills`: concepts/evals-skills, comparisons/evals-skills
- `llmintegrationpatterns`: concepts/llm-integration-patterns, comparisons/llm-integration-patterns
- `openclawecosystem`: concepts/open-claw-ecosystem, concepts/openclaw-ecosystem

## 4. Index Reconciliation

- **22 pages** are on disk but not listed in index.md
- **27 index entries** reference files that no longer exist

### Not-Indexed by Category

- concepts: 22

## 5. Oversized Pages (>200 lines)

321 pages exceed the 200-line threshold.

- **queries/2026-10-04-uncommitted-wip-snapshot-query** — 3680 lines
- **concepts/agentic-search** — 1212 lines
- **entities/simon-willison** — 1008 lines
- **entities/harvey** — 985 lines
- **entities/ed-zitron** — 918 lines
- **entities/anthropic** — 909 lines
- **concepts/rlm-recursive-language-models** — 742 lines
- **entities/fireworks-ai** — 740 lines
- **concepts/dspy-rlm** — 698 lines
- **entities/openai** — 685 lines
- ... and 311 more

## 6. Stale Pages (>90 days since update)

2385 pages have not been updated in over 90 days.

## 7. Tag Violations

1 pages use non-canonical tags.

## 8. Recommended Actions

- [MEDIUM] Fix 352 cross-namespace / bare wikilinks
- [MEDIUM] Add inbound links to 485 content-rich orphan pages
- [HIGH] Review and consolidate 16 potential duplicate groups
- [LOW] Consider splitting 321 oversized pages (>200 lines)
- [HIGH] Fix 1 pages with non-canonical tags
- [MEDIUM] Remove 27 stale index entries (files missing)
- [LOW] 2385 pages stale >90 days - review needed

---
*Generated by `scripts/_weekly_graph_report.py`*
