---
title: Weekly Wiki Graph Analysis
created: 2026-06-19
updated: 2026-06-19
type: query
tags: [wiki-maintenance, graph-analysis]
sources: []
---

# Weekly Wiki Graph Analysis

**Date**: 2026-06-19 15:22 UTC
**Wiki root**: `/opt/data/ai-topics/wiki/`

## Summary

| Metric | Count |
|--------|-------|
| Total pages scanned | 2,105 |
| Entities | 812 |
| Concepts | 1,247 |
| Comparisons | 31 |
| Events | 11 |
| Queries | 4 |

## 1. Frontmatter Health

| Field | Missing | Rate |
|-------|---------|------|
| Missing frontmatter entirely | 5 | 0.2% |
| Missing `sources` field | 674 | 32.0% |
| Missing `type` | 34 | - |
| Missing `created` | 28 | - |
| Missing `updated` | 13 | - |
| Status skeleton | 0 | 0% |

**Action**: 674 pages (~32%) lack a `sources` field. These should get `sources: []` if truly source-less. ~5 pages have no frontmatter at all.

## 2. Orphan Pages (no inbound links)

**Total orphans**: 36 (all content-rich)

Top orphans by size (need cross-referencing):

| Page | Lines | Outbound Links |
|------|-------|----------------|
| `concepts/automation-series` | 281 | 0 |
| `concepts/qlora` | 234 | 0 |
| `comparisons/codex-app-server-vs-agent-protocols` | 209 | 0 |
| `comparisons/harness-backend-routing` | 185 | 0 |
| `concepts/glut-of-circuits` | 160 | 0 |
| `entities/antoine-buteau` | 149 | 0 |
| `concepts/cloudflare-email-sending` | 131 | 0 |
| `concepts/good-regulator-theorem` | 125 | 0 |
| `concepts/hermes-codex-app-server-runtime` | 125 | 0 |
| `comparisons/google-alerts-alternatives-2026` | 119 | 0 |

**Action**: These 36 pages have substantial content but zero inbound links. Some (like `automation-series`, `qlora`) are high-value topics that should be linked from related concept pages. Each has 0 outbound links suggesting they were created independently and never integrated.

## 3. Broken Wikilinks

**Total broken links**: 4,597

| Category | Count |
|----------|-------|
| Bare wikilink (target missing) | 2,523 |
| Missing (namespaced target not found) | 1,141 |
| Bare wikilink (fixable - page exists) | 871 |
| Cross-namespace (fixable) | 62 |

**Fixable**: 933 links can be auto-repaired (bare wikilinks → namespaced, cross-namespace)

The 871 **bare wikilinks** are almost entirely in `entities/_index.md` where entity names are linked without namespace prefix (e.g. `[[abacaj]]` should be `[[entities/abacaj]]`).

