# PDF Paper Ingestion — Non-arXiv Source Papers

Ingest papers from non-arXiv sources (company CDN PDFs, whitepapers, system cards, tech reports hosted on custom domains) into `wiki/raw/papers/`.

Distinguishes from the arXiv pipeline (`references/arxiv-paper-pipeline.md`) which handles arXiv-sourced papers with API metadata and peer-review triage.

## Workflow

### 1. Download PDF

```bash
mkdir -p ~/wiki/raw/papers && cd ~/wiki/raw/papers
curl -L -o "temp-download.pdf" "<PDF_URL>"
```

### 2. Extract Text with PyMuPDF

PyMuPDF (`fitz`) is preferred over `pdftotext` for better layout preservation.

```python
import fitz  # PyMuPDF
doc = fitz.open('temp-download.pdf')
text = ''
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    text += f'--- Page {page_num + 1} ---\n'
    text += page.get_text()
    text += '\n\n'
with open('output.md', 'w', encoding='utf-8') as f:
    f.write(text)
print(f'Extracted {len(text)} characters from {len(doc)} pages')
```

Run via terminal (NOT execute_code — blocked in cron mode):

```bash
python3 -c "import fitz; ..."
```

For large PDFs (100+ pages), the inline Python may hit shell quoting issues. Write to `/tmp/extract.py` first:

```bash
write_file("/tmp/extract.py", <python_code>)
terminal("python3 /tmp/extract.py")
```

### 3. Rename File

Convention: `{YYYY-MM-DD}_{source}_{short-title}.md`

- Date = publication date (from PDF metadata or title page), NOT ingestion date
- Source = publisher domain or org name (e.g., `anthropic`, `openai`, `meta-fair`)
- Short-title = kebab-case slug

```bash
mv output.md 2026-06-09_anthropic_claude-fable5-mythos5-system-card.md
mv temp-download.pdf claude-fable5-mythos5-system-card.pdf
```

Keep the PDF alongside the .md file if it's a primary source (system cards, official reports).

### 4. Add YAML Frontmatter

Use `patch` tool (NOT `write_file` — preserves existing content):

```yaml
---
title: "Full Paper Title"
created: YYYY-MM-DD
source: <PDF_URL>
type: paper
tags:
  - <tag1>
  - <tag2>
notes: |
  Brief description of the paper and its significance.
---
```

**Tag validation**: All tags must exist in `wiki/SCHEMA.md`. Check before committing:
```bash
grep -i "tagname" ~/ai-topics/wiki/SCHEMA.md
```

### 5. Update log.md

Append entry at the end of log.md with:
- Section header: `## [YYYY-MM-DD] Paper Ingest — <Short Title>`
- Bullet list of key findings from the paper
- Source URL

### 6. Update index.md — Raw Papers Section

If `## Raw Papers` section does not exist in index.md, create it **before** the `## Transcripts` section:

```markdown
## Raw Papers (N pages)

- [[raw/papers/filename]] — Brief description.
```

If the section already exists:
- Add the new entry in alphabetical or chronological order
- Update the section count in the header

### 7. Commit and Push

```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: Add <title> to raw/papers" && git push
```

## Naming Examples

| Source | URL Pattern | Filename |
|--------|------------|----------|
| Anthropic system card | `www-cdn.anthropic.com/...pdf` | `2026-06-09_anthropic_claude-fable5-mythos5-system-card.md` |
| OpenAI technical report | `cdn.openai.com/...pdf` | `2026-03-15_openai_gpt5-system-card.md` |
| Meta FAIR paper | `ai.meta.com/...pdf` | `2026-02-01_meta-fair_llama4-report.md` |
| Google DeepMind | `storage.googleapis.com/...pdf` | `2026-04-10_deepmind_gemma3-report.md` |

## Pitfalls

- **`execute_code` blocked in cron mode**: Use `write_file` + `terminal python3` for extraction scripts. Do NOT use inline `python3 -c` for complex extraction (shell quoting issues with large code).
- **Large PDFs (300+ pages)**: Text extraction produces 500K+ chars. This is fine for raw/papers/ — they're Layer 1 (immutable source material). Don't try to summarize or truncate.
- **PDF with images/scanned pages**: PyMuPDF `get_text()` returns empty for image-only pages. Check output size; if <100 chars per page, the PDF may be scanned. Fall back to OCR tools if needed.
- **Frontmatter via `write_file` overwrites content**: Always use `patch` to prepend frontmatter to existing extracted text. Using `write_file` will destroy the extracted content.
- **"Raw Papers" section placement in index.md**: Must go BEFORE `## Transcripts` section. Check with `grep -n "^## Transcripts" wiki/index.md` to find the insertion point.
- **PDF alongside .md**: Keep the original PDF in the same directory when it's a primary source document (system cards, official reports). Don't keep PDFs for papers that are freely available on arXiv.
- **Tag hygiene**: Non-arXiv papers often introduce new org/model names as tags. Check SCHEMA.md first; add missing tags before committing.
- **Language policy applies to derived pages**: When creating comparison pages or concept pages from ingested papers, the wiki language policy (English-only for non-raw/ content) still applies. Even if the user communicates in Japanese, all section headers, tables, and prose in comparison/concept/entity pages must be English. Raw papers in `raw/papers/` are exempt (Layer 1 immutable).
- **Comparison page workflow**: When the user provides a new paper URL and asks to compare with an existing wiki paper, the sequence is: (1) download + extract new paper to `raw/papers/`, (2) read key sections from both papers, (3) create comparison page in `wiki/comparisons/`, (4) update `index.md` (increment comparison count + add entry), (5) update `log.md`, (6) commit + push. Load `wiki-comparison-page-routing` skill if available for comparison page structure guidance.
