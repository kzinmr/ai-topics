---
title: "Functional Taxonomy of World Models"
type: concept
created: 2026-06-09
updated: 2026-06-09
tags:
  - world-models
  - spatial-intelligence
  - taxonomy
  - reinforcement-learning
  - robotics
  - simulation
  - generative-ai
sources:
  - raw/articles/2026-06-03_fei-fei-li_x_article_world-model-taxonomy.md
  - https://x.com/drfeifei/status/2062247238143996275
---

# Functional Taxonomy of World Models

A framework proposed by [[entities/fei-fei-li|Fei-Fei Li]] and the [[world-labs|World Labs]] team that classifies "world models" into three functional categories based on what they output from the agent-environment interaction loop: **renderers**, **simulators**, and **planners**.

## The POMDP Loop

The taxonomy is grounded in the classical reinforcement learning framework (Sutton & Barto): the **partially observable Markov decision process** (POMDP). An agent takes **actions** that affect the **state** of the world. The agent never sees state directly — it receives **observations** (photons, sensor readings, pixels). New observations inform new actions, and the loop continues.

The term "world model" traces to Kenneth Craik's 1943 proposal that minds reason by running "small-scale models" of reality. Different things now called "world models" are in fact different projections of this same loop — each outputs a different piece of it.

## Three Functional Categories

### 1. Renderer (Observations → Pixels)

- **Outputs**: Observations in the form of pixels for human eyes
- **Quality metric**: Visual fidelity
- **Examples**: Text-to-video models, Google Genie 3, World Labs RTFM
- **Limitation**: No explicit understanding of 3D structure; produces what a viewer *would see*, not what *is*
- **Maturity**: Most commercially mature category

### 2. Simulator (State → Geometry/Physics/Dynamics)

- **Outputs**: Geometrically, physically, or dynamically faithful representations of world state
- **Quality metric**: Structural accuracy — geometry that holds up under inspection, physics that respects Newton's laws
- **Serves two consumers**:
  - Human professionals (architects, designers, filmmakers, game developers)
  - Computer programs (RL agents, robot controllers, autonomous vehicles)
- **Why it's the linchpin**: Bridge between renderers and planners; the structural backbone from which both visual appearance and action consequences can be derived
- **Commercial surface area**: NVIDIA Omniverse targets >$1T addressable market in factories, warehouses, supply chains, digital twins

### 3. Planner (Observations → Actions)

- **Outputs**: Actions — what the agent should do next given an observation and a goal
- **Quality metric**: Task success, safety, efficiency
- **Inverse of the renderer**: Takes observations as input, produces actions as output (closing the perception-action loop)
- **Examples**: Vision-Language-Action (VLA) models, model-based systems, World Action Models
- **Maturity**: Most nascent; robotics demos impressive but confined to constrained lab setups

## Key Insight: Convergence

The three categories are not fundamentally separate. The same underlying knowledge — geometry, physics, dynamics — sits beneath all of them. A model that can render a cup from any angle ought to simulate what happens when the cup is pushed and plan a hand to pick it up. The three categories are **three projections of a single underlying understanding**.

Recent work demonstrates convergence:
- Pretrained video renderers used as backbone for joint world-and-action prediction
- World Labs' Marble outputs Gaussian splats + collision meshes from a single model (renderer ↔ simulator boundary dissolving)
- Renderers becoming action-conditioned, simulators becoming more controllable, planners deliberating rather than reacting

## The Logical Endpoint: Unified World Model

One foundation model that can:
1. Render photorealistic views
2. Produce physically accurate structure
3. Plan action sequences

...switching between output modalities depending on what the downstream consumer needs.

## Open Problems

| Challenge | Description |
|-----------|-------------|
| **Data scarcity** | Renderers awash in internet video; simulators/planners face acute shortages of 3D assets and robot demonstrations |
| **Beauty vs. precision** | Optimizing for visual beauty can sacrifice the precision a robot or simulation needs |
| **Sim-to-real gap** | Difference between simulation behavior and real-world behavior persists |
| **Generative geometry risks** | AI-generated geometry can look correct but contain self-intersections or wrong scale producing nonsensical physics |
| **Multi-physics at scale** | Rigid bodies + deformable objects + fluids + cloth interacting is orders of magnitude more expensive than single-domain simulation |

## Comparison with Existing World Model Concepts

| Dimension | This Taxonomy | [[world-models-for-agents\|ECHO / Agent World Models]] | [[world-models-science\|Scientific World Models]] |
|-----------|---------------|------|------|
| **Scope** | Physical/spatial world | Terminal/software environments | Scientific domains |
| **Agent type** | Robots, embodied systems | CLI/browser agents | Research agents |
| **"World" means** | 3D space, physics, dynamics | Terminal output, tool responses | Biological/physical systems |
| **Key output** | Pixels, state, actions | Next-token predictions | Hypotheses, experiments |

## Related Concepts

- [[world-models-for-agents]] — World models for software agents (ECHO, VAGEN)
- [[world-models-science]] — World models for scientific discovery
- [[entities/fei-fei-li]] — Author; CEO of World Labs
- [[world-labs]] — Company building spatial intelligence and Marble

## See Also

- [[entities/fei-fei-li]] — Author and proposer of the taxonomy
- [[world-labs]] — World Labs, building Marble (first renderer+simulator product)
- [[world-models-for-agents]] — Complementary perspective: world models in software agent training
