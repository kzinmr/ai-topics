# Site-Specific Extraction Quick Reference

When extracting blog content, check this list first for known patterns before trying generic approaches.

## Databricks (Gatsby 5)

**Framework:** Gatsby 5.15.0, Tailwind CSS, Marketo forms
**curl works?** Yes — content is inline in HTML, not SPA
**Problem:** 50KB+ of `<style>` tag CSS bloat
**Solution:** `curl | python3` with script/style stripping. See `references/databricks-gatsby-extraction.md`
**Meta tags:** `article:published_time`, `og:description` are reliable

## Anthropic / claude.com/blog (Webflow SSR)

**Framework:** Webflow (SSR, not pure SPA)
**curl works?** Yes — article body IS in the HTML, but buried under ~50KB of CSS/JS noise
**Solution:** `curl -sL URL` → Python targeted extraction (find unique article text, strip tags from that offset). Jina Reader is a fallback.
**Key detail:** The page includes `datePublished` in JSON-LD (`<script type="application/ld+json">`), and `<meta>` tags for og:title/og:description. Article body starts at a unique phrase (e.g., "The fifth spec release of the Model Context Protocol") — find that offset, then strip HTML tags from there. Navigation/footer noise appears AFTER the article text.
**Pitfall:** Do NOT use broad regex from the start of the file — the CSS/JS block is ~50KB and will dominate extraction. Anchor on a unique content string first.
**Also noted:** `delegate_task` with `web` toolset often returns only a brief summary for claude.com/blog, not full content — prefer direct curl+Python.

## OpenAI / openai.com (Next.js RSC)

**Framework:** Next.js with React Server Components
**curl works?** No — returns empty `<div id="__next">`
**Solution:** Jina Reader or tagged-text-block extraction from RSC payloads

## Hex.tech (Astro/React)

**Framework:** Astro with React islands
**curl works?** No — navigation noise only
**Solution:** Jina Reader

## Cognition.ai (SPA)

**Framework:** SPA
**curl works?** No — 404 or empty
**Solution:** Jina Reader

## Google Slides

**Solution:** `/export/txt` first, then `browser_console` with `document.body.innerText`
See `references/google-slides-ingestion.md`

## Addy Osmani / Xe Iaso / Simple Blog Templates

**Framework:** Static HTML, simple templates
**curl works?** Yes
**Solution:** Regex-only extraction (no BS4 needed). See content-extraction-fallbacks.md "Regex-Only Extraction" section.
