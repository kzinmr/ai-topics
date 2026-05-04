# Manual Article Ingest Patterns

Common patterns that apply across all manual wiki-ingest operations (URL-based, not batch pipeline).

## Pattern 1: Author Identification via Secondary Search

`web_extract(url)` often returns the article body **without the author byline** — especially on publication platforms (Every, Substack, The Conversation, Medium, bulletins).

**Do not assume the author is unknown.** The byline is usually in the page's `<meta>` tags, schema.org JSON-LD, or the page title/subtitle region that `web_extract` omits.

### Detection
- Check if the scraped content starts with the article body directly (no "By Author Name" line)
- Check if the search result snippet from `web_search` or `web_extract`'s `description` field contains the author name
- If the article mentions a colleague or co-author by name but not the current author, that's a strong signal you need to search deeper

### Resolution Steps
1. **Try `/about/` URL first** — For individual-author blogs (danielmiessler.com, simonwillison.net, etc.), `web_extract(url + "/about/")` often returns a complete biography with career timeline, key projects, and philosophy. This is faster and richer than building bio from fragments.
2. **Search the article URL directly**: `web_search(query="<article URL> author")` — the meta description in search results often includes the byline
3. **Search the site with article title**: `web_search(query="site:every.to \"Guide to Agent-native Product Management\" by")`
4. **Search for the companion/promotional post**: The publication may have a separate "about this guide" post that names the author (e.g., Every publishes a companion essay alongside their guides)
5. **Check social media cross-posts**: If the article was promoted on X, the tweet introducing it often names the author
6. **Fallback — search for the quoted intro text**: Extract a distinctive first-person sentence from the scraped content and search it in quotes — the search result snippet often reveals the author

### Example (Every.to)
- `web_extract("https://every.to/guides/ai-product-management-guide")` returned body without byline
- The author says "I'm a one-person team working on Spiral" → search "Spiral general manager" + "Every" + keyword from article
- `web_search("site:every.to \"I'm responsible for product management\" author")` revealed the promotional post mentioning "Marcus Moretti, General Manager of Spiral"

### Example (Daniel Miessler)
- `web_extract("https://danielmiessler.com/about/")` returned full biography: career timeline (Apple, HP, Robinhood, US Army), key projects (Fabric AI, SecLists, PAI, TELOS), Human 3.0 philosophy, and personal interests — all used directly for entity page creation

## Pattern 2: Related-Concept Detection and Disambiguation

Before creating a new concept page, you MUST check for existing pages that cover related but distinct concepts. The risk is either:
- **Duplicating** an existing concept under a different name
- **Overwriting** a related concept when a cross-reference or disambiguation page is more appropriate

### Resolution Steps
1. **Search for the exact concept name** in `~/wiki/concepts/` (files)
2. **Search for aliases and related terms** — the concept may exist under a different slug
3. **Search content of existing concept pages** for mentions of the new article's key terms
4. **If a related page exists, decide the relationship**:
   - **Same concept, different source** → Update the existing page (add section, sources, cross-refs)
   - **Related but distinct concept** → Create a new page with explicit cross-references to the existing one
   - **Same name, different scope** → Create a redirect page at the ambiguous slug, pointing to both variants

### Example: Compound Engineering
| Page | Source | Scope |
|------|--------|-------|
| `compound-engineering-loop` (Simon Willison) | simonwillison.net | Code-level feedback cycle (Write→Review→Improve→Save→Repeat) |
| `compound-engineering-every` (Every Inc.) | every.to | Business-level philosophy + plugin (ce:strategy, ce:product-pulse) |

**Decision**: Different scope → separate pages. The ambiguous slug `compound-engineering-loop` became a redirect to both.

## Pattern 3: Author's Organization & Products Mapping

When an article discusses a company's products or philosophy, create entity pages for:
- **The company** (if not already in wiki)
- **The author** (if a notable voice, GM, or recurring writer)
- **Key named colleagues** referenced in the article (if they have influence beyond one article)

### Example (Every.to guide)
| Entity | Reason |
|--------|--------|
| every-inc | Company behind the guide, 5 AI-native products, Compound Engineering plugin |
| marcus-moretti | Author, GM of Spiral, created ce:strategy/ce:product-pulse |
| kieran-klaassen | Referenced as colleague, author of Compound Engineering guide, GM of Cora |
| dan-shipper | Not created (no independent material in article) — CEO context captured in every-inc page |

## Pattern 4: MCP-Connected Tools Identification

When an article mentions data sources for agent workflows, extract the specific tools:
- **Analytics**: PostHog, Mixpanel, Amplitude
- **Tracing**: Datadog, Sentry, Logfire
- **Payments**: Stripe, Paddle
- **Databases**: Read-only replicas

These are valuable signals for the MCP ecosystem mapping. If a tool isn't yet in the wiki, consider creating a stub entity page for it (e.g., Logfire, Paddle).

## Pattern 5: Empirical Data Report → Cross-Page Enrichment (No New Pages)

