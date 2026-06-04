# Author Entity Backfill During Article Ingestion

When ingesting a blog post or research article, the author(s) often already have entity pages in the wiki. These existing entity pages must be updated with the new publication — this step is easily missed when delegating to subagents.

## When to Trigger

After saving the raw article and creating concept/entity pages for the article's subject, check if the **article authors** have existing entity pages. This applies to:
- Blog posts by known researchers (e.g., Benjamin Clavié, Simon Willison, Nathan Lambert)
- Research papers with tracked authors (e.g., arXiv preprints)
- Company blog posts by employees who have entity pages

## Detection

```bash
# Search for author entity pages
search_files(pattern="^title:.*AuthorName", path="wiki/entities/", target="files")
search_files(pattern="AuthorName|author-handle", path="wiki/entities/benjamin-clavie.md", target="content")
```

## Update Checklist (per author entity page)

1. **Frontmatter `sources:`** — add the new article URL and/or arXiv URL
2. **Frontmatter `updated:`** — set to today's date
3. **Current Work / Notable section** — add a paragraph about the new paper/article with `[[concepts/new-concept|wikilink]]`
4. **Related Concepts** — add `concepts/<new-concept-page>` if not already listed
5. **Sources section** (bottom of page) — add the URLs with one-line descriptions

## Example (Benjamin Clavié ← Latent Terms paper)

```markdown
# In entity page "Current Work" section, insert:
**Latent Terms — SAE-extracted BM25-ready Vocabularies (2026-06):** Clavié et al. 
published a preprint showing that dense retrievers contain information far beyond 
what single-vector scoring can express. ... arXiv:2605.29384. [[concepts/latent-terms|Latent Terms]]

# In entity page sources section, append:
- https://arxiv.org/abs/2605.29384 — Latent Terms paper (May 2026)
- https://www.mixedbread.com/blog/latent-terms — Latent Terms blog post (June 2026)

# In frontmatter:
updated: 2026-06-03  # today's date
```

## Pitfalls

- **Subagents won't do this automatically.** If you delegate raw/concept/entity creation to subagents, the author backfill must be done by the parent agent or as a separate subagent task with explicit instructions.
- **Multiple authors may each need updates.** A paper with 4 authors might mean 4 entity page updates. Prioritize authors who are first/last author or have significant existing pages.
- **Don't create entity pages for minor authors.** Only backfill pages that already exist. If a co-author doesn't have an entity page and isn't notable enough for L2/L3 threshold, skip them.
- **Section placement matters.** Put new work under "Current Work" or "Recent Work" if it exists. If the entity page uses a different structure (e.g., chronological research sections), insert in the appropriate timeline slot.
