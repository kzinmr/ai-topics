---
title: Zyphra
type: entity
category: company
tags:
  - lab
  - open-source
  - infrastructure
  - amd
  - model
  - vlm
  - ai-agents
  - zyphra
status: active
aliases: [ZyphraAI]
sources:
  - https://www.zyphra.com/about
  - https://huggingface.co/Zyphra
  - https://www.zyphra.com/post/zaya1-vl-8b
  - https://pitchbook.com/profiles/company/437883-40
  - https://startup-seeker.com/company/zyphra~com
created: 2026-05-09
updated: 2026-05-09
---

# Zyphra

**Zyphra** is an open superintelligence research and product company based in San Francisco, CA. The company operates across two pillars: **Zyphra Research** (training multimodal open models on heterogeneous compute) and **Zyphra Cloud** (a full-stack AI platform built on AMD for developers, enterprises, and hyperscalers).

## Company

- **Founded**: 2020-2023
- **Headquarters**: Palo Alto / San Francisco, CA; with presence in Montreal and London
- **CEO/Founder**: Krithik Puthalath; co-founders include Tomás Figliolia and Travis Oliphant
- **Team**: ~20-31 employees
- **Funding**: ~$121M total; Series A of $110M (Oct 2025) led by AMD and IBM at ~$1B valuation
- **Key investors**: AMD Ventures, IBM, BC VC, Bison Ventures, Future Ventures, Defined Capital

## Mission

Zyphra's mission is to build human-aligned AI that helps individuals and organizations reach their fullest potential. They believe intelligence should not be controlled by a few. Their principles:

- **Transparent**: Open models provide visibility into AI knowledge, reasoning, and decision-making
- **Sovereign**: Users own their models, data, and deployments
- **Customizable**: AI adaptable to specific domains and workflows
- **Distributed**: Intelligence runs across any hardware without lock-in

## Models

### ZAYA1 Series

The ZAYA1 family uses Mixture of Experts (MoE) architecture, trained end-to-end on AMD hardware.

| Model | Type | Active / Total Params | License | Status |
|-------|------|----------------------|---------|--------|
| [[concepts/zaya1-8b]] | LLM (base) | 700M / 8B | Apache 2.0 | Released |
| [[concepts/zaya1-vl-8b]] | VLM | 700M / 8B | Apache 2.0 | Released (May 2026) |
| [[concepts/zaya1-74b-preview]] | LLM (reasoning-base) | 4B / 74B | Apache 2.0 | Preview |

### Architectural Innovations

- **Vision-specific LoRA parameters** (ZAYA1-VL-8B): Specialized LoRA on MLPs and CCA weights activated only on vision tokens
- **Bidirectional attention for image tokens** (ZAYA1-VL-8B): Non-causal attention across image regions
- **MoE on AMD**: All models trained end-to-end on AMD GPUs

## Zyphra Cloud

A full-stack AI platform built on AMD, designed for advanced AI systems with focus on long-horizon agents. Also developing **MaiaOS**, a multimodal agent system combining neural network architectures, long-term memory, and reinforcement learning.

## See Also

- [[concepts/zaya1-vl-8b]]
- [[concepts/zaya1-74b-preview]]
- [[concepts/mixture-of-experts]]
- [[entities/amd]]
