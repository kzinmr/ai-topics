---
title: "Interactive Explanations"
type: concept
aliases:
  - interactive-explanations
  - animated-explanations
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - agentic-engineering
  - code-intelligence
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/interactive-explanations/"
---

# Interactive Explanations

A pattern for having coding agents generate **interactive animations and visualizations** to intuitively understand algorithms and concepts.

## Definition

> "A good coding agent can produce [animations and interactive interfaces] on demand to help explain code - its own code or code written by others."

Transforming abstract algorithm explanations into visually and interactively understandable formats.

## Resolving Cognitive Debt

> "When we lose track of how code written by our agents works we take on cognitive debt."

> "If the core of our application becomes a black box that we don't fully understand we can no longer confidently reason about it, which makes planning new features harder and eventually slows our progress in the same way that accumulated technical debt does."

### Cognitive Debt vs Technical Debt
| | Technical Debt | Cognitive Debt |
|--|-----------|---------|
| **Target** | Code structure | Developer understanding |
| **Cause** | Compromised design | Black-boxing of agent-generated code |
| **Impact** | Reduced maintainability | Difficulty planning new features |
| **Repayment** | Refactoring | Interactive explanations & walkthroughs |

## Practical Example: Word Cloud Algorithm

Inspired by Max Woolf's Rust word cloud app, Simon had Claude Code investigate it.

### Problem
> "Claude's report said it uses 'Archimedean spiral placement with per-word random angular offset for natural-looking layouts'. This did not help me much!"

### Solution Approach
1. **Linear Walkthrough** → Understanding Rust code structure (insufficient)
2. **Animated Explanation** → Intuitive algorithm understanding

### Animation Generation Prompt
```
Fetch https://raw.githubusercontent.com/simonw/research/refs/heads/main/rust-wordcloud/walkthrough.md to /tmp using curl so you can read the whole thing.
Inspired by that, build animated-word-cloud.html - a page that accepts pasted text (which it persists in the `#fragment` of the URL such that a page loaded with that `#` populated will use that text as input and auto-submit it) such that when you submit the text it builds a word cloud using the algorithm described in that document but does it animated, to make the algorithm as clear to understand. Include a slider for the animation which can be paused and the speed adjusted or even stepped through frame by frame while paused. At any stage the visible in-progress word cloud can be downloaded as a PNG.
```

### Results
- Animation visualizes each word's placement process
- Slider enables pausing, speed adjustment, and frame-by-frame stepping
- PNG download functionality included
- Claude Opus 4.6 has good "taste for explanatory animations"

## Why It's Effective

1. **Active learning**: Slider interaction lets you verify understanding
2. **Visualization**: Abstract concepts become concrete
3. **Shareable**: Can be shared as an HTML file
4. **Verifiable**: Since the actual algorithm is visualized, there's no gap between explanation and implementation

## Related Concepts

- [[concepts/harness-engineering/agentic-workflows/linear-walkthroughs]] — Structured code explanation (static)
- [[concepts/cognitive-debt]] — The debt to be resolved
- [[concepts/showboat]] — Walkthrough generation tool
- [[concepts/harness-engineering/agentic-engineering]] — Higher-level concept

## References
- [[entities/simon-willison]] — Pattern originator
