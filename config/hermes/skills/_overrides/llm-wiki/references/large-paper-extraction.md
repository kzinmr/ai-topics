# Large Paper Extraction When web_extract Times Out

## Problem

`web_extract` times out on long arXiv papers (144K+ chars) with:
> LLM summarization timed out. To fix: increase auxiliary.web_extract.timeout in config.yaml, or use a faster auxiliary model.

The existing pitfall in `llm-wiki` covers this for *articles* (use `browser_navigate` or `web_search` for supplements), but for papers the extraction is more systematic.

## Solution: Targeted HTML Download + Python Section Extraction

### Step 1: Download arXiv HTML version

```bash
curl -sL "https://arxiv.org/html/XXXX.XXXXXvN" -o /tmp/paper.html
```

Use the HTML version (not PDF) — it's plain text wrapped in `<div>` tags, much easier to parse than PDF layout.

Verify download:
```bash
wc -c /tmp/paper.html  # Should be ~1-2MB
```

### Step 2: Extract section headings

```python
import re
with open('/tmp/paper.html') as f:
    html = f.read()

# Find all h2/h3 headings to understand paper structure
for tag in ['h2', 'h3']:
    pattern = f'<{tag}[^>]*class="ltx_title[^"]*"[^>]*>(.*?)</{tag}>'
    for m in re.finditer(pattern, html, re.DOTALL):
        title = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        print(f'  [{tag}] {title} (pos {m.start()})')
```

### Step 3: Identify which sections are new/changed

For a paper update (v1→v2→v3), read the abstract page first:
```bash
web_extract "https://arxiv.org/abs/XXXX.XXXXX"
```
This gives you the submission history with dates for each version.

Compare the changelog/user description of what's new against the section headings to identify which sections to extract.

### Step 4: Targeted keyword extraction

Instead of extracting full sections, search for specific new-content keywords:

```python
import re
with open('/tmp/paper.html') as f:
    html = f.read()

# Clean HTML → plain text
html = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', html, flags=re.DOTALL)
text = re.sub(r'<[^>]+>', ' ', html)
text = re.sub(r'\s+', ' ', text)

# Search for new-content keywords
for kw in ['OpenCode', 'depth=2', 'depth=3', 'MRCR', 'syntax error']:
    positions = [m.start() for m in re.finditer(re.escape(kw), text)]
    for pos in positions:
        snippet = text[max(0, pos-300):pos+500]
        print(f"=== '{kw}' at pos {pos} ===\n{snippet}\n")
```

### Step 5: Compile the raw file update

Write an updated raw paper file that:
1. Keeps the existing structure from the previous version
2. Adds a "New in vN" section with key findings extracted from the keyword search
3. Updates the version line and any changed benchmark numbers
4. Replaces outdated tables with new ones

### Step 6: Update wiki pages

After the raw file is updated, use `patch` for targeted updates to concept/entity pages:
- Bump version references (`v1→v2` → `v1→v2→v3`)
- Add new findings sections
- Update benchmark tables
- Add error analysis details if expanded

## When NOT to use this

- Papers under 50K chars: `web_extract` on the abstract page (HTML tab) usually works
- Papers with no HTML version: Use `browser_navigate` on the PDF URL instead
- First-time paper ingestion (not an update): Worth trying `web_extract` on the PDF URL first, which sometimes works for shorter papers
