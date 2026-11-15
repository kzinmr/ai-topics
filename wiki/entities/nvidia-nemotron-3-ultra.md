---
title: "NVIDIA Nemotron 3 Ultra"
type: entity
created: 2026-06-05
updated: 2026-11-15
tags:
  - model
  - open-source
  - nvidia
  - ai-agents
  - inference
aliases: [Nemotron 3 Ultra, Nemotron-3-Ultra]
sources:
  - raw/newsletters/2026-11-14-open-source-ai-without-jensen-body.md
  - raw/newsletters/2026-06-05-ainews-not-much-happened-today.md
  - raw/newsletters/2026-08-12-ainews-how-to-steal-a-reasoning-trace.md
  - raw/articles/2026-08-14_nvidia_nemotron-teacher-competition-coding.md
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

## Companion Release: MOPD Teacher — Teacher Competition Coding

In August 2026 NVIDIA released **NVIDIA-Nemotron-Labs-Teacher-Competition-Coding**, a coding-specialized teacher model that supplies training signal to Nemotron 3 Ultra's [[concepts/multi-teacher-on-policy-distillation|Multi-Teacher On-Policy Distillation (MOPD)]] stage. It is produced by taking the post-trained Nemotron 3 Ultra student and adding a coding-focused SFT + RL round (execution-verified solutions, compiler/test-verified RL). It is released as a standalone checkpoint (550B total / 55B active, OpenMDW-1.1 license) because it is a strong competitive-coding model in its own right — and, more importantly, as one of **10+ domain-specialized teachers** whose public release makes Nemotron 3 Ultra's MOPD recipe inspectable for researchers.

Source: [[raw/articles/2026-08-14_nvidia_nemotron-teacher-competition-coding]]

## Ecosystem Verdict: "Not mission accomplished" (November 2026)

Benchmark coverage above measures the model; Nathan Lambert's post-Jensen assessment ([[events/nvidia-ceo-transition-2026]], Nov 14, 2026) measures the *program* — and finds it short despite its inputs:

> "The best people for attracting talent are the ones at the front of movements. Jensen helped catalyze this, and on many metrics was still losing. **Nemotron has had the right level of ambition and strong people, but it hasn't delivered to the point of being called 'mission accomplished.'** The competition here in building leading-edge models is more fierce than most give credit to. Having an organization with billions of dollars, solid people, and good vibes may not get you there. **You normally need something special.**"

This is a dated, contested counterweight to the "strongest US open-weights model" framing above: Lambert grants NVIDIA the funding, the ambition and the people, and argues precisely that those three are insufficient without a movement-leading champion — and that the champion (Jensen, who was "flooding the zone with funding") is now gone. See [[entities/nathan-lambert]] and [[concepts/open-source-ai-must-win]].

## Related

- [[entities/nvidia]] — Parent company
- [[entities/nvidia-nemotron-3-nano-omni]] — Nemotron 3 family's multimodal variant
- [[concepts/mixture-of-experts]] — MoE architecture
- [[concepts/long-context]] — Extended context window models
