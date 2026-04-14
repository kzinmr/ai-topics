---
status: active
created: 2026-04-14
updated: 2026-04-15
tags: local-llm, inference, overview
---

# Local LLM Ecosystem — Overview

Local LLM inference on personal hardware. This page is the index for the local-llm concept cluster.

## Sub-pages

### Inference Engines
- [[concepts/local-llm/llama-cpp]] — llama.cpp inference engine (CPU, Apple Silicon, CUDA)
- [[concepts/local-llm/vllm]] — vLLM high-throughput serving (PagedAttention)

### Model Formats & Compression
- [[concepts/local-llm/gguf]] — GGUF quantization format (K-Quants, I-Quants)
- [[concepts/local-llm/model-quantization]] — Quantization overview (GPTQ, AWQ, EXL2, FP8)
- [[concepts/local-llm/model-distillation]] — Knowledge distillation for local models

### Tools & Runners
- [[concepts/local-llm/ollama]] — Ollama local LLM runner
- [[concepts/local-llm/inference-hardware]] — Consumer GPU, Apple Silicon, edge devices
- [[concepts/local-llm/server-dgx-spark]] — DGX Spark + NemoClaw setup guide

## Summary

The local LLM ecosystem encompasses the tools, formats, and hardware that enable running large language models on personal infrastructure rather than cloud APIs. Key drivers include privacy, cost efficiency, offline capability, and freedom from vendor lock-in.

Two critical techniques enable local inference:
1. **Quantization** — Reduces model size (FP16 → 4-bit) with minimal quality loss
2. **Distillation** — Compresses frontier model knowledge into smaller student models

Together, these techniques allow a distilled 3-8B model at Q4 quantization to run on consumer hardware with performance approaching much larger unquantized models.

## Related wikilinks

- [[concepts/local-llm]] — Original consolidated page (reference)
- [[concepts/harness-engineering]] — Local LLMs as harness components
- [[concepts/agentic-engineering]] — Using local LLMs in agent workflows
- [[concepts/reasoning-models]] — Distillation for CoT transfer
- [[concepts/llm-inference]] — Inference optimization techniques

## Sources

- r/LocalLLaMA, r/LocalLLM community discussions
- llama.cpp GitHub (ggerganov/llama.cpp)
- Ollama documentation
- vLLM project (vllm-project/vllm)
- Hugging Face blog on distillation
- Georgi Gerganov, PR #4856 and The Changelog #532
