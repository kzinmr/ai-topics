---
title: Benchmarking Qwen 3.6 35B MoE (3B active) on an RTX 3090
source: Giles Thomas (gilesthomas.com)
source_url: https://www.gilesthomas.com/2026/07/benchmarking-qwen-3-6-35b-moe-rtx-3090
date: 2026-07-24
author: Giles Thomas
type: blog_post
tags: [qwen, model, local-llm, quantization, llama-cpp, gpu, benchmark, inference]
---

# Benchmarking Qwen 3.6 35B MoE (3B active) on an RTX 3090

## Headline Results

Using Unsloth's UD-IQ4_NL_XL quantization of Qwen3.6-35B-A3B from Hugging Face, with Llama.cpp:

**GPU only (Vulkan)**:
- Generation: ~120 tok/s
- Prompt processing: ~2,800 tok/s
- Context window constrained to ~50,000 tokens (vs native 262,144)

**GPU + CPU offload (Vulkan, 12 layers FFN offloaded)**:
- Generation: ~65 tok/s
- Prompt processing: 600 tok/s
- Full context length available

**CUDA (self-compiled, GPU only)**:
- Generation: 140 tok/s
- Prompt processing: 3,300+ tok/s
- Context window: 89,600 tokens

**CUDA + CPU offload (10 layers)**:
- Generation: 89 tok/s
- Prompt processing: ~1,100 tok/s
- Full context length

**Intel Arc B70 Pro (32 GiB, comparison)**:
- Generation: 75-80 tok/s initially, drops to high 50s as context expands

## Model Architecture Notes

Qwen3.6-35B-A3B is a Mixture of Experts model: 35B total, 3B active per token.

Key architectural insight: The embedding layer and output head each use 508,559,360 parameters (~1B total), meaning over 1B of the 3B active parameters are just for token in/out. Only ~2B active parameters for attention and FFNs — similar imbalance to GPT-2 small.

## Quantization Learnings

Quantization is more like lossy compression than precision reduction. Weights are stored in compressed format and "decompressed" at runtime on the GPU. This explains:
- Why "4.1-bit quants" exist (average bits per weight in compressed format)
- Why different quant types exist at similar bit levels (UD-IQ4_NL, UD-Q4_K_M, UD-IQ4_NL_XL, UD-Q4_K_XL) — different trade-off spaces
- How GPUs without native FP4 support (RTX 3090) can still run 4-bit quants — all computation is in native formats

## Key Insight

MoE doesn't reduce memory usage significantly — all experts must be memory-resident since different tokens in a prompt may need different experts. MoE reduces computation, not memory.
