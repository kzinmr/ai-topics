---
title: "DSPy — Declarative Foundation Model Programming"
tags: [research, framework, NLP]
created: 2026-04-24
updated: 2026-04-24
type: sub-entity
---

# DSPy: Declarative Foundation Model Programming (2022–present)

DSPy is [[entities/omar-khattab]]'s framework that replaces ad-hoc prompt engineering with composable, optimizable LM programs.

## Philosophy

> *"It's actually better to think of language models as modules in programs, not end products."*
> — Omar Khattab, Cohere talk (2024)

DSPy treats LMs as **learnable modules** in a computational graph:
1. **Define** a program with LM modules (Chain of Thought, ReAct, program-level reasoning)
2. **Specify** a metric for evaluation
3. **Optimize** the prompts (or fine-tune weights) automatically using built-in optimizers

## Key Insight

DSPy unifies prompting, fine-tuning, and retrieval-augmented generation under a single programming model. Small models (T5, <1B parameters) expressed in DSPy routinely outperform large standalone LMs with hand-crafted prompts.

## Open-Source

- PyPI packages: `dspy`, `dspy-ai`
- GitHub: stanfordnlp/dspy
- 500,000+ monthly downloads

## Related

- [[concepts/dspy]] — Concept page
- [[entities/omar-khattab]] — Creator
