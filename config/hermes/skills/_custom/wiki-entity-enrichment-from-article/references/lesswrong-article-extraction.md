# LessWrong Article Extraction

LessWrong uses a React/Vulcan framework. Articles are NOT in static HTML — content lives as **unicode-escaped HTML inside large `<script>` tags** in the page source. This means BeautifulSoup and `web_extract` return nothing useful, but **a browser is NOT required** — plain `curl` + Python parsing works.

## Why This Matters

- Subagents with only `web`+`file` toolsets **cannot** fetch LessWrong articles (no browser, no terminal)
- The parent agent must handle LessWrong extraction directly via `terminal`
- Jina Reader (`r.jina.ai`) may work as an alternative but was not tested for LessWrong

## Extraction Workflow (curl + Python)

### Step 1: Find the Article URL

```bash
curl -sL --max-time 15 "https://search.brave.com/search?q=lesswrong+%22ARTICLE_TITLE%22" 2>/dev/null \
  | grep -oP 'https?://[^"]*lesswrong[^"]*posts[^"]*' | head -5
```

Brave Search works reliably for LessWrong article discovery. DuckDuckGo and Google are less consistent.

### Step 2: Fetch and Extract

```python
import re, json

# Fetch HTML
import subprocess
result = subprocess.run(
    ['curl', '-sL', '--max-time', '30', URL],
    capture_output=True, text=True
)
raw = result.stdout

# Extract all script tags
scripts = re.findall(r'<script[^>]*>(.*?)</script>', raw, re.DOTALL)

# Find the large script containing article content (~100-200K)
# Search for target keyword to identify the right script
target_script = None
for s in scripts:
    if 'TARGET_KEYWORD' in s.lower() and len(s) > 10000:
        target_script = s
        break

# Extract content: find keyword occurrences, get surrounding chunk
indices = [m.start() for m in re.finditer(r'TARGET_KEYWORD', target_script, re.IGNORECASE)]
start = max(0, indices[0] - 5000)  # before first mention
end = min(len(target_script), indices[-1] + 15000)  # after last mention
chunk = target_script[start:end]

# Decode unicode escapes
chunk = chunk.encode().decode('unicode_escape', errors='replace')

# Strip HTML tags
chunk = re.sub(r'<[^>]+>', '\n', chunk)
chunk = re.sub(r'\n{3,}', '\n\n', chunk)
```

### Step 3: Extract Metadata

Metadata is embedded as JSON in the same script:

```python
# Author
author_match = re.search(r'"displayName":"([^"]+)"', target_script)
# Date
posted_match = re.search(r'"postedAt":"([^"]+)"', target_script)
# Karma/score
score_match = re.search(r'"baseScore":(\d+)', target_script)
# Word count
wc_match = re.search(r'"wordCount":(\d+)', target_script)
```

### Step 4: Save as Raw Article

Standard YAML frontmatter:

```yaml
---
title: "Article Title"
source_url: "https://www.lesswrong.com/posts/SLUG/TITLE-SLUG"
author: "display_name"
date: YYYY-MM-DD
source: "LessWrong"
scraped_date: YYYY-MM-DD
tags: [tag1, tag2]
word_count: NNNN
---
```

Filename: `YYYY-MM-DD_lesswrong-author-slug.md`

## Pitfalls

- **Unicode escapes**: LessWrong content uses `\u003c` for `<`, `\u003e` for `>`, `\u0026` for `&`. Decode with `.encode().decode('unicode_escape', errors='replace')`.
- **Multiple script tags**: The page has 100+ script tags. The article content is in the largest one (~100-200K). Filter by length AND keyword presence.
- **Content is HTML within JSON**: After unicode decoding, you still need to strip HTML tags (`<p>`, `<li>`, `<h2>`, `<a>`, etc.).
- **Search the full script for metadata**: `postedAt`, `displayName`, `baseScore`, `wordCount` are in the same script blob but may be far from the article content.
- **Subagent delegation fails**: Delegates with `web`+`file` toolsets cannot run `curl` or `terminal`. Always use `terminal` directly in the parent session for LessWrong.
- **Article slug vs search slug**: LessWrong URL slugs sometimes differ from the search result slug. Use the full URL from Brave search results.
- **Brave Search blocked in some environments**: If Brave returns empty, try `curl -sL "https://www.bing.com/search?q=..."` as fallback.
