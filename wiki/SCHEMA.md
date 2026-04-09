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
Newsletter emails → `scripts/process_email.py` → `raw/articles/`
The Hermes agent processes raw articles into entity/concept pages via Discord commands.
