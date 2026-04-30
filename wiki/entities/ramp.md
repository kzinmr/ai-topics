---
title: Ramp
created: 2026-04-30
updated: 2026-04-30
type: entity
tags: [company, ai-agents, coding-agents, financial-services]
sources: [raw/articles/2026-04-30_ramp-inspect-background-agent.md]
---

# Ramp

## Overview

**Ramp** is a financial technology company that has developed **Inspect**, a custom background coding agent for internal software development. As of April 2026, Inspect handles approximately **30% of all merged pull requests** at Ramp, demonstrating that production-grade background agents are viable in real engineering teams.

## Key Products

### Inspect (Background Coding Agent)

Ramp's internal AI agent for software development that:
- Runs asynchronously in the cloud
- Verifies its own work with production context
- Integrates with Slack, web UI, and Chrome extension
- Uses the user's GitHub token for PRs (not an app-owned bot)

## Architecture

### Infrastructure Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Sandbox** | [[concepts/modal-sandboxes]] | Isolated VMs with pre-built images |
| **Agent Framework** | [[entities/opencode]] | Open-source, server-first, typed SDK |
| **State Management** | Cloudflare Durable Objects | Per-session SQLite databases |
| **Real-time** | Cloudflare Agents SDK | Streaming with WebSocket hibernation |
| **Authentication** | GitHub OAuth | User-based PR creation |
| **Image Registry** | Modal | Per-repo images rebuilt every 30 min |

### Design Principles

1. **Build your own**: "Owning the tooling lets you build something significantly more powerful than an off-the-shelf tool will ever be."
2. **Fast starts matter**: "When background agents are fast, they're strictly better than local: same intelligence, more power, and unlimited concurrency."
3. **Verification is core**: Agent proves its work with tests, telemetry, and visual QA
4. **Multiplayer by design**: Sessions are shareable for collaboration and review

## Client Interfaces

| Interface | Key Feature |
|-----------|-------------|
| **Slack Bot** | Auto-classification of repos, public-channel virality, Block Kit updates |
| **Web UI** | Hosted VS Code (`code-server`), streamed desktop for computer use |
| **Chrome Extension** | Visual editing for non-engineers, DOM/React internals extraction, MDM deployment |

## Key Metrics

- ~30% of all merged PRs handled by Inspect
- 30-minute image rebuild cycle
- Unlimited concurrency via Modal

## Related Entities

- [[entities/inspect]] — Ramp's background coding agent
- [[entities/opencode]] — Agent framework used by Ramp
- [[concepts/background-coding-agent]] — Concept pioneered by Inspect
- [[concepts/modal-sandboxes]] — Execution layer

## Sources

- Ramp Engineering, "Why We Built Our Background Agent", builders.ramp.com, April 2026
