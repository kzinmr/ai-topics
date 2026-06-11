---
title: "Inference — LLM Inference Engine Comparison"
type: concept
aliases:
  - inference-engines
  - llm-inference
tags:
  - concept
  - inference
  - mlops
  - local-llm
status: active
description: "The three major LLM inference engines: llama.cpp (local CPU/GPU), vLLM (server high-throughput), SGLang (agent-optimized)"
created: 2026-04-09
updated: 2026-04-30
sources:
  - "https://github.com/ggml-org/llama.cpp"
  - "https://github.com/vllm-project/vllm"
  - "https://github.com/sgl-project/sglang"
  - "raw/newsletters/2026-04-30-ainews-the-inference-inflection.md"
related:
  - "[[concepts/inference/llama-cpp]]"
  - "[[concepts/inference/vllm]]"
  - "[[concepts/inference/sglang]]"
  - "[[concepts/local-llm/_index]]"
  - "[[concepts/inference-speed-development]]"
  - "[[concepts/gguf-quantization]]"
  - "[[concepts/serving-llms-vllm]]"
---

# Inference — LLM Inference Engines

Three major engines for optimizing LLM inference and how to choose between them.

## Three Major Engine Comparison

| | **llama.cpp** | **vLLM** | **SGLang** |
|---|---|---|---|
| **Developer** | Georgi Gerganov (→ Hugging Face) | UC Berkeley / vLLM team | LMSYS Org (→ PyTorch) |
| **Primary Target** | Local/Edge | Server/API | Agent/RAG |
| **KV Cache** | Standard | PagedAttention | RadixAttention (prefix sharing) |
| **Format** | GGUF only | HuggingFace | HuggingFace |
| **Hardware** | CPU, Apple Silicon, GPU | NVIDIA/AMD GPU | NVIDIA, AMD, Intel, **CPU support** |
| **Structured Output** | ❌ | ❌ | ✅ xgrammar (native) |
| **Key Strength** | Lightweight, local operation | High throughput, continuous batching | Long shared prefix caching |
| **2026 Trend** | Joined Hugging Face (Feb 2026), Speculative Checkpointing | Large-scale de facto | Joined PyTorch (Mar 2025), RL rollout backend |

## Selection Guide

### When to Choose llama.cpp
- **Local/Edge inference** — run on CPU or Apple Silicon
- **GGUF models** — using quantized models
- **Lightweight deployment** — minimize dependencies
- **Consumer hardware** — Mac, laptop, Raspberry Pi
- Ollama, LM Studio, text-generation-webui backend engine

### When to Choose vLLM
- **Server/API deployment** — high throughput required
- **Multi-LoRA** — serve multiple fine-tuned models simultaneously
- **Continuous batching** — efficient concurrent request handling
- **Production de facto standard** — most proven track record

### When to Choose SGLang
- **Agent workloads** — long system prompts/tool definitions
- **RAG pipelines** — lots of shared context
- **Structured output** — JSON Schema/regex constrained generation
- **RL training** — frontier model rollout backend
- **Prefill-decode separation** — advanced scaling

## Latest Optimization Techniques

### Speculative Checkpointing (llama.cpp, Apr 2026)
- Up to 40% VRAM reduction
- Up to 20% token throughput improvement
- Fundamentally redesigned inference memory state management

### RadixAttention (SGLang)
- Sharing common prefixes across requests as tree-structured KV cache
- 3-5x throughput improvement in agent loops
- Compute system prompts, tool definitions, and few-shot examples once and reuse

### PagedAttention (vLLM)
- Applying virtual memory paging concepts to KV cache management
- Eliminating memory fragmentation, maximizing throughput
- 24x throughput vs. HuggingFace Transformers (claim)

## The Inference Inflection (April 2026)

A major industry shift from training-dominant to inference-dominant AI workloads, signaled by multiple industry leaders at NVIDIA GTC 2026 and beyond. The thesis: as AI moves from model-building to agent-running, inference compute becomes the primary cost driver.

### Industry Leaders Signal the Shift

- **Sam Altman (OpenAI CEO):** "To a significant degree, we have to become an AI inference company now." — acknowledging that inference demand is eclipsing training demand.
- **Noam Brown (OpenAI):** "Inference compute is a strategic resource, currently undervalued." [[entities/noam-brown]]
- **Jensen Huang (NVIDIA CEO):** Computing demand has increased **1 million times** in two years. "AI now has to think... In order to think, it has to inference... it's way past training now."

### The CPU Shortage

Despite the GPU narrative, the AI inference boom is creating a **CPU refresh cycle crisis**:

- **Intel CEO Lip-Bu Tan** reported rising CPU demand for AI workloads — software simulation (RL gyms), production agents, and coding agent tools run heavily on CPUs.
- **Doug (SemiAnalysis):** "Usually what you do is you have this big refresh... but everyone has essentially scrounged all of their budget [for GPUs]... we might actually be seeing a CPU shortage partially 'cause of this refresh cycle."

### FlashQLA — Linear Attention for Inference

**Qwen's FlashQLA** delivers high-performance linear attention kernels:
- **2–3× forward speedups** for long-context workloads
- Specifically optimized for personal/edge devices
- Represents a promising direction for efficient inference on consumer hardware

### vLLM on NVIDIA Blackwell

Running [[concepts/inference/vllm]] on Blackwell GPUs achieves **230 tokens/sec** on DeepSeek V3.2 using NVFP4 quantization and speculative decoding — showcasing the ceiling of current inference optimization.

### Implications

The Inference Inflection reframes the landscape:
- Inference infrastructure (not training clusters) becomes the competitive frontier
- CPU capacity planning for agent workloads becomes critical
- Edge inference (llama.cpp, FlashQLA) gains strategic importance
- [[concepts/local-llm/_index]] and [[concepts/serving-llms-vllm]] become complementary rather than alternatives

## 100K Stars (llama.cpp, Mar 2026)

Georgi Gerganov:
> "Now that 90% of the code worldwide is being written by AI agents, I predict that within 3-6 months, 90% of all AI agents will be running locally with llama.cpp 😄"

## Industry Consolidation Trends

| Date | Event | Impact |
|------|---------|------|
| 2025-03 | SGLang joins PyTorch ecosystem | Official framework support |
| 2026-02 | llama.cpp joins Hugging Face | Model distribution and inference layer integration |
| 2026-04 | Speculative Checkpointing merged | Significant local inference performance improvement |

## Related Concepts

- [[concepts/inference/llama-cpp]] — llama.cpp details
- [[concepts/inference/vllm]] — vLLM details
- [[concepts/inference/sglang]] — SGLang details
- [[concepts/gguf-quantization]] — Quantization format
- [[concepts/local-llm/_index]] — Local LLM ecosystem
- [[concepts/inference-speed-development]] — Inference speed optimization
