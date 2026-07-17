---
title: Weekly Wiki Graph Analysis
created: 2026-07-17
updated: 2026-07-17
type: query
tags: [wiki-maintenance, graph-analysis]
sources: []
---

# Weekly Wiki Graph Analysis

**Date**: 2026-07-17 15:06 UTC

## Summary

| Metric | This Week (Jul 17) | Last Week (Jul 10) | Change |
|--------|-------------------|-------------------|--------|
| Total pages | **2,249** | 2,201 | **+48** |
| Entities | 849 | 836 | +13 |
| Concepts | 1,342 | 1,312 | +30 |
| Comparisons | 35 | 34 | +1 |
| Queries | 6 | 4 | +2 |
| Events | 17 | 15 | +2 |
| Orphans (no inbound links) | **38** | 38 | 0 |
| Broken wikilinks | **4,302** | 4,274 | **+28** 🔴 |
| Fixable wikilinks | **99** | 224 | **−125** ✅ |
| Duplicate groups | **16** | 14 | **+2** 🔴 |
| Oversized pages (>200 lines) | **211** | 207 | **+4** 🔴 |
| Missing sources | 5 (0.2%) | 5 (0.2%) | → same |
| Tag violations | 0 | 0 | ✅ perfect |
| Stale pages (>90 days) | **106** | 59 | **+47** 🔴 |
| Not indexed in index.md | 2 | 2 | → same |
| Stale index entries | 542 | 541 | +1 🔴 |
| Person→Concept graph | 188P × 1,811C | 187P × 1,781C | +1P/+30C |

**Overall Health Trend**: The wiki continues to grow steadily (+48 pages). Fixable wikilinks dropped significantly (−125), indicating automated link repair is working. However, **stale pages nearly doubled to 106** as the April bulk import cohort passes the 90-day threshold. Broken links crept up (+28) — likely from new pages adding references to pages that don't exist yet. Duplicate groups increased by 2, suggesting new pages were created with naming inconsistencies.

## 1. Orphan Pages (No Inbound Links)

**38 total orphans** — unchanged from last week. All are content-rich.

### Top 10 Content-Rich Orphans (Need Linking)

| Page | Lines | Outbound Links | Type |
|------|-------|----------------|------|
| concepts/automation-series | 281 | 0 | Concept |
| concepts/qlora | 234 | 0 | Concept |
| queries/wiki-graph-analysis-weekly-2026-07-10 | 228 | 0 | Query |
| comparisons/codex-app-server-vs-agent-protocols | 209 | 0 | Comparison |
| comparisons/harness-backend-routing | 185 | 0 | Comparison |
| concepts/glut-of-circuits | 160 | 0 | Concept |
| entities/antoine-buteau | 149 | 0 | Entity |
| concepts/cloudflare-email-sending | 131 | 0 | Concept |
| concepts/good-regulator-theorem | 125 | 0 | Concept |
| concepts/hermes-codex-app-server-runtime | 125 | 0 | Concept |

**0 orphans resolved this week** — no progress on linking. The automation-series (281 lines) is the highest-value target: adding it to a relevant concept page (agentic-automation, AI-pipelines) would fix the biggest gap.

## 2. Broken Wikilinks

**4,302 total broken links** (up from 4,274 last week, +28 🔴). Fixable links dropped sharply from 224→99.

| Issue Type | This Week | Last Week | Change |
|------------|-----------|-----------|--------|
| bare-wikilink-missing | 2,855 | 2,765 | +90 |
| missing | 1,348 | 1,285 | +63 |
| cross-namespace | 83 | 82 | +1 |
| bare-wikilink | 16 | 142 | **−126** ✅ |

**Fixable**: 99 links (cross-namespace / bare → namespaced) — the automated repair pipeline is making progress on bare wikilinks (−126).

### Top Missing Targets (Pages Needing Creation)

