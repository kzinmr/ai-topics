# Web Article Fetching for Wiki Ingestion

## Problem
`terminal` + `curl` may time out or be blocked on headless servers (timeout, network policy, Cloudflare challenges). Blog articles need to be fetched for raw article saving and wiki page creation.

## Solution: delegate_task with web toolset

Use `delegate_task` with `web` toolset to fetch article content. The subagent returns full markdown text that can be used directly.

### Pattern

```
delegate_task(
  goal="Fetch the full text content of <URL> and return the complete article text in markdown format. Include the title, author, date, and all section headings and body text.",
  toolsets=["web"]
)
```

### What the subagent returns
- Full article body in markdown (headings, lists, bold, links)
- Title, author, date
- Summary of what it found

### Workflow integration
1. Call `delegate_task` to fetch article
2. Save the returned markdown as raw article to `wiki/raw/articles/` with proper frontmatter
3. Use the content to create/enrich concept or entity pages
4. The subagent does NOT save files — parent agent handles all wiki writes

### When to use this vs terminal+curl
- **Use delegate_task+web** when: curl times out, Cloudflare blocks, SPA content, sites requiring JS rendering
- **Use terminal+curl** when: simple static sites, fast response expected, need to control headers/extraction precisely

### Example (actual session)
Fetching `https://florianbrand.com/posts/open-model-safety`:
- `terminal` + `curl` timed out (blocked)
- `delegate_task` with `web` completed in ~125s, returned full article text
- Article saved to `raw/articles/florian-brand-open-model-safety.md`, concept page created

### Limitations
- delegate_task is synchronous — blocks parent turn
- No control over HTTP headers or extraction logic
- Subagent may return extra metadata/summary beyond raw article text (strip if needed)
- ~2 min latency typical for web fetch
- **SPA sites (Next.js, React, Astro)**: delegate_task with web/browser toolsets often FAILS to return article content — the subagent reports success but returns only a brief summary or empty content. This was observed on openai.com (Next.js RSC), claude.com/blog (Webflow SPA), and similar sites. The subagent's web tool may not render JS fully.

## Recommended Fallback for SPA Sites: Jina Reader

For JS-rendered sites (openai.com, claude.com, cognition.ai, hex.tech, any Webflow/Next.js/Astro SPA), **skip delegate_task entirely** and use Jina Reader first:

```bash
curl -sL "https://r.jina.ai/https://example.com/article" -H "Accept: text/markdown" 2>&1
```

**Why Jina Reader over delegate_task for SPAs:**
- Actually renders JS server-side and returns full content
- Single terminal call (~5-10s) vs delegate_task (~2min) with unreliable results
- Returns clean markdown with title, date, and structured content
- No browser session or Python dependencies needed

**Date discovery via Jina**: The output often includes publication dates in the rendered text (e.g., "Jun 25, 2026" appears near the title). Search the output for date patterns when meta tags are unavailable via curl.

**Priority order for article fetching:**
1. `terminal` + `curl` — try first for static sites
2. `terminal` + Jina Reader (`curl r.jina.ai/URL`) — use for pure SPA sites (empty div, no content in HTML)
3. `delegate_task` with web toolset — use only when both above fail (e.g., paywalled, geo-blocked)

**Webflow SSR sites (claude.com/blog etc.):** curl returns full HTML with article body embedded under ~50KB CSS/JS noise. Use `python3 -c "import re; ..."` with a unique content anchor string to skip the noise. See `references/site-specific-extraction.md` under "Anthropic / claude.com/blog". Do NOT default to Jina Reader for Webflow — curl+Python is faster and more reliable.
