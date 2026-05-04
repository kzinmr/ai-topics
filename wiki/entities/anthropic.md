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
updated: 2026-05-04
sources: [
  "https://x.com/RLanceMartin/status/2041927992986009773",
  "raw/articles/openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md",
  "raw/newsletters/2026-04-26-openai-is-cooking-the-anthropic-sweep-and-spacex-courts-cursor.md",
  "raw/articles/2026-04-28-anthropic-claude-creative-coalition.md",
  "raw/articles/2026-04-30-anthropic-claude-security-public-beta.md",
  "raw/newsletters/2026-05-03-gemini-gets-to-work-claude-s-big-pull-and-openai-unchained.md"
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

### Creative Coalition (Apr 2026)

Anthropic launched **9 connectors** for professional creative tools, positioning Claude as a hub for creative and professional workflows:

| Connector | Functionality |
|-----------|--------------|
| **Adobe for Creativity** | 50+ Creative Cloud tools (Photoshop, Premiere, Express) for design workflows |
| **Autodesk Fusion** | Natural language control for 3D modeling and engineering design |
| **Blender** | MCP-based connector; Python API natural-language interface; Anthropic donated to Blender Foundation |
| **Affinity by Canva** | Batch image adjustments, layer renaming, file export automation |
| **SketchUp** | Room/furniture descriptions → 3D model starting points |
| **Ableton** | Product documentation for Live and Push (music production) |
| **Splice** | Royalty-free sample catalog search within Claude |
| **Resolume** | Real-time VJ/live visual artist control (Arena/Wire) |

- Built on **MCP (Model Context Protocol)** — interoperable with other LLMs
- Educational partnerships: RISD, Ringling College, Goldsmiths University
- Part of Anthropic's enterprise expansion strategy alongside Managed Agents

### Claude Security (Public Beta, Apr 2026)

Anthropic launched **Claude Security** in public beta for Enterprise customers, powered by **Claude Opus 4.7**:

- **Deep Code Reasoning**: Traces data flows, reads source code, examines file interactions — beyond pattern matching
- **Vulnerability Insights**: Confidence ratings, severity/impact assessment, reproduction steps
- **Targeted Patching**: Generates fix instructions; open and apply directly in Claude Code on the Web
- **Workflow Integration**: Scheduled scans, directory targeting, CSV/Markdown exports, webhooks to Slack/Jira
- **Ecosystem Partners**: CrowdStrike, Microsoft Security, Palo Alto Networks, SentinelOne, TrendAI, Wiz
- **Services Partners**: Accenture, BCG, Deloitte, Infosys, PwC

### Claude Security Performance

- **Claude Mythos** found **271 zero-day vulnerabilities in Firefox** in one sweep — ~4× what Mozilla patched in all of 2025
- Early users report moving from "scan to applied patch" in a single sitting
- Multi-stage validation pipelines reduce false positives

### Market Position (May 2026)

Anthropic leads enterprise AI adoption with strong market metrics:
- **40%** of enterprise LLM spend (surpassing OpenAI)
- **54%** of enterprise coding market share
- **$30B ARR** (annual recurring revenue)
- **IPO target**: October 2026 at $400–500B valuation
- Cleaner unit economics than OpenAI; focused on enterprise over consumer scale

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
- [[claude-mythos]] — Claude Mythos model (used by Claude Security)
- [[foundation-capital]] — Partner in Claude Managed Agents
- [[concepts/claude-managed-agents]] — Managed Agents platform details
- [[concepts/project-glasswing]] — Defensive security initiative

## References

- 2026-04-12-anthropic-openclaw-subscription-ban
- 2026-04-15-property-based-testing-anthropic

- 2026-04-26-claude-code-anthropic-agentic-coding-system
- anthropic-claude-code-session-management-1m-context
