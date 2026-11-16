---
title: "Positional Embeddings in Modern LLMs"
type: concept
created: 2026-11-16
updated: 2026-11-16
tags: [transformer, rope, architecture, model, education, research]
sources:
  - raw/articles/2026-11-15_raschka_understanding-positional-embeddings.md
  - https://magazine.sebastianraschka.com/p/understanding-positional-embeddings
confidence: high
related:
  - "[[concepts/transformer-architecture]]"
  - "[[entities/jianlin-su]]"
  - "[[concepts/inkling]]"
  - "[[concepts/subquadratic-attention]]"
---

# Positional Embeddings in Modern LLMs

How LLMs represent token position — the methods, their economics, and which 2026 architectures use what. The definitive 2026 survey is Sebastian Raschka's "Understanding Positional Embeddings in Modern LLMs" (Nov 15, 2026, HN 228 pts), which doubles as an empirical gallery survey of positional choices across 2025–2026 open-weight releases.

## Why position information is needed

Self-attention over a token sequence is permutation-invariant: "the red fox jumps over the gray fox" and "the gray fox jumps over the red fox" produce identical embeddings and attention scores without position signals. A causal (autoregressive) mask injects *implicit* order — each token only sees itself and earlier tokens — which is enough in principle to distinguish the two sentences (this is the theoretical basis of **NoPE**, no-positional-encoding models). But the mask cannot distinguish a separation of one position from a separation of ten, so explicit positional signals remain useful or essential.

## The method families

| Method | Where position enters | Used by | Key constraint |
|---|---|---|---|
| Learned absolute embeddings | Add a learned position vector to token embeddings before the first block | GPT, GPT-2 | Table sized at training time; at 100k context the position table would exceed 22% of total weights (vs 0.30% at GPT-2 Medium's 1,024) — economically prohibitive |
| Fixed sinusoidal | Add sine/cosine-derived vectors before the blocks | Original Transformer (2017) | No learned parameters; same sinusoid family later underlies RoPE |
| **RoPE** (rotary) | Rotate query/key vectors inside every attention layer → scores depend on relative distance | Llama, [[entities/qwen\|Qwen]], DeepSeek, Mistral, [[entities/jianlin-su\|invented by Jianlin Su]] | Still the 2026 default, but its share is slipping (see survey) |
| Partial RoPE | Rotate only a subset of Q/K features | Majority of RoPE models in 2026 gallery | Shrinks cos/sin tables but **not** the KV cache (full key still stored) — memory win small; quality rationale unclear |
| Learned relative bias | Add a learned, query-conditioned relative bias to attention scores before softmax | [[concepts/inkling\|Inkling]] (Thinking Machines, 2026), reviving T5 | Notable 2026 new entrant |
| NoPE | Omit explicit positional encoding in some or all layers | Growing; "NoPE-only" entries in the gallery are all recurrent hybrids with softmax attention | Relies on causal-mask implicit ordering |

## 2026 empirical trends (Raschka LLM Architecture Gallery)

Grouping gallery entries by release date (2025 vs early-2026 vs late-2026 snapshots):

- **RoPE in every softmax attention layer remains the most common choice**, but its share fell from 2025 to 2026 and again in late 2026 — a possible trend.
- **Mixing RoPE and NoPE across layers is growing** (groups still small).
- Among RoPE users, **partial RoPE flipped from minority (2025) to majority (both 2026 groups)**.
- "Other" positional designs: xLSTM 7B (no softmax attention) and Inkling's learned query-conditioned relative bias.
- Raschka's forecast: RoPE predominance carries into 2027, with possibly more Inkling-like learned-bias designs.

## Why this matters

Positional encoding is the load-bearing wall of long-context support: the absolute-embedding economics explain why learned absolute tables died, and RoPE's relative-rotation design is what made length extrapolation tricks (position-interpolation family) possible at all. The 2026 shift toward partial RoPE and NoPE hybrids tracks the broader [[concepts/subquadratic-attention|subquadratic attention]] and hybrid-recurrent wave, where dropping per-layer position tables saves memory in models already minimizing attention cost.

## Related

- [[concepts/transformer-architecture]] — the architecture positional embeddings plug into
- [[entities/jianlin-su]] — inventor of RoPE
- [[concepts/inkling]] — learned query-conditioned relative attention bias (T5 revival)
- [[concepts/subquadratic-attention]] — the attention-efficiency wave interacting with positional choices
- [[entities/sebastian-raschka]] — author of the survey and the from-scratch LLM fundamentals series

## Sources

- [[raw/articles/2026-11-15_raschka_understanding-positional-embeddings]] — Raschka survey, Nov 15 2026
