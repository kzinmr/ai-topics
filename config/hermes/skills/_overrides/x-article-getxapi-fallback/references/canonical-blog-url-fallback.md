# Canonical Blog URL Fallback for X Article Bookmarks

## When to Use This Pattern

When processing an X bookmark that has `article.title` but:
- `article.plain_text` is missing (fetch error)
- The `unwound_url` returns HTTP 500 or other error
- The article was originally published on the author's personal blog, Substack, Medium, or other canonical URL

**Do NOT use this for X-native long-form articles** (those only published on x.com/i/article/...). For those, use the GetXAPI Tier 3 or secondary source Tier 4 paths.

## The Pattern

X Articles are sometimes just wrappers/redirects to content the author published on their own site. The x.com/i/article/... URL is a forward, not the original. When the X article endpoint fails, skip it entirely and go to the source:

```python
# Step 1: Search for canonical URL
web_search(query='"<article.title>" <author name>')

# Step 2: web_extract the canonical URL (not the x.com wrapper)
web_extract(urls=["https://author-site.com/blog/post-slug"])
```

## Key Insight

**Most established tech bloggers cross-post to X Articles as a secondary channel, not their primary publishing platform.** If the author has a known domain (addyosmani.com, simonwillison.net, gwern.net, etc.), searching `"<title>" <author>` almost always returns the canonical URL as the top result.

## Real Example: Addy Osmani "Don't Outsource the Learning"

**Bookmark data:**
```json
{
  "article": {"title": "Don't Outsource the Learning"},
  "text": "https://t.co/jKCIAEzai7",
  "entities": {"urls": [{"unwound_url": "https://x.com/i/article/2055936913211899904", "status": 500}]}
}
```

**What failed:**
- xurl couldn't fetch article body (500 on unwound URL)
- No `article.plain_text` in the data

**What worked:**
```python
web_search(query='"Don\'t Outsource the Learning" AI agent article 2026')
# → First result: https://addyosmani.com/blog/dont-outsource-learning/
web_extract(urls=["https://addyosmani.com/blog/dont-outsource-learning/"])
# → Full article body with all sections, research citations, and quotes
```

**Result:** Complete raw article saved with original source URL (addyosmani.com), not the X wrapper. Wiki pages enriched with full research findings.

## When This Pattern Beats Other Approaches

| Approach | When it works | When it doesn't |
|----------|--------------|-----------------|
| xurl read (Tier 1) | Always gets metadata | Never gets body |
| web_extract tweet URL (Tier 2) | X renders preview | JS-rendered, truncated |
| GetXAPI (Tier 3) | X-native articles | Cross-posted content |
| **Canonical blog URL (this pattern)** | **Author has known blog** | X-native only, unknown author domain |
| Secondary sources (Tier 4) | News covers it | Niche/obscure content |

## Authors with Known Canonical Domains

When you see these authors in X bookmarks, skip the X article wrapper and go straight to their known domains:
- Addy Osmani → addyosmani.com
- Simon Willison → simonwillison.net
- Gwern Branwen → gwern.net
- Andrej Karpathy → karpathy.github.io
- Lilian Weng → lilianweng.github.io
- Xe Iaso → xeiaso.net
- Julia Evans → jvns.ca
- Dan Luu → danluu.com

**Discovery rule:** If the author has a known personal domain (check `entities/<author>.md` in the wiki), try `"<title>" site:<domain>` first.

## Pitfalls

- **Not all X Articles have canonical URLs.** Some content is X-native only. This pattern only works when the author is a known blogger who cross-posts.
- **The article might be slightly different on the canonical site** — X Articles sometimes have truncated or edited versions. The canonical URL is the authoritative version.
- **Don't assume the domain.** If you're not sure, use web_search first, not a guessed URL.
- **Paywalled canonical URLs** — Medium, Substack, and some personal blogs have paywalls. web_extract handles Medium paywalls reasonably well but Substack may truncate.
