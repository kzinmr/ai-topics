---
title: Weekly Wiki Graph Analysis
created: 2026-10-30
updated: 2026-10-30
type: query
tags: []
sources: []
---

# Weekly Wiki Graph Analysis

**Date**: 2026-10-30 15:01 UTC

## Summary

| Metric | Value |
|--------|-------|
| Total pages scanned | 3351 |
| Entities | 959 |
| Concepts | 2267 |
| Comparisons | 35 |
| Queries | 45 |
| Events | 45 |
| Orphans (no inbound links) | 477 |
| Content-rich orphans | 466 |
| Broken wikilinks | 3378 |
| Fixable wikilinks | 172 |
| Duplicate groups | 18 |
| Oversized pages (>200 lines) | 325 |
| Missing sources | 0 (0%) |
| Tag violations | 1 |
| Stale pages (>90 days) | 2420 |
| Skeleton pages | 0 |
| Not indexed in index.md | 29 |
| Stale index entries | 28 |

## 1. Orphan Pages

477 pages have zero inbound links from other wiki pages.

### Content-Rich Orphans (top 15)

- **queries/2026-10-04-uncommitted-wip-snapshot-query** — 3680 lines, 1297 outbound links
- **concepts/harness-engineering/system-architecture/claude-code-best-practices** — 385 lines, 19 outbound links
- **concepts/multi-objective-policy-distillation** — 279 lines, 24 outbound links
- **entities/openenv** — 234 lines, 6 outbound links
- **concepts/claude/system-card-milestones** — 231 lines, 6 outbound links
- **entities/ibrahim-diallo** — 227 lines, 9 outbound links
- **concepts/symphony** — 208 lines, 9 outbound links
- **concepts/ai-benchmarks/skillspector** — 188 lines, 13 outbound links
- **concepts/hegel-property-based-testing** — 187 lines, 14 outbound links
- **concepts/spine-swarm-agents** — 187 lines, 15 outbound links
- **comparisons/codex-app-server-vs-claude-agent-sdk** — 185 lines, 1 outbound links
- **comparisons/openclaw-pi-hermes-state-management** — 183 lines, 8 outbound links
- **concepts/reasoning-trace-extraction-vulnerability** — 181 lines, 8 outbound links
- **concepts/db9-filesystem-sql** — 179 lines, 3 outbound links
- **queries/saas-future-and-agent-developer-career** — 178 lines, 19 outbound links

### All Orphans by Category
- content-rich: 466
- skeleton: 11

## 2. Broken Wikilinks

3378 total broken links.

| Issue Type | Count | Description |
|------------|-------|-------------|
| bare-wikilink-missing | 1680 | Bare name, target page does not exist |
| missing | 1526 | Namespaced link to a page that does not exist |
| bare-wikilink | 133 | Bare name without namespace prefix (auto-fixable) |
| cross-namespace | 39 | Entity ↔ concept namespace mismatch (auto-fixable) |

### Top Broken Targets (pages that need creating)

- [[]] — 39 references
- [[agent-evaluation]] — 24 references
- [[entities/cursor]] — 13 references
- [[concepts/enterprise-ai]] — 12 references
- [[concepts/ai-governance]] — 12 references
- [[concepts/agent-architecture]] — 10 references
- [[concepts/ai-adoption]] — 10 references
- [[concepts/inference-optimization]] — 9 references
- [[concepts/bitter-lesson]] — 9 references
- [[entities/huggingface]] — 9 references
- [[concepts/claude-opus-4-7]] — 9 references
- [[concepts/ai-benchmarks/swe-bench\]] — 9 references
- [[concepts/ai-coding]] — 8 references
- [[entities/ben-clavie]] — 8 references
- [[ai-governance]] — 8 references

### Fixable Links (sample)

172 links can be auto-fixed (cross-namespace or bare → namespaced).

- `entities/alloomi-ai`: [[context-engineering]] → [[concepts/context-engineering]]
- `entities/apple-onnx-mlx-modelscope`: [[entities/mlx]] → [[concepts/mlx]]
- `entities/bill-gates`: [[ai-employment-displacement]] → [[concepts/ai-employment-displacement]]
- `entities/cohere`: [[tools/wiz]] → [[entities/wiz]]
- `entities/dqwen3-5`: [[diffusion-language-models]] → [[concepts/diffusion-language-models]]
- `entities/dqwen3-5`: [[ssm-mamba]] → [[concepts/ssm-mamba]]
- `entities/dqwen3-5`: [[transformer-architecture]] → [[concepts/transformer-architecture]]
- `entities/dqwen3-5`: [[diffusion-language-models]] → [[concepts/diffusion-language-models]]
- `entities/dqwen3-5`: [[qwen]] → [[entities/qwen]]
- `entities/dqwen3-5`: [[ssm-mamba]] → [[concepts/ssm-mamba]]
- ... and 162 more

## 3. Duplicate / Similar Pages

18 potential duplicate groups detected by normalized name matching.

- `index`: entities/_index, concepts/_index
- `cline`: entities/cline, concepts/cline
- `deliberatecoder`: entities/deliberate-coder, entities/deliberatecoder
- `eugeneyan`: entities/eugene-yan, entities/eugeneyan
- `gilesthomas`: entities/giles-thomas, entities/gilesthomas
- `lilianweng`: entities/lilian-weng, entities/lilianweng
- `martinfowler`: entities/martin-fowler, entities/martinfowler
- `nvidiaopenshell`: entities/nvidia-openshell, concepts/nvidia-openshell
- `omnara`: entities/omnara, concepts/omnara
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

- **29 pages** are on disk but not listed in index.md
- **28 index entries** reference files that no longer exist

### Not-Indexed by Category

- concepts: 24
- entities: 4
- queries: 1

## 5. Oversized Pages (>200 lines)

325 pages exceed the 200-line threshold.

- **queries/2026-10-04-uncommitted-wip-snapshot-query** — 3680 lines
- **concepts/agentic-search** — 1212 lines
- **entities/harvey** — 1032 lines
- **entities/simon-willison** — 1019 lines
- **entities/anthropic** — 921 lines
- **entities/ed-zitron** — 918 lines
- **entities/fireworks-ai** — 760 lines
- **concepts/rlm-recursive-language-models** — 742 lines
- **entities/openai** — 699 lines
- **concepts/dspy-rlm** — 698 lines
- ... and 315 more

## 6. Stale Pages (>90 days since update)

2420 pages have not been updated in over 90 days.

## 7. Tag Violations

1 pages use non-canonical tags.

## 8. Recommended Actions

- [MEDIUM] Fix 172 cross-namespace / bare wikilinks
- [MEDIUM] Add inbound links to 466 content-rich orphan pages
- [HIGH] Review and consolidate 18 potential duplicate groups
- [LOW] Consider splitting 325 oversized pages (>200 lines)
- [HIGH] Fix 1 pages with non-canonical tags
- [MEDIUM] Remove 28 stale index entries (files missing)
- [LOW] 2420 pages stale >90 days - review needed

---
*Generated by `scripts/_weekly_graph_report.py`*
