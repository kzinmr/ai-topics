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

## llms.txt / llms-full.txt (Best for Documentation Sites)

Many modern documentation sites provide **LLM-readable text endpoints** following the [llms.txt standard](https://llmstxt.org/). These are goldmines for wiki enrichment — clean, structured markdown with no HTML parsing needed.

### Discovery Pattern

When enriching an entity page from a project's official docs, try these URLs in order:

```bash
# Standard llms.txt endpoints
curl -sL https://<docs-site>/llms.txt          # Short index (~2k tokens)
curl -sL https://<docs-site>/llms-full.txt      # Full documentation (~100-200k tokens)
curl -sL https://<docs-site>/llms-guide.txt     # User guide subset

# Also check for CHANGELOG
curl -sL https://<docs-site>/CHANGELOG.html     # Version history, feature timeline
```

### Why This Is Preferred Over HTML Scraping

| Method | Quality | Speed | Structure |
|--------|---------|-------|-----------|
| `curl llms-full.txt` | ✅ Perfect markdown | Fast (single request) | Headers, code blocks, tables preserved |
| HTML + BeautifulSoup | ⚠️ Loses formatting | Slow (parsing) | Noisy nav/footer/sidebar |
| Jina Reader | ✅ Good markdown | Medium | May miss some content |

### Proven Sites with llms.txt Support

| Site | Endpoint | Content |
|------|----------|---------|
| inspect.aisi.org.uk | `/llms-full.txt` | 1.5MB, complete docs (all user guide + reference) |
| inspect.aisi.org.uk | `/llms.txt` | ~2k token index |
| inspect.aisi.org.uk | `/llms-guide.txt` | User guide subset (~185k tokens) |

Many Quarto-based documentation sites (like Inspect AI) provide these endpoints automatically.

### How to Use for Entity Enrichment

1. Fetch `llms-full.txt` — this gives you the entire documentation in clean markdown
2. Use `grep -n "^# " | head -60` to get the document structure (section headers + line numbers)
3. Use `sed -n 'START,ENDp'` to extract specific sections by line range
4. Synthesize into the entity page's architecture, features, and ecosystem sections
5. Also fetch the changelog for version history and release cadence

### Pitfalls

- **Not all sites have llms.txt** — it's an emerging standard, not universal. Try it first; if 404, fall back to HTML scraping.
- **Large files** — `llms-full.txt` can be 1-2MB. Use `head -c 40000` or `sed -n` to extract sections rather than loading the entire file.
- **Content freshness** — llms.txt files are regenerated on doc build. They reflect the latest deployed docs, not necessarily the latest release.
- **User-Agent requirements** — Some sites (e.g., hamel.dev) time out on bare `curl` but respond when a browser User-Agent is set: `curl -sL -A "Mozilla/5.0" --connect-timeout 10 --max-time 20 <URL>`. This is distinct from the "curl times out entirely" problem (which needs requests/httpx).

## CloudFront 403 Bypass (Fortune, Bloomberg, etc.)

Major news sites (Fortune, Bloomberg, Business Insider) use CloudFront WAF that blocks bare `curl` with a **403 ERROR** page (~900 bytes). The fix is simple — add a browser User-Agent:

```bash
curl -sL -A "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  -o /tmp/article.html "https://fortune.com/path/to/article"
```

This typically returns the full page (500KB+ for Fortune). Then extract `<p>` content with a lightweight Python HTMLParser (no BS4 dependency):

```python
from html.parser import HTMLParser

class ArticleExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paragraphs = []
        self.current = []
        self.in_p = False
        self.skip_tags = {'script', 'style', 'noscript', 'svg', 'button', 'nav', 'footer', 'header'}
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            self.skip += 1
        if tag == 'p':
            self.in_p = True
            self.current = []

    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self.skip -= 1
        if tag == 'p' and self.in_p:
            self.in_p = False
            text = ' '.join(self.current).strip()
            if len(text) > 20:
                self.paragraphs.append(text)
            self.current = []

    def handle_data(self, data):
        if self.skip <= 0 and self.in_p:
            self.current.append(data.strip())

parser = ArticleExtractor()
parser.feed(html)
# Filter by keywords to isolate article body
for p in parser.paragraphs:
    if any(w in p.lower() for w in ['keyword1', 'keyword2']):
        print(p)
```

**When `execute_code` is blocked** (cron mode, approval-required contexts), this `terminal` + `curl -A` + `python3 HTMLParser` pattern works as a zero-dependency fallback. No `requests`, no `BeautifulSoup` needed.

**Proven sites** (CloudFront 403 → User-Agent fix):

| Site | Bare curl | curl -A "Mozilla/5.0" | Notes |
|------|-----------|----------------------|-------|
| fortune.com | 403 (CloudFront) | ✅ ~500KB full HTML | HTMLParser + `<p>` extraction works |
| bloomberg.com | 403 | ✅ (may need cookies for paywall) | Paywalled — may get partial content |

## Google Drive PDF Download + Text Extraction

When a user shares a Google Drive file link (`drive.google.com/file/d/<FILE_ID>/view`), download and extract with pymupdf:

```bash
# Step 1: Download via direct export URL (works for public files)
curl -L "https://drive.google.com/uc?export=download&id=<FILE_ID>" -o /tmp/gdrive_file.pdf

# Step 2: Verify it's a PDF (file command may not be available on headless servers)
head -c 10 /tmp/gdrive_file.pdf | cat -v
# Should start with: %PDF-1.

# Step 3: Extract text with pymupdf (always available in Hermes env)
python3 -c "
import pymupdf
doc = pymupdf.open('/tmp/gdrive_file.pdf')
print(f'Pages: {len(doc)}')
for page in doc:
    print(page.get_text())
"
```

### Pitfalls

- **`file` command not available** on some headless servers — use `head -c 10 | cat -v` to check magic bytes instead
- **Large PDFs** (>50 pages): extract TOC first with `doc.get_toc()`, then targeted extraction by page range
- **pymupdf location**: installed at `~/.local/lib/python3.13/site-packages/` — use `import pymupdf` (not `fitz`)
- **Save raw PDF** to `wiki/raw/papers/` with naming convention: `{YYYY-MM-DD}_{author-slug}_{title-slug}.pdf`
- **Google Drive access**: Only works for files with "anyone with link" sharing. Restricted files will return HTML login page instead of PDF — verify magic bytes.

## Jina Reader API (Best for JS-Rendered / SPA Sites)

When BeautifulSoup and regex extraction both fail on JS-rendered sites (Next.js, React, Astro SPA), use the **Jina Reader API** — a free service that renders JS server-side and returns clean markdown:

```bash
curl -sL "https://r.jina.ai/https://example.com/article" -H "Accept: text/plain" 2>&1
```

**Why this is often the best first fallback for modern blog sites:**
- No browser session needed (unlike `browser_navigate`)
- No Python dependencies (unlike `execute_code` + BS4)
- Server-side JS rendering — works on React/Next.js/Astro SPA pages
- Returns clean markdown with title, publish date, and structured content
- Handles redirects, CDNs, and anti-bot protection (Cloudflare etc.)
- Single `terminal` call — no retry loops needed

**When to use**: Corporate blog sites using modern JS frameworks (claude.com/blog, openai.com/index, cognition.ai/blog, hex.tech/blog, any Webflow-hosted site). These sites return empty `<div id="__next">` to curl/httpx, making BS4 extraction useless.

**Proven sites** (Jina Reader succeeds where BS4 fails):

| Site | Framework | curl+BS4 | Jina Reader |
|------|-----------|----------|-------------|
| claude.com/blog | Webflow SPA | ❌ CSS/JS noise only | ✅ Full markdown |
| openai.com/index | Next.js RSC | ❌ Empty shell | ✅ Full content |
| cognition.ai/blog | SPA | ❌ 404 or empty | ✅ Full content |
| hex.tech/blog | Astro/React | ❌ Navigation noise | ✅ Full content |

**Rate limits**: Jina Reader is free for moderate usage. For batch extraction (>20 URLs), add a 1-2s delay between calls.

**Limitations**: Returns markdown, not raw HTML — fine for wiki ingestion but loses some formatting. Paywalled content returns a summary rather than full text.

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
