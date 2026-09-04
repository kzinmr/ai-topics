# OpenAI Blog + Paper Dual Ingestion Pattern

OpenAI regularly publishes blog posts accompanied by research papers. This pattern covers the
dual ingestion workflow when both sources are available.

## Trigger Signals
- User shares an `openai.com/index/` blog URL that references a PDF paper
- Blog mentions "our paper shows..." or links to `cdn.openai.com/pdf/...`
- User explicitly asks to ingest both the blog article and the paper

## Workflow

### Step 1: Fetch Blog via Jina Reader
OpenAI's blog is a Next.js SPA — `curl` returns an empty shell. Use Jina Reader:

```bash
curl -sL "https://r.jina.ai/https://openai.com/index/<slug>/" -H "Accept: text/markdown"
```

This returns:
- Title and publication date (often in the last lines as `[..., date](url)`)
- Full article body in clean markdown
- Links to referenced papers (look for `cdn.openai.com/pdf/` URLs)

### Step 2: Extract Paper URL
Scan the Jina output for paper links:
- Pattern: `https://cdn.openai.com/pdf/<uuid>/<paper-slug>.pdf`
- Also check for arXiv links if referenced

### Step 3: Download and Extract Paper
```bash
# Download PDF
curl -sL -o /tmp/openai-paper.pdf "<paper-url>"

# Extract text with pymupdf (always available in Hermes env)
python3 -c "
import pymupdf
doc = pymupdf.open('/tmp/openai-paper.pdf')
print(f'Pages: {len(doc)}')
for i, page in enumerate(doc):
    text = page.get_text()
    if text.strip():
        print(f'=== PAGE {i+1} ===')
        print(text)
"
```

### Step 4: Create Raw Files
1. **Raw article**: `wiki/raw/articles/{date}_openai-{slug}.md`
   - Full blog content from Jina Reader
   - YAML frontmatter with `type: article`, `source: openai.com`

2. **Raw paper**: `wiki/raw/papers/{date}_openai-{paper-slug}.md`
   - Structured summary with: abstract, key findings, methodology, data points
   - YAML frontmatter with `type: paper`, `source: openai`, `blog_url` linking back
   - Register in papers_index: `python3 scripts/papers_index.py --add <filename> <pdf-url>`

### Step 5: Create/Update Concept Page
- Create concept page that synthesizes both sources
- Reference paper's formal findings (stylized facts, methodology) alongside blog's narrative
- Cross-link to related entity pages (e.g., `[[entities/openai-codex]]`)

### Step 6: Update Existing Entity Pages
- Add both raw article and raw paper to entity's `sources:` list
- Add concept page link to entity's Related Topics section

## Example: "How Agents Are Transforming Work" (June 2026)

**Blog**: `openai.com/index/how-agents-are-transforming-work/`
**Paper**: `cdn.openai.com/pdf/5d1e1489-21c0-43e4-9d42-f87efdbf0082/the-shift-to-agentic-ai-evidence-from-codex.pdf`

Created:
- `raw/articles/2026-06-25_openai-agents-transforming-work.md` (blog content)
- `raw/papers/2026-06-25_openai-shift-to-agentic-ai.md` (50-page paper summary)
- `concepts/agentic-knowledge-work.md` (synthesized from both sources)
- Updated `entities/openai-codex.md` (added both sources + concept link)

## Pitfalls

- **Blog date extraction**: Jina Reader often appends the date at the very end of output as
  `[Title, Category, Date](url)`. Parse this carefully — it's the most reliable date source.
- **Paper has no arXiv ID**: OpenAI papers at `cdn.openai.com/pdf/` don't have arXiv IDs.
  Use `source: openai` in frontmatter and register via papers_index with the PDF URL.
- **delegate_task with browser/web may return minimal results** for OpenAI sites.
  Prefer direct `terminal` + `curl` + Jina Reader over delegation for these extractions.
- **Paper PDF is large** (50+ pages): Use pymupdf to extract all pages, then summarize
  key sections (abstract, introduction, findings, methodology) into the raw paper file.
  Don't try to include the full verbatim text — structure it for wiki consumption.
