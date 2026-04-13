---
title: "Apple's Illusion of Thinking & Neurosymbolic Robotics"
created: 2026-04-13
updated: 2026-04-13
tags: [concept, neurosymbolic, robotics, apple-research, tower-of-hanoi]
aliases: ["illusion of thinking", "VLA generalization gap"]
related:
  - concepts/neurosymbolic-ai
  - entities/gary-marcus
---

# Apple's Illusion of Thinking & Neurosymbolic Robotics

## Overview

A series of research papers in 2025-2026 demonstrated that **pure LLMs fail at logical planning tasks** they appear to solve, and that **neurosymbolic hybrids dramatically outperform Vision-Language-Action (VLA) models** on robotics tasks requiring multi-step reasoning.

## Apple (2025): The Illusion of Thinking

Apple Research published a paper showing that LLMs pass small-scale Tower of Hanoi puzzles but **fail completely as disk count increases**. The key finding: LLMs appear to reason but are actually pattern-matching on training data — when the problem scales beyond seen examples, the illusion breaks.

## Tufts (Feb 2026): Duggan, Lorang, Lu, Scheutz

Extended Apple's findings to **Vision-Language-Action (VLA) robotics models**:

| Task | Neurosymbolic Model | Best VLA |
|------|-------------------|----------|
| 3-block Tower of Hanoi | **95%** success | 34% success |
| Unseen 4-block variant | **78%** success | 0% success |

The neurosymbolic model achieves **~100x (two orders of magnitude) more energy-efficient** operation than LLMs/VLAs while delivering superior generalization.

## Gary Marcus's Analysis

Marcus argues these papers validate his 25-year thesis:

> *"What the Apple paper shows, most fundamentally, regardless of how you define AGI, is that LLMs are no substitute for good well-specified conventional algorithms."*

> *"LLMs are an efficient way to pattern recognition where perfect results are not required, but an inefficient way to reason a plan. Different tools for different jobs."*

> *"As a society we could spend another trillion dollars pursue LLMs, or a trillion dollars seeking new, hybrid approaches. I for one know which I would pick."*

## Key Insight: Architecture-Task Matching

The research suggests a clear division of labor:
- **LLMs** → Probabilistic pattern recognition, natural language understanding
- **Symbolic planners** → Deterministic logic, multi-step reasoning, robotics control
- **Neurosymbolic hybrids** → Best of both — neural perception + symbolic reasoning

## Related

- [[concepts/neurosymbolic-ai]] — The broader architectural paradigm
- [[entities/gary-marcus]] — Primary advocate and analyst
- [[concepts/scaling-without-slop]] — Complementary critique of pure scaling
