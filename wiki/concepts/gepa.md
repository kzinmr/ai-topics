---
title: "GEPA (Genetic-Pareto Prompt Evolution)"
created: 2026-05-14
updated: 2026-05-14
type: concept
tags: [gepa, evolutionary-algorithms, prompting, optimization, self-improving, agent-skills, hermes-agent, nous-research, evaluation]
sources:
  - raw/articles/2026-05-13_akshaypachaar_hermes-agent-masterclass.md
  - raw/papers/2025-07-25_2507.19457_gepa-reflective-prompt-evolution.md
  - https://arxiv.org/abs/2507.19457
aliases: [genetic-pareto, gepa-optimizer]
---

# GEPA (Genetic-Pareto Prompt Evolution)

> **TL;DR:** A reflective, sample-efficient prompt optimizer that uses natural language reflection + evolutionary search instead of reinforcement learning. Outperforms GRPO by 6% on average (up to 20%) using **35× fewer rollouts**. ICLR 2026 Oral. MIT licensed.

GEPA (Genetic-Pareto) is a prompt optimizer for compound AI systems that merges **textual reflection** with **multi-objective evolutionary search**. Developed by a multi-institution collaboration (UC Berkeley, Stanford, Databricks, MIT), it iteratively mutates prompts using LLM-generated natural language feedback from execution traces. Unlike RL methods (GRPO) that collapse complex trajectories into scalar rewards, GEPA treats those trajectories as rich textual artifacts to diagnose, reflect on, and evolve.

## How It Works

The core pipeline:

1. **Read current skill/prompt** from the target system (e.g., a Hermes Agent skill)
2. **Generate evaluation dataset** — synthetic test cases (via Claude Opus), real session history (from SQLite), or hand-curated golden sets
3. **GEPA optimization loop:**
   - **Execution traces** → Run candidate prompts on minibatches, capture full trajectories (reasoning, tool calls, outputs)
   - **Failure analysis** → LLM reflects on traces in natural language to diagnose *why* things failed, not just *that* they failed
   - **Candidate generation** → Propose targeted prompt mutations informed by accumulated ancestral lessons
   - **LLM-as-judge scoring** → Score candidates with rubrics (not binary pass/fail), using **Actionable Side Information (ASI)** — error messages, profiling data, reasoning logs
4. **Constraint gates:** 100% test suite pass, skills under 15KB, caching compatibility preserved, semantic purpose doesn't drift
5. **Best variant** goes out as a **PR**, never a direct commit — human oversight retains final control

GEPA maintains a **Pareto front** of top-performing prompts and stochastically explores across it, preventing the local optima that plague greedy prompt optimizers.

## Key Innovations

- **Execution-trace-based evaluation vs self-report:** Instead of asking an agent "did you do well?" (which invites self-congratulation), GEPA reads what actually happened in the execution trace — which tool calls failed, where the reasoning diverged, what outputs were produced
- **Pareto optimization:** Maintains a diverse population of high-performing prompts rather than converging on a single "best" — crucial for robust generalization across diverse problem instances
- **Constraint gates:** Hard enforcement of correctness (100% test pass), size limits, caching compatibility, and semantic preservation — preventing optimization from producing prompts that score well but break in practice

## Relationship to Hermes Agent

GEPA is **not built into the Hermes Agent runtime**. It lives in a companion repository: **`NousResearch/hermes-agent-self-evolution`** (MIT licensed). It operates as an **offline optimization pipeline** that:

- Reads skills from a Hermes repo
- Generates evaluation datasets from session history or synthetic data
- Runs the GEPA optimizer to produce improved skill variants
- Submits the best variant as a PR against the Hermes repo for human review

This addresses a known weakness of Hermes Agent's in-agent learning loop: agents tend toward self-congratulation and can overwrite manual customizations with worse versions. GEPA provides objective, execution-trace-grounded quality assurance.

## Cost & GPU Requirements

| Resource | Requirement |
|----------|-------------|
| **GPU** | **None required** — everything runs via API calls |
| **Cost per optimization run** | ~$2–10 |
| **Rollouts for major benchmarks** | 400–1,200 (vs 24,000+ for GRPO) |
| **Licensing** | MIT |

## ICLR 2026 Oral Paper

- **arXiv:** [2507.19457](https://arxiv.org/abs/2507.19457)
- **Title:** *GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning*
- **Venue:** ICLR 2026 (Oral), presented April 24, 2026 — Oral Session 3A: Agents
- **Primary Area:** Foundation or frontier models, including LLMs
- **Keywords:** prompt optimization, natural language reflection, evolutionary algorithms, Pareto front
- **Key results:** +6% average over GRPO across 6 tasks (HotpotQA, AIME, LiveBench-Math, IFBench, and more), +12% on AIME-2025 over MIPROv2, 35× fewer rollouts
- **Code:** https://github.com/gepa-ai/gepa

## Ecosystem Adoption

Used in production by Shopify, Databricks, Dropbox, Pydantic, Nous Research, OpenAI, and others. Integrated into DSPy as `dspy.GEPA` and available standalone via `pip install gepa`.

## See Also

- [[hermes-agent]] — The agent framework GEPA optimizes skills for
- [[nous-research]] — Creator of Hermes Agent and the self-evolution companion repo
- [[agent-skills]] — The skill files GEPA optimizes: Markdown playbooks with YAML frontmatter
- [[concepts/dspy]] — DSPy framework with built-in GEPA optimizer (`dspy.GEPA`)
- [[entities/omar-khattab]] — Lead author and principal investigator
