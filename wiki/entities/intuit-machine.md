---
title: "Intuit Machine"
type: entity
aliases: [intuit-machine]
tags: [entity, agentic-ai, skills-design, harness-engineering]
status: complete
description: "AI agent framework company focused on agentic AI skills design. Published 'Ten Design Principles of Agentic AI Skills Design' — structural insights about how AI systems achieve 10x-100x effectiveness."
created: 2026-04-27
updated: 2026-04-27
sources: [
  "https://x.com/IntuitMachine/status/2043071219667480853"
]
related: [
  "[[concepts/agentic-ai-skills]]",
  "[[concepts/agent-harness]]",
  "[[concepts/harness-engineering]]"
]
---

# Intuit Machine

## Overview

**Type:** AI Framework / Consulting Company
**Focus:** Agentic AI skills design, harness engineering, prompt-to-skill transition
**Key Publication:** ["Ten Design Principles of Agentic AI Skills Design"](https://x.com/i/article/2043069686313594880) (April 2026)

## Key Contribution: Ten Design Principles

Intuit Machine published a comprehensive framework for designing AI agent skills — reusable documents that teach AI how to approach entire categories of tasks. Their central thesis: extraordinary results (10x-100x better) come not from smarter models, but from how models are wrapped — specifically, how skills are designed.

### Core Principles

1. **Skills are recipes, not orders** — Describe processes with parameters, not one-shot commands
2. **Teach thinking, not conclusions** — Invoke judgment; don't pre-decide outcomes
3. **Draw the line between judgment and computation** — AI handles judgment; tools handle computation
4. **Read everything, synthesize** — Don't pre-filter; the power is in synthesis from full picture
5. **Right document at right moment** — Build resolvers; don't load everything everywhere
6. **Push intelligence up, push execution down** — Skills = rich, harness = thin, tools = dumb
7. **Fast and narrow beats slow and general** — Tools should do one thing in <500ms
8. **Chase "pretty good"** — OK responses contain more improvement signal than bad ones
9. **Write it once, it runs forever** — Skills compound; models improve them automatically
10. **Same process, different world** — A skill's process works across domains

## Philosophy

The key distinction: **context engineering vs prompt engineering**. Prompt engineering optimizes individual interactions ("how do I phrase this question better?"). Context engineering designs information architecture ("what information does this AI need, and how do I structure it?").

## Notable Frameworks

### Three-Layer Architecture
- **Skills** — Rich documents with process, judgment, wisdom (90% of value)
- **Harness** — Thin plumbing (200 lines max), manages context and tool calls
- **Tools** — Fast, narrow, dumb programs with deterministic behavior

### Anti-Pattern: Fat Harness
A harness with 40+ tool definitions, embedded business logic, and thin skills as afterthoughts. This is exactly backwards from the recommended approach.

## Related
- [[concepts/agentic-ai-skills]] — Their 10 design principles
- [[concepts/agent-harness]] — The harness layer in their architecture
- [[concepts/harness-engineering]] — Broader harness engineering principles
