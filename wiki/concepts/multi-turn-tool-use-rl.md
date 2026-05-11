---
title: Multi-Turn Tool Use with Reinforcement Learning
created: 2026-05-08
updated: 2026-05-08
type: concept
tags:
  - tool
  - reinforcement-learning
  - training
  - ai-agents
  - fine-tuning
  - evaluation
  - coding-agents
aliases: [Tool Use RL, Multi-Turn Tool Use RL]
sources: [raw/articles/2026-05-08_bespokelabs_multi-turn-tool-use-rl.md]
related:
  - concepts/bfcl-v3
  - concepts/grpo
  - concepts/deepseek-r1
  - entities/bespoke-labs
---

# Multi-Turn Tool Use with Reinforcement Learning

A training methodology where reinforcement learning (RL) — specifically [[GRPO]] (Group Relative Policy Optimization) — is used to teach language model agents how to **orchestrate multiple tools** across multiple interaction turns, without relying on human demonstrations or teacher model outputs.

## Core Idea

Prompt engineering and supervised fine-tuning for agent tool use are both bottlenecked by human-generated data. RL allows models to **self-discover** effective tool-use strategies through trial-and-error, receiving rewards from environment feedback. This scales with compute rather than human effort — directly following Rich Sutton's *Bitter Lesson* principle.

## Key Result (Bespoke Labs, 2025)

| Metric | Before Training | After Training |
|---|---|---|
| BFCL v3 multi-turn accuracy | 55% | **78%** (+23%) |
| Training samples | — | **100** (50-50 split) |
| Model | Qwen2.5-7B-Instruct | Qwen2.5-7B-Instruct (RL-tuned) |
| Algorithm | — | GRPO, 1600 steps |
| Hardware | — | 4× H200 141GB |

The agent learned to:
1. **Plan** a correct sequence of tool calls in advance
2. **Synthesize** responses from earlier tools as inputs to later tools
3. **Orchestrate** multiple tools (e.g., `get_nearest_airport_by_city` → `get_flight_cost` → `book_flight`)

## Training Recipe (Bespoke Labs)

### Algorithm
- **GRPO** (Group Relative Policy Optimization) — same core algorithm behind [[DeepSeek-R1]]
- 1600 steps (100 epochs)
- μ=2 (one on-policy step + one off-policy step per batch)

### Hyperparameters
| Parameter | Value |
|---|---|
| per_device_batch_size | 1 |
| gradient_accumulation_step | 4 |
| max_grad_norm | 0.2 |
| Learning rate | 1e-6 (constant, 20 warmup) |
| KL beta | 0.001 |
| Reference model update | Every 100 steps |

### Reward Design
**Simple binary reward** (correctness only):
- Reward = 1 if BFCL eval check passes (state-based + response-based)
- Reward = 0 otherwise

Complex multi-component rewards (tool execution success + format check + correctness) performed **worse** due to reward hacking.

## Key Findings

### 1. Completion Length Blowup Mitigation

During GRPO training with tool-use environments, models frequently degenerate into producing long strings of gibberish (repeated tokens, random characters). This causes complete collapse in training and eval accuracy.

| Approach | Result |
|---|---|
| Dr.GRPO reward rescaling | ❌ Still blowup |
| Gibberish penalty (GPT-4o-mini judge) | ❌ Blowup even earlier |
| Overlong filtering + no KL penalty (DAPO-style) | ❌ Fast collapse at ~300 steps |
| **Overlong filtering + small KL weight (0.001)** | ✅ Stable, best performance |

The finding that removing KL penalty (per DAPO) causes rapid collapse corroborates similar observations from the HuggingFace TRL team.

### 2. Less Is More for Reward Design

A single correctness-based reward outperformed multi-component rewards combining tool execution success rate, format adherence, and correctness. The hypothesis: complex rewards create more opportunities for **reward hacking**.

### 3. Reference Model Update

Updating the reference model every 100 steps (rather than keeping it fixed at the initial checkpoint) boosted performance. Intuition: as the policy model improves, the KL regularizer needs a stronger reference model to pull against — otherwise the KL term anchors the model to its initial (weaker) performance.

## Comparison: Prompt Engineering vs SFT vs RL

| Method | Scalability | Data Requirement | Bottleneck |
|---|---|---|---|
| Prompt Engineering | Low | None | Human trial-and-error |
| Supervised Fine-Tuning | Medium | Human/teacher demos | Human data collection |
| **RL for Tool Use** | **High** | Environment + reward function | Compute |

## Relationship to DeepSeek-R1

Uses the same GRPO algorithm that powers [[DeepSeek-R1]]'s reasoning capabilities, but applies it to a different domain: **tool orchestration** rather than mathematical reasoning. The overlong filtering technique from DAPO and KL penalty tuning are shared concerns.

## Open Questions

- Can this approach scale to larger models (7B → 70B+)?
- How does the learned tool-use ability generalize to unseen tools?
- What's the optimal reward function for more complex multi-agent orchestration scenarios?
- Can RL-trained tool use be combined with reasoning RL for agents that both *think* and *act*?

## See Also

- [[concepts/grpo]] — Group Relative Policy Optimization algorithm
- [[concepts/bfcl-v3]] — Berkeley Function Calling Leaderboard (BFCL) benchmark
- [[concepts/deepseek-r1]] — DeepSeek-R1 reasoning model (uses GRPO for reasoning)
- [[entities/bespoke-labs]] — Bespoke Labs, the research lab behind this work
- [[concepts/agent-evaluation]] — Agent evaluation methodologies
