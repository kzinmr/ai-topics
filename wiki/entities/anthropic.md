---
title: "Anthropic"
type: entity
aliases: [anthropic]
tags:
  - entity
  - model
  - anthropic
  - managed-agents
  - safety-research
status: complete
description: "AI safety-focused company behind Claude. Launched Claude Managed Agents for enterprise deployment. Also released Claude Code CLI agent and Promptfoo for prompt testing."
created: 2026-04-27
updated: 2026-04-28
sources: [
  "https://x.com/RLanceMartin/status/2041927992986009773",
  "raw/articles/openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md",
  "raw/newsletters/2026-04-26-openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md"
]
related: [
  "[[anthropic]]",
  "[[claude-code]]",
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
- Memory stored as files (editable, exportable, auditable, versionable, rollback via API) — not a black-box vector store
- Mounted at `/mnt/memory/<store-name>/` in agent containers
- Multiple agents can access the same memory store with real-time sync
- Concurrency handling prevents agents from overwriting each other's updates
- Memories can be exported via the API
- Files are interpretable and sharable

The filesystem-as-memory approach was validated through [DavidSHershey's Claude Plays Pokémon experiment](https://x.com/DavidSHershey), showing that later models (Opus 4.6) learn to organize memory files much more effectively than earlier ones (Sonnet 3.5).

See [[concepts/claude-managed-agents]] for full details.

### Live Artifacts in Cowork

Anthropic introduced **live artifacts** in Cowork mode (Apr 2026):
- Dashboards and trackers stay connected to apps/files
- Pulls fresh data on reopen — persistent live views

### Consumer Connectors

Claude now integrates with 15 new everyday consumer apps:
Booking.com, Resy, Spotify, Audible, Instacart, AllTrails, Thumbtack, TurboTax, Uber, and more.
Directory now exceeds **200 connectors** total.

### Claude Design (Apr 2026)

Anthropic launched **Claude Design**, an AI-driven design tool focused on marketing assets and brand creation:
- Requires importing design systems first (fonts, colors, components) — aligns with Google's proposed **Design MD** standard
- **Strengths**: Marketing assets, landing pages, brand kits, content-to-slides workflows
- **Weaknesses**: Complex product UX and app components (struggles with reasoning under rigid constraints)
- **Signature style tell**: Overuses italicized serif fonts on landing pages
- **Iteration speed**: 5–10 minute generation cycles per tweak vs. Figma's instant feedback
- Represents Anthropic's expansion beyond language models into creative tooling
- GPT Image 2.0 + Codex integration makes standalone design tools like Claude Design potentially redundant

### Claude Code

Anthropic's CLI coding agent (see [[claude-code]]). A terminal-based agent that can:
- Read, write, and edit code
- Run commands
- Understand codebases at scale
- Operate via CLAUDE.md configuration

## Claude

Claude is Anthropic's flagship language model series. Key versions referenced in recent discussions:
- **Claude Opus** — Most capable
- **Claude Sonnet** — Balanced capability and speed
- **Claude Haiku** — Fast, efficient

## Mythos Breach (Apr 2026)

Anthropic's internal "too dangerous to release" model **Mythos** was accessed on launch day by four individuals in a private Discord. The group:
- Guessed the endpoint URL from naming conventions + a Mercor breach leak
- Used a contractor's legitimate evaluation credentials
- Used the model to build simple websites (not malicious purposes, but the access was unauthorized)

The incident highlights risks of: inference endpoint discoverability, credential sharing among contractors, and naming convention predictability.

## Research Focus

Anthropic's research priorities:
- AI safety and alignment
- Constitutional AI
- Scalable oversight
- Interpretability

## Related
- [[anthropic]] — The model family
- [[claude-code]] — Claude Code CLI agent
- [[foundation-capital]] — Partner in Claude Managed Agents

## References

- 2026-04-12-anthropic-openclaw-subscription-ban
- 2026-04-15-property-based-testing-anthropic

- 2026-04-26-claude-code-anthropic-agentic-coding-system
- anthropic-claude-code-session-management-1m-context