| Missing Target | Refs This Week | Refs Last Week | Trend |
|----------------|---------------|----------------|-------|
| concepts/context-engineering | **131** | 128 | ⬆️ +3 |
| concepts/security-and-governance/ai-safety | **71** | 67 | ⬆️ +4 |
| concepts/coding-agents/coding-agents | **64** | 52 | ⬆️ +12 |
| concepts/harness-engineering/agent-harness | **61** | 61 | → same |
| concepts/post-training/grpo-rl-training | **36** | 36 | → same |
| concepts/security-and-governance/agent-sandboxing | **34** | 34 | → same |
| concepts/anthropic/managed-agents | **32** | 32 | → same |
| concepts/post-training/grpo | **33** | 32 | ⬆️ +1 |
| concepts/post-training/rlhf | **31** | 31 | → same |
| concepts/security-and-governance/agent-governance | **30** | 30 | → same |

**Note**: Most references are going up (new pages link to these missing targets), making it even more urgent to create stub pages. `context-engineering` alone now accounts for 131 broken links — creating this single page would fix ~3% of ALL broken wikilinks.

Many missing targets reference sub-paths (`security-and-governance/ai-safety`, `post-training/grpo`) suggesting a planned hierarchical restructuring that was never completed. Creating redirect stubs would resolve hundreds of links at once.

## 3. Duplicate / Similar Pages

**16 potential duplicate groups** (up from 14 last week, +2).

### Entity↔Entity Duplicates (same person, different slug)

| Normalized | Pages | Status vs Last Week |
|------------|-------|---------------------|
| deliberatecoder | entities/deliberate-coder, entities/deliberatecoder | → same |
| eugeneyan | entities/eugene-yan, entities/eugeneyan | → same |
| gilesthomas | entities/giles-thomas, entities/gilesthomas | → same |
| lilianweng | entities/lilian-weng, entities/lilianweng | → same |
| martinfowler | entities/martin-fowler, entities/martinfowler | → same |
| samuelcolvin | entities/samuel-colvin, entities/samuelcolvin | → same |

**No progress on entity dupes for 2 weeks**. These 6 pairs need consolidation.

### Entity↔Concept / Concept↔Concept Cross-Type Duplicates

| Normalized | Pages | Status |
|------------|-------|--------|
| index | entities/_index, concepts/_index | **Legitimate** — both needed |
| cline | entities/cline, concepts/cline | 🔴 NEW this week |
| qwen | entities/qwen, concepts/qwen | 🔴 NEW this week |
| agentharnesses | concepts/agent-harnesses, comparisons/agent-harnesses | → same |
| alphaproofnexus | concepts/alpha-proof-nexus, concepts/alphaproof-nexus | → same |
| deerflow | concepts/deer-flow, concepts/deerflow | → same |
| dspyrlm | concepts/dspy-rlm, concepts/dspyrlm | → same |
| evalsskills | concepts/evals-skills, comparisons/evals-skills | → same |
| llmintegrationpatterns | concepts/llm-integration-patterns, comparisons/llm-integration-patterns | → same |
| openclawecosystem | concepts/open-claw-ecosystem, concepts/openclaw-ecosystem | → same |

**2 new duplicates detected**: `cline` and `qwen` now exist in both entities/ and concepts/. These need disambiguation — should be entities (products/companies) with concept pages linking back.

**Duplicate content concern**: `concepts/dspy-rlm` (698 lines) and `concepts/rlm-recursive-language-models` (698 lines) still appear to be identical content. Both also appeared as **oversized** last week. Needs investigation and merge.

## 4. Index Reconciliation

| Metric | This Week | Last Week | Change |
|--------|-----------|-----------|--------|
| Pages not in index.md | **2** | 2 | → same |
| Index entries not on disk | **542** | 541 | +1 |

The 2 index gaps are `_index` pages for entities and concepts — these are meta-pages that don't need indexing.

542 stale index entries (files referenced in index.md that no longer exist on disk) need a cleanup sweep.

