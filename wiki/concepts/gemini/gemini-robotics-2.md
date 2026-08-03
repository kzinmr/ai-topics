---
title: "Gemini Robotics 2"
type: concept
created: 2026-08-03
updated: 2026-08-03
tags:
  - concept
  - robotics
  - model
  - multimodal
  - google-deepmind
  - embodied-ai
sources:
  - raw/newsletters/2026-08-02-deepseek-s-flash-sale-google-s-gemini-finds-its-feet-and-music-copyright-bites-b.md
  - https://thesignal.substack.com/p/deepseeks-flash-sale-googles-gemini
---

# Gemini Robotics 2

**Gemini Robotics 2** is a family of three AI models released by [[entities/deepmind|Google DeepMind]] in August 2026 that lets robots control their entire bodies, handle delicate objects, and work together in teams. It is the second generation of the Gemini Robotics line (following the 2025 original documented in [[concepts/gemini/index]] and [[concepts/vla-models]]).

## Model Family

| Model | Role |
|-------|------|
| **Gemini Robotics 2** | Base model for whole-body robot control |
| **Gemini Robotics ER 2** | Extended-reasoning variant; plans tasks requiring hundreds of decisions over several minutes |
| **Gemini Robotics 2 (on-device)** | Deployable version for on-robot inference |

## Key Capabilities (per Google DeepMind, reported by The Signal Aug 2 2026)

- **Full humanoid control for the first time**: the model controls a complete humanoid body, so **Apptronik Apollo 2** can walk to a table, pick up a watering can, and place it on a shelf from a single spoken instruction.
- **Multi-finger dexterity**: multi-finger tasks succeed **between 32% and 92% of the time** on DeepMind's own testing.
- **Sample-efficient adaptation**: adapting to a new robot requires **fewer than 200 examples**.
- **Long-horizon planning**: the ER 2 variant plans tasks requiring **hundreds of decisions** spanning several minutes.

## Significance

Gemini Robotics 2 represents a step change from first-generation [[concepts/vla-models|VLA models]]: whole-body control (not just arm manipulation), dramatically lower adaptation data requirements, and extended-reasoning long-horizon planning. It competes in the embodied AI space alongside [[concepts/physical-ai|Physical AI]] efforts from Physical Intelligence (π0 line) and [[entities/figure-ai|Figure AI]] (Helix).

## Related Pages

- [[concepts/gemini/index]] — Gemini model family index
- [[concepts/vla-models]] — Vision-Language-Action model survey
- [[entities/deepmind]] — Developer organization
- [[concepts/physical-ai]] — Physical AI and robotics
- [[concepts/robotics]] — Robotics landscape
