# Next.js SSR Content Extraction

Next.js sites with SSR (Server-Side Rendering) often serve full article content in the initial HTML, making browser tools unnecessary.

## Pattern

Next.js SSR pages contain article content in two places:
1. **HTML body** — the rendered content in standard HTML tags
2. **`__NEXT_DATA__` JSON** — a `<script id="__NEXT_DATA__">` tag containing the page props as JSON

## Extraction Strategy

**Simplest approach**: Use `curl` + BeautifulSoup to extract from the HTML body directly.

```python
import requests
from bs4 import BeautifulSoup

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Most blog-style Next.js sites put content in a div with id="content" or class="prose"
content_div = soup.find('div', {'id': 'content'}) or soup.find('div', class_='prose')
if content_div:
    paragraphs = content_div.find_all(['p', 'h1', 'h2', 'h3', 'li'])
    text = '\n\n'.join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
```

**Fallback**: If the HTML body is empty or minimal (true SPA), extract from `__NEXT_DATA__`:

```python
import json

script = soup.find('script', {'id': '__NEXT_DATA__'})
if script:
    data = json.loads(script.string)
    # Content is typically in data['props']['pageProps']
    content = data['props']['pageProps'].get('content', '')
```

## Known Working Sites

| Site | SSR? | Extraction Method |
|------|------|-------------------|
| calv.info | Yes (SSR) | HTML body, `div#content` |
| Next.js blogs with `getStaticProps` | Usually yes | HTML body |
| Next.js blogs with client-side fetch | No (SPA) | `__NEXT_DATA__` or browser |

## When to Use Browser Instead

Use browser tools (delegate_task with `browser` toolset) when:
- Content is behind authentication
- Content requires JavaScript execution to render (true SPA without SSR)
- Content is in a non-standard format that BeautifulSoup can't parse
- Site blocks curl/requests (403, Cloudflare challenge)

## Historical Incidents

- **2026-06-17**: calv.info/openai-reflections — Full article extracted via curl + BeautifulSoup from HTML body. `div#content` contained all paragraphs. No browser needed despite Next.js framework.
