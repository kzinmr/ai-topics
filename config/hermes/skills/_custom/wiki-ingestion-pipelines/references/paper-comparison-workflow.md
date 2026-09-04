# Paper/System Card Comparison Workflow

When the user provides a URL to a new paper and asks to compare it with an existing wiki paper.

## Trigger Signals
- User provides PDF URL + says "compare with [existing page]"
- User provides PDF URL + says "compare this with" (Japanese: このものと比較して)
- Two related system cards / technical reports need side-by-side analysis

## Workflow

### 1. Ingest New Paper (see pdf-paper-ingestion.md)
```bash
mkdir -p ~/wiki/raw/papers
curl -sL "<URL>" -o ~/wiki/raw/papers/<filename>.pdf
```
Extract text with PyMuPDF, add frontmatter, save as `.md`.

### 2. Read Key Sections from Both Papers
Focus on comparable sections:
- Executive summary / abstract
- Risk evaluations (RSP, CB, cyber)
- Alignment assessment summary
- Model welfare findings
- Capability benchmarks
- Key methodological differences

Use `search_files` to locate section headers, then `read_file` with offset/limit.

### 3. Create Comparison Page
Path: `wiki/comparisons/<descriptive-slug>.md`

Structure:
```yaml
---
title: "Comparison: X vs Y"
created: YYYY-MM-DD
type: comparison
tags:  # MUST be in SCHEMA.md — see precommit-pitfalls.md
  - ...
sources:
  - "[[raw-paper-page-1]]"
  - "[[raw-paper-page-2]]"
  - "<url1>"
  - "<url2>"
---
```

Body should include:
- Overview table (pages, date, scope, baseline)
- Section-by-section comparison with tables
- Key changes / evolution summary
- References to both raw papers via `[[wikilinks]]`

### 4. Update index.md
- Find `## Comparisons (N pages)` section
- Increment count N → N+1
- Add entry in alphabetical order with brief description

### 5. Update log.md
Append entry with date and summary of changes.

### 6. Commit + Push
```bash
cd ~/ai-topics && git add wiki/ && git commit -m "wiki: ..." && git push
```

**If blocked by pre-commit**: See precommit-pitfalls.md for tag violations, language blocks, etc.

## Pitfalls
- **English only**: Comparison pages are non-raw/ content -> must be English even if user writes in Japanese
- **Tag mapping**: `claude` -> `model`, `system-card` -> `evaluations`/`ai-safety`, `model-evaluation` -> `evaluations`
- **Sources format**: Use multi-line YAML array, NOT single-line `[...]` format
- **Existing comparison check**: Before creating a new comparison, check if one already exists: `search_files(pattern="comparison-slug", target="files", path="wiki/comparisons/")`
