# Cross-Cutting Concept Page Creation Pattern

When multiple sources/products/entities share a common theme, create a **cross-cutting concept page** that ties them together under a unified analysis, then update each referenced page with cross-links.

## When to Use

- 3+ entities/products converging on the same architectural pattern (e.g., multi-model synthesis)
- User explicitly asks to "tie together" or "discuss in relation to" multiple topics
- Simultaneous releases from different providers solving the same problem
- A new architectural pattern emerging across multiple implementations

## Workflow

### 1. Research Phase
- Fetch all source articles (use Jina Reader for SPAs: `curl -sL "https://r.jina.ai/URL"`)
- Read existing wiki pages for all related entities/concepts
- Identify the shared theme and each entity's distinct approach

### 2. Create Cross-Cutting Concept Page
- Save all raw articles first (mandatory per wiki policy)
- Create the concept page with:
  - **Overview** framing the shared theme and why convergence matters
  - **Per-approach sections** (each with architecture, results, source attribution)
  - **Comparative analysis table** (architecture, user control, cost strategy, best-for, benchmarks)
  - **Relationship to existing concepts** (link to related concept pages like model-routing, harness-engineering)
  - **Open questions** section for unresolved tensions
  - **Related pages** section with wikilinks to all referenced entities/concepts

### 3. Cascade Updates to Referenced Pages
Each entity/concept page that participates in the cross-cutting analysis gets:
- A new section summarizing their specific contribution (3-5 lines)
- A wikilink to the cross-cutting concept page
- Updated `sources` frontmatter with the raw article path

### 4. Update Adjacent Concept Pages
If the cross-cutting concept relates to an existing concept page (e.g., model-routing → multi-model-synthesis), update that page too:
- Add a section referencing the new pattern
- Add cross-link to the new concept page

### 5. Index and Log
- Add new concept entry to `index.md` in alphabetical order
- Add all updated entity/concept entries to `index.md` recently-updated section
- Append to `log.md`

## Pitfalls

- **Tag validation**: Check SCHEMA.md for existing canonical tags BEFORE committing. The `multi-model` → `multi-llm` substitution (June 2026) wasted a commit cycle.
- **Language policy**: All non-raw wiki content must be in English. Even brief Japanese phrases in concept pages or index.md entries are blocked by pre-commit hooks.
- **Partial-match corruption on entity updates**: When patching entity pages that have long Related sections, include enough context in `old_string` to uniquely match. Multiple similar section headers (e.g., "## Related" appearing once) can cause wrong placement.
- **Cross-referencing order**: Create the cross-cutting concept page FIRST, then update entity pages to link TO it. This avoids orphan wikilinks during the commit window.

## Example Session (June 2026)

**Trigger**: User asked to ingest Cognition Devin Fusion blog + OpenRouter Fusion blog + discuss in relation to Sakana Fugu.

**Cross-cutting page created**: `concepts/multi-model-synthesis-strategies.md`
- 3 approaches compared: Sidekick (Cognition), Panel Synthesis (OpenRouter), Evolved Orchestration (Sakana)
- Comparative analysis table, economics argument, harness engineering implications, open questions

**Entity pages updated (3)**: `entities/cognition.md`, `entities/openrouter.md`, `concepts/sakana-fugu.md`
**Adjacent concept updated (1)**: `concepts/coding-agents/model-routing.md`
**Raw articles saved (2)**: cognition-devin-fusion, openrouter-fusion-api
