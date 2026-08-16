---
title: "LittleLearner"
type: concept
created: 2026-08-16
updated: 2026-08-16
tags:
  - training
  - pretraining
  - datasets
  - curriculum
  - small-language-model
  - distillation
  - grpo
  - benchmark
  - interpretability
sources:
  - raw/articles/2026-08-13_littlelearner_curriculum-exposure.md
  - https://littlelearner-ll.github.io/
  - https://arxiv.org/abs/2608.13545
related:
  - concepts/scaling-laws
  - concepts/post-training/grpo
  - concepts/fineweb
  - concepts/synthetic-data
---

# LittleLearner

**LittleLearner** is a controlled-sandbox research project studying whether language models *acquire* new capabilities or merely *elicit* capabilities already present in their training data. It trains models from scratch on a corpus restricted to the U.S. elementary-school curriculum (K–5), then tests whether scaling, post-training, and in-context learning can push the models past that curriculum. The headline finding is **"elicitation, not acquisition"**: the pretraining filter sets the effective capability ceiling.

Introduced August 13, 2026 by Fanfei Li, Jana Zeller, Manuel Prada-Corral, Thaddäus Wiedemer, Prasanna Mayilvahanan, Ryan Cotterell, and Wieland Brendel ([arXiv:2608.13545](https://arxiv.org/abs/2608.13545)). A hosted 5B model is available to chat with live in the browser.

## Motivation

Modern LMs are trained on "everything at once," making it hard to tell whether a newly observed skill was **learned** during training or merely **elicited** from latent knowledge. LittleLearner resolves this by constraining the training distribution itself: an 88B-token corpus filtered to the K–5 curriculum, with models trained from scratch on it and matched *unfiltered* controls for clean comparison. Because the knowledge boundary is under experimental control, the question "can standard interventions push a model past what its pretraining data taught it?" can be asked cleanly.

## LittleCurriculum (Dataset)

An **88B-token corpus distilled from [[concepts/fineweb|FineWeb-Edu]]** through a five-stage filtering pipeline aligned with the Common Core K–5 standards. Concepts, facts, and vocabulary taught above Grade 5 are explicitly excluded.

## Models

Three scales — **0.6B / 1.3B / 5B** — trained from scratch on LittleCurriculum, each shipped with a **matched Unfiltered control** sharing its architecture, tokens, and recipe. Variants include:

- **Base**: the pretrained model.
- **GRPO**: math specialists post-trained on MathCAMPS (may skew toward math-oriented output).
- **Chatty**: variants tuned for general chat.

## Findings

Each intervention amplifies **in-scope** (within-curriculum) ability; none of them meaningfully improves **out-of-scope** (beyond-K–5) performance.

- **Scaling**: increasing model size improves performance within the controlled knowledge exposure and extends modestly along the same learning trajectory, but yields little improvement on problems requiring more advanced capabilities outside the exposure.
- **Post-training**: GRPO post-training significantly boosts in-scope K–5 capabilities but fails to recover out-of-scope capabilities, *even when training with out-of-scope data*.
- **In-context learning**: with the prompts tested, in-context learning does not unlock new reasoning capabilities in beyond-K–5 tasks.

The practical upshot: these interventions act as **amplifiers of the curriculum**, not as a bridge across the capability boundary set by pretraining. This gives empirical support to the view that the pretraining distribution — not post-training or prompting — is the primary determinant of a model's capability ceiling, with direct implications for [[concepts/scaling-laws|scaling]] and data-curation strategy.

## Related Pages

- [[concepts/scaling-laws]] — Scaling behavior and its limits
- [[concepts/post-training/grpo]] — GRPO, the post-training algorithm used here
- [[concepts/fineweb]] — FineWeb-Edu, the source corpus for LittleCurriculum
- [[concepts/synthetic-data]] — Data curation and filtering for pretraining
