# Temporary Venv for PDF Extraction

When the main Hermes venv (`/opt/hermes/.venv/`) has permission issues that prevent installing `pymupdf`, create a disposable temp venv:

```bash
python3 -m venv /tmp/pdfenv
/tmp/pdfenv/bin/pip install pymupdf -q
```

Then extract text:

```python
/tmp/pdfenv/bin/python3 << 'PYEOF'
import pymupdf

doc = pymupdf.open("/tmp/input.pdf")
print(f"Pages: {len(doc)}")

full_text = []
for i, page in enumerate(doc):
    text = page.get_text()
    full_text.append(f"--- Page {i+1} ---\n{text}")

combined = "\n".join(full_text)
with open("/tmp/extracted_text.txt", "w") as f:
    f.write(combined)

print(f"Total chars: {len(combined)}")
PYEOF
```

## When to Use

- `uv pip install pymupdf` fails with `Permission denied` on the main venv
- `pip` / `pip3` not found (no global pip)
- Need to extract text from a PDF for wiki ingestion

## Pitfalls

- The temp venv lives at `/tmp/pdfenv` and survives within a session but may be cleaned on reboot
- For large PDFs (100+ pages), extraction completes in seconds — no need for background processing
- `pymupdf` (PyMuPDF) is preferred over `fitz` (older import name) — both work but `pymupdf` is the current package name
- The extracted text includes `--- Page N ---` markers which are useful for reference but should be stripped when creating wiki content
