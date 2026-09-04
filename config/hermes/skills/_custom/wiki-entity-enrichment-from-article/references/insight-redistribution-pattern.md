# Insight Redistribution When Ingesting Comprehensive Documents

## Problem

When a user provides a comprehensive document (Q&A thread, lecture notes, multi-topic analysis) covering several related concepts, the naive approach is to create one new concept page with all content. This leads to:
- Duplication with existing pages that already cover sub-topics
- A bloated new page that overlaps with the existing knowledge graph
- Missed opportunities to enrich existing pages with fresh perspectives

## The Pattern

### Step 1: Map Each Insight to Its Natural Home

Before writing anything, identify each distinct insight in the source document and determine where it naturally belongs:

| Insight | Natural Home | Rationale |
|---------|-------------|-----------|
| Unique framing/synthesis not in wiki | **New concept page** | This is the page's raison d'etre |
| Detailed technical content matching existing page's scope | **Existing page** (enrich) | Strengthens existing coverage |
| Perspective that bridges two existing pages | **New page** (overview) + cross-refs | Provides connective tissue |
| Concrete examples/tables for existing concepts | **Existing page** (append) | More discoverable where people look |

### Step 2: Create the New Page for Unique Synthesis Only

The new concept page should contain:
- The overarching framing that connects multiple concepts
- Novel structural insights (e.g., "DPO and GRPO converge on the same pattern")
- Open questions that emerge from the synthesis
- Cross-references to existing pages for detailed sub-topics

### Step 3: Enrich Existing Pages with Distributed Insights

For each insight that belongs on an existing page:
1. Read the existing page to find the right insertion point
2. Add the insight as a new subsection or enrichment to an existing section
3. Add a backlink to the new synthesis page

### Step 4: Compress the New Page's Duplicated Sections

If the new page initially contains detailed content that duplicates existing pages:
- Replace detailed sections with brief summaries (1-2 sentences + table)
- Add cross-references with section anchors: `[[concepts/foo#Section Name|display text]]`
- Keep only the unique synthesis angle, not the full technical walkthrough

### Step 5: Verify Cross-Reference Graph

After redistribution:
- New page → links to all existing pages it references
- Each enriched existing page → backlinks to new page
- No orphan references (every `[[wikilink]]` has a matching backlink)

## Example: LLM-as-Policy Ingestion (2026-06-15)

Source: Comprehensive Q&A covering LLM-as-Policy, RM vs Critic, SFT as behavior cloning, DPO/GRPO convergence.

**Distribution decisions:**
| Insight | Destination | Action |
|---------|------------|--------|
| Core formulation (state/action/policy mapping) | `llm-as-policy.md` (new) | Created as defining content |
| DPO/GRPO implicit modeling convergence | `llm-as-policy.md` (new) | Created as unique novel insight |
| RM vs Critic comparison + credit assignment example | `rl-algorithms-for-llm-training.md` | Added new subsection after Actor-Critic |
| Traditional RL vs LLM-RL distinction (3 factors) | `on-policy-vs-off-policy-rl.md` | Added new subsection before "2026 Landscape" |
| SFT as behavior cloning (detailed) | `on-policy-vs-off-policy-rl.md` | Already covered; compressed in new page to cross-ref |
| Inference-time scaling as exploration | Both pages | Different angles in each; kept both |

**Result:** New page went from ~190 lines (bloated) to ~170 lines (focused). Existing pages gained 15-25 lines each of targeted enrichment.

## Pitfalls

- **Don't create a "summary page" that just links to everything**: The new page must have unique intellectual content, not just a table of contents
- **Compress ruthlessly**: If a section in the new page reads like a copy of an existing page, replace it with a cross-ref
- **Check pre-commit hooks**: If redistributing content to existing pages, verify that the additions pass the same validation (no CJK in non-raw, tag validation, etc.)
- **Preserve the source**: Always save the raw document to `wiki/raw/articles/` first, even if insights get distributed across multiple pages
