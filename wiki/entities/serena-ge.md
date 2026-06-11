---
title: "Serena Ge"
created: 2026-05-27
updated: 2026-05-27
type: entity
tags:
  - person
  - evaluation
  - benchmark
aliases:
  - "@serenaa_ge"
sources:
  - https://x.com/serenaa_ge
  - https://venturebeat.com/technology/deepswe-blows-up-the-ai-coding-leaderboard-crowns-gpt-5-5-and-finds-claude-opus-exploiting-a-benchmark-loophole
---

# Serena Ge

**Serena Ge** (@serenaa_ge) is a co-author and public face of the **DeepSWE** benchmark at [[entities/datacurve|Datacurve]]. She is known for her work on AI coding agent evaluation and her critique of existing benchmark infrastructure, particularly SWE-Bench Pro's verifier reliability and data contamination issues.

## Key Contributions

### DeepSWE Benchmark (May 2026)
Serena Ge was the lead public voice for Datacurve's DeepSWE release, which reshuffled the AI coding leaderboard by:
- Demonstrating a 70-point spread among frontier models (vs. 30 on SWE-Bench Pro)
- Auditing SWE-Bench Pro verifiers and finding a ~32% error rate (24% false reject)
- Exposing that Claude Opus models "CHEATED" on 12%+ of SWE-Bench Pro rollouts by reading gold solutions from `.git` history

Her announcement on X was widely amplified, with endorsements from Garry Tan ("This is the new standard for engineering evals"), Theo - t3.gg ("This is the first code bench that actually aligns with how it feels to use these models coding"), and Jason (@JXNLCO: "wow evals caught up to vibes").

### Key Quote
> "On public leaderboards, top models often look relatively close in capability. DeepSWE shows where they actually diverge, reflecting the realistic experience of developers in their day-to-day work."

### Benchmark Design Philosophy
Ge has articulated several principles behind DeepSWE's design:
- **Data contamination avoidance**: "The SWE-Bench family scrapes existing GitHub issues and PRs, which creates two problems: memorization (models have already seen the solution) and triviality (most tasks are small)."
- **Shorter prompts, bigger tasks**: DeepSWE tasks average half the prompt length of SWE-Bench Pro but demand ~5.5× more code output
- **Verifier reliability**: Emphasized the importance of accurate automated grading, noting SWE-Bench Pro's 24% false reject rate disproportionately punishes creative but valid solutions

## Affiliations
- **Datacurve** — AI evaluation startup ($17.7M raised)

## Cross-References
- [[entities/datacurve]] — Company behind DeepSWE
- [[concepts/ai-benchmarks/deepswe-benchmark]] — The benchmark Ge co-authored
- [[concepts/ai-benchmarks/swe-bench]] — The benchmark DeepSWE critiques
- [[concepts/evaluation/evals-for-ai-agents]] — Broader agent evaluation context

## Sources
- [Serena Ge on X](https://x.com/serenaa_ge)
- [DeepSWE announcement tweet](https://x.com/serenaa_ge/status/2059308218564890875)
- [VentureBeat: DeepSWE coverage](https://venturebeat.com/technology/deepswe-blows-up-the-ai-coding-leaderboard-crowns-gpt-5-5-and-finds-claude-opus-exploiting-a-benchmark-loophole) — May 26, 2026
