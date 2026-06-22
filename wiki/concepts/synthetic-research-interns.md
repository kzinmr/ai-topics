---
title: "Synthetic Research Interns"
type: concept
created: 2026-06-16
updated: 2026-06-16
tags:
  - evaluation
  - lab
  - training
sources:
  - https://arxiv.org/abs/2606.07462
  - raw/newsletters/2026-06-15-import-ai-461-alignment-is-not-on-track-frontiercode-and-synthetic-research-inte.md
related:
  - concepts/aarri-bench
  - concepts/synthetic-data
  - concepts/ai-benchmarks/frontiercode
  - concepts/ai-evals
---

# Synthetic Research Interns

The "synthetic research intern" concept refers to AI systems designed to perform the full spectrum of activities that a human research intern would — not just code execution, but literature review, hypothesis generation, experiment design, data analysis, and ethical reasoning.

## AARRI-Bench

The primary benchmark for this concept is **[[concepts/aarri-bench|AARRI-Bench]]** (Act As a Real Research Intern), introduced in arXiv:2606.07462 (Wang et al., June 2026). It evaluates frontier LLMs and agentic harnesses across four dimensions:

1. **Context**: Field awareness and literature familiarity
2. **Mindset**: Self-awareness, autonomy, research judgment
3. **Hands-on**: Technical proficiency in experiment execution
4. **Interaction**: Tool use and human collaboration

The benchmark reveals that even the best current system (Claude Opus 4.7 + Mini-SWE-Agent) scores only 68.3%, indicating a significant gap between technical competence and full research internship capability.

## Context

The concept emerged alongside broader discussions about AI agents moving beyond task execution into genuine research roles. Key questions include:

- Can an AI system identify when it doesn't understand a domain well enough to proceed?
- Can it detect fabricated or poisoned research data?
- Can it make ethical judgment calls in ambiguous research situations?
- Can it integrate feedback from human collaborators effectively?

These are fundamentally different from coding benchmarks (which test correctness and mergeability) — they test research *maturity*, not just technical ability.

## Related Benchmarks

- [[concepts/aarri-bench]] — AARRI-Bench: The primary synthetic research intern benchmark
- [[concepts/ai-benchmarks/frontiercode]] — Tests code mergeability, not research capability
- [[concepts/ai-benchmarks/swe-bench]] — Tests issue resolution via test passing
- [[concepts/synthetic-data]] — Synthetic data generation and evaluation
