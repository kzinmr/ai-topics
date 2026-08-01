---
title: "Agentic Engineering Patterns"
type: concept
aliases:
  - agentic-engineering-patterns
created: 2026-04-25
updated: 2026-08-01
tags:
  - concept
status: active
sources:
  - https://www.infoq.com/news/2026/03/agentic-engineering-patterns
  - raw/articles/crawl-2026-04-29-paul-duvall-agentic-patterns.md
  - https://github.com/paulDuvall/ai-development-patterns
  - raw/articles/gilesthomas.com--2026-07-ai-use--34d7bf95.md
related:
  - concepts/agentic-engineering
  - concepts/test-driven-development
  - concepts/spec-driven-development
  - concepts/subagents
---

# Agentic Engineering Patterns

Patterns and practices for building AI agent systems that reinforce — rather than replace — software engineering discipline.

## Paul Duvall, Paul Stack & Gergely Orosz (InfoQ, March 2026)

As AI increases the volume and velocity of code generation, traditional manual reviews become impractical. Engineering quality shifts from human inspection to **automated validation and agentic guardrails**.

### Key Insight: Validation over Review

> "You're putting in mechanisms... such that the code is reviewed... but it might not be reviewed literally by you every single time." — Paul Duvall (author of "Continuous Integration")

### Red, Green, Refactor — XP Revival

AI workflows are naturally replicating **Extreme Programming (XP)** patterns — the agent literally follows "red, green, refactor":

1. **Red** — Agent writes failing test (or identifies failing requirement)
2. **Green** — Agent generates code to pass
3. **Refactor** — Agent cleans up while maintaining test pass rate

This is not coincidence — the test-driven loop is the most reliable way to produce correct code, and agents converge on it naturally.

## Specification-Driven Development

Vague prompts lead to "random results." To achieve consistency, developers must provide agents structured, high-fidelity intent:

- **Intent Definition**: Structured prompts describing Role, Context, and Constraints
- **Agent-Readable Specs**: Define expected behavior and acceptance criteria upfront so agents can validate their own output
- **Issue-Based Workflows**: Paul Stack (System Initiative) suggests moving away from traditional PRs toward collaborative design via issues
- **Plan Mode**: Using Claude's "plan mode" to review intent before execution prevents "AI horror stories"

## Key Agentic Engineering Patterns

Paul Duvall's [repository of patterns](https://github.com/paulDuvall/ai-development-patterns):

| Pattern | Description |
|---------|-------------|
| **Specification-Driven** | Defining behavior and constraints before generation |
| **Codified Rules** | Embedding architectural constraints into agent context |
| **Atomic Decomposition** | Breaking tasks into small parts for parallel agents |
| **Observable Development** | Using automated traceability and production telemetry |
| **Ralph Loops** | Sub-agents iteratively refining until requirements met |

## Shift-Left and Shift-Right Integration

- **Shift-Left**: Provide accurate architectural patterns so agents produce code coherent with existing codebase
- **Shift-Right**: Use AI to analyze production telemetry expansively, identifying issues fed back as new requirements

## The Future of Engineering Role

- **Team Size**: Move toward "one pizza teams" as coordination overhead decreases
- **Identity**: Engineers move "up a level" beyond code itself
- **Taste**: Human "architectural and design taste" remains critical for high-stakes systems

## See Also
- [[concepts/agentic-engineering]]
- [[concepts/test-driven-development]]
- [[concepts/spec-driven-development]]
- [[concepts/subagents]]
- [[concepts/harness-engineering]]

## Case Study: Giles Thomas — "AIs identify problems and I fix them myself" (July 2026)

[[entities/giles-thomas|Giles Thomas]] (gilesthomas.com) documents a disciplined human-in-the-loop workflow for learning-oriented writing and coding: **"AIs identify problems and I fix them myself."** The text and code on his blog are human-generated (not a moral stand but a constraint of "learning in public"), with AI input limited to specific checkpoints:

- **Rubber duck mode**: asks LLMs to operate in a rubber-duck mode during ideation so explanations don't rob him of the learning
- **AI code review, not AI fixes**: pastes code into a chat session, tells the LLM what it's meant to do, and asks it to check for bugs — explicitly instructing it *not* to make fixes, only point them out
- **The editorial board**: drafts posts without AI, then runs them past Claude for comments on technical errors, missing steps, overexplaining, and conclusions that don't follow — again with a standing instruction *not to rewrite anything*
- **Second opinion**: ChatGPT pass with a "much more pernickety attitude" (metaphor/technical-term clashes), then a rotating cast of other LLMs (DeepSeek, Grok, GLM-5.2, Kimi K3), then a final Claude pass
- **The learning test for delegation**: "if I would learn something by writing the code, I'll write it. If not, I'm happy to delegate to an AI" — non-educational glue code (matplotlib charts, visualizers) gets delegated
- **Deliberate friction**: even for delegated code, uses chat sessions rather than agentic systems (Claude Code, Codex) "to add friction" — preventing a throwaway task from growing and consuming time/cognitive space; he *is* keen on agentic tools for non-blog projects (OpenClaw, Codex, Claude Code)

This is a concrete real-world implementation of the [[concepts/agentic-engineering|agentic engineering]] discipline: AI as amplifier with explicit human authorship and review boundaries. Contrast with fully-autonomous delegation patterns in [[concepts/multi-agents/agent-team-swarm]].

Source: [[raw/articles/gilesthomas.com--2026-07-ai-use--34d7bf95.md]]
