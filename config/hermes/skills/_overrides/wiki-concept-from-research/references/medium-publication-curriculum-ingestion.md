# Medium Publication Curriculum Ingestion Pattern

## When to Use
When a Medium publication contains a systematic, curriculum-structured series of articles by a single author covering a coherent discipline (e.g., Query Understanding, Search Engineering, RLHF). The articles form a bottom-up or top-down curriculum that can be synthesized into a single comprehensive concept page.

## Discovery Phase

### Step 1: Extract the archive
```
web_extract("https://<publication>.com/archive")
```
The Medium archive page lists top stories with:
- Title, URL, date
- Read counts (engagement signal)
- Opening excerpt (content signal)
- Response counts

This gives you a ranked article list without needing to scrape individually.

### Step 2: Expand via web_search
```
web_search("site:<publication>.com <author name>")
```
The archive only shows ~10 top articles by reads. web_search with `site:` finds the long tail — older articles, less-read but conceptually important ones, and recent additions not yet ranked high in the archive.

### Step 3: Map the curriculum structure
The introduction article (if it exists) typically lays out the curriculum roadmap. Look for phrases like:
- "We'll start at the bottom of the stack with..."
- "We'll continue on to..."
- "Finally, we'll look at..."

This gives you the layer structure for the concept page.

## Extraction Phase

### Medium articles extract well via web_extract
Unlike Substack/LessWrong (which often return machine-generated summaries), Medium articles generally return usable content via `web_extract`. The extracted markdown preserves headings, key quotes, and technical details. For a concept page synthesis, web_extract output is sufficient — you don't need browser fallback.

### 404 risk on guessed URLs
Medium article URLs follow the pattern `https://<publication>.com/<slug>-<hash>`. Guessing slugs from article titles mentioned in the introduction often fails (the articles may have been renamed, deleted, or the slug wasn't what you expected). Only reference URLs you've confirmed exist via web_search or archive.

## Synthesis Phase

### Hierarchical concept page structure
When the articles form a curriculum with explicit layers, structure the concept page as:

1. **Definition & Philosophy** — From the manifesto/introduction articles
2. **The Stack Diagram** — ASCII art showing the layer hierarchy
3. **Layer-by-layer breakdown** — Each layer gets a subsection with a technique table
4. **Cross-cutting concerns** — Techniques that span multiple layers (e.g., autocomplete)
5. **Full article catalog** — Numbered table mapping all articles to their layers
6. **Modern relevance** — How classical techniques map to LLM-era equivalents
7. **Distinction from related concepts** — Per SCHEMA.md requirements

### Technique table format
For each layer, use a consistent table:
```
| Technique | What It Does | Key Trade-off / Challenge |
|---|---|---|
```

### Layer ordering
The introduction article's roadmap determines the layer order. Bottom-up (characters → tokens → rewriting → context → conversation → results) is typical for search/IR curricula.

## Entity Page Update

The author's entity page should gain a "Publication Series" section with:
- Full numbered table (all articles, dates, layer assignments)
- Links to both the original Medium URLs and the saved raw articles (when saved)
- A pointer to the synthesized concept page

Format:
```
| # | Article | Date | Layer |
|---|---|---|---|
| 1 | [Title](URL) [[raw/articles/...]] | Date | Layer |
```

### Dual-Series Entity Page Enrichment
When the same author has **multiple companion publication series** (e.g., Tunkelang's Query Understanding 2016–2024 AND Content Understanding 2021–2022), stack the series tables sequentially on the entity page. Each series gets its own `## Publication Series` subsection, ordered chronologically by the first series. The entity page's index.md summary line should mention both series and link to both concept pages.

## Cross-Publication Cross-Referencing

When you systematize **two companion publication series** by the same author (e.g., QU + CU), cross-reference them both ways in each concept page:

1. In **both** concept pages' "Distinction from Related Concepts" section, add the other as the **first entry** — it's the most closely related concept.
2. The cross-reference should explain the relationship directionally:
   - From QU: "CU is the document/index-side counterpart. While QU interprets searcher intent, CU enriches content to make it findable. They form a virtuous cycle through engagement data."
   - From CU: "QU is the query-side counterpart. CU represents content in the index (foundation); QU interprets searcher intent. They complement each other through engagement data."

This creates bidirectional navigation that makes both pages discoverable from each other.

## Non-Hierarchical Stack Structures

Not all publication series follow a strict bottom-up layer hierarchy. Some (e.g., Content Understanding) have a flatter structure:
- Technique layer (classification + annotation — parallel, not stacked)
- Rich representation (similarity)
- Document engineering (structure)
- Ranking (quality)
- Applications (moderation, extraction)

When the curriculum doesn't have explicit layers, organize by **functional grouping** rather than forcing a hierarchy. Use the introduction article's structure as a guide — it usually implies the author's intended organization.

## Dangling Wikilink Resolution

Before creating the concept page, check if the author's entity page already has a `[[concepts/<name>]]` wikilink pointing to it:
```bash
grep -rn 'concepts/<proposed-slug>' wiki/ --include='*.md' -l
```
If it exists, creating the concept page immediately resolves the dangling reference — this is the highest-value outcome.
