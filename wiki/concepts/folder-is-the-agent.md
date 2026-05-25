---
title: "Folder Is the Agent"
created: 2026-05-25
updated: 2026-05-25
type: concept
tags:
  - concept
  - agent-architecture
  - agent-design-patterns
  - context-engineering
  - filesystem
  - agent-tooling
sources:
  - "raw/articles/2026-04-17_every-to_folder-is-the-agent.md"
  - "https://every.to/source-code/the-folder-is-the-agent"
---

# Folder Is the Agent

**Origin**: Kieran Klaassen (Cora GM at [[entities/every-inc|Every]]), April 2026

## Core Insight

A project folder with CLAUDE.md/AGENT.md, skill definitions, and accumulated context **IS** an agent. The context transforms a general-purpose LLM into a domain specialist — no custom infrastructure needed.

## Why This Matters

After 3 months of experimenting with agent swarms (Claude Code teams, lead-worker orchestration, nested agents), Klaassen discovered that **more agents ≠ more productivity**. The bottleneck isn't agent count — it's human review capacity. When 10 agents finish simultaneously, the human still has to evaluate 10 outputs without enough context to trust them.

## Architecture

### The Folder Structure
```
~/cora/
├── CLAUDE.md              # Conventions, standards, naming, test structure
├── .claude/
│   ├── agents/            # Specialized agents (reviewers, planners, creators)
│   └── skills/            # Capability definitions
├── docs/
│   ├── developer-docs/    # Institutional knowledge (architecture, pipelines)
│   ├── runbooks/          # Operational memory from real incidents
│   ├── investigations/    # Problem-solving patterns
│   └── postmortems/       # Learned failure patterns
└── bin/                   # Background daemons (scheduler, processors, monitors)
```

### Agent Onboarding (Reading Order)
1. Read CLAUDE.md first
2. Architecture document
3. Assistant system report
4. Assistant's prompt
5. Component creator agent

### Dispatch Layer
A lightweight Ruby daemon orchestrates the 44 folders-as-agents:
1. User types `/orchestrate "task description"`
2. Lead agent breaks task into subtasks → writes each as file
3. Daemon picks up files, spawns workers in correct folders
4. Workers inherit folder's full context
5. Workers report back by writing files
6. Daemon checks status every 60 seconds
7. Pull request appears for human review

**Key insight**: No custom networking or agent-to-agent protocol needed. Files are the communication layer.

## The Trust Principle

> "Build it, use it, trust it, orchestrate it."

Don't hand a new folder to the dispatch layer immediately. Build the flow, use it yourself, establish predictable patterns, THEN automate orchestration. Skipping this step leads to:
- Agents opening PRs for work already finished
- Duplicate issues filed by multiple agents
- Lost context and trust erosion

## Scale at Every

- **44 folders-as-agents** running across multiple projects
- Each folder = specialized agent with accumulated institutional knowledge
- Dispatch layer handles routing between folders
- Human reviews all PRs before merging

## Relationship to Industry Trends

This pattern anticipated and validates:
- **Anthropic's Claude Managed Agents** — the folder-as-agent makes managed autonomy possible: a trusted, specialized environment the model runs inside without hand-holding
- **Context Engineering** — the folder IS the context engineering layer
- **File-as-Interface** — filesystem is the most battle-tested agent interface

## Related Pages
- [[entities/every-inc]] — Where this pattern was developed
- [[entities/dan-shipper]] — Every's CEO who champions this approach
- [[concepts/compound-engineering-every]] — The broader engineering philosophy
- [[concepts/agent-native-architecture]] — Design principles this pattern exemplifies
- [[openclaw]] — Alternative agent architecture (folder-vs-hosted)
- [[concepts/context-engineering]] — The folder as context container
