---
title: "llama.cpp"
tags: [local-llm, inference, engine, open-source]
created: 2026-04-14
updated: 2026-04-27
type: concept
sources:
  - raw/articles/crawl-2026-04-27-llamacpp-features.md
---

# llama.cpp

llama.cpp is a C/C++ inference engine for running LLMs efficiently on consumer hardware, created by Georgi Gerganov and now maintained under ggml-org. As of April 2026, it has evolved from a simple CPU inference engine into a full-featured local LLM serving platform (build b8946, 2026-04-27).

## Key Capabilities

- **CPU-first inference** with Apple Silicon (Metal), NVIDIA GPU (CUDA), AMD GPU (ROCm/HIP), Intel GPU (XPU), and Vulkan/SYCL support
- **Exclusive GGUF format** — supports all quantization levels from IQ2 to Q8
- **CPU+GPU hybrid inference** — partial acceleration for models exceeding VRAM
- **RISC-V support** — RVV, ZVFH, ZFH extensions
- **Continuous batching** — enabled by default for server deployments

## HTTP Server Features

llama.cpp ships a lightweight pure C/C++ HTTP server with full OpenAI-compatible and Anthropic Messages API endpoints:

| Feature | Status |
|---------|--------|
| OpenAI Chat Completions | ✅ |
| OpenAI Embeddings | ✅ |
| Anthropic Messages API | ✅ (chat completions) |
| Reranking endpoint | ✅ (`--rerank` flag) |
| Multimodal | ✅ (experimental) |
| Prometheus metrics | ✅ (`--metrics`) |
| JSON schema constraint | ✅ |
| Grammar constraint | ✅ (BNF grammar) |
| Tool use / function calling | ✅ (~any model) |
| Assistant message prefilling | ✅ (Claude-like) |
| Parallel decoding + multi-user | ✅ |
| Agent tools | ✅ (`--tools` flag) |
| Docker images | ✅ (server, server-cuda) |

## Speculative Decoding — Six Variants

llama.cpp now supports the most comprehensive set of speculative decoding implementations of any inference engine:

| Variant | Approach | Best For |
|---------|----------|----------|
| **Draft Model** | Small GGUF model generates candidates | General speedup, best performance |
| **N-gram Simple** | Token history pattern matching | Code refactoring, repetitive text |
| **N-gram Map Key** | Hash-map tracking frequent sequences | Structured output, repetitive tasks |
| **N-gram Map K4V** | Up to 4 continuations per key (experimental) | Multiple common continuations |
| **N-gram Mod** | Hash pool with LCG (~16MB memory) | Long-running servers, reasoning models |
| **N-gram Cache** | Statistics about short n-grams | External data integration |

Speculative checkpointing (PR #19493, merged 2026-04-19) improved stability and consistency across all variants. Recommended for reasoning models: `--spec-type ngram-mod --spec-ngram-size-n 24 --draft-min 48 --draft-max 64`.

## Ecosystem Role

llama.cpp is the foundational inference engine for the local LLM ecosystem. Most user-facing tools (Ollama, LM Studio, text-generation-webui) wrap llama.cpp under the hood. It powers:

- Personal AI assistants on laptops and desktops
- Edge deployment on Raspberry Pi and mobile devices
- Privacy-sensitive enterprise inference (no cloud dependency)
- RAG pipelines with local reranking

## Related wikilinks

- [[concepts/local-llm/gguf]] — Quantization format used by llama.cpp
- [[concepts/local-llm]] — Local LLM overview and ecosystem
- [[concepts/speculative-decoding]] — Inference acceleration technique
- [[concepts/inference/vllm]] — Production serving alternative
- [[entities/georgi-gerganov]] — Creator of llama.cpp and GGML/GGUF

## Sources

- github.com/ggml-org/llama.cpp — Server README and release notes
- raw/articles/crawl-2026-04-27-llamacpp-features.md
- r/LocalLLaMA community benchmarks and discussions
- Mintlify documentation at mintlify.com/ggml-org/llama.cpp
