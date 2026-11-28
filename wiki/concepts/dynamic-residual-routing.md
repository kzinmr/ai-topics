---
title: "Dynamic Residual Routing (DCA / AttnRes lineage)"
created: 2026-11-28
updated: 2026-11-28
type: concept
tags:
  - transformer-architecture
  - training-efficiency
  - residual-networks
  - google
  - ai-research
  - model-training
confidence: medium
sources:
  - raw/articles/2026-11-27_google-research_deepcrossattention-residual-connections.md
  - "https://news.ycombinator.com/item?id=50672565"
related:
  - concepts/kimi-k3
  - concepts/deepseek-v4
  - concepts/transformer-architecture
  - concepts/inkling-2-small
---

# Dynamic Residual Routing (DCA / AttnRes lineage)

A November 2026 Google Research blog post ([Supercharging transformer residual
connections](https://research.google/blog/supercharging-transformer-residual-connections/),
Axiotis & Fu, HN 416 pts, Nov 27) put **DeepCrossAttention (DCA)** — an ICML 2025 paper — on the
front page and crystallized a named research lineage: replacing the fixed additive residual
connection with **learned, per-token routing over the history of preceding layers**. The post is
retrospective (the paper is from ICML 2025) but its timing reads as a positioning statement:
Google explicitly situates DCA alongside Kimi K3's AttnRes, DeepSeek's Hyper-Connections, and
Thinking Machines' Inkling 2 as evidence that "dynamic residual routing" is now an active,
competitive area.

## The problem: information dilution in the residual stream

Standard residual connections sum a layer's output with its input — every prior representation is
carried forward with **equal weight**. As depth grows, high-resolution details from early layers get
averaged out or distorted ("the Telephone game"), forcing the network to recompute them and wasting
training budget.

## DCA's two mechanisms

| Mechanism | What it does |
|---|---|
| **Dynamic layer routing** | Per-token mixing weights = static learnable base + input-dependent projection; the network can slide between purely sequential and fully parallel processing per token |
| **Depth-wise cross-attention (split Q/K/V)** | Attention applied **across layers** instead of across tokens — each token queries a dynamically weighted mix of all prior layer embeddings |

Claimed results (Google's own benchmarks, so treat as vendor-reported):
- Same quality **up to 3× faster** training; up to **5× fewer steps** to reach baseline perplexity on LM1B/C4.
- Parameter reductions of **30–40%** at matched quality; PPL <14 on LM1B at 30 layers vs 42 for baseline (29% depth cut).
- Overhead **<0.2% parameters**, but increased memory **bandwidth** (prior layer representations kept intact rather than blended).
- **Retrofit-friendly**: DCA initializes to behave identically to a standard residual net, so continued pre-training on an existing checkpoint (rather than from scratch) dropped LM1B perplexity by 0.19 vs 0.02 for plain continued training.

## The lineage named in the post

The post groups several "dynamic residual" techniques by how they break fixed addition:

- **AttnRes (Kimi K3 / Moonshot)** — learnable softmax attention over prior layers with per-layer
  pseudo-queries; a "Block AttnRes" variant partitions layers into blocks for memory efficiency.
  Moonshot claims ~25% training efficiency at <2% extra cost
  ([[concepts/kimi-k3]]).
- **Hyper-Connections (DeepSeek)** — expands the residual stream into multiple parallel channels
  with learnable mixing matrices; breaks the identity-mapping property, which can destabilize
  training at scale ([[concepts/deepseek-v4]]).
- **Manifold-constrained hyper-connections** — constrain mixing matrices to be doubly stochastic
  (Sinkhorn–Knopp) to restore stable signal propagation.
- **Inkling 2 (Thinking Machines)** — adopted both the AttnRes-style design *and* DCA's cross
  attention (Q/K/V split) mechanism ([[concepts/inkling-2-small]]).

## Interpretation

- The residual stream is being recognized as a **bottleneck/resource** in its own right, distinct
  from width and depth — a third axis for scaling ("memory scaling that goes beyond simply
  increasing model width or depth", per the post).
- Convergence across labs (Google, Moonshot, DeepSeek, Thinking Machines) on variants of the same
  idea is the strongest signal in the post — analogous to how sparse attention techniques
  cross-pollinated in 2025.
- Caveat: headline numbers are first-party (Google Research internal benchmarks on LM1B/C4 and
  image classification); no independent frontier-scale replication is cited. Whether DCA-style
  routing holds at GPT/Gemini-class scale is untested in public.

## Related

- [[concepts/kimi-k3]] — AttnRes at frontier scale
- [[concepts/deepseek-v4]] — Hyper-Connections lineage
- [[concepts/transformer-architecture]] — baseline residual design
- [[concepts/inkling-2-small]] — first public model combining AttnRes + DCA mechanisms
