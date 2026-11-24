---
title: "Scaffold vs RL Debate"
type: concept
created: 2026-04-25
updated: 2026-11-23
tags:
  - concept
  - agentic-rl
  - harness-engineering
  - agent-harness
  - test-time-scaling
  - reinforcement-learning
  - post-training
  - ai-agents
aliases:
  - scaffold-vs-rl-debate
  - scaffolding-vs-rl
  - scaffold-or-rl
sources:
  - raw/articles/2026-07-04_lilianweng-harness-engineering-self-improvement.md
  - https://lilianweng.github.io/posts/2026-07-04-harness/
related:
  - "[[concepts/agentic-scaffolding]]"
  - "[[concepts/harness-engineering]]"
  - "[[concepts/just-large-models]]"
  - "[[concepts/test-time-compute]]"
  - "[[concepts/post-training/rlvr]]"
---

# Scaffold vs RL Debate

The **scaffold vs RL debate** is the central strategic disagreement about how to get the most capability out of a language model on agentic, long-horizon tasks: improve the **harness/scaffold** around a frozen model (tools, prompts, control flow, verification, search), or bake the capability **into the weights** via reinforcement learning (RLVR, agentic RL, process-reward training).

It is the applied form of the broader [[concepts/just-large-models|bitter-lesson]] tension: do you *compensate* for what the model cannot do with engineering scaffolding, or do you *elicit* it by training the model to do it natively?

## The Two Positions

| Dimension | Scaffold camp | RL camp |
|-----------|---------------|---------|
| **Locus of improvement** | Outer loop (harness, tools, prompts, orchestration) | Inner loop (weights, reward, training data) |
| **What changes** | The system around a frozen model | The model itself |
| **Iteration speed** | Hours — edit a prompt/tool, re-run eval | Weeks — collect rollouts, run RL, retrain |
| **Cost profile** | Recurring inference/token cost ("harness tax") | Upfront training cost, cheaper inference later |
| **Transferability** | Brittle — scaffold tuned for one model breaks on the next | Generalizes across tasks once learned |
| **Verifiability** | Explicit — every step is inspectable/gated | Opaque — capability lives in weights, hard to audit |
| **Failure mode** | Scaffold overfits the eval; capability evaporates on model swap | Reward hacking; capability only on trained task distribution |

## The Scaffold Argument

Scaffolding is the structure that turns a raw text-completion engine into a working agent. As [[concepts/agentic-scaffolding|agentic scaffolding]] documents, this includes tool routing, plan-then-execute flow, verification gates, and human-in-the-loop checkpoints. Proponents argue:

- **Verifiability over trust.** Scaffolding makes agent behavior *inspectable and verifiable* rather than hoping the weights behave. Capability elicitation through a harness is auditable; RL-trained capability is not.
- **Speed of iteration.** When frontier models ship every few weeks, a scaffold tuned to model N is obsolete the moment model N+1 lands — but a *general* harness pattern (subagents, context compaction, verification loops) compounds across model generations.
- **No training access needed.** Frontier models are accessed via API. Scaffolding is the only lever available to most teams.

The counter-argument, the **harness tax**: scaffolding is a *depreciating asset*. Every reasoning-model release absorbs part of the scaffold's job (a model that plans natively needs less plan-then-execute prompt engineering; a model with built-in tool-use needs less orchestration glue). This is the [[concepts/just-large-models|scale-first]] prediction.

## The RL Argument

RL proponents (e.g. the agentic-RL / RLVR line of work) argue that scaffolding is a **crutch that masks a missing capability** and should eventually be trained away:

- **Internalized competence beats external crutches.** A model trained with RL on tool-use trajectories, code execution with verifiable rewards (RLVR), or multi-step reasoning (GRPO/PPO on pass/fail signals) needs no prompt scaffolding to plan or verify — it *is* the planner/verifier.
- **Scaffolding hits a ceiling.** Search, branching, and self-correction bolted onto a frozen model cannot exceed the model's intrinsic discrimination. If the base model cannot tell a good solution from a bad one, no amount of best-of-N sampling helps. RL raises that intrinsic floor.
- **Compounding on the right axis.** Scaffolding improvements don't survive model swaps; RL improvements move the Pareto frontier permanently.

The counter-argument: RL is **slow, expensive, and reward-hackable**. Designing a reward that doesn't get gamed is hard, and capability learned on a narrow task distribution collapses off-distribution.

## Resolution: A Spectrum, Not a Binary

The debate has largely resolved into a **layered view** rather than a winner:

1. **Reasoning-internal tasks** (math, logic) → RL wins. Train it in (see [[concepts/test-time-compute]], [[concepts/chain-of-thought]]).
2. **Environment-interaction tasks** (tool use, navigation) → both. RL trains the tool-use prior; the harness exposes the tools and gates the side effects.
3. **Long-horizon / organizational tasks** (multi-file coding, research) → harness wins near-term because rewards are too sparse/delayed to train effectively.
4. **The frontier (2026)**: *self-improving* systems blur the line — the harness runs an RL-like loop against a verifiable signal, or rewrites its own scaffold. See [[concepts/recursive-self-improvement]] and [[concepts/self-evolving-agents]].

The pragmatic practitioner's rule: **scaffold first to discover what capability is actually missing, then RL only the capabilities that recur across enough tasks to justify the training cost.** Scaffolding is the cheap probe; RL is the expensive consolidation.

## Graph Structure Query

```
[scaffold-vs-rl-debate] ──extends──→ [concepts: harness-engineering]
[scaffold-vs-rl-debate] ──contrasts──→ [concepts: just-large-models]   (elicit vs compensate)
[scaffold-vs-rl-debate] ──relates-to──→ [concepts: agentic-scaffolding]
[scaffold-vs-rl-debate] ──relates-to──→ [concepts: test-time-compute]
[scaffold-vs-rl-debate] ──relates-to──→ [concepts: post-training/rlvr]
[scaffold-vs-rl-debate] ──embodies──→ [concept: bitter-lesson (rich-suttons)]
[scaffold-vs-rl-debate] ──follows──→ [concepts: recursive-self-improvement]  (frontier resolution)
```

> Frames the elicitation-vs-compensation axis that runs through [[concepts/just-large-models]], operationalized for agentic systems via [[concepts/harness-engineering]] and [[concepts/agentic-scaffolding]].

## Related Concepts

- [[concepts/agentic-scaffolding]] — the scaffold side, in concrete layers
- [[concepts/harness-engineering]] — umbrella: "Agent = Model + Harness"
- [[concepts/just-large-models]] — the scale-first/elicit thesis (depreciating scaffold)
- [[concepts/test-time-compute]] — scaffolding's cheapest weapon (search, best-of-N)
- [[concepts/post-training/rlvr]] — RL with verifiable rewards (the RL side)
- [[concepts/recursive-self-improvement]] — where the line dissolves
- [[entities/andrej-karpathy]] — articulates elicitation-vs-compensation framing

## Sources

- Lilian Weng, "Agent Harness / self-improvement" (2026-07-04) — https://lilianweng.github.io/posts/2026-07-04-harness/
- Internal framing across [[concepts/just-large-models]] and [[concepts/agentic-scaffolding]]
