---
title: "Vibe Physics"
created: 2026-05-06
updated: 2026-05-06
type: concept
tags:
  - concept
  - scientific-discovery
  - frontier-models
  - ai-agents
  - reasoning
aliases:
  - "Vibe Physics (Lupsasca)"
related:
  - [[concepts/vibe-coding]]
  - [[entities/openai]]
  - [[concepts/jagged-frontier]]
sources:
  - raw/newsletters/2026-05-05-doing-vibe-physics-alex-lupsasca-openai.md
  - https://open.substack.com/pub/swyx/p/lupsasca
---

# Vibe Physics

**Vibe Physics** describes the use of frontier LLMs (GPT-5.x series) to perform genuine **scientific discovery** in theoretical physics — extending human knowledge rather than recombining existing code. Coined by Alex Lupsasca (2024 Breakthrough Prize winner, OpenAI researcher) on the *Latent Space* podcast (May 2026).

## Summary

Unlike "Vibe Coding" which recombines existing code patterns, Vibe Physics represents the AI-driven **extension of the knowledge frontier**. GPT-5.x models can reproduce months of human theoretical physics work in ~30 minutes and generate entirely novel results (110 pages of new graviton physics in a single day). The role of the physicist shifts from "calculator" to "architect and validator."

## Key Breakthroughs

### Reproducing Known Results at Speed

- A complex paper that took Lupsasca months to write was reproduced by GPT-5.x in **30 minutes**
- A calculation typically taking a human days was completed in **11 minutes**

### The Gluon Problem

| Aspect | Detail |
|--------|--------|
| **Challenge** | "Single-minus gluon tree amplitudes" — one equation spanned a quarter-page with 32 complex terms |
| **AI Solution** | GPT identified a "half-collinear regime" limiting case, collapsing the math into a simple, intuitive formula |
| **Novelty** | The proof used a technique previously unknown to the human authors |

### The Graviton Paper ("Vibe Physics")

- **Prompt**: "Do the same research you did for gluons, but for gravitons"
- **Output**: 110 pages of novel physics in a single day
- **Verification**: Took the human team **3 weeks** to verify
- **Result**: New paper on quantum gravity: [arXiv:2603.04330](https://arxiv.org/abs/2603.04330)

## The Vibe Physics Workflow

The interaction follows an agent-like pattern:

```
GPT: Here's your <long, detailed, awesome result>.
     Would you like me to do <another really cool thing>?
Alex: Yes, please do!
GPT: <does the really cool thing>
```

This mirrors modern AI coding agent loops but applied to **theoretical research** rather than software engineering. The model proposes novel results, and the human validates.

## Key Insights

### The "Priming Trick"

Lupsasca found that models performed better when first given a **textbook warmup problem** before being asked to solve a cutting-edge research problem. This suggests that models benefit from "in-context curriculum learning" — building up from known territory before tackling the unknown.

### The Jagged Frontier at the Science Extreme

While GPT-5's improvements on everyday tasks (email, writing) seemed incremental to the general public, capabilities at the **science frontier** had fundamentally shifted. This echoes the [[concepts/jagged-frontier]] concept: AI capability is unevenly distributed, and the most dramatic advances may occur in specialized domains invisible to most users.

### Scientist Role Transformation

| Before | After |
|--------|-------|
| Derive equations by hand | Prompt AI to derive |
| Spend months on one paper | Explore multiple avenues simultaneously |
| Do the math yourself | **Validate** AI-generated math |
| Narrow scope | Broad scope — "one theorist can achieve a lot, lot more" |

## Implications

1. **Validation is the new bottleneck** — AI can output results faster than humans can verify them (3 weeks to verify 1 day of AI output)
2. **Scope expansion** — A single theoretical physicist can now explore many more ambitious avenues simultaneously
3. **Domain-specific frontier** — The capability jump is most dramatic in specialized domains (quantum gravity) rather than general tasks

## Related Concepts

- [[concepts/vibe-coding]] — The software engineering analog: AI recombining existing code patterns
- [[concepts/jagged-frontier]] — AI capability is unevenly distributed across domains
- [[entities/openai]] — GPT-5.x models enabling this frontier

## Sources

- [🔬Doing Vibe Physics — Alex Lupsasca, OpenAI (Latent Space)](https://open.substack.com/pub/swyx/p/lupsasca) — May 5, 2026
- [Extending Single-Minus Amplitudes to Gravitons (arXiv:2603.04330)](https://arxiv.org/abs/2603.04330)
- [Full prompt-to-paper transcript (OpenAI)](https://cdn.openai.com/pdf/gluon-to-graviton-paper.pdf)
