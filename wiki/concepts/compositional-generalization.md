---
title: "Compositional Generalization"
created: 2026-07-21
updated: 2026-07-21
type: concept
tags:
  - compositional-generalization
  - agent-harness
  - rlm
  - reinforcement-learning
  - scaling
  - harness-engineering
  - context-management
sources:
  - https://alexzhang13.github.io/blog/2026/harness/
  - https://alexzhang13.github.io/blog/2026/mgh/
  - raw/articles/2026-07-20_zhang-khattab_language-model-harnesses-compositional-generalizers.md
---

# Compositional Generalization

## TL;DR

**Compositional generalization** is the ability to solve unseen problems by composing familiar concepts and patterns. Zhang & Khattab (MIT CSAIL, 2026) argue this is the key meta-capability for scaling AI systems — without it, every new domain demands its own training data investment. The capacity for compositional generalization can live in the **harness** (the program between the LLM and the external world), not just in the neural network weights.

## Core Thesis

> "Unless our models compose the individual lessons they learn, scaling will have slower returns than it should, as every new domain will demand its own investment in the form of training data."
> — Zhang & Khattab, "Language model harnesses are compositional generalizers" (Jul 2026)

Modern post-training is a brute-force paradigm of curating ever more environments and ever longer training horizons. Transformers remain poor compositional generalizers — their narrow design space of differentiable neural operators (from the 2017 [[concepts/transformer-architecture|Transformer]] paper) misses something fundamental about encoding higher-level inductive biases.

## The Harness as Compositional Generalizer

### Definition: Harness

A **harness** $H: s \rightarrow a$ is the program that sits between the external world and the neural network. It decides how to encode the current state $s$ of the environment (which can be arbitrarily long and complex) into one or more inputs to the LLM and how to determine the next action.

Examples: [[concepts/dspy-rlm|RLM]], [[concepts/codeact|CodeAct]], [[entities/claude-code|Claude Code]], [[entities/codex|Codex]].

### Locally In-Distribution (LID) Observations

A good harness shapes each call to the underlying Transformer so that every observation is **locally in-distribution (LID)** — each individual LM call handles a prompt that is in-distribution with respect to its training data.

> "A good harness is a harness that *reduces unfamiliar problems to familiar ones* and *reduces complex problems to simple ones*."
> — Zhang & Khattab (2026)

**Why existing harnesses fail at LID:** Claude Code and Codex fundamentally rely on flooding the context window with interleaved task-specific information, tool call outputs, and reasoning that get continuously appended. This causes **[[concepts/context-rot|context rot]]** — bloated histories quickly fall out of the training distribution.

### Harness-Induced Equivalence Classes

A well-designed harness induces an equivalence relation $\sim_H$ over the set of all task states $\mathcal{T}$. Structurally similar tasks fall under the same equivalence class and produce similar token-level trajectories for the neural network. This is the formal mechanism enabling compositional generalization.

**Example:** BrowseComp-Plus and OOLONG are two different tasks, but an [[concepts/dspy-rlm|RLM]] harness can make them appear token-for-token identical on the root LM's context window by deferring task-specific queries to sub-calls and moving information through REPL variables.

## Experimental Evidence (Zhang & Khattab, Jul 2026)

### Length Generalization

Training an RLM exclusively on **short tasks** generalizes to held-out tasks **8–32x longer**, with roughly **10x the eval lift** over training the underlying Transformer directly.

**Benchmarks tested:**
- MRCRv2 (64k → 2M tokens)
- GraphWalks (<128K → >1M tokens)
- LongBenchPro (32k → 256k tokens)
- OOLONG (32k → 256k tokens)
- OOLONG-Pairs (8k → 146k output)
- Ada-LEval (8k → 128k tokens)

**Model:** Qwen3-30B-A3B-Instruct-2507. Training: 150 steps, batch size 64, Decoupled PPO with GRPO-like advantages + KL loss.

### Cross-Domain (Strategy) Generalization

Training on one domain transfers to other domains at a far better rate than vanilla Transformers. The RLM's eval lift matches or exceeds train lift on completely different domains that share latent decomposition structure.

### Trajectory Similarity

Eval trajectories from the RLM on unseen tasks are significantly closer to training trajectories (measured by edit distance, 3-gram containment, Jaccard similarity) than those of base Transformers. The RLM induces a **quotient set** $\mathcal{H}_i/Q$ over all trajectories, reducing similar tasks to the same token trajectory.

## Two Key Mechanisms

### 1. Context Offloading

Input-specific context is passed as a **symbolic variable** so the root LM call does not directly see it. Different problems appear similar at the first step.

*Limitation:* On its own, context offloading does not prevent environment feedback and sub-agent information from returning to the main context. Over long horizons, the main context becomes OOD.

### 2. Programmatic Sub-Agent Calling

Sub-agents and tools are treated as **functions in a code REPL**. The root LM selectively chooses information and passes it around via variables without ever seeing task-specific outputs directly. This is equally important as context offloading for abstracting task-specific information.

## Connection to the Mismanaged Geniuses Hypothesis (MGH)

The [[concepts/mismanaged-geniuses-hypothesis|MGH]] argues that tasks humans care about can almost always be decomposed into sub-tasks that are far simpler and not beyond current LMs. Compositional generalization is the mechanism that makes this decomposition practical — enabling the system's reachable task space to extend beyond its training set's direct coverage.

## Scaling Implications

> "Scaling data will remain the biggest driver of progress, but the machinery that we feed that data into and its inductive biases are what will determine the coefficients of that scaling."
> — Zhang & Khattab (2026)

The argument is NOT to impose problem-specific programmatic strategies (which would violate the [[concepts/bitter-lesson|Bitter Lesson]]). Instead: the harness architecture itself should be designed so that end-to-end RL training can discover generalizable decomposition strategies. The harness provides the **scalable inductive bias**; RL provides the learning signal.

## Related

- [[concepts/dspy-rlm]] — The RLM harness that demonstrates compositional generalization
- [[entities/omar-khattab/rlm]] — RLM as Khattab's research program
- [[entities/alex-zhang]] — First author
- [[concepts/mismanaged-geniuses-hypothesis]] — MGH thesis
- [[concepts/context-rot]] — Why naive harnesses fail
- [[concepts/bitter-lesson]] — Scaling vs. design tension
- [[entities/omar-khattab]] — Co-author
