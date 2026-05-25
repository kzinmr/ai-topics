---
title: "Arcee AI"
type: entity
created: 2026-05-25
updated: 2026-05-25
tags:
  - company
  - open-source
  - post-training
  - moe
  - distributed-training
  - rlhf
aliases:
  - Arcee
sources:
  - raw/articles/substack.com--redirect-a74f95f1-0e4a-44c1-8dea-64d936fa8d49--3f8b9141.md
  - https://www.arcee.ai/
  - https://www.arcee.ai/open-source-catalog
---

# Arcee AI

**Arcee AI** is an open-model startup that pivoted from post-training services to frontier model pretraining. Based in the U.S., Arcee develops and releases open-weight Mixture-of-Experts (MoE) models under the **Trinity** family. They are one of the key participants in [[concepts/open-model-consortium|the open model ecosystem]], alongside organizations like Ai2 (OLMo), Hugging Face, Nous Research, and Prime Intellect.

## Company Background

Arcee AI began as a **post-training and fine-tuning shop**, building specialized models for enterprise customers. This gave them deep expertise in SFT, DPO, RLHF, and model merging (they created **MergeKit**). Recognizing that the open-model ecosystem needed U.S.-based frontier pretraining, Arcee pivoted to building their own models from scratch.

### Leadership

| Person | Role | Background |
|--------|------|------------|
| **[[entities/mark-mcquade|Mark McQuade]]** | Founder/CEO | Previously at Hugging Face (monetization), Roboflow |
| **[[entities/lucas-atkins|Lucas Atkins]]** | CTO | Leads pretraining/architecture, wrote the Trinity Manifesto |
| **Varun Singh** | Pretraining Lead | — |

- **Team size**: 13 people dedicated to model training
- **Total training cost** for Trinity Large: ~$20 million (compute, salaries, data, storage, ops)
- **Timeline**: 6 months from design to release for Trinity Large

## Trinity Model Family

Arcee's models are named after the **Trinity** series, reflecting their three-tier approach (Nano → Mini → Large).

### Trinity Large (Preview)

- **Architecture**: Sparse Mixture-of-Experts (MoE)
- **Total parameters**: 400B
- **Active parameters**: 13B
- **Experts**: 256
- **Training compute**: 22,048 NVIDIA B300 GPUs
- **Training data**: 17 trillion tokens
- **Optimizer**: Muon (not Adam)
- **Framework**: Modified TorchTitan
- **MoE balancing**: Modified DeepSeek V3 auxiliary-loss-free loss + sequence loss
- **Cost**: $20 million total
- **Benchmarks**: AIME 2025 mid-80s, GPQA Diamond ~75, MMLU Pro ~82

Key technical decisions:
- **Muon optimizer** chosen over Adam for faster convergence with less memory (one momentum buffer vs Adam's two beta buffers)
- **No multi-token prediction or FP8** to reduce risk during first large-scale training run
- **Post-training integration**: SFT fine-tuning integrated directly into TorchTitan on the same cluster, not a separate post-training phase — avoids MoE instabilities between training and inference engines
- **SFT dataset**: 230 billion tokens (10x typical post-training datasets)
- **RL pipeline**: Still immature; next priority focuses on tool-use RL (search + code integrated reasoning, 100+ tool calls per response)

### Trinity Mini

- **Total parameters**: 26B
- **Active parameters**: 3B
- **Training**: 512 H100s, ~45 days

### Trinity Nano Preview

- **Total parameters**: 6B
- **Active parameters**: 1B
- **Training**: 512 H200s, ~30 days
- **Notable**: Model card describes it as having "a delightful personality and charm" but warns it "may be unstable in certain use cases" due to pushing boundaries at small scale

## Training Infrastructure

- **Primary cluster**: 22,048 NVIDIA B300 GPUs (among the largest public MoE training runs on B300s)
- **Secondary cluster**: 512 H100s for smaller models (Mini, Nano)
- **Previous cluster**: 64 H100s for post-training work
- **B300 challenges**: Early software ecosystem lacked out-of-the-box B300 support; required custom bug fixes from the data center team
- **Training stability**: First 10 days showed expert collapse after ~1 trillion tokens; required intervention to stabilize MoE routing

## Open Source Tools

Arcee AI maintains **MergeKit**, an open-source model merging toolkit for combining model weights without retraining. Developed during their post-training services phase, it remains widely used in the open-model community.

## Business Model

Arcee monetizes through **enterprise-grade open-weight model deployments**. Their strategy:
1. Build reputation with high-quality open models
2. Offer on-prem deployment services to enterprises
3. Use open-source as a business moat (demonstrates capability, builds trust)
4. Specialize in domain-specific fine-tuning (their original expertise)

As CEO Mark McQuade (ex-Hugging Face monetization) puts it: they're proving that open models can be a viable business, not just a research project.

## Relationship to ATOM Project

Arcee AI is one of the key participants responding to [[entities/nathan-lambert|Nathan Lambert]]'s **[[concepts/ram-relative-adoption-metric|ATOM Project]]** call to action for U.S.-based open model development. They are among the handful of companies (alongside Prime Intellect, Nous, Moondream, Pleias, Jina, Hugging Face pretraining team, Allen AI, Eleuther) building open AI infrastructure.

## Timeline

| Date | Event |
|------|-------|
| Pre-2025 | Post-training/fine-tuning services, MergeKit development |
| Jul 2025 | Release of Arcee 4.5B dense model |
| Late 2025 | Trinity Nano Preview and Mini development |
| Apr 2026 | Interconnects podcast interview with Nathan Lambert |
| May 2026 | Trinity Large release (400B/13B MoE) |
| 2026 (planned) | Trinity reasoning model (RL-focused) |

## Cross-References

- **[[entities/nathan-lambert]]** — Podcast host, ATOM Project advocate, OLMo collaborator
- **[[concepts/open-model-consortium]]** — Arcee is a key participant in the open model ecosystem
- **[[concepts/post-training]]** — Arcee's expertise spans SFT, DPO, RLHF, and model merging
- **[[concepts/moe-architecture]]** — Trinity family uses sparse MoE at multiple scales
- **[[entities/mark-mcquade]]** — Founder/CEO, ex-Hugging Face monetization
- **[[entities/lucas-atkins]]** — CTO, pretraining lead, Trinity Manifesto author

## Sources

- [Interconnects: Arcee AI goes all-in on open models built in the U.S.](https://www.interconnects.ai/p/arcee-ai-goes-all-in-on-open-models) — Podcast transcript with Lucas Atkins, Mark McQuade, Varun Singh (Apr 2026)
- [Arcee AI Open Source Catalog](https://www.arcee.ai/open-source-catalog)
- [Trinity Large Technical Report](https://www.arcee.ai/blog/trinity-large) (via Interconnects)
