---
title: "SGLang (Structured Generation Language)"
type: concept
created: 2026-04-15
updated: 2026-04-15
status: complete
tags:
  - inference
  - sglang
  - lab
  - pytorch
aliases: ["sglang-serving", "radix-attention", "xgrammar"]
sources:
  - url: "https://github.com/sgl-project/sglang"
    author: "LMSYS Org"
    title: "SGLang GitHub Repository"
  - url: "https://docs.sglang.io/"
    author: "SGLang Team"
    title: "SGLang Documentation"
  - url: "https://pytorch.org/blog/sglang-joins-pytorch/"
    author: "PyTorch Blog"
    title: "SGLang Joins PyTorch Ecosystem (2025-03)"
  - url: "https://huggingface.co/docs/inference-endpoints/en/engines/sglang"
    author: "Hugging Face"
    title: "SGLang on HF Inference Endpoints"
---


# SGLang (Structured Generation Language)

**SGLang** is a high-performance serving framework for LLMs and multimodal models, developed by **LMSYS Org** (the team behind LLaVA and Chatbot Arena). Joined the **PyTorch ecosystem** in March 2025.

## Core Differentiators vs. vLLM

| Feature | SGLang | vLLM |
|---------|--------|------|
| **KV Cache Strategy** | RadixAttention (prefix-sharing tree) | PagedAttention (paged memory) |
| **Structured Output** | ✅ Native JSON Schema + regex via xgrammar | ⚠️ Outlines integration (separate) |
| **Best Workload** | Long shared prefixes (agents, RAG, tool-use) | General serving, multi-LoRA hot-swap |
| **Prefill-Decode** | Disaggregation support | Chunked prefill |
| **CPU Inference** | ✅ (`--device cpu`) | ❌ GPU-only |

### RadixAttention

SGLang's signature optimization. Builds a **tree-structured KV cache** across requests sharing common prefixes:

```
Request 1: [system prompt] → [user query A] → response
Request 2: [system prompt] → [user query B] → response  ← hits RadixAttention cache
Request 3: [system prompt] → [tool definitions] → ...    ← further prefix sharing
```

**Impact**: 3–5× higher throughput on workloads with long shared prefixes — agentic loops, RAG pipelines, few-shot evaluation — because the system prompt / tool definitions / few-shot examples are computed **once** and reused.

### xgrammar (Structured Generation)

Built-in constrained decoding via grammar engines:
- **JSON Schema** — guarantee schema-valid output at the decoding layer (no post-hoc parsing, no retry loops)
- **Regex constraints** — fastest path for dates, codes, IDs
- Logit masking at each step ensures the model can only emit tokens that keep output valid

Critical for agentic tool-use where structured outputs (function calls, JSON) are mandatory.

## Key Features

- **Zero-overhead CPU scheduler** — minimizes batch scheduling latency
- **Continuous batching** — dynamic request admission
- **Speculative decoding** — Eagle2 support
- **Tensor/Pipeline/Expert/Data parallelism** — scales from single GPU to large clusters
- **Multi-LoRA batching** — serve multiple fine-tuned adapters simultaneously
- **Quantization** — FP4, FP8, INT4, AWQ, GPTQ
- **OpenAI-compatible API** — drop-in replacement for OpenAI clients
- **Broad model support** — Llama, Qwen, DeepSeek, Kimi, GLM, GPT-oss, Gemma, Mistral, LLaVA, WAN (diffusion)
- **Hardware** — NVIDIA (GB200/B300/H100/A100/Spark/5090), AMD (MI355/MI300), Intel, CPU

## Production Adoption

- Deployed at scale generating **trillions of tokens per day** in production
- Used as the **rollout backend for RL training** of frontier models (proven in post-training pipelines)
- **HuggingFace Inference Endpoints** — officially supported engine alongside TGI and vLLM
- **SkyPilot/SkyServe** — one-click deployment to cloud GPUs
- 25.5K+ GitHub stars (as of 2026-04)

## Quick Start

```bash
pip install "sglang[all]"

# Launch server with Llama 3.1 8B + structured generation
python -m sglang.launch_server \
  --model-path meta-llama/Llama-3.1-8B-Instruct \
  --port 30000 \
  --mem-fraction-static 0.88 \
  --enable-regex-constraint

# Or via Docker
docker run --gpus all -p 30000:30000 lmsysorg/sglang:latest \
  python -m sglang.launch_server --model-path meta-llama/Llama-3.1-8B-Instruct --port 30000
```

## When to Choose SGLang

| Scenario | Recommendation |
|----------|---------------|
| Agentic loops with long system prompts / tool definitions | ✅ **SGLang** (RadixAttention cache hits) |
| RAG pipelines with shared context | ✅ **SGLang** (prefix sharing) |
| Structured JSON output required | ✅ **SGLang** (native xgrammar) |
| RL training rollout backend | ✅ **SGLang** (proven in post-training) |
| Multi-LoRA hot-swap in production | ⚠️ **vLLM** (more mature) |
| Pure local/CPU inference | ✅ **llama.cpp** (better CPU perf) |
| Consumer hardware (Mac, laptop) | ✅ **Ollama** / llama.cpp |

