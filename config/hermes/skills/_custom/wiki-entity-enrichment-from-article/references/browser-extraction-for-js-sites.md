# Browser-Based Article Extraction for JS-Heavy Sites

When `web_extract` returns only navigation/skeleton content from JavaScript-rendered sites (e.g., Galileo blog, many corporate blogs), fall back to browser-based extraction.

## Detection

`web_extract` returns a title/content mismatch — the title matches the URL but the content is only site navigation, footer links, or a sitemap rather than the article body. You'll see things like "Platform / Docs / Pricing / Resources / About" instead of the expected article text.

## Workflow

### 1. Navigate with Browser

```python
browser_navigate(url="https://example.com/blog/article-slug")
```

### 2. Extract Full Text via Console

Use `browser_console` with a JavaScript expression to pull the article body:

```javascript
document.querySelector('article, main, .post-content, .blog-content, .prose')?.innerText || document.body.innerText
```

This tries several common article container selectors before falling back to `document.body.innerText`.

### 3. Alternative: Full Snapshot

If the console approach doesn't work well, use `browser_snapshot(full=true)` to get the full accessibility tree. This can be very large but contains all text content.

## Pitfalls

- **Don't use `browser_snapshot` blindly**: For articles, the console approach is usually cleaner and faster. Use snapshot as a fallback.
- **Don't spend browser budget on non-wiki-worthy articles**: Evaluate wiki-worthiness first (from the tweet text + link titles) before opening the browser.
- **Some sites have anti-bot protection**: If the browser page shows CAPTCHAs or blank pages, the article may not be extractable. Note it and move on.
- **Large snapshots**: `browser_snapshot(full=true)` on long articles can produce 10K+ lines of output. Use the console approach for cleaner article text.

## Example

Galileo blog (May 2026): `web_extract` returned only the site sitemap. `browser_navigate` + `browser_console` with `document.querySelector('article')?.innerText || document.body.innerText` extracted the full 4,000-word article text cleanly.
