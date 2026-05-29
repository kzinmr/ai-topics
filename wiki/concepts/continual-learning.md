---
title: "Continual Learning — Continuous Improvement in AI Systems"
type: concept
aliases:
  - continual-learning
  - lifelong-learning-ai
  - incremental-learning
created: 2026-04-27
updated: 2026-05-29
tags:
  - concept
  - ai-agents
  - model
  - training
status: complete
description: "Continual learning for AI agents and models — a framework across three layers: model, harness, and context."
---

# Continual Learning

## Three-Layer Learning Framework

AI agents can learn continuously across three layers (@hwchase17, 2026-04-24):

### 1. Model Layer
Updates the model weights themselves. Uses methods such as SFT (Supervised Fine-Tuning) and RL (Reinforcement Learning / GRPO).

**Central Challenge: Catastrophic Forgetting**
When the model is updated with new data or tasks, previously learned knowledge degrades. This is an open research problem.

**Example:** OpenAI's Codex model is trained specifically for the Codex agent. Theoretically, each user could have their own LoRA, but in practice most learning happens at the agent level.

### 2. Harness Layer
The code driving the agent, along with the instructions and tools always included in the harness.

**Meta-Harness: End-to-End Optimization of Model Harnesses**
While the agent runs in a loop: execute tasks → evaluate → save logs to the filesystem → analyze traces with a code agent and propose changes to the harness code.

Theoretically, different code harnesses could be learned per user, but in practice most of this happens at the agent level.

### 3. Context Layer
Configuration information (instructions, skills, tools) located outside the harness. Commonly referred to as "memory".

Similar types of context also exist within the harness (base system prompts, skills). The distinction is whether it is part of the harness or part of the configuration.

**Update Levels:**
- **Agent level** — The agent has persistent "memory" and updates its own configuration over time (e.g., OpenClaw's SOUL.md)
- **Tenant level** — Each tenant (user, organization, team) has its own context (e.g., Hex's Context Studio, Decagon's Duet, Sierra's Explorer)
- **Hybrid** — Can combine agent-level, user-level, and organization-level context updates

**Update Methods:**
- **Offline batch processing** — Runs recent traces to extract insights and update context (equivalent to OpenClaw's "dreaming")
- **Hot path execution** — The agent updates its own memory while working on core tasks (or the user instructs it via prompts)

**Another dimension:** Explicit vs. implicit updates. Whether the user prompts the agent to remember, or the agent remembers based on the harness's own core instructions.

## Continual Learning in Classical ML

Attempts at continual learning in classical ML literature:

- Self-distillation
- Real-time RL
- Memory scaffolds
- Replay methods
- Regularization
- Gradient projections
- KL penalties
- On-policy data
- Countless others

Many of these have been criticized as "not even trying to solve the right problem" (@carnot_cyclist, 2026-04-24):

> "We are not short of attempts at achieving continual learning — self-distillation, real-time RL, memory scaffolds, replay methods, regularization, gradient projections, KL penalties, on-policy data, and countless more. My complaint with a lot of these is that they are not even trying to solve the right problem."

 Attempts a principled and ambitious definition — rooted in both classical ML literature and discourse.

## References

- [Continual learning for AI agents](../raw/articles/2040467997022884194_continual-learning-for-ai-agents.md) (2026-04-24, @hwchase17) — 3-layer learning framework
- [Defining Continual Learning](../raw/articles/2041479655035679163_defining-continual-learning.md) (2026-04-24, @carnot_cyclist) — Principled definition of continual learning
- [Improving Composer through Real-Time RL](../raw/articles/2026-04_cursor_real-time-rl-for-composer.md) (2026-04, Cursor) — Production real-time RL for coding agents
- [Continual Learning with Prime Intellect: part 1](../raw/articles/2026-04-06_27upon2_continual-learning-prime-intellect.md) (2026-04-06, @27upon2) — Open-source continual learning CLI

## Real-World Implementations

### Cursor Real-Time RL (2026)

[[entities/cursor-ai|Cursor]] applies real-time RL to continuously improve Composer, their coding agent — shipping new checkpoints every ~5 hours using reward signals from real user interactions. This is a production-grade implementation of model-layer continual learning.

See: [[concepts/real-time-rl]], [cursor.com/blog/real-time-rl-for-composer](https://cursor.com/blog/real-time-rl-for-composer)

### Rollouts — Open-Source Continual Learning (2026)

[[entities/sriraam-27upon2|Sriraam (@27upon2)]] built **[rollouts](https://github.com/13point5/rollouts)** — an open-source CLI implementing Cursor-inspired continual learning for coding agents using [[entities/prime-intellect|Prime Intellect]]'s hosted training, [[entities/opencode|OpenCode]], and [[concepts/prime-rl-post-training|prime-rl]]. Demonstrates that personalized continual learning is achievable with open infrastructure and ~2B tokens of personal coding data.

See: [[entities/sriraam-27upon2]], [x.com/27upon2/status/2040975201068810670](https://x.com/27upon2/status/2040975201068810670)

## Related Concepts

- [[concepts/harness-engineering]] — Context for three-layer learning
- [[concepts/cognitive-debt]] — Related to context layer updates
- [[concepts/multi-agent-consensus-patterns]] — Continuous learning across multiple agents
- [[concepts/real-time-rl]] — Production RL training paradigm
- [[entities/sriraam-27upon2]] — Open-source continual learning implementation