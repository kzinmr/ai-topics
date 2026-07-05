---
title: Weekly Wiki Graph Analysis
created: 2026-07-05
updated: 2026-07-05
type: query
tags: [wiki-maintenance, graph-analysis]
sources: []
---

# Weekly Wiki Graph Analysis

**Date**: 2026-07-05 17:42 UTC

## Summary

| Metric | Value |
|--------|-------|
| Total pages scanned | 2205 |
| Entities | 839 |
| Concepts | 1316 |
| Comparisons | 33 |
| Queries | 4 |
| Events | 13 |
| Orphans (no inbound links) | 43 |
| Content-rich orphans | 43 |
| Broken wikilinks | 4890 |
| Fixable wikilinks | 997 |
| Duplicate groups | 39 |
| Oversized pages (>200 lines) | 198 |
| Missing sources | 684 (31%) |
| Tag violations | 0 |
| Stale pages (>90 days) | 0 |
| Skeleton pages | 0 |
| Not indexed in index.md | 1994 |
| Stale index entries | 20 |

## 1. Orphan Pages

43 pages have zero inbound links from other wiki pages.

### Content-Rich Orphans (top 15)

- **concepts/automation-series** — 281 lines, 0 outbound links
- **concepts/qlora** — 234 lines, 0 outbound links
- **comparisons/codex-app-server-vs-agent-protocols** — 209 lines, 0 outbound links
- **comparisons/harness-backend-routing** — 185 lines, 0 outbound links
- **concepts/glut-of-circuits** — 160 lines, 0 outbound links
- **entities/antoine-buteau** — 149 lines, 0 outbound links
- **concepts/cloudflare-email-sending** — 131 lines, 0 outbound links
- **concepts/good-regulator-theorem** — 125 lines, 0 outbound links
- **concepts/hermes-codex-app-server-runtime** — 125 lines, 0 outbound links
- **comparisons/google-alerts-alternatives-2026** — 119 lines, 0 outbound links
- **entities/luke-curley** — 116 lines, 0 outbound links
- **concepts/slow-search** — 108 lines, 0 outbound links
- **concepts/altman-three-observations** — 101 lines, 0 outbound links
- **concepts/nvidia-egpu-macos** — 96 lines, 0 outbound links
- **concepts/megakernel-inference** — 85 lines, 0 outbound links

### All Orphans by Category
- content-rich: 43

## 2. Broken Wikilinks

4890 total broken links.

| Issue Type | Count | Description |
|------------|-------|-------------|
| bare-wikilink-missing | 2684 | Bare name, target page does not exist |
| missing | 1209 | Namespaced link to a page that does not exist |
| bare-wikilink | 931 | Bare name without namespace prefix (auto-fixable) |
| cross-namespace | 66 | Entity ↔ concept namespace mismatch (auto-fixable) |

### Top Broken Targets (pages that need creating)

- [[[[concepts/context-engineering]]]] — 120 references
- [[[[concepts/security-and-governance/ai-safety]]]] — 67 references
- [[[[concepts/harness-engineering/agent-harness]]]] — 60 references
- [[[[concepts/coding-agents/coding-agents]]]] — 46 references
- [[[[concepts/post-training/grpo-rl-training]]]] — 34 references
- [[[[concepts/security-and-governance/agent-sandboxing]]]] — 33 references
- [[[[concepts/post-training/grpo]]]] — 31 references
- [[[[concepts/local-llm/_index]]]] — 30 references
- [[[[concepts/anthropic/managed-agents]]]] — 30 references
- [[[[concepts/post-training/rlhf]]]] — 30 references
- [[[[concepts/security-and-governance/agent-governance]]]] — 29 references
- [[[[concepts/evaluation/ai-evals]]]] — 26 references
- [[[[concepts/claude/mythos]]]] — 23 references
- [[[[concepts/claude-code/claude-code]]]] — 23 references
- [[[[concepts/claude/fable-5]]]] — 21 references

### Fixable Links (sample)

997 links can be auto-fixed (cross-namespace or bare → namespaced).

