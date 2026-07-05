---
title: "Prime-RL Post-Training for Subagents"
created: 2026-05-14
updated: 2026-05-14
type: concept
sources: [raw/articles/2026-05-07_RampLabs_building-fast-accurate-agents-with-prime-rl-post-t.md]
tags:
  - training
  - reinforcement-learning
  - ai-agents
  - tool
  - verification
  - qwen
  - company
  - agent-training
  - evaluation
  - search

---

# Prime-RL Post-Training for Subagents

Applying RL post-training to build specialized retrieval subagents — the Ramp Labs "Fast Ask" case study.

## Overview

Ramp Labs built **Fast Ask**, a specialized retrieval subagent for spreadsheet navigation, by fine-tuning a [[qwen|Qwen3.5-35B-A3B]] model (~3B active parameters) with [[grpo|GRPO]] on [[entities/prime-intellect|Prime Intellect]]'s platform. The resulting model beat Claude Opus 4.6 by 4 percentage points on exact-match accuracy while running at Haiku 4.5 latency. The project serves as a case study for when and how to apply RL post-training to narrow, verifiable sub-tasks.

## Motivation: Why Retrieval as a Subagent

In Ramp's production traces, the main agent spent 17.8% of all tool calls on retrieval overhead — opening tabs, reading ranges, filtering irrelevant sheets. About 75% of those read calls were immediately followed by another read call, indicating the agent often failed to retrieve the right information on the first attempt.

Three properties make retrieval a strong fit for a specialist subagent:

1. **Context protection.** A retrieval subagent shields the main agent from irrelevant rows and decoy sheets, returning only the answer-relevant cells or computed value.
2. **Latency sensitivity.** Users perceive faster responses when the main agent receives spreadsheet facts quickly rather than spending turns exploring.
3. **Verifiability.** Unlike open-ended financial reasoning, many spreadsheet questions resolve to an exact value — a date, an invoice ID, a cent amount, a yes/no answer. This makes the task **deterministically scorable**, a natural fit for RL because trajectories can be scored without human labels or LLM judges.

This pattern — training small, verifiable subagents for narrow bottlenecks while letting frontier models spend tokens on judgment rather than retrieval — generalizes beyond spreadsheets.

## Experimental Setup

### Base Model and Platform

Fast Ask used [[qwen|Qwen3.5-35B-A3B]] (a sparse MoE with ~3B active parameters) as the base model, trained on Prime Intellect's Lab platform. The training environment directly mirrored Ramp's production deployment harness.

The run used:
- **100 training steps**, batch size 256, 8 rollouts per example
- Evaluation every 20 steps on 128 held-out examples
- Thinking mode **disabled** — matching the low-latency production setting
- Training completed in ~26 hours

### Synthetic Dataset

Each task consists of a synthetic business workbook, a natural language question, and a ground-truth answer. The workbooks reflect real finance workflows: revenue rollups, invoice reconciliation, spend analysis, time-filtered lookups, and multi-join aggregations.

The dataset spans **14 task types across three families**, with three differently-phrased variants per task (e.g., investor memo requests, collections follow-ups, fundraise model questions). This prevents the model from overfitting to a single prompt template.

Synthetic data enabled the team to:
- Scale the task distribution while maintaining reliability
- Control answers exactly
- Vary surface phrasing without changing the underlying skill

### Adversarial Workbook Design

Three strategies make the training environment tough enough to produce a robust policy:

- **Decoy sheets.** Medium/hard workbooks include finance-adjacent but answer-irrelevant tabs (e.g., `HiringPlan`, `CapTable`). A model that reads indiscriminately wastes its turn budget.
- **Partial helper summaries.** Some workbooks include summary sheets like `RegionalPnL` that look like shortcuts but omit computed columns. The model must verify or aggregate from source data. At hard difficulty, helper summaries are removed entirely.
- **Identifier obfuscation.** In ~15–20% of reconciliation tasks, questions reference an invoice by a payment clue (source system, method, date, amount) rather than by its `INV-####` ID. The model must resolve the reference before it can answer.

### Tool Interface

The model gets **three tools** and a **15-turn budget**:

