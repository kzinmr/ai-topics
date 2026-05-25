---
title: "OPUS (Optimizer-induced Projected Utility Selection)"
type: concept
aliases:
  - OPUS
  - optimizer-induced utility selection
  - dynamic data selection
created: 2026-05-25
updated: 2026-05-25
tags:
  - training
  - optimization
  - datasets
  - training-efficiency
  - scaling
related:
  - concepts/fineweb
  - concepts/scaling-hypothesis
  - concepts/synthetic-data
  - concepts/llm-training-coherence-evolution
sources:
  - raw/papers/2026-02-05_2602.05400_opus-data-selection.md
---

# OPUS (Optimizer-induced Projected Utility Selection)

> **Discriminative summary:** OPUS is a **dynamic, per-step data selection framework** for LLM pre-training that scores training samples based on their contribution to the model's **optimizer-induced effective update** — not raw gradients. Unlike static filters (FineWeb-Edu, DCLM) or optimizer-agnostic dynamic methods (GREATS, MATES), OPUS aligns data selection with the actual update trajectory of modern optimizers (AdamW, Muon), achieving 6x data efficiency with only 4.7% overhead.

## Motivation: The Data Wall Problem

High-quality public text is projected to be exhausted by 2026–2028 (Villalobos et al., 2022). This "Data Wall" forces a paradigm shift in pre-training:

| Era | Strategy | Limitation |
|-----|----------|------------|
| **Past** | More tokens (`scale data volume`) | Hitting the Data Wall |
| **Present** | Better tokens (`static quality filters`) | Ignores training dynamics |
| **Future (OPUS)** | Optimal tokens per step (`dynamic, optimizer-aware selection`) | Small overhead (4.7%) |

## Core Innovation

### Optimizer-Induced Utility

The key insight: a training batch is valuable only insofar as it **moves parameters in a direction that improves model performance under the optimizer's specific geometry**.

Traditional dynamic methods (GREATS, MATES) score data in **raw gradient space**, implicitly assuming SGD. But modern LLM training uses **AdamW** or **Muon** — these optimizers apply **preconditioning** ($P_t$) that transforms the gradient before updating parameters. Scoring in raw gradient space creates a **mismatch** between what you select and how the model actually updates.

OPUS defines utility in the **optimizer-induced update space**:

$$U_z^{(t)} \approx \eta_t \langle \underbrace{P_t \nabla_\theta \mathcal{L}(z; \theta_t)}_{\text{effective update}}, \underbrace{\nabla_\theta \mathcal{L}(D_{val}; \theta_t)}_{\text{target direction}} \rangle$$

where $P_t$ is the optimizer's preconditioner (e.g., AdamW's diagonal scaling or Muon's Newton-Schulz iteration).

### Comparison with Existing Approaches

| Method | Type | Criteria | Optimizer-Aware | Overhead |
|--------|------|----------|-----------------|----------|
| **Random sampling** | Baseline | Uniform | N/A | 0% |
| **FineWeb-Edu** | Static | Quality classifier (training-agnostic) | No | ~0% (pre-computed) |
| **DCLM** | Static | Perplexity-based filtering | No | ~0% (pre-computed) |
| **GREATS** | Dynamic | Raw gradient alignment | No (assumes SGD) | High (full gradients) |
| **MATES** | Dynamic | Raw gradient alignment | No (assumes SGD) | Medium |
| **OPUS** | Dynamic | Optimizer-preconditioned update alignment | **Yes** (AdamW, Muon) | **4.7%** |

## Key Components

### 1. Bench-Proxy Construction

Instead of using the costly validation set directly as the target direction, OPUS builds a **stable in-distribution proxy pool**:

1. Embed benchmark validation set + pre-training corpus using **Arctic-Embed-L v2** (frozen sentence encoder)
2. Compute cosine similarity; max-similarity aggregation per document
3. Accumulate highest-scoring documents up to token budget (e.g., 30M tokens)
4. During training, randomly sample proxy batch from this pool

This avoids using the downstream benchmark directly (distribution shift + gradient noise) while providing a more targeted signal than a random hold-out set.

### 2. Scalable Estimation: Ghost + CountSketch

Computing full per-sample gradients for utility scoring would be **prohibitively expensive**. OPUS uses two techniques:

- **Ghost technique:** Represents gradients as rank-1 outer products ($g = a \otimes b$), avoiding materialization of full gradient tensors
- **CountSketch:** Projects the ghost features into a low-dimensional space ($\mathbb{R}^m$) via random projections, enabling efficient inner product computation

Combined overhead: **~4.7%**, making it practical for large-scale pre-training.

### 3. Boltzmann Sampling with Redundancy Penalty

After scoring, OPUS selects a subset $K = \lfloor \rho N \rfloor$ from the candidate pool using:

- **Boltzmann (softmax) sampling:** Temperature-controlled probability distribution over candidates. Prevents diversity collapse and is robust to noisy proxy estimates.
- **In-step redundancy penalty:** A term $-\eta_t^2 \langle \mathbf{u}_z, \mathbf{G} \rangle$ penalizes selecting samples whose effective updates align with already-selected samples, discouraging redundant batches.

## Empirical Results

### GPT-2 Pre-training (FineWeb, 30B tokens)

| Setting | OPUS Performance |
|---------|-----------------|
| GPT-2 Large, FineWeb, AdamW | Outperforms Random (60B), FineWeb-Edu (30B), DCLM (30B) |
| GPT-2 XL, FineWeb, Muon | Avg accuracy **41.75** vs Random 40.29 |
| GPT-2 Large, FineWeb-Edu, AdamW | Matches or exceeds full **200B-token** Random training with only 30B tokens |

### Continued Pre-training (Qwen3-8B-Base → SciencePedia)

- OPUS with **0.5B tokens** achieves superior performance vs full training with **3B tokens**
- **6x data efficiency** in specialized domain adaptation

### Generalization to OOD Benchmarks

OPUS achieves best performance on **out-of-distribution benchmarks** not aligned with its proxy construction (avg 40.07% vs next best 39.42%), suggesting the method selects data for general model improvement rather than benchmark overfitting.

## Practical Implications

1. **Data Wall mitigation:** Extends effective data utility by 2-6x, buying time as high-quality text becomes scarce
2. **Optimizer-aware training pipelines:** Data selection should be coupled with the optimizer choice — not treated as an independent preprocessing step
3. **Low overhead:** 4.7% makes OPUS viable for production pre-training runs, not just research experiments
4. **Composability:** Works on top of static filters (FineWeb-Edu + OPUS > either alone), enabling incremental adoption in existing pipelines

## Related Pages

- [[concepts/fineweb]] — Industrial-scale static data filtering used as baseline and compositional partner
- [[concepts/scaling-hypothesis]] — Broader context of scaling laws and data efficiency
- [[concepts/synthetic-data]] — Complementary approach (generating new data vs selecting existing data)
- [[concepts/llm-training-coherence-evolution]] — Training dynamics that OPUS leverages for per-step selection
