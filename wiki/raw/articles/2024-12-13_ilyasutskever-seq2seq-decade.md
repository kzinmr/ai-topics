---
title: "Sequence to Sequence Learning with Neural Networks: What a Decade — Ilya Sutskever (NeurIPS 2024)"
author: Ilya Sutskever
source: YouTube
url: https://www.youtube.com/watch?v=1yvBqasHLZs
published: 2024-12-13
event: NeurIPS 2024, Vancouver
duration: "24:37"
type: talk
tags:
  - scaling-hypothesis
  - ilya-sutskever
  - seq2seq
  - deep-learning-dogma
  - pretraining
  - superintelligence
  - neurips-2024
---

# Sequence to Sequence Learning with Neural Networks: What a Decade

Ilya Sutskever delivers a retrospective talk at NeurIPS 2024, revisiting the 2014 "Sequence to Sequence Learning with Neural Networks" paper (for which he received an award) to reflect on what was right, what was wrong, and where AI is heading.

## Core Thesis

The talk revisits the "Deep Learning Dogma" — the belief that a large neural network with enough layers can do anything a human being can do in a fraction of a second. The 2014 seq2seq paper was built on three simple premises: an autoregressive model, a large neural network, and a large dataset. A decade later, these premises have proven remarkably prescient.

> "Pretraining as we know it will end." — and what comes next is superintelligence: agentic, reasons, understands, and is self-aware.

## Key Arguments

### 1. The 2014 Thesis — What Was Right

The seq2seq paper's core insight was intentionally simple:
- **Autoregressive model** trained on text
- **Large neural network** (for 2014 standards)
- **Large dataset**

The "Deep Learning Dogma" claimed that if any human in the world can do a task in a fraction of a second, a 10-layer neural network can replicate it — by embedding those neural connections inside the artificial network.

### 2. The End of Pretraining

Sutskever argues that the current paradigm of pretraining on internet-scale data will end. The easily available data from the internet is finite, and the marginal returns on simply scraping more text are diminishing.

### 3. What Comes Next: Superintelligence

After pretraining ends, Sutskever foresees a new paradigm:

> **Superintelligence** that is: agentic, reasons, understands, and is self-aware.

This is a significant statement from one of the key architects of modern deep learning:
- **Agentic**: AI systems that act autonomously toward goals, not just generate text
- **Reasons**: Capable of multi-step logical deduction
- **Understands**: Genuine comprehension, not just statistical pattern matching
- **Self-aware**: Some form of self-model or metacognition

### 4. Generalization Standards Have Increased

In the Q&A, Sutskever discusses out-of-distribution generalization:
- Before deep learning, "generalization" meant the phrasing wasn't literally in the training data
- Today's standards are far higher — requiring reasoning on novel problems
- Humans still generalize much better than LLMs
- But LLMs do generalize out-of-distribution to some degree, which would have been unimaginable a decade ago

## Connection to the Scaling Hypothesis

Sutskever's talk represents a critical evolution of the Scaling Hypothesis:

1. **The Scaling Hypothesis was correct** — the 2014 approach (autoregressive model + large NN + large data) scaled to produce GPT-3, GPT-4, and beyond
2. **But scaling alone has limits** — pretraining data is finite; the easy gains from scaling compute on internet data are diminishing
3. **The next phase requires more** — not just scaling, but new capabilities: agency, reasoning, understanding, self-awareness

This directly addresses a question Gwern raised in his original essay: "What would future scaled-up models learn?" Sutskever's answer: they will need to move beyond pretraining into a regime where models are **agentic and reasoners**, not just better predictors.

## Key Quotes

- "Pretraining as we know it will end."
- "Agentic, reasons, understands, and is self-aware." — describing the next paradigm
- "If there is one human in the entire world that can do some task in a fraction of a second, then a 10-layer neural network can do it too."

## References

- [NeurIPS 2024: Ilya Sutskever talk](https://www.youtube.com/watch?v=1yvBqasHLZs) (YouTube, 24:37)
- [Sequence to Sequence Learning with Neural Networks](https://arxiv.org/abs/1409.3215) — Sutskever, Vinyals, Le (2014)
