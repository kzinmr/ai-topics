---
title: Groq
created: 2026-06-17
updated: 2026-06-17
type: entity
tags: [hardware, llm-inference, inference, company, startup, lpu, asic]
aliases: [Groq Inc., Groq LPU]
sources: [https://groq.com/]
---

# Groq

**Groq** is an AI inference infrastructure company that designs and manufactures custom **LPU (Language Processing Unit)** ASICs for ultra-low-latency large language model inference. Founded by ex-Google TPU engineers, Groq competes directly with GPU-based inference providers (NVIDIA, AMD) and cloud inference platforms (Together AI, Fireworks, Cerebras).

## LPU Architecture

The LPU is a **deterministic, single-core architecture** designed specifically for the sequential nature of autoregressive text generation:

- **TSP (Tensor Streaming Processor)**: Groq's first-generation chip, featuring a simplified core with massive on-die SRAM instead of HBM
- **Deterministic execution**: Unlike GPUs, the LPU's architecture guarantees predictable latency — no cache misses, no thread divergence
- **Memory architecture**: 230 MB of on-chip SRAM per chip, eliminating off-chip memory bottlenecks during inference
- **Scale-out design**: Multiple LPUs connected via RealScale™ mesh interconnect for linear throughput scaling

### Key Specifications

| Feature | Groq LPU | Typical GPU (H100) |
|---------|----------|---------------------|
| Memory type | On-chip SRAM | HBM3 (off-chip) |
| Memory bandwidth | 80 TB/s (on-chip) | 3.35 TB/s (HBM3) |
| Latency profile | Deterministic | Variable (cache, warp divergence) |
| Power efficiency | Higher for inference | Better for training |
| Architecture | Single-core TSP | Many-core SIMT |

## Performance Characteristics

Groq's primary differentiator is **inference speed**:

- **Token generation**: Sub-millisecond time-to-first-token on small-to-medium models
- **Throughput**: Competitive tokens/second for high-concurrency batched inference
- **Model support**: Primarily optimized for transformer-based LLMs (Llama, Mixtral, Gemma families)
- **Limitations**: Smaller on-chip memory restricts maximum model size per chip; less efficient for training workloads

## Product Evolution

### GroqCloud (2024)
Cloud API platform offering LPU inference as a service. Includes:
- REST API compatible with OpenAI SDK
- Pay-per-token pricing
- Model library with pre-optimized open-source models

### GroqSystem (2025+)
On-premise inference appliances for enterprise deployment:
- Rack-scale LPU clusters
- Sovereign/private cloud inference
- Integration with existing enterprise infrastructure

## Competitive Position

Groq occupies a distinct niche in the inference landscape:

| Provider | Architecture | Strength | Weakness |
|----------|-------------|----------|----------|
| **Groq** | Custom LPU ASIC | Lowest latency, deterministic | Limited model capacity/chip |
| **Together AI** | GPU clusters (NVIDIA) | Broad model support, training | GPU supply constraints |
| **Fireworks AI** | GPU + optimization | Compound AI, LoRA serving | GPU-dependent |
| **Cerebras** | Wafer-scale (CS-3) | Massive single-chip throughput | Niche form factor |
| **Groq competitor** | GPU-based (vLLM, SGLang) | Commodity hardware, flexible | Higher latency, variable perf |

## Company

- **Founded**: 2016 by Jonathan Ross (ex-Google TPU team)
- **HQ**: Mountain View, California
- **Funding**: $640M+ raised (Series D: $300M at $2.8B valuation, Aug 2023; additional rounds in 2024)
- **Key investors**: Tiger Global, D1 Capital, The Spruce House Partnership, Cisco Investments, Samsung Catalyst Fund
- **Notable hires**: Yann LeCun (technical advisor), multiple ex-Google/TPU, ex-Intel engineers

## Related Pages

- [[entities/together-ai]] — GPU-based inference platform
- [[entities/fireworks-ai]] — Compound AI inference
- [[entities/cerebras]] — Wafer-scale AI compute
- [[concepts/inference-engines]] — Landscape of LLM inference runtimes
- [[concepts/vllm]] — Popular GPU inference engine
- [[concepts/llm-inference]] — Overview of LLM inference techniques
- [[concepts/speed-as-scaling-law]] — Groq cited in speed-first AI discourse

## References

- Groq official website: https://groq.com/
- Groq LPU architecture overview: https://groq.com/technology/
- GroqCloud documentation: https://console.groq.com/docs
- "Groq's LPU: A New Architecture for AI Inference" — SemiAnalysis, 2024
