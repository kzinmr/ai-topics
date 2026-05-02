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
  - search
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

|In 2025, Bergum founded **Hornet** (hornet.dev), a retrieval engine built from the ground up for AI agent workloads. The company addresses the fundamental shift from human-paced queries to agent-driven search loops that issue thousands of structured queries per session. Hornet is model-agnostic, open-source, and designed to run in VPC or on-premises alongside agent infrastructure. Key team members include many ex-Vespa engineers — Henning Baldersheim (CTO), Erik Dyrkoren (COO), and others.

## Timeline

| Date | Event |
|------|-------|
| ~2008–2010 | Joins Vespa (then Yahoo Search Technology team) as a search engineer |
| ~2010–2023 | Rises to Chief Scientist at Vespa.ai, leading retrieval architecture and research integration |
| 2020 | Publishes extensively on Vespa's hybrid search capabilities (BM25 + vector) |
| 2022 | Announces Vespa ColBERT embedder — native support for late-interaction retrieval |
| 2022 | Writes "Announcing the Vespa ColBERT embedder" blog, positioning ColBERT for production use |
| 2023 | Demonstrates ColBERT retrieval power in a browser-based demo (22M parameters) |
| 2023 | Announces search.vespa.ai — a new Vespa-powered search experience using LangChain and OpenAI |
| 2024 | Publishes "Small but Mighty" blog on using Answer.ai's ColBERT-small model in Vespa |
| 2024 | Writes on adaptive in-context learning with Vespa for retrieval-augmented generation |
| Jan 2025 | Publishes "How we build a retrieval engine for agents" — introducing Hornet's design philosophy |
| Mar 2025 | Publishes "The scaling dimensions of keyword search" — analyzing Block-Max WAND performance for agent queries |
| Oct 2025 | Publishes "The case for a new retrieval engine for agents" — the founding Hornet blog post |
| Jan 2026 | Co-authors "What we learned building a 100M-document search engine" with Elisabeth and Janne |
| Feb 2026 | Publishes "The context window is not your database" — arguing that retrieval still matters for agents |
| 2026 | Launches Hornet as a company with co-founders Henning Baldersheim (CTO), Erik Dyrkoren (COO) |

## Core Ideas

### Agents Are the New User of Search

Bergum's central insight is that the primary consumer of search is no longer humans — it's AI agents. This changes everything about retrieval infrastructure design:

> "Agents issue long, structured queries inside reasoning loops. They read entire documents and trade latency for throughput and recall. Force-fitting these workloads onto legacy retrieval infrastructure raises costs and leads to poor results."
> — Hornet.dev homepage

Human search expects short keyword queries, sub-second response times, and ranked snippets. Agent search expects long-form structured queries (sometimes hundreds of tokens), iterative retrieval loops (re-querying based on intermediate results), parallel retrieval across multiple data sources, and full-document context rather than snippets. The Hornet API is designed to "look and feel like a coding environment" because frontier models are increasingly optimized via reinforcement learning to reason through code execution and file systems.

### The Context Window Is Not Your Database

