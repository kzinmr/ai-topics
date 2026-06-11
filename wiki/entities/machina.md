---
title: Machina
type: entity
created: 2026-06-01
updated: 2026-06-01
tags:
  - person
  - blogger
  - x-account
  - ai-slop
aliases:
  - "@EXM7777"
  - "Machina"
sources:
  - raw/articles/2026-05-30_exm7777_fix-ai-slop-using-hermes.md
  - https://x.com/EXM7777
related:
  - concepts/eval-loops
  - concepts/ai-slop
  - entities/hermes-agent
---

# Machina

**Machina** (@EXM7777) is an AI practitioner and writer who runs AI-powered agencies. Known for the viral X Article "How To Fix AI Slop (Using Hermes)" (May 2026), which introduced a practical 6-move framework for building automated eval loops inside [[entities/hermes-agent|Hermes Agent]].

## Key Facts

| Field | Value |
|-------|-------|
| X Handle | [@EXM7777](https://x.com/EXM7777) |
| Focus | AI-powered agencies, AI output quality |
| Website | machina.ventures |

## Notable Contributions

### How To Fix AI Slop (May 2026)

A comprehensive X Article arguing that AI slop is an **output-side systems problem**, not a prompt problem. Key thesis: the people whose AI output is consistently clean aren't better at prompting — they measure every output against a standard before it ships.

The article provides a concrete implementation guide using Hermes Agent's built-in primitives (skills, memory, cron, approval buttons) to create a self-hardening eval loop:
1. Stand up Hermes on a reachable channel
2. Load gold-standard examples into persistent memory
3. Turn quality rubric into a reusable judge skill
4. Make the test suite a versioned skill
5. Gate all changes with regression testing + approval
6. Watch production via cron for quality degradation

The framework closes the loop: flagged bad outputs automatically become new permanent test cases, raising the quality floor over time.

> "The prompt was never the system. The eval loop is the system."

## Core Ideas

1. **AI slop = missing quality layer**: Better prompts and models are input-side fixes that don't address verification. The industry has no equivalent of software testing for LLM output.
2. **Quality as a number**: A rubric-scored metric (0-1) transforms slop from a subjective feeling into a debug-able bug.
3. **Self-hardening suites**: The eval loop should automatically incorporate failures as new test cases — the quality floor rises without manual intervention.
4. **Agent-native implementation**: Hermes Agent's skills, memory, cron, and approval buttons provide all the primitives needed for a production eval loop without external tooling.

## Cross-References

- [[concepts/evaluation/eval-loops]] — The core concept page for AI eval loops
- [[concepts/ai-slop]] — The problem that eval loops are designed to solve
- [[entities/hermes-agent]] — The agent platform used for the reference implementation

## References

- [[raw/articles/2026-05-30_exm7777_fix-ai-slop-using-hermes]] — "How To Fix AI Slop (Using Hermes)"
