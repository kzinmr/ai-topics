---
title: "Inference-Time Compute"
type: concept
aliases:
  - inference-time-compute
  - inference-time scaling
created: 2026-04-25
updated: 2026-10-26
tags:
  - concept
  - reasoning
  - test-time-scaling
  - inference
  - optimization
related:
  - "[[concepts/test-time-scaling]]"
  - "[[concepts/test-time-compute]]"
  - "[[concepts/chain-of-thought]]"
  - "[[concepts/sleep-time-compute]]"
  - "[[entities/andrej-karpathy]]"
sources:
  - https://arxiv.org/abs/2408.03314
  - "[[queries/test-time-compute-three-axes-2026-09-24]]"
---

# Inference-Time Compute

**Inference-time compute** is the total computational work a model performs *when generating an answer* — as opposed to the compute spent during training. Historically, capability gains came almost exclusively from scaling training compute (pretraining + post-training); inference was a fixed, latency-bound cost. Since ~2024 (OpenAI o1, DeepSeek-R1), the field's center of gravity has shifted: spending *more* compute at inference — longer chains of thought, more samples, search, tool use — buys accuracy that more training parameters no longer reliably delivers.

## Key Ideas

- **The third scaling axis.** Beyond model size and data, inference-time compute is a third axis on the compute-vs-capability frontier. Models can be *trained to use* extra inference compute (RL on long reasoning traces) rather than merely being big.
- **Train-time vs inference-time tradeoff.** Reasoning models deliberately shift cost to inference time: a smaller model that "thinks longer" can match a much larger model that answers immediately (the RLM/small-model-plus-deep-recursion pattern).
- **Diminishing — and eventually negative — returns.** Accuracy rises with compute only up to a peak; past it, extra tokens can inject self-contradiction and degrade performance. See the three-axes analysis in [[queries/test-time-compute-three-axes-2026-09-24]].
- **Token economics.** Inference compute is a marginal cost per request, so it is the axis where deployment economics live — budget-per-task, budget-per-query, and per-token Elo analyses all measure this axis.

## Where This Page vs. Sister Pages

| Page | Focus |
|------|-------|
| **This page** | The general concept: compute spent at inference, its economics, its place in scaling |
| [[concepts/test-time-scaling]] | Canonical deep-dive: scaling laws, parallel/sequential strategies, RLVR, s1/s2 budgets |
| [[concepts/test-time-compute]] | Hub: the three axes (sleep-time / test-time / post-peak) |
| [[concepts/sleep-time-compute]] | Offline precomputation before any query arrives |

## Terminology

- **Inference-time compute**: FLOPs/token-latency consumed generating one response, including hidden reasoning tokens.
- **Test-time compute**: near-synonym, used when the extra compute is spent against a *evaluation/test* problem (benchmarks, competitions).
- **Compute-optimal budget**: the token allocation at which marginal accuracy gain per marginal token crosses the payoff threshold.

## Related Concepts

- [[concepts/test-time-scaling]] — the canonical technical treatment of this concept
- [[concepts/test-time-compute]] — three-axes framing (sleep / test / post-peak)
- [[concepts/chain-of-thought]] — the original cheap form of inference-time compute
- [[concepts/rlvr]] — RL with verifiable rewards, the training recipe that teaches models to *use* inference compute
- [[concepts/token-economics]] — pricing and budgeting of this compute axis

## Graph Structure Query

```
[inference-time-compute] ──part-of──→ [concept: test-time-scaling]
[inference-time-compute] ──contrasts──→ [concept: training-time scaling laws]
[inference-time-compute] ──relates-to──→ [concept: sleep-time-compute]
[inference-time-compute] ──popularized-by──→ [entity: andrej-karpathy] ("all the training happens at test time" framing)
```

## Sources

- [Large Collective Reasoning / test-time compute survey](https://arxiv.org/abs/2408.03314)
- [[queries/test-time-compute-three-axes-2026-09-24]] — wiki-internal synthesis of the three compute axes
