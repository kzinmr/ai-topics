# Cross-Cutting Article Ingestion

When an article touches **multiple existing wiki pages**, distribute its content across those pages rather than creating a new standalone page.

## When This Applies

- Article covers a topic that already has 2+ existing concept/entity pages
- Article's key insights span multiple domains (e.g., "RLM + DataFrame + Sandboxing")
- Creating a new page would duplicate content already partially covered elsewhere

## Workflow

1. **Map article themes to existing pages** — identify which existing pages each section of the article enriches
2. **Save raw article** to `wiki/raw/articles/` (always, for provenance)
3. **Patch each existing page** with the relevant slice of the article:
   - Add new sections (not just a link — extract the substance)
   - Update frontmatter: `updated`, `sources` (add raw article path)
   - Maintain each page's existing voice and structure
4. **Create new pages only for genuinely new concepts** that don't fit any existing page
5. **Update cross-references** — if page A now references page B's topic, add wikilinks in both directions
6. **Update `index.md`** — enrich descriptions of updated entries to reflect new content
7. **Update `log.md`** — single log entry covering all files touched, with a "Key insight" summarizing the cross-cutting theme
8. **Commit all changes atomically** — one commit for the entire ingestion

## Example: Article Touching 3 Existing Pages

Article: "A Data Scientist RLM That Lives in Your Program" (kmad.ai)
- **`concepts/dspy-rlm.md`** ← SandboxSerializable protocol, DataFrame support, DABench benchmark
- **`concepts/agent-sandboxing.md`** ← WASM sandbox (Deno+Pyodide) as new isolation tier
- **`concepts/dspy-modules.md`** ← (could have added DataFrame module reference)

## Sub-Pattern: Opinion Leader Policy Essays

When an opinion leader (CEO, policy director, senior researcher) publishes a comprehensive policy essay spanning multiple domains, the ingestion has distinct requirements beyond standard cross-cutting articles:

### Entity Page Treatment
- Add to **publications table** (if one exists) with year and one-line significance
- Add a **detailed "Recent Commentary" section** with:
  - Core thesis in 1-2 sentences
  - Framework structure (numbered list of domains/areas)
  - Key quotes (2-4) — direct quotes carry outsized weight for policy essays
  - Wikilinks to each concept page the essay touches
- This is NOT just a mention — extract the substance for readers who won't click through to concept pages

### Concept Page Treatment
Each concept page gets a **domain-specific section** that extracts the essay's specific proposals/arguments for THAT domain:
- Use `## <Author>'s <Framework Name> (<Date>)` heading
- Summarize proposals in bullet points with bold labels
- Include 1-2 key quotes relevant to this specific domain
- Cross-reference other concept pages touched by the same essay
- Contrast with prior positions if applicable

### New Concept Page Threshold
Create a new concept page when the essay introduces a **substantial domain not yet in the wiki**:
- The domain should have ≥3 distinct conceptual subsections
- Frame as a standalone concept page, not a summary of the essay
- Use the essay as primary source but structure around the concept itself
- Example: Amodei's "Policy on the AI Exponential" → new `ai-labor-displacement.md` (3-tier framework, meaning problem, international dimension)

### Index.md Enrichment
Update descriptions of ALL touched entries to reflect the new policy framework — these essays often significantly change the scope of existing concept pages.

## Pitfalls

- **Don't create thin "summary" pages** that just link to the raw article. The value is in synthesizing the new info into existing pages.
- **Don't overwrite** existing page content — use `patch` to add sections.
- **Frontmatter discipline**: always bump `updated` date and add the raw article to `sources` on every touched page.
- **One commit, not N**: commit all related changes together so the atomicity reflects the conceptual unit.
- **Policy essays need substance, not just links**: A concept page entry like "Amodei discussed this in his essay" is worthless. Extract the specific proposals, frameworks, and quotes for that domain.
- **Don't create a concept page for every section of a policy essay**: Only when the domain is genuinely new AND substantial enough to stand alone.
