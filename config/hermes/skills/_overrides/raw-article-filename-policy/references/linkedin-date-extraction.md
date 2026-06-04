# LinkedIn Post Date Extraction

LinkedIn posts embed their publication date in JSON-LD structured data with `@type: SocialMediaPosting`. This is the most reliable method.

## Extraction Pattern

```python
import urllib.request, re, json

url = "https://www.linkedin.com/posts/{handle}_{slug}-activity-{activity_id}-{hash}"
req = urllib.request.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
    "Accept": "text/html,application/xhtml+xml"
})
resp = urllib.request.urlopen(req, timeout=15)
html = resp.read().decode("utf-8")

# Extract JSON-LD SocialMediaPosting
for m in re.finditer(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', html, re.DOTALL):
    try:
        ld = json.loads(m.group(1))
        if isinstance(ld, dict):
            # LinkedIn wraps in a @graph array or single object
            items = ld.get('@graph', [ld])
            if not isinstance(items, list):
                items = [items]
            for item in items:
                if item.get('@type') == 'SocialMediaPosting':
                    date_str = item.get('datePublished')  # ISO 8601 format
                    print(f"Published: {date_str}")
                    # Extract just the date part
                    date_only = date_str[:10]  # "2026-04-21"
                    return date_only
    except (json.JSONDecodeError, KeyError):
        pass
```

## Key Fields

| JSON-LD Path | Format | Example |
|---|---|---|
| `datePublished` | ISO 8601 with milliseconds | `2026-04-21T02:12:01.055Z` |
| `headline` | Plain text | `"Don't waste too much time on the original RAG paradigm."` |
| `@id` | URL | `https://www.linkedin.com/posts/...` |

## Activity ID Caution

LinkedIn URLs contain an activity ID (e.g., `activity-7452177290798686208`), but **do not attempt to extract a timestamp from it** — LinkedIn uses a non-standard encoding, not the Snowflake format. Always use JSON-LD `datePublished` instead.

## LinkedIn Article vs LinkedIn Post

- **LinkedIn Posts** (short-form, like this session's target): Use `@type: SocialMediaPosting` → `datePublished`
- **LinkedIn Articles** (long-form, rarely encountered): These have a different template; check for `article:published_time` meta tags or the byline date text

## Source Slug Convention

For LinkedIn posts used as raw articles:
- `source-slug` = the LinkedIn handle without `@` (e.g., `softwaredoug`)
- Same convention as X/Twitter handles in the filename policy
- Example: `2026-04-21_softwaredoug_dont-waste-time-on-rag-paradigm.md`
