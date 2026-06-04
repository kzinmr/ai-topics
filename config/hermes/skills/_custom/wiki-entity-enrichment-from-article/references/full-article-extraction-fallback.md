# Full Article Extraction When web_extract Truncates

## Problem

`web_extract` (Hermes tool) often returns **summarized/truncated** content for long-form blog posts and technical articles. The truncation marker is:

```
[... summary truncated for context management ...]
```

This loses critical technical details (performance tables, architecture diagrams, code samples, training hyperparameters) needed for wiki ingestion.

## Fallback Strategy (preferred order)

### Tier 1: `execute_code` with `requests` + `BeautifulSoup`

```python
import requests
from bs4 import BeautifulSoup

resp = requests.get('https://example.com/article', timeout=30)
soup = BeautifulSoup(resp.text, 'html.parser')

# Find main content — try common selectors
article = soup.find('article')
if not article:
    article = soup.find('main')
if not article:
    article = soup.find('div', class_='prose')
if not article:
    article = soup.find('body')

# Extract structured text
for elem in article.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'pre', 'li', 'table', 'blockquote']):
    tag = elem.name
    text = elem.get_text().strip()
    if not text:
        continue
    if tag.startswith('h'):
        level = int(tag[1])
        print(f"\n{'#'*level} {text}")
    elif tag == 'pre':
        print(f"\n```\n{text}\n```")
    elif tag == 'li':
        print(f"- {text}")
    elif tag == 'blockquote':
        print(f"> {text}")
    else:
        print(f"\n{text}")
```

**Why this works when `curl` fails**: Python `requests` uses a more browser-like User-Agent and handles redirects/chunked encoding differently than `curl` in the terminal tool. Sites that timeout on `curl` (e.g., turbopuffer.com) often respond fine to `requests`.

### Tier 2: `browser_navigate` + `browser_snapshot`

If Chrome is installed (requires `agent-browser install`), use the browser stack:
- Navigate to the page → get accessibility tree snapshot
- Better for JS-rendered content

### Tier 3: Accept the truncated version

If neither fallback works, use the truncated `web_extract` content and note in the raw article: "Content truncated — full article not retrievable."

## When to Use This

Trigger: after the FIRST `web_extract` call for a substantive article (>3000 words), if the output contains the truncation marker, immediately switch to Tier 1. Don't waste turns on repeated `web_extract` calls — they will produce the same truncated result.

## Proven Sites

| Site | web_extract | execute_code+BS4 | Notes |
|------|-------------|------------------|-------|
| turbopuffer.com/blog | Truncated | ✅ Full | curl times out; requests works |
| Most personal blogs | Full | — | Usually no fallback needed |
| Substack | Varies | ✅ Full | JS-heavy but mostly SSR |
