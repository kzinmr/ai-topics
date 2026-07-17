---
title: "CocoIndex"
type: entity
created: 2026-07-17
updated: 2026-07-17
tags:
  - open-source
  - tool
  - embeddings
  - vector-search
  - code-intelligence
  - developer-tools
  - documentation
  - postgres
aliases: [cocoindex_io]
sources:
  - raw/articles/2026-07-16_cerebras_knowledge-base-architecture.md
  - https://www.cerebras.ai/blog/how-we-built-our-knowledge-base
related:
  - "[[entities/cerebras-systems]]"
  - "[[concepts/enterprise-knowledge-base-architecture]]"
---

# CocoIndex

**CocoIndex** ([@cocoindex_io](https://x.com/cocoindex_io)) is an open-source document embedding framework that specializes in vectorizing codebases. It provides language-specific code chunking with hierarchical splitting boundaries, incremental re-embedding on commits, and native Postgres integration for synchronization metadata.

## Key Features

### Language-Specific Code Chunking

CocoIndex splits code using regex boundaries ordered from coarse to fine:
1. **Class-level** boundaries first
2. **Method-level** boundaries as fallback
3. **Smaller blocks** for remaining large chunks

A single file generates multiple embeddings at different levels of specificity (file-level, function-level), enabling granular code search.

### Incremental Synchronization

CocoIndex tracks synchronization metadata in Postgres. On each commit, it re-embeds and re-exports only the changed code chunks — no full-repository recomputation. This is particularly efficient when the embedding store and synchronization state live in the same database.

### Configuration-Driven Onboarding

Repository onboarding is driven by configuration files that teams can submit themselves, including allowlists and denylists at the file-path level. This supports large organizations with many repos (Cerebras has repos larger than 40 GB).

## Usage at Cerebras

Cerebras adopted CocoIndex to embed their internal code repositories for the Cerebras Knowledge Base. The tool enabled:
- Vector search over 40GB+ monorepos
- Per-commit incremental updates
- Multi-level embeddings (file + function) for granular retrieval
- Self-service repo onboarding via config files

See [[concepts/enterprise-knowledge-base-architecture]] for the full architecture.

## Related

- [[entities/cerebras-systems]] — Primary known user
- [[concepts/enterprise-knowledge-base-architecture]] — Architecture using CocoIndex
- [[concepts/code-intelligence]] — Code intelligence for LLMs

## References

- [Cerebras: How We Built Our Knowledge Base](https://www.cerebras.ai/blog/how-we-built-our-knowledge-base) — July 2026
- [@cocoindex_io on X](https://x.com/cocoindex_io)
