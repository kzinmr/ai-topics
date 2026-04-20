---
status: skeleton
created: 2026-04-14
tags: local-llm, inference, engine
---

# llama.cpp

llama.cpp is a C/C++ inference engine for running LLMs efficiently on consumer hardware, created by Georgi Gerganov.

## Key Points

- CPU-first inference with Apple Silicon (Metal) and NVIDIA GPU (CUDA) support
- Supports GGUF format exclusively
- Powers many downstream tools: Ollama, LM Studio, text-generation-webui
- Active development with regular architecture updates (Llama, Mistral, Qwen, etc.)
- Key innovations: flash attention, speculative decoding, batched inference

## Ecosystem Role

llama.cpp is the foundational inference engine for the local LLM ecosystem. Most user-facing tools (Ollama, LM Studio) wrap llama.cpp under the hood.

## Related wikilinks

- [[local-llm/gguf]] — Quantization format used by llama.cpp
- [[georgi-gerganov]] — Creator
- [[local-llm]] — Local LLM overview

## Sources

- github.com/ggerganov/llama.cpp
- r/LocalLLaMA community benchmarks
