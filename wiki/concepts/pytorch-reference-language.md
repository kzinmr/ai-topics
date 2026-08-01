---
title: "PyTorch: A Reference Language"
created: 2026-08-01
updated: 2026-08-01
type: concept
tags: [pytorch, framework, model, training, verification, optimization]
sources:
  - raw/articles/2026-07-25_pytorch_reference-language.md
  - https://docs.pytorch.org/devlogs/compiler/2026-07-25-pytorch-a-reference-language/
  - HN discussion: 80 points
---

## Overview

In July 2026, PyTorch team member Edward Z. Yang proposed framing PyTorch as a **reference language** for ML computation — a dual-role perspective where PyTorch serves simultaneously as both the *reference implementation* (the clear, correct specification of what should be computed) and the *implementation language* (the production system that actually runs at scale). This framing addresses a growing tension in ML infrastructure: as kernel DSLs and coding agents increasingly take over the actual production implementation of training steps and operators, PyTorch's role shifts from being the execution engine to being the executable specification against which optimized implementations are verified.

The proposal positions PyTorch not as a framework being displaced by compilers, but as the lingua franca that binds reference implementations, optimized kernels, and verifiers into a coherent development workflow.

## What Makes a Reference Language?

A reference implementation is traditionally a simplified but complete version of a system that trades performance for clarity. A **reference language** is the fabric of APIs and conventions from which such implementations are cut. PyTorch naturally fits this definition — it is already called the lingua franca of modern deep learning.

However, three common objections arise:

1. **"Reference implementations aren't deployed to production, but I train with PyTorch."** The proposal resolves this by recognizing PyTorch's dual role: when scale is modest or the compiler is working well, the reference implementation *can* ship. At frontier scale, the reference implementation stands apart as a correctness oracle.

2. **"Everyone uses kernel DSLs — what is PyTorch's role beyond gluing kernels?"** Kernel authors already maintain PyTorch reference implementations alongside optimized kernels for numerical correctness verification. This pattern generalizes: the high-level API serves as the spec.

3. **"AI coding means any stack can be rewritten from scratch — why does PyTorch matter?"** The proposal argues coding agents change *how* production implementations are written, not *whether* a reference implementation is needed. The reference implementation becomes the ground truth.

## Implications for ML Compiler Design

This perspective implies a fundamental shift away from the **compiler-maximalist** view, which holds that end users should write high-level code (e.g., NumPy/PyTorch-style) and trust the compiler to produce optimal execution. For critical operations like matrix multiplies and attention, compilers struggle to guarantee peak performance, leading to the proliferation of kernel DSLs.

Instead of trying to make compilers smart enough to replace hand-written kernels, the reference language model embraces a **verify-don't-compile** paradigm:

1. Keep traditional PyTorch autograd-friendly code as the **reference implementation**.
2. Use coding agents (LLMs) to generate an explicit forward-backward version of the code as the **production implementation**, which can be optimized independently.
3. Apply a **verifier** that checks equivalence between reference and production — through bitwise tests, graph capture, or structural equivalence (in the tradition of translation validation).
4. When one side has a fusion the other doesn't, provide a reference implementation of the fusion as an inverse pattern match.

This recipe avoids the brittleness of compiler pattern matching on implicit backwards graphs, while preserving the correctness guarantee that autograd traditionally provided.

## Comparison to Other ML Frameworks (JAX, TensorFlow)

**JAX** takes a fundamentally compiler-centric approach: programs are expressed as pure functions and transformed via `jit`, `vmap`, `grad`, etc. JAX's functional purity and explicit PRNG make it naturally amenable to compiler optimization, but it does not embrace the dual-role reference/implementation split — the compiled form *is* the production form.

**TensorFlow** historically pursued the compiler-maximalist path through XLA and its graph-execution model. TF 2.x moved closer to eager execution (similar to PyTorch), but without the explicit reference-language framing.

The PyTorch reference language proposal is distinct in that it treats the *eager-mode program as the specification* and allows the production implementation to diverge arbitrarily, so long as it can be verified equivalent. This is a more flexible model than JAX's functional-transform approach or TensorFlow's graph-compilation approach — it gives developers full control over optimizations while maintaining correctness through verification rather than compilation guarantees.

## Relationship to torch.compile and PyTorch 2.0

PyTorch 2.0 introduced `torch.compile` as a JIT compiler that captures FX graphs and applies backend optimizations. The reference language proposal is complementary rather than competitive: `torch.compile` handles the case where the compiler *can* deliver adequate performance automatically. When it cannot — for frontier-scale training with custom fused kernels, explicit backward graphs, or novel parallelism strategies — the reference-language pattern provides an escape hatch.

The key architectural insight is that `torch.compile` and hand-optimized kernels can coexist within the same project, with the reference implementation serving as the common correctness baseline. This addresses Horace He's open question from 2025: *"How can we get all of the control of eager-mode execution with some of the conveniences of graph-level abstraction?"*

## Related Pages

- [[compiler-design]] — Broader context on ML compiler architecture and the compiler-maximalist debate
- [[pytorch-fsdp]] — PyTorch in production at scale with Fully Sharded Data Parallel
- [[fused-kernels]] — Kernel fusion and the performance motivations behind kernel DSLs
- [[tinygrad]] — Another minimal ML framework that explores the reference-implementation philosophy
- [[transformer-architecture]] — The dominant architecture whose training patterns drive this infrastructure design