| Tool | Description |
|------|-------------|
| `get_workbook_metadata` | Returns sheet names, tab colors, approximate used ranges |
| `read_ranges` | Returns cell data, hard-capped at 1,000 cells per call (oversized requests rejected) |
| `run_python` | Sandboxed Python (standard library only), state persists across calls within a rollout |

Keeping the tool space small is intentional: with only three tools, efficient and wasteful trajectories are easier to distinguish in the reward signal.

## RL Algorithm Design

### Reward Function

The reward function directly encodes production priorities — correct answer, fast, concise:

$$R(y_i) = 1.0 \cdot \text{correct}(y_i) + 0.1 \cdot \text{efficiency}(y_i) + 0.05 \cdot \text{concise}(y_i)$$

- **Correctness (1.0)** dominates. Fires only when the final `"ANSWER:"` line parses into the expected type and exact-matches ground truth.
- **Efficiency (0.1)** and **concision (0.05)** are small shaping rewards. They cannot rescue a wrong answer, but they distinguish between correct trajectories — a correct answer in five turns scores slightly higher than the same answer after wandering through irrelevant sheets.

### GRPO with Async Off-Policy Training

Training used [[grpo|Group Relative Policy Optimization (GRPO)]], which estimates advantages from groups of rollouts sampled for the same prompt, eliminating the need for a separate value model:

$$A_i = R(y_i) - \frac{1}{G}\sum_{k=1}^{G}R(y_k)$$

The policy gradient update pushes probability mass toward behaviors that made the final answer correct: reading metadata first, avoiding decoy sheets, using helper summaries when valid, falling back to raw rows when needed, and emitting a parseable `"ANSWER:"` line.

A critical practical enabler was **async off-policy RL**. Multi-turn spreadsheet rollouts are slow — much slower than ordinary supervised fine-tuning data loading. Prime Intellect's `prime-rl` stack keeps rollout workers generating trajectories while the trainer updates the model, using clipped importance weighting to correct for bounded staleness:

$$J(\theta) = \sum_{i,t} \min\left(\rho_{i,t}(\theta) A_i,\ \text{clip}(\rho_{i,t}(\theta), 1-\epsilon, 1+\epsilon) A_i\right)$$

Without this, GPU utilization would suffer dramatically since trainers would idle waiting for fresh trajectories after every update.

## Results

On the held-out evaluation set:

| Model | Exact-Match Accuracy | Wall-Clock Time |
|-------|---------------------|-----------------|
| Fast Ask (RL-trained Qwen3.5-35B-A3B) | **Beats Opus 4.6 by 4pp** | Haiku 4.5 latency |
| Base Qwen3.5-35B-A3B (no RL) | −10pp below trained | Slower |

RL training added **10 percentage points of accuracy** over the base model while **reducing** average completion time. Reward climbed from roughly 0.2 to 0.8 over the first 40 steps before plateauing.

Notably, total cells read per rollout stayed roughly flat during training — the model didn't learn to read less overall, but rather to **allocate its reads better**.

## Key Insights

1. **RL works for verifiable sub-tasks.** The environment made spreadsheet retrieval measurable and repeatable. No human-labeled trajectories or LLM judges were needed — only a deterministic correctness check against ground truth.

2. **Environment design is the important work.** The right tasks, a minimal tool interface, and a reward function grounded in production behavior mattered more than model architecture or scale.

3. **Async off-policy RL makes multi-turn agent training practical.** When rollouts involve tool calls, Python execution, and multi-step reasoning, keeping the GPU busy requires decoupling rollout generation from weight updates.

4. **Specialized subagents can beat frontier models at narrow tasks.** A ~3B active parameter model, trained with RL in a tightly-scoped environment, outperformed a general-purpose frontier model at a fraction of the cost and latency.

## Related Concepts

- [[concepts/sid-1]] — First model trained end-to-end with RL (GRPO) for agentic retrieval, directly comparable approach
- [[concepts/unbundled-agents]] — Architectural pattern of specialist subagents exposed as tools within a harness
- [[concepts/post-training-distributional-view]] — Distributional lens on SFT vs. RL vs. On-Policy Distillation
- [[verifiers-rl]] — TRL-based multi-turn RL framework using GRPO for environment and tool interactions
- [[concepts/qwen]] — The Qwen model family used as the base model for Fast Ask
