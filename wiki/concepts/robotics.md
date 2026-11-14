---
title: "Robotics (AI Robotics)"
type: concept
aliases:
  - robotics
  - ai-robotics
created: 2026-04-25
updated: 2026-11-15
tags:
  - concept
  - robotics
  - embodied-ai
  - humanoid-robot
  - physical-ai
sources:
  - wiki/concepts/vla-models.md
  - wiki/entities/figure-ai.md
  - wiki/entities/nvidia-cosmos-3.md
---

# Robotics (AI Robotics)

**Robotics** in this wiki means robots whose behavior is driven by learned models rather than hand-written control pipelines — the physical frontier of [[concepts/ai-agents]]. Since ~2024 the field has converged on a foundation-model recipe: pretrain a vision-language model on web-scale data, then post-train into a [[concepts/vla-models|vision-language-action (VLA)]] policy on robot trajectories, optionally bootstrapped with simulation and video generation.

## The Modern Stack

```
Internet video + VLM pretraining
        │
World models / video generation ──→ synthetic data & imagination (COSMOS, Genie, Sana-WM)
        │
VLA policy (RT-2 → π0 → Robostral Navigate → Gemini Robotics)
        │
Low-level control (RL, whole-body MPC) + fleet teleoperation data
```

| Layer | Representative work in this wiki |
|-------|----------------------------------|
| Foundation/world models | [[entities/nvidia-cosmos-3]] ([[concepts/physical-ai]]), [[concepts/jepa-world-models]], [[concepts/gemini/gemini-robotics-2]], [[concepts/lingbot-world-infinity]], [[concepts/flux-video-action-models]] |
| VLA policies | [[concepts/mistral-robostral-navigate]] (8B, single RGB camera, sim-only pretrain + online RL), Gemini Robotics, Figure Helix |
| Humanoids & platforms | [[entities/figure-ai]], Unitree, Tesla Optimus |
| Dexterous manipulation | [[entities/jim-fan]] (Stanford: tactile-reactive dexterity, TREX dataset), [[concepts/enpire]] |
| Infrastructure | [[entities/nvidia]] GR00T / Isaac, [[entities/aspire-nvidia]], [[entities/nvidia-sana-wm]] |

## Key Debates

1. **Real data vs simulation vs video.** End-to-end imitation from teleoperation is expensive; the field's "bitter lesson" bet ([[concepts/rich-suttons-bitter-lesson]]) is that simulation + video-pretrained world models scale further — Robostral Navigate's sim-only training is the strongest recent evidence.
2. **Monolithic VLA vs hierarchical.** Figure's Helix and Gemini Robotics 1.5/2 split a slow "System 2" reasoner from a fast visomotor "System 1" controller — the robotics mirror of [[concepts/system-one-models]] agent architectures.
3. **When does the ChatGPT moment arrive?** The recurring question (Jim Fan, Fei-Fei Li) of whether scaling internet video + trajectories yields a general manipulation policy, or whether contact physics keeps robotics fundamentally data-starved.

## Related Concepts

- [[concepts/embodied-ai]] — the parent research framing (agents with physical bodies)
- [[concepts/vla-models]] — the dominant model class
- [[concepts/physical-ai]] — NVIDIA's framing: world models + robots
- [[concepts/world-model-taxonomy]] — classification of world-model approaches
- [[concepts/multimodal]] — the VLM substrate VLAs inherit

## Sources

- Aggregated from wiki entity/concept pages: figure-ai, nvidia-cosmos-3, mistral-robostral-navigate, jim-fan, enpire, gemini-robotics-2, aspire-nvidia (2026)
