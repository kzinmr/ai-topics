---
title: "SkillOpt"
created: 2026-05-26
updated: 2026-05-26
type: concept
tags:
  - optimization
  - prompting
  - ai-agents
  - self-improving
  - evaluation
  - training
  - trace-analysis
  - gepa
sources:
  - raw/papers/2026-05-26_2605.23904_skillopt-executive-strategy-self-evolving-agent-skills.md
  - https://arxiv.org/abs/2605.23904
aliases: [skill-optimizer, skill-optimization]
related:
  - concepts/gepa
  - concepts/hermes-agent
  - agent-skills
---

# SkillOpt

> **TL;DR:** A text-space optimizer that trains a frozen LLM agent's skill document using deep-learning discipline — rollout batches, validation gates, learning rates, and momentum. Best or tied-best on all 52 evaluated (model, benchmark, harness) cells. +23.5 pts average gain over no-skill. Outperforms [[concepts/gepa|GEPA]], TextGrad, and EvoSkill across the board.

SkillOpt is a skill optimization framework by Microsoft Research, Shanghai Jiao Tong University, Tongji University, and Fudan University (May 2026). It treats an agent's **skill document** (a natural-language policy in the system prompt) as a **trainable external state** and applies training-style controls borrowed from deep learning: batches, validation gates, learning rates, momentum. The deployed artifact is a compact `best_skill.md` file (~300–2,000 tokens) with zero additional inference cost.

The core insight: if the recurring object of adaptation is the agent's procedure, the skill document itself should be trainable with the same discipline that makes weight-space optimization reproducible.

## Optimization Loop

SkillOpt's optimizer loop maps 1:1 to deep learning concepts:

| DL Concept | SkillOpt Analogue |
|------------|-------------------|
| Training minibatches | Rollout batches + reflection minibatches |
| Learning rate | Edit budget L_t (max edits per step) |
| Held-out validation | Validation gate on selection split D_sel |
| Gradient history | Rejected-edit buffer (negative feedback) |
| Momentum | Epoch-wise slow/meta update |
| Optimizer model | Separate frontier LLM (not deployed) |
| Forward/backward pass | Rollout evidence → minibatch reflection |

### 1. Rollout Batch (Forward Pass)
The target model executes a batch of tasks with the current skill. The harness captures full trajectories: reasoning steps, tool calls, observations, and scores.

### 2. Minibatch Reflection (Backward Pass)
Failures and successes are partitioned into **reflection minibatches** (default size: 8). The optimizer model analyzes each minibatch and proposes structured **add/delete/replace** edits:
- **Failure minibatches** → missing or corrective rules
- **Success minibatches** → preserve behaviors that already work
- Edits are merged hierarchically, with failure corrections prioritized

> *This is the key difference from GEPA: SkillOpt's reflection is minibatch-structured rather than population-based. Each minibatch focuses on common procedural errors, not anecdotal fixes.*

### 3. Bounded Text Updates (Learning Rate L_t)
An **edit budget** L_t limits the number of edits applied per step (default: L_t=4, cosine schedule with floor 2). This prevents catastrophic forgetting and overfitting. Without bounded updates, unbounded rewrites can erase useful rules, introduce incompatible instructions, or overfit to local failures.

### 4. Validation Gate & Rejected-Edit Buffer
Every candidate skill is evaluated on a **held-out selection split** D_sel. It is accepted **only if score strictly improves** (ties rejected). Rejected edits are stored in a buffer and shown to the optimizer in later calls — acting as negative feedback without inference cost.

### 5. Epoch-Wise Slow/Meta Update
At epoch boundaries, the same training items are re-evaluated under the previous and current skill. The optimizer writes longitudinal guidance into a **protected region** of the skill document (`<!-- SLOW_UPDATE_START -->`...`<!-- SLOW_UPDATE_END -->`). A separate **optimizer-side meta skill** summarizes edit patterns that helped or hurt, but is never shipped with the deployed artifact.

### 6. Harness-Agnostic Deployment
A lightweight adapter interface allows the same optimizer to work with direct chat, Codex CLI, Claude Code, and embodied environments. Only `best_skill.md` is deployed — no model weight changes, no optimizer dependency at runtime.

## Experimental Results

**Setup:** 6 benchmarks (SearchQA, SpreadsheetBench, OfficeQA, DocVQA, LiveMathematicianBench, ALFWorld), 7 target models (GPT-5.5 through GPT-5.2, Qwen3.5-4B, Qwen3.6-35B-A3B), 3 harnesses (direct chat, Codex, Claude Code). **52 total cells** in the evaluation matrix.

| Setting | SkillOpt Gain |
|---------|--------------|
| **All 52 cells** | **Best or tied-best** in every cell |
| GPT-5.5 direct chat avg | +23.5 pts over no skill; +5.4 over best per-cell baseline |
| GPT-5.5 Codex harness avg | +24.8 pts over no skill; +14.0 over EvoSkill |
| GPT-5.5 Claude Code avg | +19.1 pts over no skill; +3.2 over EvoSkill |
| GPT-5.4-nano (smallest) avg | +26.7 pts over no skill |
| SpreadsheetBench GPT-5.5 | 41.8 → 80.7 (+38.9) |

Key findings:
- **Procedural benchmarks benefit most**: SpreadsheetBench, OfficeQA, ALFWorld show the largest gains
- **Not frontier-model-dependent**: Small models benefit most in relative terms
- **Training evidence scales**: SpreadsheetBench rises from 47.5 to 78.0 with full training set (vs 1%)
- **Validation gate is critical**: Removing it drops performance significantly
- **Edit budget L_t=4 near optimal**: Smaller loses exploration, larger risks overfit

## Comparison with GEPA

SkillOpt and [[concepts/gepa|GEPA]] are both text-space skill optimizers that work without model weight changes, but they diverge on optimization philosophy:

| Dimension | GEPA | SkillOpt |
|-----------|------|----------|
| **Search method** | Evolutionary (Pareto front) | Gradient-style (bounded stepwise) |
| **Edit mechanism** | Mutations from ancestral lessons | Structured add/delete/replace from minibatch reflection |
| **Population** | Pareto front of multiple candidates | Single best candidate with rejected buffer |
| **Validation** | Constraint gates + test suite (100% pass) | Strict held-out validation gate (score must improve) |
| **Learning rate** | Implicit (population diversity) | Explicit (L_t, cosine schedule, floor) |
| **Stability** | Pareto diversity + human PR review | Validation gate + rejected buffer + slow update |
| **Epoch awareness** | None | Epoch-wise slow/meta update |
| **Deployment** | PR against repo | `best_skill.md` file |
| **Rollout efficiency** | 400–1,200 rollouts | Not directly comparable (different benchmarks) |

SkillOpt's results are generally stronger in head-to-head comparisons where both appear, but GEPA's Pareto-based approach may be more robust for diverse skill portfolios where a single "best" skill is insufficient. The approaches are **complementary**: SkillOpt provides training-style stability controls that could enhance GEPA's exploration, while GEPA's population-based search could improve SkillOpt's candidate diversity.

## See Also

- [[concepts/gepa]] — Genetic-Pareto Prompt Evolution: the evolutionary alternative to SkillOpt, used in [[entities/hermes-agent]]'s self-evolution pipeline
- [[entities/hermes-agent]] — The agent framework where GEPA (and potentially SkillOpt) optimize skills
- [[concepts/agent-skills]] — The skill files being optimized: Markdown playbooks with YAML frontmatter
- [[entities/dspy]] — DSPy framework with built-in GEPA optimizer; could potentially integrate SkillOpt
