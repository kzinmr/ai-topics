---
title: "Axiom Math"
type: entity
created: 2026-06-04
updated: 2026-06-04
tags:
  - entity
  - company
  - formal-methods
  - agent-safety
  - reinforcement-learning
sources:
  - path: raw/newsletters/2026-06-03-scaling-past-informal-ai-carina-hong-axiom-math.md
status: active
---

# Axiom Math

Axiom Math is a company developing **Verified Generation**, a methodology that uses formal proof checking (Lean proof assistant) as a reward signal for reinforcement learning training, departing from traditional GRPO/RLHF approaches.

## Leadership

- **Carina Hong** (CEO) — interviewed on Latent Space AI for Science podcast (June 2026)

## Core Technology

**Verified Generation** uses the Lean proof assistant as a deterministic reward signal for RL training:

| Traditional RLHF | Verified Generation |
|-----------------|-------------------|
| Learned preference model as reward | Lean proof checker as reward |
| Statistical — susceptible to reward hacking | Deterministic — only valid proofs accepted |
| Requires human preference data | Uses mathematical correctness as signal |

### Key Theses

1. **Code ability is necessary but insufficient for AGI** — formal verification bridges the gap between code generation and mathematical certainty
2. **Scaling through compounding** — verified proofs become building blocks for more complex proofs, creating compounding returns
3. **Ramanujan analogy** — discovery without proof is incomplete; the Hardy→Ramanujan feedback loop mirrors the AI→proof-checker relationship

## Relation to Other Approaches

- **AlphaProof (Google DeepMind)**: theorem proving search using Lean (post-hoc verification)
- **DeepSeek-Prover-V2**: automated Lean proof generation
- **Vericoding**: using LLMs to generate formally verified code
- **Axiom Math**: uses proof checking *as the RL training signal itself*

## Relevance

Connects to [[concepts/formal-verification-llm-agents]] (formally verified code for LLM agents) and [[concepts/security-and-governance/ai-safety]] (deterministic vs statistical alignment guarantees).
