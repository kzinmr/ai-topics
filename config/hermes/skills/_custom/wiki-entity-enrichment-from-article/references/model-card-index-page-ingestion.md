# Model Card Index Page Ingestion

When ingesting AI model documentation from provider "model cards" index pages (e.g., DeepMind's model cards hub), the workflow differs from single-article ingestion because the source is a **structured index linking to multiple sub-resources**.

## DeepMind Model Cards Pattern (deepmind.google/models/model-cards/)

The page is a structured HTML table listing two families:

### Gemini Models (PDF links)
PDFs hosted on `storage.googleapis.com/deepmind-media/Model-Cards/`. Filename conventions:
- Underscores: `Gemini_2_5_Pro_Model_Card.pdf`, `Gemini_1_5_Pro_Model_Card.pdf`
- Hyphens: `Gemini-2.5-Flash-Model-Card.pdf`, `Gemini-2.0-Flash-Lite-Model-Card.pdf`

**PITFALL**: As of 2026-06-10, most Gemini 2.x PDF URLs return `NoSuchKey` XML errors from GCS even though they are linked from the official page. Always verify downloaded files:
```bash
# Check file size — XML error responses are ~220 bytes
ls -la *.pdf
# Verify PDF header
head -c 4 file.pdf  # Should be "%PDF"
```
Only `Gemini-Robotics-On-Device-Model-Card.pdf` (412KB) was confirmed accessible. Keep the URLs in wiki pages for future re-download.

### Gemma Models (ai.google.dev subpages)
Links go to `ai.google.dev/gemma/docs/` pages (not PDFs). These are web-based model cards. Pattern: `https://ai.google.dev/gemma/docs/<variant>/model_card`.

## Ingestion Workflow

1. **Scrape the index page** → save to `wiki/raw/articles/YYYY-MM-DD_<provider>-model-cards-page.md`
2. **Parse structured tables** to extract model name, update date, and URL for each card
3. **Attempt PDF downloads** for Gemini-style PDF cards:
   - Use `curl -sL` to download
   - Verify file size > 1KB (XML errors are ~220 bytes)
   - Save valid PDFs to `wiki/raw/papers/<provider>-model-cards/`
4. **Identify existing wiki coverage**: Check `entities/` and `concepts/` for existing pages matching the model names
5. **Enrich existing pages** by adding a Model Cards section with links to all cards
6. **Create new pages** only for model families/variants not yet covered

## Concept vs Entity for Model Families

- **Model family spanning multiple generations** → `concepts/` page (e.g., `concepts/gemma-family.md` covering Gemma 1–4 + all variants)
- **Specific model generation with detailed specs** → `entities/` page (e.g., `entities/gemma-4.md` with benchmarks, architecture, pricing)
- **Individual model card** → reference link within the parent entity/concept page, not a standalone page

Example: The Gemma family has 13 models across 4 generations. Create one `concepts/gemma-family.md` with a complete model card index table, and keep `entities/gemma-4.md` for the detailed latest-generation analysis.

## Tag for Model Card Content

`model-card` tag is already in SCHEMA.md taxonomy. Use it on any page that primarily documents or indexes model cards. Also add to `concepts/model-cards-system-cards` as a cross-reference.

## Sources Pattern

When ingesting from an index page, cite both the raw scraped article AND the live URL:
```yaml
sources:
  - raw/articles/YYYY-MM-DD_provider-model-cards-page.md
  - https://provider.com/models/model-cards/
```
