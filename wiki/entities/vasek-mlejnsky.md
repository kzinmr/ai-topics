---
title: "Vasek Mlejnsky"
created: 2026-10-17
updated: 2026-10-17
type: entity
tags:
  - entity
  - person
  - ai-agents
  - agent-infrastructure
sources:
  - raw/articles/2026-10-16_mlejva_sandboxes-are-dead.md
---

# Vasek Mlejnsky

**X:** [@mlejva](https://x.com/mlejva)
**Role:** CEO & co-founder of [[entities/e2b|E2B]]

## Overview

CEO of E2B, a cloud sandbox platform for AI agents founded in 2023. Writes publicly about the evolution of agent infrastructure; his October 2026 X Article "Sandboxes are dead" (390 bookmarks, ~125K impressions at capture) argues that commodity microVM sandboxes are obsolete for production agents and that the future is an "agent-driven private cloud" — one auto-optimized private cloud per agent, with the agent itself deciding which tools and resources each task needs.

## Key Ideas

- **Three-wave model of agent capability** (code snippets → app building → full computer operation), with the claim that infrastructure must be built one wave ahead of current agent capability: "Teams that build for the current wave are already one wave behind."
- **Anti-commoditization thesis:** competing on cold-start ms and $/vCPU-hour is "the wrong answer for the third wave"; sandboxes must become platforms (storage, firewall, inter-sandbox networking, observability, elastic compute, browsers, secrets).
- **Trace data as moat:** billions of production agent runs as the basis for predicting an agent's resource/tool profile before execution.

## Related
- [[entities/e2b]] — his company
- [[concepts/agent-sandbox-patterns]] — sandbox isolation taxonomy
- [[concepts/sandbox]] — sandboxing concept page

## Sources
- [[raw/articles/2026-10-16_mlejva_sandboxes-are-dead]] — "Sandboxes are dead" (X Article, 2026-10-16)