In his February 2026 blog post, Bergum (via Hornet's Head of DevRel Skip Everling) makes a crucial argument:

> "Context windows can hold more than ever, but more context doesn't mean better answers. Here's why retrieval still matters, especially for agents."
> — hornet.dev/blog, Feb 2026

The prevailing narrative in 2024–2025 was that expanding context windows (128K, 1M, even 10M tokens) would make retrieval obsolete. Bergum argues the opposite: as context windows grow, the *signal-to-noise* problem worsens. Agents need precise, relevant context injection — not just more tokens. Better retrieval produces better context, which produces better reasoning.

### Mutually Assured Distraction

In a January 2026 blog post titled "Mutually Assured Distraction," the Hornet team (with Lester Solbakken) identified a critical failure mode in agentic systems:

> "In agentic systems, retrieval is context injection. Better retrievers produce more convincing distractors; better reasoners trust those distractors more deeply. This is mutually assured distraction."
> — hornet.dev/blog, Jan 2026

This is perhaps Bergum's most conceptually rich contribution. As retrieval systems improve, they become better at surfacing documents that *look* relevant but aren't — and as reasoning models improve, they become better at constructing plausible-sounding arguments from those distractors. The result is a compounding error: better retrieval + better reasoning = more confidently wrong answers. This insight has significant implications for how retrieval systems should be designed for agentic workloads — emphasizing verifiability and explainability over raw relevance scores.

### ColBERT and Explainable Semantic Search

During his tenure at Vespa, Bergum was one of the most prominent advocates for ColBERT (Contextualized Late Interaction over BERT) as a production retrieval architecture. His key argument:

> "Genuine explainability in semantic search relies on contextual token-level embeddings, allowing each query token to interact with all document tokens. This (late) interaction also unlocks explainability. Explaining why a passage scores as it does for a query has been a significant challenge in neural search with traditional text embedding models."
> — Vespa blog, "Announcing the Vespa ColBERT embedder"

ColBERT's late-interaction approach encodes each token as a small vector rather than compressing an entire document into a single embedding. At scoring time, the MaxSim operator computes the maximum similarity between each query token and all document tokens. This provides both higher retrieval quality and — crucially — explainability. You can trace which query tokens matched which document tokens, something impossible with single-vector embeddings.

### The Speed of the Reindex-Evaluate Loop

In a March 2026 blog post about building a 100M-document search engine, Bergum's team distilled their most important lesson:

> "The biggest lesson was not about any single configuration. When every experiment takes 30 hours, the speed of your reindex-evaluate loop determines how good your system can get."
> — hornet.dev/blog, Mar 2026

This is a fundamental engineering insight about retrieval systems: iteration speed matters more than individual technique sophistication. If you can run 10 experiments in the time it takes others to run 1, you'll arrive at a better system — even if each individual experiment is less clever. Hornet's architecture is designed to maximize this iteration speed.

### Schema-First, Verifiable APIs for Agents

Hornet's API design philosophy departs from traditional search APIs in two key ways:

1. **Schema-first:** Agents need structured, predictable inputs and outputs. Free-text search APIs produce unpredictable results that are hard for agents to reason about. Hornet's schema-first approach ensures agents can programmatically understand and validate the data they retrieve.

2. **Verifiable:** The API exposes enough information about the retrieval process that agents can audit and improve their own context. "Agents stop just querying data and start improving their own context."

This connects to Bergum's broader thesis that retrieval for agents isn't just about finding relevant documents — it's about providing a programmable interface that agents can use to iteratively refine their understanding.

## Key Quotes

> "Agents need more than access to data; they need highly relevant context at scale."
> — "The case for a new retrieval engine for agents," Oct 2025

> "We've seen legacy infrastructure buckle under the new user of search: agents. We built and scaled the retrieval technologies that power consumer products and sophisticated search engines for billions of users."
> — Hornet.dev homepage

> "We know the limits of these systems because we defined them."
> — Hornet.dev homepage

> "The context window is not your database."
> — Hornet blog title, Feb 2026

> "Better retrievers produce more convincing distractors; better reasoners trust those distractors more deeply. This is mutually assured distraction."
> — Lester Solbakken, Hornet blog, Jan 2026

## Online Presence

- **X/Twitter**: [@jobergum](https://x.com/jobergum)
- **GitHub**: [jobergum](https://github.com/jobergum)
- **LinkedIn**: [jo-bergum](https://no.linkedin.com/in/jo-bergum)
- **Medium**: [bergum.medium.com](https://bergum.medium.com/)
- **Hornet**: [hornet.dev](https://hornet.dev/)

## Related Concepts

- [[concepts/colbert]] — The late-interaction retrieval model Bergum championed
- [[late-interaction]] — His primary research and engineering focus
- [[concepts/vespa]] — The search engine where he spent 15 years
- [[concepts/hornet]] — His new company, a retrieval engine for agents
- [[concepts/agentic-retrieval]] — The paradigm shift he's building for
- [[concepts/mutually-assured-distraction]] — His key insight about retrieval-reasoning compounding errors
- [[doug-turnbull]] — Fellow search relevance engineer, co-author of "AI-Powered Search"

## Sources

- Hornet.dev: https://hornet.dev
- Hornet Blog: https://hornet.dev/blog
- Vespa Blog (author page): https://blog.vespa.ai/authors/jobergum/
- LinkedIn: https://www.linkedin.com/in/jo-bergum/
- Twitter/X: @jobergum
- GitHub: https://github.com/jobergum
- Vespa ColBERT blog: https://blog.vespa.ai/announcing-colbert-embedder-in-vespa/
- Vespa ColBERT-small blog: https://blog.vespa.ai/introducing-answerai-colbert-small/

## Related Pages

- [[entities/_index]]
