---
title: "LLM Inference Optimization"
tags: [llm-inference-optimization-performance]
created: 2026-04-24
updated: 2026-04-24
---

# LLM Inference — Index

Techniques and engines for fast LLM inference, from consumer hardware to production clusters.

## Inference Engines

| Engine | Best For | Key Tech |
|--------|----------|----------|
|| [[concepts/inference/tgi]] | **Multi-LoRA serving, HF ecosystem** | Punica/LoRAX kernels, first-class multi-adapter, deep Hub integration |
|| [[concepts/inference/sglang]] | **Agentic loops, RAG, structured output** | RadixAttention, xgrammar, prefill-decode disaggregation |
|| [[concepts/inference/vllm]] | **General production serving** | PagedAttention, continuous batching, speculative decoding |
|| [[concepts/inference/llama-cpp]] | **CPU / Apple Silicon / consumer GPU** | GGUF format, local-first, zero cloud dependency |
|| Ollama | **Local LLM runner (CLI + API)** | Wraps llama.cpp, model library, one-line setup |
|| [[concepts/tensorrt-llm]] | **NVIDIA GPU 最高効率** | TensorRT compiler, FP8/FP4, Triton統合, ハードウェア最適化最大 |

## Optimization Techniques

1. **Speculative Decoding**: Using smaller models to draft tokens, larger models to verify
2. **KV Cache Optimization**: Efficient memory management for context windows (PagedAttention, RadixAttention)
3. **Batching Strategies**: Maximizing throughput on available hardware (continuous, chunked prefill)
4. **Model Parallelism**: Splitting large models across multiple devices (tensor, pipeline, expert)
5. **Quantization**: Reducing precision while maintaining quality (FP4/FP8/INT4/AWQ/GPTQ)
6. **Structured Generation**: Grammar-constrained decoding (JSON Schema, regex via xgrammar)

## When to Choose Which Engine

| Workload | Recommended Engine | Why |
|----------|-------------------|-----|
| Agentic loops with long system prompts | **SGLang** | RadixAttention shares KV cache across prefix |
| RAG pipelines with shared context | **SGLang** | Prefix tree caching |
| Structured JSON output required | **SGLang** | Native xgrammar constrained decoding |
|| Multi-LoRA production serving (30+ adapters) | **TGI** | Native multi-adapter, ~3% VRAM overhead for 30 adapters |
|| RL training rollout backend | **SGLang** | Proven in post-training pipelines |
|| General API serving | **vLLM** | Industry standard, broad adoption |
| Consumer hardware (Mac, laptop) | **llama.cpp** / Ollama | CPU/Apple Silicon optimized |
| Zero-config local testing | **Ollama** | One-line install, model library |

## Related

- [[concepts/local-llm]] — Local LLM ecosystem (quantization, distillation, hardware)
- [[concepts/structured-outputs]] — Structured generation patterns
- [[concepts/inference-speed-development]] — Inference speed economics (Steipete)
- [[concepts/compute-scaling-bottlenecks]] — Hardware constraints on AI scaling
