# Survey Taxonomy Ingestion Pattern

When the user provides a URL to a comprehensive survey paper/project page that proposes a novel **taxonomy or classification framework** (e.g., ETCLOVG, agent harness layers), the ingestion requires a layered strategy:

## Decision Tree

1. **Does the taxonomy itself warrant a standalone concept page?**
   - YES if: the taxonomy is a novel contribution, has a memorable acronym, and serves as a navigation/organization primitive for other pages
   - NO if: it's a minor reclassification of known concepts → just enrich the existing umbrella page

2. **Does the existing wiki already have an umbrella page covering the domain?**
   - Check `wiki/concepts/` and `wiki/comparisons/` for related pages
   - If an umbrella page exists (e.g., `concepts/harness-engineering.md`), enrich it with a taxonomy reference section rather than creating a competing page
   - The taxonomy page and the umbrella page should cross-reference each other

## Page Structure for Taxonomy Concept Pages

```markdown
# [Acronym] Taxonomy

## Overview — acronym expansion, what it classifies, who proposed it

## Layer Details — one subsection per layer, with primary concern per layer

## Project Mapping — if the survey includes coded data (table format)

## Cross-Layer Synthesis — system-level dynamics that span multiple layers

## Engineering Phases — if the survey proposes a historical progression

## Open Problems — forward-looking research questions

## Relationship to Other Frameworks — distinguish from existing wiki pages
```

## Cross-Referencing Strategy

When the taxonomy touches an existing umbrella page in the wiki:

1. **Create the taxonomy page** with full detail
2. **Enrich the umbrella page** with a taxonomy summary section + `[[wikilink]]` to the taxonomy page
3. **Update comparison pages** that would benefit from the taxonomy as a source/reference
4. **Add `[[concepts/etclovg-taxonomy]]` (or equivalent) to related frontmatter** of all touched pages

## Example: ETCLOVG Ingestion

- **Survey**: "Agent Harness Engineering: A Survey" by Li et al. (2026)
- **Taxonomy**: ETCLOVG (Execution, Tooling, Context, Lifecycle, Observability, Verification, Governance)
- **Existing umbrella**: `concepts/harness-engineering.md` (392 lines, eval-centric focus)
- **Decision**: Create standalone `concepts/etclovg-taxonomy.md` + enrich umbrella page with taxonomy section
- **Cross-refs**: Updated `comparisons/agent-harnesses.md`, `comparisons/open-harness-vs-agent-framework.md` context

## Pitfalls

- **Don't replace the umbrella page.** The taxonomy is a lens, not a replacement. The umbrella page has accumulated knowledge (case studies, industry patterns) that the survey taxonomy doesn't cover.
- **Don't create a content-free stub.** If the survey page only mentions the taxonomy name without layer details, enrich the umbrella page instead of creating a thin standalone page.
- **Check for companion repos.** Survey pages often have companion GitHub repos (Awesome-Agent-Harness, datasets on HuggingFace). Include these as sources and mention the repo stats (stars, entry count).
