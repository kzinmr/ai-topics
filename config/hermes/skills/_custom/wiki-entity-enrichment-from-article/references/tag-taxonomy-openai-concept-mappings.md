# Tag Taxonomy — OpenAI Concept Page Mappings

Additional non-canonical → canonical tag mappings discovered during OpenAI concept page batch creation (2026-06-17).

## Mappings

| Non-Canonical | Canonical | Notes |
|---|---|---|
| `culture` | `ai-organization` | Use for org culture topics |
| `product-development` | `product` | Use the shorter form |
| `personalization` | `personal-ai` | Use for personalization/AI assistant topics |
| `competitive-dynamics` | `strategy` | Use for competitive analysis |
| `healthcare` | `biotech` or `ai-safety` | No dedicated healthcare tag — choose based on context |
| `research-funding` | `research` + `philanthropy` | Use both tags together |
| `realtime-api` | `api` | Use the broader `api` tag; specificity goes in page body |

## Japanese Content Policy

**Non-raw wiki pages (entities, concepts, comparisons, events, queries) must be written in English.** The pre-commit hook detects Japanese content (hiragana, katakana, CJK) in non-raw files and blocks the commit. Only `raw/` and `transcripts/` directories can contain non-English content.

When creating concept pages from Japanese-language sources:
1. Translate all section headers and body text to English
2. Keep source quotes in original language only if block-quoted with attribution
3. Frontmatter must always be English

## Pre-Ingestion Duplicate Check

Before batch-processing raw articles into concept pages, check ALL wiki directories — not just the target:

```
# Check index.md for existing coverage
search_files(pattern="<article-topic>", path="wiki/index.md")

# Check across all Layer 2 directories
search_files(pattern="<topic>", path="wiki/concepts", target="files")
search_files(pattern="<topic>", path="wiki/entities", target="files")
search_files(pattern="<topic>", path="wiki/events", target="files")
```

Many articles are already ingested in non-obvious locations (e.g., `concepts/gpt/`, `events/`, `entities/`). Processing duplicates wastes time and creates conflicting pages.

**Real example (2026-06-17)**: 5 out of 30 OpenAI raw articles were already covered:
- `2026-06-08_openai-built-to-benefit-everyone.md` → `events/2026-06-08-openai-built-to-benefit-everyone.md`
- `2026-06-10_openai-deployment-safety-hub.md` → `concepts/gpt/gpt-deployment-safety-hub.md`
- `2026-06-04_openai_frontier-safety-blueprint.md` → `concepts/frontier-safety-blueprint.md`
- `2026-06-04_openai_gpt-rosalind-new-capabilities.md` → `concepts/gpt/gpt-rosalind.md`
- `2026-06-07_reuters_openai-chatgpt-intent-router.md` → `concepts/gpt/chatgpt-intent-router.md`

See also: `references/pre-ingestion-duplicate-check.md` for the full checklist.