- `entities/_index`: [[entities/abacaj]] → [[entities/abacaj]]
- `entities/_index`: [[entities/adam-mastroianni]] → [[entities/adam-mastroianni]]
- `entities/_index`: [[entities/addy-osmani]] → [[entities/addy-osmani]]
- `entities/_index`: [[entities/agentcraft]] → [[entities/agentcraft]]
- `entities/_index`: [[entities/agibot-10000-units]] → [[entities/agibot-10000-units]]
- `entities/_index`: [[entities/akira-realmcore]] → [[entities/akira-realmcore]]
- `entities/_index`: [[entities/alec-radford]] → [[entities/alec-radford]]
- `entities/_index`: [[entities/alex-banks]] → [[entities/alex-banks]]
- `entities/_index`: [[entities/ali-farhadi]] → [[entities/ali-farhadi]]
- `entities/_index`: [[entities/amazon-rivr]] → [[entities/amazon-rivr]]
- ... and 987 more

## 3. Duplicate / Similar Pages

39 potential duplicate groups detected by normalized name matching.

- `index`: entities/_index, concepts/_index
- `agentmemory`: entities/agentmemory, concepts/agent-memory
- `agno`: entities/agno, concepts/agno
- `antoinechaffin`: entities/antoine-chaffin, concepts/antoine-chaffin
- `apertus`: entities/apertus, concepts/apertus
- `autoreason`: entities/autoreason, concepts/autoreason
- `companyaipilled`: entities/company-ai-pilled, concepts/company-ai-pilled
- `contentengine`: entities/content-engine, concepts/content-engine
- `datasetteagent`: entities/datasette-agent, concepts/datasette-agent
- `deliberatecoder`: entities/deliberate-coder, entities/deliberatecoder
- `dspy`: entities/dspy, concepts/dspy
- `eliezeryudkowsky`: entities/eliezer-yudkowsky, concepts/eliezer-yudkowsky
- `embeddings`: entities/embeddings, concepts/embeddings
- `eugeneyan`: entities/eugene-yan, entities/eugeneyan
- `gilesthomas`: entities/giles-thomas, entities/gilesthomas
- `hermesagent`: entities/hermes-agent, concepts/hermes-agent
- `lilianweng`: entities/lilian-weng, entities/lilianweng
- `macstudiolocalai`: entities/mac-studio-local-ai, concepts/mac-studio-local-ai
- `maithinking1`: entities/mai-thinking-1, concepts/mai-thinking-1
- `martinfowler`: entities/martin-fowler, entities/martinfowler
- `nvidiasanawm`: entities/nvidia-sana-wm, concepts/nvidia-sana-wm
- `openclaw`: entities/openclaw, concepts/openclaw
- `openenv`: entities/openenv, concepts/openenv
- `projectglasswing`: entities/project-glasswing, concepts/project-glasswing
- `ramp`: entities/ramp, concepts/ramp

## 4. Index Reconciliation

- **1994 pages** are on disk but not listed in index.md
- **20 index entries** reference files that no longer exist

### Not-Indexed by Category

- concepts: 1206
- entities: 773
- events: 11
- queries: 4

## 5. Oversized Pages (>200 lines)

198 pages exceed the 200-line threshold.

- **concepts/agentic-search** — 1191 lines
- **entities/anthropic** — 702 lines
- **concepts/dspy-rlm** — 698 lines
- **concepts/rlm-recursive-language-models** — 698 lines
- **entities/ed-zitron** — 603 lines
- **concepts/ai-native-state-management** — 562 lines
- **entities/andrej-karpathy** — 545 lines
- **concepts/_index** — 517 lines
- **entities/simon-willison** — 516 lines
- **concepts/harness-engineering** — 506 lines
- ... and 188 more

## 6. Stale Pages (>90 days since update)

0 pages have not been updated in over 90 days.

## 7. Tag Violations

0 pages use non-canonical tags.

## 8. Recommended Actions

- [HIGH] Add 1994 pages to index.md (batch orphan reg script needed)
- [MEDIUM] Fix 997 cross-namespace / bare wikilinks
- [MEDIUM] Add inbound links to 43 content-rich orphan pages
- [HIGH] Review and consolidate 39 potential duplicate groups
- [LOW] Consider splitting 198 oversized pages (>200 lines)
- [MEDIUM] Remove 20 stale index entries (files missing)
- [HIGH] 684 pages (31%) missing sources field - set to []

---
*Generated by `scripts/wiki_graph_analysis_weekly.py`*
