---
title: "RLM — Recursive Language Models"
tags:
  - lab
  - inference
  - context
created: 2026-04-24
updated: 2026-04-24
type: sub-entity
---

# RLM: Recursive Language Models (2025–2026)

**Co-authors:** Alex L. Zhang, Tim Kraska, Omar Khattab
**Paper:** arXiv:2512.24601 (Dec 2025, revised Jan 2026)
**Code:** [github.com/alexzhang13/rlm](https://github.com/alexzhang13/rlm)
**Ecosystem:** DSPy v3.1.2+ ships built-in RLM support; Google ADK has enterprise-ready implementation

RLMs represent [[entities/omar-khattab]]'s latest contribution — an **inference-time scaling paradigm** that allows LMs to process arbitrarily long prompts by treating context as an external variable in a REPL environment.

## Khattab's Role

As co-author and PhD advisor to [[entities/alex-zhang]], Khattab provided the theoretical foundation for treating **context as an environment** rather than a fixed prompt. This connects directly to his broader thesis of **foundation model programming** — LMs should be programmable components, not monolithic text processors.

## The Deep Insight

Khattab framed RLMs' core contribution on X:

> *"Most people misunderstand RLMs to be about LLMs invoking themselves. The deeper insight is LLMs interacting with their own prompts as objects."*
> — Omar Khattab (@lateinteraction), 2026

This reframes RLMs from mere recursive calling to **context-as-data** manipulation. The model doesn't just call itself — it writes code to examine, filter, chunk, and selectively expose parts of its input. This is an **out-of-core algorithm design** pattern applied to language models.

## RLM as the Culmination of Khattab's Research Program

| Phase | Framework | What it delays | Why it matters |
|-------|-----------|---------------|----------------|
| **Phase 1** | ColBERT | Interaction (token-level matching) | Quality without compute at index time |
| **Phase 2** | DSPy | Prompt design (optimization) | Declarative programs over ad-hoc prompts |
| **Phase 3** | RLMs | Context consumption (selective reading) | Models manage what they see and when |

The through-line across all three: **architectural flexibility over brute-force scaling.**

## Benchmark Results (MIT OASYS Lab)

- **RLM(GPT-5-mini)** outperforms GPT-5 by >34pts on OOLONG (132k context)
- **RLM-Qwen3-8B** beats base Qwen3-8B by 28.3% average across 4 benchmarks
- **BrowseComp-Plus:** perfect performance at 1000 documents (10M+ tokens)
- **Cost:** RLM runs are comparable to or cheaper than base model calls (median)
- **Scale:** effectively processes 10M+ token inputs — 100× beyond native context windows

## Connection to "The Second Half"

Both Khattab/Zhang's RLM framework and [[shunyu-yao]]'s RL generalization thesis converge on the same insight: **how we structure the interaction** matters more than the raw capability of the model. Khattab's RLM makes the **environment** (the REPL, the context-as-data) the focus; Yao's work makes the **environment design** (Agent-Computer Interfaces) the focus.

## Related

- [[concepts/rlms]] — Concept page
- [[entities/omar-khattab]] — Co-author
- [[entities/alex-zhang]] — First author

## References

- 2026-04-25-rlm-gepa-combo
- 2026-04-26-rlm-gepa-experiment
- raw-works-rlms-new-reasoning-models-2026-04-20
- raw-works-rlms-sota-on-longcot-2026-04-19
