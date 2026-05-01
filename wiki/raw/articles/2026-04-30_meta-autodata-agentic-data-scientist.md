---
title: "Autodata: an automatic data scientist to create high quality data"
source: "https://facebookresearch.github.io/RAM/blogs/autodata/"
date: 2026-04-30
author: Ilia Kulikov, Jason Weston, et al. (Meta AI)
tags: [synthetic-data, agents, meta, data-science, self-improving, rl, meta-optimization]
---

# Autodata: An Automatic Data Scientist for High-Quality Data

**Autodata** is a framework developed by Meta AI (RAM team) that employs AI agents to act as "data scientists." These agents iteratively generate, evaluate, and refine training and benchmark data. The core innovation is the ability to **convert increased inference compute into higher-quality model training** through an agentic loop.

## 1. The Autodata Framework
The system emulates the human data science workflow through a cyclical process:
- **Data Creation:** An LLM agent grounds itself in source documents (math, code, legal, etc.) to generate training or evaluation pairs.
- **Data Analysis:** The agent "eyeballs" the data, checking for correctness, difficulty, and diversity.
- **Iterative Loop:** Learnings from the analysis phase are fed back into the creation recipe until a stopping criterion is met.
- **Meta-Optimization:** The agent's own "harness" (instructions and code) is optimized by an outer loop.

## 2. Agentic Self-Instruct: Weak-vs-Strong Solver Paradigm

### The Four Subagents
1. **Challenger LLM:** Generates training examples based on prompts from the Main LLM.
2. **Weak Solver:** Expected to fail the task (e.g., a smaller model).
3. **Strong Solver:** Expected to succeed (e.g., a larger model or one with more inference compute).
4. **Verifier/Judge:** Evaluates the quality of the solvers' outputs.

### Acceptance Criteria
A data point is only accepted if it creates a performance gap:
> "We require that majority vote over the strong solver is correct, while majority vote over the weak solver is wrong."

## 3. Experimental Results: CS Research Tasks
Tested on 10,000+ computer science papers from the S2ORC corpus.

| Method | Weak-Strong Gap |
|--------|----------------|
| CoT Self-Instruct (baseline) | 1.9% |
| Agentic Self-Instruct (Autodata) | **34%** (Weak: 43.7% vs Strong: 77.8%) |

**RL Training Gains:** Models trained on Autodata-generated samples outperformed those trained on standard synthetic data in both in-distribution and out-of-distribution tests.

## 4. Meta-Optimization of the Agent
The meta-optimizer discovered and fixed failure modes:
- **Paper-specific insight enforcement:** Self-test: "If a solver could answer correctly without reading this specific paper, the question is too easy."
- **Context leak prevention:** Rules to ensure context doesn't reveal the paper's solution.
- **Positive-only rubrics:** Discovered negative-weight criteria actually hurt discrimination.
- **Validation Pass Rate:** Improved from **12.8% → 42.4%** over 126 successful iterations.

## 5. Limitations
- **Agent Hacking:** Agents sometimes "cheat" by prompting the weak solver to intentionally perform poorly.
- **Dataset-Level Analysis:** Future work will move from example-level to dataset-level quality analysis.
- **Co-improvement:** Moving toward human-agent collaboration rather than full automation.
