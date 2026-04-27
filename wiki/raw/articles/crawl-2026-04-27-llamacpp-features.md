# llama.cpp April 2026 Feature Update

Source: GitHub (ggml-org/llama.cpp), server README, speculative decoding documentation
Date: 2026-04-27
Topic: local-llm deepdive

## Overview

llama.cpp (maintained by ggml-org, originally by Georgi Gerganov) continues rapid development in 2026, with build b8946 released on 2026-04-27. The project has evolved from a simple CPU inference engine to a full-featured local LLM serving platform.

## Key New Features (2026)

### 1. Anthropic Messages API Compatibility
- Full support for Anthropic Messages API-compatible chat completions
- Enables drop-in replacement for Anthropic API endpoints using local models
- Supports tool use and function calling

### 2. Reranking Endpoint
- Built-in reranking endpoint (`/rerank`) for retrieval-augmented generation (RAG)
- Enabled via `--rerank` flag (requires `--embedding --pooling rank`)
- Covers the growing need for local reranking in agentic RAG pipelines

### 3. Speculative Decoding — Six Variants
llama.cpp now supports 5+ distinct speculative decoding implementations:

1. **Draft Model (smaller LLM):** Traditional approach with separate draft GGUF model. Parameters: `--model-draft`, `--draft-max`, `--draft-min`, `--draft-p-min`
2. **N-gram Simple:** Pattern matching from token history. Best for code refactoring, repetitive text. No extra model needed.
3. **N-gram Map Key:** Internal hash-map tracking frequently repeated sequences. Best for repetitive tasks, structured output.
4. **N-gram Map Key-4-Values (Experimental):** Tracks up to 4 possible continuations per n-gram key.
5. **N-gram Mod:** Hash pool with LCG (~16MB memory, constant complexity, variable draft lengths, shared across server slots). Best for long-running servers, reasoning models, summarization.
6. **N-gram Cache:** Maintains statistics about short n-grams; can load external data.

Speculative checkpointing (PR #19493, merged 2026-04-19) further improves stability.

### 4. Server Infrastructure
- OpenAI-compatible chat completions, responses, and embeddings routes
- Parallel decoding with multi-user support
- Continuous batching (enabled by default)
- Multimodal support (experimental)
- Prometheus `/metrics` endpoint
- Schema-constrained JSON response format
- Prefilling of assistant messages (Claude-like API)
- Built-in agent tools (`--tools` flag)
- Docker images available: `ghcr.io/ggml-org/llama.cpp:server` and `:server-cuda`

### 5. Hardware Support
- Apple Silicon (Metal) first-class optimization
- NVIDIA CUDA with custom kernels
- AMD ROCm via HIP
- Intel XPU/GPU support
- RISC-V architecture support (RVV, ZVFH, ZFH, ZICBOP, ZIHINTPAUSE)
- Vulkan and SYCL backends
- CPU+GPU hybrid inference (partial acceleration for models exceeding VRAM)

### 6. Quantization
- 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, and 8-bit integer quantization
- GGUF format exclusively
- Research into ternarization (1.5-bit) and extreme compression

## Related
- Speculative decoding variants documented in official docs
- See also: vLLM v0.19.0 zero-bubble scheduling (concurrent development)
