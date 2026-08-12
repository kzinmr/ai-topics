---
title: "NVIDIA Nemotron 3 Ultra"
type: entity
created: 2026-06-05
updated: 2026-08-12
tags:
  - model
  - open-source
  - nvidia
  - ai-agents
  - inference
aliases: [Nemotron 3 Ultra, Nemotron-3-Ultra]
sources:
  - raw/newsletters/2026-06-05-ainews-not-much-happened-today.md
  - raw/newsletters/2026-08-12-ainews-how-to-steal-a-reasoning-trace.md
---

# NVIDIA Nemotron 3 Ultra

An open-source 550B parameter LatentMoE hybrid model from [[entities/nvidia|NVIDIA]], with 55B active parameters and 1M context window. Released June 2026 as part of the Nemotron 3 family alongside [[entities/nvidia-nemotron-3-nano-omni|Nemotron 3 Nano Omni]].

## Specifications

| Property | Value |
|----------|-------|
| **Architecture** | LatentMoE hybrid (Mamba-2 interleaving + MoE + selected attention) |
| **Total parameters** | 550B |
| **Active parameters** | 55B |
| **Context window** | 1M tokens |
| **License** | Fully open weights, recipes |
| **Quantization** | NVFP4 (recommended), BF16 |
| **Positioning** | Long-running agent workloads |

## Performance

- **Intelligence Index**: 47.7 (NVFP4), 48.2 (BF16) — per @ArtificialAnlys, strongest US open-weights model
- **Speed**: Up to 5x faster than comparable models for agentic workloads
- **Cost**: ~30% lower cost for agentic serving
- **Inference**: Minimum 8x GB200/B200/GB300/B300, 16x H100, or 8x H200

## Companion Release: Nemotron 3.5 ASR

A smaller companion model — 0.6B parameter streaming ASR model with 40 language-locale combinations, sub-100ms latency, built on cache-aware FastConformer/RNN-T design.

## Companion Release: Nemotron 3.5 Lightning

Released August 2026, **Nemotron 3.5 Lightning** is a 30B parameter [[concepts/mixture-of-experts|Mixture-of-Experts (MoE)]] model with roughly 3B active parameters, positioned for always-on agent workloads. It delivers up to 4× throughput with a 1M context window, and ships open, customizable release artifacts. Available via Together AI, Ollama, Baseten, vLLM, and the Perplexity API; @kimmonismus dubbed it NVIDIA's "local agent workhorse."

## Related

- [[entities/nvidia]] — Parent company
- [[entities/nvidia-nemotron-3-nano-omni]] — Nemotron 3 family's multimodal variant
- [[concepts/mixture-of-experts]] — MoE architecture
- [[concepts/long-context]] — Extended context window models
