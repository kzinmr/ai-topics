# Substack Custom Domain Bypass

## Problem

When `web_extract` or `curl` to `open.substack.com/pub/{handle}/p/{slug}` returns a **Cloudflare challenge page** ("Just a moment..."), the main Substack domain is protected. However, many publications have **custom domains** that bypass this protection.

## Working Pattern

1. **Identify the custom domain** from the publication's Substack settings or the `app-link/post` redirect chain
2. **Extract article body** via `<article>` tag from the custom domain URL
3. **JSON-LD** may still return metadata (headline, isAccessibleForFree, datePublished) even from blocked domains

## Confirmed Working Examples (June 2026)

| Publication | Main Domain (Blocked) | Custom Domain (Works) |
|-------------|----------------------|----------------------|
| AINews / Latent Space | `open.substack.com/pub/swyx/p/...` | `latent.space/p/...` |
| Import AI | `open.substack.com/pub/importai/p/...` | `importai.substack.com/p/...` (sometimes works) |

## Extraction Code

```python
import subprocess, re

# Try custom domain first when main domain is blocked
custom_url = "https://latent.space/p/ainews-frontiercode-benchmarking"
result = subprocess.run(
    ['curl', '-sL', '-A', 'Mozilla/5.0', custom_url],
    capture_output=True, text=True, timeout=20
)
html = result.stdout

# Extract article body
article = re.search(r'<article[^>]*>(.*?)</article>', html, re.DOTALL)
if article:
    paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', article.group(1), re.DOTALL)
    print(f"Article paragraphs: {len(paragraphs)}")
    for i, p in enumerate(paragraphs[:5]):
        text = re.sub(r'<[^>]+>', '', p).strip()
        if len(text) > 50:
            print(f"P{i+1}: {text[:300]}")
```

## When to Use

- `web_extract` returns "Just a moment..." on Substack URLs
- `open.substack.com` is Cloudflare-blocked
- The publication has a known custom domain (check `app-link/post` redirect chain or publication settings)

## Limitations

- Not all publications have custom domains
- Custom domains may still be paywalled (`isAccessibleForFree: false`)
- The `<article>` tag extraction works for free posts only; paywalled posts require section-heading extraction technique
