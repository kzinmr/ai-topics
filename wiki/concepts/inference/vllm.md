---
title: "vLLM"
tags: [local-llm, inference, serving]
created: 2026-04-14
updated: 2026-04-24
type: concept
---

# vLLM

vLLM is a high-throughput LLM serving engine with PagedAttention optimization.

## Key Points

- PagedAttention: virtual memory-inspired KV cache management
- 24x throughput vs. HuggingFace Transformers (claimed)
- Supports continuous batching, chunked prefill, speculative decoding
- Primary deployment target: server-side serving (API endpoints)
- Growing support for local/consumer GPU setups
- Compatible with HuggingFace model format

## vs. llama.cpp

| Aspect | vLLM | llama.cpp |
|--------|------|-----------|
| Target | Server serving | Local inference |
| Hardware | NVIDIA/AMD GPU | CPU, Apple Silicon, GPU |
| Format | HF Transformers | GGUF |
| Throughput | Very high (batched) | Moderate |
| Latency | Low (optimized) | Low |

## Related wikilinks

- [[concepts/local-llm]] — Local LLM overview
- [[concepts/inference/vllm]] — Project entity (if exists)

## Sources

- vllm-project/vllm on GitHub
- PagedAttention research paper
