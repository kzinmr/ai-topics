# Medium Article Extraction via RSS (Gzip Recovery)

When `web_extract` returns gzip-compressed or reconstructed content for Medium articles,
the RSS feed provides the full uncompressed HTML under `<content:encoded>` with accurate
`<pubDate>` timestamps.

## When to Use

- `web_extract` returns content like: *"The provided content was compressed (gzip) and not fully readable..."*
- `web_extract` returns a brief summary/reconstruction instead of the full article
- You need the exact publication date (RSS `<pubDate>` is authoritative)

## Workflow

### Step 1: Discover the RSS feed URL

Medium blogs use the pattern: `https://username.medium.com/feed`

```bash
# For User-Hosted (username.medium.com):
curl -sI "https://dtunkelang.medium.com/feed" | head -3
# HTTP/2 200, content-type: text/xml

# For Publication-Hosted (medium.com/publication-name):
curl -sI "https://medium.com/feed/publication-name" | head -3
```

### Step 2: Extract the target article from RSS

```bash
# Find the article entry with context (5 lines before, 15 after)
curl -s "https://username.medium.com/feed" | grep -B5 -A15 "article-url-slug"
```

This returns:
- `<pubDate>` — authoritative publication date (e.g., `Thu, 26 Mar 2026 13:01:00 GMT`)
- `<atom:updated>` — ISO 8601 timestamp (e.g., `2026-03-26T13:01:00.699Z`)
- `<content:encoded>` — full article HTML with links, formatting, images
- `<category>` — Medium tags applied to the article
- `<dc:creator>` — author name

### Step 3: Extract `<content:encoded>` body for raw article

The `<content:encoded>` field is HTML-wrapped in CDATA. Parse it out and convert to markdown:

```python
import re

# Extract content:encoded from RSS item
match = re.search(r'<content:encoded><!\[CDATA\[(.*?)\]\]></content:encoded>', rss_item, re.DOTALL)
html_body = match.group(1)

# Basic HTML → markdown conversion:
# - Strip <img> tags (tracking pixels)
# - Convert <h3> → ###, <h4> → ####
# - Convert <p> → paragraph
# - Convert <a href="X">text</a> → [text](X)
# - Convert <ul>/<li> → markdown lists
# - Convert <strong> → **text**
# - Convert <em> → *text*
```

### Step 4: Determine publication date

The RSS `<pubDate>` is authoritative — use it as the `date:` in raw article filename and frontmatter:

```python
from datetime import datetime
pubdate = "Thu, 26 Mar 2026 13:01:00 GMT"
dt = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
date_str = dt.strftime("%Y-%m-%d")  # → "2026-03-26"
```

## Real Example

**Article**: "Agentic Search as an Agile Engineering Process"
- URL: `https://dtunkelang.medium.com/agentic-search-as-an-agile-engineering-process-5514b0790e8e`
- `web_extract` returned: reconstructed summary, lost full content
- RSS feed at `https://dtunkelang.medium.com/feed` returned full 5,000+ word article
- pubDate: `Thu, 26 Mar 2026 13:01:00 GMT` → filename: `2026-03-26_daniel-tunkelang_agentic-search-agile-engineering.md`
- Co-author discovered: Asif Makhani (only visible in full `<content:encoded>` body, lost in `web_extract` summary)

## Pitfalls

- **RSS returns only the 10–15 most recent articles** — older articles won't be in the feed. For historical Medium articles, use browser or curl the page directly.
- **Co-authors may only appear in full body text** — `web_extract` summaries often drop byline details
- **Medium tracking pixels**: `<img>` tags with `medium.com/_/stat` are tracking, not content — strip them
- **RSS `<content:encoded>` is HTML**: Needs HTML→markdown conversion for raw article storage. Use regex, not BeautifulSoup, to keep dependencies minimal.
- **Publication-hosted Medium blogs** (e.g., `medium.com/towards-data-science`) use a different RSS pattern: `https://medium.com/feed/publication-name`
