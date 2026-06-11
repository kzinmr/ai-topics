---
title: "Code Hoarding / Knowledge Accumulation"
type: concept
aliases:
  - hoarding
  - knowledge-hoarding
  - skill-hoarding
created: 2026-04-13
updated: 2026-05-27
tags:
  - concept
  - agentic-engineering
  - person
status: complete
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/"
---

# Code Hoarding / Knowledge Accumulation

A practice advocated by Simon Willison where developers intentionally accumulate learned skills and solutions for reuse.

## Definition

> "Every time I write some code to solve a problem I save it. The next time I have a similar problem, I can reuse what I've already written — and improve it if it's still not quite right. It's hoarding, but a productive kind of hoarding."

## Accumulation Mechanism

1. **Write code to solve a problem**
2. **Save that code** (scripts, utilities, snippets)
3. **Reuse it for the next similar problem**
4. **Improve if necessary**
5. **Save again**

## Power in the Age of Coding Agents

Willison notes this pattern becomes more powerful in the AI coding agent era:

> "The more things I know how to do, the more I can compose together to do new things. And the more I can compose together, the more useful my hoard becomes to a coding agent."

**Integration with agents**:
- Accumulated skills can be reused as context passed to LLMs
- Collections of small utility scripts become "initial context" for larger projects
- Coding agents can improve and reorganize hoarded code

## Composability

Combining accumulated components to build more complex solutions — this is the true value of the "hoard."

```
Utility A (file processing)
Utility B (data transformation)
Utility C (API client)
→ A + B + C = Complete data pipeline
```

## Related Concepts
- [[concepts/harness-engineering/agentic-workflows/compound-engineering-loop]] — Iterative improvement cycle (the hoard grows during the "Save" phase)
- [[concepts/harness-engineering/agentic-engineering]] — Agentic Engineering overview
- [[concepts/context-engineering/context-window-management|Context Window Management]] — Context window management (the hoard functions as context)
