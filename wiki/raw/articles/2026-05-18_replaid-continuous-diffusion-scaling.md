# RePlaid: Continuous Diffusion Scales Competitively with Discrete Diffusion for Language

**Source:** arXiv:2605.18530
**Submitted:** May 18, 2026
**Authors:** Wei Guo et al.

## Abstract

Revisits Plaid, a likelihood-based continuous diffusion language model (DLM), and constructs RePlaid by aligning architecture with modern discrete DLMs. Establishes first scaling law for continuous DLMs that rivals discrete DLMs.

## Key Results

- **SOTA PPL bound**: 22.1 on OpenWebText among continuous DLMs — beats MDLM (23.1), Duo (25.2), Plaid (24.4), LangFlow (32.2)
- **20× compute gap vs autoregressive**: Continuous diffusion scales competitively — not the 100-1000× gap previously believed
- **Outperforms Duo with fewer parameters**
- **Outperforms MDLM in over-trained regime**
- **Generation quality surpasses all prior continuous DLMs**

## Technical Insights

1. **ELBO variance minimization** naturally yields linear cross-entropy over time — no heuristic time reparameterization needed
2. **Likelihood-based embedding optimization** creates structured geometries and drives the most significant likelihood gains (learnable token embeddings are the primary driver)
3. **Self-conditioning** improves results (22.1 with, 23.6 without on OWT)
4. **Continuous nature enables**: PFODE distillation, latent-space inference-time scaling — unavailable to discrete diffusion

## Benchmark Table (OpenWebText PPL)

| Model | Type | PPL |
|-------|------|-----|
| RePlaid (s.c.) | Continuous | **22.1** |
| MDLM (low var.) | Discrete | 23.1 |
| Plaid | Continuous | 24.4 |
| Duo | Discrete | 25.2 |
| LangFlow | Continuous | 32.2 |
| Diffusion-LM | Continuous | 38.4 |

## Significance

This paper challenges the belief that continuous diffusion is inherently less scalable than discrete approaches for language modeling. Combined with NVIDIA's Nemotron-Labs-Diffusion (practical 6.4× speedup), diffusion language models are emerging as a viable alternative to autoregressive architectures.
