---
title: "Siyan Zhao"
type: entity
created: 2026-05-18
updated: 2026-05-19
tags:
  - person
  - training
  - reasoning
  - model
sources:
  - raw/articles/2026-05-18_opsd-blog-siyan-zhao.md
  - https://siyan-zhao.github.io/
  - https://siyan-zhao.github.io/blog/2026/opsd/
  - https://arxiv.org/abs/2601.18734
  - https://github.com/siyan-zhao/OPSD
aliases:
  - Siyan Zhao
  - siyan-zhao
---

# Siyan Zhao

**Siyan Zhao** is a 4th-year PhD student in Computer Science at UCLA, advised by Professor **Aditya Grover**, with research affiliations at **Meta Superintelligence Labs**. Her research focuses on endowing machines with human-like reasoning and efficiency through reinforcement learning, preference alignment, and LLM inference optimization.

She is best known for **On-Policy Self-Distillation (OPSD)**, a method where a single LLM acts as both teacher and student, achieving GRPO-level reasoning performance at ~1/64 the token cost. She also led the **d1** paper (NeurIPS 2025 Spotlight) on scaling reasoning in diffusion LLMs via RL.

## Overview

- **Affiliation**: UCLA (PhD candidate) / Meta Superintelligence Labs (part-time internship)
- **Advisor**: Aditya Grover
- **Education**: B.A.Sc. Engineering Science (Machine Intelligence), University of Toronto
- **Awards**: Amazon Fellowship (2024)
- **Website**: https://siyan-zhao.github.io/
- **GitHub**: https://github.com/siyan-zhao
- **Prior work**: 3D perception and RL algorithms for autonomous driving agents (pre-PhD)

## Research Focus Areas

Siyan Zhao's research spans three interconnected areas:

### 1. Scaling (Diffusion) LLM Reasoning via RL
- **d1** (NeurIPS 2025 Spotlight, 3.2% acceptance rate) — Scaling reasoning in diffusion LLMs via reinforcement learning. First systematic exploration of how RL can enhance reasoning in non-autoregressive diffusion language models.
- **IGPO** (ICLR 2026) — Inpainting-Guided Policy Optimization for Diffusion Large Language Models. Uses inpainting to guide policy optimization, accepted alongside SPG.
- Probing the Decision Boundaries of In-context Learning in LLMs (NeurIPS 2024, Best Paper Runner-Up at MINT Workshop).

### 2. Efficient Preference Alignment & Personalization
- **GPO** — Group Preference Optimization (ICLR 2024). Few-shot alignment of LLMs.
- **PrefEval** (ICLR 2025, Oral Presentation, 1.8% acceptance rate) — Evaluating personalized preference following in LLMs. Do LLMs recognize your individual preferences?
- Invited talks on "Scaling Reasoning in Diffusion LLMs via RL" at ASAP seminar, HKU NLP Group, UCSD Hao AI Lab, NVIDIA, and Tesla AI (2025).

### 3. LLM Inference Efficiency & Modular RL Design
- **Prepacking** (AISTATS 2025) — A simple method for fast prefilling and increased throughput.
- **Decision Stacks** (NeurIPS 2023) — Flexible reinforcement learning via modular generative models.

## Key Contributions

### On-Policy Self-Distillation (OPSD) — ICML 2026

Lead author of OPSD, a post-training method where a single LLM serves as both student and teacher. The teacher has privileged access to ground-truth solutions and provides dense token-level supervision on the student's own on-policy trajectories. The technique achieves GRPO-level reasoning performance at ~1/64 the token cost (1 rollout vs 8, 1024 tokens vs 16k per problem).

**Key Innovation**: Self-distillation — a model rationalizes ground-truth solutions through its teacher policy (conditioned on privileged info) and distills that knowledge into its student policy (conditioned only on the problem). This avoids the need for a separate larger teacher model.

**Token Efficiency**: 4–12× more token-efficient than GRPO across mathematical reasoning benchmarks, tested on the Qwen3 model family.

See [[concepts/on-policy-self-distillation]] for the full method.

### d1 — Scaling Reasoning in Diffusion LLMs (NeurIPS 2025 Spotlight)

First work to systematically apply RL to enhance reasoning in diffusion-based LLMs. Accepted at NeurIPS 2025 as Spotlight (3.2% acceptance rate).

### IGPO — Inpainting-Guided Policy Optimization (ICLR 2026)

Novel approach using inpainting as a mechanism for policy optimization in diffusion language models.

## Publication Record

| Year | Venue | Paper | Role |
|------|-------|-------|------|
| 2026 | ICML | Self-Distilled Reasoner: On-Policy Self-Distillation (OPSD) | Lead Author |
| 2026 | ICLR | IGPO — Inpainting-Guided Policy Optimization for Diffusion LLMs | Co-Author |
| 2026 | ICLR | SPG | Co-Author |
| 2025 | NeurIPS (Spotlight) | d1: Scaling Reasoning in Diffusion LLMs via RL (3.2%) | Lead Author |
| 2025 | ICLR (Oral) | PrefEval — Personalized Preference Following (1.8%) | Lead/Co-Author |
| 2025 | AISTATS | Prepacking — Fast Prefilling in LLMs | Co-Author |
| 2024 | NeurIPS + MINT Workshop (Best Paper) | Probing Decision Boundaries of In-context Learning | Co-Author |
| 2024 | ICLR | Group Preference Optimization (GPO) | Co-Author |
| 2023 | NeurIPS | Decision Stacks: Flexible RL via Modular Generative Models | Co-Author |

## Related Pages

- [[concepts/on-policy-self-distillation]] — OPSD technique
- [[concepts/sdar-self-distilled-agentic-rl]] — SDAR: OPSD adapted for agent training
- [[concepts/on-policy-distillation]] — Broader OPD paradigm
- [[concepts/grpo-rl-training]] — GRPO, the baseline OPSD improves upon
- [[concepts/diffusion-llm]] — Diffusion-based LLMs, the focus of d1

## Sources

- [Siyan Zhao Homepage](https://siyan-zhao.github.io/) — Bio, publications, talks
- [OPSD Blog Post](https://siyan-zhao.github.io/blog/2026/opsd/) — Detailed technical overview
- [arXiv 2601.18734](https://arxiv.org/abs/2601.18734) — Self-Distilled Reasoner paper
- [OPSD GitHub](https://github.com/siyan-zhao/OPSD) — Training code and configs
