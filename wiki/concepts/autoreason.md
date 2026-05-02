---
title: Autoreason
created: 2026-04-27
updated: 2026-04-27
type: concept
tags:
  - reasoning
  - lab
  - nous-research
  - karpathy
aliases: ["AutoReason", "Autoreasoning"]
sources:
  - https://github.com/NousResearch/autoreason
  - https://github.com/karpathy/autoresearch
status: complete
---

# Autoreason

A self-refinement framework for AI reasoning that extends [[karpathy-loop]] (Karpathy's AutoResearch) into the subjective reasoning domain. Addresses three structural failures in iterative self-refinement: prompt bias, scope creep, and lack of restraint.

## Definition / Core Idea

Autoreason (by SHL0MS & Hermes Agent at [[nous-research]]) fixes the core problem with LLM self-improvement: models hallucinate flaws when asked to critique their own work, outputs expand without bound on each revision, and models never say "no changes needed."

## Core Mechanism

Each iteration produces **three competing versions**:
1. **The unchanged incumbent (A)** — keep as-is
2. **An adversarial revision (B)** — deliberately challenge the current approach
3. **A synthesis (AB)** — combine the best of both

These are judged by **fresh agents with no shared context** via blind **Borda count** voting. Critically, **"do nothing" is always a first-class option** — preventing unnecessary scope expansion.

## Three Structural Problems Solved

| Problem | Description | Autoreason Fix |
|---------|-------------|----------------|
| **Prompt bias** | Models hallucinate flaws when asked to critique | Blind Borda count with fresh agents |
| **Scope creep** | Outputs expand unchecked each pass | "Do nothing" as first-class option |
| **Lack of restraint** | Models never say "no changes needed" | Incumbent (A) preserved as viable candidate |

## Connection to Karpathy's AutoResearch

- [[karpathy-loop]] focuses on autonomous ML research execution (630 lines of code running experiments overnight)
- **Autoreason** extends this into the *subjective reasoning* domain — not just running experiments, but improving the quality of reasoning itself
- Both share the philosophy of removing human bottlenecks from research/improvement loops

## Connection to Other Concepts

- [[karpathy-loop]] — AutoResearch as the precursor for autonomous research loops
- [[agentic-scaffolding]] — Autoreason provides scaffolding around reasoning itself
- [[gepa]] — Both use multi-candidate evaluation and Pareto-style optimization

## TODO: Research Items
- [ ] Track NousResearch paper publication and benchmark results
- [ ] Compare with other self-refinement frameworks (Reflexion, Self-Correction)
- [ ] Document Borda count implementation details for agent voting
