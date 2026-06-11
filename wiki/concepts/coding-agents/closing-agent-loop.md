---
title: "Closing the Agent Loop — Write/Catch/Fix/Merge"
aliases:
  - closing-the-agent-loop
  - agent-autofix
  - write-catch-fix-merge
created: 2026-04-13
updated: 2026-06-07
tags:
  - concept
  - agentic-engineering
  - cognition
  - coding-agents
  - automation
related:
  - "[[cognition-devin-philosophy]]"
  - "[[agentic-engineering-patterns]]"
  - "[[concepts/evaluation/evals-for-ai-agents]]"
  - "[[ai-agent-engineering/_index]]"
sources:
  - "https://cognition.ai/blog/closing-the-agent-loop-devin-autofixes-review-comments"
  - "https://cognition.ai/blog/devin-review"
---

# Closing the Agent Loop — Write/Catch/Fix/Merge

A fully automated loop for coding agents and review processes, published by Cognition in January–February 2026.

## Background: Review Becomes the New Bottleneck

> *"Agents are generating code faster than teams can review them. The human bottleneck shifts from writing code to reviewing it."*
> — "Closing the Agent Loop"

Findings from Devin Review (January 2026):

- The **"Lazy LGTM problem"** — as PR volume increases, review quality degrades
- "Never in the field of software engineering has so much code been created by so many, yet shipped to so few"
- Traditional GitHub PR reviews assume small PRs and cannot cope with large-scale AI-generated code

## Write → Catch → Fix → Merge Loop

```
┌─────────┐    ┌──────────┐    ┌─────────┐    ┌──────────┐
│  WRITE   │───▶│  CATCH   │───▶│  FIX    │───▶│  MERGE   │
│  Devin   │    │  Review  │    │  Devin  │    │  Human   │
│  writes  │    │  bots    │    │  auto-  │    │  decides │
│  code    │    │  find    │    │  fixes  │    │          │
│          │    │  issues  │    │         │    │          │
└─────────┘    └──────────┘    └─────────┘    └──────────┘
                     │                │
              ┌──────┴────────────────┴──────┐
              │  Bot Triggers (Lint, CI,     │
              │  Security Scanner, Deps)     │
              └──────────────────────────────┘
```

### Step Details

| Step | Owner | Description |
|---------|--------|------|
| **Write** | Devin (coding agent) | Plan → Implement → Self-test → Create PR |
| **Catch** | Devin Review + bot swarm | Intelligent diff organization, AI bug detection (Red/Yellow/Gray), Lint/CI/Security |
| **Fix** | Devin (automatic) | Auto-fix triggered by bot comments. No human intervention |
| **Merge** | Human (judgment only) | Final review of architecture, product direction, edge cases |

### Bot Triggers

Bots that Devin can automatically handle:

- **Linter** — Code style, syntax errors
- **CI/CD** — Test failures, build errors
- **Security Scanner** — Vulnerabilities, dependency issues
- **Dependency Manager** — Updates, compatibility

> *"No human in the loop for mechanical fixes."*

## Why Two Agents Are Needed

> *"Why couldn't the code just be correct the first time? Even the best engineers might not catch everything on their first pass — you're focused on solving the problem, not stress-testing the solution."*

- **Writing Agent**: Focused on problem-solving. Cannot cover everything on the first pass
- **Reviewing Agent**: Intensive validation after diff completion. Catches issues that deviate from the original plan
- This separation mimics the human code review process of "write then verify"

## Devin Review's Three Capabilities

1. **Intelligent Diff Organization** — Organizes changes by logical groups rather than alphabetical order
2. **Interactive Chat** — Ask Devin questions within the PR (understands the entire codebase)
3. **AI Bug Detection** — Classified as Red (definite bug), Yellow (warning), Gray (FYI)

## Unresolved Gaps

> *"There's still a gap: running the app, clicking through flows, writing unit tests. We're closing it."*

- Running the app and testing UI flows
- Auto-generating unit tests
- These have been addressed in Devin 2.2 via Computer Use

## Comparison with Simon Willison

| Dimension | Cognition (Write/Catch/Fix/Merge) | Simon Willison |
|------|-----------------------------------|----------------|
| Testing | AI bug detection + Bot Autofix | Red/Green TDD + First Run Tests |
| Review | Devin Review (AI-organized) | Human review with context |
| Automation | Full delegation to agents | Human-centric, agent-assisted |
| Quality | "No human in the loop for mechanical fixes" | "You remain responsible for final correctness" |

## Related

- [[cognition-devin-philosophy]] — Cognition's overall philosophy
- [[agentic-engineering-patterns]] — Agentic Engineering pattern collection
- [[concepts/evaluation/evals-for-ai-agents]] — Agent evaluation
- [[ai-agent-engineering/_index]] — AI Agent Engineering system design
