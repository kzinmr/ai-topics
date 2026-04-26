---
title: "The Causal Backbone Conjecture"
created: 2026-04-18
updated: 2026-04-18
type: concept
tags:
  - agent-architecture
  - selection-theorem
  - resource-allocation
  - information-theory
  - causal-reasoning
sources:
  - https://www.lesswrong.com/posts/BcrPdMipzqecg4JdQ/the-causal-backbone-conjecture
  - raw/articles/tailcalled-causal-backbone-conjecture-2024.md
---

# The Causal Backbone Conjecture

**Author:** tailcalled (LessWrong)  
**Date:** 2024-08-17  
**Type:** Selection theorem for agent-like structures under resource constraints

## Core Thesis

> "For events where there are causes which point in contradictory directions, the cause with more resources tends to win out."

The conjecture proposes that **agent-like structures emerge naturally from resource constraints**, not from the need to model "a sufficiently rich set of tasks." In environments with finite resources (compute, energy, capital, attention), the causal structure of influence follows a **long-tailed distribution** — a small subset of entities dominate the pathways that actually matter.

## Key Arguments

### 1. Against Exhaustive World Modeling

The conjecture directly challenges assumptions like those in *The Gooder Regulator Theorem*, which claims agents must model systems to handle diverse tasks. tailcalled argues this leads to **information overload** — attempting to model everything causes computational collapse.

> "The vast majority of the complexity that has sprung up around the resources has ~no influence on their distribution or long-term development."

### 2. The Universal Causal Backbone

The universe has a **"universal backbone"** of causal dynamics that really matter:
- **Dominant resource flows** — mass, energy, capital, compute
- **Entities that can redirect those flows** — major corporations, key individuals, planetary systems
- **Pathways of influence** — the mechanisms by which resources move and concentrate

Survival requires modeling only the backbone segments directly relevant to the agent, not the entire environment.

### 3. Resource Distribution Shifts

Periodic, massive redistributions of resources occur. Entities anchored to outdated distributions without adaptive capacity face **extinction or severe marginalization**. This creates evolutionary pressure for agents to:
- Continuously track macro-level resource reallocations
- Update internal models to new backbone configurations
- Maintain flexibility to shift causal models as distributions change

### 4. Interconnected Modeling Incentive

Because all agents track the backbone, its components become tightly coupled. This creates systemic pressure to model the **"top" of the backbone** (highest-leverage dynamics/entities) rather than isolated local branches.

## Implications for AI Agent Design

| Principle | Traditional Approach | Causal Backbone Approach |
|-----------|---------------------|-------------------------|
| **Modeling Scope** | Exhaustive world simulation | Sparse, high-leverage node tracking |
| **Resource Allocation** | Fixed compute budget | Dynamic, backbone-weighted filtering |
| **Adaptation** | Retraining on new data | Monitoring distribution shifts |
| **Architecture** | Monolithic model | Modular, backbone-segment specialists |
| **Failure Mode** | Information overload | Missing backbone shifts |

## Relationship to Other Concepts

- ****: Proposes resource constraints as the driving force for agent-like structure emergence, contrasting with task-richness theories
- **[[world-models-science]]**: Argues against exhaustive world modeling in favor of sparse, strategically-relevant modeling
- ****: Suggests designs should prioritize identifying and tracking high-resource, high-influence nodes
- ****: Natural filtering mechanism — only backbone-relevant information passes through
- **[[karpathy-loop]]**: The loop implicitly operates on causal backbones — which experiments to run is determined by resource-weighted hypotheses

## Open Questions

1. How do agents discover the causal backbone without prior knowledge?
2. What is the minimum modeling fidelity required for backbone segments?
3. How do backbone configurations change during technological paradigm shifts (e.g., AI compute scaling)?
4. Is there a formal metric for "backbone leverage" — how much influence per unit of modeling effort?

## Sources

- [The Causal Backbone Conjecture](https://www.lesswrong.com/posts/BcrPdMipzqecg4JdQ/the-causal-backbone-conjecture) by tailcalled, LessWrong (2024-08-17)
- Related: [Rationalists are missing a core piece for agent-like structure](https://www.lesswrong.com/posts/tailcalled-previous-post)
- Related: [Fixing The Good Regulator Theorem](https://www.lesswrong.com/posts/fixing-good-regulator)
