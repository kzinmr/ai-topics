---
title: "Reasoning models from scratch (Raschka video course)"
created: 2026-10-30
updated: 2026-10-30
type: concept
tags:
  - reasoning
  - reasoning-model
  - education
  - ml-education
  - post-training
  - reinforcement-learning
  - test-time-scaling
  - pytorch
  - developer-tooling
sources:
  - raw/articles/magazine.sebastianraschka.com--p-building-reasoning-models--9e41ab02.md
related:
  - concepts/reasoning-models
  - concepts/post-training/rlvr
  - concepts/test-time-scaling
  - concepts/model-distillation
  - concepts/agent-harnesses
confidence: high
---

# Reasoning models from scratch (Raschka video course)

On 2026-10-24 Sebastian Raschka published **"Building Reasoning Models from the
Ground Up"**, an eight-video / **11+ hour** implementation course that takes a
pre-trained small LLM and adds reasoning capability in Python and PyTorch. It is the
video companion to his July 2026 book *Build a Reasoning Model (From Scratch)*
(~440 pages, Manning) and the sequel to his "Coding LLMs from the Ground Up" course.

Source: [magazine.sebastianraschka.com/p/building-reasoning-models](../raw/articles/magazine.sebastianraschka.com--p-building-reasoning-models--9e41ab02.md)
(HN: **854 points / 116 comments**, 2026-10-26 — a low-drama, high-signal thread).

## Scope and method

- Starts from a **pre-trained small Qwen3 model** rather than pretraining from zero —
  an explicit scoping decision so that effort goes to the four interesting stages:
  **evaluation, inference-time scaling, reinforcement learning, and distillation**.
- Implementation-only pedagogy. Raschka's stated rationale: reimplementing is "still
  the best way to understand and learn how things really work." This matches his
  published methodology of validating understanding by reimplementation and matching
  intermediate tensors against published weights.
- **Prerequisites**: comfortable with Python and PyTorch. The earlier
  *Build a Large Language Model (From Scratch)* material is recommended but not
  required — the reasoning materials are standalone.
- **Compute**: early text-generation and evaluation examples run on CPU; training
  experiments realistically need a GPU. Video 1 covers environment setup (uv for
  dependencies), CUDA vs Apple Silicon checks, and remote-GPU-via-VS-Code workflows.
- Recommended study loop: read a book chapter → code along with the matching video →
  do the exercises. A separate ~90-minute LinkedIn Learning course covers the concepts
  without implementations, positioned as an optional preview.

## The LLM → reasoning model → agent harness taxonomy

The most wiki-relevant content is a definitional section Raschka added because he is
"often asked how reasoning models relate to today's AI agents." It is a clean,
three-layer decomposition worth adopting as vocabulary:

| Layer | Definition | Role |
|---|---|---|
| **Conventional LLM** | base pretrained model | baseline |
| **Reasoning model** | "an upgrade from a conventional LLM, that is, adding more post-training via **reinforcement learning with verifiable rewards** (and optionally **inference scaling** techniques)" to solve harder problems | the **engine** |
| **Agent harness** | "a software or tooling framework around the LLM/reasoning model" whose task is "sophisticated context management and giving the LLM access to tools" | the **machinery** |

Three corollaries he states explicitly:

1. Reasoning models are classically built for **math and code**, but the capability
   "can generalize to other problem domains as well."
2. An agent may run on **either** a conventional LLM or a reasoning model, but
   reasoning models are "the more typical choice as they are more capable."
3. "Almost all current-generation LLMs today are reasoning models or offer a reasoning
   mode" — with variable reasoning-effort settings. This is why he considers the topic
   "still as relevant as ever" rather than a solved 2024 curiosity.

The engine/machinery analogy is drawn from his own *Components of a Coding Agent*
article. It is a useful complement to [[concepts/agent-harnesses]], which tends to
catalog harness components; this framing keeps the training-side
([[concepts/post-training/rlvr]], [[concepts/test-time-scaling]],
[[concepts/model-distillation]]) and harness-side concerns from being conflated. His
bottom line: "reasoning models, as the 'engine,' remain an important part of
understanding modern LLM agents."

## Video inventory

1. Motivation and code setup — LLM/reasoning-model/agent relationship, why learn by
   implementing, dependencies, hardware choice, remote GPU troubleshooting
2. Loading a base model, text generation, and **KV caching**
3.–8. Evaluation, inference-time scaling, reinforcement learning, and distillation
   stages (with the book as companion)

## Why this belongs in the wiki

- It is a **rare end-to-end open implementation path** for RLVR + inference scaling +
  distillation on a small model, which are otherwise mostly frontier-lab-internal
  techniques. It lowers the cost of the "understand the engine" tier of
  [[concepts/reasoning-models]].
- Reception signal: 854 HN points with only 116 comments — agreement/interest rather
  than dispute, which is Raschka's usual profile (compare his book launch coverage in
  [[entities/sebastian-raschka]]).
- The three-layer taxonomy is reusable vocabulary for onboarding and for
  distinguishing harness-level from model-level improvements in eval discussions
  (cf. [[concepts/coding-agents/evaluation-coding-agents]]).

## Limits

- It is an educational artifact, not new research: the methods (RLVR, best-of-n /
  inference scaling, distillation) are established; the contribution is
  implementation accessibility.
- Paid/commercial material (Manning book, Substack, LinkedIn Learning) — the course is
  not free, so "open implementation path" here means *personally reproducible*, not
  libre-licensed content.
- Single-author curriculum; no third-party assessment of learning outcomes.

## Related pages

- [[entities/sebastian-raschka]] — author
- [[concepts/reasoning-models]]
- [[concepts/post-training/rlvr]]
- [[concepts/test-time-scaling]] · [[concepts/inference-time-scaling]]
- [[concepts/model-distillation]]
- [[concepts/agent-harnesses]]
- [[concepts/kv-cache]]
- [[concepts/genai-handbook]]
