# Content Extraction Fallback Strategies

When ingesting web articles for wiki raw/article creation, content extraction tools have varying reliability.
This reference documents the fallback chain and failure modes observed in practice.

## Tool Chain (in priority order)

| Priority | Tool | Best for | Failure mode |
|----------|------|----------|-------------|
| 1 | `web_extract` | Quick article extraction with LLM summarization | Truncation at ~5,000 chars when auxiliary LLM times out |
| 2 | `browser_navigate` + `browser_console` (`document.body.innerText`) | Full browser-rendered text without summarization | 2-3 round trips for large docs; loses formatting |
| 3 | `browser_snapshot` (full=true) | Accessibility tree extraction | Truncation at ~8,000 chars |
| 4 | `execute_code` + `httpx` + `BeautifulSoup` | Reliable full-text extraction (no summarization) | Requires Python dependencies; slower than web_extract |

## Fallback Pattern (Python)

When `web_extract` truncates content, use `execute_code` with:

```python
import httpx
from bs4 import BeautifulSoup

url = "https://example.com/article"
resp = httpx.get(url, timeout=15)
soup = BeautifulSoup(resp.text, 'html.parser')

article = soup.find('article') or soup.find('main') or soup.find('div', class_='post') or soup
text = article.get_text(separator='\n', strip=True)
print(text[:10000])  # Adjust limit as needed
```

### Key Points
- Use `separator='\n'` to preserve paragraph breaks
- `strip=True` removes excessive whitespace
- Fallback chain for content container: `article` → `main` → `div.post` → entire `soup`
- Set timeout explicitly (15s is reasonable)
- Print to stdout; execute_code captures it in `output` field

## Browser Console Full-Text Extraction via innerText

When `browser_navigate` loads a page successfully but `browser_snapshot` (full=true) truncates
content, use `browser_console` to extract the full text directly from the DOM:

```js
document.body.innerText.substring(0, 15000)
```

Then call again with higher offsets for remaining content:
```js
document.body.innerText.substring(15000)
```

**When to use**: Google Slides `/htmlpresent` (see `google-slides-ingestion.md`), documentation
pages with lots of rendered text, or any page where the accessibility snapshot is truncated but
the DOM holds the full content.

**Advantages**: Reliable full-text capture from browser-rendered pages. No LLM summarization
risk. Works for any page, not just articles.

**Disadvantages**: 2-3 round trips for large documents. Loses formatting. Requires a browser
session (overhead vs. curl/httpx).

**Order in fallback chain**: After `web_extract` fails (truncation), try this before
falling back to `execute_code` + `httpx`. For Google Slides specifically, prefer
`/export/txt` first (see `google-slides-ingestion.md`), then this as fallback.

## When browser_navigate Also Fails

If both `web_extract` and `browser_navigate` fail (e.g., Chrome not installed), skip
directly to `execute_code` + `httpx` — don't keep retrying the broken tools.

## Pre-commit Tag Validator

The `.githooks/pre-commit-tag-validator.py` hook scans ALL staged files, not just your changes.
If unrelated files have pre-existing tag taxonomy violations, the commit will be blocked.

Per `AGENTS.md`: use `git commit --no-verify` as a last resort for "residual noise that can't
be added to the tag taxonomy." Ensure your own files use SCHEMA.md tags.

## JS-Rendered / RSC Payload Extraction

When a page is JS-rendered (Next.js, React), BeautifulSoup's `get_text()` returns mostly navigation
noise. The actual article content is often embedded in React Server Component (RSC) payloads inside
`<script>` tags. Use this technique:

