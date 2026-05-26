---
title: "Cognitive Debt"
type: concept
aliases:
  - cognitive-debt
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - agentic-engineering
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/interactive-explanations/"
  - "https://simonwillison.net/guides/agentic-engineering-patterns/"
  - "https://simonwillison.net/2025/Oct/30/linear-walkthrough/"
---

# Cognitive Debt

**Cognitive debt** accumulates when we lose understanding of how AI-agent-generated code works. It is the cognitive counterpart to technical debt, and is accelerated by [[concepts/vibe-coding]].

## Definition

> "When we lose track of how code written by our agents works we take on cognitive debt."

## Comparison with Technical Debt

| | Technical Debt | Cognitive Debt |
|--|-----------|---------|
| Object | Code structure | Developer understanding |
| Cause | Compromised design | Black-boxing of agent-generated code |
| Impact | Reduced maintainability | Difficulty planning new features |
| Repayment | Refactoring | Interactive explanations and walkthroughs |
| Visualization | Code metrics | **Linear Walkthrough** |

## Why It Matters

> "If the core of our application becomes a black box that we don't fully understand we can no longer confidently reason about it, which makes planning new features harder and eventually slows our progress in the same way that accumulated technical debt does."

Willison identifies cognitive debt as **the biggest problem with Vibe Coding**. In Vibe Coding, developers work in a cycle of "request in natural language → agent generates code → immediate deploy," accumulating code without understanding its detailed behavior.

> "The problem with vibe-coding is that it leads to cognitive debt."

## Cognitive Debt Mechanism

1. **Request via prompt** → agent generates code
2. **Test without reviewing** → it works, so it's OK
3. **Next feature addition** → don't understand existing code
4. **Request fix with new prompt** → even more incomprehensible code added
5. **Loop continues** → core application becomes a black box

### Vibe Coding vs Agentic Engineering

| | Vibe Coding | Agentic Engineering |
|--|------------|-------------------|
| Speed | Fastest | Moderate |
| Cognitive debt | **Accumulates heavily** | Managed and repaid |
| Testing | None or minimal | Systematic |
| Quality | Low (long-term) | High |
| Sustainability | Short-term | Long-term |

> "The key distinction between vibe-coding and agentic engineering: vibe coding produces speed at the cost of cognitive debt, agentic engineering manages that debt."

## Repayment Methods

### 1. [[concepts/harness-engineering/agentic-workflows/linear-walkthroughs]] — Structured code explanation
A CLI tool Willison built himself that displays code processing flow as a tree, making it **visually understandable** which functions are called through which paths.

```
$ llm --plugin llm-linear-walkthrough explain --file src/app.py
```

### 2. [[concepts/interactive-explanations]] — Interactive animations
Step through code execution in the browser, visualizing variable changes in real-time.

### 3. [[concepts/harness-engineering/agentic-workflows/agentic-manual-testing]] — Verification through execution
Test the actual UI using CLI browser tools like [[concepts/harness-engineering/agentic-workflows/rodney]] to verify that agent-generated features actually work.

### 4. [[concepts/showboat]] — Recording and sharing tests
Save verification results as Markdown documents so the entire team can review.

## Repayment Cycle

Cognitive debt repayment is **not a one-time event**. Agentic Engineering requires a continuous repayment cycle:

```
Code generation → Test → Understand via Linear Walkthrough → 
  Deep-dive unclear points with interactive explanations → Record verification in Showboat → 
    Next code generation
```

## References
- [[entities/simon-willison]] — Originator of the concept
- [[concepts/vibe-coding]] — Primary source of cognitive debt
- [[concepts/harness-engineering/agentic-workflows/linear-walkthroughs]] — Primary repayment tool
- [[concepts/interactive-explanations]] — Interactive understanding tool
- [[concepts/harness-engineering/agentic-workflows/agentic-manual-testing]] — Verification tool
