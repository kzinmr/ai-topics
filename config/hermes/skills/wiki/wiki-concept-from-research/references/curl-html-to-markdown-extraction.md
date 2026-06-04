# curl/httpx + Regex HTML-to-Markdown Extraction

Fallback method for extracting full article text from **static blogs** (Jekyll, Hugo, Astro, GitHub Pages, etc.) when `web_extract` times out with `LLM summarization timed out` and `browser_navigate` is unavailable.

This is the second-choice path in the extraction chain: `web_extract → execute_code(httpx+regex) → browser_navigate`.

## When to Use

- `web_extract` returns `LLM summarization timed out` (content > 5,000 chars)
- `browser_navigate` fails (no Chrome: `agent-browser install` blocked or absent)
- The target site is a **static blog** serving full HTML content (Jekyll, Hugo, Astro, GitHub Pages)

## Preferred: httpx via execute_code (try FIRST)

The `subprocess curl` approach often times out. Use `execute_code` with `httpx` instead — Python-native HTTP client with better timeout handling:

```python
import httpx
import re

url = "https://example.com/blog-post/"
resp = httpx.get(url, timeout=30, follow_redirects=True)
html = resp.text

# Remove non-content elements
for tag in ['script', 'style', 'nav', 'header', 'footer']:
    html = re.sub(f'<{tag}[^>]*>.*?</{tag}>', '', html, flags=re.DOTALL)

# Extract main content area
article_match = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
if not article_match:
    article_match = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
text = article_match.group(1) if article_match else html

# Strip remaining HTML tags
text = re.sub(r'<[^>]+>', '\n', text)
import html as html_lib
text = html_lib.unescape(text)  # decode &amp; &gt; &lt; etc.
text = re.sub(r'\n{3,}', '\n\n', text)
text = re.sub(r'[ \t]+', ' ', text)
text = text.strip()

print(f"Length: {len(text)} chars")
print(text[:12000])
```

### Simple tag-stripping vs full markdown conversion

For **raw article saving**, the simple approach above (strip all tags, clean whitespace) is sufficient — the article text is preserved in readable form. Full markdown conversion (headings, links, code blocks) is only needed when the output will be directly embedded in concept pages. For most wiki ingestion, the simple approach works and avoids complex regex bugs.

## Verification Checklist

After extraction, verify the output:
- [ ] Title appears as `# Heading`
- [ ] Section headings are `##` / `###` 
- [ ] Links are `[text](url)` format
- [ ] No raw HTML tags remain (no `<div>`, `<span>`, `<a href=...>`)
- [ ] Length ratio: extracted content should be ~80-95% of the original HTML body size
- [ ] Code blocks use triple backtick fencing

## Limitations

- **JS-rendered sites** (React, Next.js): `curl` returns empty `<body>`. Don't use this for Next.js/React sites — fall back to `web_search` for secondary coverage.
- **HTML entities**: `&amp;` `&gt;` `&lt;` `&quot;` are NOT decoded by this approach. Most remain readable, but `&amp;` in URLs will break links.
- **Nested lists, tables, complex formatting**: The regex-based approach handles common blog patterns but not deeply nested structures.
- **Image alt text**: Images are stripped entirely — alt text is lost.

## Known-Good Targets

This approach has been validated on:
- **GitHub Pages (Jekyll)**: `rlancemartin.github.io` — full extraction of 16,677-char article
- **Hugo**: Works for most Hugo blogs with standard `<article>` wrappers
- **Astro**: Works for Astro blogs with `<article>` content

## Integration with the Pipeline

Use the extracted content to:
1. Save to `wiki/raw/articles/` as a complete raw article
2. Use as source material for concept page enrichment
3. Cross-reference against any partial `web_extract` output for fact-checking
