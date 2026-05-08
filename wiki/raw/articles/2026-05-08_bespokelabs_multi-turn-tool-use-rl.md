---
title: "Improving Multi-Turn Tool Use with Reinforcement Learning"
source: "Bespoke Labs Blog"
url: "https://www.bespokelabs.ai/blog/improving-multi-turn-tool-use-with-reinforcement-learning"
date: "2025-04-17"
scraped: "2026-05-08"
authors:
  - "Richard Zhuang"
  - "Trung Vu"
  - "Alex Dimakis"
  - "Maheswaran Sathiamoorthy"
tags: [reinforcement-learning, tool-use, grpo, fine-tuning, ai-agents, post-training]
---

# Improving Multi-Turn Tool Use with Reinforcement Learning

**Bespoke Labs** — April 2025

## Introduction

Learning to use tools is critical for building agents that can interact with the external world. For example, a deep research agent for private enterprise data needs to master a wide range of tools, such as search, SQL, and Pandas, to generate a report. It must not only be able to invoke a single tool in isolation, but also combine the output of multiple tools as the input to another — in essence, the agent should be able to *orchestrate* many tools.

Manual prompt engineering for building agents is easy to start with, but doesn't scale well. To begin with, the list of tools may be long and diverse. Moreover, a prompt engineer designing the agent has to spend increasing amounts of time to cover more and more edge cases with handcrafted rules through trial-and-error. Such a manual approach is reminiscent of what Rich Sutton warned against in his essay, *The Bitter Lesson*.

An alternative method is to use supervised finetuning, where the model learns from demonstrations of responses to user queries. We can collect these demonstrations from humans, which can be expensive. We can also collect these demonstrations from a teacher model, but this only works when we have existing teacher models that are already very good at the task.

**We need a more scalable method that can teach agents to use tools.**

## The Promise of Reinforcement Learning

Reinforcement learning (RL) algorithms can take on many forms, such as PPO or GRPO, but at their core, they allow models to learn by trial-and-error. A model explores a wide range of actions and receives feedback from the environment in the form of rewards. Actions that result in high reward are then reinforced and actions that result in low reward are discouraged. In this way, the model learns to take actions that maximize its reward.

RL is a scalable learning algorithm because it allows models to self-discover solutions by learning from its own experience. Unlike prompt engineering or supervised finetuning, which are both ultimately bottlenecked by human-generated data, RL holds the promise of scaling arbitrarily with compute.

## Reinforcement Learning for Tool Use

Recently, OpenAI has demonstrated that RL can be used to train a research agent that uses tools to carry out complex, multi-step workflows. However, they did not disclose a lot of details about their training recipe. Meanwhile, experiments in the open-source and research community are often single-turn, lacking back-and-forth interaction with an environment.

Bespoke Labs improved Qwen2.5-7B-Instruct's tool use performance by **23%** (55% → 78%) on a subset of the BFCL benchmark using only **100 training samples**, with GRPO.

## Learning to Orchestrate Tools Without Demonstration

**Before Training**: The agent attempts a single tool call (`book_flight`) using a non-existent airport code (NYC) and wrong cost ($0). It fails the task.

**After Training**: The agent:
1. Uses `get_nearest_airport_by_city` for LAX and JFK
2. Uses `get_flight_cost` to retrieve the price ($2400)
3. Uses `book_flight` with correct parameters

It learned to **plan** a correct sequence, **synthesize** previous tool responses, and **orchestrate** multiple tools — without a single demonstration.

## Training Recipe

- **Data**: 200 questions from BFCL v3 multi-turn-base, 50-50 train-test split
- **Model**: Qwen-2.5-7B-Instruct
- **Algorithm**: GRPO, 1600 steps (100 epochs)
- **Hardware**: 4× H200 141GB (3 training, 1 vLLM inference)
- **Hyperparameters**: per_device_batch_size=1, gradient_accumulation_step=4, max_grad_norm=0.2, LR=1e-6 (constant, 20 warmup), KL beta=0.001, μ=2 (one on-policy + one off-policy step per batch)
- **Reward**: Binary (1 if BFCL eval check passes, 0 otherwise)

## Key Findings

### 1. Mitigating Completion Length Blowup
- Dr.GRPO rescaling → still blowup
- Gibberish penalty (GPT-4o-mini judge) → blowup even earlier
- Overlong filtering + no KL → fast collapse at ~300 steps
- **✅ Overlong filtering + KL weight = 0.001** → stable, best performance

### 2. Less Is More for Reward Design
Complex multi-component reward (tool execution + format check + correctness) led to worse stability due to reward hacking. The simplest reward (correctness only) performed best.

### 3. Reference Model Update Boosts Performance
Updating the reference model every 100 steps boosted performance vs. keeping it fixed. A stronger policy model needs a stronger reference model as regulator.

## Authors

- **Richard Zhuang** (Bespoke Labs)
- **Trung Vu** (Bespoke Labs)
- **Alex Dimakis** (Bespoke Labs)
- **Maheswaran Sathiamoorthy** (Bespoke Labs)

## Related
- [[concepts/multi-turn-tool-use-rl]] — Concept page
- [[entities/bespoke-labs]] — Bespoke Labs entity
- [[concepts/bfcl-v3]] — BFCL benchmark
