---
title: "Compound Engineering (Every)"
created: 2026-05-25
updated: 2026-05-25
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
