---
title: CoreWeave
type: entity
tags:
  - company
  - hardware
  - infrastructure
created: 2026-06-15
updated: 2026-06-15
sources:
  - "https://coreweave.com"
  - "https://investors.coreweave.com"
  - "https://corbt.com/posts/openpipe-coreweave"
---

# CoreWeave

**Type:** GPU cloud provider / AI infrastructure platform
**Founded:** 2017 (originally as Atlantic Crypto; pivoted to AI ~2019–2020)
**Founders:** Michael Intrator (CEO), Brian Venturo (CTO)
**HQ:** New York / New Jersey
**IPO:** March 2025, NASDAQ (ticker: CRWV)
**Website:** https://coreweave.com

## Overview

CoreWeave is a purpose-built GPU cloud provider for AI workloads. Originally founded as a cryptocurrency mining company, it pivoted to become one of the largest GPU cloud platforms serving the AI industry. CoreWeave differentiates from hyperscalers (AWS, GCP, Azure) by offering bare-metal GPU access at lower cost and higher performance for ML training and inference workloads.

## Business Model

CoreWeave operates GPU clusters optimized for AI training and inference:
- **Bare-metal GPU access**: NVIDIA H100, A100, and next-gen GPUs without the overhead of hyperscaler abstractions
- **Kubernetes-native**: CoreWeave Kubernetes Service (CKS) for workload orchestration
- **Competitive pricing**: Typically 50-80% cheaper than equivalent hyperscaler GPU instances
- **Long-term contracts**: Multi-year capacity agreements with major customers

## Key Customers

- **Microsoft**: One of CoreWeave's largest customers; multi-billion dollar cloud infrastructure deal
- **OpenAI**: Reportedly uses CoreWeave for training compute
- **Various AI labs and startups**: Training workloads that need large GPU clusters

## Acquisitions (2025)

CoreWeave executed a series of acquisitions to vertically integrate from compute infrastructure into the ML platform layer:

### Weights & Biases (~$1.7B, 2025)
The largest acquisition. W&B provides experiment tracking, model management, and LLM observability. See [[entities/weights-and-biases|Weights & Biases]].

**Strategic rationale**: CoreWeave moves from being a pure compute provider to offering a full-stack AI platform — GPU cloud (CoreWeave) + training tracking (W&B) + LLM tracing (W&B Weave).

### OpenPipe (2025)
RL post-training company founded by [[entities/kyle-corbitt|Kyle Corbitt]]. Provides GRPO-based RL training as a service for custom agent models. See [[entities/openpipe|OpenPipe]].

**Strategic rationale**: Adds the post-training layer — customers can go from compute (CoreWeave GPUs) to custom-trained models (OpenPipe ART) to observability (W&B) on a single platform. Kyle Corbitt's blog post: [OpenPipe is Joining CoreWeave](https://corbt.com/posts/openpipe-coreweave).

### SkyPilot (2025)
Open-source framework for running AI workloads on any cloud, originally from UC Berkeley's Sky Computing Lab. SkyPilot provides a unified interface for launching jobs across cloud providers with cost optimization.

**Strategic rationale**: SkyPilot simplifies multi-cloud GPU orchestration. By acquiring SkyPilot, CoreWeave gains both the technology (cost-optimized job scheduling) and the team (Berkeley Sky Lab researchers) to make CoreWeave the easiest cloud to run AI workloads on.

## Vertical Integration Strategy

The three acquisitions form a coherent stack:

```
┌─────────────────────────────────────┐
│  LLM Application Layer              │
│  W&B Weave (tracing + evaluation)   │
├─────────────────────────────────────┤
│  Training & Post-Training           │
│  W&B Models (experiment tracking)   │
│  OpenPipe ART (RL post-training)    │
├─────────────────────────────────────┤
│  Compute Orchestration              │
│  SkyPilot (multi-cloud scheduling)  │
├─────────────────────────────────────┤
│  GPU Infrastructure                 │
│  CoreWeave Cloud (H100, A100, etc.) │
└─────────────────────────────────────┘
```

This vertical integration mirrors the trend of cloud providers moving up the stack: instead of just renting GPUs, CoreWeave aims to be the one-stop platform for the entire AI development lifecycle.

## Industry Position

- **vs. Hyperscalers (AWS, GCP, Azure)**: CoreWeave focuses exclusively on GPU/AI workloads, offering better price-performance for training and inference
- **vs. Other Neoclouds (Lambda, Together AI, Crusoe)**: CoreWeave has the largest scale and most complete platform after the acquisitions
- **Post-IPO**: One of the largest tech IPOs of 2025; valuation reached ~$23B+ at peak

## Market Context

CoreWeave's growth is driven by the massive demand for GPU compute from AI labs. The company's long-term capacity agreements (particularly with Microsoft) provide revenue visibility, while the platform acquisitions (W&B, OpenPipe, SkyPilot) aim to increase stickiness and move up the value chain.

## Risk Factors

- **Customer concentration**: Heavy dependence on Microsoft and a few large customers
- **GPU supply**: Reliance on NVIDIA for GPU allocation; AMD/Intel competition
- **Capital intensity**: Massive CapEx for GPU cluster buildout; debt-financed growth
- **Hyperscaler competition**: AWS, GCP, Azure are investing heavily in AI-optimized infrastructure

## Related

- [[entities/weights-and-biases|Weights & Biases]] — Acquired (2025)
- [[entities/openpipe|OpenPipe]] — Acquired (2025)
- [[entities/wandb-weave|W&B Weave]] — LLM tracing (part of W&B acquisition)
- [[entities/kyle-corbitt|Kyle Corbitt]] — OpenPipe CTO, now at CoreWeave
- [[entities/ed-zitron]] — Commentator on neocloud business models
- [[concepts/ai-subprime]] — Market risk analysis including CoreWeave exposure
- [[concepts/google-spacex-ai-compute-deal]] — AI compute deal context
