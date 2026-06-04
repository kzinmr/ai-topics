# web_extract Truncation Workaround

## Problem

`web_extract` summarizes pages over ~5000 characters via LLM, losing detail from long technical articles. The summary may miss critical code examples, nuanced arguments, or complete section structures.

## Detection

If `len(content) < 2000` or the article seems to cut off mid-argument, it's likely truncated.

## Workaround: curl + Python HTML Stripping

```python
import subprocess, re

# Fetch full HTML
result = subprocess.run(
    ["curl", "-sL", "https://example.com/article/"],
    capture_output=True, text=True, timeout=15
)
html = result.stdout

# Extract body (adjust regex to match the site's structure)
body_match = re.search(r'<article.*?>(.*?)</article>', html, re.DOTALL)
body = body_match.group(1) if body_match else html

# Strip HTML tags
body = re.sub(r'<pre[^>]*>.*?</pre>', 
    lambda m: '\n```\n' + re.sub(r'<[^>]*>', '', m.group(0)) + '\n```\n', 
    body, flags=re.DOTALL)
body = re.sub(r'<code>(.*?)</code>', r'`\1`', body)
body = re.sub(r'<[^>]*>', ' ', body)
body = re.sub(r'&amp;', '&', body)
body = re.sub(r'&lt;', '<', body)
body = re.sub(r'&gt;', '>', body)
body = re.sub(r'&quot;', '"', body)
body = re.sub(r'&#39;', "'", body)
body = re.sub(r'\n\s*\n\s*\n+', '\n\n', body)
body = body.strip()
```

## Site-Specific Patterns

| Site | Content Container |
|------|-------------------|
| `lucumr.pocoo.org` | `<article>...</article>` |
| `simonwillison.net` | `<div class="entry-content">...</div>` |
| Substack | `<div class="body">...</div>` |
| Medium | `<article>...</article>` |

## Fallback

If curl+regex fails, use the truncated LLM summary as-is. The summary is still useful for quick understanding, just incomplete for full extraction.