```python
import httpx, re

resp = httpx.get(url, timeout=30, headers={"User-Agent": "Mozilla/5.0"})
html = resp.text

# Remove script, style, nav, header, footer noise first
html = re.sub(r'<(script|style|nav|header|footer)\b[^>]*>.*?</\1>', '', html, flags=re.DOTALL)

# Extract tagged text blocks directly (don't use .get_text() on whole document)
blocks = []
for tag in ['p', 'h1', 'h2', 'h3', 'h4', 'li', 'pre', 'code', 'blockquote']:
    for m in re.finditer(f'<{tag}\\b[^>]*>(.*?)</{tag}>', html, re.DOTALL):
        text = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        text = text.replace('&#x27;', "'").replace('&quot;', '"').replace('&amp;', '&')
        text = text.replace('&lt;', '<').replace('&gt;', '>').replace('&#x2F;', '/')
        if len(text) > 5:
            blocks.append((tag, text))

# Filter navigation/sidebar noise with a skip list
skip_starts = ['Login', 'Navigation Menu', 'Sign in', 'START TRAINING', ...]
filtered = [(tag, text) for tag, text in blocks 
            if not any(text.startswith(s) for s in skip_starts)]

# Build markdown: h1→#, h2→##, p→paragraph, pre→```, li→-
```

### Key Points
- Extract tagged text blocks from raw HTML, NOT `.get_text()` on the whole document
- Decode HTML entities (`&#x27;`, `&quot;`, `&amp;`, `&lt;`, `&gt;`) into plain text
- Use a `skip_starts` list to filter navigation/sidebar noise
- Prefer this over BeautifulSoup for JS-rendered pages where soup parsing produces navigation soup
- For the publication date: check `<meta property="article:published_time">`, JSON-LD, and visible "Published" text before falling back to the page content date

## Regex-Only Extraction (No External Dependencies)

When BeautifulSoup is not available (or undesirable), use `httpx` + `re` only. This works well
for simple blog pages (like Addy Osmani's, Xe Iaso's, etc.) and avoids the BS4 dependency:

```python
import httpx, re

resp = httpx.get(url, follow_redirects=True, timeout=30)
html = resp.text

# Strip non-content elements
for tag in ['script', 'style', 'nav', 'header', 'footer']:
    html = re.sub(f'<{tag}[^>]*>.*?</{tag}>', '', html, flags=re.DOTALL)

# Strip all remaining HTML tags and decode entities
text = re.sub(r'<br\s*/?>', '\n', html)
text = re.sub(r'<li[^>]*>', '\n• ', text)
text = re.sub(r'<[^>]+>', '', text)
text = text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
text = text.replace('&quot;', '"').replace('&#39;', "'")
text = text.replace('&mdash;', '—').replace('&ndash;', '–')

# Remove excessive blank lines
text = re.sub(r'\n{3,}', '\n\n', text)

# Trim to content by finding the blog title
lines = text.split('\n')
for i, line in enumerate(lines):
    if title_keyword in line.strip():  # e.g., 'Cognitive Surrender'
        text = '\n'.join(lines[i:])
        break

print(text[:20000])
```

This approach was validated on `addyosmani.com/blog/cognitive-surrender/` (16K chars, extracted
fully in 0.66s) and works reliably for straightforward blog templates. Skip it for JS-rendered
pages — use the tagged-text-block extraction above instead.

## Raw Article Quality: Replace Summaries with Full Content

> **⚠️ IMPORTANT**: Before creating a concept page from an existing raw article, verify the raw
> article contains the FULL original content — not a brief LLM summary.

Many raw articles in `wiki/raw/articles/` were ingested via pipeline scripts that used
`web_extract` which truncates at ~5,000 chars. These are often **brief summaries** (40-50 lines)
rather than the complete article. When you find such a summary:

1. **Extract the full article** using one of the fallback methods above
2. **Replace the raw article file** entirely — bump its `scraped` date, keep the same filename
3. **Then create/enrich the concept page** from the complete content

Example: `raw/articles/2026-05-05_addyosmani_cognitive-surrender.md` was 41 lines (summary).
Replaced with full 16K article before creating `concepts/cognitive-surrender.md`.

The concept page quality depends directly on raw article completeness. Don't build on summaries.
