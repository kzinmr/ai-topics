# Wiki Schema — AI Topics Knowledge Base

## Domain
AI/ML technology trends, research papers, tools, frameworks, and industry developments.
Focused on: AI agents, LLMs, training techniques, inference optimization, safety, and developer tooling.

## Conventions

### Frontmatter (required for all Layer 2 pages)
```yaml
---
title: "Page Title"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [tag1, tag2]
aliases: ["alternative name"]
---
```

### Wikilinks
Use `[[page-name]]` for internal links. Use `[[page-name|display text]]` for custom display.

### File Naming
- Lowercase, hyphen-separated: `transformer-architecture.md`
- Entities: `entities/openai.md`, `entities/andrej-karpathy.md`
- Concepts: `concepts/rag-retrieval-augmented-generation.md`
- Comparisons: `comparisons/rag-vs-llm-wiki.md`

### Directory Structure Policy

#### Layer 1 — Raw Sources (`raw/`)
Immutable source material. The agent reads but never modifies these files.
Only content that has been triaged and deemed worth preserving goes here.
- **`raw/articles/`** — Scraped web articles (auto from `process_email.py`, or manually ingested)
- **`raw/papers/`** — arXiv papers, PDFs (reserved)
- **`raw/transcripts/`** — Podcast/interview transcripts (reserved)
- **`raw/assets/`** — Images, diagrams referenced by sources (reserved)

Note: Newsletter digests and RSS scan reports live in `inbox/` (outside wiki/),
not in `raw/`. The `inbox/` is the pipeline output before triage; `raw/` is the
curated source archive.

#### Layer 2 — Curated Knowledge
Hermes agent processes `raw/` into structured knowledge pages:
- **`entities/`** — People, companies, products, organizations (who/what)
- **`concepts/`** — Single ideas, frameworks, methodologies, techniques (how/why)
- **`comparisons/`** — Technical comparisons of two or more tools, models, or approaches
  - Rule: If a page is primarily evaluating alternatives against each other (features, trade-offs, selection criteria), it belongs in `comparisons/`
  - File naming: Use `vs` separator for comparisons (e.g., `langsmith-vs-braintrust.md`, `rag-vs-graph.md`)
  - Comparisons should include a structured table or matrix, not just narrative text
  - Related single-concept pages (e.g., `ai-evals.md`) stay in `concepts/`; only multi-tool/framework comparisons go in `comparisons/`
- **`queries/`** — Research query results (reserved)

### Tag Taxonomy
- **domain:** `ai-agents`, `llm`, `training`, `inference`, `safety`, `tooling`, `research`
- **type:** `framework`, `model`, `technique`, `paper`, `product`, `company`, `person`
- **status:** `active`, `archived`, `emerging`, `deprecated`
- **source:** `newsletter`, `auto-ingested`, `manual`, `arxiv`

### Source Attribution
All claims should link to their source in `raw/` via `[[raw/articles/filename]]`.

### Contradiction Handling
When sources disagree, note both positions with dates and sources.
Use `> [!warning] Contradiction` callout blocks.

## Auto-Ingestion Pipeline

```
Subscription & Receiving:
  Newsletter emails → process_email.py → inbox/newsletters/ (digest)
                                        → raw/articles/     (scraped links)
  RSS feeds → blogwatcher-cli (cron)    → inbox/rss-scans/   (scan report)

Triage (Hermes agent):
  inbox/* → identify important articles → ingest into raw/articles/ or raw/papers/

Curation (Hermes agent, llm-wiki skill):
  raw/* → entities/, concepts/, comparisons/, queries/
  → index.md, log.md updated
  → git push
```
