---
title: "Lucas Atkins"
type: entity
created: 2026-05-25
updated: 2026-05-25
tags:
  - person
  - ml-engineering
  - moe
  - post-training
  - distributed-training
aliases:
  - Lucas Atkins
sources:
  - raw/articles/substack.com--redirect-a74f95f1-0e4a-44c1-8dea-64d936fa8d49--3f8b9141.md
---

# Lucas Atkins

**Lucas Atkins** is the CTO and co-founder of [[entities/arcee-ai|Arcee AI]], a U.S.-based open-model startup. He leads pretraining and architecture work, and authored the **Trinity Manifesto** — a document outlining Arcee's philosophy on open-weight model development.

## Background

Lucas Atkins leads the technical side of Arcee AI's transition from a post-training services company to a frontier model pretraining operation. His work spans architecture design, optimizer selection, training infrastructure, and the full model lifecycle from pretraining through RL post-training.

## Key Technical Work

### Trinity Large (2026)

Lucas led the architecture and training of **Trinity Large** (400B total, 13B active MoE), including:
- **Muon optimizer adoption** — chose Muon over Adam for faster convergence and reduced memory footprint (one momentum buffer vs Adam's two beta buffers), following Kimi's precedent
- **B300 GPU cluster management** — first public MoE training run at this scale on NVIDIA B300s; had to handle early software ecosystem gaps and data center bug fixes
- **MoE balancing** — implemented modified DeepSeek V3 auxiliary-loss-free loss plus sequence loss to prevent expert collapse during training
- **TorchTitan modifications** — integrated SFT fine-tuning directly into the pretraining framework, avoiding cross-engine MoE instabilities between training and inference
- **230B token SFT dataset** — 10x larger than typical post-training datasets

### Training Philosophy

Lucas has articulated several key principles:
1. **"Simplicity is key"** for SFT — avoids complex distillation and merging tricks now that RL dominates post-training
2. **RL is the future** — Arcee's RL pipeline is still immature but is where the next performance gains will come from
3. **Tool-use RL** — the next major hurdle is training models for 100+ tool call scenarios (search + code integrated reasoning)
4. **Open models need U.S. representation** — Trinity Manifesto advocates for U.S.-built open models as a counterweight to Chinese open-model dominance (Qwen, Kimi, GLM, MiniMax)

### Small Model Focus

Lucas believes **smaller MoE models** (like Trinity Nano/Mini) offer the best ROI for enterprise customers: "there's a tremendous amount of cost savings a company can get from optimizing on a smaller model." Arcee plans to push both the small-model frontier and the large-model frontier.

## Relationship to Open Model Ecosystem

Lucas frequently collaborates with [[entities/nathan-lambert|Nathan Lambert]] and other open-model researchers. His work is part of the broader **ATOM Project** movement to maintain U.S. leadership in open AI development.

## Trinity Manifesto

The Trinity Manifesto (authored by Lucas) outlines:
- Why U.S.-built open models matter (geopolitical and technical sovereignty)
- Why MoE architectures at small active-parameter counts are the future
- Why open weights + closed API is a false dichotomy — enterprise on-prem deployments are the real market
- Why simplicity in SFT + sophistication in RL is the right post-training strategy

## Cross-References

- **[[entities/arcee-ai]]** — Company co-founded with Mark McQuade
- **[[entities/mark-mcquade]]** — Co-founder/CEO
- **[[entities/nathan-lambert]]** — Collaborator, podcast host
- **[[concepts/moe-architecture]]** — Arcee's Trinity family uses sparse MoE
- **[[concepts/open-model-consortium]]** — Part of the U.S. open model ecosystem

## Sources

- [Interconnects: Arcee AI goes all-in on open models built in the U.S.](https://www.interconnects.ai/p/arcee-ai-goes-all-in-on-open-models) — Podcast interview with Nathan Lambert (Apr 2026)
- [Arcee AI Open Source Catalog](https://www.arcee.ai/open-source-catalog)
