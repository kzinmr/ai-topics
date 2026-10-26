---
title: "Software 2.0"
type: concept
aliases:
  - software-2.0
created: 2026-04-25
updated: 2026-10-26
tags:
  - concept
  - ai-industry
  - philosophy
  - deep-learning
  - software-engineering
related:
  - "[[entities/andrej-karpathy]]"
  - "[[concepts/probabilistic-era-software]]"
  - "[[concepts/bitter-lesson]]"
sources:
  - https://www.swyx.io/software-3-0
---

# Software 2.0

**Software 2.0** is Andrej Karpathy's 2017 thesis (published on Medium, later refined) that neural networks are not merely a tool *for* programming but a **new programming paradigm**: instead of humans writing explicit code (Software 1.0), they curate datasets and objective functions, and the network "compiles" the program by fitting weights.

## The Core Argument

- **Neural networks are programs.** A network's weights are its source code; gradient descent is the compiler; the dataset is the spec.
- **Two kinds of code.** 1.0 = hand-written, explicit, deterministic, debuggable (C++, Python). 2.0 = learned, differentiable, opaque, probabilistic — but superior wherever the task can be expressed as pattern recognition over data.
- **Where 2.0 wins:** perceptual/empirical tasks (vision, speech, translation, recommendation) and continuous control (Tesla Autopilot — Karpathy's motivating case, where camera→control code was progressively replaced by networks).
- **Where 1.0 persists:** explicit logic, state management, OS kernels, anything requiring guarantees. The "compiler gap": there is no 2.0 equivalent for many symbolic operations, so they remain hand-written.
- **New engineering disciplines.** 2.0 debugging = dataset surgery and loss inspection; 2.0 "code review" = data curation; failure modes include dataset poisoning and adversarial examples.

## Consequences Karpathy Predicted

1. Software 2.0 eats 1.0 from the edges (first vision/speech, then broader domains via transformers).
2. A few general-purpose networks (the "average" of many programs) displace many bespoke ones — foreshadowing foundation models.
3. Hardware co-design: the world adapts to GPUs/TPUs because 2.0 has one dominant compute pattern (dense matrix multiply).

## Lineage & Successors

- **Software 3.0** (Karpathy, 2025 "Software is changing" / YC AI Startup School): prompts in natural language as programs written to the LLM "computer"; the LLM as a new OS. Many treat 3.0 as a special case of 2.0 (LLMs being the ultimate Software 2.0 artifact). See [[entities/karpathy-ideas]].
- Related wiki framing: [[concepts/probabilistic-era-software]], [[concepts/bitter-lesson]] (the data/compute side of the same bet), [[concepts/agent-generated-software]].

## Graph Structure Query

```
[software-2.0] ──author──→ [entity: andrej-karpathy]
[software-2.0] ──followed-by──→ [concept: software-3.0]
[software-2.0] ──embodies──→ [concept: bitter-lesson]
[software-2.0] ──contrasts──→ [concept: software-engineering (1.0)]
```

## Sources

- Karpathy, *Software 2.0* (Nov 2017), Medium
- [[entities/andrej-karpathy]] — timeline entry and key-quotes section
