---
title: Weekly Wiki Graph Analysis
created: 2026-07-31
updated: 2026-08-03
type: query
tags: []
sources: []
---

# Weekly Wiki Graph Analysis

**Date**: 2026-07-31 15:15 UTC

## Summary

| Metric | Value |
|--------|-------|
| Total pages scanned | 2877 |
| Entities | 871 |
| Concepts | 1945 |
| Comparisons | 35 |
| Queries | 4 |
| Events | 22 |
| Orphans (no inbound links) | 45 |
| Content-rich orphans | 45 |
| Broken wikilinks | 3261 |
| Fixable wikilinks | 146 |
| Duplicate groups | 16 |
| Oversized pages (>200 lines) | 286 |
| Missing sources | 5 (0%) |
| Tag violations | 941 |
| Stale pages (>90 days) | 978 |
| Skeleton pages | 0 |
| Not indexed in index.md | 25 |
| Stale index entries | 7 |

## 1. Orphan Pages

45 pages have zero inbound links from other wiki pages.

### Content-Rich Orphans (top 15)

- **concepts/local-llm/dgx-spark-nim** — 302 lines, 0 outbound links
- **concepts/automation-series** — 281 lines, 0 outbound links
- **concepts/qlora** — 234 lines, 0 outbound links
- **comparisons/codex-app-server-vs-agent-protocols** — 209 lines, 0 outbound links
- **comparisons/harness-backend-routing** — 185 lines, 0 outbound links
- **concepts/ai-benchmarks/simpleqa** — 174 lines, 0 outbound links
- **concepts/ai-benchmarks/ifeval** — 172 lines, 0 outbound links
- **concepts/ai-benchmarks/mrcr** — 161 lines, 0 outbound links
- **concepts/glut-of-circuits** — 160 lines, 0 outbound links
- **entities/antoine-buteau** — 149 lines, 0 outbound links
- **concepts/ai-benchmarks/bfcl-v3** — 146 lines, 0 outbound links
- **concepts/cloudflare-email-sending** — 131 lines, 0 outbound links
- **concepts/good-regulator-theorem** — 125 lines, 0 outbound links
- **concepts/hermes-codex-app-server-runtime** — 125 lines, 0 outbound links
- **comparisons/google-alerts-alternatives-2026** — 120 lines, 0 outbound links

### All Orphans by Category
- content-rich: 45

## 2. Broken Wikilinks

3261 total broken links.

| Issue Type | Count | Description |
|------------|-------|-------------|
| bare-wikilink-missing | 1627 | Bare name, target page does not exist |
| missing | 1488 | Namespaced link to a page that does not exist |
| cross-namespace | 123 | Entity ↔ concept namespace mismatch (auto-fixable) |
| bare-wikilink | 23 | Bare name without namespace prefix (auto-fixable) |

### Top Broken Targets (pages that need creating)

- [[concepts/claude-code/claude-code]] — 35 references
- [[agent-evaluation]] — 23 references
- [[grpo]] — 22 references
- [[gaia-benchmark]] — 19 references
- [[reinforcement-learning]] — 18 references
- [[entities/sglang]] — 17 references
- [[concepts/agent-evaluation]] — 15 references
- [[hal-leaderboard]] — 15 references
- [[agentdojo]] — 14 references
- [[concepts/agent-memory]] — 13 references
- [[entities/cursor]] — 13 references
- [[concepts/ai-safety]] — 13 references
- [[concepts/ai-governance]] — 13 references
- [[agent-security-bench]] — 12 references
- [[re-bench]] — 12 references

### Fixable Links (sample)

146 links can be auto-fixed (cross-namespace or bare → namespaced).

- `entities/andrew-chen`: [[entities/mac-studio-local-ai]] → [[concepts/mac-studio-local-ai]]
- `entities/claude-code`: [[entities/coding-agents]] → [[concepts/coding-agents]]
- `entities/deepmind`: [[concepts/gemma-4]] → [[entities/gemma-4]]
- `entities/denseon-lateon`: [[concepts/embeddings]] → [[entities/embeddings]]
- `entities/drew-breunig--core-ideas`: [[entities/dspy]] → [[concepts/dspy]]
- `entities/drew-breunig`: [[entities/dspy]] → [[concepts/dspy]]
- `entities/dsprrr`: [[entities/dspy]] → [[concepts/dspy]]
- `entities/harvey`: [[entities/claude]] → [[concepts/claude]]
- `entities/hugo-bowne-anderson`: [[entities/show-us-your-agent-skills]] → [[concepts/show-us-your-agent-skills]]
- `entities/jina-ai`: [[concepts/embeddings]] → [[entities/embeddings]]
- ... and 136 more

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

- **25 pages** are on disk but not listed in index.md
- **7 index entries** reference files that no longer exist

### Not-Indexed by Category

- concepts: 23
- entities: 2

## 5. Oversized Pages (>200 lines)

286 pages exceed the 200-line threshold.

- **concepts/agentic-search** — 1191 lines
- **entities/anthropic** — 782 lines
- **entities/ed-zitron** — 729 lines
- **concepts/dspy-rlm** — 698 lines
- **concepts/rlm-recursive-language-models** — 698 lines
- **entities/simon-willison** — 665 lines
- **entities/openai** — 598 lines
- **entities/claude-code** — 564 lines
- **entities/fireworks-ai** — 562 lines
- **concepts/ai-native-state-management** — 562 lines
- ... and 276 more

## 6. Stale Pages (>90 days since update)

978 pages have not been updated in over 90 days.

## 7. Tag Violations

941 pages use non-canonical tags.

## 8. Recommended Actions

- [MEDIUM] Fix 146 cross-namespace / bare wikilinks
- [MEDIUM] Add inbound links to 45 content-rich orphan pages
- [HIGH] Review and consolidate 16 potential duplicate groups
- [LOW] Consider splitting 286 oversized pages (>200 lines)
- [HIGH] Fix 941 pages with non-canonical tags
- [MEDIUM] Remove 7 stale index entries (files missing)
- [LOW] 978 pages stale >90 days - review needed

---
*Generated by `scripts/_weekly_graph_report.py`*
