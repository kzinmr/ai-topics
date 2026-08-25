---
title: AI Discovery Acceleration (METR Differential Acceleration)
type: concept
created: 2026-08-25
updated: 2026-08-25
tags:
  - ai-research
  - evaluation
  - ai-in-science
  - mathematics
  - cybersecurity
sources:
  - raw/articles/2026-08-14_metr_have-we-seen-an-acceleration-in-discoveries.md
  - https://metr.org/notes/2026-08-14-llm-contribution-to-discoveries/
---

# AI Discovery Acceleration (METR Differential Acceleration)

**"Differential acceleration"** is METR's finding (Cunningham & Rush, 2026-08-14) that AI is **not** accelerating all of science/technology uniformly. Instead, advances come in **lumpy pockets**: some domains (cyber security) are accelerating sharply, while others (algorithmic optimization) show little or no measurable change. This nuance is a recurring theme in frontier-lab and policy discussion — it undercuts both "AI accelerates everything" and "AI hasn't accelerated anything" narratives.

## Three-Domain Comparison

| Domain | Finding | Evidence |
|--------|---------|----------|
| **Cyber security (vulnerabilities)** | **MAJOR acceleration** | Reported-vuln rate "dramatically accelerated" 2026 vs 2025 — cURL, OpenSSL, Firefox, Microsoft; aggregate DBs (US NVD, OSV). *Exploited*-vuln DBs (CISA, Vulncheck KEVs) grow far slower → **discovery outpacing exploitation** |
| **Mathematics** | **MINOR acceleration, hard to measure** | 3 curated-list problems solved with AI in 2026 (Jacobian conjecture — Smale list; Green's Problem 44 "halving sieve"; sofic half of Green's Problem 100); arXiv submissions doubled in some areas in <12 months; Erdős list shows clear but un-baselineable acceleration |
| **Algorithmic optimization** | **NO measurable acceleration** | No slope change across CIFAR-10, Hutter compression, Gurobi MIP, MIPLIB, nanoGPT, Stockfish, matrix-multiplication exponent — despite Jan 2026 excitement (Yuksekgonul et al.) |

## Why Differential? (Candidate Explanations)
METR lists four drivers for the lumpy pattern:
1. **Variation in inference expenditure** — money poured into LLM-based vulnerability discovery (or traditional vuln discovery out of fear).
2. **Variation in LLM difficulty per domain** — some problem shapes are intrinsically easier/costlier for LLMs.
3. **Variation in disclosure** — AI-related algorithmic progress may be kept confidential.
4. **Variation in data quality** — fast-observed progress may just be where data is higher quality; hard-to-track domains flatten observed acceleration.

**Caveat:** findings are based on **public** discoveries only; labs may be making non-disclosed internal progress.

## Cited Examples
- **Anthropic / Riemann**: Jarred Sumner (non-mathematician, Anthropic) "prompted Claude to 'take a real stab' at the hypothesis itself."
- **Google DeepMind AlphaEvolve**: "readily scaled up to study large classes of problems at a time, without requiring extensive expert supervision."
- **Mythos Preview**: Claude Code prompted with "find a security vulnerability in this program" → overnight RCE exploit with no formal security training.

## Why it matters
- **Policy / capability forecasting**: acceleration is domain-specific, so "time horizon to AGI" or "when will X be solved" estimates must be domain-conditional.
- **Security**: the exploited-vs-known vulnerability gap means the attack surface is growing faster than defenders are patching — a [[concepts/ai-safety]] and [[concepts/cybersecurity]] concern.
- **Evals methodology**: measuring "discovery" velocity requires domain-appropriate baselines (pre-existing problem lists, record-setting benchmarks), not a single universal metric.

## Related Pages
- [[entities/metR]] — the publishing lab
- [[concepts/evaluation/ai-evals]] — evaluation methodology
- [[concepts/scaling-laws]] — scaling dynamics
- [[concepts/intelligence-explosion]] — time-horizon / AGI forecasting
- [[concepts/recursive-self-improvement]] — RSI
- [[concepts/cybersecurity]] — vulnerability discovery vs exploitation

## Sources
- [METR — Have We Seen an Acceleration in Discoveries?](https://metr.org/notes/2026-08-14-llm-contribution-to-discoveries/) (Cunningham & Rush, 2026-08-14)
- Raw article: `raw/articles/2026-08-14_metr_have-we-seen-an-acceleration-in-discoveries.md`
- Discussed in Import AI 470 (Jack Clark, 2026-08-24)
