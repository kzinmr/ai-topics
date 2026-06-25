---
title: "Weaviate"
type: entity
created: 2026-05-22
updated: 2026-06-25
tags:
  - company
  - database
  - search
  - ai-agents
  - platform
  - infrastructure
  - memory
aliases: ["Weaviate Inc."]
sources:
  - raw/newsletters/2026-06-25-ainews-it-s-meta-harness-summer.md
---

# Weaviate

**Weaviate** is an open-source vector database platform that enables hybrid search (BM25 + vector) with built-in MCP server support for coding agents. Weaviate 1.37 introduced native MCP integration, allowing coding agents to perform hybrid search without additional processes.

| | |
|---|---|
| **Type** | Vector Database / AI Infrastructure |
| **Key Products** | Weaviate vector database, MCP Server, MMR Reranking, Engram |
| **Key Features** | Hybrid BM25 + vector search, built-in MCP server, MMR reranking, Engram async memory |

## Key Facts

- **Weaviate 1.37** (May 2026): Built-in MCP server enabling coding agents to perform hybrid BM25+vector search without extra processes
- **MMR Reranking**: Maximum Marginal Relevance reranking for search diversity
- **Engram GA** (June 2026) — Memory-as-asynchronous-infrastructure product for AI agents. Frames memory as a first-class systems layer that operates independently of agent execution. ([AINews, Jun 2026](https://open.substack.com/pub/swyx/p/ainews-its-meta-harness-summer))
- Hybrid search across dense vectors and BM25 lexical matching

## Related

- [[entities/exa]] — Competitor in AI search infrastructure
- [[entities/turbopuffer]] — Competitor in vector/lexical search
- [[concepts/mcp]] — Model Context Protocol used for Weaviate agent integration
- [[concepts/vector-search]] — Vector search technology
