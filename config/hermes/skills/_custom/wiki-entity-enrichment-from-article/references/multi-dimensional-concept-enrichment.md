# Multi-Dimensional Concept Enrichment

Enriching an existing concept page with a **complementary dimension** that the page's original sources did not cover.

## When to Use

The existing concept page is well-structured but covers only dimension A (e.g., pretraining-scale data). A new article covers dimension B (e.g., RLHF/alignment/CAI with synthetic data). Both dimensions are valid and complementary — neither replaces the other.

**Not to be confused with:**

| Pattern | Relation to Existing Page | Action |
|---------|--------------------------|--------|
| **Multi-dimensional** (this) | New dimension entirely absent | Add parallel H2 sections |
| Production case study | Adds implementation example within existing framework | Add H3 under relevant H2 |
| Multi-paper expansion (levels) | Contrasting perspectives on the SAME dimension | Add Level 2, Level 3 H2 |
| Single-experiment multi-page | Distributes one experiment across pages | Patch multiple pages at different granularities |

## Detection Signals

- Article leads with keywords the existing concept page doesn't have (e.g., "Constitutional AI", "Superalignment" on a page about "synthetic data for pretraining")
- The existing concept page has a **noticeable absence** of a major sub-topic (e.g., instruction/preference/critique hierarchy, open-source library examples)
- The existing concept page's `aliases` and `tags` are a strict subset of what the new article would introduce
- The concept page already existed under a different focus, was written for a different source (e.g., arXiv paper → pretraining), and the new article (e.g., Substack guide → RLHF/alignment) targets the same umbrella topic from a separate angle

## Workflow

### 1. Read Full Existing Page
Understand its current structure, dimensions covered, and planned future expansion. Note which sections exist and which don't.

### 2. Identify Complementary Dimensions
From the new article, list the major thematic sections that don't appear in the existing page.
e.g., for `synthetic-data.md`: Strategic Roles (closed vs open), CAI framework, Hierarchy of Data Types, Practical Tips, Open-Source Examples, Superalignment

### 3. Plan Insertion Point
Multi-dimensional sections go at the **same H2 level** as existing sections, not nested under them. Insert before or after the existing structural sections:
- Before: e.g., "Pre-training Best Practices" (existing) — these are downstream concerns, so background sections come first
- After: if the new dimension is independent philosophy/conceptual framework

The rule: **keep the existing structure intact.** Don't merge the new dimension into existing sections — the new sections are peers, not children.

### 4. Update Frontmatter
- Add new `aliases` (e.g., `constitutional-ai`, `rlaif`, `superalignment-synthetic-feedback`)
- Add new `tags` (e.g., `alignment`, `sft`, `rlhf`)
- Add `related:` links to any other concept pages the new dimension introduces (e.g., `dataset-engineering`)
- Add new raw article to `sources:`
- Bump `updated` date

### 5. Add Sections at Identified Insertion Point
Use `patch` with enough surrounding context for uniqueness. Each section is a full H2 with subsections as needed.

### 6. Update Related Concepts and Sources Bottom Sections
- Add cross-references for all new dimensions
- Add new sources alongside existing ones (not replacing)

### 7. Update index.md Description
Widen the one-line description to cover both dimensions:
- Before: "Synthetic data for LLM pre-training: techniques from simple rephrasing..."
- After: "AI-generated training data for LLMs: covers Constitutional AI (CAI/RLAIF), instruction/preference/critique hierarchy, pre-training scaling..."

## Example from Session

**Existing page:** `concepts/synthetic-data.md` — covered pretraining-scale data augmentation (Megadocs, rephrasing, agentic data creation, distributional shift paradox). Based on a single arXiv paper.

**New article:** Nathan Lambert, "Synthetic data: Anthropic's CAI, scaling, OpenAI's Superalignment..." (Interconnects, Nov 2023) — covered six entirely different dimensions: closed vs open model strategy, CAI/RLAIF pipeline, synthetic data types hierarchy (instructions → preferences → critiques), practical tips, open-source examples, and Superalignment.

**Approach:** Added all six as parallel H2 sections between "Agentic Data Creation" and "Pre-training Best Practices." Existing pretraining content untouched. Frontmatter aliases/tags/sources/related updated to reflect both dimensions. index.md description widened.

## Pitfalls

- **Don't try to merge** the new dimension into an existing section. If there's no "CAI" section, create one — don't force CAI under "Key Approaches"
- **Don't rewrite** the existing page's structure. The original framework may be the right framework for its dimension
- **Frontmatter aliases vs tags:** Add conceptual aliases (e.g., `constitutional-ai`, `rlaif`) so graph queries find the page from new directions. Add functional tags (e.g., `alignment`, `sft`, `rlhf`) for filtering.
- **Index description update is required** in multi-dimensional enrichment because the page's scope has fundamentally widened — unlike incremental expansions where the description may not need to change
- **Related Concepts may need expansion** to include pages that exist in the new dimension but weren't relevant to the old dimension (e.g., adding `dataset-engineering` to `synthetic-data`'s related list)
