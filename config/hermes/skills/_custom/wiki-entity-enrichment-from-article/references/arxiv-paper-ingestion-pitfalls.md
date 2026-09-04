# arXiv Paper Ingestion — Common Pitfalls

## 1. Tag Taxonomy Violation on Commit

When creating a new concept page with a tag not yet in `wiki/SCHEMA.md`, the pre-commit hook blocks the commit. This is especially common with arXiv paper ingestion where specialized tags (e.g., `scaling-laws`, `dense-retrieval`, `neural-ranking`) may not exist yet.

**Prevention checklist:**
1. Before writing the concept page, grep SCHEMA.md for your planned tags
2. If any tag is missing, `patch` SCHEMA.md to add it to the appropriate category (Techniques, Models, etc.)
3. Then `git add wiki/` and commit — both files go in together

**Recovery if commit was blocked:**
```bash
# Add missing tag to SCHEMA.md
# Then re-add everything and commit
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: ..."
```

## 2. PDF Text Extraction Chain

When `pdftotext` (poppler-utils) is not available:

```bash
python3 -m pip install --break-system-packages pymupdf
```

```python
import fitz
doc = fitz.open('/tmp/paper.pdf')
text = ''.join(page.get_text() for page in doc)
```

**Order of preference:** pdftotext → pymupdf → arxiv HTML endpoint → web_extract

The arxiv HTML endpoint (`https://arxiv.org/html/{id}`) is NOT available for most papers — it only works when authors uploaded LaTeX source that can be converted.

## 3. Raw Paper vs Concept Page

- **Raw paper** → `wiki/raw/papers/{arxiv_id}_{short-title}.md` — metadata + abstract + key findings (immutable source)
- **Concept page** → `wiki/concepts/{topic-name}.md` — synthesized analysis, cross-references, design guidelines

The arxiv skill's "Wiki Ingestion" section covers this but the distinction is easy to miss.

## 4. Updating Existing Concept Pages

When a new paper relates to an existing concept (e.g., adding embedding-dimension-scaling-laws to the existing `scaling-laws` page):
- Use `patch` (not `write_file`) to add a new subsection
- Add the paper to the existing page's `sources` list
- Create the new detailed concept page separately
- Cross-link both ways: existing page references new page, new page `[[wikilinks]]` back
