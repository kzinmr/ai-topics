---
title: "Can Agents Replace the Search Stack?"
author: Doug Turnbull
date: 2026-04-28
source_url: https://softwaredoug.com/blog/2026/04/28/search-apis-replaced-by-agents
domain: softwaredoug.com
type: blog_post
tags:
  - agentic-search
  - bm25
  - embeddings
  - search-architecture
  - llm-agents
  - evaluation
  - ndcg
---

# Can Agents Replace the Search Stack?

Traditional search stacks are complex — query understanding, backend retrieval, reranking — all layered
on top of basic search backends. Could an LLM agent replace all of that? If you give a basic BM25 backend
to an agent, could it take the Search API's job?

## Key Experiment: Amazon ESCI Benchmark

**Dataset:** Amazon ESCI (e-commerce product search)
**Metric:** NDCG

### Baselines
- BM25: 0.289 NDCG
- E5 embeddings: 0.314 NDCG

### Agent Setups (GPT-5-mini, zero-shot, no data-specific tuning)

| Tools Used | NDCG |
|---|---|
| E5 embeddings only | 0.359 |
| BM25 only | 0.385 |
| Both (BM25 + E5) | 0.410 |
| GPT-5 (larger model) with both | **0.453** |

> "I've barely lifted a finger. I just set up a stock LLM with some search tools. Nothing here has been
> fit to my data. A 0.289→0.453 jump in quality depends only on model quality + simple retrievers."

## Agent Behavior: Mostly One Call

For most queries, the agent issues **one search call** per tool, retrieves up to 20 results, and ranks them.

Rare exceptions with BM25 trigger a *second* query (sequential or parallel) when initial results are poor:

- **Sequential reformulation**: "pvc coupler" → networking results (RJ45) → agent recognizes mismatch →
  reformulates to "PVC pipe coupler" → correct plumbing results
- **Parallel queries**: Agent anticipates inconsistent results and issues two queries simultaneously
  (e.g., "AN10 oil catch can no filter" + "AN10 oil catch can without breather filter")

**Key insight**: Keyword search nudges the agent to try more queries because mismatches are observable
(cause-and-effect). Agents can interpret results, understand why they didn't match, and take next steps.

## Encouraging Exploration Improves Results

Two harness constraints added to push agents beyond single-call pattern:

1. **Require at least 4 tool calls** — prompting "wow these are great, but I bet you can do better!"
2. **Disallow duplicate/similar queries** — reject queries >0.9 cosine similarity to previous ones

Results with GPT-5-mini:

| Strategy | NDCG (mean) | NDCG (median) |
|---|---|---|
| Both tools, no nudging | 0.4101 | 0.3743 |
| Require 4 calls, disallow duplicates | 0.4290 | 0.3948 |
| Require 4 calls, reject queries >0.9 sim | 0.4308 | 0.4258 |

Even a smaller model can approach the GPT-5 benchmark with more exploration. Future potential:
retrieval tools rich with affordances — category filters, recency filters, metadata — would give
the agent even more control.

## Agentic Search Models (SID-1)

Frontier LLMs treat search as "web search": one query → trust results → move on.
Dedicated **agentic search models** (e.g., SID-1) are trained to:

- Reason about search relevance realistically
- Understand your company's specific, less-sophisticated retrievers
- Explore thoughtfully, retry, and focus solely on retrieving relevant results
- Act as a **self-hosted subagent**, leaving the main LLM to concentrate on the user's task

**Tradeoffs**: Models would be domain-specific (e-commerce, job search, document retrieval), much like
embedding models. Training data dictates the sweet spot; moving outside that domain yields suboptimal results.

> "One wonders if we'll have agentic search LLMs tailored to different domains. … Or search teams fine
> tuning agentic search models for their domain?"

## "Finding Things" vs "Deep Research"

The experiments above focus on **finding things** (products, jobs, etc.).
When the task becomes *information the agent doesn't already know*, the agent-driven approach **breaks down**.

**MSMarco passages dataset test**:
- Embedding model (trained on MSMarco) baseline → no improvement from an agent driving tools
- The LLM cannot evaluate what it doesn't know; if it knew the correct information, it wouldn't need search

**Two worlds of agentic search**:
1. **Agentic search** — agent helps locate items; it can reason about relevance of existing retrievals
2. **Deep Research** — agent needs *new* information to fill knowledge gaps. The traditional search stack
   (retrieval + relevance ranking) still excels here because the LLM lacks ground-truth knowledge.

> "This latter case is where the traditional search stack still thrives."

## Conclusion

- Simple agents with basic retrieval tools can dramatically beat traditional search baselines out-of-the-box
- The biggest gains come from encouraging exploration (multiple diverse tool calls)
- Agentic search excels at "finding things" but not "deep research" (knowledge gap filling)
- Dedicated agentic search models (SID-1) offer a composable subagent path forward
- The future: agents as the search API, with traditional stacks reserved for deep research use cases

## Related

- [[concepts/agentic-search]] — Full concept page on agentic search
- [[entities/doug-turnbull-core-ideas]] — Doug Turnbull's core ideas
- [[concepts/sid-1]] — SID-1 agentic retrieval model
- [[concepts/bm25]] — BM25 scoring
- [[concepts/vector-search]] — Vector/embedding search
