---
title: AskUserQuestion Pattern
created: 2026-04-30
updated: 2026-04-30
type: concept
tags: [ai-agents, prompting, harness-engineering]
sources: [raw/articles/2026-04-30_lessons-from-building-ai-agents-financial-services.md]
---

# AskUserQuestion Pattern

## Definition

The **AskUserQuestion Pattern** is an agent interaction design where an autonomous agent can **pause its execution flow** and request human clarification before proceeding with high-stakes decisions. This is implemented as a structured tool call (e.g., `AskUserQuestion`) that surfaces a specific question to the user with optional context.

## Why It Matters

In high-precision domains like financial services, agents **must not guess** when critical parameters are ambiguous. The AskUserQuestion pattern:

- Prevents errors from incorrect assumptions (e.g., using wrong financial estimates)
- Maintains human oversight for consequential decisions
- Reduces the need for post-hoc corrections

## Fintool Implementation

```
Agent: "Should I use consensus estimates or management guidance for this DCF valuation?"
User:  "Use management guidance — the company gave specific forward numbers."
Agent: [Proceeds with correct data source]
```

The tool integrates with:
- **Real-time streaming**: Questions delivered via WebSocket/Redis Streams
- **Session state**: Agent pauses without losing context
- **UI rendering**: Questions appear as interactive prompts in the user interface

## Design Principles

1. **Specific, answerable questions** — not open-ended "what do you want?"
2. **Context-rich** — provide the agent's current understanding and options
3. **Blocking but resumable** — agent pauses execution, resumes on answer
4. **Logged** — questions and answers are recorded for auditability

## Related Patterns

- [[harness-engineering/system-architecture/building-effective-agents]] — Anthropic recommends human-in-the-loop for high-stakes workflows
- [[human-in-the-loop]] — broader pattern that includes AskUserQuestion as one implementation
- [[agent-security-patterns]] — question-based verification as a security control

## Sources

- Nicolas Bustamante (Fintool), "Lessons from Building AI Agents for Financial Services", LinkedIn, April 2026
