---
title: "OpenClaw Philosophy — Primitives Over Defaults"
type: concept
aliases:
  - openclaw-philosophy
  - primitives-over-defaults
  - openclaw-design-philosophy
created: 2026-04-18
updated: 2026-04-18
tags:
  - concept
  - openclaw
  - philosophy
  - agentic-engineering
related:
  - concepts/openclaw/_index
  - concepts/skill-architecture-patterns
  - entities/peter-steinberger
sources:
  - "elvis analysis (April 2026) — 9-hour side-by-side source code study"
  - "OpenClaw VISION.md"
  - "https://steipete.me/"
---

# OpenClaw Philosophy — Primitives Over Defaults

The core of OpenClaw's design philosophy is **"Primitives over Defaults"** — providing primitives rather than defaults. This is close to the design philosophy of the Linux kernel or Kubernetes.

## Core Principles

### 1. Explicit > Implicit
> "Tool activation correctness is better on OpenClaw than Hermes for tasks where the agent has to pick the right CLI/API from ~50 options." — elvis

Rather than having the agent guess "which skill to load" at runtime, **priority rules are explicitly written into the system prompt.**

**Implementation:** Five-Tier Skill Precedence model

### 2. Guarantees > Defaults
> "You're not getting defaults, you're getting guarantees. OpenClaw does exactly what you told it to do, nothing more, nothing less. Boring in the best way." — elvis

- Not bundling hundreds of skills by default
- Only minimal baseline skills
- Everything else explicitly added by the user

### 3. Legibility > Autonomy
> "When something breaks at 3am, you can trace it in one grep instead of guessing which skill the agent triggered." — elvis

Hermes' self-authoring skills generate new skills "like magic," but **tracking what's happening is difficult**. OpenClaw eliminates the "magic" and prioritizes deterministic behavior that can be traced with grep.

### 4. Bounded Growth > Organic Growth

| | OpenClaw (Bounded) | Hermes (Organic) |
|---|---|---|
| Skill addition | Via ClawHub, explicit approval | Agent autonomously creates |
| Limits | Byte caps, candidate caps | None |
| Security | Rejects symlinks, verified files only | Via prompting |
| Corpus degradation | Preventable (requires intent) | Occurs (Skill Explosion Problem) |

## Rails vs Linux/Kubernetes Analogy

Product positioning framework from elvis's analysis:

| | Hermes = Rails | OpenClaw = Linux/K8s |
|---|---|---|
| Value | "Opinionated defaults" | "Minimal primitives" |
| Philosophy | Happy path ready from the start | Build what you need yourself |
| Tradeoff | High initial productivity, complex customization | Initial setup required, fully controllable |
| Target | "Agent that knows 100+ things from Day One" | "Only what was instructed, nothing more, nothing less" |

## Ship Beats Perfect

> "I don't read code anymore. I weave it." — Steinberger

Steinberger's development philosophy:
- Rather than reading code line by line, "weave" it
- Shipping speed over perfection
- If it's verifiable, that's good enough (compile → run → test)
- Functional judgment (does it work?) over aesthetic judgment (spacing, naming)

## Closed Loop Principle

> "Code works well with AI because it's verifiable. You can compile it, run it, test it. That's the loop. You have to close the loop." — Steinberger

For AI agents to work effectively:
1. Structure to produce **verifiable output**
2. Prepare a CLI test runner
3. Define synthetic user flows
4. Enable agents to self-verify

## Polyagentmorous Development

> "Powered by Vienna coffee culture" — steipete GitHub bio

Steinberger **orchestrates 5-10 AI agents in parallel**:
- Claude Code
- OpenAI Codex
- Custom MCP servers
- Each agent is a specialist (file operations, web scraping, terminal automation, screenshot analysis)
- He is not a coder but a "conductor"

## Relationship with Local-First

OpenClaw's philosophy is deeply connected to the [[concepts/local-first-software]] movement:
- Local inference (Ollama, LM Studio, llama.cpp)
- Local filesystem access
- Local MCP servers
- Minimizing platform dependency

## Related

- [[entities/openclaw]] — OpenClaw concept aggregation
- [[concepts/openclaw/five-tier-precedence]] — Five-Tier Skill Precedence
- [[concepts/skill-architecture-patterns]] — Comparison with Hermes
- [[concepts/local-first-software]] — Local-first software
- [[entities/peter-steinberger]] — Designer
- [[comparisons/hermes-vs-openclaw-architecture]] — Detailed architecture comparison
