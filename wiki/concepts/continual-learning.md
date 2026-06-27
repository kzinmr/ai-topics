---
title: "Continual Learning — Continuous Improvement in AI Systems"
type: concept
aliases:
  - continual-learning
  - lifelong-learning-ai
  - incremental-learning
created: 2026-04-27
updated: 2026-06-27
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
- [The Next Paradigm — AIs Learning on the Job](../raw/articles/dwarkesh.com--p-the-next-paradigm--a0808e54.md) (2026-06-26, Dwarkesh Patel) — RLVR generalization limits, OPSD, dreaming, and the 4th scaling axis

## Real-World Implementations

### Cursor Real-Time RL (2026)

[[entities/cursor-ai|Cursor]] applies real-time RL to continuously improve Composer, their coding agent — shipping new checkpoints every ~5 hours using reward signals from real user interactions. This is a production-grade implementation of model-layer continual learning.

See: [[concepts/coding-agents/real-time-rl]], [cursor.com/blog/real-time-rl-for-composer](https://cursor.com/blog/real-time-rl-for-composer)

### Rollouts — Open-Source Continual Learning (2026)

[[entities/sriraam-27upon2|Sriraam (@27upon2)]] built **[rollouts](https://github.com/13point5/rollouts)** — an open-source CLI implementing Cursor-inspired continual learning for coding agents using [[entities/prime-intellect|Prime Intellect]]'s hosted training, [[entities/opencode|OpenCode]], and [[concepts/post-training/prime-rl-post-training|prime-rl]]. Demonstrates that personalized continual learning is achievable with open infrastructure and ~2B tokens of personal coding data.

See: [[entities/sriraam-27upon2]], [x.com/27upon2/status/2040975201068810670](https://x.com/27upon2/status/2040975201068810670)

## Advanced Frameworks — Dwarkesh Patel (June 2026)

Dwarkesh Patel's June 2026 essay ["The Next Paradigm — AIs Learning on the Job"](../raw/articles/dwarkesh.com--p-the-next-paradigm--a0808e54.md) extends the continual learning conversation with several novel frameworks for how AIs can improve from deployment experience.

### RLVR Generalization Limits

Dwarkesh argued that current RLVR (Reinforcement Learning from Verifiable Rewards) training may not generalize from short-horizon to long-horizon tasks. Citing Dario Amodei: *"There's the context length you train at and there's a context length that you serve at"* — short-horizon RL may not transfer to long-horizon real-world problems.

The **grindability problem**: domains must be both verifiable AND parallelizable/replayable (like coding in containers). Domains requiring real-world interaction — business building, litigation, politics — cannot be recreated as deterministic simulators. You can't have 1,000 agents ordering from Amazon in parallel to collect training data.

### On-Policy Self-Distillation (OPSD)

OPSD addresses the sample efficiency problem without requiring outer-loop verifiable rewards. A teacher model (with session context accumulated during deployment) trains the base model by matching its per-token probability distribution. Advantages over RLVR:

1. **No outer-loop reward needed** — no verifier required
2. **Much denser supervision signal** — per-token probabilities vs a single reward per trajectory
3. **Preserves RL's sparsity advantage over SFT** — does not force the model to memorize irrelevant session details

See also [[entities/sasha-rush]]'s blackboard lecture on OPSD.

### Dreaming as the 4th Scaling Axis

"Dreaming" or test-time training proposes that AIs build simulations of reality to rehearse skills. Like EfficientZero playing dozens of simulated Atari games for each real step, future LLMs could generate RL environments to practice skills relevant to specific users. This would become a **fourth axis of scaling** alongside pretraining, RL, and inference-time compute. Instead of `/compact` (KV cache compression), users would hit `/dream` — consuming large compute but providing genuine weight updates from synthetic experience.

### KV Cache vs Weight Update Density

The fundamental tension: the KV cache in Llama 3 70B stores ~320KB per token, while training stores only ~0.075 bits per token — a ~35 million fold difference in information density. In-context learning (KV cache) is sample-efficient but does not scale with memory. Weight updates are dense but sample-inefficient. The gap requires architectural innovations for intermediate representations.

### 2027 Vision

Progression: RLVR → competent deployment agents → OPSD/dreaming distills session learnings back into weights → AIs improve from deployment experience, not just pre-release training. *"Every time you interact with AI, it'll be smarter — not only from your previous sessions but from all its interactions with all the other users."*

## Related Concepts

- [[concepts/harness-engineering]] — Context for three-layer learning
- [[concepts/cognitive-debt]] — Related to context layer updates
- [[concepts/multi-agents/multi-agent-consensus-patterns]] — Continuous learning across multiple agents
- [[concepts/coding-agents/real-time-rl]] — Production RL training paradigm
- [[entities/sriraam-27upon2]] — Open-source continual learning implementation
- [[entities/dwarkesh-patel]] — RLVR generalization limits, OPSD, dreaming framework
- [[entities/sasha-rush]] — Blackboard lecture on OPSD