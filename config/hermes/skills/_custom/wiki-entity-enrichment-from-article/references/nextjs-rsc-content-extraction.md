# Next.js RSC (React Server Components) Content Extraction

## Problem

Next.js App Router sites (2024+) use RSC payloads — content is embedded inline in `<script>` tags as serialized React component trees, NOT in the HTML body. A `curl` fetch returns a 100KB+ page with the actual article text buried inside `self.__next_f.push([1,"..."])` script tags. Standard `grep` on the raw HTML finds nothing because quotes are escaped as `\"` and special characters use Unicode escapes.

**Detection**: HTML contains `self.__next_f.push([1,"..."])` script blocks. The `<main>` or `<article>` tag contains only a `<div hidden=""><!--$--><!--/$--></div>` placeholder.

## Extraction Technique

### Step 1: Unescape the RSC payload

```bash
curl -sL --max-time 15 'URL' | sed 's/\\"/"/g; s/\\u0026/\&/g; s/\\u003c/</g; s/\\u003e/>/g'
```

### Step 2: Extract text from `"children":"text"` patterns

```bash
# Quick extraction — works for titles, descriptions, short content
curl -sL URL | sed 's/\\"/"/g' | grep -oP '"children"\s*:\s*"[^"]{20,}"' | sed 's/"children":\s*"//' | sed 's/"$//'
```

### Step 3: For full article body — Python parsing

The article body is in deeply nested RSC structures. Save to file and parse:

```bash
curl -sL --max-time 15 'URL' > /tmp/page.html

cat /tmp/page.html | sed 's/\\"/"/g; s/\\u0026/\&/g; s/\\u003c/</g; s/\\u003e/>/g' | python3 -c "
import sys, re
html = sys.stdin.read()
scripts = re.findall(r'self\.__next_f\.push\(\[1,\"(.*?)\"\]\)', html, re.DOTALL)
all_text = []
# Define keyword filters to exclude metadata/code strings
skip_kw = ['className', 'props:', 'sys:', 'metadata', 'contentType', ...]
for s in scripts:
    s = s.replace('\\\\n', '\n').replace('\\n', '\n')
    for m in re.finditer(r'\"([^\"]{20,})\"', s):
        t = m.group(1)
        if any(kw in t for kw in skip_kw):
            continue
        if re.search(r'[a-zA-Z]{3,}', t):
            all_text.append(t)
seen = set()
for t in all_text:
    if t not in seen:
        seen.add(t)
        print(t)
"
```

### Skip-keyword list (critical for noise filtering)

The RSC payload contains hundreds of CSS class names, component props, Contentful CMS metadata, navigation strings, and boilerplate. A comprehensive skip-list is essential. Key categories to filter:
- CSS classes: `className`, `col-span`, `flex`, `grid`, `text-`, `bg-`, `rounded`, `transition`, etc.
- RSC internals: `props:`, `sys:`, `metadata`, `contentType`, `publishedVersion`, `createdAt`, etc.
- CMS fields: `cmsName`, `slug`, `pageType`, `searchText`, `metaDescription`, etc.
- Layout/navigation: `Header`, `Footer`, `Terms`, `Privacy`, `navigation`, etc.
- React internals: `react.`, `Router`, `Sreact`, `Next.`, `parallel`, `fragment`, etc.

## Alternative: RSS Feed

Next.js sites often have RSS feeds. Check for `<link rel="alternate" type="application/rss+xml">` in the HTML head. RSS gives clean text without RSC parsing.

**openaifoundation.org example**: RSS at `/rss.xml` provided titles, dates, and descriptions cleanly. But full article body required RSC extraction.

## Key Differences from Other SPA Patterns

| Pattern | Content Location | Extraction |
|---------|-----------------|------------|
| Simple SPA (React/Vue) | Loaded via `fetch()` at runtime | Need browser automation |
| SSR (traditional) | In HTML body | Standard `curl + grep` |
| Next.js RSC | In `<script>` RSC payload | `sed + grep/Python` on raw HTML |
| Static site + MD | `.md` file at same path | Try `.md` extension |

## Pitfalls

- **"404" in RSC payload**: Next.js RSC payloads may contain `404: This page could not be found.` alongside actual page content. This is a default RSC error state — ignore it and extract the real content below it.
- **Filter aggressively**: Without a comprehensive skip-keyword list, the output is 90% CSS class names and CMS metadata. The skip list is critical.
- **Unicode escapes**: RSC payloads use `\\u0026` (`&`), `\\u003c` (`<`), `\\u003e` (`>`). Handle these in the `sed` preprocessing step.
- **Body text in nested structures**: Titles and descriptions are in simple `"children":"text"` patterns, but article body text is in deeply nested RSC structures that require Python parsing with regex extraction.

## Real-World Example: openaifoundation.org

- Site: Next.js App Router with Contentful CMS backend
- RSS: Available at `/rss.xml` (5 articles, descriptions only)
- RSC extraction yielded: full article body, grantee quotes, researcher names, dollar amounts
- Content included Unicode escapes (`\\u0026` for `&`) and nested RSC JSON structures
- The `404: This page could not be found.` string appeared in RSC payload despite pages being valid (likely a default RSC error state rendered alongside actual content)
