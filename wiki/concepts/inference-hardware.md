---
title: "Inference Hardware"
type: concept
aliases:
  - inference-hardware
  - ai-inference-silicon
  - accelerator-landscape
created: 2026-04-25
updated: 2026-11-20
tags:
  - concept
  - infrastructure
  - hardware
  - ai-hardware
  - gpu
  - inference
  - llm-inference
  - asic
sources: []
related:
  - "[[concepts/inference]]"
  - "[[concepts/custom-ai-silicon]]"
  - "[[concepts/cuda-moat]]"
  - "[[concepts/llm-cost-crisis]]"
---

# Inference Hardware

**Inference Hardware** is the silicon-and-systems layer that determines the floor cost,
latency, and throughput of serving an LLM or agent. The software stack — engines like
vLLM/SGLang ([[concepts/inference]]) and serving patterns — runs *on top of* this
layer. This page is the **umbrella index** over the wiki's hardware topics: it organizes
them into tiers and shows how the pieces connect, rather than duplicating the detail in
each leaf page.

The hardware layer is decisive economically: "cheaper hardware directly changes the
economics" of the [[concepts/llm-cost-crisis|LLM cost crisis]], and the viability of
non-NVIDIA serving is the crux of both the [[concepts/cuda-moat|CUDA-moat]] and
[[concepts/custom-ai-silicon|custom-silicon]] debates.

## The Hardware Tiers

LLM serving spans a spectrum from cloud-scale racks down to a laptop. Each tier has its
own wiki coverage:

| Tier | Role | Representative pages |
|------|------|----------------------|
| **Data-center GPUs** | Frontier training + high-throughput serving | [[concepts/nvidia-blackwell-architecture]], [[concepts/nvidia-vera-rubin]], [[concepts/nvidia-dynamo]] |
| **Custom / cloud ASICs** | Diversification away from NVIDIA | [[concepts/custom-ai-silicon]], [[concepts/trnrt-trainium-inference-engine]] (Trainium), [[concepts/openai-jalapeno-inference-chip]], [[concepts/torchtpu]] (TPU) |
| **Wafer-scale / special** | Extreme-throughput niche | [[concepts/cerebras-disaggregated-inference]], [[concepts/cerebras-cs4]] |
| **Consumer / workstation GPU** | Local serving, fine-tune | [[concepts/gpu-pricing-spread]], [[concepts/gpu-cloud-rankings]], [[concepts/gpu-cluster-tco-goodput]] |
| **CPU inference** | Memory-bound, low-batch, privacy | [[concepts/cpu-inference-llm]] |
| **Apple silicon / edge** | On-device, local-LLM | [[concepts/apple-silicon-m6-m5-ultra]], [[concepts/local-llm/local-llm-inference-hardware]] |

## Why the Hardware Layer Matters

- **Cost floor.** Per-token price is set by silicon + memory bandwidth + utilization.
  Software (batching, quantization, KV-cache) recovers a constant factor; hardware
  changes the asymptote. See [[concepts/llm-cost-crisis]] and
  [[concepts/gpu-cluster-tco-goodput]].
- **Memory-bound regime.** Decoding is bandwidth-limited, not FLOP-limited. This is why
  [[concepts/cpu-inference-llm|CPU inference]] is viable for low-batch/long-context and
  why HBM capacity (not just TFLOPS) drives model choice — the RAM-tier logic in
  [[concepts/local-llm/local-llm-inference-hardware]].
- **The CUDA moat.** Most serving software assumes NVIDIA. Whether non-NVIDIA silicon
  can serve *agentic* workloads economically is the open question — TrnRT
  ([[concepts/trnrt-trainium-inference-engine]]) is an early answer; the broader thesis
  lives in [[concepts/cuda-moat]] and [[concepts/custom-ai-silicon]].
- **The GPU bubble.** Supply/demand of accelerators swings pricing and availability —
  [[concepts/gpu-bubble-ai-inference]], [[concepts/gpu-pricing-spread]],
  [[concepts/gpu-cloud-rankings]].

## Software Stacking On Top

The same hardware runs radically different engines depending on the workload (local vs
server vs agentic). The engine layer is documented separately in
[[concepts/inference]] (llama.cpp / vLLM / SGLang) and
[[concepts/llm-inference]]. Disaggregation (separating prefill and decode across
devices) is its own theme: [[concepts/cerebras-disaggregated-inference]],
[[concepts/nvidia-dynamo]].

## Cross-Cutting Concerns

- **Security of the inference substrate.** Cache side-channels between co-located
  agents ([[concepts/cpu-cache-covert-channels-between-agents]]), inference-engine
  security ([[concepts/inference-engine-security]]), provable/attested inference
  ([[concepts/provable-inference]]).
- **Economics & sourcing.** [[concepts/gpu-cluster-tco-goodput]] (goodput per dollar),
  [[concepts/space-gpus]] (compute in orbit), export-control dynamics underpinning the
  custom-silicon push.

## How to Use This Page

- New accelerator / serving-silicon story → file under the appropriate tier above, then
  ensure it's linked here.
- Engine/serving *software* question → [[concepts/inference]], not this page.
- This page should stay an **index/orientation** page; deep technical detail belongs in
  the leaf pages to avoid drift.

## Graph Structure Query

```
[inference-hardware] ──umbrella-of──→ [concept: custom-ai-silicon]
[inference-hardware] ──umbrella-of──→ [concept: cuda-moat]
[inference-hardware] ──umbrella-of──→ [concept: trnrt-trainium-inference-engine]
[inference-hardware] ──umbrella-of──→ [concept: cpu-inference-llm]
[inference-hardware] ──supports──→ [concept: inference]            # engines run on hardware
[inference-hardware] ──determines──→ [concept: llm-cost-crisis]    # hardware sets cost floor
[inference-hardware] ──relates-to──→ [concept: gpu-bubble-ai-inference]
[inference-hardware] ──part-of──→ [concept: infrastructure]
```

> Informs graph queries: this is the hardware hub. Engines ([[concepts/inference]])
> sit above it; the cost floor it sets drives [[concepts/llm-cost-crisis]]; the
> diversification thesis is [[concepts/custom-ai-silicon]] vs [[concepts/cuda-moat]].

## Related Pages

- [[concepts/inference]] — engines that run on this hardware
- [[concepts/custom-ai-silicon]] — the diversification thesis
- [[concepts/cuda-moat]] — the lock-in thesis
- [[concepts/trnrt-trainium-inference-engine]] — non-NVIDIA agentic serving test case
- [[concepts/cpu-inference-llm]] — the CPU tier
- [[concepts/local-llm/local-llm-inference-hardware]] — local RAM-tiering
- [[concepts/llm-cost-crisis]] — economics the hardware layer sets
- [[concepts/gpu-bubble-ai-inference]] — accelerator supply/demand
