---
title: "LlamaIndex"
type: entity
tags:
  - llamaindex
  - rag
  - data-framework
  - ai-agents
created: 2026-04-27
updated: 2026-04-28
aliases: [LlamaIndex Framework, GPT Index, Llama Hub]
related: [[langchain]], [[agent-orchestration-frameworks]], [[rags]], [[context-engineering]], [[llamaparse]], [[llamacloud]]
sources: [https://www.llamaindex.ai/, https://github.com/run-llama/llama_index, https://developers.llamaindex.ai/]
---

# LlamaIndex

## Overview

LlamaIndex (formerly GPT Index) is an open-source data framework for building LLM-powered applications, with a particular focus on **Retrieval-Augmented Generation (RAG)** and **enterprise data agents**. Created by **Jerry Liu** and launched in late 2022, it provides a modular toolkit for ingesting, indexing, retrieving, and synthesizing data from diverse sources — enabling LLMs to reason over proprietary and structured data. The framework supports Python and TypeScript under the MIT License.

LlamaIndex popularized **context engineering** as a discipline in 2025 — emphasizing that how information is structured and delivered to LLMs matters as much as model capability.

## History & Key Milestones

| Date | Milestone |
|------|-----------|
| Late 2022 | Initially released as **GPT Index** by Jerry Liu |
| 2023 | Renamed to **LlamaIndex**; rapid community growth in the LLM application ecosystem |
| Jun 2023 | Raised **$8.5M seed round** led by Greylock; Simon Suo joins as CTO |
| 2023 | Surpassed **600,000+ monthly downloads**; became the leading RAG framework |
| Jan 2024 | Launched **LlamaIndex CLI** — RAG as a one-liner |
| Feb 2024 | Launched **LlamaParse** — enterprise document parsing platform |
| Mar 2024 | LlamaParse launched independently as the first GenAI-native document parser |
| May 2024 | Introduced **Property Graph Index** — knowledge graph integration |
| Jun 2024 | **LlamaDeploy** (formerly llama-agents) — turn agents into microservices |
| Jul 2024 | **LlamaTrace** — first-class observability platform |
| Aug 2024 | Introduced **Workflows** (beta) — event-driven orchestration engine |
| Sep 2024 | **LlamaParse Premium Mode** — advanced parsing capabilities |
| Mar 2025 | Raised **$19M Series A**; **LlamaCloud** GA — managed platform for deploying data agents |
| Jun 2025 | **Workflows 1.0** — stable release of the event-driven orchestration engine |
| 2025 | Native **MCP (Model Context Protocol)** integration launched |
| 2025 | Introduced **Document Agents** — specialized sub-agents per document coordinated by a meta-agent |
| 2026 | Vision for **"agents go from workflows to employees"** — increasingly autonomous document processing agents |

## Core Architecture

LlamaIndex uses a modular, layered architecture with fully swappable components:

### Data Ingestion Layer
- **Connectors** — 300+ integration packages via LlamaHub covering cloud storage, databases, file formats, APIs, and enterprise systems
- **Documents** — generic containers for any data source (PDF, API, DB, web page) with metadata and relationship annotations
- **Node Parsers** — customizable chunking strategies: fixed-size, sentence-aware, semantic, and custom

### Indexing Layer
- **Nodes** — chunked units of Documents; the first-class indexed entity with metadata and relationship pointers
- **Index Types:**
  - **Vector Store Index** — semantic search with embeddings (standard for RAG)
  - **Summary Index** — extractive summarization
  - **Tree Index** — hierarchical document structure
  - **Keyword Table Index** — keyword-based retrieval
  - **Property Graph Index** — knowledge graph-based indexing (introduced May 2024)

### Retrieval Layer
- **Retrievers:** Vector (cosine similarity), Keyword (BM25), Hybrid (dense + sparse), Router, Auto-Merging, Recursive
- **Advanced RAG Patterns:**
  - Sentence Window Retrieval — retrieve sentences, expand to surrounding context
  - Parent-Child Retrieval — index small chunks, retrieve larger parent chunks
  - Recursive Retrieval — traverse node relationships for broader context
  - Hybrid Search — dense vectors + sparse BM25 for higher recall
  - Reranking — cross-encoder/reranker re-scores retrieved Nodes

### Synthesis Layer
- **Query Engines** — combine Retriever + Response Synthesizer
  - Types: Simple, Sub-Question, Router, SQL, Pandas, Citation
  - Fully composable and chainable
- **Response Synthesizers:**
  - Refine (iterative refinement)
  - Compact (context-window optimized)
  - Tree Summarize (hierarchical summarization)
  - Simple Summarize

### Workflows (v1.0, Jun 2025)
- Event-driven, async-first orchestration engine replacing chain-based patterns
- Typed state, resource injection, OpenTelemetry/Arize Phoenix observability
- Stateful execution (pause/resume)
- Supported as standalone packages: `llama-index-workflows` / `@llamaindex/workflow-core`
- Branching, looping, conditional execution, and parallel processing

## Agent Capabilities

LlamaIndex extends beyond passive retrieval into autonomous reasoning and action:

- **Tool use** — APIs, code execution, database queries
- **Planning & multi-step reasoning** — break complex queries into sub-problems
- **Conversation memory** — maintain state across interactions
- **Self-reflection & retry logic** — evaluate answer quality and re-retrieve when needed

### Document Agents Pattern
- Specialized sub-agents assigned to individual documents
- Coordinated by a meta-agent that routes queries to the appropriate document agent
- Enables question-answering across large document corpora

### Router Agent
- Classifies incoming queries and routes to the optimal retrieval strategy
- Adaptive retrieval based on query type

### Multi-Step Query Decomposition
- Breaks complex questions into sub-queries
- Aggregates results into coherent answers

### Self-Correcting Retrieval
- Evaluates context adequacy
- Triggers additional retrieval rounds when context is insufficient

## The LlamaIndex Ecosystem

| Product | Type | Description |
|---------|------|-------------|
| **LlamaIndex** | Open-source framework | Core Python/TypeScript framework for building RAG and agent apps |
| **LlamaParse** | Commercial product | GenAI-native document parsing — best-in-class for complex documents |
| **LlamaCloud** | Commercial platform | Managed deployment platform for data agents and RAG apps (GA Mar 2025) |
| **LlamaDeploy** | Open-source | Turn agents into microservices (event-driven architecture) |
| **LlamaTrace** | Commercial product | Observability platform for LlamaIndex applications (with Arize AI) |
| **LlamaHub** | Open-source | 300+ integration packages for connectors, tools, and vector stores |
| **create-llama** | Open-source CLI | One-liner for spinning up full-stack RAG applications |

## Funding & Business

- **Total raised:** ~$28M
- **Seed (Jun 2023):** $8.5M led by Greylock
- **Series A (Mar 2025):** $19M led by Dave Zilberman
- **Key investors:** Greylock, 468 Capital, Andreessen Horowitz, Index Ventures, Spark Capital
- **Key people:** Jerry Liu (CEO, co-founder), Simon Suo (CTO, co-founder)

## Key Concepts Coined
- **Context Engineering** — the discipline of optimizing how information is structured and delivered to LLMs (2025)

## Related Concepts
- [[langchain]] — Competing general-purpose LLM application framework
- [[rags]] — Retrieval-Augmented Generation patterns and techniques
- [[agent-orchestration-frameworks]] — Comparative analysis of agent frameworks
- [[context-engineering]] — Discipline popularized by LlamaIndex
- [[llamaparse]] — Enterprise document parsing
- [[llamacloud]] — Managed deployment platform
- [[mcp]] — Model Context Protocol (natively supported in LlamaIndex)
- [[dspy]] — Declarative LM programming framework (alternative paradigm)

## Sources
- [LlamaIndex Official Site](https://www.llamaindex.ai/)
- [GitHub Repository](https://github.com/run-llama/llama_index)
- [LlamaIndex Documentation](https://developers.llamaindex.ai/)
- [LlamaIndex 2024 Year In Review](https://www.llamaindex.ai/blog/the-year-in-llamaindex-2024)
- [AI Wiki: LlamaIndex](https://aiwiki.ai/wiki/llamaindex)
- [Forbes Profile: LlamaIndex](https://www.forbes.com/profile/llamaindex/)
