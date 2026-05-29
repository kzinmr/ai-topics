---
title: Nico Gerold
type: entity
created: 2026-05-29
updated: 2026-05-29
tags:
  - person
  - ai-agents
  - agent-skills
  - coding-agents
  - developer-tooling
  - agentic-engineering
aliases:
  - Nicolay Gerold
  - nicolaygerold
sources:
  - raw/articles/2026-05-21_vanishing-gradients_show-us-your-agent-skills-ep3.md
  - https://www.nicolaygerold.com/
  - https://github.com/nicolaygerold
  - https://ampcode.com/
  - https://sourcegraph.com/amp
---

# Nico Gerold (Nicolay Gerold)

**Nico Gerold** is a software engineer at **Sourcegraph** building **Amp** (formerly Amp Neo), a frontier coding agent platform. He is the host of the *How AI Is Built* podcast and founder of **Aisbach**, an AI consulting and venture-building firm. Based in Munich, Germany, he has been working with language models since 2019, fine-tuning them for banks and insurance companies before the current wave of LLM adoption. He is known for his provocative "Coding Agents Are Dead" thesis.

## Overview

| Field | Detail |
|-------|--------|
| **Location** | Munich, Germany |
| **Role** | Software Engineer @ Sourcegraph (Amp) |
| **Founded** | Aisbach (AI consulting + venture builder) |
| **Podcast** | How AI Is Built |
| **Known For** | "Coding Agents Are Dead" thesis, agent design patterns, postmortem introspection |
| **Started LLM Work** | 2019 — finetuning models for banking/insurance |

## Key Contributions

### Amp (Sourcegraph)
Amp is a frontier coding agent platform built for leading models and what comes next. Key differentiators:
- **Ruthlessly on the frontier**: Deletes old workflows and stale assumptions to stay close to what works now
- **Plugin system inspired by Pi**: Extensible via plugins that hook into events, add tools, standardize policy
- **Enterprise/team focus**: Thread sharing, team collaboration on agent conversations
- **Handoff system**: Built to replace /compact — preserves instructions that summaries lose
- **Skills as capabilities**: Skills bundle instructions, MCP servers, and toolboxes into self-contained packages

### "Coding Agents Are Dead" (2026)
A deliberately provocative blog post arguing the current generation of coding agents (terminal-based, locally running) is obsolete. Key arguments:
- Agents must move to **cloud/background execution** — not editing and running locally
- Products like Codex were the first to go fully cloud/background; Amp, Warp following
- The product scope must expand to cover the **entire SDLC**: design phase through validation, not just code writing
- This makes review more challenging — how to inspect changes that happen elsewhere

### How AI Is Built Podcast
Hosts conversations with AI builders about the reality of building AI agents, data systems, and language model applications in production.

## Show Us Your (Agent) Skills Episode 3 (2026-05-21)

Nico demonstrated Amp's agent architecture with a focus on **feedback loops, validation, and introspection**:

### Skills as Capabilities
- **GCloud skill**: Teaches the agent about their specific cloud infrastructure — services, components, where logs live — so it doesn't waste tokens rediscovering the setup for every thread
- **Tmux skill**: Agent can spawn tmux panes, run dev versions of Amp's CLI, send keyboard shortcuts, and inspect output — enables full reproduction of issues inside the agent's own environment
- **Design principle**: Skills are about giving agents *capabilities* (what services exist, how tools work in your specific setup), not just slash commands

### Validating Fix AND Root Cause
- **Reproduction-first debugging**: Agent spawns dev CLI in tmux, reproduces the problem (e.g., focus issue), inspects logs, verifies it's seeing the same issue
- **Focus tree inspector**: Built a debug tool specifically to let the agent inspect the widget focus tree — instead of guessing the root cause, it can *see* the actual state
- **Two validations required**: (1) Validate the *assumption about what the problem is* (root cause), (2) Validate the *fix actually works*
- **Feedback loops as primitives**: Give agents tools to gather structured information (storybook, debug panes, log aggregation) rather than adding more prompt instructions — "for things causing a lot of bugs, sit down and think what tools to give it"

### Postmortem Skill (Agent Introspection)
- A private skill that analyzes agent conversation threads to understand *why* failures occurred
- Asks structured questions: which instruction caused the mistake? Missing, conflicting, or ambiguous?
- Categorizes failures: steering issue, undo, repetition, confusion, wrong tool, missing context, under-agentic, over-agentic
- Default bias: **remove instructions rather than add** — agents tend to add new rules; push against this
- Surprising amount of failures traced to outdated documentation in agent instruction files

### System Prompt Minimalism
- Amp's system prompts are "really trimmed down" compared to most tools
- Every line must target a clear behavior — if not, rip it out
- Limited "instruction budget" — user should have as much remaining capacity as possible
- Default in skills: remove instructions, not add them — agents have a finite capacity to comply

### Review Triage Heuristics
- **Hot path vs. periphery**: Core logic (every user interacts) gets deep review; frontend/settings gets periodic cleanup passes
- **Agent strengths**: Excellent at small refactorings — iterate on one page, then tell it "apply this to 50 other components"
- **Code quality gradient**: Different standards for different code regions, priority-based review

### Frustrations
- GPT-5.5 tendency to add unnecessary helper/wrapper functions instead of inline code
- Architecture difficulties: placing logic at the right abstraction level for a given codebase area
- Growing validation challenge: agents generate functioning code that looks correct but has edge cases or violates business constraints

## Related
- [[entities/paul-iuzstin]] — Decoding AI founder; Episode 3 co-guest; researching coding agents from scratch
- [[entities/pi-agent-harness]] — Pi harness that Amp's plugin system is inspired by
- [[entities/vincent-warmerdam]] — marimo Pair; shared agent-notebook paradigm in same episode
- [[entities/hugo-bowne-anderson]] — Vanishing Gradients host; co-hosting "How to Build a Coding Agent" workshop
- [[concepts/coding-agents]] — Coding agent landscape
- [[concepts/agent-skills]] — Skill design patterns
