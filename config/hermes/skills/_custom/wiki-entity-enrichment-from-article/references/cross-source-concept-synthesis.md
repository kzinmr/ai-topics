# Cross-Source Concept Synthesis Workflow

When the user provides N URLs that discuss the same topic from different angles (different products, different layers, different perspectives), the goal is a **unified concept page** that identifies the common thread plus individual entity pages for each source.

## Example

User gives: LinkedIn post about Qdrant branch-aware search + Qdrant tutorial + Neon database branching docs.
Output: `concepts/branch-aware-search.md` (unified pattern + comparison table) + `entities/qdrant.md` + `entities/neon-database.md` + raw article.

## Sequence

1. **Fetch all sources in parallel** — use terminal curl for each URL. LinkedIn pages need the same HTML stripping as docs pages. Tutorial/framework docs often render content inside `<main>` tags — try extracting that specifically if the first attempt returns mostly navigation.

2. **Identify the common thread** — what concept connects these sources? Name it. This becomes the concept page title.

3. **Create raw article(s)** — one per distinct source or a combined summary if the sources are tightly linked. Save to `wiki/raw/articles/YYYY-MM-DD_slug.md`.

4. **Create the concept page** (`concepts/<name>.md`):
   - Problem statement (what gap does this pattern fill?)
   - Core pattern / mechanism (technical details)
   - **Comparison table** — dimension-by-dimension comparison of the different implementations
   - Shared design principles (what makes them instances of the same pattern)
   - Use cases (union of all sources)
   - Open questions (from comments, discussions, gaps)
   - Wikilinks to each entity page

5. **Create entity pages** (`entities/<name>.md`) — one per distinct product/tool/company:
   - Standard entity frontmatter
   - Link back to the concept page via wikilink
   - Include the specific implementation details that differentiate this entity

6. **Update SCHEMA.md, index.md, log.md** — standard wiki update flow

7. **Single commit + push**

## Tips

- The concept page is the **synthesis layer** — it should be more than the sum of its parts. Don't just concatenate summaries; identify the shared abstraction.
- The comparison table is the highest-value artifact. Choose dimensions that highlight both similarities and differences.
- LinkedIn posts often contain the best framing (problem statement, key insight) while docs contain the technical details. Use both.
- If the user asks "is X similar to Y?" — the answer is usually "yes, here's the shared pattern" and that shared pattern IS the concept page.
