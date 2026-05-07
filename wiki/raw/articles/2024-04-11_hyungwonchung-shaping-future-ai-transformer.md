---
title: "Shaping the Future of AI from the History of Transformer — Hyung Won Chung (Stanford CS25)"
author: Hyung Won Chung (@hwchung27)
source: YouTube / Google Slides
url: https://www.youtube.com/watch?v=orDKvo8h71o
slides: https://docs.google.com/presentation/d/1u05yQQaw4QXLVYGLI6o3YoFHv6eC3YN8GvWD8JMumpE
published: 2024-04-11
uploaded: 2024-06-11
event: Stanford CS25 — Transformers United, Spring 2024
duration: "36:30"
type: talk
tags:
  - scaling-hypothesis
  - bitter-lesson
  - transformer-architecture
  - encoder-decoder
  - decoder-only
  - hyung-won-chung
  - instruction-finetuning
  - flan
---

# Shaping the Future of AI from the History of Transformer

Hyung Won Chung (OpenAI) delivers a talk at Stanford CS25 on April 11, 2024, arguing that understanding the *change itself* — specifically the driving force of exponentially cheaper compute and scaling — is the key to predicting the future of AI.

## Core Thesis

Instead of chasing every new AI development, researchers should study the **dominant driving force** behind change: exponentially cheaper compute and associated scaling. The history of Transformer architectures is a journey of **removing human-imposed structure** (inductive biases) in favor of more general methods that can leverage massive scale.

> "Compute is getting cheaper faster than we are becoming better researchers."

## Key Arguments

### 1. The Structure Paradox

Adding structure (inductive biases) improves performance at low compute levels, but these structures become limitations that hinder scaling later. The actionable advice: "Adding optimal inductive bias for a given level of compute is critical. These are shortcuts that will hinder further scaling later on. **Remove them later.**"

### 2. Transformer Evolution = Structural Simplification

| Architecture | Structure Level | Era | Limitation |
|---|---|---|---|
| Encoder-Decoder (T5) | Highest | 2017-2021 | Separate parameters for input/target; information bottleneck |
| Encoder-Only (BERT) | Medium | 2018-2022 | Cannot generate; task-specific heads |
| Decoder-Only (GPT) | Lowest | 2020–present | Initially underperformed on benchmarks |

### 3. Three Structures Being Removed

**A. Separate Parameters for Input and Target**
- Originated from machine translation (2017) where input/target were different languages
- Modern LMs learn *world knowledge*, not just language — sharing parameters across input/target lets models combine knowledge across languages
- Encoder-Decoder models perform better on academic benchmarks because those datasets have long inputs and short targets — this is a "task-specific shortcut"

**B. The Information Bottleneck**
- Encoder-Decoder: decoder attends only to the final encoder layer
- Different layers encode different granularities — restricting to the final layer loses information
- Decoder-only models allow layer-to-layer interaction (layer $l$ attends to layer $l$)

**C. Bidirectionality vs. Causality**
- At sufficient scale, bidirectional attention doesn't provide significant performance edge
- Bidirectionality creates an engineering challenge for multi-turn chat — every new turn requires re-encoding the entire conversation
- Unidirectional (causal) attention enables KV caching — only the newly added message needs encoding

### 4. Case Study: Instruction Finetuning (Flan)

In "Scaling Instruction-Finetuned Language Models" (2022), Encoder-Decoder models showed larger gains on academic datasets. However, this was because academic datasets have long inputs and short targets — a distribution that favors separate encoder-decoder parameters.

### 5. Prediction Framework

> "What is better in the long term almost always looks worse now."

To predict where AI is heading: identify where we are still imposing human "logic" on models and expect those structures to be replaced by more general, compute-intensive methods.

## Key Quotes

- "Compute is getting cheaper faster than we are becoming better researchers."
- "If clever modeling techniques and fancy math were the driving force, it would have been a completely different story."
- "Adding optimal inductive bias for a given level of compute... is critical. These are shortcuts that will hinder further scaling later on. Remove them later."
- "What is better in the long term almost always looks worse now."

## Connection to Wiki Concepts

- [[concepts/scaling-hypothesis]] — Direct application of scaling hypothesis to architecture design
- [[concepts/bitter-lesson-harnessing]] — Sutton's Bitter Lesson as the philosophical foundation
- [[concepts/scaling-laws]] — Why architecture choices change as compute scales
- [[entities/gwern]] — Gwern's Scaling Hypothesis essay provides the theoretical framing for why Chung's observations hold

## References

- [Stanford CS25 Lecture: Hyung Won Chung](https://www.youtube.com/watch?v=orDKvo8h71o) (YouTube, 36:30)
- [Google Slides](https://docs.google.com/presentation/d/1u05yQQaw4QXLVYGLI6o3YoFHv6eC3YN8GvWD8JMumpE)
- [Scaling Instruction-Finetuned Language Models (Flan)](https://arxiv.org/abs/2210.11416) — Chung et al., 2022
- [The Bitter Lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) — Rich Sutton, 2019
