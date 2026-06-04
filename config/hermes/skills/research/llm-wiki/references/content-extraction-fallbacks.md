# Web Content Extraction Fallbacks

When `web_extract` fails (blocked, timeout, JS-rendered), use this decision tree. Start at the top and work down.

## Decision Tree

### 1. `web_extract` → works? Done.
- Pass URLs as a list for batched parallel extraction. Most efficient.
- Watch for "LLM summarization timed out" — content is partially usable (~5K chars); try `browser_navigate` for the full page.

### 2. `web_extract` blocked (private/internal network error)
Some hosting platforms (GitHub Pages with certain configs, some CDNs) trigger this even for public URLs. Fall back:

**a) Curl raw HTML:** `curl -sL --max-time 30 -H "User-Agent: Mozilla/5.0" "<URL>"`
- ⚠️ Not all JS frameworks are the same. **Next.js with SSG (static site generation)** — used by Anthropic, Figure, and many company blogs — **serves full article content in the initial HTML**, even though it loads JS. The text lives in `<p>` elements and/or the Next.js RSC JSON payload. Always check the curl output for `<p>` content before declaring it unusable.
- True CSR sites (Quartz, Gatsby CSR, most SPA blogs) return only a shell with `<div id="root">` — no content. Move to step (b) or (c).
- Static HTML sites (raw markdown exporters, plain text archives) return full content immediately.
- **If the curl output has usable `<p>` text**, use targeted extraction instead of broad `sed` stripping (see "Better Curl Extraction Recipes" below).

**b) Try raw markdown endpoint:** `curl -sL "<URL>.md"` (Quartz sites, some static generators expose this)

**c) Search for alternative mirrors:** `web_search "Author Name" "Article Title" full text`
- Common mirrors: textfiles archives, Internet Archive, PhilPapers, academic citation sites, mailing list archives
- Key insight: **canonical essays by known authors (Yudkowsky, Gwern, etc.) usually have multiple mirrors** — the JS-rendered archive is rarely the only copy

**d) `browser_navigate`:** Requires Chrome installed via `agent-browser install`. Falls back to this for JS-heavy sites with no alternative mirror.

### 3. `web_extract` timed out (LLM summarization)
- First ~5,000 characters are still usable for key facts
- Use `browser_navigate` for the full page text snapshot
- If browser not available, `curl` the page and `sed` strip HTML

### 4. `web_extract` succeeded but returned only navigation chrome (no article body)
**Silent failure mode** — `web_extract` reports success with 5,000-15,000 chars, but all of it is navigation menus, footer links, and product cards. The actual article body is JS-rendered and not in the static HTML that `web_extract` sees. Common on official company blogs (Google DeepMind, OpenAI, Anthropic) and modern JS frameworks.

**a) `web_search` triangulation (primary fallback on headless servers):**
Run 2-3 `web_search` queries with different angles. Third-party tech news sites (MarkTechPost, The Register, The Decoder, NDTV, Ars Technica) that covered the same announcement will reproduce key quotes, data points, and structural details. Google's rich snippets for well-indexed tech blogs often include direct quotes from the original.

Query pattern:
```
web_search("<Company> <Product Name> <key detail> <year>")
web_search("<Company> \"<direct quote from snippet>\" <year>")
web_search("<Company> <Product> <technical detail> <year>")
```

**b) `browser_navigate`:** Falls back to this if Chrome is available. Returns full JS-rendered content including article body.

**c) Curl + JS parsing:** Rarely worth it — modern JS bundles are opaque. Use (a) or (b) instead.

**Example: Google DeepMind AI Pointer blog (May 2026):**
```
# Step 1: web_extract deepmind.google/blog/ai-pointer/ → 12K chars of nav chrome only
# Step 4a: web_search "DeepMind AI pointer Gemini cursor context May 2026"
#   → MarkTechPost had all 4 principles with quotes
#   → The Register had product integration details
#   → The Decoder had author names + strategic framing
# Step 4a (second query): web_search "DeepMind 'Adrien Baranes' 'Rob Marchant' pointer"
#   → Confirmed author names from Google snippet
# Combined: 80%+ of article content reconstructed from 3 third-party sources
```

