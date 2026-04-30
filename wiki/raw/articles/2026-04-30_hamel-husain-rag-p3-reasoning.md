---
title: "P3: Optimizing Retrieval with Reasoning Models"
source: https://hamel.dev/notes/llm/rag/p3_reasoning.html
author: Hamel Husain (featuring Orion Weller)
date: 2025
type: article
---

# P3: Optimizing Retrieval with Reasoning Models

**Presenter:** Orion Weller (Johns Hopkins University)
**Key Theme:** Moving beyond static keyword matching by embedding instruction-following and reasoning into retrieval.

## 1. The Core Problem

RAG retrieval is stuck in a 1999 keyword-matching paradigm. LLMs are used only to rewrite queries or summarize results — the retrieval step itself is "instruction-blind."

## 2. Promptriever: Instruction-Aware Bi-Encoder

Fast embedding model that follows instructions during initial retrieval.

**Key Innovation: Instruction Negatives** — Document relevant to query but NOT its specific instruction (e.g., "find a document using a metaphor"). Forces model to encode abstract instructions into query embedding.

**Features:** Zero-shot hyperparameter tuning via natural language, low variance across paraphrased prompts.

## 3. Rank1: Reasoning-Based Reranker

Cross-encoder using Test-Time Compute (Chain-of-Thought) to judge relevance.

**Key Features:** Verbalizes reasoning logic before scoring. Trained via SFT on reasoning chains from DeepSeek R1. 7B model outperforms much larger baselines on 10x less data.

**Performance:** BRIGHT benchmark nearly doubled. NevIR (Negation) more than doubled. 10-point gain from including reasoning in training.

## 4. Finding "Invisible" Documents

Rank1 finds relevant documents that human annotators missed in old benchmarks (DL19/DL20). After re-judging, Rank1 became top performer — revealing a "long tail" of previously invisible content.

## 5. Retrieval Paradigms

| Paradigm | Mechanism | Limitation |
|----------|-----------|------------|
| Keyword Search | Exact lexical matching | Fails on synonyms/semantics |
| Semantic Search | Vector/Embedding | Ignores stylistic/logical instructions |
| Instruction Search | Promptriever (Bi-Encoder) | Fast, lacks deep reasoning |
| Reasoning Search | Rank1 (Cross-Encoder) | Powerful, higher latency |
