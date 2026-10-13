---
title: "Prompt Optimizers Miss Unscored Requirements"
created: 2026-10-13
updated: 2026-10-13
type: concept
tags:
  - prompting
  - optimization
  - evaluation
  - gepa
  - self-improving
  - ai-agents
aliases: [TG (targeted gating), unscored-requirement failure]
sources:
  - raw/papers/2026-10-09_2610.13287_prompt-optimizers-unscored-requirements.md
  - https://arxiv.org/abs/2610.13287
related:
  - concepts/gepa
  - concepts/prompt-engineering
  - concepts/prompt-debt
  - concepts/evaluation/prompt-engineering-evaluation
confidence: medium
---

# Prompt Optimizers Miss Unscored Requirements

> **TL;DR:** Automated prompt optimizers (GEPA, MIPROv2) improve *scored* metrics (exact-match on QA) dramatically but **leave unscored requirements essentially unchanged** — because nothing in the optimization loop measures them. A "targeted gating" (TG) procedure that rolls candidates forward only on a small held-out subset of *hard-case diagnostics* improves some unscored requirements, but cannot guarantee they will not degrade. (arXiv:2610.13287, Oct 2026)

## The Problem

Automatic prompt optimization — see [[concepts/gepa]] — assumes the optimization metric captures what you care about. In practice, prompts carry many **requirements that no eval scores**: tone, format compliance, refusal boundaries, robustness edge-cases. The optimizer, given a metric like exact-match (EM), will happily trade away anything it does not measure.

This is the optimizer-side counterpart of [[concepts/prompt-debt]]: even when a prompt is *machine-optimized*, the parts of the specification that never appear in a scoring function silently rot.

## The Experiment (Meta)

Three tasks: **HotpotQA** and **SQuAD 2.0** (extractive QA, scored by EM) and **IFEval** (instruction-following, near-saturated). Three optimizers: **GEPA**, **MIPROv2**, and a **targeted-gating (TG)** wrapper.

Key design: a *requirement pool* of 17 explicit, verifiable requirements is defined per task, but the optimization loop only sees the EM score. A held-out **HARD CASE** subset of 56 examples is used as a small diagnostic set.

## Preregistered Results

| Task | Metric | Initial | GEPA | MIPRO | TG |
|------|--------|---------|------|-------|-----|
| HotpotQA | EM | 0.193 | 0.536 | 0.406 | 0.517 |
| SQuAD 2.0 | EM | 0.350 | 0.748 | 0.720 | 0.780 |
| IFEval | score | 0.908 | ~unchanged | ~unchanged | ~unchanged |

- **GEPA matches the frontier-model baseline** on the scored metric while using **~1,000× fewer rollouts** than RL (consistent with GEPA's published 35× claim, scaled up here).
- The unscored requirements stay flat: optimization moves EM by 0.3+ but leaves the unmeasured specification untouched.

## Targeted Gating (TG)

TG rolls a candidate prompt forward **only if it passes a small subset of hard-case diagnostics** — cheap, non-differentiable checks on requirements the main metric ignores.

- Improves some previously-stuck unscored requirements (TG is the best optimizer on SQuAD EM *and* lifts some requirements).
- **Cannot guarantee non-degradation** — a small diagnostic set is itself an imperfect proxy. The authors are explicit: TG "improves some requirements but cannot guarantee others will not degrade."

## Why It Matters

1. **Metric = destiny for prompt optimizers.** As DSPy/GEPA/MIPRO-style optimization replaces hand-tuning, the requirements you *don't* score are the ones you *lose*. Specify every requirement you care about as a measurable check, or keep a human in the loop.
2. **Diagnostic gating is a partial, not complete, fix.** Small held-out hard-case sets are the cheapest available guardrail, but inherit all the usual overfitting-to-the-test-set risk.
3. **Preregistration is rare and welcome** in prompt-optimization papers; all 54 runs, 27 selections, 87 evaluations completed with no missing items — the negative result on unscored requirements is trustworthy.

## Open Questions

- Can requirement coverage be *audited* automatically from a spec (e.g., LLM-generated requirement pool) rather than hand-specified?
- What is the minimum diagnostic-set size at which gating reliably prevents regressions vs. merely decorates them?

## See also

- [[concepts/gepa]] — the reflective prompt optimizer studied here
- [[concepts/prompt-engineering]] / [[concepts/evaluation/prompt-engineering-evaluation]]
- [[concepts/prompt-debt]] — fragile instructions that optimization can't see
