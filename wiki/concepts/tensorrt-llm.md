---
title: "TensorRT-LLM — NVIDIA Inference Optimization Engine"
type: concept
created: 2026-05-01
updated: 2026-05-01
tags:
  - concept
  - inference
  - nvidia
  - optimization
status: L1
aliases:
  - tensorrt-llm
  - nvidia-tensorrt
  - trt-llm
sources: []
related:
  - "[[concepts/inference/_index]]"
  - "[[concepts/inference/vllm]]"
  - "[[concepts/inference/sglang]]"
  - "[[concepts/serving-llms-vllm]]"
  - "[[concepts/kv-cache]]"
  - "[[concepts/training-infra/gpu-vram-fundamentals]]"
  - "[[concepts/training-infra/model-serving-autoscaling]]"
  - "[[concepts/training-infra/_index]]"
---

# TensorRT-LLM — NVIDIA Inference Optimization Engine

> NVIDIA's LLM inference optimization engine. Integrates with Triton Inference Server to deliver the best inference performance on NVIDIA GPUs (especially H100/B200). Enables lower-level hardware optimization compared to vLLM.

## Why This Matters

TensorRT-LLM aims for **absolute lowest latency** and **highest hardware efficiency** on NVIDIA GPUs. While vLLM prioritizes versatility and community-driven evolution, TensorRT-LLM maximizes NVIDIA GPU capabilities (FP8 Transformer Engine, NVLink optimization, SM occupancy tuning).

## Outline

### 1. Architecture Overview

- **TensorRT Compiler**: Compiles model graphs into optimized CUDA kernels
- **Plugin system**: Specialized kernels for FlashAttention, MoE, FP8 inference
- **Weight-only quantization**: INT4/INT8/FP8/Float32 support
- **KV Cache quantization**: Memory reduction via INT8 KV Cache
- **In-flight batching**: Equivalent to vLLM's continuous batching
- **Paged KV Cache**: Equivalent to vLLM's PagedAttention
- **Speculative Decoding**: Standard support (Medusa, Eagle compatible)

### 2. Key Optimizations

| Feature | Description | Effect |
|------|------|------|
| **FP8 Quantization** | Leverages Transformer Engine | H100/B200: 2x vs FP16 |
| **INT4 AWQ** | Activation-aware weight quantization | 4x memory reduction, high quality maintained |
| **In-flight Batching** | Dynamic batch management | Throughput comparable to vLLM |
| **PagedAttention** | Virtual memory-style KV cache management | Memory fragmentation reduction |
| **Speculative Decoding** | Draft model + Target model | 2-4x latency improvement |
| **Multi-GPU TP/PP** | Tensor/Pipeline Parallel | Large model support |
| **CUDA Graph Capture** | Full CUDA Graph capture | Kernel launch overhead reduction |
| **SM Partitioning** | GPU partitioning alternative to MIG | High-efficiency multi-tenancy |

### 3. vLLM vs TensorRT-LLM Comparison

| Aspect | vLLM | TensorRT-LLM |
|------|------|-------------|
| **Developer** | UC Berkeley (community) | NVIDIA |
| **GPU Optimization** | General CUDA | NVIDIA-specific, optimized per generation |
| **Model Support** | Broad (via HF Hub) | Limited (per-model builds) |
| **Compilation** | Not needed (JIT/Fallback) | Required (TensorRT IR build) |
| **Triton Integration** | Via C API | Native integration |
| **Deployment Complexity** | Low (pip install) | High (Docker build required) |
| **Peak Throughput** | High | Very high |
| **Minimum Latency** | Low | Very low |
| **Community** | Active (broad contributors) | NVIDIA-led |
| **License** | Apache 2.0 | NVIDIA Proprietary |

### 4. Deployment Patterns

- **Triton Inference Server + TensorRT-LLM backend**: Standard configuration
- **Single GPU**: 70B model within 1 GPU via FP4/INT4 quantization
- **Multi-GPU**: Distributed via TP/PP, NVLink effective
- **Multi-Node**: Cluster inference via InfiniBand
- **Mixed Models**: Multi-model management via Triton

### 5. Performance Benchmarks (Approximate)

| Model | GPU | Engine | Throughput (tok/s) | Latency (ms/tok) |
|--------|-----|--------|---------------------|-------------------|
| LLaMA-2 70B (FP16) | 1x H100 | vLLM | ~1200 | ~25ms |
| LLaMA-2 70B (FP16) | 1x H100 | TRT-LLM | ~1500 | ~20ms |
| LLaMA-2 70B (FP8) | 1x H100 | TRT-LLM | ~2800 | ~10ms |
| GPT-175B (FP16) | 8x H100 | TRT-LLM | ~5000 | ~8ms |
| Nemotron-4 340B | 8x B200 | TRT-LLM | ~8000 | ~7ms |

*(Note: Actual values vary significantly by workload and configuration)*

### 6. When to Use TensorRT-LLM

#### ✅ Best Suited For
- Maximum throughput required on NVIDIA GPU clusters
- Stringent latency SLOs (< 50ms P99)
- Existing Triton Inference Server deployment
- Inference cost minimization is top priority
- Team capable of CUDA kernel-level tuning

#### ❌ Not Suited For
- Frequent switching between diverse models (build time)
- Open source transparency needed
- Small teams (high operational cost)
- vLLM already provides sufficient throughput
- Non-NVIDIA GPUs (AMD, Intel, Apple Silicon)

### 7. Integration with Ecosystem

- **Triton Inference Server**: Integrated as standard backend
- **NVIDIA NIM**: Containerized microservice
- **Kubernetes + GPU Operator**: Automated deployment
- **NVIDIA AI Enterprise**: Enterprise support
- **NeMo / Megatron-LM**: Seamless export from training

## Key Resources

- [TensorRT-LLM GitHub](https://github.com/NVIDIA/TensorRT-LLM)
- [Triton Inference Server](https://github.com/triton-inference-server/server)
- [NVIDIA NIM](https://build.nvidia.com/explore/reasoning)
- [NVIDIA GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/)

## Related Pages

- [[concepts/inference/_index]] — Inference engine comparison
- [[concepts/inference/vllm]] — vLLM (primary competitor)
- [[concepts/inference/sglang]] — SGLang (agent-optimized)
- [[concepts/serving-llms-vllm]] — vLLM serving patterns
- [[concepts/training-infra/gpu-vram-fundamentals]] — NVIDIA GPU capabilities
- [[concepts/training-infra/model-serving-autoscaling]] — Production serving infrastructure
- [[concepts/training-infra/_index]] — Parent page

## TODO

- [ ] Add detailed FP8/FP4 quantization benchmark results
- [ ] Add Triton Inference Server integration config examples
- [ ] Add Docker build process walkthrough
- [ ] Add multi-node TP/PP configuration guide
- [ ] Add speculative decoding support details (Eagle3, Medusa)
- [ ] Add TensorRT model format (.engine) build optimization tips
- [ ] Add benchmark methodology and caveats (prompt length, batch size effects)
