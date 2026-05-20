# Training SID-1 to beat GPT-5 at search with 1k+ QPS RL

**Source:** https://turbopuffer.com/blog/reinforcement-learning-sid-ai
**Authors:** Max Rumpf (Co-founder of SID) and Sam Dauncey (Researcher at SID)
**Published:** May 20, 2026
**Saved:** 2026-05-20

## Overview

SID is a research lab for search. They trained SID-1, an agentic search model, using large-scale reinforcement learning (RL). SID-1 nearly doubles recall over classical retrieval pipelines and outperforms frontier LLMs at orders of magnitude lower latency and cost.

The training became bottlenecked on search latency, so they migrated the search backend to turbopuffer. This post shares how they train SID models using large-scale, synchronous RL rollouts at 1k+ searches per second over 10M+ document corpora across thousands of training steps.

## Performance Highlights

```
model            recall   time per question   cost per 1k questions
────────────────────────────────────────────────────────────────────
SID-1 (4x)       0.84     5.5s                $1.40
GPT-5.1 (high)   0.78     131s                $240
SID-1            0.77     5.5s                $0.62
Gemini 3 Pro     0.66     156s                $120
Sonnet 4.5       0.64     35s                 $540
Reranker @10     0.45     0.78s               $0.61
Vector only @10  0.44     0.15s               $0.0098
```

Source: sid.ai/research/sid-1

SID-1 achieves higher recall than GPT-5.1, Gemini 3 Pro, and Sonnet 4.5, while being ~20x faster and dramatically cheaper.

---

## Iterative Search vs. Static Retrieval

### Static Retrieval Pipelines Fail Uniformly

Static ("RAG") pipelines follow a fixed sequence (rewrite → retrieve → rerank). Every important decision is hard-coded once, at design time, and applied uniformly to all queries. No fixed set of choices is right for every question, causing a long tail of failures.

### SID-1's Iterative Approach

SID-1 treats search as an iterative, multi-turn process driven by an LLM. It decides:
- Which tools to use (ANN, BM25, regex, etc.)
- How to phrase queries
- When to stop and rank results

This iterative process corrects the fundamental problem of static retrieval. Every design decision is now made by a model that adapts its approach to each query.

### SID-1 as a Subagent for Frontier Models

When a frontier model searches directly, every retrieved document and reasoning thought accumulates in its context. Incorrect documents pollute the context and waste tokens. SID-1 acts as a subagent gatekeeper, delivering only the best results, enabling reasoning over millions of documents without context bloat.

A frontier model with a 1M-token limit can see ~10k retrieved chunks (100 tokens each) before saturating. By calling SID-1 as a subagent, the frontier model can feasibly reason over millions of documents.

---

## Training SID-1 with RL (Modified GRPO)

### Setup
- **Algorithm:** Modified GRPO (first introduced by DeepSeek)
- **Per training step:** 256 questions, each with 16 attempts (up to 4,096 attempts per step)
- **Corpora:** Finance, science, legal, email, general knowledge; from 5k curated abstracts to internet-scale
- Each question has a golden list of required documents

### Reward Structure
Each attempt is graded on:
1. Whether it found the correct documents
2. Ranking quality
3. Speed (timeliness rewarded)

At the end of each step, GRPO compares all 16 attempts' rewards and steers the model toward better-than-average behavior.

### Example Training Question (Multi-hop)
```
What's the age gap between the TV producer who created the soap that premiered on the same night a major UK channel launched and the Prime Minister who represented the producer's hometown in Parliament?

Correct documents: Brookside → Phil Redmond (b. 1949) → Huyton constituency → Harold Wilson (b. 1916)
Answer: 33 years
```

---

## Tool Selection and Emergent Behaviors

SID-1 is free to choose whichever search tool it finds most effective, building preferences through reinforcement:

- **ANN (dense vector)**: Preferred over BM25 as training progresses
- **BM25 (full-text search)**: Never fully abandoned — uniquely suited for some tasks
- **HyDE (Hypothetical Document Embeddings)**: SID-1 natively learns to draft plausible answer documents and embed them as search vectors
- **Parallel multi-query BM25**: Issues mix of narrow and broad queries simultaneously
- **Metadata filtering**: Native, index-aware filtering

Learned tool preference opens interesting research avenues: If RL makes a model prefer some tool, it is likely a better tool.

---

## Speed and Parallelism

- In later training stages, the model makes ~20 search tool invocations per attempt
- Each turn demands 800-1400ms to think and generate tool calls
- **Parallelism emerges naturally**: The model learns to issue 4-8 searches per turn rather than one
- This drops latency to ~5s on hard questions and ~1.5s on easy ones
- Result: ~20x faster than frontier LLMs while outperforming them on recall

```
Time spent per question:
Gemini 3 Pro:   156s
GPT-5.1 (high): 131s
Sonnet 4.5:     35s
SID-1:          5.5s
```

---

## Keeping GPUs Hot — Search Backend Challenges

Training with synchronous RL creates extreme search demands:
- Up to 81,920 searches per training step (256 questions × 16 attempts × ~20 searches)
- >1,000 training steps
- 1k+ QPS bursts at the start of each step when all 4,096 attempts fire initial searches
- Some corpora have 10M+ records

A conventional search backend can only scale reads by replicating stateful indexes in memory across nodes. If limited to 20 QPS economically, processing 81,920 searches takes ~68 minutes — but GPUs can run through all attempts ~10x faster. Idling GPUs = lost money.

---

## Scaling the Search Backend on turbopuffer

turbopuffer's architecture is well-adapted to RL training traffic:

### Stateless Readers, High QPS
- Query tier is a stateless layer on top of object storage
- Compute decoupled from storage — read capacity isn't bottlenecked by a single machine
- Any query node with cache headroom can serve any query
- New nodes hydrate cache from object storage on demand (vs. copying shards)

### Diverse Toolbox
- Single query planner routes across BM25, dense vector, sparse vector, regex, glob search
- Combined with native, index-aware filtering

### Huge Corpora
- Public ceiling: 100 billion vectors in a single search index

### Scale to Zero
- Object-storage-first: inactive namespaces pay only cold storage costs
- ~100x cheaper than memory-resident vector databases for cold storage
- Namespace pinning keeps data hot on reserved compute during training runs

### Branching for Corpus Updates
- Native namespace branching (constant-time operation)
- New branch shares parent's underlying storage
- Updates apply only to branch — parent untouched for reproducibility

---

## Summary Table

| RL-for-search need | turbopuffer solution |
|---|---|
| Parallel, bursty reads | Stateless readers, high QPS |
| Diverse toolbox | ANN, BM25, regex, metadata filtering |
| Huge corpora | 100B+ document namespaces |
| Scale down to zero | Object-storage-native, pay-per-usage, pinning |
| Corpus updates | Branching |

---

## Key Links
- SID research: https://sid.ai/research/sid-1
- turbopuffer: https://turbopuffer.com
- Join SID waitlist: https://sid.ai

---

*Raw article saved from turbopuffer.com blog. Content reflects the state as of May 20, 2026.*
