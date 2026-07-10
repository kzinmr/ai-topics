---
title: Weekly Wiki Graph Analysis
created: 2026-07-10
updated: 2026-07-10
type: query
tags: [wiki-maintenance, graph-analysis]
sources: []
---

# Weekly Wiki Graph Analysis

**Date**: 2026-07-10 15:05 UTC

## Summary

| Metric | This Week | Last Week (Jul 5) | Change |
|--------|-----------|-------------------|--------|
| Total pages | 2,201 | 2,205 | -4 |
| Entities | 836 | 839 | -3 |
| Concepts | 1,312 | 1,316 | -4 |
| Comparisons | 34 | 33 | **+1** |
| Queries | 4 | 4 | 0 |
| Events | 15 | 13 | +2 |
| Orphans (no inbound links) | 38 | 43 | **-5** ✅ |
| Broken wikilinks | 4,274 | 4,890 | **-616** ✅ |
| Fixable wikilinks | 224 | 997 | **-773** ✅ |
| Duplicate groups | 14 | 39 | **-25** ✅ |
| Oversized pages (>200 lines) | 207 | 198 | **+9** 🔴 |
| Missing sources | 5 (0.2%) | 684 (31%) | **HUGE improvement** ✅ |
| Tag violations | 0 | 0 | ✅ |
| Stale pages (>90 days) | 59 | 0 | **⚠️ NEW** |
| Not indexed in index.md | 2 | 1,994 | **-1,992** ⭐ |
| Stale index entries | 541 | 20 | **+521** 🔴 |
| Unprocessed raw articles | 4,734 | — | — |
| Person→Concept graph | 187 persons × 1,781 concepts | — | — |

**Overall Health Trend**: Significant improvement this week. The index.md now covers virtually all pages (down from 1,994 gaps to just 2). Missing sources fixed en masse (31%→0.2%). Broken links reduced by 616 and duplicate groups consolidated from 39 to 14. Main new concern: 59 pages have now passed the 90-day stale threshold.

## 1. Orphan Pages (No Inbound Links)

**38 total orphans** (down from 43 last week). All are content-rich.

### Top 10 Content-Rich Orphans (Need Linking)

| Page | Lines | Outbound Links | Type |
|------|-------|----------------|------|
| concepts/automation-series | 281 | 0 | Concept |
| concepts/qlora | 234 | 0 | Concept |
| comparisons/codex-app-server-vs-agent-protocols | 209 | 0 | Comparison |
| comparisons/harness-backend-routing | 185 | 0 | Comparison |
| concepts/glut-of-circuits | 160 | 0 | Concept |
| entities/antoine-buteau | 149 | 0 | Entity |
| concepts/cloudflare-email-sending | 131 | 0 | Concept |
| concepts/good-regulator-theorem | 125 | 0 | Concept |
| concepts/hermes-codex-app-server-runtime | 125 | 0 | Concept |
| comparisons/google-alerts-alternatives-2026 | 120 | 0 | Comparison |

### 5 orphans resolved since last week
Pages that were orphans but now have inbound links:
- (not tracked per-page; overall count dropped from 43→38)

## 2. Broken Wikilinks

**4,274 total broken links** (down from 4,890 last week, -616).

| Issue Type | Count | Description |
|------------|-------|-------------|
| bare-wikilink-missing | 2,765 | Bare name, target page does not exist |
| missing | 1,285 | Namespaced link to nonexistent page |
| bare-wikilink | 142 | Bare name without namespace (auto-fixable) |
| cross-namespace | 82 | Entity↔Concept namespace mismatch (auto-fixable) |

**Fixable**: 224 links (cross-namespace / bare → namespaced) — down from 997 last week. Significant progress on auto-fixable links.

### Top Missing Targets (Pages Needing Creation)

| Missing Target | References | Impact |
|----------------|-----------|--------|
| concepts/context-engineering | 128 | **Critical** — most referenced missing page |
| concepts/security-and-governance/ai-safety | 67 | High |
| concepts/harness-engineering/agent-harness | 61 | High |
| concepts/coding-agents/coding-agents | 52 | High |
| concepts/post-training/grpo-rl-training | 36 | Medium |
| concepts/security-and-governance/agent-sandboxing | 34 | Medium |
| concepts/anthropic/managed-agents | 32 | Medium |
| concepts/post-training/grpo | 32 | Medium |
| concepts/post-training/rlhf | 31 | Medium |
| concepts/security-and-governance/agent-governance | 30 | Medium |

