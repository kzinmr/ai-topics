---
title: "SGLang (Structured Generation Language)"
type: concept
created: 2026-04-15
updated: 2026-04-15
status: skeleton
tags: [inference, serving, structured-generation, sglang, lmsys, pytorch]
aliases: ["sglang-serving", "radix-attention", "xgrammar"]
related: [[concepts/inference/vllm]], [[concepts/inference/llama-cpp]], [[concepts/structured-outputs]], [[concepts/inference-speed-development]]
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
- [[concepts/local-llm]] — Local LLM ecosystem overview