## 5. Oversized Pages (>200 lines)

**211 pages** exceed the threshold (up from 207, +4).

| Page | Lines | Change vs Last Week |
|------|-------|---------------------|
| concepts/agentic-search | 1,191 | +0 |
| entities/anthropic | 710 | +0 |
| concepts/dspy-rlm | 698 | +0 |
| concepts/rlm-recursive-language-models | 698 | +0 |
| entities/ed-zitron | 650 | +45 🔴 |
| entities/simon-willison | 614 | +45 🔴 |
| entities/openai | 580 | +11 |
| concepts/ai-native-state-management | 562 | +0 |
| concepts/harness-engineering | 550 | +0 |
| entities/andrej-karpathy | 546 | +0 |

**entity pages growing rapidly**: ed-zitron (+45 lines) and simon-willison (+45 lines) grew significantly. agentic-search (1,191 lines) remains the single largest page.

**Duplicate content concern persists**: dspy-rlm and rlm-recursive-language-models are both 698 lines — almost certainly identical copies.

## 6. Stale Pages (>90 Days Since Update)

**106 pages** stale (up from 59 last week, **+47** 🔴). This is the most concerning metric.

### Most Stale (>98 days)
- concepts/caid-coordination — 99d ago
- concepts/reasoning-model-cost-transparency — 99d ago
- **57 entity pages** from bulk import (Apr 10) — 98d ago
  - entities/abacaj, entities/adam-mastroianni, entities/agibot-10000-units, entities/amazon-rivr, entities/andriy-burkov, entities/arlan-r, entities/berthub-eu, entities/brutecat-com, entities/chad-nauseam-home, entities/chipro, entities/daniel-de-laney, entities/derek-thompson, entities/dorialexander, entities/doug-turnbull-blog, entities/doug-turnbull-core-ideas, entities/doug-turnbull-timeline, entities/downtowndougbrown-com, entities/drew-breunig--projects, etc.

**Expect this to grow further** — another ~250 entity pages will hit 90 days in the next 2 weeks. Consider a bulk entity refresh run.

## 7. Person × Concept Graph Analysis

**188 persons** and **1,811 concepts** analyzed (+1 person, +30 concepts since last week).

### Hub Persons (Most Connected)

| Person | Concepts | Persons | Core Ideas | Total | Change |
|--------|----------|---------|------------|-------|--------|
| **simon-willison** | 50 | 5 | 19 | **55** | +4 |
| **andrej-karpathy** | 25 | 1 | 17 | **26** | → same |
| **armin-ronacher** | 24 | 2 | 6 | **26** | → same |
| **peter-steinberger** | 19 | 4 | 7 | **23** | +1 |
| **doug-turnbull** | 20 | 1 | 13 | **21** | → same |
| **lilian-weng** | 14 | 3 | 6 | **17** | → same |
| **benjamin-clavie** | 15 | 1 | 8 | **16** | → same |
| **will-brown** | 9 | 6 | 7 | **15** | → same |
| **antirez-com** | 14 | 0 | 10 | **14** | → same |
| **florian-brand** | 9 | 5 | 4 | **14** | → same |

**simon-willison** extended his lead as the most connected hub (+4 concepts). New entries at the bottom of the top-20 include **shunyu-yao** (12 concepts), **dwarkesh-patel** (12), **chip-huyen** (11), and **elie-bakouch** (11) — all tied at 13 total connections.

### Bridge Concepts (Most Persons Connected)

| Concept | Persons | Key Contributors |
|---------|---------|-----------------|
| **_index** | 16 | Karpathy, antirez, simon-willison, etc. |
| **harness-engineering** | 15 | addy-osmani, boris-cherny, drmaciver, etc. |
| **agentic-engineering** | 15 | Karpathy, simon-willison, anildash, etc. (+1 new) |
| **vibe-coding** | 9 | Karpathy, addy-osmani, peter-steinberger (+1 new) |
| **context-engineering** | 8 | addy-osmani, drew-breunig, etc. |

