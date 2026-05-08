---
title: "Noumena Network"
created: 2026-05-08
updated: 2026-05-08
type: entity
tags: [company, lab, moe, training, infrastructure, agents, open-source]
sources: [raw/articles/2026-03-14_noumena-research-12-posts.md]
---

# Noumena Network

**Noumena Network** is an AI research lab and product company building expert-grade AI systems. Their motto: "AI Engineered for mastery."

## Overview

Noumena is built on the belief that expert work requires intelligence designed for it — not generic AI that optimizes for plausibility. They target **ASI** (Artificial Superintelligence), not AGI, and view each generation of their system as building the next.

**Tagline:** "Intelligence held to the same standard as the work it serves."

## Philosophy

- **ASI, Not AGI** — Aiming for superintelligence, not just general intelligence
- **Built to Think, Not to Guess** — Precision over plausibility
- **Evolves in Real Use** — Each interaction teaches the system
- **Feedback Teaches, Not Flattens** — Expert judgment refines capability
- **Respects Expertise** — Systems that improve with, not despite, expert input

## Two Major Workstreams

### 1. nmoe — MoE Training Infrastructure

**nmoe** is Noumena's open-source Mixture-of-Experts trainer for NVIDIA Blackwell B200 (`sm_100a`). It's intentionally narrow and opinionated:

- **RDEP** (Research Dispatch/Expert Parallelism): Direct dispatch/return via CUDA IPC instead of NCCL all-to-all
- **B200-first**: Optimized for Blackwell architecture with FP8 native support
- **No tensor parallel**: Deliberate design choice
- **Speedrun methodology**: Small-model rapid-turnaround experiments as research instruments
- Configs: Moonlet (1-GPU research), Moonlight (8-GPU RDEP), Speedrun suite
- GitHub: [Noumena-Network/nmoe](https://github.com/Noumena-Network/nmoe) (384 stars)

### 2. Agent Systems — "Skill is All You Need"

Noumena built an AI-native Growth Intelligence system for marketing, applying lessons from their MoE research to agent architecture:

- **File-system-as-memory**: Directory structures storing expert knowledge, inspired by Cursor's `.mdc` files
- **Cognitive Layering**: Atomic Skills (stable execution) + Thinkflows (runtime path selection)
- **Skill DevOps**: Two specialized agents (Skill Builder, Skill Evolver) that enable domain experts to build skills without coding
- **File-based RL loop**: Experts as reward models, Builder/Evolver as policy optimizers
- Blog: [Skill is All You Need](https://huggingface.co/blog/Noumena-AI/skill-is-all-you-need-lessons-from-building-market) (Dec 2025)

## Research Program

Noumena published 12 research posts on March 14, 2026, covering their MoE training methodology. Key themes:

| Theme | Posts |
|-------|-------|
| **Speedrun Methodology** | The Speedrun Loop, Let the Speedrun Search Itself |
| **MoE Training Dynamics** | Why Training MoEs is So Hard, Super-4096, Do MoE Experts Need Different Learning Rates? |
| **Measurement & Metrics** | Make It Measurable, The Atlas Hypothesis, What Are We Holding Fixed? |
| **Systems** | RDEP, What We Built, NVFP4 Dynamics |
| **Reproducibility** | Reproducing Canon, mHC, and Engram |

See [[concepts/moe-training-noumena-methodology]] for full synthesis.

## Roadmap

- **Spring '26**: Platform — API, console, lab, training, docs
- **Fall '26**: Research Lab — Research and product in one loop
- **Winter '26**: Next Generation Model — Designed and built by the previous generation

## Related Pages

- [[concepts/moe-training-noumena-methodology]] — Full methodology synthesis
- [[concepts/rdep]] — Research Dispatch/Expert Parallelism
- [[concepts/mixture-of-experts]] — General MoE concept
- [[entities/deepseek]] — DeepSeek (major MoE practitioner)