## Related wikilinks

- [[concepts/inference/vllm]] — vLLM high-throughput serving (PagedAttention)
- [[concepts/inference/llama-cpp]] — llama.cpp CPU/Apple Silicon inference
- [[concepts/structured-outputs]] — Structured output patterns
- [[concepts/inference-speed-development]] — Inference speed optimization
- [[concepts/local-llm/_index]] — Local LLM ecosystem overview

## Overview
**SGLang** is a high-performance inference engine for large language models (LLMs) and vision-language models (VLMs), developed by [[entities/lmsys-org]]. It was introduced in January 2024 with the novel **RadixAttention** mechanism for efficient prefix caching across multiple generation calls.

SGLang has become one of the most widely deployed open-source LLM inference engines, alongside vLLM and TensorRT-LLM. It provides Day-0 support for major model releases and has deep hardware partnerships with NVIDIA, AMD, and Intel.


### Prefill-Decode (PD) DisaggregationSeparates the prompt processing (prefill) and token generation (decode) phases across different GPU instances, enabling independent scaling and optimized resource allocation.


### Expert Parallelism (EP)Specialized support for Mixture-of-Experts (MoE) models like DeepSeek-V3/V4, Qwen3, and Nemotron 3. Features include DeepEP backend, mega-MoE fused kernels, Elastic EP for fault tolerance.


### Pipeline Parallelism (PP)Chunked Pipeline Parallelism for ultra-long context inference. Achieves 3.31× prefill throughput for DeepSeek-V3.1 with dynamic chunking, enabling million-token contexts.


### Inference Optimizations- **FlashMLA**: Fused multi-head latent attention kernel for Hopper/Blackwell GPUs
- **FlashInfer TRTLLM-Gen MoE**: MXFP8 × MXFP4 weight support for Blackwell
- **TileLang mHC**: Manifold-constrained hyper-connections kernel with split-K
- **DeepGEMM Mega MoE**: Fused EP dispatch, GEMM, SwiGLU pipeline
- **Flash Compressor**: Fused 5-stage compression in single kernel pass (up to 80% peak bandwidth)
- **Lightning TopK**: Cluster-of-8 radix-select reduction for top-k (15µs latency)


### Memory Management- **HiSparse**: Hierarchical memory for sparse attention — offloads inactive KV to CPU, up to 5× throughput gain
- **HiCache**: Hierarchical KV caching with storage backend integration
- **ShadowRadix**: Native prefix caching for hybrid attention (SWA + compressed) in DeepSeek-V4


### Speculative Decoding- **MTP** (Multiple Token Prediction): DeepSeek-V4 native MTP support
- **SpecForge**: Training framework for speculative decoding
- **SpecBundle**: Configuration toolkit for speculative bundling
- **EAGLE-3**: Speculative decoding integration


### Diffusion Model Support- **SGLang-Diffusion**: Video generation model serving for models like Wan2.2
- Token-level sequence sharding (SP-Sharding)
- Distributed Parallel VAE for high-resolution encoding
- Fused JIT kernels (CuTeDSL) for WanVideo


### Reinforcement Learning- **Miles** integration for RL post-training
- INT4 Quantization-Aware Training (QAT) pipeline
- FP8 end-to-end training support
- GRPO/PPO training with Megatron-LM backend


## Hardware Support
| Platform | Status |
|----------|--------|
| NVIDIA Hopper (H100, H200) | Full support |
| NVIDIA Blackwell (B200, GB200 NVL72) | Full support |
| NVIDIA Blackwell Ultra (GB300 NVL72) | Full support — 25× improvement |
| NVIDIA DGX Spark | Verified |
| AMD Instinct MI300X/MI350X | Full support (ROCm) |
| Intel Xeon 6 (Granite Rapids) | Verified — cost-effective CPU deployment |
| Huawei NPU | Experimental support |


## Key Integration Partners|- **NVIDIA**: Dynamo, NIXL, TensorRT-LLM kernels
|- **AMD**: ROCm for both inference and RL training
|- **Alibaba Cloud**: EPD Disaggregation, Mooncake
|- **Ant Group**: Production MoE serving, Elastic EP
|- **Intel**: Xeon optimization
|- **Meituan**: LongCat-Flash deployment


## Recent Model Support Timeline- **Apr 2026**: DeepSeek-V4 (Pro 1.6T, Flash 284B)
- **Mar 2026**: NVIDIA Nemotron 3 Super (120B/12B active)
- **Feb 2026**: Qwen3 & Qwen3-VL on AMD MI300X
- **Jan 2026**: GLM-4.5
- **Aug 2025**: OpenAI gpt-oss-120b
- **Jul 2025**: Kimi K2 (1T parameters)
- **May 2025**: DeepSeek V3/R1 large-scale deployment


## Links- [GitHub Repository](https://github.com/sgl-project/sglang)
- [Documentation](https://docs.sglang.io)
- [Cookbook](https://cookbook.sglang.io)
- [LMSYS Blog Posts](https://lmsys.org/blog/)

