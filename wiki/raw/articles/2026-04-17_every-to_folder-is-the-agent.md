---
title: "The Folder Is the Agent"
author: "Kieran Klaassen"
source: "every.to/source-code/the-folder-is-the-agent"
date: "2026-04-17"
tags: ["agent-architecture", "folder-as-agent", "dispatch-layer", "compound-engineering"]
---

# The Folder Is the Agent

Key insight: A project folder with CLAUDE.md/AGENT.md, skill definitions, and accumulated context IS an agent. The context transforms a general model into a specialist.

Kieran Klaassen (Cora general manager at Every) spent 3 months trying agent swarms, found that more agents ≠ faster. The real leverage: specialized folders with institutional knowledge.

## Architecture: Folder-as-Agent
- CLAUDE.md: conventions, standards, naming, test structure
- docs/developer-docs/: institutional knowledge (architecture, pipelines, system design)
- docs/runbooks/ and docs/investigations/: operational memory from real incidents
- .claude/agents/: specialized agents (reviewers, planners, component creators)
- .claude/skills/: capability definitions
- bin/: background daemons (scheduler, inbox processor, health monitor)
- docs/postmortems/: learned patterns

## Dispatch Layer
Ruby daemon watches directory for spawn requests:
1. User types /orchestrate "task description"
2. Lead agent breaks task into subtasks, writes each as file
3. Daemon picks up files, spawns worker agents in correct folders
4. Workers inherit folder's full context (CLAUDE.md, agents, knowledge)
5. Workers report back by writing files
6. Daemon checks status every 60 seconds
7. PR appears for human review

## Key Principle: Build, Use, Trust, Orchestrate
Don't hand folders to dispatch immediately. Build the flow, use it yourself, establish trust, THEN orchestrate. Skipping this leads to duplicate work and lost context.

## Scale
Running 44 folders-as-agents across multiple projects.

## Connection to Claude Managed Agents
Anthropic's Claude Managed Agents handles sandboxing, state management, tool execution — the folder-as-agent pattern makes managed autonomy possible.
