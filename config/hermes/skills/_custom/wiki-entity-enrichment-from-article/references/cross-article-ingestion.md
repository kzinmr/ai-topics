# Cross-Article Comparative Ingestion Pattern

> When a user provides 2+ article URLs and asks to discuss them together, ingest any missing ones, and cross-link.

## Trigger

User message like: "Here's article A and B. Discuss them together. If B isn't in the wiki yet, ingest it."

Or: "compare these articles / cross-reference them / how do they relate"

## Workflow

### 1. Check All Articles for Existing Wiki Pages

Run TWO searches per article — one for file existence, one for content mentions:

```
search_files(target="files", pattern="<domain-slug>", path="wiki/")
search_files(target="content", pattern="<unique-url-slug>", path="wiki/")
```

This catches both dedicated pages AND mentions within other pages.

### 2. Triage

| Status | Action |
|--------|--------|
| All already in wiki | Skip ingestion, load existing pages, proceed to synthesis |
| One missing | Ingest the missing one (Step 3), then cross-link |
| All missing | Ingest all, then cross-link |

### 3. Ingest Missing Article(s)

Follow the standard workflow from the parent skill:
- Extract content via `web_extract`
- Determine publication date (URL path, meta tags, JSON-LD)
- Save raw article to `wiki/raw/articles/` following `raw-article-filename-policy`
- Decide: concept page, entity page (if author is notable and new), or section in existing page
- Add any new tags to `wiki/SCHEMA.md` before using them in frontmatter
- Create pages with proper frontmatter

### 4. Cross-Link Between Articles

For each existing page related to the articles:
- Add the new page(s) to the `See Also` section
- Add relevant `[[wikilinks]]` in the body where natural
- Bump the `updated` date in frontmatter
- Consider adding new tags that connect the concepts

For each new page:
- Include `[[wikilinks]]` to the other article's concept page
- Include `[[wikilinks]]` to the author's entity page (if created)
- Use the `related:` frontmatter field

### 5. Update Infrastructure

- `wiki/index.md`: add entries for any new pages
- `wiki/log.md`: append a single entry covering all actions in the session
- Commit + push: `cd ~/ai-topics && git add wiki/ && git commit -m "wiki: ..." && git push`

### 6. Provide Comparative Synthesis

Present the cross-discussion covering:
- **How they converge**: common problem, shared insight
- **How they differ**: layer (philosophy vs. infrastructure), scope, approach
- **How they complement**: what each contributes that the other doesn't
- **Overall picture**: the combined architecture or framework they imply

Use a summary table at the end listing all files created/modified.

## Real Example

This session: TurboPuffer `rank-by-attribute` (already in wiki) + softwaredoug `metadata-the-3rd-kind-of-retrieval` (not in wiki).

- TurboPuffer provided the **infrastructure layer** (Saturate/Decay functions, vectorized query engine)
- Doug Turnbull provided the **philosophy layer** (metadata as 3rd retrieval paradigm, explainable ranking)
- Convergence: both recognize BM25-only limits, both advocate per-attribute similarity functions
- New pages: `concepts/metadata-retrieval.md`, `entities/doug-turnbull.md`
- Updated: `concepts/turbopuffer-rank-by-attribute.md` (+cross-links, +tags)

## Pitfalls

- Don't forget to add new tags to SCHEMA.md **before** using them in page frontmatter — pre-commit will block otherwise
- When cross-linking, read the target page's full "See Also" section to know where to insert without breaking structure
- Entity pages for article authors are optional — only create if the author has notable contributions beyond this single article
- The `search_files` + `target: files` check confirms dedicated pages exist; `target: content` catches mentions within other pages
