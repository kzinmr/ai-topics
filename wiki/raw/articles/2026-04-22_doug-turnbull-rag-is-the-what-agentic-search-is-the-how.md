---
title: "Rag is the What. Agentic search is the How." — Doug Turnbull
created: 2026-04-22
author: Doug Turnbull (@softwaredoug)
source: YouTube
url: https://www.youtube.com/watch?v=UXQ916WRK0A
type: talk
duration: 54:49
tags: [agentic-search, rag, information-retrieval, search-engineering, tool-calling, bm25, sid-1, harness-engineering]
---

# Talk Overview

A comprehensive 54-minute talk by search relevance expert **Doug Turnbull** (author of *AI-Powered Search*, *Relevant Search*) arguing that the paradigm has shifted from classical RAG (retrieval-augmented generation) to **agentic search** — where complexity moves from the retrieval layer to the agent+harness layer.

## Core Thesis

> "Don't waste too much time on the original RAG paradigm. AI has moved on."

Originally in RAG, complexity lived in retrieval. With agentic search, it's accruing in the **agent+harness**, leaving us to question whether we even need complex retrievers.

## Key Argument Progression

### 1. RAG Was Just a "Thick Daddy" Search System
Problem after problem, RAG began to resemble exactly what we've built for decades:
- Query understanding / routing on ingress
- Different retrieval strategies for candidates (lexical, embedding, etc.)
- Combine + rerank results
- Aggregate statistics
- Append results to LLM context

> A big "thicc daddy" search system. Like what we've always built. We're unwinding that now to let an agent search using the parts.

### 2. The Unwinding: Agents Replace the Search Stack
Turnbull traces the evolution through four stages:

| Stage | What Changed | Impact |
|-------|-------------|--------|
| **Structured Attributes** | LLMs perform query understanding reliably via schema | Structured query languages for agents |
| **Tool Calling** | Agents know they're searching, not force-fed context | Intentional search behavior |
| **Agent Reasoning** | Agents reflect on results, analyze patterns, search again | Iterative, self-correcting retrieval |
| **Dumb Retrievers** | Agents get by with BM25, grep | Complexity moves to harness |

### 3. Why Dumb Retrievers Work for Agents
When agents can reason about search results:
- They understand exactly how results are produced
- They can iteratively refine queries through multiple rounds
- They can reflect on relevance and retry with different strategies
- They don't need sophisticated embedding-based reranking — the LLM itself handles semantic understanding

> "Do we literally just let an LLM drive a BM25 retriever? Or grep? Why chunk and embed when an LLM knows all about the 'semantics' of your query?"

### 4. Where Complexity Moves: The Scaffold + Tools
Today it's increasingly about the **scaffold and tools** that push agents toward relevance:
- **Agentic skills** — helping agents plan how to use simple search tools
- **SID-1** — models that speed up the search reasoning loop (RL-trained agentic retrieval)
- **Semantic grep** — making "simple retrievers" waste fewer tokens

### 5. The Core Design Principle
> "I wouldn't start RAG today assuming you need the classic RAG embedding+chunking paradigm. I'd focus on tools that deliver needed context. **The dumbest thing that can work, with simplest**"

## Connection to Wiki Concepts

### Agentic Search (Three Levels)
This talk directly validates and synthesizes all three levels of the [[concepts/agentic-search]] framework:

- **Level 1 (IR)**: Turnbull explicitly endorses BM25 + SID-1 as the retrieval backbone, aligning with the academic findings that sparse/lexical retrievers outperform dense for agent queries.
- **Level 2 (Harness)**: The entire talk is about harness architecture — how to design tools and scaffolds that let agents search effectively.
- **Level 3 (Externalized Processing)**: Turnbull's "dumb retriever" argument is the practitioner's version of the Cao et al. thesis: coding agents with grep/scripts outperform complex retrieval pipelines.

### SID-1
Mentions SID-1 explicitly as the model that speeds up search reasoning — an RL-trained approach that makes "simple retrieval" practical at production scale.

### Doug Turnbull's Core Ideas
This talk is a live recording of the ideas documented in [[entities/doug-turnbull-core-ideas]]:
- "Search relevance as engineering" — in agentic search context
- "Agents need simple search" — demonstrated with full argument chain
- "RAG isn't a vector search problem" — expanded into architectural critique
- "Query understanding > ranking" — now done by agents, not search stacks

## Key Quotes
- "Don't waste too much time on the original RAG paradigm."
- "A big thicc daddy search system. We're unwinding that now."
- "Why chunk and embed when an LLM knows all about the 'semantics' of your query?"
- "I wouldn't start RAG today assuming you need the classic RAG embedding+chunking paradigm."
