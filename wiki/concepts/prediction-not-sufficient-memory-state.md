---
title: "Prediction Is Not a Sufficient Memory State"
created: 2026-10-12
updated: 2026-10-12
type: concept
tags: [memory-systems, agent-memory, recurrent, control-plane, interpretability]
sources: [raw/papers/2026-10-09_2610.13881_prediction-not-sufficient-memory-state.md]
confidence: high
related: [concepts/llm-memory-architecture, concepts/memory-systems-design-patterns, concepts/ssm-mamba]
---

# Prediction Is Not a Sufficient Memory State

A memory state that faithfully reproduces a model's *current* predictions can still have
forgotten *how to learn from the next observation*. Jenkinson Alvarez (arXiv:2610.13881,
Oct 2026) proves an exact characterization of this gap for cumulative learning and attention:
two histories that induce the same predictor can require arbitrarily different amounts of
hidden state to continue updating correctly.

This is a theoretical result about **what future updates reveal**, not a new algorithm or a
claim about trained-model gains.

## Core claim

For exact cumulative learning, the state a recurrent/attention memory must carry is *larger*
than the state needed to represent its current output. The surplus — "hidden evidence" — is
what the next gradient step depends on, even though it leaves the current prediction
unchanged.

Key results (smooth convex residual losses, unrestricted real features/labels):

- A continuous recurrent state of **fixed dimension exists exactly when the loss is
  polynomial**.
- For an unweighted polynomial of degree $D$, the exact state requires precisely
  $r=\binom{d+D}{D}-1$ coordinates. Even among histories that share one fixed current
  predictor, exactly $r-d$ coordinates remain necessary purely for continuation.
- **Non-polynomial losses have unbounded** state requirements on such equal-prediction
  histories.
- For ridge regression the hidden evidence is the **design matrix**: exact state costs
  $dp + d(d+1)/2$ versus $dp$ for the predictor alone. On a well-conditioned
  zero-prediction family, optimal $B$-bit compression retains a one-update error of order
  $d^{-1}2^{-2B/s_d}$ (with $s_d = d(d+1)/2$) even with arbitrary randomized codes.
- Kernel attention yields a second exact "closure" classification of the same kind.

## Why it matters for agent memory

The result is a caution against a common intuition behind [[concepts/llm-memory-architecture]]
and KV-cache/"context-as-memory" designs: **compressing or caching a memory down to whatever
reproduces today's outputs is lossy for tomorrow's update**. A memory that looks behaviorally
faithful (same predictions) can be structurally inadequate the moment it must incorporate a new
observation. This connects to the [[concepts/context-rot]] and retrieval-vs-state debate in
[[concepts/memory-systems-design-patterns]] — the "hidden evidence" that a summary drops is
exactly the part that future learning consumes.

It also reframes recurrent-state design: the fixed-dimension state of an RNN/SSM exists only
for polynomial losses; more general objectives provably need unbounded memory on
equal-prediction histories, which bears on the expressivity limits discussed in
[[concepts/ssm-mamba]].

## Open questions

- Does the effect bite in practice for SGD on smooth but non-polynomial losses (logistic,
  cross-entropy)? The paper constructs bounded scalar logistic examples that *retain* the
  obstruction after fixing any finite derivative jet — a worst-case signal, not an empirical
  measurement.
- What is the practical compression–continuation trade-off for real KV-cache eviction policies?

## Related

- [[concepts/llm-memory-architecture]]
- [[concepts/memory-systems-design-patterns]]
- [[concepts/ssm-mamba]]
- [[concepts/context-rot]]
