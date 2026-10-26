---
title: "micrograd"
type: concept
aliases:
  - micrograd
created: 2026-04-25
updated: 2026-10-26
tags:
  - concept
  - education
  - deep-learning
  - open-source
related:
  - "[[entities/andrej-karpathy]]"
  - "[[entities/karpathy-projects]]"
  - "[[concepts/nanogpt]]"
sources:
  - https://github.com/karpathy/micrograd
---

# micrograd

**micrograd** is Andrej Karpathy's tiny auto-differentiation engine and backpropagation teaching library — ~150 lines of pure Python implementing a scalar-value computational graph (`Value`) with reverse-mode autodiff, plus `nn`-style Module/Parameter abstractions. Released March 2020 as the practical companion to his "Neural Networks: Zero to Hero" video series.

## What It Is

- **`Value` node**: wraps a number + `grad` + list of parents; `backward()` performs topologically-ordered reverse-mode autodiff via chain rule.
- **`Module`/`Param`**: minimal layer abstraction (Linear, MLP) mirroring PyTorch's API.
- **Curriculum context**: built live on video, then extended into makemore (bigram → MLP word models) → [[concepts/nanogpt]] → llm.c → microgpt. micrograd is step one: *no PyTorch, no tensors, just scalars* — so every gradient is hand-checkable.

## Why It Matters

- **Canonical "build autodiff yourself" exercise.** Reading micrograd is the accepted rite of passage for understanding what frameworks do under the hood; "implement micrograd from memory" is a common ML interview probe.
- **Scalar simplicity as pedagogy.** Restricting to scalars removes broadcasting/tensor-shape noise, isolating the conceptual core: the chain rule over a DAG.
- **Karpathy's teaching philosophy in miniature**: "what I cannot create, I do not understand" (Feynman) — each successor project strips one more abstraction layer.

## Usage Sketch

```python
from micrograd.engine import Value
a = Value(2.0, requires_grad=True)
b = Value(-3.0, requires_grad=True)
c = (a * b) + a   # forward
c.backward()      # reverse-mode autodiff fills a.grad, b.grad
```

## Related Concepts

- [[entities/andrej-karpathy]] — author
- [[entities/karpathy-projects]] — project timeline
- [[concepts/nanogpt]] — the culmination of the Zero-to-Hero progression
- [[concepts/tinygrad]] — Hotz's ~1000-line tensor library often compared with micrograd (tensors vs scalars)

## Sources

- [karpathy/micrograd on GitHub](https://github.com/karpathy/micrograd)
- [Neural Networks: Zero to Hero (YouTube series)](https://www.youtube.com/playlist?list=PLA89dcF4L7ATjLpFDcIZN3mMJLrK609EN)
