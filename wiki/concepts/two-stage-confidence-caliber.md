---
title: "CALIBER: Two-Stage Confidence for Reasoning Models (Cohere)"
created: 2026-10-24
updated: 2026-10-24
type: concept
tags:
  - evaluation
  - llm-evaluation
  - safety-calibration
  - chain-of-thought
  - model-routing
aliases:
  - CALIBER
  - two-stage confidence
  - initial vs final confidence
sources:
  - raw/articles/2026-10-24_cohere_rethinking-confidence-in-reasoning-models.md
---

# CALIBER: Two-Stage Confidence for Reasoning Models

**One-line summary**: Cohere's CALIBER trains reasoning models to report *two* confidence numbers — before reasoning ("can I solve this?") and after ("is this answer right?") — cutting 7B math ECE from 0.059 to 0.028 (−52.5%) vs the best single-confidence baseline.

## The problem: one score, two questions

A single confidence number conflates two distinct predictions:

| Stage | Question answered | Training target |
|---|---|---|
| Pre-reasoning | "How likely am I to solve this?" | Empirical solve rate (e.g. 7/10 rollout successes → 0.70) |
| Post-reasoning | "How likely is *this* answer correct?" | Binary correctness of that specific attempt |

Standard reasoning models produce detailed chains of thought without any guarantee the accompanying uncertainty is meaningful — consistent with [[concepts/llm-confidence-calibration]]'s finding that self-reported scores are autoregressively generated tokens, not introspective signals.

## Method

- RL reward combines: correct answer + accuracy of *both* confidence estimates against their respective targets.
- Admitting uncertainty on a wrong answer earns the confidence reward but not the correctness reward — no incentive to fake confidence.
- Trained on 30,000 math problems; evaluated on 1,000 held-out problems + 3 QA benchmarks.

## Results (verbatim from Cohere blog, 2026-10-20)

- **BigMathDigits 7B**: ECE 0.059 → 0.028 (−52.5%); best AUROC 0.806, Brier 0.130.
- **Zero-shot transfer (no further training)**: ECE −26.8% GPQA, −32.2% TriviaQA, −36.2% SimpleQA.
- **30B caveat**: ECE 0.022 vs CoCA-lite 0.023 (trivial gap), but AUROC 0.797 vs 0.508 — the baseline is calibrated on average yet its confidence carries no error-detection signal. ECE alone is insufficient; always report AUROC alongside.
- **Confidence movement is diagnostic**: for correct answers mean confidence rises 78.5%→83.5%; for incorrect, falls 62.6%→54.5%. Reasoning that *lowers* confidence is a feature, not a bug.

## Why it matters for agents

Two-stage confidence is a natural gate for [[concepts/model-routing]] / [[concepts/oracle-model-routing]]: initial confidence decides model tier before spending tokens; final confidence decides verify/accept/abstain afterwards. Cohere explicitly did *not* test abstention/retrieval triggers — stated as future work. Pairs with [[concepts/monitorability-metrics]]: both lines of work treat "one number is not enough" as the core lesson.

## Sources

- [Rethinking Confidence in Reasoning Models — Cohere](https://cohere.com/blog/rethinking-confidence-in-reasoning-models) (2026-10-20)
- Related: [[entities/cohere]], [[concepts/llm-confidence-calibration]]
