# OpenAI Blog Cloudflare Blocking — Syndicated Source Recovery

**Date observed:** May 2026  
**Affected URLs:** `openai.com/index/*`, `openai.com/jv-ID/index/*`

## Problem

OpenAI's engineering blog (`openai.com/index/...`) blocks automated access:
- `web_extract` returns LLM-summarized content at best, often truncated
- `curl` returns empty body or Cloudflare challenge page
- `browser_navigate` hits Cloudflare "Just a moment..." interstitials

This is a known, stable state — the block is consistent across all access methods.

## Recovery Pattern

Don't fight the block. Fall back to syndicated sources:

1. **`web_extract` first** — accept whatever it returns (even if truncated). It usually gets the first ~5,000 chars which covers the introduction and section headers.
2. **`web_search` for title + author** — e.g., `"Unrolling the Codex agent loop" Michael Bolin`
3. **Prioritize these syndication sources:**
   - `engineering.fyi` — full article reproductions with structured formatting
   - `arstechnica.com` — detailed summaries with direct quotes, useful for key technical details
   - `infoq.com` — architecture-focused recaps, good for protocol/API articles
   - `apollothirteen.com` — engineering deep-dives
   - `lqdev.me` — full article mirrors
4. **Combine sources** — the truncated `web_extract` output + one syndicated source usually covers 90%+ of the article content
5. **Save raw article** with `syndicated: true` and list the sources used

## Example

```
web_extract → truncated (intro + section headers only)
web_search → "Unrolling the Codex agent loop" Michael Bolin
web_extract → engineering.fyi/article/unrolling-the-codex-agent-loop (full content)
web_extract → arstechnica.com/ai/2026/01/openai-spills-technical-details (key quotes)
→ Combined into comprehensive raw article
```

## Do NOT

- Retry `curl` multiple times (same Cloudflare block)
- Retry `browser_navigate` (same interstitial)
- Use `browser_console` chunking (the page body is the Cloudflare challenge, not article content)
- Give up and work from memory alone — the syndicated sources are reliable and complete
