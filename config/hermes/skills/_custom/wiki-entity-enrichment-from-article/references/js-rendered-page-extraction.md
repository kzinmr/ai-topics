# Handling JS-Rendered / SPA Article Pages

> **See also**: `references/nextjs-rsc-content-extraction.md` for Next.js App Router sites that use RSC (React Server Components) payloads — a different pattern from simple client-side rendering.

## Problem
Many personal blogs and documentation sites use client-side rendering (React, Vue, Next.js SSR, or simple `fetch()` + Markdown rendering). A `curl` or `terminal` fetch returns HTML shells with `<script>` tags and empty `<article>` / `<main>` containers — no actual content.

## Pattern: Try the `.md` Extension First

Before falling back to browser automation (`delegate_task` with browser toolset), try fetching the same URL with `.md` substituted for `.html`:

```
# Page URL:  https://www.k-a.in/rl-algo.html
# Try:       https://www.k-a.in/rl-algo.md
curl -sL "https://www.k-a.in/rl-algo.md"
```

**Why this works**: Many static-site generators and personal blogs (especially those using `marked.js`, `markdown-it`, or similar client-side Markdown renderers) store the raw `.md` files at the same path. The HTML page is a thin shell that `fetch()`es the `.md` and renders it.

**Detection heuristics** in the HTML source:
- `<script src="...marked.min.js">` → Markdown renderer loaded client-side
- `fetch('filename.md')` or `fetch('./content.md')` in inline `<script>` blocks
- Empty `<article id="content">` or `<main>` container with no server-rendered content
- Heavy CSS/JS imports (Prism, KaTeX, highlight.js) with minimal HTML body

## Jina Reader API — Best First Fallback

For JS-rendered sites (Next.js, React, Astro SPA) — especially **corporate blogs with Cloudflare protection** (openai.com, claude.com, cognition.ai) — skip the `.md` extension trick and go straight to Jina Reader:

```bash
curl -sL "https://r.jina.ai/https://example.com/article" -H "Accept: text/markdown" 2>&1
```

This is faster and more reliable than browser automation for these sites. See `references/content-extraction-fallbacks.md` § "Jina Reader API" for the full site compatibility table and rate limit notes.

## Other Fallback Strategies (in order)

1. **Check `robots.txt` / `sitemap.xml`** — sometimes reveals content paths
2. **Check GitHub/GitLab source** — many dev blogs are open-source repos with `.md` files
3. **RSS feed** — if the site has RSS, the full content may be in the feed XML
4. **Hacker News / Wayback Machine** — cached or plain-text versions
5. **Browser automation** — `delegate_task` with `browser` toolset (last resort, most expensive)

## Example: k-a.in Blog

- URL: `https://www.k-a.in/rl-algo.html`
- HTML detection: `fetch('rl-algo` found in inline script
- Raw content: `curl -sL https://www.k-a.in/rl-algo.md` → 262 lines of Markdown with KaTeX math
- Result: Full article retrieved without browser automation
