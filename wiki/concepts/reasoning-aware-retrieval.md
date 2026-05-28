---
title: Reasoning-Aware Retrieval
created: 2026-05-28
updated: 2026-05-28
type: concept
tags:
  - search
  - ai-agents
  - deep-research
  - embeddings
  - training
  - information-retrieval
  - agentic-search
  - rag
  - benchmark
  - methodology
  - fine-tuning
aliases:
  - reasoning-aware-retrieval
  - agentir
  - dr-synth
  - agent-retrieval-co-design
sources:
  - raw/papers/2026-05-28_2603.04384_agentir-reasoning-aware-retrieval.md
  - https://arxiv.org/abs/2603.04384
  - https://texttron.github.io/AgentIR/
related:
  - concepts/agentic-search
  - concepts/deep-research
  - concepts/embeddings
  - concepts/q2q-reformulation
  - concepts/hyde
  - concepts/bm25
  - concepts/colbert
  - raw/papers/2026-02-25_2602.21456_revisiting-text-ranking-in-deep-research.md
  - raw/articles/2026-05-20_turbopuffer_reinforcement-learning-sid-ai.md
---

# Reasoning-Aware Retrieval

> A retrieval paradigm that jointly embeds an AI agent's **reasoning trace** alongside its search query, exploiting the free contextual signal that deep research agents naturally generate before each search. Introduced by Chen et al. (2026) in the AgentIR paper, this approach achieves **+18% absolute accuracy** over conventional retrievers at half the parameter count.

## The Core Insight

Deep research agents don't just issue queries — they **think before they search**. At each turn, the agent generates a natural language reasoning trace (τ_t) that reveals:

1. **Task intent** — what the agent is really trying to find (disambiguating keyword queries)
2. **Prior-result reflection** — what was already learned from previous searches
3. **Hypothetical search targets** — grounded speculation about where the answer might be found

**Before AgentIR**: The retriever only sees the raw query q_t — R(q_t). The reasoning trace is discarded.
**With AgentIR**: The retriever sees both — R(τ_t, q_t). The reasoning trace is jointly embedded with the query.

This is a **"for free" signal** — the reasoning trace costs nothing extra since the agent already generates it as part of its ReAct-style loop.

```
Standard:  Agent → [reasoning (discarded)] → query → retriever → documents
AgentIR:   Agent → [reasoning + query] → retriever → documents
```

## Relationship to Existing Retrieval Paradigms

### Q2Q Reformulation vs. Joint Embedding

**[Q2Q reformulation](../raw/papers/2026-02-25_2602.21456_revisiting-text-ranking-in-deep-research.md)** (Meng et al., 2026) uses reasoning traces to translate keyword queries into natural language questions **before** retrieval:

```
keyword query "61,880 football attendance"
  → reasoning trace: "highest attendance"
  → Q2Q: "What football match had an attendance of 61,880?"
  → retriever
```

AgentIR's **reasoning-aware retrieval** goes further — instead of translating then retrieving, it **jointly embeds** the reasoning trace alongside the query. The embedding model learns to weight the reasoning signal internally:

```
keyword query "61,880 football attendance" + reasoning trace "highest attendance"
  → [joint embedding] → retriever
```

The Q2Q approach is an explicit two-step pipeline (translate → retrieve). AgentIR collapses this into a single embedding step by training the retriever to understand reasoning traces natively. The result: AgentIR-4B at **4B** parameters outperforms Q2Q + Qwen3-Embed-8B at **8B** parameters.

### vs. HyDE (Hypothetical Document Embeddings)

**HyDE** generates hypothetical answer documents and embeds them as search vectors. The approach is speculative — the model guesses what an answer might look like.

AgentIR's reasoning traces provide a **grounded alternative**: instead of pure speculation, the hypotheses are conditioned on the agent's full interaction history — prior search results, accumulated knowledge, and identified gaps. This makes them more accurate than standalone HyDE.

### vs. SID-1 (RL-Trained Retrieval)

**[[SID-1]]** (SID AI, 2025) uses reinforcement learning to train agentic retrieval end-to-end. AgentIR is complementary — it improves the retrieval **backbone** that even RL-trained agents depend on. A stronger retriever means fewer search calls and better training signal for RL.

| Approach | Training Signal | Retriever Type | Retriever Size |
|----------|---------------|----------------|----------------|
| BM25 | None (lexical) | Sparse | — |
| Q2Q Reformulation | Reasoning trace → NL question | Any retriever | — |
| **AgentIR (Reasoning-Aware)** | Joint embedding of τ_t + q_t | Bi-encoder | **4B** |
| SID-1 | RL (NDCG reward) | Multi-turn agent | 14B |

## DR-Synth: Training Data for Agent Retrievers

The key enabler behind AgentIR is **DR-Synth**, a data synthesis pipeline that converts standard QA datasets into agent sub-query training data. Standard QA datasets provide only global (Q, A, P) triples — the question, answer, and positive documents. AgentIR needs sub-query-level instances: (reasoning trace, query) → (positive document, hard negatives).

DR-Synth bridges this gap in three steps:

### Step 1: Agent Rollouts