**Note**: Many missing targets reference sub-paths like `security-and-governance/ai-safety` or `post-training/grpo` — these suggest a planned hierarchical restructuring of the concept directory that hasn't been carried out. Creating stub redirect pages or _index pages for these directories would fix most of these broken links at once.

## 3. Duplicate / Similar Pages

**14 duplicate groups detected** (down from 39 last week, -25). Major consolidation achieved.

### Entity↔Entity Duplicates (same person, different slug)

| Normalized | Pages | Action Needed |
|------------|-------|---------------|
| deliberatecoder | entities/deliberate-coder, entities/deliberatecoder | Merge to deliberate-coder |
| eugeneyan | entities/eugene-yan, entities/eugeneyan | Merge to eugene-yan |
| gilesthomas | entities/giles-thomas, entities/gilesthomas | Merge to giles-thomas |
| lilianweng | entities/lilian-weng, entities/lilianweng | Merge to lilian-weng |
| martinfowler | entities/martin-fowler, entities/martinfowler | Merge to martin-fowler |
| samuelcolvin | entities/samuel-colvin, entities/samuelcolvin | Merge to samuel-colvin |

### Entity↔Concept Cross-Type Duplicates (need disambiguation)

| Normalized | Pages | Action Needed |
|------------|-------|---------------|
| index | entities/_index, concepts/_index | **Legitimate** — both needed |
| agentharnesses | concepts/agent-harnesses, comparisons/agent-harnesses | Consolidate to comparisons |
| alphaproofnexus | concepts/alpha-proof-nexus, concepts/alphaproof-nexus | Merge |
| deerflow | concepts/deer-flow, concepts/deerflow | Merge to deer-flow |
| dspyrlm | concepts/dspy-rlm, concepts/dspyrlm | Merge to dspy-rlm |
| evalsskills | concepts/evals-skills, comparisons/evals-skills | Consolidate to comparisons |
| llmintegrationpatterns | concepts/llm-integration-patterns, comparisons/llm-integration-patterns | Consolidate to comparisons |
| openclawecosystem | concepts/open-claw-ecosystem, concepts/openclaw-ecosystem | Merge to open-claw-ecosystem |

**25 duplicate groups resolved since last week** — excellent progress. Remaining 14 are mostly low-hanging fruit.

## 4. Index Reconciliation

**Pages not in index.md**: **2** (down from 1,994 last week — **massive improvement** ⭐)
- concepts/_index
- entities/_index

**Index entries not on disk**: **541** (up from 20 last week 🔴)
- This spike likely reflects the addition of many new pages to index.md during the bulk reconciliation effort
- Many entries may reference pages that were renamed or merged during the duplicate consolidation
- Recommend running an index sweep to remove stale entries

## 5. Oversized Pages (>200 lines)

**207 pages** exceed the threshold (up from 198 last week, +9).

| Page | Lines | Why It's Big |
|------|-------|--------------|
| concepts/agentic-search | 1,191 | Comprehensive survey — candidates for splitting |
| entities/anthropic | 710 | Company timeline + product catalog |
| concepts/dspy-rlm | 698 | Deep technical explainer |
| concepts/rlm-recursive-language-models | 698 | Mirrors dspy-rlm content → **possible duplication** |
| entities/ed-zitron | 605 | Blog compilation |
| entities/openai | 569 | Company timeline |
| entities/simon-willison | 569 | Major thought leader |
| concepts/ai-native-state-management | 562 | Technical deep-dive |
| concepts/harness-engineering | 550 | Core concept |
| entities/andrej-karpathy | 546 | Major thought leader |

**duplicate content alert**: `dspy-rlm` (698 lines) and `rlm-recursive-language-models` (698 lines) appear to be copies of each other. Recommend merging.

## 6. Stale Pages (>90 Days Since Update)

