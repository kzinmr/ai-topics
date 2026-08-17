---
title: Weekly Wiki Graph Analysis
created: 2026-08-14
updated: 2026-08-17
type: query
tags: [wiki]
sources: []
---

# Weekly Wiki Graph Analysis

**Date**: 2026-08-14 15:15 UTC

## Summary

| Metric | Value |
|--------|-------|
| Total pages scanned | 2962 |
| Entities | 901 |
| Concepts | 1995 |
| Comparisons | 35 |
| Queries | 4 |
| Events | 27 |
| Orphans (no inbound links) | 479 |
| Content-rich orphans | 476 |
| Broken wikilinks | 3463 |
| Fixable wikilinks | 209 |
| Duplicate groups | 16 |
| Oversized pages (>200 lines) | 303 |
| Missing sources | 4 (0%) |
| Tag violations | 1021 |
| Stale pages (>90 days) | 1313 |
| Skeleton pages | 0 |
| Not indexed in index.md | 26 |
| Stale index entries | 8 |

## 1. Orphan Pages

479 pages have zero inbound links from other wiki pages.

### Content-Rich Orphans (top 15)

- **concepts/harness-engineering/system-architecture/claude-code-best-practices** — 385 lines, 19 outbound links
- **concepts/multi-objective-policy-distillation** — 279 lines, 24 outbound links
- **concepts/ai-energy** — 274 lines, 27 outbound links
- **entities/openenv** — 234 lines, 6 outbound links
- **concepts/claude/system-card-milestones** — 231 lines, 6 outbound links
- **entities/ibrahim-diallo** — 227 lines, 9 outbound links
- **concepts/symphony** — 208 lines, 9 outbound links
- **concepts/autonomous-agent-marketplace-stack** — 199 lines, 7 outbound links
- **concepts/ai-benchmarks/skillspector** — 188 lines, 13 outbound links
- **concepts/llm-memory-architecture** — 188 lines, 6 outbound links
- **concepts/mistral-ocr-4** — 188 lines, 11 outbound links
- **concepts/hegel-property-based-testing** — 187 lines, 14 outbound links
- **concepts/spine-swarm-agents** — 187 lines, 15 outbound links
- **concepts/nvidia-blackwell-architecture** — 186 lines, 15 outbound links
- **comparisons/codex-app-server-vs-claude-agent-sdk** — 185 lines, 1 outbound links

### All Orphans by Category
- content-rich: 476
- skeleton: 3

## 2. Broken Wikilinks

3463 total broken links.

| Issue Type | Count | Description |
|------------|-------|-------------|
| bare-wikilink-missing | 1765 | Bare name, target page does not exist |
| missing | 1489 | Namespaced link to a page that does not exist |
| cross-namespace | 124 | Entity ↔ concept namespace mismatch (auto-fixable) |
| bare-wikilink | 85 | Bare name without namespace prefix (auto-fixable) |

### Top Broken Targets (pages that need creating)

- [[concepts/claude-code/claude-code]] — 35 references
- [[agent-evaluation]] — 23 references
- [[grpo]] — 22 references
- [[]] — 21 references
- [[gaia-benchmark]] — 19 references
- [[reinforcement-learning]] — 18 references
- [[entities/sglang]] — 17 references
- [[concepts/agent-evaluation]] — 16 references
- [[hal-leaderboard]] — 15 references
- [[agentdojo]] — 14 references
- [[concepts/agent-memory]] — 13 references
- [[entities/cursor]] — 13 references
- [[concepts/ai-safety]] — 13 references
- [[concepts/ai-governance]] — 13 references
- [[agent-security-bench]] — 13 references

### Fixable Links (sample)

209 links can be auto-fixed (cross-namespace or bare → namespaced).

- `entities/alex-ellis`: [[concepts/opencode]] → [[entities/opencode]]
- `entities/cactuscompute`: [[edge-llm-microcontroller]] → [[concepts/edge-llm-microcontroller]]
- `entities/cactuscompute`: [[small-language-models]] → [[concepts/small-language-models]]
- `entities/claude-code`: [[entities/coding-agents]] → [[concepts/coding-agents]]
- `entities/deepmind`: [[concepts/gemma-4]] → [[entities/gemma-4]]
- `entities/denseon-lateon`: [[concepts/embeddings]] → [[entities/embeddings]]
- `entities/drew-breunig--core-ideas`: [[entities/dspy]] → [[concepts/dspy]]
- `entities/drew-breunig`: [[entities/dspy]] → [[concepts/dspy]]
- `entities/dsprrr`: [[entities/dspy]] → [[concepts/dspy]]
- `entities/harvey`: [[entities/claude]] → [[concepts/claude]]
- ... and 199 more

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

- **26 pages** are on disk but not listed in index.md
- **8 index entries** reference files that no longer exist

### Not-Indexed by Category

- concepts: 23
- entities: 2
- queries: 1

## 5. Oversized Pages (>200 lines)

303 pages exceed the 200-line threshold.

- **concepts/agentic-search** — 1191 lines
- **entities/ed-zitron** — 885 lines
- **entities/simon-willison** — 863 lines
- **entities/anthropic** — 827 lines
- **concepts/rlm-recursive-language-models** — 742 lines
- **entities/fireworks-ai** — 711 lines
- **concepts/dspy-rlm** — 698 lines
- **entities/claude-code** — 629 lines
- **entities/harvey** — 613 lines
- **entities/openai** — 611 lines
- ... and 293 more

## 6. Stale Pages (>90 days since update)

1313 pages have not been updated in over 90 days.

## 7. Tag Violations

1021 pages use non-canonical tags.

## 8. Recommended Actions

- [MEDIUM] Fix 209 cross-namespace / bare wikilinks
- [MEDIUM] Add inbound links to 476 content-rich orphan pages
- [HIGH] Review and consolidate 16 potential duplicate groups
- [LOW] Consider splitting 303 oversized pages (>200 lines)
- [HIGH] Fix 1021 pages with non-canonical tags
- [MEDIUM] Remove 8 stale index entries (files missing)
- [LOW] 1313 pages stale >90 days - review needed

---
*Generated by `scripts/_weekly_graph_report.py`*
