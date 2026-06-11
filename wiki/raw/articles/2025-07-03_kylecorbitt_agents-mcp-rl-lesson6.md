---
title: "Lesson 6: Training Agents with GRPO — Experiment Iteration & Advanced Reward Design"
type: article
created: 2026-06-11
updated: 2026-06-11
tags:
  - reinforcement-learning
  - grpo
  - agentic-rl
  - reward-engineering
  - agent-evaluation
  - experiment-tracking
  - ai-agent-engineering
sources:
  - transcripts/2025-07-03_kylecorbitt_agents-mcp-rl-lesson6-lecture.md
  - https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
  - https://github.com/willccbb/ai-agent-engineering
---

# Lesson 6: Training Agents with GRPO — Experiment Iteration & Advanced Reward Design

**Instructor:** Kyle Corbitt (CTO, [[concepts/corbett-kyle-corbitt|OpenPipe]])
**Date:** July 3, 2025 | **Course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
**Lecture transcript:** [[transcripts/2025-07-03_kylecorbitt_agents-mcp-rl-lesson6-lecture]]

Final lecture of the course. After getting the Art E training loop running in Lesson 5, Kyle focuses on **practical experimentation patterns** for RL training — how to iterate fast, track experiments, and what ablation results reveal about reward design, LM-as-judge, and dataset size requirements.

---

## Training Run Results

The Art E email search agent (Qwen 2.5 14B) trained via GRPO achieves **~86% accuracy** on the Enron email QA task — close to state-of-the-art (high eighties to low nineties). Training was stable with healthy reward standard deviation (~0.15–0.20), indicating sufficient output diversity for learning.

The previous lesson's bug was a simple **indentation error** — training lines were indented one level too far, causing `await groups` to fire per-scenario instead of per-batch.

---

## Experiment Registry Pattern

Rather than editing hyperparameters in a single file (error-prone), ART uses a structured approach:

1. **`RunConfig`** Pydantic model holds all experiment parameters — logged to W&B and saved with checkpoints
2. **`all_experiments.py`** registry file — each experiment is a named `TrainableModel` with its config
3. **`model_copy()` branching** — clone an existing experiment and override specific parameters
4. **SkyPilot cluster-per-experiment** — each run gets its own GPU cluster (named after the model), enabling parallel experiments

```python
# Branch off existing model, override one parameter
models["run_2"] = models["run_1"].model_copy()
models["run_2"].name = "run_2"
models["run_2"].config.rollouts_per_group = 8
```

---

## Key Findings

### 1. Simple Rewards Can Outperform Complex Ones

Two reward functions compared on the same task:

| | Complex (Model 8) | Simple (Model 14) |
|---|---|---|
| Reward signal | Partial credit for finding/reading emails, source matching, turn efficiency, format penalties | 1.0 if correct, 0.0 if wrong |
| Convergence | ~300–540 steps | ~90 steps |
| Final accuracy | ~86% | ~86% |
| Turn efficiency | Better (rewarded for fewer turns) | Worse (not rewarded) |

**Takeaway:** Simple binary rewards converge faster. Complex rewards give control over secondary behaviors (efficiency, tool usage) but may slow convergence. Start simple, add complexity only when needed.

### 2. LM-as-Judge Without Ground Truth Works

An O3-based judge that sees only the 4 rollouts in a group (no ground truth answer) can train a model that:
- **Converges faster** than ground-truth-based training
- Reaches **similar final accuracy**
- Works by comparing trajectories — e.g., noticing one rollout read the right email while others didn't

Not foolproof (Qwen 3 32B as judge collapsed during training), but a promising research direction for tasks where ground truth is unavailable.

**Cost caveat:** O3-as-judge costs ~$1,000/run vs. ~$30–50 for training compute.

### 3. Dataset Size: 16–256 Examples Are Sufficient

Ablation across powers of 4 (1 to 4096 training examples), keeping total training steps constant:

| Examples | Val Accuracy | Notes |
|---|---|---|
| 1 | ~63% | Still improves; no catastrophic overfitting (unlike SFT) |
| 16 | High 80s | Comparable to best prompted models |
| 256 | Full convergence | Same as 4096 |

**Key insight:** RL does not catastrophically overfit like SFT. Even looping on a single example doesn't cause collapse — normalization and selective training prevent it.

---

## GPU Utilization Patterns

The bottleneck in RL training is the **rollout phase**, not weight updates:
- **Straggler problem**: Some agents take 10+ turns while others finish in 3
- **External tool latency**: Web search etc. leaves GPU idle
- **Target**: 30–40 simultaneous requests on an H100
- **`limit_concurrency`** helper in ART prevents overload for large batches

OpenPipe is developing a **shared GPU fleet** for hosted RL — multiple users on the same base model (LoRA) share aggregate GPU utilization, smoothing out spiky patterns.

---

## Practical Guidance

### When to Use SFT Before RL
- Look at initial reward and reward std dev
- If the model succeeds sometimes and std dev is decent → skip SFT
- If the model is hopeless → SFT to bootstrap basic skills first
- **Qwen 2.5/3** are usually good enough out of the box for tool-calling tasks

### Qwen 3 Training Gotchas
- Thinking mode requires XML `<think></think>` tags at each turn start
- Thinking tokens only serialized for the most recent turn
- Complicates multi-turn training; 2.5 vs 3 difference is usually small

### MCP in Training Loops
- MCP lacks per-user authentication (as of mid-2025)
- Requires many server processes for diverse training data
- Expected fix: multi-user MCP servers

---

## Ecosystem Context

- **Other RL trainers**: Verifiers (Will Brown), veRL (academic), RLLM (Together/Agentica), SkyRL (veRL wrapper). ART built because existing options weren't easy enough.
- **OpenAI's consulting move** into fine-tuning suggests industry consensus: task-specific training yields large gains even with frontier models.
- **Favorite agentic use cases**: Deep research, customer support, outbound list building, root cause analysis of downtime.

---

## Related

- [[concepts/agents-mcp-rl-course]] — Course portal
- [[transcripts/2025-07-03_kylecorbitt_agents-mcp-rl-lesson6-lecture]] — Full transcript
- [[raw/articles/2025-07-02_kylecorbitt_agents-mcp-rl-lesson5]] — Lesson 5: Formulating Business Problems as RL Tasks
- [[raw/articles/2025-07-03_willbrown_agents-mcp-rl-lesson5-5]] — Bonus: GRPO Details
- [[raw/articles/2025-06-27_kylecorbitt_agents-mcp-rl-office-hours]] — Office Hours with Kyle
- [[concepts/grpo-rl-training]] — GRPO algorithm details
- [[concepts/reward-hacking]] — Reward hacking taxonomy
- [[concepts/rl-harness-lifecycle]] — Agent-RL co-evolution framework
- [[raw/articles/2025-07-11_corbt_ruler-easy-mode-rl-rewards]] — RULER: related work on LM-as-judge rewards
