# Single-URL Blog Post Ingestion Workflow

When the user gives a single blog post URL and says "ingest this" / "取り込んで" / "wikiに入れて".

## Pre-checks (before any writes)

1. **Extract metadata**: title, date, author, source domain from the URL
2. **Check if raw article already exists**: `search_files` in `wiki/raw/articles/` for filename patterns matching the source + slug. Blogwatcher often auto-ingests — the file may already exist with `blogwatcher` naming (e.g., `simonwillison.net--2026-jul-31-stateless-mcp--b7e83578.md`)
3. **Check existing wiki coverage**: `search_files` for the topic keywords across `wiki/concepts/`, `wiki/entities/`, `wiki/comparisons/`
4. **Read relevant existing pages**: At minimum skim the raw article (if exists), any related concept pages, and the main entity page for the author

## Decision tree

```
Raw article exists?
├─ YES → Enrich frontmatter (add date, type, tags per raw-article-filename-policy)
│        Skip content rewrite (raw/ is immutable layer)
└─ NO  → Fetch + save with proper filename policy

Concept page exists for the topic?
├─ YES → Check if article adds new info not yet covered
│        ├─ New info → patch concept page (append section, update sources)
│        └─ Already covered → skip concept page update
└─ NO  → Evaluate: does the topic warrant a standalone concept page?
         ├─ YES → Create concept page (full wiki-entity-enrichment-from-article flow)
         └─ NO  → Enrich the most relevant existing concept page

Entity page for author exists?
├─ YES → Add a dedicated section covering the article's key points
│        (don't just add to sources — write a substantive subsection)
└─ NO  → Create entity skeleton (separate workflow)
```

## Entity section enrichment pattern

When adding an article-driven section to an existing entity page:

1. **Find insertion point**: Before "Blog articles (unprocessed)" list or before "Sources" section
2. **Section title format**: `### Topic Name (Month Year)` — e.g., `### MCP Renaissance: Stateless MCP & Three New Tools (July 2026)`
3. **Content structure**:
   - Opening context sentence (why this matters, what changed)
   - Key technical points (comparisons, data, architecture)
   - Tools/projects mentioned (table format if 3+)
   - Author's stance/opinion (direct quotes preferred)
   - Connection to existing wiki concepts (wikilinks)
   - Source wikilink to raw article
4. **Update frontmatter**: bump `updated` date, add raw article to `sources` list if not already there

## Post-write (always)

1. Update `wiki/index.md` — refresh the entity/concept entry description
2. Append to `wiki/log.md` — follow existing log format
3. Commit + push: `cd ~/ai-topics && git add wiki/ && git commit -m "wiki: ..." && git push`

## Pitfalls

- **Don't create duplicate concept pages**: If `mcp-2026-07-28-spec.md` already covers the topic comprehensively (including the article's content), don't create `stateless-mcp.md`
- **Don't just append to sources list**: The entity page enrichment should be a *readable section*, not just a source reference
- **Raw files are immutable**: Only fix frontmatter in raw articles, never rewrite content
- **Check multiple existing pages**: One article may touch multiple concept/entity pages — search thoroughly before deciding "no existing coverage"
- **Blogwatcher naming vs policy naming**: Existing raw files from blogwatcher use `domain--date-slug--hash.md` format. Don't rename them — just enrich frontmatter.
