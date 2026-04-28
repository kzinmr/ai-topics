---
title: "Jo Kristian Bergum"
type: entity
aliases:
  - jo-kristian-bergum
  - jobergum
  - Jo Bergum
created: 2026-04-25
updated: 2026-04-27
tags:
  - entity
  - person
  - search-engine
  - vespa
  - vector-search
  - norway

---

# Jo Kristian Bergum

**Jo Kristian Bergum** (also known as Jo Bergum, @jobergum) is a Norwegian search and retrieval engineer, former Distinguished Engineer at Yahoo, co-founder and Chief Scientist of Vespa.ai, and since 2025, founder and CEO of **Hornet** (hornet.dev) — a retrieval engine purpose-built for AI agents. With over two decades of experience in information retrieval, he is a leading voice on sparse and dense vector search, hybrid ranking, and large-scale serving infrastructure.

## Biography

Bergum began his career in search and recommendation systems in **2001** at **Fast Search & Transfer (FAST)**, a Norwegian search technology company headquartered in Trondheim. FAST was a seminal force in search technology, producing a generation of engineers and researchers with deep ties to the Norwegian University of Science and Technology (NTNU). Through Yahoo's acquisition of Overture (which had previously acquired FAST's technology), Bergum joined Yahoo, where he would spend the next ~18 years working on search infrastructure.

At Yahoo, Bergum became a key architect and contributor to **Vespa** — the company's internal big-data serving engine that powered search, recommendations, and ad serving across Yahoo properties. He held the title of **Distinguished Engineer** at Yahoo, reflecting his deep technical leadership.

When Yahoo spun out Vespa as an independent company in **October 2023**, Bergum was a co-founder and served as its **CTO** (and later **Chief Scientist**). After the spin-out, he continued to lead technical strategy, authoring influential blog posts on billion-scale vector search, hybrid ranking, and neural search.

By 2025, Bergum transitioned out of Vespa to found **Hornet**, a retrieval engine designed specifically for AI agent workloads. He serves as its CEO, joined by several former Vespa engineers (including CTO Henning Baldersheim and COO Erik Dyrkoren).

## Role at Vespa

- **Co-founder & CTO** — Vespa.ai (post spin-out, 2023–2025)
- **Chief Scientist** — Vespa.ai (2022–2024, as listed on Vespa blog bylines)
- **Distinguished Engineer** — Yahoo! Vespa (pre-spin-out, ~2005–2023)
- Architect and primary technical contributor to Vespa's neural search capabilities, ranking infrastructure, and tensor compute layer
- Public face of Vespa's engineering — authored the majority of Vespa's technical blog content and spoke at major search conferences

## Core Technical Contributions

Bergum's work spans traditional information retrieval, neural search, and large-scale distributed systems:

### Vector Search & Approximate Nearest Neighbor (ANN)
- **Billion-scale vector search using hybrid HNSW-IF** — Developed cost-efficient, high-accuracy ANN indexing combining HNSW (Hierarchical Navigable Small World) with inverted file (IF) structures for billion-scale datasets
- **Query-time constrained ANN** — Pioneered Vespa's ability to combine approximate nearest neighbor search with real-time query filters (metadata constraints, boolean filters) without separate vector database hops
- **Matryoshka + Binary Quantization** — Implemented support for combining Matryoshka Representation Learning (MRL) with binary quantization in Vespa's native embedder, dramatically reducing vector search costs

### Hybrid Search & Ranking
- **Hybrid sparse-dense retrieval** — Integrated BM25 (sparse keyword) with dense vector embeddings in a single unified ranking pipeline, enabling state-of-the-art zero-shot ranking performance
- **Zero-shot ranking improvements** — Published two-part series demonstrating hybrid ranking models combining multi-vector representations with BM25, achieving strong results on the BEIR benchmark without task-specific fine-tuning
- **Multi-stage ranking pipeline** — Helped architect Vespa's configurable multi-phase ranking (retrieval → lightweight reranking → deep neural reranking), enabling complex ML-powered ranking at scale

