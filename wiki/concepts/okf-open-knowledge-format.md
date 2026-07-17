---
title: "OKF (Open Knowledge Format)"
type: concept
created: 2026-07-17
updated: 2026-07-17
tags:
  - knowledge-management
  - documentation
  - wiki
  - coding-agents
  - agents-md
  - context-engineering
  - google
  - langchain
  - open-source
sources:
  - raw/articles/2026-07-16_langchain_openwiki-0.2-okf.md
  - https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
  - https://github.com/GoogleCloudPlatform/knowledge-catalog
related:
  - "[[concepts/openwiki]]"
  - "[[concepts/wiki-memory]]"
  - "[[entities/langchain]]"
---

# OKF (Open Knowledge Format)

OKF (Open Knowledge Format) is a proposed standard from **Google Cloud** for structuring knowledge wikis, designed to make codebase documentation machine-readable and agent-navigable. It defines a lightweight set of conventions — YAML frontmatter for page metadata, `index.md` for directory summaries, and `log.md` for audit trails — that together create a deterministic, queryable knowledge base structure.

## Core Conventions

### YAML Frontmatter

Every wiki page in OKF carries structured metadata:

```yaml
---
type: <Type name>                  # REQUIRED - identifying concept of the doc
title: <Optional display name>
description: <Optional one-line summary>
resource: <Optional canonical URI for the underlying asset>
tags: [<tag>, <tag>, ...]          # Optional
timestamp: <ISO 8601 datetime>     # Optional last-modified time
---
```

This is deliberately minimal — the `type` field is the only required key, making it easy to integrate into existing documentation pipelines.

### index.md — Directory Summaries

Each wiki directory contains an `index.md` that summarizes its files and subdirectories. The index can be generated deterministically by extracting the `description` field from each file's YAML frontmatter:

```markdown
# Section / Group Heading

* [Title 1](relative-url-1) - description of item 1
* [Title 2](relative-url-2) - description of item 2
```

### logs.md — Change Tracking

`logs.md` tracks wiki updates over time, functioning as an append-only changelog. After documentation changes, tools update `logs.md` with a timestamped entry describing what changed, which files were touched, and where to look for more detail.

## Agent Retrieval Benefits

OKF adds structured metadata that enables **deterministic search** over tags, categories, descriptions, and resource URLs. Instead of relying entirely on open-ended agentic semantic search, coding agents can filter precisely:

- All docs in the `BigQuery tables` category
- Every doc tagged `billing`
- All pages with a specific `type` value

Agentic search is useful but can be unnecessarily slow and expensive for simple lookups. Structured metadata gives agent documentation tools a cleaner path toward faster, cheaper retrieval.

## Ecosystem

Because OKF is an open format, compatible tools can interoperate:

- **Google Cloud Knowledge Catalog** — Reference implementation and visualizer at `github.com/GoogleCloudPlatform/knowledge-catalog`. Includes an open-source wiki visualizer for inspecting relationships between documents.
- **OpenWiki** (LangChain) — First major adopter; generates and maintains OKF-format wikis from codebases (see [[concepts/openwiki]])
- **OWOX ecosystem tools** — Community-built viewers, renderers, and linters documented at [owox.com/blog/articles/okf-ecosystem-tools](https://www.owox.com/blog/articles/okf-ecosystem-tools)

## Adoption

### OpenWiki 0.2 (July 2026)

[[LangChain|entities/langchain]] adopted OKF as the native format for OpenWiki 0.2. Wikis generated or updated by OpenWiki now include YAML frontmatter with `title`, `description`, `tags`, `categories`, and `resource` URLs. The changelog convention (`logs.md`) is particularly valuable — after each OpenWiki run, agents and developers can check what changed without re-reading the entire wiki.

See [[concepts/openwiki]] for full details on the OpenWiki integration.

## Comparison with Other Wiki Knowledge Formats

| Aspect | OKF | Karpathy LLM Wiki | Wiki Memory |
|--------|-----|-------------------|-------------|
| **Origin** | Google Cloud (enterprise docs) | Individual knowledge management | Agent context engineering |
| **Primary consumer** | Coding agents, deterministic search | Human + LLM dual-use | Long-running autonomous agents |
| **Metadata** | YAML frontmatter (type, tags, resource, timestamp) | YAML frontmatter (created, updated, tags, sources) | YAML frontmatter + AGENTS.md pointers |
| **Change tracking** | `logs.md` (append-only changelog) | `log.md` (append-only, manual) | File-based state diffing |
| **Index** | `index.md` (generated from frontmatter) | `index.md` (manual, alphabetical) | Agent-discovered via `AGENTS.md` |

## Related Concepts

- [[concepts/openwiki]] — First major OKF adopter
- [[concepts/wiki-memory]] — Harrison Chase's wiki-as-context thesis
- [[concepts/context-engineering]] — The discipline OKF serves (structured context generation)
- [[concepts/coding-agents]] — Primary consumer of OKF-structured documentation
- [[entities/google]] — Originator of the OKF spec

## References

- [OKF Spec](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) — Google Cloud
- [Google Cloud Knowledge Catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog) — Reference implementation
- [OpenWiki 0.2 OKF announcement](https://x.com/i/article/2077795070166913027) — LangChain AI (July 2026)
