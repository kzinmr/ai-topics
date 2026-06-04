# Substack Article Body Extraction via Raw HTML

When JSON-LD body_html is empty (common even for free articles), extract article text directly from the raw HTML via `<article>` tags or `<p>` paragraph filtering. Validated June 2026 against three Substack publications (Latent Space, Interconnects, Import AI).

## Approach 1: `<article>` Tag Extraction (Preferred)

Most Substack pages wrap the post content in an `<article>` tag. This works for both podcast transcript pages and written articles.

```python
import subprocess, re

result = subprocess.run(
    ["curl", "-sL", "https://open.substack.com/pub/{handle}/p/{slug}"],
    capture_output=True, text=True, timeout=20
)
html = result.stdout

m = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
if m:
    text = re.sub(r'<[^>]+>', ' ', m.group(1))
    text = re.sub(r'\s+', ' ', text).strip()
    # text now contains the full article body with HTML stripped
```

**What this captures**: Full article content including post body, podcast show notes, embedded X posts text, section headers, and links. May include some UI chrome (subscribe buttons, share buttons) at the bottom — but the main content is reliably in the `<article>` tag.

## Approach 2: `<p>` Paragraph Filtering (Fallback)

If `<article>` tag is not found, extract all `<p>` tags and filter to meaningful paragraphs:

```python
paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', html, re.DOTALL)
meaningful = [re.sub(r'<[^>]+>', '', p).strip() for p in paragraphs if len(p) > 50]
for p in meaningful[:40]:
    print(p)
```

**Threshold**: Filter to paragraphs with >50 chars to exclude navigation UI, footer text, and empty `<p>` tags.

## Approach 3: `available-content` Div

Some Substack layouts use `class="available-content"` for the free preview:

```python
m = re.search(r'class="available-content[^"]*"[^>]*>(.*?)</div>', html, re.DOTALL)
```

**Limitation**: Only captures the free preview section, not the full post. Useful for paywalled articles.

## Cron Mode Implementation

In cron mode (execute_code and pipe-to-interpreter are blocked):

```python
#!/usr/bin/env python3
# Save as /tmp/fetch_post_body.py
import subprocess, re, sys

url = sys.argv[1] if len(sys.argv) > 1 else "https://open.substack.com/pub/swyx/p/video-agents"
result = subprocess.run(["curl", "-sL", url], capture_output=True, text=True, timeout=20)
html = result.stdout

# Try <article> tag first
m = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
if m:
    text = re.sub(r'<[^>]+>', ' ', m.group(1))
    text = re.sub(r'\s+', ' ', text).strip()
    print(text[:5000])
    sys.exit(0)

# Fallback: <p> paragraph filtering
paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', html, re.DOTALL)
meaningful = [re.sub(r'<[^>]+>', '', p).strip() for p in paragraphs if len(p) > 50]
for p in meaningful[:40]:
    print(p[:200])
```

Run via: `terminal → python3 /tmp/fetch_post_body.py <url>`

## What to Expect

| Extraction Method | Reliability | Captures | Notes |
|-----------------|-------------|----------|-------|
| JSON-LD headline | Always | Title, author, date, paywall status | Use for metadata only |
| JSON-LD body_html | Often empty | Full body (when present) | Do not rely on |
| `<article>` tag | Reliable | Full post content | May include some UI chrome at bottom |
| `<p>` paragraph | Reliable | Clean text paragraphs | Filters navigation; good fallback |
| `available-content` | Partial | Free preview only | Use for paywalled articles |
