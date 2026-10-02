---
title: "Odyssey"
description: "Oliver Cameron and Jeff Hawke's world-model AI lab — general-purpose foundation world models (Odyssey-3, Agora-2 multi-agent, Starchild-1 multimodal, PROWL RL), $310M Series B with AWS as preferred cloud"
type: entity
created: 2026-09-26
updated: 2026-09-26
aliases:
  - odyx
  - Odyssey
  - odyssey.ml
  - odysseyml
tags:
  - entity
  - company
  - generative-ai
  - video-generation
  - world-models
  - timeline
sources:
  - https://odyssey.ml
  - https://odyssey.ml/about
  - https://odyssey.ml/our-series-b
  - https://odyssey.ml/introducing-agora-2
  - https://arxiv.org/abs/2605.18803
  - https://x.com/odysseyml
---

# Odyssey

**Odyssey** is an AI lab founded in **2023 by Oliver Cameron and Jeff Hawke** to build **general world models** — foundation models that learn and simulate the physical world (physics, dynamics, causality, human behavior) rather than only language. The company's origin thesis is directly inherited from autonomous driving: the founders previously built self-driving systems and concluded that world prediction was the transferable idea.

> *"More than a decade ago, Jeff, myself, and our founding team began working on one of the most ambitious problems in AI: teaching cars to navigate the world at superhuman performance... These systems demonstrated the immense power of world prediction as a path toward intelligence."* — Oliver Cameron, Series B announcement

Mission statement: **"We learn the world to make it better."** Target applications: robotics, autonomous driving, science, healthcare, education, gaming, defense, energy.

## Funding & Partnerships

- **Series B: $310M** — positioned as a bet that the field is approaching *"the GPT-3 moment for world models."* Natural Capital's Jay Zaveri called Odyssey **its largest investment to date**.
- **Investors**: GV (which has backed Odyssey since the beginning), Natural Capital, and others listed on the About page.
- **AWS is the preferred cloud provider**, with collaboration with **Amazon Annapurna Labs** to optimize world models on **Trainium** silicon. Amazon frames world models as *"one of the most demanding workloads in AI — massive compute throughput with tight latency constraints."*
- **Advisor/supporter roster** includes Jeff Dean (DeepMind), Soumith Chintala (Thinking Machines), Max Jaderberg (Isomorphic Labs), Tim Rocktäschel (Recursive).
- Team recruited from DeepMind, Waymo, and similar frontier groups; **CTO Jeff Hawke** presented the lab's research at RAAIS 2026.

## Model lineage

| Model | Type | Contribution |
|---|---|---|
| **Odyssey-2 Max** | Foundation world model | Materially advanced state-of-the-art in **physics accuracy** for general world simulation |
| **Starchild-1** | Real-time **multimodal** world model | First real-time world model learning beyond visual-only observation; technical report at starchild.odyssey.ml |
| **Odyssey-3** | Foundation world model | "General-purpose physical intelligence"; the lab's most powerful model to date on physical accuracy |
| **Agora-1 → Agora-2** | **Multi-agent** world model | Shared interactive simulation; Agora-2 supports up to **20 humans and agents**, 5× Agora-1, multiple environments, longer horizons |
| **PROWL-1** | RL + world models | RL-driven **adversarial** framework where an agent explores game environments *to improve the world model*; paper at arXiv:2605.18803 |

## Agora-2 architecture (learned game engine)

Agora-2 is the clearest public view of Odyssey's stack. It is described as **a learned game engine**: humans and agents share one generated environment, and each participant sees the consequences of everyone's actions from their own perspective.

```
participant actions
        │
        ▼
┌────────────────────────────┐
│ Simulation model           │  predicts how combined actions change
│ (entity properties, recent │  shared state; attention across entities
│  actions, surrounding geom)│  resolves interaction consequences
└────────────┬───────────────┘
             ▼
┌────────────────────────────┐
│ World server / shared state│  entity properties persist even when
│                            │  out of frame — no re-inference from pixels
└────────────┬───────────────┘
             ▼
┌────────────────────────────┐
│ Rendering model (per       │  flow matching on sequences with varying
│  participant, compressed   │  visual noise; visual history is often
│  visual representation)    │  dropped during training to force reliance
└────────────────────────────┘  on state; entity errors upweighted
```

Key design decisions:
- **Explicit shared state** rather than one video stream — a single-agent model (Odyssey-3) simulates one participant's experience; Agora maintains state accounting for all participants.
- **State-persistence over visual memory**: entities remain known while off-screen, avoiding reconstruction from each participant's visual history.
- **Flow matching** training with history dropout and entity-error upweighting.
- **RL-trained agents** that pursue opponents, route around obstacles, and recover when separated — learned from *partially observed* views.
- Trained on **Diablo II** (Blizzard) captures pairing observations with actions and state — games chosen as long-standing AI research environments.

A playable research preview runs at agora.odyssey.systems; a developer API exists at developer.odyssey.ml.

## Safety framing

Odyssey explicitly motivates multi-agent world models with **agent-safety evaluation**: citing reports of AI-powered cyberattacks and agent collusion (Anthropic threat-intelligence reporting; METR's Hugging Face incident investigation), it argues multi-agent simulations let harmful inter-agent behavior be studied in controlled environments before real systems are exposed. PROWL closes the loop the other way — agents improving the world model they train inside.

## Related

- [[concepts/world-models]] — Odyssey's core research program
- [[concepts/video-generation]] — streaming pixel generation as an interface paradigm
- [[concepts/reinforcement-learning]] — PROWL's adversarial exploration loop
- [[concepts/multi-agent-systems]] — Agora's shared-state motivation
- [[concepts/ai-safety]] — simulation-based evaluation of inter-agent risk
- [[entities/aws]] — preferred cloud + Trainium co-optimization partner

## Sources

- [odyssey.ml](https://odyssey.ml) and [About](https://odyssey.ml/about) (scraped 2026-09-26)
- [Our $310 Million Fundraise to Accelerate World Simulation](https://odyssey.ml/our-series-b)
- [Introducing Agora-2: Advancing Multi-Agent World Simulation](https://odyssey.ml/introducing-agora-2)
- [PROWL-1 paper](https://arxiv.org/abs/2605.18803) · [X @odysseyml](https://x.com/odysseyml)
