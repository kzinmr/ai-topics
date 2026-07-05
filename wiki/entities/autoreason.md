---
title: Autoreason
type: concept
created: 2026-04-27
updated: 2026-05-27
status: L2
sources: [https://github.com/NousResearch/autoreason, https://x.com/SHL0MS/status/2043415274196435325]
tags:
  - reasoning
  - multi-agent
  - person
aliases: [auto-reason]
---

# Autoreason

A technique for **automating self-refinement in subjective domains**, co-developed by SHL0MS (@SHL0MS) and Hermes Agent (NousResearch). An extension of Karpathy's AutoResearch to the domain of subjective evaluation.

## Core Problem

Iterative self-improvement (critique-and-revise) fails due to three structural flaws:

1. **Prompt Bias**: When asked for criticism, the model tends to fabricate flaws
2. **Scope Creep**: Output expands uncontrollably with each iteration
3. **Lack of Restraint**: The model does not output "no change needed"

## Methodology

Each iteration generates **3 competing versions**, scored via **blinded Borda voting** by **context-isolated fresh agents**. "Do nothing" is always a first-class option.

| Version | Description |
|-----------|------|
| **A** | Incumbent (no changes) | |
| **B** | Adversarial revision (critique-based rewrite) | |
| **AB** | Synthesis of A and B | |

```
Task Prompt → Incumbent A
                  ↓
        ┌─── Critic (fresh agent) ───→ Critique
        │
        ├─── Author B (fresh agent) ──→ Revision (B)
        │
        └─── Synthesizer (fresh) ─────→ Synthesis (AB)
                  ↓
          Judge Panel (3 fresh agents, Borda count)
                  ↓
              Winner → new A  (or converge if A wins k=2 times)
```

**Key design points**:
- 3 judges provide optimal convergence speed (1 has too much noise, 7 takes 3x as long to converge)
- Both B and AB are necessary. If either is missing, the tournament collapses
- Wins 3 out of 4 tasks even in length-controlled evaluation

## Key Results

| Finding | Detail |
|---------|--------|
| **42/42 perfect sweep** | Haiku 3.5 + autoreason won complete Borda sweep across 3 tasks; all baselines degraded below single-pass |
| **77% vs 73%** | Sonnet 4.6 in 150 CodeContests problems (private-test): autoreason vs single-pass |
| **40% vs 31%** | Haiku 3.5 autoreason vs best-of-6 sampling (matched compute) |
| **Haiku 4.5: transition point** | Gains disappear at 60% private accuracy — suggests convergence of the generation-evaluation gap |
| **Refinement destroys weak models** | Critique-and-revise reduces Haiku 3.5 output by 59-70% over 15 passes |
| **Code scaling curve** | Haiku 3.5 (40%) → Haiku 4.5 (60%) → Sonnet 4 (64%) → Sonnet 4.6 (77%) |

## Repository

[NousResearch/autoreason](https://github.com/NousResearch/autoreason)
- `paper/` — LaTeX source, figures, PDF
- `tasks/` — Task prompts (5 open-ended, 3 constrained)
- `human_eval/` — Blinded materials for human evaluation
- `experiments/` — Experiment runner, results, ablations

## Citation

```bibtex
@article{shl0ms2026autoreason,
  title={Autoreason: Self-Refinement That Knows When to Stop},
  author={SHL0MS and Hermes Agent},
  year={2026},
  url={https://github.com/NousResearch/autoreason}
}
```

## Significance

Autoreason is the **first application of "automated self-improvement" to the domain of subjective evaluation**. In subjective domains like "aesthetic judgment," "literary talent," and "design" — which cannot be addressed by conventional benchmark-based methods — it provides a competitive selection approach via Borda voting, replacing the structurally flawed critique-and-revise pattern. Its design feature is preventing unnecessary degradation by making "do nothing" a first-class option.

A natural extension of Karpathy's AutoResearch and an important milestone in automating research and creative processes with LLMs.

## Related Concepts
- [[entities/autoreason]]

- [Karpathy's AutoResearch](https://karpathy.github.io/2025/04/28/self-play-benchmark.html)
- [Agent Disagreement (Agreement Bug)](agreement-bug.md)
- [Multi-Agent Systems](multi-agent-systems.md)

## References

- raw/articles/2026-04-12-shl0ms-autoreason-paper.md
