---
title: "Half-Quadratic Quantization (HQQ)"
created: 2026-07-25
updated: 2026-07-25
type: concept
tags:
  - concept
  - quantization
  - inference
  - optimization
  - training-free
sources:
  - raw/articles/2026-07-25_mobiusml_hqq-half-quadratic-quantization.md
  - https://dropbox.github.io/hqq_blog/
  - https://github.com/dropbox/hqq
related:
  - "[[concepts/model-quantization]]"
  - "[[concepts/gguf-quantization]]"
  - "[[concepts/cpu-inference-llm]]"
---

## Overview

**Half-Quadratic Quantization (HQQ)** is a calibration-free, weight-only quantization technique for large machine learning models. Developed by Hicham Badri and Appu Shaji at Mobius Labs GmbH (now under Dropbox), HQQ uses half-quadratic optimization with a sparsity-promoting loss to find optimal quantization parameters directly from model weights — no calibration data required.

Published in November 2023, HQQ addresses the two main pain points of calibration-based quantizers like GPTQ and AWQ: calibration data bias and slow quantization time. HQQ quantizes Llama-2-70B in under 5 minutes (>50x faster than GPTQ) while achieving competitive perplexity.

## How It Works

HQQ formulates quantization as a robust optimization problem minimizing weight reconstruction error:

$$\\underset{z,s}{\\text{argmin}}\\,\\phi(W - Q^{-1}_{z,s}(Q_{z,s}(W)))$$

Where $\\phi()$ is a sparsity-promoting loss (typically $l_p$ norm with $p<1$, default $p=0.7$), capturing the heavy-tailed outlier error distribution better than squared error.

The non-convex problem is solved via **Half-Quadratic splitting** — introducing an auxiliary variable $W_e$ and performing alternating optimization:

1. **Sub-problem 1 (Proximal step):** Solved via the generalized soft-thresholding operator: $\\text{shrink}_{l_p}(x, \\beta) = \\text{sign}(x) \\cdot \\text{relu}(|x| - |x|^{p-1}/\\beta)$
2. **Sub-problem 2:** Average over the quantization grouping axis to find the zero-point $z$

Default solver parameters: $p=0.7$, $\\beta=1$, $\\kappa=1.01$, 20 iterations with early stopping.

## Key Features

- **No calibration data needed** — works solely from model weights
- **Extremely fast** — <5 minutes for Llama-2-70B, >50x faster than GPTQ
- **Competitive quality** — Llama-2-70B @ 2-bit outperforms full-precision Llama-2-13B
- **Supports 8, 4, 3, 2, 1 bits** with configurable group sizes
- **Works on any model** — LLMs, Vision Transformers, and more
- **Linear dequantization** — compatible with optimized CUDA/Triton kernels and `torch.compile`
- **PEFT/LoRA compatible** — supports parameter-efficient fine-tuning on quantized models

## Comparison with Other Methods

| Method | Calibration Data | Speed (70B) | Quality | Bits Supported |
|--------|-----------------|-------------|---------|----------------|
| **HQQ** | None required | ~5 min | Competitive with GPTQ/AWQ | 1-8 |
| GPTQ | Required | ~4+ hours | High | 2-8 |
| AWQ | Required | Moderate | High (activation-aware) | 4 |
| bitsandbytes | None required | Fast (online) | Lower than HQQ | 4, 8 |
| GGUF/GGML | None required | Fast | Good (k-quant methods) | 2-8 |

HQQ outperforms bitsandbytes by +3.1% top-1 accuracy on ViT-B-32 at 4-bit. Its 2-bit Llama-2-70B beats full-precision Llama-2-13B.

## Axis Parameter

- **`axis=0`**: Groups weights along the output dimension. Better quality especially at low bits. NOT supported for fast inference kernels.
- **`axis=1`**: Groups along the input dimension. Slightly lower quality but supports optimized fused inference kernels (GemLite, TorchAO). **Recommended for deployment.**

## HQQ+ Extension

**HQQ+** extends HQQ with trainable low-rank adapters to improve quality at extreme low-bit settings (1-2 bits). See `examples/hqq_plus.py` in the repo and the [1-bit blog post](https://dropbox.github.io/1bit_blog/).

## Integration Ecosystem

- **HuggingFace Transformers**: Native `HqqConfig` support via `quantization_config` parameter in `from_pretrained()`
- **vLLM**: Supported via GemLite backend for high-throughput serving (~158 tok/s on Llama3-8B @ 4-bit on RTX 4090)
- **PEFT**: Compatible with LoRA/QLoRA training via HuggingFace PEFT library
- **Backends**: PYTORCH (default), PYTORCH_COMPILE (torch.compile), ATEN (CUDA), GemLite, TorchAO int4
- **FSDP**: Multi-GPU training supported via fsdp_qlora integration

## Resources

- **Blog**: https://dropbox.github.io/hqq_blog/
- **GitHub**: https://github.com/dropbox/hqq (949★, Apache 2.0)
- **PyPI**: `pip install hqq` (v0.2.8.post1)
- **HuggingFace models**: https://huggingface.co/mobiuslabsgmbh
