---
title: "Local LLM Ecosystem — Overview"
tags: [local-llm, inference, overview]
created: 2026-04-14
updated: 2026-04-15
---

# Local LLM Ecosystem — Overview

Local LLM inference on personal hardware. This page is the index for the local-llm concept cluster.

## Sub-pages

### Inference Engines
- [[concepts/local-llm]] — llama.cpp inference engine (CPU, Apple Silicon, CUDA)
- [[concepts/local-llm/ollama]] — Ollama local LLM runner (model library, REST API)
- [[concepts/inference/vllm]] — vLLM high-throughput serving (PagedAttention)
- [[concepts/inference/sglang]] — SGLang serving framework (RadixAttention, structured generation)

### Model Formats & Compression
- [[concepts/local-llm/gguf]] — GGUF quantization format (K-Quants, I-Quants)
- [[concepts/local-llm/model-quantization]] — Quantization overview (GPTQ, AWQ, EXL2, FP8)
- [[concepts/local-llm/model-distillation]] — Knowledge distillation for local models

### Tools & Hardware
- [[concepts/local-llm/inference-hardware]] — Consumer GPU, Apple Silicon, edge devices
- [[concepts/local-llm/server-dgx-spark]] — DGX Spark + NemoClaw setup guide
- [[concepts/local-llm/self-hosting-ai-development]] — Self-hosting economics and workflow

## Model Comparisons
- [[comparisons/local-llm-models-april-2026]] — Local LLM Models Comparison (gpt-oss, GLM-4.5, Qwen 3, specialized edge models)

## Summary

The local LLM ecosystem encompasses the tools, formats, and hardware that enable running large language models on personal infrastructure rather than cloud APIs. Key drivers include privacy, cost efficiency, offline capability, and freedom from vendor lock-in.

Two critical techniques enable local inference:
1. **Quantization** — Reduces model size (FP16 → 4-bit) with minimal quality loss
2. **Distillation** — Compresses frontier model knowledge into smaller student models

Together, these techniques allow a distilled 3-8B model at Q4 quantization to run on consumer hardware with performance approaching much larger unquantized models.

## Inference Engine Comparison

| Engine | Best For | Hardware | Structured Output |
|--------|----------|----------|-------------------|
| **llama.cpp** | CPU/Apple Silicon local | CPU, Metal, CUDA, Vulkan | Basic (grammar sampling) |
| **Ollama** | Zero-config local runner | CPU, Metal, CUDA | Via Modelfile |
| **vLLM** | Production serving | NVIDIA, AMD GPU | Outlines integration |
| **SGLang** | Agentic loops, RAG | NVIDIA, AMD, CPU | ✅ Native (xgrammar) |

## Related wikilinks

- [[concepts/local-llm]] — Original consolidated page (reference)
- [[concepts/harness-engineering]] — Local LLMs as harness components
- [[concepts/harness-engineering/agentic-engineering]] — Using local LLMs in agent workflows
- [[concepts/reasoning-models]] — Distillation for CoT transfer
- [[concepts/inference]] — Inference optimization techniques
- [[concepts/inference-speed-development]] — Development cadence at inference speed

## Sources

- r/LocalLLaMA, r/LocalLLM community discussions
- llama.cpp GitHub (ggerganov/llama.cpp)
- Ollama documentation
- vLLM project (vllm-project/vllm)
- SGLang documentation (sgl-project/sglang)
- Hugging Face blog on distillation
- Georgi Gerganov, PR #4856 and The Changelog #532
