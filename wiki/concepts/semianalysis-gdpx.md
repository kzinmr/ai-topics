---
title: "SemiAnalysis GDPx — professional-task benchmark"
created: 2026-11-10
updated: 2026-11-10
type: concept
tags:
  - benchmark
  - evaluation
  - evals
  - labor
  - domain-expertise
  - semianalysis
sources:
  - raw/newsletters/2026-11-10-spotify-s-claude-code-token-trick-tested-the-real-savings.md
  - https://www.aibyaakash.com/p/spotifys-90-trick
---

# SemiAnalysis GDPx — professional-task benchmark

**GDPx** is a **SemiAnalysis** evaluation that gives frontier models **real tasks from 11 professional fields** — including chip design, law, and finance — rather than academic or code-competition style problems.

## Headline result

As reported in November 2026, **the best model, Claude Opus 5.5, scored just 12%**. Jack Clark-style framing ("AI still struggles at real professional work") is the natural reading: even the top frontier model completes professional-grade work at a level far below what an expert in the field would produce. See [[concepts/ai-evals]], [[concepts/claude/opus-5]].

## Why it matters

The number is a useful counterweight to benchmark-driven capability claims. Frontier models post near-ceiling scores on software-engineering and math suites while performing poorly on open-ended professional deliverables, which is the same pattern as the **METR** differential-acceleration result — acceleration is lumpy and domain-specific rather than uniform (see [[entities/metr]], [[concepts/ai-discovery-acceleration]]). For the labor-displacement debate, the load-bearing question is exactly this gap between verifiable benchmark tasks and legible professional work, see [[concepts/labor-economics]] and [[concepts/ai-adoption-barbell]].

The 12% figure should be read as a specific task-set result, not a general "AI is 12% as good as professionals" claim; per-field breakdowns and task definition are the parts that decide what it licenses.

## Related

- [[concepts/evaluation/ai-evals]] — evaluation methodology
- [[entities/anthropic]] — provider of the top-scoring model
- [[entities/metr]] — independent capability assessment org
- [[concepts/recursive-self-improvement]] — verifier-availability argument: professional deliverables lack the fast verifiers that make benchmark progress meaningful

## Sources

- Aakash Gupta, ["Spotify's Claude Code Token Trick, Tested"](https://www.aibyaakash.com/p/spotifys-90-trick), *AI by Aakash*, Nov 9, 2026 — reporting SemiAnalysis's new GDPx test.
