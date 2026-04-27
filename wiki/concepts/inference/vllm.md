---
title: "vLLM"
tags: [local-llm, inference, serving, open-source, performance]
created: 2026-04-14
updated: 2026-04-27
type: concept
sources:
  - raw/articles/crawl-2026-04-27-vllm-features.md
---

# vLLM

vLLM is a high-throughput LLM serving engine with PagedAttention optimization, developed by UC Berkeley and maintained by the vLLM project. As of April 2026, the v0.19.0 release (448 commits, 197 contributors) represents a major advancement in production LLM serving.

## Key Capabilities

- **PagedAttention** — Virtual memory-inspired KV cache management (24x throughput vs. HF Transformers)
- **Continuous batching** and chunked prefill
- **Zero-bubble async scheduling** + speculative decoding (v0.19.0)
- **Model Runner V2** — Piecewise CUDA graphs for PP, rejection sampler
- **Performance mode** — `--performance-mode {balanced, interactivity, throughput}` (v0.17.0)

## Latest Features (v0.18.0–v0.19.1)

### Gemma 4 Support (v0.19.0)
- Full architecture support: MoE, multimodal, reasoning, tool-use
- Requires `transformers>=5.5.0`
- Pre-built Docker: `vllm/vllm-openai:gemma4`
- v0.19.1 patch: streaming tool call fixes, BOS injection, quantized MoE, Eagle3, LoRA

### Anthropic API Compatibility
- Anthropic thinking blocks support
- `count_tokens` API endpoint
- `tool_choice=none`
- Streaming and image handling fixes

### Qwen3.5 GDN (Gated Delta Networks)
- Full support with FP8 quantization
- MTP (Multi-Token Prediction) speculative decoding
- Reasoning parser support

### Performance & Engine
- **Zero-bubble async scheduling** — overlaps scheduling with execution, eliminating idle bubbles
- **DBO generalization** — Dual-Batch Overlap now works with all models (not just specific architectures)
- **CPU KV cache offloading** (V1) — pluggable cache policy, block-level preemption, hybrid models
- **ViT Full CUDA Graphs** — reduced vision encoder overhead for multimodal serving
- **Triton autotuning disk cache** enabled by default
- **FlexAttention** — custom mask modifications for attention

### Hardware
- **NVIDIA Blackwell** — optimized SM120 CUTLASS blockwise FP8 GEMM, DeepGEMM E8M0
- **NVIDIA B300/GB300** (SM 10.3) — allreduce fusion enabled by default
- **AMD ROCm 7.2.1** — DeepEP all2all, FP8×FP8 attention, AWQ Marlin, RDNA4
- **Intel XPU** — MLA model support, CompressedTensor W4A8
- **CPU** — tcmalloc by default (48.9% throughput improvement for pooling models)

## Comparison with Alternative Inference Engines

| Aspect | vLLM | llama.cpp | SGLang |
|--------|------|-----------|--------|
| Target | Production serving | Local inference | Research + production |
| Throughput | Very high (batched) | Moderate | High |
| Latency | Low (optimized) | Low | Very low (RadixAttention) |
| GPU support | NVIDIA, AMD, Intel, TPU | CPU, Apple, NVIDIA, AMD, Vulkan | NVIDIA, AMD, CPU |
| Model format | HF Transformers | GGUF | HF Transformers |
| Structured output | Outlines integration | Grammar/JSON schema | Native (xgrammar) |
| Speculative decoding | ✅ (v0.19 zero-bubble) | ✅ (6 variants) | ✅ |

## Q2 2026 Roadmap

- **torch.compile**: 1.3x cold compile speedup, ≤2s warm compile (5x improvement with PyTorch 2.12)
- **Full vLLM IR migration**
- **Improved performance dashboard** for tracking compile speedups
- **Custom helion kernel** by default
- **Weight loading and compilation overlap** (unstable in Q2, stable in Q3)

## Related wikilinks

- [[concepts/local-llm]] — Local LLM ecosystem overview
- [[concepts/inference/llama-cpp]] — Local inference engine alternative
- [[concepts/inference/sglang]] — SGLang serving framework
- [[concepts/speculative-decoding]] — Inference acceleration technique
- [[concepts/local-llm/model-quantization]] — Quantization formats and techniques

## Sources

- vllm-project/vllm on GitHub — Release notes (v0.17.0–v0.19.1)
- raw/articles/crawl-2026-04-27-vllm-features.md
- PagedAttention research paper (Kwon et al., 2023, SOSP)
- vLLM Q2 2026 Roadmap (GitHub Issue #39749)
