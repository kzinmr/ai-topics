---
title: "Production-Ready Agent Engineering — Lesson 3: Agent Evals and Optimization"
author: Will Brown
date: 2025-06-24
date_ingested: 2026-06-10
source: https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
notebook: https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec3-evals-optimization/evals_optimization.ipynb
type: lecture-summary
tags:
  - ai-agents
  - evaluation
  - llm-as-judge
  - reinforcement-learning
  - grpo
  - fine-tuning
  - reward-hacking
  - agent-evaluation
  - education
---

# Production-Ready Agent Engineering — Lesson 3: Agent Evals and Optimization

**Instructor:** Will Brown (Research Lead, [[entities/prime-intellect]])
**Co-instructor:** Kyle Corbitt (CTO, OpenPipe)
**Date:** June 24, 2025
**Companion course:** [[concepts/agents-mcp-rl-course|Production-Ready Agent Engineering: From MCP to RL]]
**Lecture transcript:** [[transcripts/2025-06-24_willbrown_agents-mcp-rl-lesson3-lecture|Agent Evals and Optimization (Lecture Transcript)]]
**Notebook:** [evals_optimization.ipynb](https://raw.githubusercontent.com/willccbb/agent-engineering/refs/heads/main/lectures-1-through-4/lec3-evals-optimization/evals_optimization.ipynb)

## Summary

The third lecture focuses on **evaluation methodology** as the foundation for RL optimization. Covers benchmark landscape (Artificial Analysis, BFCL v3, TAO Bench), **model spec** as the starting point for eval design, deterministic evals (format parsing, instruction following, set-product generation), LM judges (calibration, pairwise comparison, position bias), **supervised fine-tuning** (TRL/Axolotl/Unsloth/Torchtune, LoRA vs full, curriculum learning), and a deep dive into **GRPO** (reference models, KL penalty, on-policy vs off-policy, online reference updates).

## Key Topics

### 1. Model Spec as Eval Foundation

Before building evals, write a **model spec** — a qualitative document defining intended system behavior, edge cases, and guardrails. OpenAI's model spec is a reference. For user-facing agents, consider:
- **User simulation** — LLM-simulated users with personality profiles and few-shot examples to test multi-turn interactions
- **Guardrail evals** — ensuring agents won't perform prohibited actions
- **FAQ evals** — can the agent reliably answer questions about your system? Quick win, easy to author 20-30 test cases

### 2. Benchmark Landscape

| Benchmark | Type | Notes |
|-----------|------|-------|
| GPQA | Multiple choice science | Standard provider benchmark |
| Humanity's Last Exam | Short answer, LM-judged | Hard knowledge questions |
| LiveCodeBench | Live coding | LeetCode/Codeforces, auto-updating |
| MMLU-Pro | Multiple choice | Updated MMLU |
| BFCL v3 | Multi-turn tool calling | User simulator, decision trees |
| TAO Bench | Multi-turn agent | Grounded domains (airlines, reservations) |
| Minecraft Bench | Creative tool use | Visual/creative eval via voting |
| IFEval | Instruction following | Deterministic constraint checking |

### 3. Deterministic Evals

For verifiable tasks, use pure Python functions:
- **Format parsing** — check think-token structure, box notation (`\boxed{}`)
- **Instruction following** — letter counts, comma avoidance, word frequency
- **Set-product generation** — take Cartesian product of variable lists to generate 1,800+ test cases from a handful of parameters
- Models struggle with letter-count constraints (even GPT-4.1 fails on "use letter T at most once")

### 4. LM Judges and Golden Answers

- **LM judges** — fuzzy matchers that see ground truth + context + criteria; use chain-of-thought for better reasoning
- **Golden answers** — human data of final outputs (not full traces); agents use tools as "reasoning" to produce the final object
- **Best-of-N** — generate multiple samples, pick the best; useful for creating golden eval data (expensive upfront, but eval sets are small)
- **Judge calibration** — compare multiple judges (Nano, Mini, Opus) on the same outputs; if small model agrees with big model, fall back to small
- **Position bias** — randomize A/B order in pairwise comparisons; GPT-4.1 vs GPT-4.1 should converge to 50%
- **Confidence intervals** — run evals multiple times; if model A beats model B by more than the margin of error, it's a real improvement

### 5. Tool-Use Evals

Treat every agent action as an eval metric:
- Fraction of times model calls a tool
- Fraction of tool calls that succeed (no errors)
- Tool call count (reward non-zero use; incentivize fewer rounds if correct — Kyle Corbitt)
- Architect for a dashboard of these metrics from the start

### 6. Supervised Fine-Tuning (SFT)

**When to SFT:** API model too slow/expensive, want local inference, or need a foundation before RL.

**Dataset creation:**
- Run rollouts with a capable model → filter by reward score (top-half heuristic)
- 1,000–10,000 examples is the sweet spot
- Use DeepSeek V3 for cheap data generation (allowed to train on, doesn't overthink)

**Libraries:**

| Library | Best For | Notes |
|---------|----------|-------|
| TRL (HuggingFace) | General-purpose | Good defaults, SFTTrainer |
| Unsloth | Single GPU, max efficiency | Kernel optimizations, quantization |
| Axolotl | Distillation, bells & whistles | Built on TRL |
| Torchtune | Pure PyTorch, hackable | Official PyTorch, minimal deps |

**GPU recommendations:**
- Start small (RTX 6000, 2×48GB = $1.50/hr) for debugging
- H100 ($10/hr) for serious runs; A100 for budget-conscious
- LoRA for 7B on single GPU; full fine-tuning needs ~70GB for 7B
- **Gradient accumulation** — free win: same as larger batch, but slower in exchange for less memory

**LoRA trade-offs:**
- Pro: smaller files, single GPU, keep same base model
- Con: bounds how much you can learn
- Rule of thumb: the larger/longer/more tasks your run → the less sense LoRA makes

### 7. Curriculum Learning

- Sort dataset by difficulty (measure: fraction correct over N runs)
- Easy first, hard later
- Throw away items model always gets right (no signal) and always gets wrong (no gradient)
- Sweet spot: model gets it right sometimes, wrong sometimes → GRPO can learn from the contrast

### 8. GRPO Deep Dive

**Core algorithm:** For each step, sample a batch of prompts × rollouts per prompt. Compare good vs bad completions, compute advantage, update policy.

**Key parameters:**
- **Rollouts per prompt** — 64 is common (DeepSeek paper); more is better
- **KL penalty (beta)** — anchors to reference model; >0.1 is high, can go to 0
- **Reference model updates** — online merging (every 100 steps) prevents drift while allowing learning

**On-policy vs off-policy:**
- SFT/DPO = off-policy (fixed distribution)
- GRPO = on-policy by design (fresh samples each step)
- 1-step off-policy is safe; allows overlapping training and inference
- More off-policy = more stale rollouts = more noise

**Training failures:** Often caused by low reward variance in a batch (all 0s or all 1s) + high KL penalty. Mitigate with online reference model updates and careful beta tuning.

**LoRA for RL:** Kyle Corbitt plans to focus on LoRA for the RL portion — most students want task-specific reliability, not frontier-model competition.

**DSPy + GRPO:** Exists but not the most effective optimizer for GRPO. DSPy wants abstracted optimizers; GRPO value is in fine-grained control.

### 9. Distillation (Brief)

- Training on full logit sequences from a teacher model (not just correct token)
- Requires matching tokenizers and model heads → same model family only
- "DeepSeek distill" models are SFT, not true token distillation

## Key Takeaways

1. **Write a model spec before writing evals** — define intended behavior, then measure it
2. **Deterministic evals first** — format, instructions, tool calls; use Python functions, not LM judges
3. **LM judges need calibration** — compare multiple judges, randomize positions, compute confidence intervals
4. **SFT is the gateway to RL** — validates that your task is learnable before expensive RL runs
5. **GRPO is delicate** — reward variance, KL penalty, and on/off-policy tradeoffs all matter; start slow and safe
6. **LoRA works for most use cases** — only go full fine-tuning for multi-task or large-scale runs
