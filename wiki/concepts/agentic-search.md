---
title: Agentic Search
created: 2026-04-30
updated: 2026-04-30
type: concept
tags: [search, ai-agents, information-retrieval, deep-research, reranking]
aliases:
  - deep-research-retrieval
  - agent-query-mismatch
sources:
  - raw/articles/2026-04-30_lessons-from-building-ai-agents-financial-services.md
  - raw/papers/2026-02-25_2602.21456_revisiting-text-ranking-in-deep-research.md
  - https://arxiv.org/abs/2602.21456
  - https://github.com/ChuanMeng/text-ranking-in-deep-research
---

# Agentic Search

> Agentic search encompasses the retrieval strategies and text ranking methods used by LLM-powered agents to search the web, find relevant information, and power deep research workflows. It spans both the **IR research perspective** (how to optimize retrieval for agent-issued queries) and the **harness engineering perspective** (how to design skill/tool discovery for agents).

## Definition

**Agentic Search** refers to the retrieval systems and strategies that AI agents use to discover relevant information. It operates at two distinct levels:

### Level 1: IR/Retrieval Layer (Search Engine Interaction)
How agents query web search engines or fixed corpora to find relevant documents. This is the classical IR problem adapted for agent-driven query patterns.

### Level 2: Skill/Tool Discovery (Agent Harness Layer)
How agents discover which capabilities, skills, or tools are relevant to the current task — loading only what's needed into context to avoid token waste.

---

## Level 1: IR Research Perspective

A landmark 2026 study by Meng, Ou, MacAvaney, and Dalton (University of Glasgow) systematically evaluated IR text ranking methods for deep research agents, revealing critical design insights.

### The Query Mismatch Problem

Agent-issued queries differ fundamentally from the natural language queries used to train neural rankers. Deep research agents produce **web-search-style keyword syntax** — using quotes for exact matches, Boolean operators, and fragmented terms — while neural rankers (dense retrieval models like RepLLaMA, Qwen3-Embed) are trained on complete natural language questions.

This mismatch means that **lexical (BM25), learned sparse (SPLADE-v3), and multi-vector (ColBERTv2) retrievers outperform standard dense retrievers** in agentic search contexts.

### Key Findings

| Component | Recommendation | Evidence |
|-----------|---------------|----------|
| **Retrieval Unit** | **Passages** (~250 words) | More search/reasoning iterations before hitting context limits |
| **Base Retriever** | **BM25** (with $b=1.0$) or **SPLADE-v3/ColBERTv2** | SPLADE-v3 + Q2Q achieves 7.95% accuracy gain |
| **Re-ranking** | Implement with depth ≥ 50 | BM25–monoT5-3B reaches 0.716 recall / 0.689 accuracy |
| **Query Processing** | **Q2Q Reformulation** | Translate keywords → natural language questions using agent reasoning trace |
| **Document Access** | "Full-Document Reader" tool | Let agent retrieve full docs on-demand when evidence found in passages |

### Query-to-Question (Q2Q) Reformulation

A key innovation: using the agent's own **reasoning trace** as context to reformulate keyword queries into natural language questions.

```
Raw agent query: "61,880" football attendance
→ Reasoning trace: "The user asked about the highest attendance"
→ Q2Q: "What football match had an attendance of 61,880?"
```

This yields a **7.95% relative accuracy gain** for SPLADE-v3 neural retrieval.

### Re-ranking Architecture

A two-stage pipeline significantly outperforms single-stage retrieval:

```
Agent Keyword Query
        ↓
  BM25 Retrieval (top-50)
        ↓
  monoT5 Re-ranker (depth=50)
        ↓
  Top-10 passages → Agent Context
```

This BM25–monoT5-3B configuration approaches **GPT-5-level agent performance** at a fraction of the inference cost.

### Why Reasoning Re-rankers Underperform

Reasoning-based re-rankers (e.g., Rank1-7B) showed **no clear advantage** over standard re-rankers. They often misinterpret keyword-heavy agent queries as genuine reasoning problems rather than search retrieval requests.

---

## Level 2: Harness Engineering Perspective

In agent harness/skill systems, agentic search enables context-efficient tool discovery.

### SQL-Based Skill Discovery

Rather than loading all skills/tools upfront, the agent queries a structured database of capabilities based on current context:

1. **SQL Discovery**: Queries a structured skills database to find relevant capabilities based on the user's current context
2. **Agentic Grep/SQL Hybrid**: For unstructured content (e.g., SEC filings), performs targeted text search only when needed
3. **Lazy Loading**: Only injects relevant skills into the agent's context, avoiding token waste

### Use Case: SEC Filing Analysis

Fintool's agents need to answer questions about SEC filings (10-K, 10-Q, proxy statements). Instead of loading all 50+ analytical skills into context:

```
User asks: "What's the company's R&D spend trend?"
→ SQL query finds skills related to "financial metrics", "trend analysis"
→ Only those skills are loaded into context
→ Agent executes with focused capability set
```

---

## Experimental Setup (BrowseComp-Plus)

The IR-layer findings are based on:

- **Dataset**: BrowseComp-Plus — 830 fact-seeking, reasoning-intensive queries
- **Corpus**: 100,195 documents; 2,772,255 passages
- **Judgments**: Human-verified "gold" (contains answer) and "evidence" (supports reasoning)
- **Agents**: gpt-oss-20b (131K context), GLM-4.7-Flash 30B (200K context)
- **Retrievers**: BM25, SPLADE-v3, ColBERTv2, RepLLaMA, Qwen3-Embed
- **Re-rankers**: monoT5-3B, RankLLaMA-7B, Rank1-7B

---

## Related Concepts

- [[concepts/markdown-based-skills]] — Skills format used by agentic search (harness layer)
- [[concepts/s3-first-architecture]] — Where skills files are stored
- [[concepts/agent-harness]] — Agentic search is part of the harness layer

## Related Entities

- [[entities/doug-turnbull-core-ideas]] — Practitioner perspective on agentic search
- [[entities/sheshansh-agrawal]] — Academic IR researcher focused on agentic search

## Sources

- [Revisiting Text Ranking in Deep Research](https://arxiv.org/abs/2602.21456) — Meng, Ou, MacAvaney, Dalton (2026). Systematic evaluation of IR methods in deep research contexts.
- [Lessons from Building AI Agents in Financial Services](raw/articles/2026-04-30_lessons-from-building-ai-agents-financial-services.md) — Agentic search as skill discovery in Fintool.
- [Text Ranking in Deep Research (Code)](https://github.com/ChuanMeng/text-ranking-in-deep-research) — Open-source code and data.