**Top missing page targets** (pages that are frequently linked but don't exist):

| Missing Target | References |
|----------------|-----------|
| `concepts/context-engineering` | 113 |
| `concepts/security-and-governance/ai-safety` | 65 |
| `concepts/harness-engineering/agent-harness` | 55 |
| `concepts/coding-agents/coding-agents` | 43 |
| `concepts/post-training/grpo-rl-training` | 34 |
| `concepts/anthropic/managed-agents` | 30 |
| `concepts/post-training/rlhf` | 30 |
| `concepts/security-and-governance/agent-sandboxing` | 30 |
| `concepts/local-llm/_index` | 29 |
| `concepts/post-training/grpo` | 29 |
| `concepts/security-and-governance/agent-governance` | 27 |
| `concepts/evaluation/ai-evals` | 26 |
| `concepts/claude-code/claude-code` | 22 |
| `concepts/multi-agents/agent-team-swarm` | 19 |
| `concepts/evaluation/llm-as-judge` | 18 |

**Observation**: These missing targets represent a **planned but unrealized subdirectory structure**. The wiki often references pages as if they exist under hierarchy (e.g. `security-and-governance/ai-safety`, `post-training/grpo`) but these pages were either never created or renamed after the references were written.

**Action**: Create the most-referenced missing pages from existing content, or fix the links to point to the actual page locations.

## 4. Duplicate / Similar Pages

**32 potential duplicate groups found** (normalized name collisions):

### Entity ↔ Entity duplicates (4)
| Normalized | Pages |
|------------|-------|
| `deliberatecoder` | `entities/deliberate-coder`, `entities/deliberatecoder` |
| `eugeneyan` | `entities/eugene-yan`, `entities/eugeneyan` |
| `lilianweng` | `entities/lilian-weng`, `entities/lilianweng` |
| `samuelcolvin` | `entities/samuel-colvin`, `entities/samuelcolvin` |

### Entity ↔ Concept duplicates (28)
Examples: `agentmemory`/`agent-memory`, `dspy`, `embeddings`, `autoreason`, `hermesagent`/`hermes-agent`, `ramp`, `openclaw`, `openenv`, etc.

**Note**: Many entity↔concept pairs may be intentional (Concept = the idea/product itself, Entity = the company/organization behind it). Each needs human review.

**Action**: The 4 entity↔entity pairs are actual duplicates and should be consolidated.

## 5. Index Reconciliation

| Gaps | Count |
|------|-------|
| Pages on disk but not in `index.md` | 472 |
| Index entries referencing deleted/moved pages | 394 |

**Not-indexed breakdown**: 462 concepts, 9 entities, 1 query

**Action**: Add 472 pages to index.md (batch orphan registration script). Remove 394 stale index entries.

## 6. Oversized Pages (>200 lines)

**185 pages exceed 200 lines** — candidates for splitting:

Top 20:
| Page | Lines |
|------|-------|
| `concepts/agentic-search` | 1,191 |
| `entities/anthropic` | 702 |
| `concepts/dspy-rlm` | 698 |
| `concepts/rlm-recursive-language-models` | 696 |
| `concepts/ai-native-state-management` | 562 |
| `entities/andrej-karpathy` | 545 |
| `concepts/_index` (MOC) | 521 |
| `concepts/harness-engineering` | 506 |
| `entities/jason-liu` | 492 |
| `entities/ed-zitron` | 485 |
| `concepts/ai-bubble-economics` | 484 |
| `entities/simon-willison` | 482 |
| `concepts/query-understanding` | 474 |
| `entities/substack` | 472 |
| `entities/paulgraham-com` | 467 |
| `concepts/programmatic-tool-calling` | 435 |
| `concepts/model-quantization` | 430 |
| `comparisons/agent-harnesses` | 413 |
| `entities/openai` | 408 |
| `concepts/scaling-hypothesis` | 408 |

**Action**: Priority split candidates: `concepts/agentic-search` (1,191 lines), `entities/anthropic` (702), `concepts/dspy-rlm` (698). Consider subdirectory MOC pages for the most bloated ones.

## 7. Tag Violations (non-canonical tags)

**7 pages with invalid tags** — low, each is likely an oversight:

| Tag | Pages |
|-----|-------|
| `google-deepmind` | 1 |
| `epoch` | 1 |
| `incidents` | 1 |
| `linux` | 1 |
| `risk-management` | 1 |
| `autonomous-systems` | 1 |
| `exponential` | 1 |
| `customer-experience` | 1 |
| `agent-builder` | 1 |
| `no-code` | 1 |
| `authentication` | 1 |
| `workos` | 1 |
| `wiki-maintenance` | 1 (this page) |
| `graph-analysis` | 1 (this page) |

**Action**: Remove or correct these 12 non-canonical tags. If any are genuinely useful new categories, add them to SCHEMA.md first.

## 8. Stale Pages

**0 pages stale >90 days** — either all pages were updated recently, or the `updated` field is missing on many pages (13 missing).

## Recommended Actions (Priority Order)

### HIGH
1. **Fix 7 pages with non-canonical tags** — pre-commit will block these. Remove invalid tags or add them to SCHEMA.md if legitimate.
2. **Add `sources: []` to 674 pages** that are missing the sources field (32% coverage gap).
3. **Add 472 pages to index.md** — run batch orphan registration script.
4. **Review 32 duplicate groups** — consolidate 4 entity↔entity pairs; assess 28 entity↔concept pairs.

### MEDIUM
5. **Fix 933 cross-namespace / bare wikilinks** — most are in `entities/_index.md` referencing entity pages without namespace.
6. **Add inbound links to 36 content-rich orphan pages** — these have substantial content but no incoming links.
7. **Remove 394 stale index entries** referencing pages that no longer exist on disk.

### LOW
8. **Create the top 15 missing target pages** — `context-engineering` (113 refs), `ai-safety` (65 refs), `agent-harness` (55 refs), etc.
9. **Consider splitting 185 oversized pages** — start with `concepts/agentic-search` (1,191 lines).
