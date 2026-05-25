---
title: "Human Sandwich Pattern"
created: 2026-05-25
updated: 2026-05-25
type: concept
tags:
  - concept
  - human-sandwich
  - human-agent-collaboration
  - human-in-the-loop
  - agent-design-patterns
sources:
  - raw/articles/2026-05-21_after-automation.md
---

# Human Sandwich

> "Humans are the bread on either end of the AI's work." — Kieran Klaassen, GM of Cora at Every

A collaboration pattern for complex AI-assisted work where the human frames the task and judges the output, while the AI does the heavy lifting in between. Named by [[kieran-klaassen|Kieran Klaassen]].

## Pattern

```
[HUMAN: define task, point at right things]
         ↓
    [AI: do the work]
         ↓
[HUMAN: review, correct, decide]
```

The human is "the bread on either end of the AI's work" — crucial at both the input (framing, direction) and output (validation, judgment) stages.

## When to Use

- **Complex, creative work** where the right approach isn't obvious upfront
- **Tasks requiring judgment** about what "good" looks like
- **Iterative refinement** where human taste improves the result
- **High-stakes output** where AI alone isn't trusted

## How It Works at Every

All complex work at Every follows this pattern:

| Domain | Tool | Human Role | AI Role |
|---|---|---|---|
| Coding | Codex, Claude Code | Plan features, review output, tune compound engineering systems | Write code |
| Writing | Codex's in-app browser (Proof) | Set direction, refine taste | Draft paragraphs, research examples, copy edit |
| Email | Cora inside Codex browser | Review drafts, talk through inbox with Monologue | Draft responses (95% of CEO's work emails) |

## Contrast with Agent Employees

| Dimension | Human Sandwich | Agent Employees |
|---|---|---|
| Human involvement | Synchronous, continuous | Async, periodic maintenance |
| Task complexity | Complex, creative | Routine, well-defined |
| Tooling | Shared workspace (Codex, Claude Code, Cowork) | @-mentions in Slack, embedded in products |
| Examples | Coding features, writing essays, managing inbox | Claudie (sales proposals), Andy (newsletter digest), Viktor (growth metrics) |

See [[concepts/after-automation]] for the broader paradox this pattern lives within.

## Related Pages

- [[concepts/after-automation]] — The automation paradox
- [[entities/kieran-klaassen]] — Originator of the concept
- [[entities/every-inc]] — Where this pattern is practiced
- [[concepts/compound-engineering-every]] — Every's AI-native development philosophy
- [[concepts/agent-employees]] — The alternative async mode
