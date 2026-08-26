---
title: "Eric Hartford — SlimServe: NVFP4 inference on 3090"
date: 2026-08-25
date_ingested: 2026-08-25
source: https://x.com/QuixiAI/status/2092359612020469952
author: Eric Hartford (@QuixiAI)
type: x_post
tags: [quantization, inference, nvidia, llm-inference, gpu, open-source]
related:
  - concepts/nvfp4-4bit-floating-point
  - entities/eric-hartford
---

# Eric Hartford — SlimServe: NVFP4 inference on 3090

## Tweet

**Posted:** 2026-08-25T21:13:00Z  
**Author:** Eric Hartford (@QuixiAI), creator of the Dolphin/Samantha open-source model ecosystem  
**URL:** https://x.com/QuixiAI/status/2092359612020469952  
**Context:** Reply to @EdSealing in a thread about low-precision inference.

> I most certainly am not stuck with bf16/fp16
>
> I'm running nvfp4 on 3090
>
> [GitHub - QuixiAI/SlimServe](https://github.com/QuixiAI/SlimServe)

**Engagement (2026-08-25 UTC):** 1 like, 1 reply, 0 retweets, 0 quotes, 3 bookmarks, 46 impressions (low because very fresh at ingest).

## Linked repository: `QuixiAI/SlimServe`

- **URL:** https://github.com/QuixiAI/SlimServe
- **Description:** "By Eric Hartford, QuixiAI — a simplicity-first, opinionated inference engine for the antirez GGUF quants — ds4's interface, vLLM's engine, and every performance trick we can land."
- **Language:** Python
- **License:** Apache-2.0
- **Created:** 2026-07-29
- **Size:** ~226 MB
- **Stars/forks/watchers:** 7 / 4 / 7 at ingest
- **Default branch:** main

### What the repo says (README summary)

**SlimServe** is a specialization of **vLLM** for serving antirez's **GGUF quantized models**, with a focus on AMD MI300X and NVIDIA A100 ROCm/CUDA paths, plus an Apple Metal path. It is opinionated: only a fixed set of tested profiles in `slimserve/profiles.json` are accepted; anything else is refused.

Key features:

- **QuixiCore-rocm:** hand-tuned HIP/MFMA kernels for gfx942 (MI300X) targeting Q2_K/Q4_K routed-MoE layers, MFMA quantized GEMMs, MoE grouped GEMM, and MLA decode.
- **DSpark speculative decoding:** against a GGUF-quantized verifier.
- **TurboQuant compressed KV:** for the draft model, with sliding-window support.
- **1M-token context path:** via AITER sparse-MLA (DSA) attention on ROCm.
- **Cold start:** ~154 s on a 244 GiB GLM-5.2-Vision model (faster than llama.cpp per README).
- **Apple Metal stack:** vendored QuixiCore Metal kernel library; DFlash/DFlash 2 block-diffusion drafters; supports DeepSeek-V4 128 GiB+, Muse-Glimmer 64 GiB+, Qwen3.8 48 GiB+.

### Benchmark claims (from README)

Aggregate throughput for **GLM-5.2-Vision** by concurrent requests:

| Hardware | 1 | 4 | 8 | 16 | 32 | 64 |
|---|---:|---:|---:|---:|---:|---:|
| 2× MI300X | 82 | 141 | 176 | 260 | 297 | 408 |
| 4× MI300X | 104 | 142 | 260 | 270 | 384 | 475 |
| 8× MI300X | 111 | 212 | 333 | 501 | 607 | † |
| 4× A100 | 66 | 138 | 204 | 273 | 326 | 392 |
| 8× A100 | 81 | 167 | 305 | 333 | 550 | 626 |

† 8-GPU A100 at 64 concurrent trips an illegal memory access in vLLM's spec-decode rejection sampler during startup profiling; 8× row measured at `--max-seqs 32`.

The README states the throughput is **not** stock vLLM ROCm — it depends on QuixiCore-rocm. Without those kernels, a 244 GiB routed-MoE GGUF "simply does not serve at these rates on two GPUs."

## Significance of the tweet claim

The tweet claims **NVFP4** quantization running on an **RTX 3090** (Ampere, not Blackwell). This is noteworthy because:

- [[concepts/nvfp4-4bit-floating-point]] documents NVFP4 as NVIDIA's **Blackwell-native** 4-bit floating-point format, with dedicated Tensor Core silicon. Ampere GPUs do not have native NVFP4 Tensor Cores.
- If the claim is accurate, it implies SlimServe is either **emulating** NVFP4 on Ampere, using a different low-precision kernel path that the README labels under the NVFP4 umbrella, or the tweet is using "nvfp4" loosely to refer to a 4-bit quantized representation served through QuixiCore's custom kernels.
- The repo README's quant tags include `mxfp4` (MXFP4), `xxs` (IQ2_XXS/Q2_K), `q4ktail` (Q4K-tail), and `q2k` (Q2_K); the tweet's "nvfp4 on 3090" likely refers to one of these 4-bit paths, but the exact mapping is not spelled out in the public README.
- Either way, it reinforces the trend of **aggressive low-precision inference on consumer/older GPUs** through hand-tuned kernels, which is a major theme in Eric Hartford's recent work (MI300X benchmarks, custom kernels, open inference engines).

## Wiki context

This post adds a concrete data point to [[concepts/nvfp4-4bit-floating-point]]: NVFP4/4-bit floating-point inference is being pushed beyond Blackwell via custom kernel stacks, at least in the open-source local-AI community. The [[entities/eric-hartford]] entity page should be updated to reflect SlimServe and QuixiCore as current projects.

## Related pages

- [[concepts/nvfp4-4bit-floating-point]] — NVFP4 format and quantization landscape
- [[entities/eric-hartford]] — Eric Hartford / QuixiAI
- [[concepts/inference/vllm]] — upstream vLLM framework
