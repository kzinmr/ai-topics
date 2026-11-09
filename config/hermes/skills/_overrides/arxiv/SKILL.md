---
name: arxiv
description: "Search arXiv papers by keyword, author, category, or ID."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [Research, Arxiv, Papers, Academic, Science, API]
    related_skills: [ocr-and-documents, wiki-ingestion-pipelines]
---

# arXiv Research

Search and retrieve academic papers from arXiv via their free REST API. No API key, no dependencies — just curl.

## Quick Reference

| Action | Command |
|--------|---------|
| Search papers | `curl "https://export.arxiv.org/api/query?search_query=all:QUERY&max_results=5"` |
| Get specific paper | `curl "https://export.arxiv.org/api/query?id_list=2402.03300"` |
| Read abstract (web) | `web_extract(urls=["https://arxiv.org/abs/2402.03300"])` |
| Read full paper (PDF) | `web_extract(urls=["https://arxiv.org/pdf/2402.03300"])` |

## Searching Papers

The API returns Atom XML. Parse with `grep`/`sed` or pipe through `python3` for clean output.

### Basic search

```bash
curl -s "https://export.arxiv.org/api/query?search_query=all:GRPO+reinforcement+learning&max_results=5"
```

### Clean output (parse XML to readable format)

```bash
curl -s "https://export.arxiv.org/api/query?search_query=all:GRPO+reinforcement+learning&max_results=5&sortBy=submittedDate&sortOrder=descending" | python3 -c "
import sys, xml.etree.ElementTree as ET
ns = {'a': 'http://www.w3.org/2005/Atom'}
root = ET.parse(sys.stdin).getroot()
for i, entry in enumerate(root.findall('a:entry', ns)):
    title = entry.find('a:title', ns).text.strip().replace('\n', ' ')
    arxiv_id = entry.find('a:id', ns).text.strip().split('/abs/')[-1]
    published = entry.find('a:published', ns).text[:10]
    authors = ', '.join(a.find('a:name', ns).text for a in entry.findall('a:author', ns))
    summary = entry.find('a:summary', ns).text.strip()[:200]
    cats = ', '.join(c.get('term') for c in entry.findall('a:category', ns))
    print(f'{i+1}. [{arxiv_id}] {title}')
    print(f'   Authors: {authors}')
    print(f'   Published: {published} | Categories: {cats}')
    print(f'   Abstract: {summary}...')
    print(f'   PDF: https://arxiv.org/pdf/{arxiv_id}')
    print()
"
```

## Search Query Syntax

