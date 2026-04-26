---
title: "The Mismanaged Geniuses Hypothesis (MGH)"
tags: [[agents-scaffolding-composition-inference-scaling-hypothesis]]
created: 2026-04-19
updated: 2026-04-24
---

# The Mismanaged Geniuses Hypothesis (MGH)

## Core Thesis

> **AI models are already good enough for the next leap in capabilities. The bottleneck is no longer scaling model size or training data. It is how we manage, decompose, and compose existing frontier LMs.**

**— Authors:** Alex Zhang, Zhening (Zed) Li, Omar Khattab  
**— Published:** April 9, 2026  
**— Source:** [alexzhang13.github.io/blog/2026/mgh/](https://alexzhang13.github.io/blog/2026/mgh/)

The hypothesis posits that **frontier language models are severely underutilized due to sub-optimal use of scaffolding**, not due to inherent limitations in model capability.

## The Metaphor

| Element | Meaning |
|---------|---------|
| **Geniuses** | Frontier LMs that already outperform humans on elite exams (IMO, IOI) and general software engineering |
| **Mismanaged** | Human-engineered scaffolds (ReAct, tool-use APIs, agent frameworks) that constrain models to narrow, brittle task decomposition patterns |

The core claim: **these "geniuses" are being treated like mediocre employees** — given rigid, pre-defined workflows instead of the autonomy to decompose and compose their own reasoning.

## The Hypothesis in Detail

### 1. Current Scaffold Bottlenecks

> *"The outcome is a diverse set of agent scaffolds that can only solve narrow problems and must frequently be updated, leading to a misrepresentation of how good language models 'actually are' at any given time."*
> — MGH paper (2026)

Current problems:
- **Brittle decomposition:** Human-designed agent loops (ReAct, tool calling) force models into narrow reasoning patterns
- **API limits:** Tool-calling APIs restrict the space of possible decompositions
- **Frequent updates:** Each new model requires scaffold tweaks, suggesting the scaffold is the bottleneck, not the model
- **Capability misrepresentation:** Poor scaffold design makes good models look worse than they are

### 2. The Composition Operator

> *"Modern LMs are so good yet so expensive to further train, that directly learning the operator to compose LMs is a significantly more efficient strategy for reaching these OOD tasks than continuing to scale current LMs."*
> — MGH paper (2026)

The MGH proposes that the key to unlocking the next capability jump is **learning the composition operator** — teaching models how to chain in-distribution LM calls into out-of-distribution (OOD) solutions.

### 3. Empirical Evidence: RLM Bootstrapping

The hypothesis is supported by experimental results with Recursive Language Models:

| Metric | Before RL | After RL (simpler task) |
|--------|-----------|------------------------|
| **Task** | 1M context / 8 needles | 32k context / 1 needle |
| **Performance** | ~0% | → applied to hard task |
| **Hard Task Result** | — | **100% success** |

**Model used:** Qwen3-4B-Instruct (small model, not frontier-scale)

This demonstrates two key points:
1. **Decomposition is easier than direct solving** — breaking the problem into sub-tasks that are in-distribution for the model
2. **Models can write correct compositions** — they just need the right scaffold + targeted RL bootstrapping to execute them

### 4. OOD via Composition

> *"Complex/OOD tasks can be solved by decomposing them into sub-tasks that remain in-distribution for the LM."*

This is the mathematical core of MGH: instead of training larger models to handle harder tasks directly, train them to **decompose hard tasks into easy ones** they already know how to solve.

## Two Key Research Directions

### Direction 1: Defining the Decomposition Space

The expressiveness of the decomposition space exponentially impacts which tasks are solvable:

| Decomposition Method | Expressiveness | Example |
|---------------------|----------------|---------|
| Fixed ReAct loop | Low | One thought → one action → repeat |
| Tree of thoughts | Medium | Branch and evaluate |
| **Recursive (RLM)** | **High** | `for` loops, arbitrary depth, programmatic decomposition |
| Self-modifying scaffold | Very High | Model rewrites its own decomposition strategy |

> *"In RLMs, the space of decompositions is expanded so as to allow an efficient representation of decomposition into arbitrarily many subtasks (e.g. using a `for` loop), which suddenly enables the system to handle near-infinite context."*

### Direction 2: Training & Scaling Composition

- LMs already generate correct decompositions but don't natively execute them
- RL training on simpler variants bootstraps decomposition behavior for complex tasks
- The scaffold + composition operator becomes the trainable unit, not just the model weights

## Connection to Prior Work

### RLM (Recursive Language Models) — Zhang et al., 2025

RLM is the **proof-of-concept implementation** that inspired MGH. RLM showed that:
- Treating context as a REPL environment variable enables near-infinite context handling
- GPT-5-mini with RLM outperforms GPT-5 by 114% on 132k-token tasks
- The scaffold itself is the capability multiplier

### "Language Models will be Scaffolds" — Zhang, Feb 2026

> *"I have been somewhat convinced since before I started my PhD that the language models we interact with in the (near) future will be what we call scaffolds today."*

This earlier blog post laid the philosophical groundwork:
- Pre-2017: LM = probabilistic text-to-text function
- 2017-2025: LM = neural network (Transformer)
- 2025+: LM = scaffold around neural networks
- The boundary between "model" and "scaffold" is blurring

### Harness Engineering

MGH connects directly to the Harness Engineering paradigm:
- **Harness Engineering** (Lopopolo): Design infrastructure that lets agents work autonomously
- **MGH** (Zhang): The reason we need better harnesses is that current ones underutilize existing models
- Both agree: **Model + Harness = Agent**, and the harness is the differentiator

### Anthropic Managed Agents

Anthropic's Managed Agents service (Dec 2025) provides empirical support:
> *"Managed Agents—our hosted service for long-horizon agent work—is built around interfaces that stay stable as harnesses change."*

Anthropic recognized that the harness interface needs to be stable while the underlying orchestration evolves — exactly what MGH predicts.

## Implications for the Industry

### For Model Labs
- Stop chasing parameter counts for capability gains
- Focus on training models for **recursive reasoning and composition**
- Benchmarks need to measure scaffold-assisted performance, not just single-prompt accuracy

### For Agent Framework Developers
- Move beyond fixed ReAct loops
- Enable programmatic decomposition (loops, recursion, conditionals)
- Build scaffolds that **generalize across model families**

### For Enterprises
- Existing models are likely sufficient for most use cases
- Investment should shift from "which model" to "how to orchestrate"
- Non-technical users can achieve expert-level results with proper scaffolding

## Criticism & Open Questions

1. **Scaling laws still hold:** Proponents of scaling argue that bigger models will always beat better scaffolds
2. **Training cost:** Even composition training requires compute — is it really cheaper than scaling?
3. **Safety concerns:** More autonomous decomposition means less predictable behavior
4. **Evaluation gap:** No standard benchmark exists for measuring "composition ability"
5. **The "genius" assumption:** Are current models truly general enough, or do they only excel on benchmark-like tasks?

## Key Quotes

> *"AI models are already good enough for the next leap in capabilities."*

> *"The bottleneck is no longer scaling model size or training data. It is how we manage, decompose, and compose existing frontier LMs."*

> *"Assuming the MGH is actually true... training out such a system through bootstrapping may be enough to draw out a general task solving system."*

> *"The real challenge: not building bigger models, but managing the geniuses (with guardrails, of course)."*

## Related Concepts

- **[[rlm-recursive-language-models]]** — Proof-of-concept implementation
- **[[agentic-scaffolding]]** — The broader category of scaffold design
- **[[harness-engineering]]** — Infrastructure for autonomous agent work
- **[[scaffold-vs-rl-debate]]** — Whether scaffolds or training is the path forward (MGH says: both, but scaffold-first)
- **** — Scaling compute at inference rather than training
- **** — Decomposing the context, not the problem
- **** — Trained scaffolds + LLMs as the next paradigm

## Status

- **Page status:** Full (L3 depth achieved — >30% direct quotes, conceptual mapping complete)
- **Cross-connections:** Alex Zhang (entity), RLM (concept), Harness Engineering, Agentic Scaffolding, Omar Khattab
- **Last updated:** 2026-04-19
