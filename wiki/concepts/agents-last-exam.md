---
title: "Agents' Last Exam (ALE)"
created: 2026-09-12
updated: 2026-09-12
type: concept
tags: [benchmark, evaluation, coding-agents, ai-agents, economics]
sources:
  - raw/articles/arxiv-2606-05405-agents-last-exam.txt
confidence: high
description: "Long-horizon, economically-valuable real-world agent benchmark (1K+ tasks, 13 industry clusters, O*NET/SOC-anchored). Mainstream agents score under 10% on the hardest tier despite 72% on Terminal-Bench."
related: [ai-benchmarks, benchmark-ceiling, agentic-benchmarks, ai-benchmarks/remote-labor-index, recursive-self-improvement, jobs-bench, ai-economics]
aliases: ["ALE", "Agents Last Exam"]
---

# Agents' Last Exam (ALE)

**Agents' Last Exam (ALE)** is a benchmark for AI agents built from *real, economically valuable workflows* rather than synthetic tasks. Its thesis: the gap between strong benchmark scores and weak real-world professional deployment is **an evaluation problem** — widely used benchmarks never measure sustained performance on GDP-relevant work. ([arXiv:2606.05405](https://arxiv.org/abs/2606.05405), Sun et al., submitted June 2026.)

The name deliberately echoes **Humanity's Last Exam (HLE)** but shifts the unit of measurement from *knowledge* to *labor*.

## Design

| Dimension | Design choice |
|-----------|--------------|
| Industry scope | Non-physical industries, mapped against **O*NET / SOC 2018** (US federal occupational taxonomy) |
| Structure | **55 sub-fields → 13 industry clusters → 1K+ tasks** |
| Task provenance | Contributed by **250+ industry experts** as projects they have *already performed* — no invented scenarios |
| Verifiability | Each task ships a task specification (`main.py`) with a three-phase lifecycle — `load()`, `start()`, `evaluate()` — running against a **remote VM**; outputs scored against references or rubrics |
| Difficulty | Three tiers; results report full-pass rate, mean score, total API cost, wall-clock time, token use |
| Lifecycle | **Living benchmark** — the task pool grows continuously as new workflows/industries are onboarded |

The remote-VM execution environment is the structural difference from chat-style benchmarks: the agent (harness + backbone) receives only a task description, acts through an action loop, and is judged on artifacts, not transcripts.

## Headline results

- On the **hardest tier**, mainstream harness/backbone configurations average a **full pass rate below 1%**; most mainstream agents — including Claude Code — record near-zero pass rates at that difficulty.
- The same systems that reach **72% on Terminal-Bench** score **below 50% on ALE's easiest tier** and **under 10% on the hardest**.
- **Model choice accounts for ~3× the spread of harness choice** among well-engineered systems — backbone identity matters more than scaffold polish.
- **Higher resource consumption does not reliably translate to better performance** (cost/time/token efficiency varies independently of scores).

## Why it matters

ALE is the sharpest available instrument for the *capability-vs-deployment* question that dominates 2026 agent discourse:

- It gives a **quantified floor** to claims of "GDP-relevant impact," the same territory [[concepts/ai-benchmarks/remote-labor-index|Remote Labor Index]] and **Jobs-Bench** measure from the wage-labor side.
- Its "hardest tier barely moves" finding is a concrete instance of the **benchmark ceiling** dynamic — see [[concepts/benchmark-ceiling]].
- Frontier-lab marketing now leads with ALE scores (e.g. GLM-5.3 at 28.5, and OpenAI's frontier models in the 40–60% range per their system cards), which makes ALE's own saturation trajectory worth tracking.

## Open questions

- Does a <1% hardest-tier pass rate measure agent inadequacy, task-specification brittleness, or both? The paper reports cost/time alongside scores but doesn't isolate harness bugs from capability gaps.
- A "living benchmark" that grows on demand avoids static contamination but makes longitudinal comparison harder — every task-pool change reshapes the denominator.
- Expert-contributed tasks inherit the biases of the expert pool (250+ people, US-taxonomy-anchored, non-physical industries only).

## Related

- [[concepts/benchmark-ceiling]] — the theory of why ALE's easy tiers will depreciate and its hard tail won't
- [[concepts/ai-benchmarks/remote-labor-index]] — measuring agent work against paid human labor
- [[concepts/recursive-self-improvement]] — PostTrainBench+ and the RSI-evaluation lineage
- [[concepts/ai-economics]] — the deployment gap ALE is designed to measure

## Sources

- Sun et al. ["Agents' Last Exam"](https://arxiv.org/abs/2606.05405). arXiv:2606.05405v2, June 2026. Raw: `raw/articles/arxiv-2606-05405-agents-last-exam.txt`
