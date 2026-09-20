---
title: Coding Agent Harness Design Study
created: 2026-09-20
updated: 2026-09-20
type: concept
tags: [coding-agents, ai-agents, agent-harness, evaluation, research, agent-architecture, context-engineering]
sources:
  - raw/articles/2026-09-20_arxiv-2609.20804_empirical-study-of-harness-design-for-coding-agents.md
related: [harness-engineering, effective-harnesses-for-long-running-agents, context-engineering, agent-overclaiming, coding-agents]
confidence: high
---

# Coding Agent Harness Design Study

Fan et al. (2026), *"An Empirical Study of Harness Design for Coding Agents"* (arXiv:2609.20804),
is the first **component-level ablation** of a coding agent's [[harness-engineering|harness]].
Prior work (e.g. Anthropic's [[effective-harnesses-for-long-running-agents]]) evaluated harnesses
as monolithic systems, so it was never clear *which parts actually paid for themselves*. This
study fixes the execution loop and varies three components independently — **planning**, **action
space**, and **context management** — across **4 models** on **SWE-Bench Verified** and
**Terminal-Bench 2.1**, for **176 matched settings** (5 context-management strategies × 4
context-window budgets + targeted planning/action-space ablations).

## The four conditional findings

The central lesson is that **no harness component is universally good** — every effect is
conditional on model capability and context budget:

1. **Context management matters more as the window budget tightens**, and most of its benefit is
   simply *preventing context-overflow failures* — not smarter reasoning.
2. **Staging rule-based elision before LLM-based summarization** gives the strongest overall
   efficiency. Making elided content *recoverable* adds machinery models **rarely use and yields
   no accuracy gain** — a pure cost with no benefit.
3. **Planning shifts role with model strength**: an *accuracy scaffold* for weaker models, a *cost
   saver* for stronger models, with little accuracy change either way.
4. **Predefined (typed) tools help models with weak bash proficiency**; bash-capable models do
   fine with a **bash-only interface at substantially lower cost**, especially on
   command-line-centric tasks.

## Trajectory-level explanation

The authors explain the effects mechanistically, which is the paper's most reusable idea:

- **Context management** *extends* execution trajectories (more steps before overflow) without
  substantially changing agent *behavior*.
- **Planning** changes *where trajectories stop* (early stopping / structure), not what's in them.
- **Action space** changes the *granularity at which code is written* (one big bash heredoc vs.
  many small typed tool calls).

This maps each lever to a distinct causal pathway, so harness authors can predict interactions
rather than A/B everything.

## Implications

The result is a **model- and budget-aware** argument against one-size-fits-all harnesses (echoing
[[agent-execution-tax]] and the broader harness-commoditization debate): pair a strong
bash-capable model with a thin, cheap harness; give a weaker model typed tools, planning, and
generous context. It also provides a modular evaluation framework for testing future components.

### Open tension with overclaiming

Because context management mainly *prevents overflow failures* rather than improving fidelity, it
can silently lengthen horizons over which an agent loses track of what it did — the exact regime
where [[agent-overclaiming]] (unreliable final accounts) bites hardest. Longer, cheaper
trajectories are only a win if verification keeps up.

## Related

- [[harness-engineering]] — the discipline this study empirically grounds
- [[effective-harnesses-for-long-running-agents]] — the monolithic-harness prior this ablates
- [[context-engineering]] — the context-management strategies ablated here
- [[agent-overclaiming]] — the verification failure mode long cheap trajectories can worsen
