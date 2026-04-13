---
name: grokipedia-enrichment
description: Enrich person entity pages using Grokipedia (AI-generated encyclopedia with 6M+ articles). Search for people by name, extract structured biographical data, and merge into wiki entity pages.
category: wiki
version: 1.0.0
metadata:
  hermes:
    tags: [wiki, enrichment, grokipedia, person, entity]
    homepage: https://grokipedia.com
prerequisites:
  skills: [wiki-entity-upgrade, opinion-leader-depth-analysis]
---

# Grokipedia Enrichment

Use [Grokipedia](https://grokipedia.com/) as a supplementary source when enriching person entity pages. Grokipedia is an AI-generated encyclopedia (Grok-powered, 6M+ articles) with strong coverage of tech/AI figures.

## When to Use

- Enriching a person entity page (L1→L2 or L2→L3)
- Need structured biographical data: education, career history, key projects
- Cross-checking facts before adding to wiki
- Person has no Wikipedia page but may have a Grokipedia article
- Bootstrapping a new entity page for a known tech figure

## ⚠️ Important Caveats

- **AI-generated content** — Grokipedia articles are written by Grok, not human editors. Always cross-reference key claims with primary sources.
- **"Fact-checked by Grok"** — this is self-verification, not independent fact-checking. Treat as a starting point, not ground truth.
- **Coverage bias** — strong for well-known tech figures (Karpathy, Willison, Sanfilippo), weaker for emerging voices.
- **Use for L1/L2 enrichment primarily** — for L3 thought analysis, prefer the person's own blog/tweets as primary sources.

## API Reference

### 1. Typeahead Search (fast, exact match)

```bash
curl -s 'https://grokipedia.com/api/typeahead?query=PERSON_NAME&limit=5'
```

Response:
```json
{
  "results": [
    {
      "slug": "Person_Name",
      "title": "Person Name",
      "snippet": "Short description...",
      "relevanceScore": 100000,
      "viewCount": "292295"
    }
  ],
  "searchTimeMs": 19.14
}
```

- `relevanceScore: 100000` = exact title match
- `slug` is used to construct the page URL: `/page/{slug}`
- Returns up to `limit` results
- **Handles may not work** — use real names (e.g., "Salvatore Sanfilippo" not "antirez")

### 2. Full-text Search (broader, via HTML scraping)

```bash
# Get search results page
curl -s 'https://grokipedia.com/search?q=QUERY' | grep -oP 'href="/page/[^"]*"' | head -10
```

Use when typeahead returns empty — the search page does fuzzy matching and finds related articles.

### 3. Article Page (SSR HTML, full content)

```bash
# Fetch full article
curl -s 'https://grokipedia.com/page/{SLUG}'
```

The page is server-side rendered — full text is in the HTML. Extract with:

```python
import subprocess, re
from html.parser import HTMLParser

def fetch_grokipedia(slug):
    """Fetch and extract text from a Grokipedia article."""
    html = subprocess.run(
        ['curl', '-s', f'https://grokipedia.com/page/{slug}'],
        capture_output=True, text=True
    ).stdout
    
    # Strip scripts/styles, extract text
    clean = re.sub(r'<(script|style|nav|header|footer)[^>]*>.*?</\1>', '', html, flags=re.DOTALL)
    clean = re.sub(r'<[^>]+>', ' ', clean)
    clean = re.sub(r'\s+', ' ', clean).strip()
    
    # Remove boilerplate (everything before the first "Fact-checked" and after "References")
    start = clean.find('Fact-checked')
    end = clean.rfind('References')
    if start > 0 and end > start:
        return clean[start:end].strip()
    return clean[:10000]  # fallback
```

## Workflow

### Step 1: Search for the person

```bash
# Try typeahead first (fast)
curl -s 'https://grokipedia.com/api/typeahead?query=Person+Name&limit=3' | python3 -m json.tool

# If empty, try full-text search
curl -s 'https://grokipedia.com/search?q=Person+Name' | grep -oP 'href="/page/[^"]*"' | head -5
```

**Name resolution tips:**
- Use full real name, not handles ("Salvatore Sanfilippo" not "antirez")
- Try variations: "Andrej Karpathy", "Karpathy"
- For non-Western names, try both orderings

### Step 2: Fetch and extract article content

```bash
curl -s 'https://grokipedia.com/page/SLUG' | python3 -c "
import sys, re
html = sys.stdin.read()
clean = re.sub(r'<(script|style|nav|header|footer)[^>]*>.*?</\\1>', '', html, flags=re.DOTALL)
clean = re.sub(r'<[^>]+>', ' ', clean)
clean = re.sub(r'\\s+', ' ', clean).strip()
start = clean.find('Fact-checked')
end = clean.rfind('References')
if start > 0 and end > start:
    print(clean[start:end])
else:
    print(clean[:8000])
"
```

### Step 3: Extract structured data for wiki entity page

From the Grokipedia article, extract:

| Field | Wiki Section | Notes |
|-------|-------------|-------|
| Birth/nationality | Frontmatter / Bio | Cross-check with primary source |
| Education | ## Education / Timeline | University, degree, years |
| Career history | ## Timeline | Companies, roles, dates |
| Key projects | ## Projects / Core Ideas | Project names, descriptions, launch dates |
| Awards/recognition | ## Recognition | Verify independently |
| Personal details | (use sparingly) | Only if relevant to their work |

### Step 4: Merge into wiki entity page

**Rules:**
- **Never overwrite existing L3 thought analysis** with Grokipedia content
- **Add Grokipedia as a source** in frontmatter: `- "https://grokipedia.com/page/{slug}"`
- **Mark Grokipedia-sourced facts** with `(via Grokipedia)` until independently verified
- **Prioritize the person's own writing** over Grokipedia's summary
- **Fill gaps only** — use Grokipedia for missing L1/L2 data, not to replace existing content

Frontmatter addition:
```yaml
sources:
  - "https://grokipedia.com/page/Person_Slug"  # L1/L2 biographical data
```

### Step 5: Commit

```bash
cd ~/ai-topics && git add wiki/entities/<person>.md && git commit -m "wiki: enrich <person> with Grokipedia data" && git push
```

## Batch Enrichment Pattern

When enriching multiple entity pages:

```python
import subprocess, json, os

def search_grokipedia(name):
    """Search Grokipedia for a person, return slug if found."""
    result = subprocess.run(
        ['curl', '-s', f'https://grokipedia.com/api/typeahead?query={name}&limit=1'],
        capture_output=True, text=True
    )
    data = json.loads(result.stdout)
    if data.get('results'):
        return data['results'][0]['slug']
    return None

# Scan entity pages missing Grokipedia source
entity_dir = os.path.expanduser('~/ai-topics/wiki/entities')
for f in sorted(os.listdir(entity_dir)):
    if not f.endswith('.md'):
        continue
    path = os.path.join(entity_dir, f)
    with open(path) as fh:
        content = fh.read(500)
    if 'person' in content and 'grokipedia' not in content.lower():
        # Extract title from frontmatter
        import re
        m = re.search(r'title:\s*"([^"]+)"', content)
        if m:
            name = m.group(1)
            slug = search_grokipedia(name)
            if slug:
                print(f"  ✅ {f} → {slug}")
            else:
                print(f"  ❌ {f} — not found on Grokipedia")
```

## URL Patterns

| Purpose | URL |
|---------|-----|
| Typeahead API | `https://grokipedia.com/api/typeahead?query={name}&limit={n}` |
| Search page | `https://grokipedia.com/search?q={query}` |
| Article page | `https://grokipedia.com/page/{slug}` |

## Pitfalls

1. **`/wiki/` path does NOT work** — articles are at `/page/{slug}`, not `/wiki/{slug}`
2. **Typeahead requires real names** — handles like "antirez" or "swyx" return empty; use "Salvatore Sanfilippo" or "Shawn Wang"
3. **AI-generated content** — do NOT treat Grokipedia as a primary source; it's useful for L1/L2 scaffolding but not for L3 thought analysis
4. **No public content API** — article text must be extracted from SSR HTML via curl + parsing
5. **Reference numbers in text** — extracted text contains `[1]`, `[2]` etc. inline; strip these during processing
6. **Rate limiting unknown** — no documented rate limits, but space requests when batch processing (1-2 sec delay)
7. **Empty results ≠ person doesn't exist** — try full-text search (`/search?q=`) as fallback when typeahead fails
8. **Coverage gaps** — niche/emerging figures may not have articles; this is supplementary, not comprehensive
9. **Do NOT cite Grokipedia as authoritative** — always add `(via Grokipedia, verify)` annotation until cross-checked
