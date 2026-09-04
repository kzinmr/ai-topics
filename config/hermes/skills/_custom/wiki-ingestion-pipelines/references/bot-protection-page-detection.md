# Bot Protection Page Detection in Blog Ingest

Some blogs serve bot protection challenge pages instead of actual content when scraped by automated tools. The blog ingest pipeline saves these as raw articles, which then get triaged incorrectly.

## Known Bot Protection Patterns

| Blog | Protection System | Detection |
|------|------------------|-----------|
| xeiaso.net | Anubis (Techaro) | Page contains "Protected by Anubis From Techaro" + version string |
| Various Substack | Cloudflare 403 | HTTP 403 with Cloudflare challenge page |
| beehiiv newsletters | Cloudflare 403 | 403 response, article body is empty or challenge page |

## Detection Heuristics

A raw article is likely a bot protection page if:
1. **Extremely short** (< 500 bytes) — real blog posts are rarely this short
2. **Contains protection system keywords**: "Anubis", "challenge", "verify you are human", "Cloudflare", "captcha"
3. **No substantive content**: Just a protection notice, version string, and mascot credit
4. **Missing expected structure**: No paragraphs, no code blocks, no images — just boilerplate

## Example: xeiaso.net Anubis Page (July 2026)

The blog ingest collected `xeiaso.net--blog-2026-hyle-pneuma--6ebcbf3e.md` which appeared to be about "Agents are monads (but not that kind)" but actually contained:

```
Protected by Anubis From Techaro. Made with ❤️ in 🇨🇦.
Mascot design by CELPHASE.
This website is running Anubis version v1.26.0-pre1.0.20260709031803-c3474d5bfb11.
```

This is NOT the actual blog post content — it's the Anubis challenge page that was served to the scraper.

## Action

When a raw article matches bot protection patterns:
1. **Do NOT create wiki pages from it** — the content is meaningless
2. **Mark as skip** in triage decisions
3. **Log the detection** so future runs can identify the pattern
4. **Consider re-fetching** with a browser-based tool (e.g., `browser` toolset) if the article is important

## Related

- `references/blog-triage-coverage-verification.md` — how to verify whether content is substantive
- xeiaso.net uses Anubis v1.26+ — this may be a persistent pattern requiring browser-based fallback
