# Databricks Gatsby Blog Extraction

Databricks blogs use **Gatsby 5** (SSR with heavy CSS). `curl` returns the full HTML but ~90% is `<style>` tag CSS bloat (Tailwind + Marketo forms). The article content is embedded inline in the page, not in a `<script>` RSC payload.

## Pattern (terminal + python3 inline)

```bash
curl -sL "https://www.databricks.com/blog/ARTICLE-SLUG" | python3 -c "
import sys, re
html = sys.stdin.read()
html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL)
html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL)
text = re.sub(r'<[^>]+>', ' ', html)
text = re.sub(r'\s+', ' ', text).strip()
# Find article start by title keyword
start = text.find('KEYWORD')
if start > 0:
    text = text[start:]
print(text[:15000])
"
```

## Key Points

- Remove `<script>` and `<style>` tags first — Databricks pages have 50KB+ of CSS
- Article text starts after the nav/menu boilerplate; find by title keyword
- Meta tags (`article:published_time`, `og:description`) are reliable for metadata
- First pass returns ~15K chars; call again with a later keyword for the remainder
- This is NOT an SPA — the content IS in the HTML, just buried under CSS
- Gatsby version confirmed: 5.15.0 (as of May 2026)

## Proven On

- `databricks.com/blog/memex-programmable-scratchpad-llm-agents` (May 2026)

## When to Use

Use this pattern instead of Jina Reader or browser when:
- The curl response contains actual HTML content (not an empty shell)
- The page has massive CSS/inline styles making BeautifulSoup slow
- You need a fast, dependency-free extraction
