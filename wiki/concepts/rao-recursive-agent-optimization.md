---
title: "RAO (Recursive Agent Optimization)"
type: concept
aliases: ["Recursive Agent Optimization", "RAO"]
created: 2026-05-11
updated: 2026-05-11
status: L2
tags:
  - ai-agents
  - reinforcement-learning
  - inference
  - optimization
  - multi-agent
  - training
sources:
  - "[[papers/2026-05-07_2605.06639_recursive-agent-optimization]]"
  - "[[articles/2026-05-08_x-thread_apurva-gandhi-rao-recursive-agent-optimization]]"
related:
  - "[[concepts/recursive-language-models]]"
  - "[[concepts/rlm-recursive-language-models]]"
  - "[[concepts/post-training/grpo]]"
  - "[[entities/apurva-gandhi]]"
---

# RAO (Recursive Agent Optimization)

**RAO (Recursive Agent Optimization)** is a method that trains LLM agents via end-to-end reinforcement learning to recursively spawn copies of themselves for delegating and coordinating subtasks. A joint research project from CMU and Amazon AGI Labs (May 2026).

## Overview

Most existing multi-agent and recursive agent systems are merely pre-trained models wrapped in inference-time scaffolds. RAO reverses this idea, training **the model itself for recursive reasoning**.

The "recursive agent" trained by RAO can:
- Spawn sub-agents and delegate parts of tasks to them
- Delegated sub-agents can themselves delegate further (deep recursion)
- Independent subtasks can be **executed in parallel**
- The same single policy operates on all nodes of the execution tree

## Core Mechanism

### Execution Tree

RAO rollouts produce dynamically generated recursive execution trees. Each node corresponds to one agent instance executing the following cycle:

```
Root Agent (depth=0)
├── Sub-Agent A (depth=1)
│   └── Sub-Agent A1 (depth=2)
└── Sub-Agent B (depth=1) ← can run in parallel with A
```

### Training Objective

The RAO training objective can be viewed as a multi-task objective across **tasks sampled from different levels** of the recursive rollout tree. Deeper-level tasks tend to be simpler subproblems of parent tasks, creating a natural curriculum learning effect.

### Credit Assignment

RAO leverages the recursive rollout structure to provide **structured dense credit assignment** for each subtask trajectory:
- Uses environmental feedback as rewards when available
- Generates rewards via **LLM-judge proxy** when unavailable
- Each node's agent receives rewards for both its own subtask success and its global contribution to the root task

## Experimental Results

### Main Benchmarks
| Metric | Result |
|------|------|
| Model | Qwen3-4B-Instruct |
| Training Steps | **75 steps** |
| Task | Deep Research |
| vs Single-Agent Baseline | **+16% SR** (Success Rate) |

### Generalization
- Scales to tasks beyond the model's context window
- Generalizes to **much harder tasks** than those seen during training
- **Adaptively adjusts inference compute** based on problem difficulty (harder problems reach deeper recursion depths)

### Efficiency
- Reduces wall-clock time compared to single-agent (due to parallel execution)
- Improved training efficiency (via dense credit assignment)

## Relationship to RLM

RAO's agent harness implementation is similar to **Recursive Language Models (RLMs)** by Zhang et al. (2025), but with these key differences:

| Aspect | RLM (Zhang 2025) | RAO (Gandhi 2026) |
|------|-----------------|-------------------|
| Recursion Depth | Limited to depth=1 (Wang 2026) | Positive results at depth > 1 |
| Parallel Execution | Sequential | Supports **asynchronous parallel execution** |
| Training Target | Language model layer recursion | Agent delegation and coordination behavior |

## Relationship to Sub-Agent / Agent Harness

RAO provides an approach that trains **the model itself for sub-agent usage**, as opposed to methods like Claude Code, Codex CLI, and OpenCode that use sub-agents as inference-time scaffolds. In the context of the Harness Effect (5-40pp performance difference from different harnesses on the same model), RAO may bridge this gap by teaching the model how to use the harness directly.

## Project Info

- **Paper**: [arXiv:2605.06639](https://arxiv.org/abs/2605.06639)
- **Project Page**: https://apga.github.io/RAO
- **Code**: Coming soon
- **Authors**: Apurva Gandhi, Satyaki Chakraborty, Xiangjun Wang, Aviral Kumar, Graham Neubig

## Future Directions

- Evaluate the harness effect of RAO-trained models in real agent harnesses (Claude Code, Codex CLI, etc.)
- Scaling to larger models (Qwen3-4B → 32B/72B)
- Evaluation on real-world tasks (SWE-bench, TheAgentCompany)
- Stability and control at deep recursion depths