> **Reliable discovery fallback (use this first if the export API is rate-limited).** The
> `export.arxiv.org/api/query` endpoint aggressively rate-limits ("Rate exceeded" can persist
> across 30–60s of sleeping — it's not a clean per-request backoff). The **arxiv.org website
> search** is far more forgiving and works with just a browser User-Agent. Prefer it for topic
> discovery when the API is being flaky:
>
> ```bash
> curl -sL -A "Mozilla/5.0" "https://arxiv.org/search/?query=%22homomorphic%20encryption%22%20language%20model&searchtype=all" -o /tmp/arx_s.html
> python3 - <<'EOF'
> import re
> html=open('/tmp/arx_s.html').read()
> for b in re.findall(r'<li class="arxiv-result">(.*?)</li>', html, re.S)[:15]:
>     m=re.search(r'arXiv:(\d{4}\.\d{4,5})', b)
>     t=re.search(r'<p class="title is-5 mathjax">\s*(.*?)</p>', b, re.S)
>     print('-', m.group(1) if m else '?', '|', re.sub(r'<[^>]+>','',t.group(1)).strip()[:95] if t else '?')
> EOF
> ```
>
> - Quote phrase terms with `%22` for exact-match (`%22foo%20bar%22`).
> - This HTML endpoint intermittently **hangs on first hit** (DNS/TLS warm-up); if it times out
>   (>60s), just retry — the second attempt usually succeeds fast.
> - `arxiv.org/list/{cat}/recent` is a **poor** discovery source: its list HTML doesn't match the
>   `arxiv-result` / title regexes above, so parsing it yields nothing. Use the search endpoint
>   instead, or the export API `id_list`/`cat:` queries once it stops rate-limiting.
>
> After discovery, fetch each candidate's abstract page (`arxiv.org/abs/{id}`) for metadata —
> that page is reliable and also gives you peer-review comments (see
> "Peer-review detection via abstract-page meta tags" below).

## Search Query Syntax (export API)

| Prefix | Searches | Example |
|--------|----------|---------|
| `all:` | All fields | `all:transformer+attention` |
| `ti:` | Title | `ti:large+language+models` |
| `au:` | Author | `au:vaswani` |
| `abs:` | Abstract | `abs:reinforcement+learning` |
| `cat:` | Category | `cat:cs.AI` |
| `co:` | Comment | `co:accepted+NeurIPS` |

### Boolean operators

```
# AND (default when using +)
search_query=all:transformer+attention

# OR
search_query=all:GPT+OR+all:BERT

# AND NOT
search_query=all:language+model+ANDNOT+all:vision

# Exact phrase
search_query=ti:"chain+of+thought"

# Combined
search_query=au:hinton+AND+cat:cs.LG
```

## Sort and Pagination

| Parameter | Options |
|-----------|---------|
| `sortBy` | `relevance`, `lastUpdatedDate`, `submittedDate` |
| `sortOrder` | `ascending`, `descending` |
| `start` | Result offset (0-based) |
| `max_results` | Number of results (default 10, max 30000) |

```bash
# Latest 10 papers in cs.AI
curl -s "https://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=descending&max_results=10"
```

## Fetching Specific Papers

```bash
# By arXiv ID
curl -s "https://export.arxiv.org/api/query?id_list=2402.03300"

# Multiple papers
curl -s "https://export.arxiv.org/api/query?id_list=2402.03300,2401.12345,2403.00001"
```

## BibTeX Generation

After fetching metadata for a paper, generate a BibTeX entry:

{% raw %}
```bash
curl -s "https://export.arxiv.org/api/query?id_list=1706.03762" | python3 -c "
import sys, xml.etree.ElementTree as ET
ns = {'a': 'http://www.w3.org/2005/Atom', 'arxiv': 'http://arxiv.org/schemas/atom'}
root = ET.parse(sys.stdin).getroot()
entry = root.find('a:entry', ns)
if entry is None: sys.exit('Paper not found')
title = entry.find('a:title', ns).text.strip().replace('\n', ' ')
authors = ' and '.join(a.find('a:name', ns).text for a in entry.findall('a:author', ns))
year = entry.find('a:published', ns).text[:4]
raw_id = entry.find('a:id', ns).text.strip().split('/abs/')[-1]
cat = entry.find('arxiv:primary_category', ns)
primary = cat.get('term') if cat is not None else 'cs.LG'
last_name = entry.find('a:author', ns).find('a:name', ns).text.split()[-1]
print(f'@article{{{last_name}{year}_{raw_id.replace(\".\", \"\")},')
print(f'  title     = {{{title}}},')
print(f'  author    = {{{authors}}},')
print(f'  year      = {{{year}}},')
print(f'  eprint    = {{{raw_id}}},')
print(f'  archivePrefix = {{arXiv}},')
print(f'  primaryClass  = {{{primary}}},')
print(f'  url       = {{https://arxiv.org/abs/{raw_id}}}')
print('}')
"
```
{% endraw %}

## Reading Paper Content

After finding a paper, read it:

```
# Abstract page (fast, metadata + abstract)
web_extract(urls=["https://arxiv.org/abs/2402.03300"])

# Full paper (PDF → markdown via Firecrawl)
web_extract(urls=["https://arxiv.org/pdf/2402.03300"])
```

For local PDF processing, see the `ocr-and-documents` skill.

## Common Categories

| Category | Field |
|----------|-------|
| `cs.AI` | Artificial Intelligence |
| `cs.CL` | Computation and Language (NLP) |
| `cs.CV` | Computer Vision |
| `cs.LG` | Machine Learning |
| `cs.CR` | Cryptography and Security |
| `stat.ML` | Machine Learning (Statistics) |
| `math.OC` | Optimization and Control |
| `physics.comp-ph` | Computational Physics |

Full list: https://arxiv.org/category_taxonomy

## Helper Script

The `scripts/search_arxiv.py` script handles XML parsing and provides clean output:

```bash
python scripts/search_arxiv.py "GRPO reinforcement learning"
python scripts/search_arxiv.py "transformer attention" --max 10 --sort date
python scripts/search_arxiv.py --author "Yann LeCun" --max 5
python scripts/search_arxiv.py --category cs.AI --sort date
python scripts/search_arxiv.py --id 2402.03300
python scripts/search_arxiv.py --id 2402.03300,2401.12345
```

No dependencies — uses only Python stdlib.

---

## Semantic Scholar (Citations, Related Papers, Author Profiles)

arXiv doesn't provide citation data or recommendations. Use the **Semantic Scholar API** for that — free, no key needed for basic use (1 req/sec), returns JSON.

### Get paper details + citations

```bash
# By arXiv ID
curl -s "https://api.semanticscholar.org/graph/v1/paper/arXiv:2402.03300?fields=title,authors,citationCount,referenceCount,influentialCitationCount,year,abstract" | python3 -m json.tool

# By Semantic Scholar paper ID or DOI
curl -s "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1234/example?fields=title,citationCount"
```

### Get citations OF a paper (who cited it)

```bash
curl -s "https://api.semanticscholar.org/graph/v1/paper/arXiv:2402.03300/citations?fields=title,authors,year,citationCount&limit=10" | python3 -m json.tool
```

### Get references FROM a paper (what it cites)

```bash
curl -s "https://api.semanticscholar.org/graph/v1/paper/arXiv:2402.03300/references?fields=title,authors,year,citationCount&limit=10" | python3 -m json.tool
```

### Search papers (alternative to arXiv search, returns JSON)

```bash
curl -s "https://api.semanticscholar.org/graph/v1/paper/search?query=GRPO+reinforcement+learning&limit=5&fields=title,authors,year,citationCount,externalIds" | python3 -m json.tool
```

### Get paper recommendations

```bash
curl -s -X POST "https://api.semanticscholar.org/recommendations/v1/papers/" \
  -H "Content-Type: application/json" \
  -d '{"positivePaperIds": ["arXiv:2402.03300"], "negativePaperIds": []}' | python3 -m json.tool
```

### Author profile

```bash
curl -s "https://api.semanticscholar.org/graph/v1/author/search?query=Yann+LeCun&fields=name,hIndex,citationCount,paperCount" | python3 -m json.tool
```

### Useful Semantic Scholar fields

`title`, `authors`, `year`, `abstract`, `citationCount`, `referenceCount`, `influentialCitationCount`, `isOpenAccess`, `openAccessPdf`, `fieldsOfStudy`, `publicationVenue`, `externalIds` (contains arXiv ID, DOI, etc.)

---

## Complete Research Workflow

1. **Discover**: `python scripts/search_arxiv.py "your topic" --sort date --max 10`
2. **Assess impact**: `curl -s "https://api.semanticscholar.org/graph/v1/paper/arXiv:ID?fields=citationCount,influentialCitationCount"`
3. **Read abstract**: `web_extract(urls=["https://arxiv.org/abs/ID"])`
4. **Read full paper**: `web_extract(urls=["https://arxiv.org/pdf/ID"])`
5. **Find related work**: `curl -s "https://api.semanticscholar.org/graph/v1/paper/arXiv:ID/references?fields=title,citationCount&limit=20"`
6. **Get recommendations**: POST to Semantic Scholar recommendations endpoint
7. **Track authors**: `curl -s "https://api.semanticscholar.org/graph/v1/author/search?query=NAME"`

## Rate Limits

| API | Rate | Auth |
|-----|------|------|
| arXiv | ~1 req / 3 seconds | None needed |
| Semantic Scholar | 1 req / second | None (100/sec with key) — **429s are common without a key**; retry after 30-60s, or fall back to abstract-page meta tags for venue/author metadata (see "Peer-review detection via abstract-page meta tags" below). Do not treat a 429 as "no venue" — it's a rate limit, not an absence. |

## Notes

- arXiv returns Atom XML — use the helper script or parsing snippet for clean output
- Semantic Scholar returns JSON — pipe through `python3 -m json.tool` for readability
- arXiv IDs: old format (`hep-th/0601001`) vs new (`2402.03300`)
- PDF: `https://arxiv.org/pdf/{id}` — Abstract: `https://arxiv.org/abs/{id}`
- HTML (when available): `https://arxiv.org/html/{id}`
- For local PDF processing, see the `ocr-and-documents` skill

## ID Versioning

- `arxiv.org/abs/1706.03762` always resolves to the **latest** version
- `arxiv.org/abs/1706.03762v1` points to a **specific** immutable version
- When generating citations, preserve the version suffix you actually read to prevent citation drift (a later version may substantially change content)
- The API `<id>` field returns the versioned URL (e.g., `http://arxiv.org/abs/1706.03762v7`)

## Withdrawn Papers

Papers can be withdrawn after submission. When this happens:
- The `<summary>` field contains a withdrawal notice (look for "withdrawn" or "retracted")
- Metadata fields may be incomplete
- Always check the summary before treating a result as a valid paper

---

## Wiki Ingestion (Next Steps)

After fetching a paper, to ingest it into the wiki:

1. **Check peer-review** — See `wiki-ingestion-pipelines` (Section D: arXiv Paper Pipeline) for the triage matrix: peer-reviewed conferences (NeurIPS, ICML, ICLR, ACL, CVPR, etc.) and tech company tech reports → ✅ OK. arXiv-only with no venue → ❌ BLOCK.
2. **Verify via Semantic Scholar** — `publicationVenue` field confirms venue. Also note citation count as signal of impact.
3. **Save raw paper** — Save to `~/ai-topics/wiki/raw/papers/{YYYY-MM-DD}_{arxiv_id}_{short-title}.md` (NOT `wiki/raw/articles/`). Include `arxiv_id`, `venue`, `published`, `citations`, `authors` in frontmatter. Add a `type: paper` field and an `abstract` field for paper-type raw files.

**Peer-review detection via abstract-page meta tags** (fast, no API):
```bash
curl -sL "https://arxiv.org/abs/{id}" | grep -E '<td class="tablecell comments|citation_.*Comments|jref' 
```
If no "Comments:" / "Published in" / "Accepted to" appears, the paper is arXiv-only. A tech-company tech report (all authors at one company, e.g. Scale AI) → ✅ OK per triage matrix. Truly arXiv-only academic preprint → ❌ BLOCK unless user explicitly requests (user override → note `user override` in the raw frontmatter `venue` field).
4. **Create/update concept page** — Follow `wiki-concept-from-research` skill for the page structure. Create comparison tables with related concepts (e.g., Shannon vs V-Information).
5. **Update index.md + log.md** — Append log entry, update concepts page count. See `wiki-ingestion-pipelines` for index/log update patterns.
6. **Commit** — `cd ~/ai-topics && git add wiki/ && git commit -m "wiki: concept page for {topic} ({authors}, {venue} {year})" && git push`

For the full workflow including triage, blocked-paper handling, and name collision resolution, load the `wiki-ingestion-pipelines` umbrella skill and consult its Section D (arXiv Paper Pipeline) and `references/arxiv-paper-pipeline.md`.

### Wiki Ingestion Pitfalls

1. **Tag taxonomy violations block commits**: When creating concept/entity pages for a paper, any tags in frontmatter must exist in `wiki/SCHEMA.md`. The pre-commit hook will block the commit. **Fix**: Before committing, check `grep "your-tag" wiki/SCHEMA.md`. If missing, add the tag to the appropriate category in SCHEMA.md first. See `wiki-entity-enrichment-from-article` skill → `references/precommit-pitfalls.md` for the full tag violation playbook.

2. **API rate limits**: The arXiv API rate-limits at ~1 req/3 sec. If you get "Rate exceeded", fall back to scraping the abstract page directly:
   ```bash
   curl -s "https://arxiv.org/abs/2604.14403" | grep 'citation_abstract' | sed 's/.*content="//;s/".*//'
   ```
   This extracts the abstract from the HTML meta tags without hitting the API.

3. **PDF extraction fallback**: When `web_extract` isn't available and `pymupdf` isn't installed in the main venv, create a temp venv:
   ```bash
   python3 -m venv /tmp/pdfvenv && /tmp/pdfvenv/bin/pip install pymupdf
   /tmp/pdfvenv/bin/python3 -c "import fitz; doc = fitz.open('/tmp/paper.pdf'); print(doc[0].get_text())"
   ```
   See `ocr-and-documents` skill → `references/temp-venv-pdf-extraction.md` for full details.

4. **Raw file location**: arXiv papers go to `wiki/raw/papers/` (NOT `wiki/raw/articles/`). The earlier claim that they go to `raw/articles/` was wrong — `raw/papers/` is the established convention per `wiki-ingestion-pipelines` Section D and existing `wiki/raw/papers/` entries.

5. **Wikilinks to subdirectory pages resolve by index name, not file path**: `[[concepts/llm-trace-judge]]` is a valid link even though the file lives at `concepts/evaluation/llm-trace-judge.md`, because the index entry is keyed by the display name. Before writing a wikilink, verify the target exists in `wiki/index.md` (search for the slug) rather than assuming the file path matches the link target. If unsure, grep `index.md` for the slug; use the link form that index.md uses.
