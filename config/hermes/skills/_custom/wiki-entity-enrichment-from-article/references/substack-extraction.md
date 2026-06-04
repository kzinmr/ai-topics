# Substack Article Extraction

`web_extract` often produces garbled/unreadable content for Substack articles. Use `curl` + Python HTML extraction instead.

## Extraction Pattern

### Step 1: Download the raw HTML
```bash
curl -sL -H 'User-Agent: Mozilla/5.0' '<URL>' -o /tmp/substack.html
```

### Step 2: Extract body content with Python
```python
import re, html as html_mod

with open("/tmp/substack.html") as f:
    html = f.read()

# Substack wraps article body in: <div dir="auto" class="body markup">
match = re.search(r'<div dir="auto" class="body markup">(.*?)<div class="visibility-check"></div>', html, re.DOTALL)
if match:
    body = match.group(1)
    # Strip script/style/svg
    body = re.sub(r'<script[^>]*>.*?</script>', '', body, flags=re.DOTALL)
    body = re.sub(r'<style[^>]*>.*?</style>', '', body, flags=re.DOTALL)
    body = re.sub(r'<svg[^>]*>.*?</svg>', '', body, flags=re.DOTALL)
    # Replace <a> tags with [text](url)
    def replace_link(m):
        href = re.search(r'href="([^"]+)"', m.group(0))
        text = re.sub(r'<[^>]+>', '', m.group(0))
        if href:
            return f'[{text}]({href.group(1)})'
        return text
    body = re.sub(r'<a[^>]*>.*?</a>', replace_link, body, flags=re.DOTALL)
    # Strip all remaining HTML tags
    body = re.sub(r'<[^>]+>', '', body)
    # Decode HTML entities
    body = html_mod.unescape(body)
    # Insert newlines between concatenated sections
    body = re.sub(r'(Retrieval\.)(This week)', r'\1\n\n\2', body)
    body = re.sub(r'(\[)(\d+\])', r'\n\n[\2]', body)  # Split paper sections
    body = re.sub(r'\n{3,}', '\n\n', body)
    body = body.strip()
```

### Step 3: Save with frontmatter
Follow `raw-article-filename-policy` for naming (`YYYY-MM-DD_domain_topic-slug.md`).

## Pitfalls
- Substack HTML body often has **no newlines** — all text concatenated. Use `[N]` section markers or regex patterns to split.
- `web_extract` is unreliable for Substack — always fall back to curl.
- The `<div class="visibility-check"></div>` marker reliably identifies the end of the article body (before the paywall/subscribe section).
- Substack newsletter posts (like RecSys) include multiple paper summaries — extract the full body, then focus on the papers relevant to the task.
