---
title: "AI Code Quality"
type: concept
created: 2026-04-25
updated: 2026-05-26
tags:
  - concept
  - ai-coding
  - code-quality
  - software-engineering
  - developer-tooling
  - methodology
sources:
  - raw/articles/2026-05-25_nolanlawson_using-ai-to-write-better-code-slowly.md
  - https://nolanlawson.com/2026/05/25/using-ai-to-write-better-code-more-slowly/
---

# AI Code Quality

The dominant narrative around AI coding tools is that they are "slop cannons" — tools for generating large volumes of low-quality code at high speed. However, a counter-movement argues that LLMs can be used just as effectively for **writing high-quality code slowly**, systematically finding and fixing bugs rather than maximizing output velocity.

## The Quality-First Approach

Pioneered by developers like [[entities/nolan-lawson|Nolan Lawson]], the quality-first philosophy treats AI as a **bug-finding superpower** rather than a productivity multiplier:

- Multiple models review the same PR in parallel
- Cross-checking results across models dramatically reduces false positives
- User-defined bug criteria (KISS/DRY violations, accessibility issues, missing indexes)
- Reports of **near-zero false positive rates** when using multi-model review

### The Slow Workflow

1. **Triage**: Use AI agents to fix critical and high-severity issues with developer guidance
2. **Pare down**: Skip issues where fix effort outweighs benefit
3. **Abort**: If a PR accumulates too many critical flaws, abandon the entire approach

This often uncovers **pre-existing bugs** outside the scope of the current PR. The tradeoff is clear: velocity may not increase, but codebase health improves and failure-mode understanding deepens.

## The Slop Cannon Debate

| Position | View | Proponents |
|----------|------|------------|
| **Slop cannon** | AI = rapid low-quality code generation; quality is the user's problem | Mainstream narrative |
| **Quality-first** | AI = systematic bug-finding; write better code more slowly | [[entities/nolan-lawson]], quality-focused practitioners |
| **Critical view** | AI coding produces "eternal sloptember" — endless low-quality output degrading OSS | [[entities/armin-ronacher]], [[entities/george-hotz]] |

The debate is not about whether AI can produce quality code, but about **incentives and defaults**: the path of least resistance in most AI coding tools defaults to fast generation, not careful review.

## Related

- [[entities/nolan-lawson]] — Key proponent of quality-first AI coding
- [[concepts/ai-coding|AI Coding]] — Broader AI-assisted programming landscape
- [[concepts/vibe-coding]] — The low-quality / high-velocity approach
- [[concepts/agentic-engineering]] — How developers structure AI-assisted workflows
