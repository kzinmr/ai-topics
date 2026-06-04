# Multi-Part Blog Series Ingestion Pattern

## When This Applies

A blog publishes a multi-part series on the same topic (e.g., "agentic retrieval" Parts 1–4). Each article builds on the previous, and the series forms a coherent knowledge unit. Simply ingesting each article into its own concept page leaves them disconnected.

## Pattern

### Step 1: Identify the Central Concept

Determine the ONE concept that the series is about. For the Hornet "agentic retrieval" series:
- Part 1: "Deep research is a retrieval problem" → core thesis
- Part 2: "This is what agentic retrieval looks like" → empirical evidence
- Central concept: **deep-research** (or the unifying topic)

### Step 2: Create/Enrich the Central Concept Page First

The central concept page becomes the **series hub**. It should:
- State the core thesis (from Part 1)
- Include key empirical data (from all parts)
- List the series timeline with future parts
- Cross-link to each part's specific concept pages

### Step 3: Cross-Link Bidirectionally

For each part's concept page (e.g., `concepts/agentic-retrieval.md`):
- Add the Part 1 article as a `source`
- Add a wikilink to the central concept page in "Related Concepts"
- Ensure the description explains the part's role in the series

For the central concept page:
- Wikilink to each part's concept page
- Wikilink to the broader framework (e.g., `concepts/agentic-search`)

### Step 4: Update the Author Entity Page

- Add each part to the **writings list** (chronological order)
- Add each part to the **timeline** (with key data points)
- Bump the `updated` date

### Step 5: Update the Product/Company Page

If the series is about a product (e.g., Hornet):
- Add all parts as `sources`
- Cross-link to the central concept page in "Related Pages"

### Step 6: Index and Log

- Add the central concept to `index.md` (alphabetical position)
- Update descriptions of modified existing entries
- Log all changes with the series context

## Real Example

**Series**: Hornet "agentic retrieval" by Jo Kristian Bergum
- Part 1 (Mar 2026): `concepts/deep-research.md` ← central hub
- Part 2 (May 2026): `concepts/agentic-retrieval.md` ← enriched with Part 1 source
- Cross-links: deep-research ↔ agentic-retrieval ↔ hornet ↔ agentic-search ↔ jo-kristian-bergum

### Pages Touched

```
concepts/deep-research.md         ← NEW (series hub)
concepts/agentic-retrieval.md     ← ENRICHED (+Part 1 source, +deep-research wikilink)
concepts/hornet.md                ← ENRICHED (+Part 1 source, +deep-research wikilink)
concepts/agentic-search.md        ← ENRICHED (+Part 1 source)
entities/jo-kristian-bergum.md    ← ENRICHED (+Part 1 writings, +timeline entry)
index.md / log.md                 ← UPDATED
```

## Pitfalls

- **Don't create a concept page per article** — if Parts 1–4 are about the same concept, create ONE central concept page, not four.
- **Don't nest too deep** — the central concept page should be the hub; each part's specific concept page (if it exists separately) should link back to the hub.
- **Update the timeline consistently** — all parts must appear in the author's timeline in date order.
- **Check for existing pages first** — the central concept may already have a stub (like `concepts/deep-research.md` was needed but didn't exist; `concepts/hornet.md` and `concepts/agentic-retrieval.md` existed as stubs).