### Intellectual Clusters (Top Similarity Pairs)

| Score | Person 1 | Person 2 | Overlap |
|-------|----------|----------|---------|
| **17.2** 🔗 | andrej-karpathy | simon-willison | _index, agent-documentation, agentic-engineering +2 |
| **13.9** 🔗 | deedydas | howdymary | autoresearch, harness-design-long-running-apps +2 |
| **12.0** 🔗 | tim-sh | tim-sherratt | digital-humanities, open-data |
| **11.5** 🔗 | koylan-ai | muratcan-koylan | agent-skills, context-engineering |
| **11.2** 🔗 | chip-huyen | lilian-weng | ai-engineering, genai-handbook, rlhf |
| **11.2** 🔗 | nathan-lambert | teknium | open-source-ai-destruction, post-training, rlhf-dpo-preference |
| **10.6** 🔗 | hillel-wayne | john-d-cook | formal-methods, formal-verification-llm-agents |
| **10.3** 🔗 | simon-willison | theo-browne | agentic-engineering, subagents, vibe-coding |

### Cross-Reference Gap Recommendations

**Person links to add** (high similarity, score ≥7, no direct link):

| Person 1 | Person 2 | Score | Shared Concepts |
|----------|----------|-------|-----------------|
| antirez-com | simon-willison | 7.5 | _index, agentic-engineering |
| drew-breunig | simon-willison | 7.5 | context-engineering, prompt-debt |
| andrej-karpathy | theo-browne | 9.0 | agentic-engineering, fable-5, vibe-coding |
| chip-huyen | will-brown | 7.9 | genai-handbook, rlhf |

Note: the antirez-com ↔ simon-willison and karpathy ↔ theo-browne gaps are high-value — these are top thought leaders who should reference each other.

**Concept cluster missing link**: `_index` ↔ `agentic-engineering` (score 6.0, 3 shared persons) still not directly linked in the wiki.

## 8. Tag Violations

**0 pages** use non-canonical tags. ✅ **Perfect compliance — 10 weeks running.**

## 9. Recommended Actions

| Priority | Action | Details | Trend |
|----------|--------|---------|-------|
| **HIGH** | Create concept/context-engineering stub | Fixes **131 broken links** from a single page | ⬆️ urgency growing |
| **HIGH** | Create redirect stubs for sub-path targets | Fix ~200 sub-path links (security-and-governance/, post-training/, coding-agents/) | → ongoing |
| **HIGH** | Merge duplicate entity pairs (6 pairs) | deliberate-coder, eugeneyan, giles-thomas, lilian-weng, martin-fowler, samuelcolvin | ⛔ no progress 2 weeks |
| **HIGH** | Disambiguate cline and qwen (entities vs concepts) | NEW dupes — decide canonical location | 🔴 NEW |
| **HIGH** | Investigate dspy-rlm ↔ rlm-recursive-language-models | Both 698 lines, same content? | → ongoing |
| **MEDIUM** | Add inbound links to 38 orphan pages | automation-series (281 lines) is highest-value target | ⛔ no progress |
| **MEDIUM** | Fix 99 auto-fixable wikilinks | cross-namespace and bare→namespaced | ✅ improving |
| **MEDIUM** | Bulk refresh for 106 stale pages | Bulk import entities from April need updating. 46 more pages per week expected. | 🔴 worsening |
| **MEDIUM** | Remove 542 stale index entries | index.md references files that no longer exist | → stable |
| **LOW** | Split top-10 oversized pages | agentic-search (1,191 lines) is biggest, ed-zitron (+45) growing | 🔴 growing |
| **LOW** | Add missing person↔concept cross-refs | 4 high-value gap recommendations from graph analysis | → same |

---

*Generated by `scripts/wiki_graph_analysis_weekly.py` + `scripts/wiki_graph.py`*
