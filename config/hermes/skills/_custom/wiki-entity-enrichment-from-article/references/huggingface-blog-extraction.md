# HuggingFace Blog Article Extraction

## Problem

HuggingFace blog pages (`huggingface.co/blog/{slug}`) use SSR/SPA rendering. The `<article>` tag extraction pattern frequently returns **navigation chrome, sidebar content, or empty results** instead of the actual article body. This affects both `web_extract()` and curl+HTML-parsing approaches.

Confirmed failures:
- `hf-cli-for-agents` — returned dataset preview widget content
- `hf-skills-training` — returned dataset preview widget content

## Solution: GitHub Raw Markdown Fallback

Every HuggingFace blog post has its source markdown on GitHub:

```
https://raw.githubusercontent.com/huggingface/blog/main/{slug}.md
```

This returns clean markdown with YAML frontmatter (title, authors, thumbnail, etc.).

### Extraction Sequence for HF Blog URLs

1. **Try GitHub raw first** (most reliable):
   ```bash
   curl -sL "https://raw.githubusercontent.com/huggingface/blog/main/{slug}.md"
   ```
   - Returns full article with frontmatter, headings, code blocks, images
   - Authors are HF usernames (resolve to `huggingface.co/{user}`)

2. **If GitHub raw 404s** (new post not yet merged to `main`):
   - Try `web_extract()` on the blog URL — may work for simpler pages
   - Try curl + HTML parsing as last resort

3. **Frontmatter enrichment** — add to the raw article file:
   ```yaml
   ---
   url: "https://huggingface.co/blog/{slug}"
   date: YYYY-MM-DD  # from page or git history
   source: huggingface-blog
   authors: [username1, username2]  # from frontmatter 'user' field
   ---
   ```

### Author Resolution

HF blog frontmatter uses `user:` fields (e.g., `burtenshaw`, `evalstate`, `celinah`, `Wauplin`). These are HuggingFace usernames, not display names. Resolve via:
- `https://huggingface.co/{user}` profile page
- The blog post's visible author display names (in the rendered HTML header)

## Related

- OpenAI blog articles also use SPA rendering — see [js-rendered-docs-workarounds.md](js-rendered-docs-workarounds.md)
- HF blog posts often link to GitHub repos (like `huggingface/skills`) — scrape the repo README as supplementary source
- **Date not in frontmatter**: HF blog raw markdown has NO `date:` field. Publication date is only in the rendered HTML. Always verify date before saving — see `article-date-verification.md`
