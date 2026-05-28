---
title: LongEmbed
created: 2026-05-28
updated: 2026-05-28
type: concept
tags:
  - embeddings
  - long-context
  - benchmark
  - evaluation
  - position-interpolation
  - context-extension
  - niah
  - rope
sources:
  - raw/papers/2024-04-18_2404.12096_longembed-extending-embedding-models.md
  - https://arxiv.org/abs/2404.12096
status: active
related_pages:
  - concepts/embedding-long-context-degradation
  - concepts/embeddings
  - concepts/mrcr
---

# LongEmbed

**LongEmbed** is both a **benchmark** and a **methodology** for extending existing embedding models to handle long-context retrieval (up to 32K tokens) without full retraining. Proposed by Dawei Zhu, Liang Wang, Nan Yang et al. (arXiv:2404.12096, Apr 2024), it addresses the fact that most embedding models (E5, BGE, GTE) only support 512 tokens — a fraction of what modern LLMs handle.

> "While the context limit of LLMs has been pushed beyond 1 million tokens, embedding models are still confined to a narrow context window not exceeding 8K tokens."

## The LongEmbed Benchmark

### Design

LongEmbed fixes the flaws of prior benchmarks (BEIR: avg <300 words; LoCo: biased distribution) with two principles:

1. **Long documents** — up to 32K tokens
2. **Uniformly dispersed target information** — prevents models from relying on header position or locality shortcuts

### Tasks

| Task | Type | Avg Doc Words | Metric |
|------|------|--------------|--------|
| Passkey | Synthetic | Varying (0.25K–32K) | Acc@1 |
| Needle | Synthetic | Varying (0.25K–32K) | Acc@1 |
| NarrativeQA | Real (Literature/Film) | 50,474 | nDCG@10 |
| QMSum | Real (Meeting transcripts) | 10,058 | nDCG@10 |
| 2WikiMultihopQA | Real (Wikipedia) | 6,132 | nDCG@10 |
| SummScreenFD | Real (Screenwriting) | 5,582 | nDCG@10 |

### Key Finding

**No existing model maintains high performance at 32K without extension.** Even BGE-en-icl (8K context) degrades beyond its training window.

## Context Window Extension Methods

### For Absolute Position Encoding (APE) Models

APE models like E5 and GTE use absolute position IDs added to token embeddings. Extension methods:

1. **Position Interpolation (PI)**: Scale position IDs down → `pos/s`. Interpolate new position embeddings. Extends ~2–4×.
2. **Parallel Context Windows (PCW)**: Chunk, encode separately, average embeddings. Simple but lossy.
3. **Grouped Positions (GP)**: Map `pos → ⌊pos/s⌋`. Less effective than PI.
4. **Recurrent Positions (RP)**: Map `pos → pos mod L₀`. Poor performance.

**Further tuning**: Freeze original position embeddings, train only newly added ones with skipping bias.

### For Rotary Position Encoding (RoPE) Models

RoPE-based models (E5-RoPE, E5-Mistral) use relative position via rotation, making them **inherently better** at context extension:

1. **NTK-Aware Interpolation**: Scale RoPE frequencies non-uniformly: `θ' = (10000λ)^{-2j/d}`. `λ` slightly > scaling factor `s`. Extends to **32K+**.
2. **SelfExtend**: Group large distances → `⌊(m-n)/w⌋`, but keep normal relative positions within neighbor window `w`. **Best performer at 32K**.

## RoPE vs APE: Why RoPE Wins

| Property | APE | RoPE |
|----------|-----|------|
| Position encoding | Absolute IDs → vector addition | Relative via rotation: `(m-n)θ` |
| Extension ceiling | ~2–4× (PI with tuning) | 32K+ (NTK/SelfExtend) |
| Generalization | Limited — new positions unseen | Natural — relative gaps generalize |
| Training cost | Can fine-tune new position vecs | Training-free extension works |

RoPE's `(m-n)θ` formulation means it inherently encodes **relative distance** — it never encounters a "position 8000" that it hasn't seen; it only computes 8000-relative distances, which is within distribution.

## Relationship to Embedding Degradation

LongEmbed provides the **extension mechanism**, while [[concepts/embedding-long-context-degradation|Jina AI's blindness study]] reveals what happens **after extension**:

| | LongEmbed | Jina Blindness Study |
|---|---|---|
| **When** | Apr 2024 | Mar 2025 |
| **Problem** | How to reach 32K | What happens at 8K |
| **Method** | PI, NTK, SelfExtend | Semantic one-hop NIAH |
| **Result** | RoPE extends to 32K | Even 8K-capable models fail at ~4K |

**Synthesis**: Position encoding is a solved problem for embedding models — RoPE + NTK/SelfExtend reliably extends context. But the Jina study shows that **semantic focus** — the ability to distinguish relevant from irrelevant content — degrades independently of position encoding. Two different walls: one architectural (solved), one representational (unsolved).