When a **corporate data science report** or **empirical data article** (Shopify, Stripe, OpenAI, Meta, etc.) provides evidence supporting existing wiki concepts rather than introducing new ones:

### Detection
- The article is authored by a **data science / research team** (not an individual blogger or journalist)
- The content is **data-driven** (metrics, percentages, growth rates, comparisons over time)
- The data **validates, supports, or quantifies** trends already documented in existing concept/entity pages
- The article does **not introduce new technology, tool, or framework** — it's empirical evidence for existing themes

### Workflow

1. **Save raw article** to `wiki/raw/articles/` as usual.

2. **Identify the anchor entity** — the organization whose data is the source (e.g., Shopify, Stripe). This entity page gets:
   - A new H2 section (e.g., "Entrepreneurship & Ecommerce Trends (Shopify Data Science, Apr 2026)")
   - Sub-sections for each key finding (metrics, quotes, thesis statements)
   - An "Implications for [Related Concept]" sub-section that explicitly connects the data to existing wiki concepts
   - Updated `sources:` frontmatter with the raw article path
   - Updated `updated:` date

3. **Identify the target concept page(s)** — existing concept pages that the data empirically grounds (e.g., solo-founder-stack). Each concept page gets:
   - A new "Empirical Support" section (e.g., "Empirical Support: Shopify Data (April 2026)")
   - Key metrics quoted inline with the concept's context
   - A cross-reference back to the anchor entity page: `See [[entities/shopify|Shopify entity page]] for full breakdown.`
   - Updated References section with raw article path
   - Updated `updated:` date

4. **Update `index.md`** — only the anchor entity's description line may need a slight expansion. Concept page descriptions usually don't change.

5. **Update `log.md`** — single entry listing: raw article saved, which entity updated, which concept(s) updated, and the nature of the empirical support added.

### Key Differences from Other Patterns

| Aspect | Pattern 2 (Disambiguation) | Pattern 5 (Empirical Report) |
|--------|---------------------------|------------------------------|
| Pages created | None (or redirect) | None |
| Pages updated | Concept page (relationship clarification) | Entity page + Concept page(s) |
| Source type | Blog/opinion (conceptual distinction) | Data report (empirical evidence) |
| Cross-linking | Between ambiguous concepts | Entity page ←→ Concept page (data anchors concept) |
| index.md change | Often none | Minor (entity description expansion) |

### Pitfalls
- The anchor entity page already exists — don't create a duplicate
- The target concept page already exists — don't create a new concept; enrich the existing one
- Concept pages may be in `~/wiki/entities/` (like `solo-founder-stack.md`) or `~/wiki/concepts/` — search both
- Frontmatter `sources:` array must be updated on both pages (entity + concept)
- The "Implications" subsection on the entity page should use explicit `[[wikilinks]]` to the concept page(s)
- The concept page's "Empirical Support" section should cite metrics directly, not just link out
- Commit message should name both pages updated, e.g.: "wiki: enrich shopify entity + solo-founder-stack with entrepreneurship data report"

## Pattern 6: Substack Multi-Part Series Batch Discovery

When given a single Substack URL that is clearly **part 1 of a series** (title includes "part 1", "part one", "1/4", numbered introduction), the naive approach is to ingest only the provided URL and stop. This wastes the rest of the series and forces a follow-up request.

### Detection Signals
- Title/URL/subtitle contains "part 1", "Part 1", "part one", "1/4", or similar numbering
- Author's Substack was launched recently (check `/about` or the landing page) — new publications often publish series in quick succession
- `web_search("site:author.substack.com \"series name\"")` returns multiple results with numbered parts
- The article itself references "part 2", "next installment", "see also" with clear part labels

### Discovery Steps

1. **Check the archive page first** — the single most efficient call:
   ```
   web_extract("https://author.substack.com/archive")
   ```
   Substack's archive page lists ALL posts in reverse chronological order with titles, dates, and engagement metrics. You can visually scan for the full series.

2. **If archive doesn't load fully** (JS-dependent Substack pages sometimes return truncated HTML), fall back to:
   ```
   web_search("site:author.substack.com \"series name\"")
   ```
   This usually catches all parts in search results.

3. **Pattern-match the URLs** — Substack series parts follow predictable URL patterns:
   - `/p/agentic-engineering-the-configuration` → part 1
   - `/p/agentic-engineering-the-interface` → part 2
   - `/p/agentic-engineering-the-orchestration` → part 3
   - `/p/agentic-engineering-the-guardrails` → part 4
   The URL slug usually encodes the content topic, not the part number — so you can't predict the Nth URL without the archive.

4. **Fetch and scrape ALL parts simultaneously** — once you have all N URLs, scrape them in parallel with a single `web_extract()` call. This saves turns vs sequential scraping.

### Workflow After Discovery

