---
title: "P2: Modern IR Evals For RAG"
source: https://hamel.dev/notes/llm/rag/p2-evals.html
author: Hamel Husain (featuring Nandan Thakur)
date: 2025
type: article
---

# P2: Modern IR Evals For RAG

**Presenter:** Nandan Thakur (University of Waterloo)
**Topic:** Why traditional IR metrics are insufficient for RAG and how FreshStack provides a modern alternative.

## 1. The Problem: Traditional IR vs. RAG Goals

Traditional IR was designed for search engines where a user clicks a single link. RAG needs a comprehensive set of evidence for LLM generation.

**The Cranfield Paradigm (1960s):** Topics → Corpus → Relevance Judgments.

**The Mismatch:**
- Traditional: Rank single most relevant page at #1 (MRR, NDCG)
- RAG: Fetch every piece of evidence ("minimal spanning document set")

## 2. Decline of BEIR

BEIR faces: data contamination, leaderboard saturation (400+ models), static/too-clean benchmarks.

## 3. FreshStack

Developed with Databricks. Evaluates retrieval for technical RAG using real-time data.

**Pipeline:** Nuggetization (GPT-4o breaks answers into atomic facts) → Oracle retrieval from GitHub → Support check (judge determines which chunks support which nuggets).

**Key Metrics:**
- **Grounding (Coverage@20):** % of unique nuggets found (completeness)
- **Diversity (alpha-nDCG@10):** Penalizes redundant documents (efficiency)
- **Relevance (Recall@50):** Baseline on-topic check

**Findings:** BM25 sometimes beats proprietary embeddings on technical docs. Performance doesn't always scale with model size. Massive gap to Oracle maximum.
