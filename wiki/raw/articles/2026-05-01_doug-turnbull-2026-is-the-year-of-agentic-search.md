---
title: "Why 2026 is The Year of Agentic Search — Doug Turnbull & Jo Kristian Bergum"
created: 2026-05-01
author: Doug Turnbull (@softwaredoug)
co-host: Jo Kristian Bergum (@jobergum, Vespa.ai)
source: YouTube
url: https://www.youtube.com/watch?v=h370222tnAQ
type: talk
duration: 65:52
tags: [agentic-search, llm-query-understanding, autoresearch, search-harnesses, llm-as-judge, search-engineering, softwaredoug, vespa]
---

# Talk Overview

A 65-minute fireside chat between **Doug Turnbull** (search relevance expert, author of *AI-Powered Search* and *Relevant Search*) and **Jo Kristian Bergum** (Vespa.ai) arguing that the search problems of 2026 are fundamentally **agentic search problems**. The conversation covers four pillars of modern search engineering: LLM-driven query understanding at scale, autoresearch (agents that write their own ranking code), agentic search harnesses (the feedback loops that make dumb retrievers smart), and LLM-as-a-Judge for principled evaluation.

Doug's course "Cheat at Search with Agents" (Maven) starting May 18, 2026 is referenced throughout.

## Core Thesis

> "The search problems of 2026 are agentic search problems."

Classical search architecture — query understanding pipeline → retrieval → reranking — is being unwound and replaced by agent-driven loops. The complexity shifts from the search stack itself to the agent harness and the feedback loops that guide agent behavior.

## Four Pillars

### 1. LLM Query Understanding at Scale

How to classify search queries with LLMs — even into thousands of fine-grained labels — without burning excessive token budgets. Doug's approach uses LLMs to hallucinate plausible labels from the schema, then map the query onto the existing classification taxonomy efficiently.

This extends Doug's earlier work: [[raw/articles/2025-04-08_softwaredoug-llm-query-understand]] and his "semantic search without embeddings" framework ([[raw/articles/2026-01-08_softwaredoug-semantic-search-without-embeddings]]).

**Key insight:** LLMs don't need full content understanding at query time. They need to understand *intent* — color, material, category, price range — as structured attributes, not semantic vectors.

### 2. Autoresearch — Agents That Write Ranking Code

Agents can craft optimized ranking code that's specific to a query or domain. Rather than hand-tuning BM25 parameters or building complex Learning-to-Rank pipelines, an agent can:

- Inspect the retrieval results
- Write a Python/ranking function optimized for NDCG
- Test it against judgment lists
- Iterate

**Key challenge:** Avoiding overfitting to a handful of training queries. The LLM may write ranking code that scores perfectly on the eval set but generalizes poorly. The solution is diversity constraints and careful evaluation design.

This topic connects to Doug's experiment described in [[raw/articles/2026-04-28_softwaredoug-can-agents-replace-search-stack]] on the Amazon ESCI benchmark.

### 3. Agentic Search Harnesses

Agents can turn simple retrieval tools (BM25, grep, even `find` + `grep` on the filesystem) into compelling search experiences — **but only if the harness provides the right feedback loops**.

The harness layer is critical:
- Agents need visibility into *why* results matched
- Simple tools (BM25, grep) give clear cause-and-effect — the agent can reason about why a keyword matched or didn't
- Thick APIs (vector search, complex reranking) obscure this reasoning, making agents trust results blindly
- The harness must enforce exploration: minimum tool calls, diversity constraints, similarity thresholds to avoid query stagnation

This directly echoes the "dumb retrievers" argument from Doug's earlier talk [[raw/articles/2026-04-22_doug-turnbull-rag-is-the-what-agentic-search-is-the-how]] and the [[concepts/agent-harness]] framework.

### 4. LLM as a Judge

A principled approach to getting highly accurate search quality evaluation using LLMs — moving beyond gut-check evaluations to systematic, reproducible quality measurement.

Doug's experience at Daydream (hybrid search with CLIP models) and work on evaluations at Shopify informs a pragmatic take:
- LLM-as-a-Judge is not a shortcut — it requires careful rubric design
- Best used for "grug-brained evals": simple thumbs-up/thumbs-down labels from coworkers rather than ML-powered perfection
- Combined with engagement-based ground truths (click-through, purchase data) for production validation

## Connection to Wiki Concepts

### [[concepts/agentic-search]]
This talk directly illustrates all three levels of the agentic search framework:
- **Level 1 (IR)**: LLM Query Understanding replaces traditional query parsing — agents classify intent, not just expand terms
- **Level 2 (Harness)**: The entire conversation about agentic search harnesses maps to skill/tool discovery + feedback loops
- **Level 3 (Externalized Processing)**: Autoresearch agents that write their own ranking code are a canonical example of externalized processing

### [[entities/doug-turnbull-core-ideas]]
- "Agents need simple search" — demonstrated with the harness feedback loop argument
- "Search relevance as engineering" — LLM-as-a-Judge as a systematic evaluation practice
- "Query understanding > ranking" — LLMs classify intent, agents do the rest

### [[concepts/agent-harness]]
The critique of thick APIs vs. thin search tools is a direct argument about harness design: agents reason better with transparent, cause-effect tools.

### Vespa.ai
Jo Kristian Bergum represents the Vespa.ai perspective — an open-source big data serving engine that handles both vector and lexical search at production scale. Vespa is frequently used as the retrieval backend in agentic search architectures.

## Related

- [[concepts/agentic-search]] — Central concept page
- [[entities/doug-turnbull]] — Main entity page
- [[entities/doug-turnbull-speaking]] — Other conference talks
- [[concepts/agent-harness]] — Agent harness architecture
- [[raw/articles/2026-04-28_softwaredoug-can-agents-replace-search-stack]] — Directly related benchmark article
- [[raw/articles/2026-04-22_doug-turnbull-rag-is-the-what-agentic-search-is-the-how]] — Previous Doug Turnbull talk