1. **Save all parts as raw articles** — one file per part, named `YYYY-MM-DD_author-series-name-partN-slug.md`
2. **Create the author entity page** (if doesn't exist) — this is the authoritative hub for the author's framework
3. **Create sub-concept pages** — one per layer/part, each with `part-of` graph edge to the parent series concept
4. **Update the parent concept page** — the existing concept page that covers the broader topic (e.g., `agentic-engineering.md`) gets a new "N-Layer Framework" section that summarizes all parts
5. **Update index.md** — add all new entity + concept entries in one batch
6. **Update log.md** — single log entry covering the entire series batch
7. **Commit once** — `git commit -m "wiki: Author Name Series Name — entity page + N sub-concept pages + parent concept update + N raw articles"`

### Example (This Session)
- Input: Single Substack URL, part 1 of "Agentic Engineering" by Paul Hoekstra
- Archive discovery: `/archive` revealed parts 1, 2, 3, 4 + 2 bonus articles
- Result: 1 entity page + 4 sub-concept pages + 1 parent concept update + 6 raw articles
- Commit: `wiki: Paul Hoekstra Agentic Engineering 4-layer framework — entity page + 4 sub-concept pages + main concept update + 6 raw articles` (14 files, 792 insertions)

### Pitfalls
- **Don't assume the series is complete** — the archive may show parts published on the same day (batched release) or spread over weeks. Always check dates.
- **Bonus articles by same author** — while on the Substack, also check for recent non-series articles (e.g., statusline customization, visual output guides). These are often worth saving as raw articles even if they don't get their own concept page — they enrich the author's entity page.
- **Archive page may be paginated** — if the author has many posts, `/archive` may only show the first page. Use `web_search` as fallback for older parts.
- **Substack's `/archive` sometimes truncates** — if the page returns minimal HTML (JS-rendered), the archive list may be empty. In this case, `web_search` is the reliable fallback.
- **Don't create duplicate entity pages** — always search existing wiki entities for the author's name first (including partial matches and alternate spellings)

## Pattern 7: Multi-Concept Analytical Article Ingest

When a single article (survey, landscape analysis, thought piece) contains **3+ independent ideas**, each may warrant its own concept page or enrichment of existing pages. The Miessler "Most Important Ideas in AI" article is the canonical example: 5 ideas → 2 new concept pages + 2 enriched existing pages + 1 entity page.

### Detection Signals
- Article title contains "most important", "top N", "key trends", "landscape", "the state of", "shifts"
- Article body has numbered sections with distinct named concepts (e.g., "1. Autonomous Component Optimization", "2. Intent-Based Engineering")
- Each section could stand alone as its own essay — clear thesis statement, named framework, independent logic chain
- The article is by an author who deserves their own entity page (regular writer, founder, or domain authority)

### Decision Matrix: New Page vs Enrichment

| Article Idea | Check | Action |
|-------------|-------|--------|
| Novel named concept, not in wiki | `search_files` for the concept name | Create new concept page |
| Novel framing of an existing concept | Check existing page for that framing | Enrich existing page (add section) |
| Generalization of an existing concept | Check if existing page covers the generalization | Create new concept with wikilink to original |
| Author's personal philosophy/background | `search_files` for author name | Create/update entity page |
| Opinion/reaction without conceptual substance | — | Save as raw article only |

### Workflow

1. **Orient**: Read full article, identify each independent idea
2. **Check prior art**: For each idea, search existing wiki (`search_files` for slug/aliases/content)
3. **Classify each idea**: New concept vs enrichment of existing vs raw-only
4. **Create new concept pages first** — fresh files before patches (avoids cross-referencing issues)
5. **Enrich existing pages** — add sections with comparison tables, cross-links back to new pages
6. **Create/update entity page for author** — use `/about/` URL if available
7. **Update all index files** — `wiki/index.md` (main + entity count + concept count), `wiki/concepts/_index.md`
8. **Update `wiki/log.md`** — single entry listing all created pages, enriched pages, and raw article
9. **Commit once** — `git commit -m "wiki: Author Name — article title"`

### Pitfalls
- **Not all ideas need pages** — Miessler's "Opacity to Transparency" (#3) and "Expertise Diffusion into Public Knowledge" (#5) were included in the entity page's key ideas section without separate concept pages because they were descriptive observations rather than named frameworks. Distinguish named frameworks from observations.
- **concepts/_index.md must be updated** — the main `wiki/index.md` is not enough. Many wikis have a separate `concepts/_index.md` that lists concepts by category. Adding a concept page without updating this causes index drift.
- **Comparison tables enrich both sides** — When creating a new concept that generalizes an existing one (e.g., Autonomous Component Optimization generalizing Karpathy Loop), add a comparison table to BOTH pages with wikilinks each way.
- **Entity page should list all concepts** — The author's entity page is the hub. Add a "Key Ideas & Contributions" section that bullets each concept with wikilinks.
- **Git auto-commit race**: The file-system write + cron auto-commit cycle can commit your new files before your batch commit. After creating files, verify with `git ls-files | grep <pattern>` — if already tracked but not in your staged diff, they were auto-committed. Just commit what remains.