Run a deep research agent (Tongyi-DR) on Q with a standard retriever. Record (τ_t, q_t) at each search turn. Only trajectories that **successfully answer Q** are kept (rejection sampling).

### Step 2: Oracle Reranking

For each search turn t:
- Retrieve top-50 documents for q_t using a standard retriever
- Prepend the known positive documents P (useful for Q overall)
- Use an LLM judge (GLM-4.6) to **rerank** the candidate pool
- The LLM sees: q_t (the sub-query), Q (the global question), and A (the answer)
- Top-ranked document → positive (d⁺_t)
- Bottom-7 → hard negatives ({d⁻_t})

### Step 3: Contrastive Training

Train a bi-encoder with contrastive loss:
```
ℒ = −log[ exp(sim([τ_t, q_t], d⁺_t)/T) / Σ exp(sim([τ_t, q_t], d)/T) ]
```
Temperature T = 0.01, in-batch negatives included.

**Scale**: 5,238 training instances from 250 WebShaper questions, ~1.15M document corpus.

## AgentIR-4B: Performance

### BrowseComp-Plus Results

| Retriever | Accuracy (%) | Recall (%) | Search Calls |
|-----------|-------------|------------|--------------|
| BM25 | 33.98 | 46.83 | 32.92 |
| Qwen3-Embed-4B | 48.67 | 59.90 | 31.02 |
| Qwen3-Embed-8B | 50.72 | 61.78 | 30.43 |
| ReasonIR-8B | 51.03 | 63.62 | 31.15 |
| Qwen3-Embed-4B + LLM Rerank | 55.66 | 68.35 | 28.85 |
| **AgentIR-4B** | **66.27** | **78.86** | **25.91** |
| AgentIR-4B + Visit | **68.07** | 76.58 | 24.49 + 3.41 Visit |

### Cross-Agent Generalization

AgentIR-4B was trained on Tongyi-DR trajectories but generalizes to other agents **without retraining**:

| Agent | Accuracy (%) |
|-------|-------------|
| Tongyi-DR | 66.27 |
| oss-120b-high | 66.99 |
| GLM-4.7 | 61.18 |

### Why It Works: Ablation

| Reasoning Signal | What It Provides |
|---|---|
| **Task intent** | Translates ambiguous keyword queries into semantically precise retrieval targets |
| **Prior-result reflection** | Provides retrieval history context — avoids re-searching already-known answers |
| **Hypothetical targets** | Grounded HyDE: speculation conditioned on actual interaction history, not pure guesswork |

## Key Design Implications

### 1. Retrievers Should Be Co-Designed for Agents

Traditional retrievers are trained on human-issued natural language queries (MS MARCO, Natural Questions). Agent queries are fundamentally different — keyword-heavy, 10-term median, with phrase quotes and `site:` operators. **AgentIR demonstrates that training retrievers specifically on agent-issued queries with reasoning context yields dramatic improvements**, even with smaller models.

### 2. Free Signals Are Underutilized

The reasoning trace costs nothing — agents generate it before every search as part of their ReAct loop. Throwing it away is leaving retrieval quality on the table. This principle likely extends to other agent-generated signals: reflection summaries, tool-call histories, and plan hierarchies.

### 3. Joint Embedding > Pipeline Architecture

The two-stage Q2Q approach (reasoning → translate → retrieve) is less effective than jointly embedding reasoning + query in a single trained model. The embedding model learns to **internalize** the translation step, avoiding the information loss that occurs at the pipeline boundary.

### 4. Smaller Models, Better Architecture

AgentIR-4B (4B parameters) outperforms:
- Qwen3-Embed-8B (2× parameter count)
- Qwen3-Embed-4B + LLM Rerank (additional 8B reranker model)
- ReasonIR-8B (purpose-built reasoning retriever, 2× larger)

The architecture matters more than parameter count when the model is trained on the **right signal**.

## Limitations & Open Questions

- **Data synthesis cost**: DR-Synth requires running full agent rollouts for each training question (250 WebShaper questions → 5,238 instances)
- **Benchmark scope**: Only tested on BrowseComp-Plus; generalization to other benchmarks (FRAMES, Bright, etc.) not demonstrated
- **Retriever type**: Only bi-encoder (dense) explored; multi-vector (ColBERT) and learned sparse (SPLADE) variants may benefit differently
- **Reasoning trace quality**: Performance depends on the agent's reasoning quality; poor reasoning traces may provide misleading signal
- **Freshness**: The retriever is trained on static corpora; reasoning traces may encode outdated world knowledge

## Related Concepts

- [[concepts/agentic-search]] — Broader framework for agent-driven retrieval; AgentIR advances Level 1 (IR/Retrieval Layer)
- [[concepts/deep-research]] — Deep research agents generate the reasoning traces that AgentIR exploits
- [[concepts/q2q-reformulation]] — Predecessor technique using reasoning traces for query reformulation
- [[concepts/hyde]] — Hypothetical document embeddings; AgentIR provides a grounded alternative
- [[concepts/bm25]] — Baseline retriever; AgentIR shows how far learned retrievers can go with the right signal
- [[concepts/embeddings]] — Bi-encoder embedding models; AgentIR-4B is a fine-tuned Qwen3-Embedding-4B
