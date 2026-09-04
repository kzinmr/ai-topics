# Framer SPA Content Extraction

Sites built with **Framer** (website builder) embed article content in a **search index JSON file**, not in the HTML. Neither Jina Reader nor BeautifulSoup can extract the article body — they get only navigation and footer.

## Discovery

Framer sites load content via `<script>` tags containing `__framer_handoverData` JSON or a separate `searchIndex-*.json` file. The content is rich-text AST, not HTML.

## Extraction Pattern

1. **Fetch the page HTML** with `curl -sL`
2. **Find the search index JSON**: grep for URLs matching `searchIndex-*.json` in the HTML source
3. **Download the JSON** and parse it — the `body` field contains rich-text blocks with `type: "paragraph"`, `type: "heading"`, etc.
4. **Convert to markdown** by walking the AST:

```python
import json, re

# After finding the search index URL in the HTML source
json_data = json.loads(json_content)

blocks = []
for item in json_data.get("items", []):
    body = item.get("body", [])
    for block in body:
        btype = block.get("type", "")
        text_parts = []
        for span in block.get("spans", []):
            text_parts.append(span.get("text", ""))
        text = "".join(text_parts)
        if btype == "heading":
            blocks.append(f"## {text}")
        elif btype == "paragraph":
            blocks.append(text)

print("\n\n".join(blocks))
```

## Proven Sites (Framer SPA)

| Site | curl+BS4 | Jina Reader | Search Index JSON |
|------|----------|-------------|-------------------|
| pioneer.ai/blog/* | ❌ Nav noise only | ❌ Footer only | ✅ Full article content |
| fastino.ai | ❌ | ❌ | ✅ |

## Why Jina Reader Fails on Framer

Framer renders content client-side from JSON data — the HTML shell has no article text. Jina Reader's server-side rendering follows the same empty HTML. The actual content lives in a separate JSON endpoint that must be discovered and fetched directly.

## Subagent Delegation Pattern

When encountering a Framer site, delegate to a subagent with clear instructions:

```
goal: "Fetch the full text of this blog article. The site uses Framer (JS-rendered SPA).
      Find the searchIndex-*.json URL in the page source, download it, and parse the
      rich-text body blocks into markdown."
toolsets: ["web", "terminal"]
```

The subagent needs `terminal` access for `curl` + `python3` JSON parsing. `web` alone won't work.
