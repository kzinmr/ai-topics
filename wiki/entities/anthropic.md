---
title: "Anthropic"
type: entity
aliases: [anthropic]
tags: [entity, llm-company, claude, managed-agents, safety-research]
status: complete
description: "AI safety-focused company behind Claude. Launched Claude Managed Agents for enterprise deployment. Also released Claude Code CLI agent and Promptfoo for prompt testing."
created: 2026-04-27
updated: 2026-04-27
sources: [
  "https://x.com/RLanceMartin/status/2041927992986009773"
]
related: [
  "[[claude]]",
  "[[concepts/claude-code]]",
  "[[foundation-capital]]"
]
---

# Anthropic

## Overview

**Type:** AI Company
**Founded:** 2021
**Focus:** AI safety, constitutional AI, Claude language models, Claude Code
**Key Products:** Claude (LLM), Claude Code (CLI agent), Claude Managed Agents, Promptfoo

## Claude Managed Agents (Apr 2026)

Anthropic launched Claude Managed Agents — a platform for deploying autonomous AI agents in enterprise environments. Key features:
- Enterprise security and compliance (SOC2, HIPAA readiness)
- Governance and auditability for agent actions
- Integration with existing enterprise systems
- Foundation Capital partnership for go-to-market

### Memory Stores

Claude Managed Agents now supports persistent **memory stores** (April 2026):
- Memory stored as files, accessible across sessions
- Mounted at `/mnt/memory/<store-name>/` in agent containers
- Multiple agents can access the same memory store with real-time sync
- Concurrency handling prevents agents from overwriting each other's updates
- Memories can be exported via the API
- Files are interpretable and sharable

The filesystem-as-memory approach was validated through [DavidSHershey's Claude Plays Pokémon experiment](https://x.com/DavidSHershey), showing that later models (Opus 4.6) learn to organize memory files much more effectively than earlier ones (Sonnet 3.5).

See [[concepts/claude-managed-agents]] for full details.

## Claude Code

Anthropic's CLI coding agent (see [[concepts/claude-code]]). A terminal-based agent that can:
- Read, write, and edit code
- Run commands
- Understand codebases at scale
- Operate via CLAUDE.md configuration

## Claude

Claude is Anthropic's flagship language model series. Key versions referenced in recent discussions:
- **Claude Opus** — Most capable
- **Claude Sonnet** — Balanced capability and speed
- **Claude Haiku** — Fast, efficient

## Research Focus

Anthropic's research priorities:
- AI safety and alignment
- Constitutional AI
- Scalable oversight
- Interpretability

## Related
- [[claude]] — The model family
- [[concepts/claude-code]] — Claude Code CLI agent
- [[foundation-capital]] — Partner in Claude Managed Agents
