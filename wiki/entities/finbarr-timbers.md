---
title: "Finbarr Timbers"
tags: [person]
created: 2026-06-17
updated: 2026-06-17
type: entity
sources:
  - raw/articles/2026-06-16_interconnects_post-training-recipe-review.md
---

# Finbarr Timbers

## Overview

Finbarr Timbers is an AI researcher and post-training expert with experience at **DeepMind**, **Midjourney**, and the **Allen Institute for AI (Ai2)**. He is a leading voice on RLHF, reinforcement learning for LLMs, and open post-training recipes. He has appeared twice on [[entities/nathan-lambert|Nathan Lambert]]'s Interconnects podcast — first in December 2024 and again in June 2026.

## Key Contributions

### Post-Training Recipes

Timbers is a co-author on **Tülu 3** (Nov 2024) and **OLMo 3**, two of the most influential fully open post-training model families. These projects established the modern open recipe: SFT → DPO/RLVR → RL with verifiable rewards.

### OLMo 3

As part of the Ai2 team led by Nathan Lambert, Timbers contributed to the OLMo 3 family (7B and 32B models), including the first fully open 32B reasoning model.

## Post-Training Expertise

### MOPD (Multi-teacher On-Policy Distillation)

In 2026, Timbers discussed the emerging **MOPD** pattern — the dominant post-training recipe for frontier models. The approach:
1. Train N domain-specialist teachers (each trained with SFT then RL on relevant domains)
2. Train one general student by sampling its own trajectories
3. On each rollout, minimize reverse-KL divergence to the relevant teacher's output distribution

Lineage: Introduced by MiMo Flash v2, then scaled by DeepSeek V4 and Nemotron 3 Ultra to more than 10 teachers.

### RL Recipe Evolution

Timbers has tracked the evolution of post-training recipes from 2022 (InstructGPT's single SFT → RM → RL pipeline) through 2024 (open recipes with SFT → DPO → RLVR) and 2025 (DeepSeek R1's reasoning RL) to the 2026 fragmented multi-specialist approach.

## Selected Works

- **Tülu 3** (Nov 2024) — Fully open post-trained models beating Llama 3.1 Instruct
- **OLMo 3** (Dec 2025) — Open LLM family with first fully open 32B reasoning model
- **Interconnects Podcast #18** (Jun 2026) — Frontier post-training recipe review

## Links

- **X/Twitter**: @finbarrtimbers (or similar handle — referenced in Interconnects podcast)
- **Google Scholar**: Available via Ai2 publications
- **GitHub**: Associated with Ai2/OLMo repositories
