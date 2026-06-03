---
title: "Compound Engineering (Every)"
created: 2026-05-25
updated: 2026-06-03
type: concept
tags:
  - concept
  - ai-agent-engineering
  - context-engineering
  - software-engineering
  - developer-tooling
  - feedback-loop
  - ai-automation
sources:
  - "https://every.to/guides/compound-engineering"
  - "raw/articles/2026-04-17_every-to_folder-is-the-agent.md"
  - "raw/articles/2026-06-02_mvanhorn_every-agentic-engineering-hack.md"
  - "https://github.com/steipete/openclaw"
---

# Compound Engineering

**Origin**: Kieran Klaassen and the [[entities/every-inc|Every]] engineering team, 2025-2026

Compound Engineering is Every's AI-native development philosophy where humans and AI agents work in a reinforcing loop that compounds in effectiveness over time.

## Core Philosophy

Unlike traditional software engineering where humans write all the code, Compound Engineering establishes a loop:
1. **Human sets up conditions** — prompts, context files, skills, architecture decisions
2. **AI agents do iterative work** — code generation, testing, refactoring
3. **Human reviews and refines** — taste, judgment, architectural decisions
4. **Context accumulates** — each cycle builds institutional knowledge in the project

The key insight: **each cycle makes the next cycle more effective** because the accumulated context (CLAUDE.md, runbooks, postmortems, specialized agents) makes the AI more capable.

## Relationship to Folder-Is-The-Agent

Compound Engineering is the methodology; [[concepts/folder-is-the-agent|Folder Is the Agent]] is the implementation pattern. The folder structure stores the "compound" — the accumulated knowledge that makes each iteration more productive.

## Key Practices

### Context Accumulation
- **CLAUDE.md/AGENT.md**: Coding conventions, naming standards, test structure
- **docs/developer-docs/**: Architecture reports, system design decisions
- **docs/runbooks/**: Operational patterns from real incidents
- **docs/postmortems/**: Lessons learned from failures
- **.claude/agents/**: Specialized agent configurations
- **.claude/skills/**: Reusable capability definitions

### Human-in-the-Loop Workflow
> "Build it, use it, trust it, orchestrate it."

1. **Build**: Human creates the initial flow with AI assistance
2. **Use**: Human operates the flow personally to understand it
3. **Trust**: Flow proves predictable and reliable through use
4. **Orchestrate**: Only then automate with dispatch layers

Skipping steps 1-3 leads to agents producing work that's hard to evaluate, duplicate efforts, and lost trust.

## Open Source Implementation

Every released an open-source plugin (7,000+ → 14,000+ GitHub stars) that implements Compound Engineering principles. The plugin is [[openclaw]]-compatible and provides:
- Structured context accumulation
- Agent skill definitions
- Workflow orchestration patterns

### /ce-plan Internals (from Van Horn's June 2026 deep-dive)

[[entities/matt-van-horn|Matt Van Horn]] (#3 contributor, June 2026) documented the internal mechanics of Compound Engineering's core commands:

- **`/ce-plan`** — Fans out parallel research agents simultaneously: one reads the codebase for patterns and conventions, one searches past solutions for learnings, and more research external docs and best practices. All results consolidate into a structured plan.md with: problem statement, approach, files to touch, acceptance criteria with checkboxes, and patterns grounded in the user's actual repo conventions.
- **`/ce-brainstorm`** — For fuzzy ideas where the user doesn't yet know what they want. Think through the problem with the agent first, then `/ce-plan` once sharp.
- **`/ce-work`** — Takes the plan.md and builds it. Context blows up? Start a new session, point it at the plan, pick up where you left off. The plan is the durable checkpoint.
- **`/ce-work --codex`** — Delegates the build phase directly to Codex from inside the Compound Engineering loop, without leaving the Claude session.

### "Plan for the Plan" Pattern

For non-code deep work (strategy docs, product specs, competitive analysis, board updates), the technique is to make the first plan a meta-plan:

> "/ce-plan make a plan for the plan. I'm about to hand you a PDF and a meeting transcript. I want a thoughtful plan for how these come together into a document. Do not write that document now. Writing it is the work. Right now I only want the plan for how you'll produce a great document."

This is the single best trick for preventing LLM laziness — asking for the deliverable directly causes corner-cutting; asking the agent to first plan how it will produce the deliverable forces deep work every time.

### Contributor Ecosystem

Van Horn's open source contributions illustrate how Compound Engineering creates a self-reinforcing ecosystem:
- **last30days** (27K stars) — Started as a skill he wanted for himself; now a multi-platform research tool
- **Printing Press** (3.7K stars, 320+ PRs) — CLI factory for agent-native service wrappers
- **AgentMail** — Open-sourced Claude Code email integration
- **Compound Engineering plugin** — #3 contributor behind core team

## Results at Every

- Team of ~30 runs 5 software products + media operation
- 95% of work emails handled by AI (via Cora)
- No one writes code by hand — all engineering is AI-assisted
- **44 folders-as-agents** running across projects
- AI agents (@Claudie, @Andy, @Viktor) are first-class Slack team members

## Industry Impact

Compound Engineering represents a shift from:
- **Traditional**: Human writes code → tests → deploys
- **Compound**: Human sets context → AI iterates → Human reviews → Context improves → repeat

This pattern influenced:
- Anthropic's **Claude Managed Agents** (hosted service for sandboxing, state management, tool execution)
- The broader **AI agent engineering** movement
- Open-source tooling for agent context management

## Related Pages
- [[concepts/folder-is-the-agent]] — Implementation pattern
- [[entities/every-inc]] — Origin company
- [[entities/dan-shipper]] — Every's CEO, philosophy champion
- [[concepts/agent-native-architecture]] — Design principles this embodies
- [[openclaw]] — Compatible agent platform
- [[concepts/human-sandwich]] — Human-AI collaboration pattern
- [[entities/matt-van-horn]] — #3 contributor, documented /ce-plan internals
- [[concepts/agentic-engineering]] — The broader practice Compound Engineering enables