**59 pages** stale (new this week — pages that haven't been updated since the bulk import in April).

### Top 20 Most Stale
- concepts/caid-coordination — 92d ago
- concepts/reasoning-model-cost-transparency — 92d ago
- 57 entity pages from bulk import (Apr 10) — 91d ago
  - entities/abacaj, adam-mastroianni, agibot-10000-units, amazon-rivr, andriy-burkov, arlan-r, berthub-eu, brute-cat-com, chad-nauseam-home, chipro, daniel-de-laney, daniel-han, derek-thompson, dorialexander, doug-turnbull, ed-zitron, etc.

**31% of entity pages (~260) are approaching 90 days** — expect this list to grow significantly next week. Consider scheduling a bulk entity refresh run.

## 7. Person × Concept Graph Analysis

**187 persons** and **1,781 concepts** analyzed in the bipartite graph.

### Hub Persons (Most Connected)

| Person | Concepts | Persons | Core Ideas | Total |
|--------|----------|---------|------------|-------|
| **simon-willison** | 46 | 5 | 19 | 51 |
| **andrej-karpathy** | 25 | 1 | 17 | 26 |
| **armin-ronacher** | 24 | 2 | 6 | 26 |
| **peter-steinberger** | 18 | 4 | 7 | 22 |
| **doug-turnbull** | 20 | 1 | 13 | 21 |

### Bridge Concepts (Most Persons Connected)

| Concept | Persons | Key Contributors |
|---------|---------|------------------|
| **_index** | 16 | Karpathy, antirez, simon-willison, etc. |
| **harness-engineering** | 15 | addy-osmani, boris-cherny, drmaciver, etc. |
| **agentic-engineering** | 14 | Karpathy, simon-willison, anildash, etc. |
| **vibe-coding** | 8 | Karpathy, addy-osmani, peter-steinberger |
| **context-engineering** | 8 | addy-osmani, drew-breunig, etc. |

### Cross-Reference Gap Recommendations

**Person links to add** (high similarity, no direct link yet):

| Person 1 | Person 2 | Score | Shared Concepts |
|----------|----------|-------|-----------------|
| antirez-com | simon-willison | 7.5 | _index, agentic-engineering |
| drew-breunig | simon-willison | 7.5 | context-engineering, prompt-debt |
| addy-osmani | mitchell-hashimoto | 6.9 | agent-harness, karpathy |
| andrej-karpathy | antirez-com | 6.9 | _index, agentic-engineering |
| andrej-karpathy | lilian-weng | 6.9 | genai-handbook, learning-llms-in-2025 |
| fred-schott | mitchell-hashimoto | 6.9 | agent-harness, why-harness-development-boom |

**Concept cluster missing link**: `_index` ↔ `agentic-engineering` (score 6.0, shared by 3 persons Karpathy/antirez/simon-willison)

## 8. Tag Violations

**0 pages** use non-canonical tags. ✅ Perfect compliance.

## 9. Raw Article Backlog

**4,734 unprocessed raw articles** remain (out of 7,899 total). The `raw-backlog-ingest` cron processes ~30 articles/day via hermes-llm-serial-gate. At current rate: ~158 days to clear.

## 10. Recommended Actions

| Priority | Action | Details |
|----------|--------|---------|
| **HIGH** | Remove 541 stale index entries | Files referenced in index.md no longer exist |
| **HIGH** | Create stub pages for top-5 missing targets | Solving `context-engineering` alone fixes 128 broken links |
| **HIGH** | Merge duplicate entity pairs | 6 entity↔entity + 3 concept↔concept pairs |
| **MEDIUM** | Add inbound links to 38 orphan pages | 281-line automation-series is the highest-value target |
| **MEDIUM** | Fix 224 auto-fixable wikilinks | cross-namespace and bare→namespaced |
| **MEDIUM** | Investigate 59 stale pages | Bulk import entities from April need refresh |
| **MEDIUM** | Add missing person↔concept cross-refs | 15 gap recommendations from graph analysis |
| **LOW** | Split top-10 oversized pages | agentic-search (1,191 lines) is the biggest |
| **LOW** | Investigate dspy-rlm ↔ rlm-recursive-language-models | Appears to be duplicate content (both 698 lines) |

---

*Generated by `scripts/wiki_graph_analysis_weekly.py` + `scripts/wiki_graph.py`*
