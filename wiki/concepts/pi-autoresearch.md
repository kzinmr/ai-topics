---
title: "pi-autoresearch — Generalizing Autoresearch Beyond Model Training"
type: concept
slug: pi-autoresearch
status: complete
tags: [autoresearch, agent-loop, ralph-loop, ai-agents, coding-agents, self-improving, optimization, tool]
created: 2026-05-13
updated: 2026-05-13
aliases: [shopify-autoresearch, pi-autoresearch-extension]
sources:
  - raw/articles/2026-04-15_shopify-autoresearch-david-cortes.md
---

# pi-autoresearch — Generalizing Autoresearch Beyond Model Training

> **Definition:** pi-autoresearch is a Pi agent harness extension (3,600+ GitHub stars) that generalizes [[concepts/karpathy-loop|Karpathy's Autoresearch]] from ML model training to **arbitrary metric optimization** — build times, test speeds, component mounting, pnpm performance, and any measurable workflow.

Built by David Cortés (Shopify Polaris team) and Tobi Lütke (Shopify CEO) and open-sourced in March 2026.

## How It Generalizes Karpathy's Autoresearch

Karpathy's original autoresearch targets a very specific loop: edit `train.py`, run fixed-duration training, evaluate validation loss, keep or discard. The metric is always model training loss.

pi-autoresearch replaces the fixed "train.py → val_loss" pipeline with a **generalized metric loop**:

| Aspect | Karpathy Autoresearch | pi-autoresearch (Shopify) |
|--------|----------------------|---------------------------|
| **Target** | Model training (train.py) | Any measurable system |
| **Metric** | Validation loss | Arbitrary: build time, render speed, test speed, memory |
| **Agent scope** | Edit one file | Full codebase (any file) |
| **Platform** | Direct script | Pi agent harness extension |
| **UI** | CLI logs | Custom table UI per iteration |
| **Multi-metric** | Single metric | Multi-metric support (Tobi's PR) |

## The Generalized Loop

```
1. Find a metric to improve (e.g., Polaris build time: 19.1s baseline)
2. Measure baseline of the metric
3. Hypothesis → test → three outcomes:
   - Faster than baseline → KEEP
   - Crashes → DISCARD
   - Slower → DISCARD
4. Repeat indefinitely (system prompt: "NEVER STOP LOOPING")
```

## Why It Works Where One-Shot Prompts Fail

A one-shot "improve build time" prompt fails because:
- No clear measurement → agent can't verify progress
- No iteration → can't learn from failures
- Human-level caution → won't try "crazy" ideas

pi-autoresearch succeeds because:
- **Targeted focus** on a single measurable metric
- **Permission to experiment** — "it has the option to try things it wouldn't try in a normal run"
- **Small increments compound** — even 1% per iteration becomes significant
- **Agent has no competing priorities** — "The toil that humans correctly deprioritize turns out to be the perfect workload for an autonomous loop"

## Results at Shopify

| Area | Improvement |
|------|------------|
| Polaris build time | **65% faster** |
| Liquid parse+render | **53% faster** |
| Liquid object allocations | **61% fewer** |
| Unit tests (some cases) | **300× faster** |
| React component mounting | **20% faster** |
| pnpm | Faster |
| 40+ metrics total | Measurable improvements |

## Tobi Lütke's Contributions

Tobi contributed a 32-commit PR adding:
- **Multi-metric support** — track multiple metrics simultaneously
- **Consistent per-iteration execution** scripts
- **Auto-commits** — agent commits successful changes automatically
- **Skill improvements** for the Pi agent

## Philosophical Shift

> "Before autoresearch, AI agents were doing the same work humans did, just faster. Autoresearch is different — it does work nobody would attempt manually."

The key insight: humans correctly deprioritize boring optimization work. An autonomous agent doesn't get bored, doesn't need ROI justification, and has no deadline pulling it elsewhere. This is a **different kind of work**, not a faster version of human work.

## Connection to Turnbull's AutoReSEARCH (HaystackConf 2026)

Doug Turnbull's AutoReSEARCH applies the same generalized metric loop to **search ranking code**, creating a direct parallel to pi-autoresearch:

| Aspect | pi-autoresearch (Shopify) | AutoReSEARCH (Turnbull) |
|--------|---------------------------|-------------------------|
| **Target metric** | Build time, render speed | NDCG on search judgments |
| **Code surface** | Any file in codebase | Single `rerank_wands()` function |
| **Primitive injection** | Build tools, test harness | BM25, vector search, query categorization |
| **Overfitting guard** | Crash = discard | LLM overfit detector + patch limits + holdout split |
| **Iteration feedback** | Faster/slower/crash | Per-query NDCG deltas |

Turnbull's implementation adds a critical insight absent from pi-autoresearch: **focused composition**. Rather than letting the agent optimize everything at once, each round narrows scope — first optimize retrieval, then hide that result behind a single tool and add query rewriting as the new capability. This staged approach prevents combinatorial explosion and yields higher metrics faster.

> *"Deep learning is a universal function approximator — it's really just linear algebra being optimized. AutoReSEARCH is just a different sort of putty being optimized, but in the same sort of harness."* — Doug Turnbull, HaystackConf 2026

Both implementations confirm the same philosophical principle: the agent does work humans correctly deprioritize. Turnbull notes that his agent discovered **reciprocal rank fusion** — the "least offensive" hybrid search solution — by exhaustively exploring within human search knowledge, similar to how pi-autoresearch finds micro-optimizations humans wouldn't bother attempting.

## Related Concepts

- [[concepts/karpathy-loop]] — The original autoresearch for ML training
- [[raw/articles/2026-05-14_softwaredoug_autoresearch-ranking-coded-by-agents-haystackconf]] — Doug Turnbull's HaystackConf talk applying autoresearch to search ranking (BM25/RRF optimization with guardrails)
- [[concepts/agent-driven-ranker-optimization]] — Guardrail framework for agent-coded rankers
- [[concepts/autonomous-component-optimization]] — Daniel Miessler's generalization to any knowledge work
- [[concepts/harness-engineering/agentic-loop]] — The canonical agent loop pattern
- [[concepts/codex-goal]] — Codex /goal command (Ralph loop built-in)
- [[concepts/self-improving-agents]] — Broader self-improving agent category

## References

- [Shopify Engineering: Autoresearch isn't just for training models](https://shopify.engineering/autoresearch) — David Cortés, April 2026
- [pi-autoresearch GitHub](https://github.com/shopify/pi-autoresearch)
- [Tobi's X post](https://x.com/tobi/status/1898335274430812572) — 53% faster Liquid, 61% fewer allocations
