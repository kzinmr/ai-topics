# Google Drive PDF Extraction & Wiki Ingestion

Pattern for fetching PDFs from Google Drive links and ingesting them into the wiki.

## Google Drive Direct Download

Google Drive file IDs can be downloaded directly without authentication:

```bash
# Extract file ID from URL: https://drive.google.com/file/d/<FILE_ID>/view
FILE_ID="1qzKI4DKnyHRpXK1J3ATPqwaqLc0iNu-M"
curl -L "https://drive.google.com/uc?export=download&id=${FILE_ID}" -o /tmp/gdrive_file.pdf --max-time 60
```

### Verify Download

```bash
# Check it's actually a PDF (not an HTML error page)
head -c 10 /tmp/gdrive_file.pdf | cat -v
# Should start with: %PDF-1.
# If you see <!DOCTYPE or <html, the download was blocked or the file isn't public
```

### Pitfalls
- Large files (>100MB) may require a confirmation token — add `&confirm=t` to the URL
- Files requiring sign-in will return HTML login page instead of PDF — verify with `head -c 10`
- Rate limiting: Google may throttle repeated downloads; add delays for batch operations

## PDF Text Extraction with pymupdf

pymupdf (`import pymupdf`) is available on the Hermes runtime at `~/.local/lib/python3.13/site-packages/`:

```python
import pymupdf

doc = pymupdf.open('/tmp/gdrive_file.pdf')
print(f'Pages: {len(doc)}')
print(f'Metadata: {doc.metadata}')  # title, author, creationDate, etc.

# Extract all text
full_text = []
for i, page in enumerate(doc):
    text = page.get_text()
    full_text.append(f'=== Page {i+1} ===\n{text}')

# Save to temp file for further processing
with open('/tmp/extracted.txt', 'w') as f:
    f.write('\n\n'.join(full_text))
```

### Pitfalls
- **Scanned PDFs** (image-only) return empty text — would need OCR (not covered here)
- **Large PDFs (50+ pages)**: Extract page-by-page and use targeted sections rather than loading all into context
- **Tables in PDF**: pymupdf extracts text linearly; table structure may be lost. Use `page.get_text("blocks")` for better structure preservation
- `file` command may not be available on all environments — use `head -c 10 | cat -v` instead

## Full Pipeline: Google Drive PDF → Wiki Page

1. **Download**: `curl -L "https://drive.google.com/uc?export=download&id=<ID>" -o /tmp/gdrive.pdf`
2. **Verify**: `head -c 10 /tmp/gdrive.pdf | cat -v` — must start with `%PDF`
3. **Extract metadata**: `python3 -c "import pymupdf; doc = pymupdf.open('/tmp/gdrive.pdf'); print(doc.metadata)"`
4. **Extract text**: Full extraction to temp file, then `read_file` in chunks
5. **Check existing wiki**: Search `index.md` + related concept/entity pages before creating new content
6. **Save raw PDF**: `cp /tmp/gdrive.pdf wiki/raw/papers/YYYY-MM-DD_<source>_<slug>.pdf`
7. **Create/enrich wiki page**: Prefer patching existing pages over creating new standalone pages
8. **Update index.md + log.md**: Always update both after wiki changes
9. **Commit + push**: `cd ~/ai-topics && git add wiki/ && git commit -m "wiki: ..." && git push`

### Pre-Ingestion Checks (Critical)

Before creating a new wiki page from a PDF:
1. Search `index.md` for existing coverage of the topic
2. Search `git log` for prior work on the topic
3. Check `concepts/` and `entities/` for related pages
4. **If an existing page covers the topic, enrich it** — don't create a duplicate

### Naming Convention for Raw PDFs

`wiki/raw/papers/YYYY-MM-DD_<source-slug>_<topic-slug>.pdf`

Examples:
- `2026-06-24_huashu_loop-engineering-anthropic-playbook.pdf`
- `2026-05-15_openai_building-effective-agents.pdf`

### Enriching Existing Pages

When a PDF covers a topic already in the wiki:
1. Read the existing page fully (`read_file`)
2. Identify sections that can be expanded or new sections to add
3. Use `patch` (not `write_file`) to add content — preserves existing content
4. Add the PDF to the page's `sources` frontmatter
5. Update the `updated` date in frontmatter
6. Add new external wikilinks (minimum 2 per page)
