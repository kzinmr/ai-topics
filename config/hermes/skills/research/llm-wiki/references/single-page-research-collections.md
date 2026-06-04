# Single-Page Research Collections

Pattern for ingesting research lab pages where multiple posts are listed on a single page with no individual post URLs. Common for AI labs (Noumena Network, academic groups, etc.).

## Recognition

The page at `/research/` lists multiple entries, each with:
- A title
- A brief summary (1-2 sentences)
- A category tag (research result, methodology result, systems framing, research hypothesis)
- A common publication date

Individual post URLs either don't exist (404) or are SPA-routed and inaccessible via `web_extract`.

## Workflow

### 1. Extract the full listing page
```bash
web_extract(urls=["https://<lab>.com/research/"])
```
Expect all posts as summaries on one page. Confirm individual post pages are not accessible.

### 2. Save as a single raw article
One file covering all posts. Name: `{YYYY-MM-DD}_{lab-slug}-research-{N}-posts.md`

### 3. Gather supplementary sources
- Lab's GitHub org (READMEs, architecture docs)
- Lab's X/Twitter account
- Any HuggingFace blog posts
- Web search for external coverage

### 4. Create entity page first
Entity page for the lab itself — philosophy, workstreams, roadmap, key people. This anchors all subsequent concept pages.

### 5. Create synthesis concept page
Group all posts into thematic clusters (methodology, results, systems). Create ONE rich concept page covering all posts rather than thin individual pages for each post. Use the grouped themes as sections.

Determine page thresholds: if a post would yield <15 lines as a standalone page, fold it into the synthesis page instead.

### 6. Cross-reference with existing stubs
Check if linked pages exist as stubs (e.g., `mixture-of-experts.md`). Add cross-references to those stubs during ingestion so the wiki graph is connected even before stubs are enriched.

### 7. Enrich related entities
If key people (founders, core engineers) have stub pages, enrich them in the same batch. Add their entry to `x-accounts.yaml` if tracked.

## Example: Noumena Network

- Page: `https://noumena.com/research/` — 12 posts on one page
- Result: 1 raw article + 1 entity page + 2 concept pages (methodology synthesis + RDEP)
- Key people enriched: xjdr (stub→full)
- Stub cross-ref added: `mixture-of-experts.md`

## Pitfalls

- **Don't guess individual post URLs** — if pattern like `/research/post-slug/` returns 404, the content only exists on the listing page. Don't waste time trying variations.
- **Don't create 12 thin pages** — a synthesis page is more valuable than 12 stubs. Group thematically.
- **Don't skip the entity page** — the lab's identity and philosophy give context to the research.
