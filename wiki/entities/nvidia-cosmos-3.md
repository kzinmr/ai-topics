---
title: "NVIDIA Cosmos 3"
created: 2026-06-10
updated: 2026-06-10
type: entity
tags: [product, nvidia, video-generation, world-models, physical-ai, robotics, embodied-ai, multimodal, simulation, generative-ai, model, gtc]
sources:
  - raw/articles/2026-06-10_nvidia_cosmos-3-platform.md
  - https://developer.nvidia.com/blog/?tag=cosmos
---

# NVIDIA Cosmos 3

**NVIDIA Cosmos 3** is [[entities/nvidia|NVIDIA]]'s unified physical AI platform, announced at [[concepts/gtc|GTC Taipei 2026]] (June 2026). It unifies three previously separate capability domains — video generation, world models, and robot policy — into a single foundation model platform for physical AI development.

Cosmos 3 represents a convergence point where generative AI meets robotics and embodied systems, enabling developers to use the same model family for simulation, planning, and control.

## Unified Capability Domains

### 1. Video Generation
Cosmos 3 generates photorealistic synthetic video data for training perception systems. Unlike general-purpose video generators, Cosmos videos are physics-aware and can serve as training data for downstream robotics models.

### 2. World Models
The platform learns internal representations of physical dynamics — how objects move, interact, and respond to forces. These [[concepts/world-models|world models]] enable:
- Physics-grounded simulation for robotics training
- Counterfactual reasoning ("what would happen if...")
- Long-horizon planning in physical environments

### 3. Robot Policy
Cosmos 3 can directly output robot control policies — the sequence of actions a robot should take to accomplish a task. By sharing representations with the video and world model components, policy learning benefits from the rich physical understanding embedded in the model.

## Architecture

| Component | Function | Output |
|-----------|----------|--------|
| **Video backbone** | Physics-aware video generation | Synthetic training data |
| **World model** | Internal physical dynamics representation | State predictions, counterfactuals |
| **Policy head** | Action sequence generation | Robot control commands |

The key architectural innovation is the **shared representation** across all three domains — a single model learns physical understanding that transfers between generation, prediction, and control tasks.

## Ecosystem and Predecessors

Cosmos 3 builds on NVIDIA's earlier physical AI work:
- **Cosmos 1** (2024): Initial world model research
- **Cosmos 2** (2025): Expanded to multi-modal physical reasoning
- **Isaac Sim**: NVIDIA's robotics simulation platform, complementary to Cosmos
- **Omniverse**: Digital twin platform that can feed Cosmos with 3D scene data

## Industry Significance

Cosmos 3 enters a competitive landscape for physical AI foundation models:

| Platform | Focus | Approach |
|----------|-------|----------|
| **NVIDIA Cosmos 3** | Unified (video + world + policy) | Single foundation model |
| [[concepts/gemini-robotics|Google Gemini Robotics]] | Robot control | Vision-language-action model |
| [[concepts/robotics-foundation-models|Robotics Foundation Models]] | Various | Domain-specific models |
| Tesla Optimus | Humanoid robot | Proprietary stack |

NVIDIA's competitive advantage is its GPU hardware ecosystem — Cosmos models are optimized for NVIDIA hardware and integrate with the Omniverse digital twin platform.

## Related Pages
- [[entities/nvidia]] — NVIDIA corporate entity
- [[concepts/world-models]] — World model concept in AI
- [[concepts/physical-ai]] — Physical AI and embodied intelligence
- [[concepts/robotics]] — Robotics in AI
- [[concepts/video-generation]] — AI video generation landscape
- [[concepts/simulation]] — Simulation for AI training
- [[concepts/embodied-ai]] — Embodied AI systems

## Sources
- [NVIDIA Cosmos blog tag page](https://developer.nvidia.com/blog/?tag=cosmos)
- [GTC Taipei 2026 announcements](https://www.nvidia.com/gtc/)
- X/Twitter: NVIDIA Cosmos 3 announcement coverage (June 2026, 42 bookmarks, 12K impressions)
