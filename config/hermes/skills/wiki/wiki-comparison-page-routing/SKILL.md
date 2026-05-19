---
name: wiki-comparison-page-routing
description: >-
  When creating or ingesting wiki pages that compare 3+ items (tools, models, frameworks, platforms, etc.),
  route them to wiki/comparisons/ — NOT wiki/concepts/. This prevents multi-item comparison pages
  from accumulating in the concepts/ directory where they're hard to find and require cleanup.
trigger: >-
  When creating ANY new wiki page, or when ingesting articles/newsletters/X posts/blog content
  that compare 3+ items (not just "A vs B").
---

# Wiki Comparison Page Routing

## Purpose

Multi-item comparison pages (3+ items) MUST be placed in `wiki/comparisons/`, never in `wiki/concepts/`. This skill defines the routing rule and provides a decision tree for all wiki page creation workflows.

## Core Rule

| Comparison Type | Destination | Example |
|----------------|-------------|---------|
| **3+ items** (tools, frameworks, models, platforms, etc.) | `wiki/comparisons/` | 9 harnesses, 4 eval tools, 5 local LLM models |
| **Head-to-head** (2 items, "A vs B") | `wiki/comparisons/` | Hermes vs OpenClaw, A Philosophy of Software Design vs Clean Code |
| **Single concept** (analysis, architecture, technique) | `wiki/concepts/` | Harness Engineering, GRPO, Agent Sandboxing |

### Why the distinction matters

Multi-item comparison pages have a fundamentally different structure from concept pages:
- **Comparison pages**: tables, matrices, axes, scoring rubrics, decision frameworks
- **Concept pages**: explanatory prose, architecture diagrams, deep dives, intellectual genealogy

Putting comparison pages in `concepts/` creates:
1. **Discovery failure** — users browsing `concepts/` don't expect comparison tables
2. **Hybrid structure confusion** — concepts trying to be comparisons end up shallow on both
3. **Cleanup debt** — every comparison-in-concepts is a future `moved_from` entry (we've accumulated 6+ already)

## Decision Tree

When creating/ingesting a new wiki page, ask:

```
Is the page about a single concept/technique/architecture?
  YES → wiki/concepts/ ✓
  NO  → Does it compare 2 items?
           YES → wiki/comparisons/ ✓
           NO  → Does it compare 3+ items?
                    YES → wiki/comparisons/ ✓
                    NO  → Is it about a person/org/tool?
                             YES → wiki/entities/ ✓
                             NO  → Reconsider: should this page exist?
```

## When This Skill Should Fire

Load this skill in any workflow that creates wiki pages:

1. **`wiki-concept-from-research`** — before Step 4 (writing phase), check: "Is this comparing 3+ items?"
2. **`wiki-ingestion-pipelines`** — all ingestion sections (newsletter, blog, X bookmarks, X accounts scan, active crawl, dreaming)
3. **`documentation-page-ingestion`** — when ingesting comparison-style docs
4. **`wiki-entity-enrichment-from-article`** — when the article is a survey/comparison roundup

## Concrete Examples

### ✅ Correct routing
| Page | Type | Destination | Why |
|------|------|-------------|-----|
| `comparisons/agent-harnesses.md` | 9 harness comparison | `comparisons/` | 9 items, multi-dimension matrix |
| `comparisons/eval-tools-comparison.md` | 4 eval tools | `comparisons/` | 4 tools, selection framework |
| `comparisons/hermes-vs-openclaw-architecture.md` | 2 architecture comparison | `comparisons/` | Head-to-head |
| `comparisons/frontier-models-2026-04.md` | Model comparison | `comparisons/` | Multiple models |
| `comparisons/local-llm-models-april-2026.md` | Local model comparison | `comparisons/` | Multiple local models |
| `comparisons/open-source-rl-libraries-comparison.md` | RL libraries | `comparisons/` | 5+ libraries |
| `concepts/harness-engineering.md` | Single concept | `concepts/` | Explanatory, not comparative |
| `concepts/agent-sandboxing.md` | Single concept | `concepts/` | Technology spectrum |
| `concepts/grpo.md` | Single algorithm | `concepts/` | Single technique |
| `entities/claude-code.md` | Product entity | `entities/` | Person/org/tool |

### ❌ Wrong routing (historically corrected)
| Page | Where it was | Where it belongs | Fixed |
|------|-------------|-----------------|-------|
| `ai-eval-tools-comparison.md` | `concepts/` | `comparisons/` | 2026-05-11 |
| `eval-tools-comparison.md` | `concepts/` | `comparisons/` | 2026-05-11 |
| `openclaw-vs-hermes-architecture-comparison.md` | `concepts/` | `comparisons/` | 2026-05-11 |
| `hermes-agent-vs-openclaw-architecture-comparison.md` | `concepts/` | `comparisons/` | 2026-05-11 |
| `agent-harness-comparison.md` | `concepts/` | `comparisons/` | 2026-05-11 |
| `coding-agent-harnesses.md` (redirect) | `comparisons/` → merged | `comparisons/agent-harnesses.md` | 2026-05-11 |

## Frontmatter Convention

Comparison pages use `type: comparison` and may include `moved_from:` if consolidated from concepts/:

```yaml
type: comparison
tags: [comparison, {topic-domain}, ...]
moved_from:
  - concepts/old-page-name.md
```

## Edge Cases

### 2-items that grow
A head-to-head comparison ("A vs B") may later expand to include C, D, E. That's fine — it stays in `comparisons/`. The rule is about the page's nature (comparative), not a fixed item count.

### Comparison as a section within a concept page
A concept page MAY contain a comparison TABLE as a subsection (e.g., `concepts/agent-sandboxing.md` has an "Isolation Technology Spectrum" table). This is acceptable because the page's primary purpose is to explain a concept, not to be a comparison portal. The table supports the explanation.

**Litmus test**: If you removed all comparison tables from the page, would it still be a coherent concept page? YES → `concepts/` is fine. NO (the page IS the comparison) → must go to `comparisons/`.

### Newsletter/blog articles that ARE comparisons
When ingesting a survey/comparison article (e.g., "9 AI Agent Harnesses Compared"), create the page in `comparisons/` even if the source is a typical concept-creation pipeline. The page type follows the CONTENT, not the pipeline origin.

## Integration with Existing Skills

### `wiki-concept-from-research`

After Step 3 (differentiation check), add a routing check before Step 4:

> **Comparison check**: Is this page comparing 3+ items (tools, models, frameworks)?
> - YES → Create at `wiki/comparisons/<name>.md` with `type: comparison`
> - NO → Continue to Step 4, create at `wiki/concepts/<name>.md`

### `wiki-ingestion-pipelines`

In every ingestion section (newsletter, blog, X bookmarks, X accounts scan, active crawl, dreaming), add:

> **Before creating a concept page**: Check if the article is a comparison/survey of 3+ items.
> If yes → route to `wiki/comparisons/`, not `wiki/concepts/`.

## Pitfalls

- **Don't move single-concept pages to comparisons/** — pages like `agent-sandboxing.md` (technology spectrum analysis) are concepts, not comparisons
- **Don't create comparison stubs in concepts/ "for later"** — they accumulate and require cleanup. Create in `comparisons/` from the start
- **Head-to-heads ARE comparisons** — "A vs B" belongs in `comparisons/`, not `entities/` or `concepts/`
- **Comparison portals ≠ entity pages** — individual tool pages go to `entities/`; the comparison of all tools goes to `comparisons/`
