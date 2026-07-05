---
title: "Test-Time Interaction Scaling"
created: 2026-06-12
updated: 2026-06-12
type: concept
tags:
  - concept
  - test-time-scaling
  - ai-agents
  - reinforcement-learning
  - reasoning
  - agentic-rl
  - inference
sources:
  - raw/articles/2026-06-01_sheriyuo_rl-for-test-time-scaling.md
  - https://arxiv.org/abs/2503.07572
related:
  - test-time-scaling
  - training-free-rl
  - reinforcement-learning
  - reasoning
  - chain-of-thought
---

# Test-Time Interaction Scaling

**Test-Time Interaction Scaling (TTI)** is the principle that for **agentic tasks**, the right axis for test-time scaling is the **number of environment interactions**, not the length of internal reasoning (thought tokens). Once the environment itself returns information, the marginal return of stacking internal monologue tokens decays fast.

> Proposed in "Thinking vs. Doing: Agents that Reason by Scaling Test-Time Interactions" (NeurIPS'25 Best Paper). Synthesized from Xiuyu Li's analysis.

## Core Argument

The paper makes an argument that challenges the dominant test-time scaling paradigm: **in agentic tasks, thinking more does not help, doing more does.**

This is a fundamental distinction from reasoning tasks (math, code) where extended CoT reliably improves accuracy. In agent settings, the environment provides real-time feedback that internal reasoning cannot substitute:

| Setting | Optimal TTS Axis | Why |
|---------|-------------------|-----|
| Math/Code reasoning | Thought tokens (CoT length) | All information is in the problem statement |
| Agentic tasks | Interaction count | Environment returns new information each step |
| Hybrid (tool-use agents) | Both, separately | Reasoning and tool-use budgets are independent |

## TTI Method

TTI uses a **curriculum-online RL** setup:

1. Start with short rollout horizons (h)
2. Gradually increase h during training
3. The model learns to adaptively decide: "explore one more step or wrap up"

This produces a model that **dynamically allocates** its interaction budget based on task difficulty — rather than using a fixed number of steps.

## Connection to Agentic RL Decoupling

TTI supports the argument from "Agentic RL: Decoupling Reasoning and Tool-use":

> The token budget for reasoning and the step budget for tool-use are two different things, and must be scaled and trained separately.

This means agentic test-time scaling has **two independent axes**:

```
Performance = f(reasoning_tokens, interaction_steps)

Optimal allocation:
  - Easy tasks: few reasoning tokens + few interactions
  - Hard reasoning: many reasoning tokens + few interactions
  - Hard exploration: few reasoning tokens + many interactions
  - Very hard: many of both (but diminishing returns)
```

## Implications

1. **Agent benchmarks should track interaction count** as a first-class metric alongside token count
2. **Agent training should use curriculum over rollout horizons** — not just longer CoT
3. **Scaffolding design**: Separate the reasoning budget from the tool-use budget in agent systems
4. **Evaluation**: Compare agents at equal interaction counts, not just equal token budgets

## Related Concepts

- [[concepts/test-time-scaling]] — The broader TTS landscape (CoT, self-consistency, beam search)
- [[training-free-rl]] — Training-free approaches to TTS
- [[reinforcement-learning]] — RL fundamentals for agent training
- [[concepts/chain-of-thought]] — The "thinking" axis that TTI complements
- [[reasoning]] — AI reasoning capabilities and benchmarks
