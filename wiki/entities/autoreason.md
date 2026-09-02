---
title: Autoreason
type: concept
created: 2026-04-27
updated: 2026-09-02
status: active
sources:
  - https://github.com/NousResearch/autoreason
  - https://x.com/SHL0MS/status/2043415274196435325
  - raw/articles/2026-04-12-shl0ms-autoreason-paper.md
tags:
  - reasoning
  - multi-agent
  - self-improving
  - autoresearch
  - nous-research
  - pseudonymous
aliases: [auto-reason]
related:
  - "[[entities/nous-research]]"
  - "[[concepts/karpathy-loop]]"
  - "[[concepts/gepa]]"
---

# Autoreason

**Autoreason** ("Self-Refinement That Knows When to Stop") is a technique by **SHL0MS** (@SHL0MS) and **Hermes Agent** at [[entities/nous-research]] that fixes iterative LLM self-improvement for subjective and open-ended domains. It extends Karpathy's AutoResearch (see [[concepts/karpathy-loop]]) from autonomous experiment-running to improving the *quality of reasoning and writing itself* — domains (aesthetic judgment, literary quality, design) where conventional benchmark-based evaluation falls short.

The paper itself is a demonstration of the method: co-authored by a human researcher and an AI agent, written using a research-paper-writing skill developed during the process. Announced 2026-04-12 (1,958 bookmarks, 304K impressions).

## Core Problem

Naive critique-and-revise self-refinement fails for three structural reasons:

| Problem | Description | Autoreason Fix |
|---------|-------------|----------------|
| **Prompt bias** | Models hallucinate flaws when asked to critique their own work | Blind Borda count by fresh, context-isolated agents |
| **Scope creep** | Outputs expand unchecked each pass | "Do nothing" is a first-class option |
| **Lack of restraint** | Models never say "no changes needed" | Incumbent (A) always preserved as viable candidate |

Measured severity: plain critique-and-revise *reduced* Haiku 3.5 output by 59–70% in word count over 15 passes — refinement actively destroys weak models.

## Method

Each iteration produces three competing versions, judged blind:

1. **A — Incumbent**: unchanged
2. **B — Adversarial revision**: critique-based rewrite by a fresh author agent
3. **AB — Synthesis**: combination of the best of both

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

Key design points:
- Judges are **fresh agents with no shared context**, voting via **blind Borda count** (beats majority voting in ablations)
- **3 judges is the sweet spot**: 1 is noisy; 7 converges 3× slower
- **Both B and AB are necessary** — removing either collapses the tournament (convergence in 2–3 passes vs 24)

## Key Results

| Finding | Detail |
|---------|--------|
| **42/42 perfect sweep** | Haiku 3.5 + autoreason achieved perfect Borda across 3 tasks; all baselines *degraded* below single-pass |
| **77% vs 73%** | Sonnet 4.6 on 150 CodeContests problems (private-test): autoreason vs single-pass |
| **40% vs 31%** | Haiku 3.5 autoreason vs best-of-6 sampling at matched compute |
| **Haiku 4.5 transition point** | Held-out gains vanish at ~60% private accuracy — the generation-evaluation gap has closed |
| **Code scaling curve** | Haiku 3.5 (40%) → Haiku 4.5 (60%) → Sonnet 4 (64%) → Sonnet 4.6 (77%) |
| **Length-controlled: 21/28 wins** | Beats 3 of 4 baselines even at matched word count |

The Haiku 4.5 transition point is the theoretically interesting result: autoreason's value scales with the **generation-evaluation gap** — once a model can reliably judge its own outputs, external tournament refinement stops adding held-out gains.

## Experimental Scope (paper contents)

- **Writing**: 5 open-ended + 3 constrained tasks, 4 baselines, 15-pass iterations; multi-seed replication (15 runs) and Monte Carlo (5 runs)
- **Competitive programming**: 150 CodeContests problems × 3 strategies × 4 model tiers
- **Model scaling**: 5 tiers (Llama 8B → Gemini Flash → Haiku 3.5 → Haiku 4.5 → Sonnet 4)
- **Ablations**: judge count (1/3/7), Borda vs majority, component necessity, length control
- **Failure analysis**: 8 remedy experiments for the Sonnet 4.6 scaling failure + failure taxonomy
- **Human evaluation**: blinded materials (5 tasks × 3 methods, randomized 4-char codes) in `human_eval/`

## Repository

[NousResearch/autoreason](https://github.com/NousResearch/autoreason) — `paper/` (LaTeX + PDF), `tasks/`, `human_eval/`, `experiments/v2/` (runners for writing/code/multi-seed/ablations, bootstrap CIs + McNemar tests, all result dirs).

```bibtex
@article{shl0ms2026autoreason,
  title={Autoreason: Self-Refinement That Knows When to Stop},
  author={SHL0MS and Hermes Agent},
  year={2026},
  url={https://github.com/NousResearch/autoreason}
}
```

## Significance

Autoreason is the first application of automated self-improvement to **subjective evaluation**, replacing the structurally flawed critique-and-revise pattern with competitive selection by context-isolated judges. Its "do-nothing-wins-out" design makes restraint explicit — a counterpoint to the constant-churn failure mode of naive agent loops.

## Related Concepts

- [[concepts/karpathy-loop]] — AutoResearch precursor: autonomous ML research loops; autoreason extends it to subjective reasoning quality
- [[concepts/gepa]] — also uses multi-candidate evaluation and reflection-driven optimization
- [[concepts/agentic-scaffolding]] — autoreason as scaffolding around the reasoning process itself
- [[entities/agreement-bug]] — judge-panel design responds to the same agent-agreement failure mode
- [[entities/nous-research]] — publishing organization; Hermes Agent as co-author

## TODO

- [ ] Track formal paper publication / arXiv posting
- [ ] Compare with Reflexion, Self-Refine, and other self-correction frameworks

## Sources

- [GitHub: NousResearch/autoreason](https://github.com/NousResearch/autoreason) — README fetched 2026-09-02
- [Announcement post](https://x.com/SHL0MS/status/2043415274196435325)
- `raw/articles/2026-04-12-shl0ms-autoreason-paper.md`
