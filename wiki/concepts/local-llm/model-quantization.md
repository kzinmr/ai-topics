---
title: "Model Quantization for Local LLMs"
aliases: [quantization, llm-quantization, k-quants, i-quants, gptq, awq, exl2, fp8]
created: 2026-04-15
updated: 2026-04-15
status: L2
tags:
  - concept
  - local-llm
  - quantization
  - gguf
  - gptq
  - inference-optimization
related:
- "[[local-llm/gguf]]"
- "[[inference/llama-cpp]]"
- "[[inference/vllm]]"
- "[[georgi-gerganov]]"
  - "[[nvidia-dgx-spark]]"
  - "[[llm-inference]]"
---

# Model Quantization for Local LLMs

**Quantization** is the process of reducing the numerical precision of model weights (and sometimes activations) to decrease memory footprint and increase inference speed, with minimal quality degradation. It is the **single most important technique** enabling local LLM inference on consumer hardware.

> *"For 2-bit quants, one basically wants to use the largest quantized model that would fit in available RAM/VRAM to get the best possible model performance."* — Georgi Gerganov (PR #4856)

## Why Quantization Matters for Local LLMs

| Metric | FP16 (baseline) | 4-bit Quantized | 2-bit Quantized |
|--------|-----------------|-----------------|-----------------|
| **Memory** | 2 bytes/param | 0.5 bytes/param | 0.25 bytes/param |
| **70B Model Size** | ~140 GB | ~35 GB | ~17.5 GB |
| **200B Model Size** | ~400 GB | ~100 GB | ~50 GB |
| **Bandwidth** | 100% | ~25-40% | ~15-25% |
| **Quality Loss** | — | < 2% perplexity | 3-8% perplexity |

Without quantization, most open-weight models would not fit in consumer GPU VRAM (24 GB on RTX 4090) or even the DGX Spark's 128 GB unified memory.

## Quantization Formats Overview

### GGUF (GGML Universal File Format)

**Primary use:** CPU and Apple Silicon inference via llama.cpp

GGUF is the **standard format for local LLM inference**, created by Georgi Gerganov as the successor to the binary GGML format (August 2023). Unlike tensor-focused formats, GGUF embeds rich metadata — tokenizer config, architecture details, hyperparameters — directly in the file, making it self-contained.

**Key quantization types in GGUF:**

| Type | Bits | Quality | Use Case |
|------|------|---------|----------|
| Q2_K | ~2.5 bpw | Noticeable loss | Maximum compression for large models |
| Q3_K_M | ~3.5 bpw | Moderate loss | Balance of size and quality |
| Q4_K_M | ~4.5 bpw | **Sweet spot** | Default recommendation for most models |
| Q5_K_M | ~5.5 bpw | Minimal loss | Quality-critical tasks |
| Q6_K | ~6.5 bpw | Near-FP16 | When memory is not a constraint |
| Q8_0 | ~8.5 bpw | Virtually lossless | Benchmarking, maximum quality |

**K-Quants** use mixed precision — attention layers (more sensitive) get higher precision than feed-forward layers. This achieves better quality than uniform quantization at the same average bit-depth.

**I-Quants** (Importance-matrix-based Quants) go further: they analyze activation statistics during a calibration run to determine which specific weights matter most, then allocate bits accordingly. Developed by Iwan Kawrakow in collaboration with Gerganov, I-Quants enable usable 2-bit quantization with much smaller quality drops.

> *"The main advantage of GGUF is that it's a single-file format with all metadata included. You don't need a separate tokenizer file, config file, or anything else."* — Gerganov, llama.cpp discussions

### GPTQ (Generative Pre-trained Quantization)

**Primary use:** GPU inference (especially NVIDIA)

GPTQ performs **post-training quantization** using a calibration dataset to minimize perplexity loss. Each layer is quantized independently using second-order information (Hessian approximation).

- **Standard:** 4-bit (most common), supports 3-bit and 8-bit
- **Speed:** Very fast on GPU (TensorCore-optimized)
- **Accuracy:** Generally better than GGUF at the same bit-depth for GPU inference
- **Formats:** Most GPTQ models use the ExLlamaV2 loader (faster than the original GPTQ implementation)

### AWQ (Activation-aware Weight Quantization)

**Primary use:** GPU inference, 4-bit deployment

AWQ is based on the insight that **only ~1% of weights are "salient"** — they contribute disproportionately to the output. AWQ protects these salient weights from aggressive quantization while compressing the rest more heavily.

- **Method:** Analyzes activation patterns to identify salient weights
- **Result:** Better quality than GPTQ at 4-bit for many models
- **Speed:** Slightly slower than GPTQ at inference (due to group-wise scaling)
- **Best for:** Models where quality at 4-bit is critical

### EXL2 (ExLlamaV2 Format)

**Primary use:** GPU inference with ExLlamaV2

EXL2 is the quantization format native to the ExLlamaV2 inference engine. It builds on GPTQ but adds:

- **Per-layer bit-depth mixing:** Different layers can use different bit depths (e.g., 4.0 bpw, 5.0 bpw, 6.0 bpw, 8.0 bpw)
- **Optimized for CUDA:** Fully leverages NVIDIA GPU architectures
- **Highest GPU throughput:** Often 2-3× faster than GGUF on the same GPU for generation

EXL2 is the format of choice for users running large models on consumer GPUs who prioritize speed.

### FP8 and MXFP8

**Primary use:** Training and inference on H100/B200 GPUs

FP8 (8-bit floating point) and its variant MXFP8 (Microscaling FP8) are emerging formats supported by NVIDIA's latest datacenter GPUs. While primarily used for training, they're gaining traction for inference:

- **FP8:** 1 sign bit, 4 exponent bits, 3 mantissa bits
- **MXFP8:** Uses shared exponent blocks for better numerical stability
- **Use case:** DGX Spark's Blackwell GPU supports NVFP4 and MXFP4 for inference

## Quantization vs. Hardware Matching

| Hardware | Recommended Format | Why |
|----------|-------------------|-----|
| **CPU (x86/ARM)** | GGUF (Q4_K_M, Q5_K_M) | llama.cpp optimized for GGUF |
| **Apple Silicon** | GGUF (Q4_K_M, Q6_K) | Metal acceleration via llama.cpp |
| **NVIDIA GPU (consumer)** | EXL2 or GPTQ (4-bit) | ExLlamaV2 maximizes throughput |
| **NVIDIA GPU (datacenter)** | FP8 / GPTQ / AWQ | TensorCore-optimized |
| **DGX Spark** | GGUF or NVFP4 | Unified memory favors GGUF; TRT-LLM supports NVFP4 |
| **Edge devices (Pi, Jetson)** | GGUF (Q2_K, Q3_K_M) | Minimal memory footprint |

## The Quantization Quality Rule

A general rule observed by the local LLM community:

> **Bigger quantized model > Smaller unquantized model**

A 70B model at Q4_K_M will typically outperform a 13B model at FP16 on most tasks, despite the quality loss from quantization. This is because model capacity (parameter count) dominates over precision for most natural language tasks.

**Exception:** Tasks requiring precise numerical reasoning, code generation with strict syntax, or mathematical proofs may benefit more from higher precision at smaller scale.

## Quantization Pipeline (How Models Are Quantized)

```
1. Train model at FP16/BF16 (or obtain from Hugging Face)
2. Collect calibration dataset (~128-512 samples)
3. Run quantization algorithm:
   a. GGUF: llama.cpp's `quantize` tool with importance matrix
   b. GPTQ: Sequential layer-by-layer optimization
   c. AWQ: Activation analysis → salient weight protection
4. Evaluate perplexity on held-out test set
5. Upload to Hugging Face for community distribution
```

The **Unsloth** and **llama.cpp** ecosystems have made step 3 nearly automated — most popular models are quantized and uploaded within hours of release.

## Related wikilinks

- [[local-llm]] — GGUF format deep-dive
- [[local-llm]] — llama.cpp inference engine
- [[georgi-gerganov]] — GGUF/K-Quants creator
- [[nvidia-dgx-spark]] — Hardware supporting NVFP4/FP4
- [[llm-inference]] — Inference optimization techniques

## Sources

- [llama.cpp quantization documentation](https://github.com/ggerganov/llama.cpp#quantization)
- [GGUF format specification](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md)
- [AWQ: Activation-aware Weight Quantization](https://arxiv.org/abs/2306.00978)
- [GPTQ: Accurate Post-Training Quantization](https://arxiv.org/abs/2210.17323)
- [ExLlamaV2 documentation](https://github.com/turboderp/exllamav2)
- Georgi Gerganov, PR #4856 and The Changelog #532
- r/LocalLLaMA quantization comparison threads (2025-2026)
