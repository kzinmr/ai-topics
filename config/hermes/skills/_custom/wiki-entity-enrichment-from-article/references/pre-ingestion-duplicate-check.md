# Pre-Ingestion Duplicate Check — Preventing Redundant Wiki Pages

When batch-processing raw articles into wiki concept/entity pages, check for existing coverage BEFORE writing new pages.

## The Problem

Raw articles often have overlapping topics with existing wiki pages. Processing duplicates wastes time, creates conflicting content, and may result in orphan pages.

## Checklist (before creating any new concept page)

### 1. Search index.md for existing coverage
```python
search_files(pattern="<article-topic>", path="wiki/index.md")
```
The index contains ALL wiki pages with descriptions. A single search often reveals existing pages in unexpected directories.

### 2. Search across ALL Layer 2 directories
```python
search_files(pattern="<topic>", path="wiki/concepts", target="files")
search_files(pattern="<topic>", path="wiki/entities", target="files")
search_files(pattern="<topic>", path="wiki/events", target="files")
```
Many articles are already ingested in non-obvious locations:
- Model-specific articles → `concepts/gpt/`, `concepts/claude/`
- Company announcements → `events/`
- People profiles → `entities/`
- Cross-cutting concepts → `concepts/` (flat)

### 3. Check raw article frontmatter
Many raw articles already have cross-references to existing wiki pages:
```yaml
---
tags: [openai, ai-safety, agi]
---
## Related
- [[concepts/frontier-safety-blueprint]]
- [[entities/openai]]
```
If the raw article already links to existing pages, those pages likely contain the knowledge already.

### 4. If existing page found → PATCH, don't create
- Read the existing page
- Add new information as a section or update existing sections
- Add the raw article to `sources:` frontmatter
- Update `updated:` date

### 5. If no existing page → create new page
Only create a new page when:
- The concept is genuinely novel (not covered by any existing page)
- The article provides substantial new information
- The concept meets the SCHEMA.md page thresholds (2+ sources or central to one source)

## Real Example (2026-06-17, OpenAI concept batch)

Processing 30 raw articles about OpenAI:
- `2026-06-08_openai-built-to-benefit-everyone.md` → already in `events/2026-06-08-openai-built-to-benefit-everyone.md`
- `2026-06-10_openai-deployment-safety-hub.md` → already in `concepts/gpt/gpt-deployment-safety-hub.md`
- `2026-06-04_openai_frontier-safety-blueprint.md` → already in `concepts/frontier-safety-blueprint.md`
- `2026-06-04_openai_gpt-rosalind-new-capabilities.md` → already in `concepts/gpt/gpt-rosalind.md`
- `2026-06-07_reuters_openai-chatgpt-intent-router.md` → already in `concepts/gpt/chatgpt-intent-router.md`

5 out of 30 articles were already covered. Checking first saved significant time.
