---
title: "Exploration Benchmarks"
created: 2026-09-27
updated: 2026-09-27
type: concept
tags: [agent-evaluation, ai-agents, benchmark, long-horizon, world-models]
aliases:
  - ExplorationBench
  - Exploration Ability
sources:
  - raw/articles/2026-09-27_arxiv_2609.30199_explorationbench.md
related:
  - concepts/world-models-for-agents.md
  - concepts/test-time-scaling.md
  - concepts/long-horizon-agents.md
  - concepts/agent-harnesses.md
confidence: medium
contested: false
---

# Exploration Benchmarks

**Exploration ability** is the capacity to *acquire* knowledge that was not in
pre-training — framing hypotheses, designing experiments (choosing probes), reading
outcomes, and applying the resulting rules to new problems. The core measurement
problem, per Zhu et al. (2026), is a tension: tasks must be **novel to the system**
(so success can't come from recall) yet **exactly verifiable by the evaluator** (so a
genuine discovery is distinguishable from a plausible-sounding claim). Existing static
math/code/QA benchmarks meet verification but not novelty; genuinely novel outputs meet
novelty but not verification. ^[raw/articles/2026-09-27_arxiv_2609.30199_explorationbench.md]

## ExplorationBench (arXiv:2609.30199)

Yuzhu Cai et al. (2026) — *ExplorationBench: Measuring AI Systems' Exploration Ability*
— resolves the tension with **verifiable Alien Worlds**: deterministic, executable
environments whose hidden rules *conflict* with familiar semantics and with a flawed
manual the system is given.

- **Two sandboxes.** *AlienCode* (31 discovery targets, 70 tasks) — a small programming
  language where, e.g., integer literals are silently XOR-ed with 27 (so `EMIT(100)`
  prints 127) and `PLUCK` counts from one although the manual says zero. *AlienLogic*
  (24 targets, 70 tasks) — a natural-deduction system with altered rules.
- **Protocol.** From the flawed manual + fixed worked examples, the system runs **four
  rounds**, choosing its own probes and adding results to an exploration history. At each
  milestone `M0–M4` it is tested **without tools**: state the rules it believes hold, and
  solve 70 held-out tasks graded by an interpreter / proof-checker (no LLM judge).
- **Recall resistance.** Before exploring, *no* AlienCode trajectory exceeds 15.7% —
  prior knowledge misleads rather than helps.

## Key Findings

- **Exploration produces the needed knowledge.** Best AlienCode trajectory reaches
  **87.6%** after four rounds; the same number of model turns *without environment
  feedback* leaves systems at 0.5–11.0%.
- **Who designs the experiments matters.** Returning a system its *own best probes*
  without letting it choose them **lowers accuracy for 9 of 10 systems**; randomized
  probes barely help. Choosing probes is itself the skill.
- **Transfer is weak.** Rank in AlienCode barely predicts rank in AlienLogic (Spearman
  0.35) — exploration ability is task-specific, not a single trait.
- **Discovery ≠ use.** Two off-by-one rules enter 51 of 70 AlienCode tasks and the
  biggest accuracy jumps coincide with their discovery — yet tasks whose required rules a
  system *states correctly* are solved only **70.9%** of the time.
- **Telling beats exploring (in AlienLogic).** Being handed the rules (93–97%) beats
  every system's own exploration — a sobering ceiling result.
- **Exploration is unreliable.** Trajectories of one system under one budget end up to
  **72.8 points apart**; 6 of 30 AlienCode trajectories end ≥3 points *below* an earlier
  milestone — continued exploration can **stall or reverse** gains.

## Why It Matters

Frontier [[concepts/long-horizon-agents]] benchmark well against recall. ExplorationBench
isolates the *acquisition of genuinely new knowledge* over a process, which is what
[[concepts/world-models-for-agents]] and real scientific/engineering workflows demand:
an agent must decide what evidence to collect and revise beliefs accordingly. The
"discovery ≠ use" gap ("knowing the rule" ≠ "reliably applying it") and the instability
of trajectories are the practical obstacles to trusting exploration, alongside the
[[concepts/test-time-scaling]] question of whether more exploration rounds monotonically
help (they demonstrably can regress).

## Open Questions

- Can methods reduce trajectory variance so exploration is trustworthy, not just
  sometimes-excellent?
- What closes the "know the rule but fail to apply it" gap — is it a retrieval,
  planning, or grounding failure?