## Example: Quartz archive site (supaiku.com)
```
# Step 1: web_extract → "Blocked: private/internal network"
# Step 2a: curl → JS shell, no content
# Step 2b: .md → 404
# Step 2c: web_search "Yudkowsky" "Staring Into The Singularity" full text
#   → Found mirror at textfiles.meulie.net
# Step 2a (again): curl mirror → static HTML, strip with sed → 1150 lines of text
```

## Curl HTML Stripping Recipe (generic)
```bash
curl -sL --max-time 30 -H "User-Agent: Mozilla/5.0" "$URL" \
  | sed 's/<[^>]*>//g' \
  | sed '/^$/N;/^\n$/D' > /tmp/raw.txt
```
⚠️ Generates a lot of noise from JSON payloads, script tags, and style blocks. Use the targeted recipes below when the page framework is known.

## Better Curl Extraction Recipes

### Extract article content from `<p>` tags (Next.js SSG, static HTML)
```bash
curl -sL --max-time 30 "$URL" \
  | grep -oP '<p[^>]*>.*?</p>' \
  | sed 's/<[^>]*>//g' \
  | sed '/^[[:space:]]*$/d' > /tmp/raw.txt
```
Useful for: Anthropic blog, company news pages, any site that renders article body as `<p>` elements in the initial HTML. The `<h1>`, `<h2>`, `<h3>` headings can be extracted separately:
```bash
curl -sL --max-time 30 "$URL" \
  | grep -oP '<h[1-3][^>]*>.*?</h[1-3]>' \
  | sed 's/<[^>]*>//g'
```

### Extract Next.js RSC / `__NEXT_DATA__` JSON payload
Some Next.js sites (Figure.ai, some Shopify blogs) store the full article text inside a `<script id="__NEXT_DATA__">` JSON blob. Extract and pretty-print:
```bash
# Extract __NEXT_DATA__ JSON, then traverse to find article content
curl -sL --max-time 30 "$URL" \
  | grep -oP '<script id="__NEXT_DATA__"[^>]*>.*?</script>' \
  | sed 's/<[^>]*>//g' \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('props',{}).get('pageProps',{}).get('page',{}).get('content',{}).get('json',{}).get('content',''))" 2>/dev/null
```
The traversal keys (`pageProps.page.content.json.content`) vary by site. First dump the shape:
```bash
curl -sL --max-time 30 "$URL" | grep -oP '__NEXT_DATA__[^>]*>.*?</script>' | sed 's/^[^>]*>//;s/<\/script>//' | python3 -c "import sys,json; d=json.load(sys.stdin); k=list(d.get('props',{}).get('pageProps',{}).keys()); print(k)"
```
Adjust traversal based on the key names shown.

### Extract from `<article>` tag (best when available)
```bash
curl -sL --max-time 30 "$URL" \
  | sed -n '/<article/,/<\/article>/p' \
  | sed 's/<[^>]*>//g' \
  | sed '/^[[:space:]]*$/d' > /tmp/raw.txt
```
Many blogs (including Anthropic, Google AI) wrap content in `<article>` elements.

## Decision: Which recipe to use?
| Signal in curl output | Recipe |
|----------------------|--------|
| `<article>` tag present | `<article>` extraction (cleanest) |
| `<h1>` heading + `<p>` paragraphs, no `<article>` | `<p>` + heading extraction |
| `__NEXT_DATA__` script tag | JSON payload extraction |
| `<script>` bundles, `<div id="root">` (CSR shell) | Curl won't help — use `web_search` triangulation (step 4a) or `browser_navigate` |

## Pitfalls
- `browser_navigate` requires Chrome — `agent-browser install` first (can be slow)
- Some mirrors (textfiles) use ancient HTML with `&copy;` entities, tab characters, etc. — still readable after sed
- Quartz sites store content in JS payloads, not in HTML source — curl will never get content directly
- Internet Archive / Wayback Machine may have snapshots when live mirrors are gone
