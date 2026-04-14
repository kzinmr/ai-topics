---
entity: "jo-bergum"
aliases: [jobergum, Jo Kristian Bergum]
url: "https://www.linkedin.com/in/jo-bergum/"
blog: "https://hornet.dev/blog"
twitter: "@jobergum"
github: jobergum
role: "CEO & Co-founder of Hornet; former Chief Scientist at Vespa.ai"
updated: 2026-04-10
tags:
  - person
  - information-retrieval
  - search-engine
  - vespa
  - colbert
  - late-interaction
  - agentic-retrieval
  - hornet
---


# Jo Kristian Bergum

**URL:** https://hornet.dev
**Blog:** https://hornet.dev/blog
**Twitter/X:** @jobergum
**LinkedIn:** https://www.linkedin.com/in/jo-bergum/
**Company:** Hornet (CEO & Co-founder)
**Former:** Vespa.ai (Chief Scientist, ~15 years)
**Role:** Retrieval Engineer, Search Infrastructure Pioneer

## Overview

Jo Kristian Bergum is a search and retrieval infrastructure veteran who spent approximately 15 years as Chief Scientist at Vespa.ai (the open-source big data serving engine developed by Yahoo and later spun out), before founding Hornet in 2025 — a new retrieval engine purpose-built for AI agents rather than human users.

Bergum's career has been defined by a deep commitment to practical, production-grade information retrieval systems. At Vespa, he authored dozens of technical blog posts and engineered features spanning vector search, hybrid retrieval, ColBERT integration, and billion-scale document serving. He was one of the earliest and most vocal advocates for ColBERT (Contextualized Late Interaction over BERT) as a production retrieval architecture, publishing extensively on its advantages over single-vector embeddings and building the native Vespa ColBERT embedder.

His founding thesis for Hornet is that **"agents are the new user of search"** — and that legacy retrieval infrastructure (designed for short keyword queries, millisecond response times, and top-ten snippets) fundamentally cannot serve agentic workloads efficiently. Agents issue long, structured queries inside reasoning loops, read entire documents rather than snippets, and trade latency for throughput and recall. Hornet provides schema-first, verifiable APIs designed to work with how frontier AI models reason and execute code.

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

## Key Projects

### Hornet (hornet.dev)
A retrieval engine purpose-built for AI agents. Provides schema-first, verifiable APIs for iterative and parallel retrieval loops. Model-agnostic and open source. Co-founded with Henning Baldershim (CTO) and Erik Dyrkoren (COO).

### Vespa.ai (vespa.ai)
Open-source big data serving engine for search and recommendation. Bergum spent ~15 years as Chief Scientist, contributing to vector search, hybrid retrieval, ColBERT integration, billion-scale serving, and more.

### Vespa ColBERT Embedder
Native ColBERT support in Vespa, enabling explainable semantic search using deep-learned token-level vector representations. One of the first production implementations of ColBERT at scale.

## Related Concepts

- [[ColBERT]] — The late-interaction retrieval model Bergum championed
- [[Late-Interaction]] — His primary research and engineering focus
- [[Vespa]] — The search engine where he spent 15 years
- [[Hornet]] — His new company, a retrieval engine for agents
- [[Agentic-Retrieval]] — The paradigm shift he's building for
- [[Mutually-Assured-Distraction]] — His key insight about retrieval-reasoning compounding errors
- [[Hybrid-Search]] — BM25 + vector search, a Vespa specialty
- [[Explainable-Semantic-Search]] — ColBERT's key advantage over single-vector embeddings

## Sources

- Hornet.dev: https://hornet.dev
- Hornet Blog: https://hornet.dev/blog
- Vespa Blog (author page): https://blog.vespa.ai/authors/jobergum/
- LinkedIn: https://www.linkedin.com/in/jo-bergum/
- Twitter/X: @jobergum
- GitHub: https://github.com/jobergum
- Vespa ColBERT blog: https://blog.vespa.ai/announcing-colbert-embedder-in-vespa/
- Vespa ColBERT-small blog: https://blog.vespa.ai/introducing-answerai-colbert-small/
