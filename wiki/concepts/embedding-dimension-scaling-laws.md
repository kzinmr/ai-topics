---
title: "Embedding Dimension Scaling Laws"
type: concept
created: 2026-06-04
updated: 2026-06-04
tags:
  - concept
  - retrieval
  - scaling-laws
  - embeddings
sources:
  - raw/papers/2602.05062-embedding-dimension-scaling-laws.md
related:
  - scaling-laws
  - dense-retrieval
  - matryoshka-representations
---

# Embedding Dimension Scaling Laws

**Embedding Dimension Scaling Laws** describe the predictable power-law relationship between embedding dimensionality and retrieval performance in dense retrieval systems. Introduced by Killingback et al. (2026), these laws enable practitioners to predict retrieval effectiveness given only the embedding dimension — and jointly with model size — providing a principled framework for balancing effectiveness and efficiency.

## Background: Why Embedding Dimension Matters

[[Dense retrieval]] encodes queries and documents into fixed-dimensional vectors, using inner-product similarity (MIPS) for efficient search. The embedding dimension $d$ directly controls:

- **Storage footprint**: Index size scales linearly with $d$
- **Retrieval latency**: Both exhaustive and ANN search cost depends on $d$
- **Expressiveness capacity**: Theoretical work (Killingback et al., Weller et al.) shows that for corpus size $M > d + 1$, there exist relevance patterns that no linear similarity function can represent

Despite this, practitioners typically use the backbone's "native" hidden size (e.g., 768 for BERT-base) without knowing if it is optimal.

## Dimension-Only Scaling Law

For a fixed model, contrastive entropy $L$ (lower = better) as a function of embedding dimension $D$ follows:

$$L(D) = \frac{A}{D^\alpha} + \delta_D$$

| Parameter | Meaning |
|-----------|---------|
| $A$ | Scaling coefficient (model-specific) |
| $\alpha$ | Power-law exponent (typically 0.5–2.2) |
| $\delta_D$ | Irreducible error (task ambiguity, label noise, model limitation) |

**Key observation**: R² > 0.95 across nearly all model × dataset combinations, confirming a robust power-law fit.

## Joint Scaling Law (Dimension + Model Size)

When both embedding dimension $D$ and model parameters $N$ vary:

$$L(D, N) = \frac{A}{D^\alpha} + \frac{B}{N^\beta} + \delta$$

This unified law reveals:
- **Larger model + smaller embedding often wins** over smaller model + larger embedding
- Both axes show diminishing returns — optimal strategy scales them jointly
- Embedding dimension cannot compensate for insufficient model capacity (and vice versa)

## Practical Design Guidelines

### 1. Optimal FLOPs Allocation
Under a fixed inference FLOPs budget $B$ per query:
- Split budget between encoding ($C_{enc} \approx 2NT$) and scoring ($C_{score} \approx 2MD$)
- Optimal configuration scales both $N$ and $D$ proportionally
- Larger corpora → smaller optimal embedding (scoring dominates cost)

### 2. ANN Changes the Calculus
With approximate nearest neighbor search ($C_{score} \approx 2D \log M$):
- Optimal embedding dimension shifts **much higher** than with exhaustive search
- Larger embeddings + efficient ANN can outperform native hidden size + brute force
- The inflection point (where adding dims hurts) is pushed far out

### 3. Matryoshka Representations
For [[matryoshka-representations]] (post-hoc embedding truncation):
- Scaling laws predict performance at any truncation level
- Enables dynamic dimension selection at query time based on latency budget

## Aligned vs. Out-of-Domain Behavior

| Setting | Scaling Predictability | Notes |
|---------|----------------------|-------|
| Aligned tasks (MSMARCO, TREC DL) | High (R² > 0.95) | Consistent power-law, diminishing returns |
| Out-of-domain (Legal QA) | Moderate | Generally improves, but erratic |
| Out-of-domain (Paper Retrieval) | Low for BERT | Performance can **degrade** at high dims, possibly due to KD overfitting |

**Hypothesis**: Knowledge distillation aligns embeddings with the teacher rather than general representations, causing degradation on novel tasks at high dimensions. Ettin models (no KD) do not show this uptick.

## Relation to Other Scaling Laws

This work extends the [[scaling-laws]] paradigm from LLM pretraining (Kaplan, Chinchilla, [[concepts/delphi-scaling-laws|InfoLaw]]) to the **retrieval-specific axis** of embedding dimensionality:

| Law | What It Scales | Domain |
|-----|---------------|--------|
| Kaplan (2020) | Parameters, data, compute | Language modeling |
| Chinchilla (2022) | Parameters vs. tokens | LLM pretraining |
| InfoLaw (2026) | Data quality, mixture, repetition | LLM pretraining |
| **Embedding Dim (2026)** | **Embedding dimension, model size** | **Dense retrieval** |

## Key Results Summary

- Power-law exponent $\alpha$ ranges from **0.45 to 2.23** depending on model and task
- Sharp gains from dim 32→256; diminishing returns beyond 1024
- For BERT-L8-H512 (41M params): dim 256 already captures most performance on MSMARCO
- BERT-L4 at dim 8K still worse than BERT-L8 at dim 256 — **model capacity trumps embedding size**
- With ANN scoring at $M=10^7$: optimal dim can be 4–8× larger than with exhaustive search

## Sources

- [Scaling Laws for Embedding Dimension in Information Retrieval](https://arxiv.org/abs/2602.05062) — Killingback, Rafiee, Manas, Zamani (UMass CIIR), arXiv 2026
- [Raw paper](raw/papers/2602.05062-embedding-dimension-scaling-laws.md)
- [Killingback et al. — Theoretical limitations of single-vector dense retrieval](https://arxiv.org/abs/2411.03954)
- [Weller et al. — Top-k realizability bounds](https://arxiv.org/abs/2411.08028)
- [Fang et al. — Dense retrieval scaling laws (prior work)](https://arxiv.org/abs/2402.14937)
