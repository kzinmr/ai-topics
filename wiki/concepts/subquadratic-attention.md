---
title: Subquadratic Attention
created: 2026-05-16
updated: 2026-05-16
type: concept
tags:
  - transformer-architecture
  - inference
  - optimization
  - context-management
  - training
sources: [raw/articles/whatllm.org--new-ai-models-may-2026-subq-subquadratic--2026-05-16.md]
---

# Subquadratic Attention

**Subquadratic attention** refers to attention mechanisms in language models whose computational complexity scales sub-quadratically with sequence length, i.e., better than O(n²). Standard transformer self-attention is O(n²) — doubling the context length quadruples the cost. Subquadratic approaches aim to break this ceiling.

## Why It Matters

The O(n²) cost of standard attention is the primary bottleneck for long-context models:
- **Cost**: Long-context API calls are priced at significant premiums (e.g., 4-8x per token vs standard context)
- **Quality degradation**: Many "1M context" claims come with quiet caveats about quality loss past certain lengths
- **Latency**: Attention computation dominates inference time at long sequences

## Approaches

| Method | Mechanism | Status |
|--------|-----------|--------|
| **Mamba / SSMs** | State-space models with linear-time recurrence | Research, plateaued at scale |
| **RWKV** | Linear attention via recurrence + time-mixing | Open-source, competitive at mid-scale |
| **Hyena** | Long convolutions + gating | Research, not scaled to frontier |
| **BASED** | Linear attention with sliding window | Research |
| **SubQ (Subquadratic)** | Sparse subquadratic attention end-to-end | First commercial release (May 2026) |
| **FlashAttention** | IO-aware exact attention (still O(n²) but faster constant) | Widely adopted |

## SubQ: First Commercial Subquadratic LLM

In May 2026, [[entities/subquadratic]] launched SubQ 1M-Preview, claiming:
- Native 12M token context window
- ~1/5 the cost of frontier models on long-context tasks
- Up to 52x faster attention at scale
- $29M seed funding

These are vendor claims awaiting independent verification. No third-party benchmarks (MRCR, RULER) have been published.

## Open Questions

- Can subquadratic attention match transformer quality at frontier scale (GPT-5.5, Opus 4.7 class)?
- Will independent benchmarks confirm the 52x speed and 1/5 cost claims?
- Is this a genuine architectural shift or another plateau like Mamba/Hyena?

## See Also

- [[entities/subquadratic]]
- [[concepts/transformer-architecture]]
- [[concepts/long-context]]
- [[concepts/inference]]
- [[concepts/mixture-of-experts]]
