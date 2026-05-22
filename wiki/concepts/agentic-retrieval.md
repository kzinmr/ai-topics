---
title: "Agentic Retrieval"
type: concept
aliases:
  - agentic-retrieval
created: 2026-04-25
updated: 2026-05-22
tags:
  - concept
  - agentic-retrieval
  - agentic-search
  - information-retrieval
  - search
  - deep-research
  - ai-agents
  - bm25
  - rag
sources:
  - raw/articles/2026-05-20_hornet_this-is-what-agentic-retrieval-looks-like.md
---

# Agentic Retrieval

**Agentic retrieval** is the paradigm where AI agents — not humans — are the primary consumers of search and retrieval infrastructure. It represents a fundamental shift in retrieval workload characteristics: from single-shot, short keyword queries to iterative, multi-call, structured query sessions driven by LLM reasoning loops.

## The Shift from Human to Agent Search

Traditional search infrastructure assumes a **"dumb client, smart server"** model: a human types 1-2 words into a search box, and the server does the heavy lifting of query understanding, expansion, and ranking. Agents invert this: they are **smart clients** that recognize entities, write long structured queries with operators, and execute iterative retrieval loops — but are forced into legacy APIs designed for the dumb-client model.

> "The one-string query interface is a holdover from human search. Systems assume a 'dumb client, smart server' (a human typing two words into a box backed by a server that does the heavy lifting), while agents are smart clients that can recognize entities and write long, well-specified queries."
> — Davis Treybig, via Jo Kristian Bergum, Hornet blog

## Empirical Characteristics

Based on GPT-5 BrowseComp-Plus analysis (830 questions, 19,279 search calls):

### Query Length Distribution

| Metric | Human (AOL log) | GPT-5 Agent |
|--------|----------------|-------------|
| Median | 2 terms | 10 terms |
| p90 | 5 terms | 17 terms |
| p99 | 8 terms | — |
| Max | — | 78 terms |
| First query avg | — | 19.1 terms |

The agent's **median query sits past the human 99th percentile**.

### Query Structure

Agents use advanced search operators at rates far beyond human usage:

| Operator | % of Queries | % of Sessions |
|----------|-------------|---------------|
| Phrase quotes (`"..."`) | 65.56% | 98.19% |
| Four-digit years | 45.60% | 95.42% |
| Multiple years | 17% | 73.61% |
| `site:` filter | 6.43% | 48.07% |

Agent-level operator combinations rarely seen from humans:
- **OR across year ranges**: `"born June" "video game composer" 1971 OR 1970 OR 1969`
- **Wildcard + subdomain**: `site:*.org "January 28, 2019" "Blog" art`
- **filetype: stacked**: `site:surrey.ac.uk filetype:pdf "student numbers" "2018/19"`
- **Negation**: `"Memphis 13" -football -soccer Wikipedia`

### Iterative Sessions

- **Median 24 search calls** per question (p90: 35, max: 63)
- Each call becomes context for the next — **errors compound**
- A missed document on turn 3 affects every subsequent turn

## Why It Matters

### The Retrieval Bottleneck

In BrowseComp-Plus, oracle retrieval (hand-picking evidence documents) achieves 93% accuracy with GPT-4.1. Weak BM25 baseline achieves 14%. That 79-point gap is the retrieval bottleneck — and where agentic retrieval workloads diverge from traditional retrieval assumptions.

### Context Window ≠ Database

A 128k context window holds ~0.017% of the BrowseComp-Plus corpus (100,195 pages, 736M tokens). Even a 1M window holds ~0.14%. **Agents must search** — retrieval determines what slice of the corpus the model reads.

### Distribution Shift

GPT-5's queries are **out of distribution** for neural retrievers trained on MS MARCO and Natural Questions (short, fluent natural-language questions). This causes trained neural retrievers to underperform on agentic workloads.

### Compound Error

Poor retrieval compounds across multi-call sessions. Each turn's search results become context for the next turn's reasoning. A retrieval miss on turn 3 cascades through turns 4–24.

## Systems Built for Agentic Retrieval

- [[concepts/hornet]] — Retrieval engine purpose-built for agent workloads
- [[concepts/vespa]] — The engine where many Hornet engineers previously worked

## Related Concepts

- [[concepts/deep-research]] — The application pattern driving agentic retrieval demand
- [[concepts/rag]] — Retrieval-Augmented Generation (evolving toward agentic retrieval)
- [[concepts/bm25]] — Keyword retrieval backbone; performs differently in agent loops vs. one-shot
- [[concepts/mutually-assured-distraction]] — Compounding error: better retrieval → more convincing distractors → more confident wrong answers
- [[concepts/browsecomp]] — The benchmark revealing the agentic retrieval bottleneck
- [[concepts/agent-loop]] — The iterative reasoning pattern that produces agentic workloads

## Open Questions

- How should retrieval benchmarks evolve to evaluate multi-call agent sessions rather than single queries?
- What retrieval architectures work best when the distribution of queries is agent-driven rather than human-driven?
- Can neural retrievers be adapted to the out-of-distribution agent query style, or do we need new training paradigms?
