---
title: "Agentic Search as an Agile Engineering Process"
author: Daniel Tunkelang (co-authored with Asif Makhani)
date: 2026-03-26
source: https://dtunkelang.medium.com/agentic-search-as-an-agile-engineering-process-5514b0790e8e
type: blog-post
tags:
  - agentic-search
  - ai-agents
  - search
  - methodology
---

# Agentic Search as an Agile Engineering Process

**Authors:** Daniel Tunkelang & Asif Makhani (Infino AI) | **Published:** March 26, 2026

## Core Thesis

**Agentic search** is not a one-time implementation but a continuous, adaptive engineering process. It evolves through short development cycles, data-driven iteration, and closed-loop learning — much like Agile software development.

> "Search is what engineering looks like when the specification is missing."

## Search as Engineering without a Specification

A traditional software project starts with a specification. Search does not. A query is an incomplete, often ambiguous description of a goal. The system must infer intent, explore interpretations, and iteratively construct an answer.

From this perspective:
- The query is a partial specification.
- Retrieval and reasoning comprise implementation.
- Results represent candidate solutions.
- Interaction becomes part of the evaluation loop.

## Agentic Search as Managing a Workflow

Traditional search executes in a single pass. Agentic systems do not:
- Break problems into subtasks.
- Delegate subtasks to tools.
- Explore multiple paths.
- Refine based on intermediate results.

> "Agentic search no longer executes queries. It manages workflows."

## Iteration as Uncertainty Reduction

Agile development is fundamentally about reducing uncertainty through iteration. Each step should be evaluated not just by what it produces, but by **how much uncertainty it removes per unit of cost**. This reframes the agentic search process as a sequence of uncertainty-reducing experiments.

## The Scope–Cost–Quality Triangle

| Dimension | Definition in Agentic Search |
|-----------|------------------------------|
| **Scope** | How much of the problem space the search covers |
| **Cost** | Aggregate spend on tokens, tool calls, computation |
| **Quality** | Correctness, completeness, and confidence |

**Three strategies:**
1. **Fixed cost + quality, reduce scope** — narrow focus, high-confidence paths, early stopping (default)
2. **Fixed scope + quality, increase cost** — broader exploration, aggressive verification ("deep research")
3. **Fixed scope + cost, sacrifice quality** — skimming, summarization, lower confidence ("quick overview")

## Searchers as Product Owners, Agents as Engineers

In agile, the product owner defines goals while engineers own execution. In agentic search:
- **Searcher = Product Owner** — defines and prioritizes the information need
- **Agents = Engineers** — own all aspects of execution

However, searchers may not know what they want until they see it. Unlike software iterations measured in days, agentic search iterations are measured in **minutes or seconds** — making the loop tighter, faster, and more volatile.

## Task Sizing: A Critical Challenge

Larger tasks increase efficiency by reducing coordination overhead but increase risk. Smaller tasks reduce risk but decrease efficiency. The optimal tradeoff balances:
- Coordination cost vs. expected cost of errors
- Number of steps an agent takes
- How much reasoning per step
- How often the agent verifies its path

> "This is one of the most important — and underexplored — design decisions in agentic search workflows."

## The Cost of Iteration: Unpredictability

Agentic search inherits — and amplifies — agile's lack of predictability:
- Searcher doesn't know: number of steps, branches to explore, sources of uncertainty
- Forcing predictability leads to: premature stopping, shallow exploration, lower-quality results

> "Predictability is not the goal for which agentic search can or should optimize."

## Replacing Predictability with Evaluability

Agile replaces predictable completion with predictable progress. Agentic search goes further:
- Does not define "done" upfront; detects completion using evaluation
- The question is never "How many steps remain?" but **"Is further work worth the cost?"**
- An agentic system is "done" when spending more is not expected to improve outcome quality

## Testing is the Definition of Done

In software, "done" = passing tests. In agentic search, **evaluation replaces the definition of done**:

| What to evaluate | Focus |
|-----------------|-------|
| **Outcome** | Correctness, completeness, usefulness |
| **Process** | Validation of exploration and verification strategies |
| **Efficiency** | Maximization of ROI, minimization of wasted effort |

## Testing Replaces Explainability

Explainability is incompatible with modern neural AI-powered search methods. What we need is not explainability, but the ability to **test the process** — evaluate outcomes and audit processes.

## Three Interacting Layers

Agentic search brings together:
1. **Agile, iterative workflow** to reduce uncertainty
2. **Scope–cost–quality constraints** and tradeoffs
3. **Evaluation process** establishing a definition of done

Together, these form a **control system for reasoning under uncertainty**.

## Design Principles

- Prioritize steps that maximize uncertainty reduction per unit of spend
- Dynamically adjust scope based on budget and confidence
- Size tasks to balance coordination costs against expected costs of errors
- Integrate verification into iteration and refinement processes
- Define and enforce evaluation-driven stopping criteria

## Final Thought

> "The shift — from execution to evaluation — is what turns search into an engineering problem and motivates an agile approach."
