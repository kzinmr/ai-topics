# Ingest-and-Compare Pattern

When a user says "取り込んで、Xとの違いを分析して" (ingest and analyze differences with X), the task has two deliverables:

1. **Wiki deliverable**: Concept/entity page with cross-references to the comparison target
2. **Chat deliverable**: Structured comparative analysis in the response

## Workflow

1. Fetch the article (Jina Reader for web pages)
2. Check existing wiki for the comparison target — read its entity/concept page
3. Create the new concept page in **English** (wiki language policy)
4. Add cross-references in **both directions**:
   - New page → `[[wikilinks]]` to comparison target in Related Pages
   - Comparison target page → add new page to its Related section
5. Update index.md + log.md
6. Commit (check pre-commit: tags in SCHEMA.md, no CJK in non-raw pages)
7. Deliver the comparative analysis in chat (not in wiki) — use tables, strategic framing

## Analysis Structure

The chat analysis should go beyond what's in the wiki page:
- **Architectural differences**: abstraction levels, API surface, control granularity
- **Use-case differentiation**: when to use which
- **Strategic interpretation**: market positioning, competitive dynamics
- **Ecosystem context**: how both relate to third-party alternatives (E2B, Modal, etc.)

## Pitfall

Don't put the comparative analysis in the wiki page body. Wiki pages describe the entity/concept itself. Comparisons go in `comparisons/` pages or in the chat response. A concept page can have a comparison table for positioning, but the strategic analysis belongs in chat or a dedicated comparison page.
