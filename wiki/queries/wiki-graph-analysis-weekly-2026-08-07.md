---
title: Weekly Wiki Graph Analysis
created: 2026-08-07
updated: 2026-08-07
type: query
tags: []
sources: []
---

# Weekly Wiki Graph Analysis

**Date**: 2026-08-07 15:11 UTC

## Summary

| Metric | Value |
|--------|-------|
| Total pages scanned | 2917 |
| Entities | 884 |
| Concepts | 1968 |
| Comparisons | 35 |
| Queries | 5 |
| Events | 25 |
| Orphans (no inbound links) | 43 |
| Content-rich orphans | 43 |
| Broken wikilinks | 3390 |
| Fixable wikilinks | 187 |
| Duplicate groups | 16 |
| Oversized pages (>200 lines) | 292 |
| Missing sources | 4 (0%) |
| Tag violations | 976 |
| Stale pages (>90 days) | 1204 |
| Skeleton pages | 0 |
| Not indexed in index.md | 26 |
| Stale index entries | 7 |

## 1. Orphan Pages

43 pages have zero inbound links from other wiki pages.

### Content-Rich Orphans (top 15)

- **concepts/local-llm/dgx-spark-nim** — 302 lines, 0 outbound links
- **concepts/automation-series** — 281 lines, 0 outbound links
- **concepts/qlora** — 234 lines, 0 outbound links
- **comparisons/codex-app-server-vs-agent-protocols** — 209 lines, 0 outbound links
- **comparisons/harness-backend-routing** — 185 lines, 0 outbound links
- **concepts/ai-benchmarks/simpleqa** — 175 lines, 0 outbound links
- **concepts/ai-benchmarks/ifeval** — 173 lines, 0 outbound links
- **concepts/ai-benchmarks/mrcr** — 162 lines, 0 outbound links
- **entities/antoine-buteau** — 149 lines, 0 outbound links
- **concepts/ai-benchmarks/bfcl-v3** — 147 lines, 0 outbound links
- **concepts/cloudflare-email-sending** — 131 lines, 0 outbound links
- **concepts/good-regulator-theorem** — 125 lines, 0 outbound links
- **concepts/hermes-codex-app-server-runtime** — 125 lines, 0 outbound links
- **comparisons/google-alerts-alternatives-2026** — 120 lines, 0 outbound links
- **entities/luke-curley** — 116 lines, 0 outbound links

### All Orphans by Category
- content-rich: 43

## 2. Broken Wikilinks

3390 total broken links.

| Issue Type | Count | Description |
|------------|-------|-------------|
| bare-wikilink-missing | 1709 | Bare name, target page does not exist |
| missing | 1494 | Namespaced link to a page that does not exist |
| cross-namespace | 125 | Entity ↔ concept namespace mismatch (auto-fixable) |
| bare-wikilink | 62 | Bare name without namespace prefix (auto-fixable) |

### Top Broken Targets (pages that need creating)

- [[concepts/claude-code/claude-code]] — 35 references
- [[agent-evaluation]] — 23 references
- [[grpo]] — 22 references
- [[gaia-benchmark]] — 19 references
- [[reinforcement-learning]] — 18 references
- [[entities/sglang]] — 17 references
- [[concepts/agent-evaluation]] — 16 references
- [[]] — 15 references
- [[hal-leaderboard]] — 15 references
- [[agentdojo]] — 14 references
- [[concepts/agent-memory]] — 13 references
- [[entities/cursor]] — 13 references
- [[concepts/ai-safety]] — 13 references
- [[concepts/ai-governance]] — 13 references
- [[agent-security-bench]] — 13 references

### Fixable Links (sample)

187 links can be auto-fixed (cross-namespace or bare → namespaced).

- `entities/alex-ellis`: [[concepts/opencode]] → [[entities/opencode]]
- `entities/claude-code`: [[entities/coding-agents]] → [[concepts/coding-agents]]
- `entities/deepmind`: [[concepts/gemma-4]] → [[entities/gemma-4]]
- `entities/denseon-lateon`: [[concepts/embeddings]] → [[entities/embeddings]]
- `entities/drew-breunig--core-ideas`: [[entities/dspy]] → [[concepts/dspy]]
- `entities/drew-breunig`: [[entities/dspy]] → [[concepts/dspy]]
- `entities/dsprrr`: [[entities/dspy]] → [[concepts/dspy]]
- `entities/harvey`: [[entities/claude]] → [[concepts/claude]]
- `entities/hugo-bowne-anderson`: [[entities/show-us-your-agent-skills]] → [[concepts/show-us-your-agent-skills]]
- `entities/jina-ai`: [[concepts/embeddings]] → [[entities/embeddings]]
- ... and 177 more

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

- concepts: 23
- entities: 2
- queries: 1

## 5. Oversized Pages (>200 lines)

292 pages exceed the 200-line threshold.

- **concepts/agentic-search** — 1191 lines
- **entities/ed-zitron** — 812 lines
- **entities/simon-willison** — 809 lines
- **entities/anthropic** — 807 lines
- **concepts/rlm-recursive-language-models** — 742 lines
- **concepts/dspy-rlm** — 698 lines
- **entities/fireworks-ai** — 634 lines
- **entities/openai** — 598 lines
- **entities/openai-codex** — 593 lines
- **entities/claude-code** — 575 lines
- ... and 282 more

## 6. Stale Pages (>90 days since update)

1204 pages have not been updated in over 90 days.

## 7. Tag Violations

976 pages use non-canonical tags.

## 8. Recommended Actions

- [MEDIUM] Fix 187 cross-namespace / bare wikilinks
- [MEDIUM] Add inbound links to 43 content-rich orphan pages
- [HIGH] Review and consolidate 16 potential duplicate groups
- [LOW] Consider splitting 292 oversized pages (>200 lines)
- [HIGH] Fix 976 pages with non-canonical tags
- [MEDIUM] Remove 7 stale index entries (files missing)
- [LOW] 1204 pages stale >90 days - review needed

---
*Generated by `scripts/_weekly_graph_report.py`*
