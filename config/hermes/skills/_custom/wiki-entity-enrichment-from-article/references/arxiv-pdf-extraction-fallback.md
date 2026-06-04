# arXiv PDF Extraction Fallback

When `web_extract` fails on arXiv (common — returns "Conversion to HTML had a Fatal error" for many papers, especially large ones), use this fallback chain.

## Fallback Priority for arXiv Papers

| Priority | Method | When to use | Notes |
|----------|--------|------------|-------|
| 1 | `web_extract` on `arxiv.org/abs/ID` | Always try first | Gets metadata (authors, abstract) even when PDF conversion fails |
| 2 | `browser_navigate` on `arxiv.org/abs/ID` | Metadata-only (authors, abstract, dates) | Snapshot gives structured metadata via accessibility tree |
| 3 | `curl` + `pymupdf` on `arxiv.org/pdf/ID` | Full text extraction | The reliable fallback; requires pymupdf installation |

## curl + pymupdf Pattern

```bash
# Step 1: Download PDF
curl -sL -o /tmp/paper.pdf "https://arxiv.org/pdf/2508.18255"

# Step 2: Install pymupdf (may need --break-system-packages on PEP 668 systems)
python3 -m pip install --break-system-packages pymupdf -q

# Step 3: Extract text
python3 -c "
import fitz
doc = fitz.open('/tmp/paper.pdf')
text = ''
for page in doc:
    text += page.get_text()
print(f'Pages: {len(doc)}, Chars: {len(text)}')
with open('/tmp/paper.txt', 'w') as f:
    f.write(text)
doc.close()
"
```

## Key Points

- **Always try Step 1+2 first** — `browser_navigate` is fast and gives you the title, authors, abstract, and submission dates, which are needed for the raw paper frontmatter
- **Only fall back to pymupdf** when `web_extract` returns a "Fatal error" for both abs and PDF URLs
- `pip install --break-system-packages` is needed on Ubuntu/PEP 668 systems where system pip is locked
- pymupdf installs to `~/.local/bin` — it's available to `python3 -c` even if not on PATH
- The extracted text preserves section structure, tables, and equations as plain text
- 40-page papers (~145K chars) extract in <5 seconds

## Pitfalls

- **Don't skip the metadata step**: pymupdf gives raw text without structured metadata. Use `browser_navigate` on the abs page first to get authors with X handles, dates, and the abstract
- **Don't assume pymupdf is installed**: it's not a system package. Always try `import fitz` first or install it
- **Don't use `web_extract` on PDF URLs as primary**: it routes through ar5iv HTML conversion, which is the exact thing failing
- **Clean up**: `/tmp/paper.pdf` and `/tmp/paper.txt` can be removed after saving to `wiki/raw/papers/`
