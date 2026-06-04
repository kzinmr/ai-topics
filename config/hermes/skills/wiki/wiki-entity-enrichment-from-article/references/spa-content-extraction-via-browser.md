# SPA Content Extraction via Browser

## Problem

Many modern blogs and documentation sites use client-side rendering (React, Next.js, Remix, etc.). When you use `web_extract` or `curl`, you get back a minimal HTML shell without the actual article content — the full text is only rendered by JavaScript in the browser.

## Symptoms

- `web_extract` returns only a 1-2 sentence summary with metadata but no body
- `curl` returns a huge HTML shell but no article text
- JSON-LD metadata is present but the article body is absent
- The page content is loaded from a `.md` file or JS bundle at runtime

## Solution: browser_console + innerText

Instead of scrolling through truncated `browser_snapshot` output, use `browser_console` with a JavaScript expression to extract all text in one shot:

```
browser_navigate("https://example.com/blog/article")
browser_console(expression="document.querySelector('article').innerText")
```

This returns the complete article text in a single tool call with no truncation issues.

### Selector Fallbacks

If `'article'` doesn't work, try these in order:
- `document.querySelector('main').innerText`
- `document.querySelector('[class*="post"]').innerText`
- `document.querySelector('[class*="content"]').innerText`
- `document.querySelector('.prose').innerText`
- `document.querySelector('.markdown').innerText`

### When browser is unavailable

If `browser_navigate` returns "Chrome not found", install agent-browser:
```bash
node /opt/hermes/node_modules/agent-browser/bin/agent-browser.js install
```
The binary lives at `/opt/hermes/node_modules/agent-browser/bin/agent-browser.js` (bundled with Hermes).

## Example Session

**URL**: https://hornet.dev/blog/this-is-what-agentic-retrieval-looks-like
**Issue**: React Router SPA — `web_extract` returned only title + description, `curl` returned homepage HTML
**Fix**: `browser_navigate` → `browser_console(expression="document.querySelector('article').innerText")` → got complete 6-min-read article in one call
