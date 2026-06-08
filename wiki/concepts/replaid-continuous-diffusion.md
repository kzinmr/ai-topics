---
title: RePlaid (Continuous Diffusion Scaling)
created: 2026-05-26
updated: 2026-05-26
type: concept
tags:
  - concept
  - diffusion
  - model
  - lab
  - optimization
  - non-transformer
  - open-source
  - training
sources: [raw/articles/2026-05-18_replaid-continuous-diffusion-scaling.md]
---

# RePlaid: Continuous Diffusion Scales Competitively with Discrete Diffusion

arXiv paper (2605.18530, May 18, 2026) by Wei Guo et al. that challenges the belief that continuous diffusion is inherently less scalable than discrete approaches for language modeling.

## Key Finding

The first unified scaling law comparison between continuous and discrete diffusion language models (DLMs) shows continuous models scale on par with discrete counterparts when properly aligned in architecture and experimental setting.

### Benchmark Results (OpenWebText Perplexity)

| Model | Type | PPL |
|-------|------|-----|
| RePlaid (s.c.) | Continuous | **22.1** |
| MDLM (low var.) | Discrete | 23.1 |
| Plaid | Continuous | 24.4 |
| Duo | Discrete | 25.2 |
| LangFlow | Continuous | 32.2 |

RePlaid achieves SOTA among continuous DLMs and rivals discrete DLMs in both likelihood and sample quality.

## Technical Insights

1. **ELBO variance minimization** naturally yields linear cross-entropy over time — eliminating the need for heuristic time reparameterizations that plagued earlier continuous diffusion
2. **Learnable token embeddings** are the primary driver of perplexity gains; likelihood-based optimization creates structured embedding geometries
3. **Self-conditioning** contributes significant improvement (22.1 with vs 23.6 without)
4. **20× compute gap to autoregressive**: Much narrower than the 100-1000× gap previously believed for continuous diffusion

## Future Directions

- PF-ODE distillation for faster sampling
- Latent-space inference-time scaling (unique to continuous diffusion)
- Extension to multi-billion parameter regime

## Relationship to Nemotron-Labs-Diffusion

While [[concepts/nemotron-labs-diffusion]] provides the practical deployment vehicle (6.4× throughput via self-speculation), RePlaid provides the theoretical foundation showing continuous diffusion is fundamentally competitive. Together, they signal that diffusion language models are emerging as a viable alternative to autoregressive architectures.

## Related Pages
- [[concepts/nemotron-labs-diffusion]] — NVIDIA's practical tri-mode diffusion LM (3B-14B)
- [[concepts/speculative-decoding]] — Related acceleration technique
- [[entities/nvidia]] — NVIDIA's research direction in diffusion LMs
