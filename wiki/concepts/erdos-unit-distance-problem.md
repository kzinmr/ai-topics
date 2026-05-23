---
title: Erdős Unit Distance Problem (AI Solution)
created: 2026-05-23
updated: 2026-05-23
type: event
tags: [event, openai, reasoning, research, model, ai, announcement, interpretability]
sources: [https://www.scientificamerican.com/article/ai-just-solved-an-80-year-old-erdos-problem-and-mathematicians-are-amazed/]
---

# AI Solves 80-Year-Old Erdős Unit Distance Problem

On May 21, 2026, OpenAI announced that an internal large language model trained for general reasoning had disproved **Paul Erdős's 1946 "unit distance" conjecture** — a long-standing open problem in combinatorial geometry. It is the first AI-generated mathematical result deemed worthy of publication in a top mathematics journal.

## The Problem

**Erdős's unit distance conjecture (1946):** For a given number of points in the plane, the maximum number of pairs exactly 1 unit apart is achieved by a carefully spaced grid-like arrangement. Erdős claimed no construction could beat his grid-based approach.

For 80 years, this conjecture stood. Human mathematicians believed it was likely true and focused on proving it, not on seeking a counterexample.

## What the AI Did

OpenAI's internal model was asked whether Erdős was right. After generating **hundreds of pages** of logic and calculations, it found a **counterexample** — a point arrangement that beats the best-known grid construction.

### The Approach

The AI did NOT use a grid. Instead it:
1. Constructed a **higher-dimensional lattice** with special mathematical symmetries
2. Developed a method to **project this lattice onto the 2D plane**, producing a flattened numerical "shadow"
3. The resulting point set is "too difficult to actually draw on paper, even for a small number of dots" (Mehtaab Sawhney)

### What It Did NOT Do

- It did NOT prove optimality — only that a better construction exists
- It did NOT invent fundamentally new mathematics — it repurposed existing techniques
- Shortly after, mathematician **Will Sawin** improved upon the AI's construction, demonstrating the collaborative human-AI dynamic

## Expert Reactions

| Expert | Reaction |
|---|---|
| **Timothy Gowers** (Cambridge) | "No previous AI-generated proof has come close" to publishable quality |
| **Daniel Litt** (Toronto) | "This is the unique interesting result produced autonomously by AI so far" |
| **Mehtaab Sawhney** | "It feels like magic... it's kind of an amazing experience to have a machine give back something which really resembles how I work" |
| **Sébastien Bubeck** (OpenAI) | "The model did not invent something fundamentally new that nobody saw coming. It just executed like an amazing mathematician" |
| **Jacob Tsimerman** | "AIs have an edge: they can play for longer and in more treacherous waters than mathematicians without getting overwhelmed" |
| **Melanie Matchett Wood** | "Maybe people should be spending more time... playing devil's advocate" |

## Why the AI Succeeded Where Humans Didn't

1. **Bias toward proof**: Human mathematicians believed Erdős was correct, so they focused on proving the conjecture rather than seeking counterexamples
2. **Willingness to explore tedious paths**: The AI explored a high-dimensional construction without being dissuaded by lack of early success
3. **Brute-force exploration**: The approach was "a straightforward approach that no human had ever attempted" — the necessary mathematical tools already existed

## Caveats & Concerns

| Issue | Detail |
|---|---|
| **Verification opacity** | Raw AI output not directly shared; only an edited reasoning trace was given to external mathematicians |
| **Attribution failure** | AI borrowed ideas from literature without citation — "professional malpractice if a human did it" (Wood) |
| **No new mathematics** | Repurposed existing techniques; genuine conceptual leaps remain beyond current LLMs |
| **Incomplete solution** | Counterexample only; the maximum number of unit distances remains an open problem |

## Broader Implications

This is the first AI math result to cross the threshold of "would be published in a top journal if humans did it alone." It follows months of less impressive AI-powered math advances involving "Erdős problems" — a collection of accessible but stubbornly unsolved conjectures.

The result demonstrates a specific AI advantage in mathematics: **bias-free exploration of solution spaces that humans have prematurely foreclosed**. Daniel Litt predicts such cases "are actually not that rare."

## Related

- [[entities/openai|OpenAI]] — the company behind the model
- [[concepts/reasoning|Reasoning]] — the capability demonstrated
- [[concepts/mathematical-ai|AI in Mathematics]]
- [[concepts/ai-safety|AI Safety]] — implications for autonomous capability
