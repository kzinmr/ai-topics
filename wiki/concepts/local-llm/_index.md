---
title: "Local LLM Ecosystem — Overview"
tags: [local-llm, inference]
created: 2026-04-14
updated: 2026-04-15
---

# Local LLM Ecosystem — Overview

Local LLM inference on personal hardware. This page is the index for the local-llm concept cluster.

## Sub-pages

### Inference Engines
- [[concepts/local-llm/_index]] — llama.cpp inference engine (CPU, Apple Silicon, CUDA)
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

## Key Figures

- **Georgi Gerganov (@ggerganov)** — Creator of llama.cpp and whisper.cpp, pioneer of GGML/GGUF quantization ecosystem. Joined Hugging Face in 2025.
- **Nous Research (@NousResearch)** — Hermes model family, open-weight post-training. Teknium leads post-training efforts.
- **Ollama Team** — Simplified local LLM deployment, model library with one-command downloads, strong Apple Silicon support.
- **[[vicki-boykis]]** — Data scientist and blogger documenting practical local model workflows. Identified GPT-OSS as the local quality inflection point (Jun 2026).

## Community Hubs

- **r/LocalLLaMA** (~500K+ members) — Model comparisons, hardware benchmarks, uncensored model discussions
- **r/LocalLLM** — Technical discussions, setup guides, troubleshooting
- llama.cpp Discord, Ollama community channels, Hugging Face forums

## Trends (2026)

1. **Consumer GPU Boom** — RTX 50 series, AMD RX 8000, Apple M-series driving local inference
2. **Small Model Renaissance** — 3B-8B models approaching 70B+ quality via better training
3. **Agentic Local AI** — Local LLMs powering autonomous agents for privacy-sensitive workflows
4. **Hybrid Cloud+Local** — Routing simple tasks locally, complex tasks to cloud
5. **Edge Deployment** — Phones, Raspberry Pi, IoT running quantized models
6. **Digital Sovereignty** — Enterprise and government adoption for data control

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
| **[[lm-studio]]** | Desktop GUI + local API | CPU, Metal, CUDA | OpenAI-compatible |

## Related wikilinks

- [[concepts/local-llm/_index]] — Original consolidated page (reference)
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