### Neural Search & Deep Learning Integration
- **ONNX model support in Vespa** — Led integration of ONNX (Open Neural Network Exchange) runtime into Vespa's ranking pipeline, allowing direct deployment of PyTorch, TensorFlow, and transformer models for inference during search
- **Vespa tensor data structure** — Contributed to Vespa's native tensor compute layer, enabling vector operations, matrix multiplication, and complex ML scoring functions directly in the search engine
- **ColPali integration** — Demonstrated how to represent and scale ColPali (vision-language model for document retrieval) in Vespa, enabling "What You See Is What You Search" — bypassing traditional text extraction for PDF retrieval

### Streaming Search & Personal Data
- **Vector streaming search** — Developed Vespa's streaming search mode for personal AI assistants, enabling per-user semantic search over private data with real-time indexing
- **RAG infrastructure** — Authored hands-on guides combining Vespa with LlamaIndex and other LLM frameworks for retrieval-augmented generation over personal and enterprise data

### MS MARCO & Benchmark Leadership
- Contributed to Vespa's strong results on the MS MARCO Passage Ranking challenge, demonstrating multiple retrieval and ranking methods within a single engine
- Published performance benchmarks comparing Vespa against Elasticsearch and Open Distro for K-NN on dense vector ranking tasks

## Key Talks & Presentations

| Year | Conference | Title |
|------|-----------|-------|
| 2022 | Vector Podcast | *Journey of Vespa from Sparse into Neural Search* — comprehensive deep-dive on Vespa architecture, tensor ranking, vector search, and his personal journey in search |
| 2022 | Berlin Buzzwords | Multiple talks including Vespa's vector search capabilities and large-scale serving |
| 2023 | Haystack EU | *Navigating Neural Search: Avoiding Common Pitfalls* — practical guidance on embedding-based retrieval |
| 2023 | Berlin Buzzwords | *The State of Neural Search and LLMs* (interview with Zeta Alpha); Panel: *The Debate Returns (with more vectors): Which Search Engine?* |
| 2024 | Haystack EU | *What You See Is What You Search: Vision Language Models & PDF Retrieval* — introducing ColPali-based document retrieval in Vespa |
| 2024 | Multiple venues | *Back to Basics for RAG* — core IR concepts for retrieval-augmented generation |

## Key Writings

### Vespa Blog (authored as Chief Scientist)
- *Pretrained Transformer Language Models for Search* — two-part series (May 2021)
- *Query Time Constrained Approximate Nearest Neighbor Search* (May 2022)
- *Billion-scale vector search using hybrid HNSW-IF* (Jun 2022)
- *Building Billion-Scale Vector Search* — two-part series (Oct 2022)
- *Improving Zero-Shot Ranking with Vespa Hybrid Search* — two-part series (Jan 2023)
- *Three Mistakes When Introducing Embeddings and Vector Search* (Apr 2023)
- *Matryoshka 🤝 Binary vectors: Slash vector search costs with Vespa* (Apr 2024)

### Medium / External
- *Will new vector databases dislodge traditional search engines?* (Sep 2022) — responded to Doug Turnbull's question on vector databases vs. traditional search
- *Managed Vector Search using Vespa Cloud* (Jul 2022)
- *Stop Using Vector Indexes (When You Don't Need Them)* (Nov 2024)
- *The Anatomy of Large-Scale Recommender Systems* (Jan 2025)
- *A Practical Guide to Benchmarking Search Systems* (Nov 2024)
- *Why separating compute from storage is a bad idea for late interaction models like ColPali* (Oct 2024)

### Hornet Blog
- *The case for a new retrieval engine for agents* (Oct 2025) — founding manifesto for Hornet

## Current Work: Hornet

In 2025, Bergum founded **Hornet** (hornet.dev), a retrieval engine built from the ground up for AI agent workloads. The company addresses the fundamental shift from human-paced queries to agent-driven search loops that issue thousands of structured queries per session. Hornet is model-agnostic, open-source, and designed to run in VPC or on-premises alongside agent infrastructure. Key team members include many ex-Vespa engineers — Henning Baldersheim (CTO), Erik Dyrkoren (COO), and others.

## Online Presence

- **X/Twitter**: [@jobergum](https://x.com/jobergum)
- **GitHub**: [jobergum](https://github.com/jobergum)
- **LinkedIn**: [jo-bergum](https://no.linkedin.com/in/jo-bergum)
- **Medium**: [bergum.medium.com](https://bergum.medium.com/)
- **Hornet**: [hornet.dev](https://hornet.dev/)

## Related Pages

- [[entities/_index]]
