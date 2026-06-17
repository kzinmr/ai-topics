---
title: "Frontier post-training recipe review with Finbarr Timbers"
source: "Interconnects (Nathan Lambert)"
date: 2026-06-16
url: "https://open.substack.com/pub/robotic/p/frontier-post-training-recipe-review"
type: article
---

Podcast interview (#18) with Finbarr Timbers on the history of post-training recipes from InstructGPT (2022) to 2026 frontier models.

Key timeline of post-training recipes:
- 2022-2023 (InstructGPT): One pipeline — SFT → reward model → RL
- 2024 (Llama 3, Tülu 3): Open recipes formalize SFT → DPO → RL with verifiable rewards
- 2025 (DeepSeek R1): Reasoning RL (R1) makes large-scale RL the centerpiece
- 2026 (MiMo Flash V2): Recipes fragment into many specialist models merged back into one

Multi-teacher On-Policy Distillation (MOPD) is the key pattern emerging in 2026:
- Train N domain-specialist teachers (each: SFT, then RL on relevant domains)
- Train one general student by sampling its own trajectories
- On each rollout, minimize reverse-KL to the relevant teacher's output distribution
- Lineage: MiMo Flash v2 introduced it → DeepSeek V4 & Nemotron 3 Ultra scale it to >10 teachers

Finbarr Timbers background: ex-DeepMind, Midjourney, Ai2. Previously interviewed in Dec 2024.

Model recipes covered: MiMo Flash, DeepSeek V4, GLM 5, Kimi K2.6, Nemotron 3 Ultra
