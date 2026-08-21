---
title: Weekly Wiki Graph Analysis
created: 2026-08-21
updated: 2026-08-21
type: query
tags: []
sources: []
---

# Weekly Wiki Graph Analysis

**Date**: 2026-08-21 15:03 UTC

## Summary

| Metric | Value |
|--------|-------|
| Total pages scanned | 2992 |
| Entities | 907 |
| Concepts | 2018 |
| Comparisons | 35 |
| Queries | 5 |
| Events | 27 |
| Orphans (no inbound links) | 477 |
| Content-rich orphans | 474 |
| Broken wikilinks | 3508 |
| Fixable wikilinks | 211 |
| Duplicate groups | 16 |
| Oversized pages (>200 lines) | 309 |
| Missing sources | 0 (0%) |
| Tag violations | 1083 |
| Stale pages (>90 days) | 1424 |
| Skeleton pages | 1 |
| Not indexed in index.md | 26 |
| Stale index entries | 7 |

## 1. Orphan Pages

477 pages have zero inbound links from other wiki pages.

### Content-Rich Orphans (top 15)

- **concepts/harness-engineering/system-architecture/claude-code-best-practices** — 385 lines, 19 outbound links
- **concepts/ai-energy** — 284 lines, 29 outbound links
- **concepts/multi-objective-policy-distillation** — 279 lines, 24 outbound links
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
- content-rich: 474
- skeleton: 3

## 2. Broken Wikilinks

3508 total broken links.

| Issue Type | Count | Description |
|------------|-------|-------------|
| bare-wikilink-missing | 1802 | Bare name, target page does not exist |
| missing | 1495 | Namespaced link to a page that does not exist |
| cross-namespace | 125 | Entity ↔ concept namespace mismatch (auto-fixable) |
| bare-wikilink | 86 | Bare name without namespace prefix (auto-fixable) |

### Top Broken Targets (pages that need creating)

- [[concepts/claude-code/claude-code]] — 35 references
- [[]] — 29 references
- [[agent-evaluation]] — 24 references
- [[grpo]] — 21 references
- [[gaia-benchmark]] — 19 references
- [[reinforcement-learning]] — 18 references
- [[entities/sglang]] — 17 references
- [[concepts/agent-evaluation]] — 16 references
- [[concepts/agent-memory]] — 15 references
- [[hal-leaderboard]] — 15 references
- [[concepts/ai-safety]] — 14 references
- [[agentdojo]] — 14 references
- [[entities/cursor]] — 13 references
- [[concepts/ai-governance]] — 13 references
- [[agent-security-bench]] — 13 references

### Fixable Links (sample)

211 links can be auto-fixed (cross-namespace or bare → namespaced).

- `entities/alex-ellis`: [[concepts/opencode]] → [[entities/opencode]]
- `entities/cactuscompute`: [[edge-llm-microcontroller]] → [[concepts/edge-llm-microcontroller]]
- `entities/cactuscompute`: [[small-language-models]] → [[concepts/small-language-models]]
- `entities/claude-code`: [[entities/coding-agents]] → [[concepts/coding-agents]]
- `entities/cohere`: [[tools/wiz]] → [[entities/wiz]]
- `entities/deepmind`: [[concepts/gemma-4]] → [[entities/gemma-4]]
- `entities/denseon-lateon`: [[concepts/embeddings]] → [[entities/embeddings]]
- `entities/drew-breunig--core-ideas`: [[entities/dspy]] → [[concepts/dspy]]
- `entities/drew-breunig`: [[entities/dspy]] → [[concepts/dspy]]
- `entities/dsprrr`: [[entities/dspy]] → [[concepts/dspy]]
- ... and 201 more

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
- **7 index entries** reference files that no longer exist

### Not-Indexed by Category

- concepts: 24
- entities: 1
- queries: 1

## 5. Oversized Pages (>200 lines)

309 pages exceed the 200-line threshold.

- **concepts/agentic-search** — 1191 lines
- **entities/harvey** — 913 lines
- **entities/ed-zitron** — 887 lines
- **entities/simon-willison** — 874 lines
- **entities/anthropic** — 831 lines
- **concepts/rlm-recursive-language-models** — 742 lines
- **entities/fireworks-ai** — 716 lines
- **concepts/dspy-rlm** — 698 lines
- **entities/claude-code** — 629 lines
- **entities/openai** — 628 lines
- ... and 299 more

## 6. Stale Pages (>90 days since update)

1424 pages have not been updated in over 90 days.

## 7. Tag Violations

1083 pages use non-canonical tags.

## 8. Recommended Actions

- [MEDIUM] Fix 211 cross-namespace / bare wikilinks
- [MEDIUM] Add inbound links to 474 content-rich orphan pages
- [HIGH] Review and consolidate 16 potential duplicate groups
- [LOW] Consider splitting 309 oversized pages (>200 lines)
- [HIGH] Fix 1083 pages with non-canonical tags
- [MEDIUM] Remove 7 stale index entries (files missing)
- [LOW] 1424 pages stale >90 days - review needed
- [MEDIUM] 1 skeleton pages need enrichment

---
*Generated by `scripts/_weekly_graph_report.py`*
