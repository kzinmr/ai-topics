---
title: TurboQuant
created: 2026-04-26
updated: 2026-04-26
type: concept
tags: [inference, optimization, quantization]
sources: [raw/articles/turboquant-google-research-blog.md, raw/articles/turboquant-arxiv-2504-19874.md, raw/articles/turboquant-lmcache-blog.md]
---
# TurboQuant

Google Research's vector quantization method for extreme LLM KV cache compression with near-optimal theoretical guarantees.

## Definition

TurboQuant is an **online vector quantization** algorithm that quantizes high-dimensional vectors while minimizing distortion in both mean-squared error (MSE) and inner product estimation. It was designed specifically for LLM KV cache compression, a critical bottleneck highlighted by Jensen Huang at GTC 2026.

## How It Works

TurboQuant employs a **two-stage quantization pipeline**:

### Stage 1: PolarQuant (Main Compression)
1. **Random rotation**: Input vectors are multiplied by a random matrix, spreading outliers across all dimensions
2. **Per-element scalar quantization**: Each rotated coordinate is quantized independently — now all elements are roughly the same scale, enabling efficient GPU-aligned bit allocation
3. Uses most of the compression budget for the primary vector representation

### Stage 2: 1-bit QJL (Residual Correction)
- Applies a **Quantized Johnson-Lindenstrauss (QJL)** transform on the residual
- Saves exactly 1 bit of the budget to align quantized vectors with original directions
- Produces a **zero-biased cosine similarity** — critical for attention accuracy
- This ensures the fundamental LLM operation (attention via cosine similarity) remains accurate

## Performance

| Metric | Result |
|--------|--------|
| KV cache quality neutrality | 3.5 bits per channel (zero quality loss) |
| Marginal quality degradation | 2.5 bits per channel |
| Memory reduction | Up to 6x |
| Context capacity increase | 4x more context per GPU |
| Theoretical optimality | Within ~2.7x constant of information-theoretic lower bounds |
| Nearest neighbor recall | Outperforms existing product quantization |
| Indexing time | Near zero |

## Key Insight

The breakthrough insight is that **MSE-optimal quantizers introduce bias in inner product estimation**. By separating the quantization into a MSE stage (PolarQuant) and an inner-product-correction stage (QJL), TurboQuant achieves both low compression distortion AND unbiased attention scores — something prior methods could not do simultaneously.

## Related Concepts

- [[quantization]] — General technique of reducing numerical precision
- [[memory-architecture]] — KV cache as the internal memory bottleneck for LLM inference
- [[recursive-language-models]] — Another approach to managing unbounded context
- [[gapa]] — Reflection-based optimization that complements quantization approaches

## Sources

- Google Research Blog (2026-03): "TurboQuant: Redefining AI efficiency with extreme compression"
- arXiv:2504.19874 (2025-04): "TurboQuant: Online Vector Quantization with Near-optimal Distortion Rate"
- LMCache Blog (2026-04-15): "What is TurboQuant and why it matters for LLM inference"

## Open Questions

- How does TurboQuant perform on non-Gaussian data distributions beyond KV caches?
- Can the random rotation matrix be learned rather than fixed?
- Does TurboQuant generalize to model weight quantization beyond KV cache?
