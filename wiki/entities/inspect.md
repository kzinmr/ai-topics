---
title: Inspect (Ramp)
created: 2026-04-30
updated: 2026-04-30
type: entity
tags: [product, coding-agents, ai-agents]
sources: [raw/articles/2026-04-30_ramp-inspect-background-agent.md]
---

# Inspect

## Overview

**Inspect** is a **background coding agent** developed by [[entities/ramp]] Engineering. As of April 2026, it handles approximately **30% of all merged pull requests** at Ramp. Unlike off-the-shelf coding assistants, Inspect is deeply integrated into Ramp's specific infrastructure and development workflow.

## Key Capabilities

| Capability | Description |
|------------|-------------|
| **Self-Verification** | Runs tests, reviews telemetry, queries feature flags, visually verifies changes |
| **Unlimited Concurrency** | Cloud-based sessions scale without taxing local hardware |
| **Multiplayer Support** | Sessions are shareable for live QA and collaborative review |
| **Zero-Setup Speed** | Pre-cloned, pre-installed environments ready in seconds |
| **Multi-Interface** | Works via Slack bot, web UI (hosted VS Code), and Chrome extension |

## Architecture

### Infrastructure Stack
- **Sandbox**: [[concepts/modal-sandboxes]] with per-repo images rebuilt every 30 minutes
- **Agent Framework**: [[entities/opencode]] (open-source, server-first, typed SDK)
- **State**: Cloudflare Durable Objects (per-session SQLite)
- **Streaming**: Cloudflare Agents SDK with WebSocket hibernation
- **Auth**: GitHub OAuth, PRs opened via user's token (not app-owned bot)

### Optimization Tactics
- **Warm Starts**: Sandbox warms as user types prompt
- **Immediate Research**: Agent reads files immediately; edits blocked until git sync completes
- **Build-Step Heavy**: Dependencies and test caches pre-populated during image build

## Why Build Instead of Buy?

> "Owning the tooling lets you build something significantly more powerful than an off-the-shelf tool will ever be. After all, it only has to work on your code."

Inspect's advantages over commercial tools:
1. Deep integration with Ramp's specific infrastructure (Postgres, Sentry, Datadog)
2. Custom verification workflows (before/after screenshots, telemetry review)
3. No token-based billing constraints
4. Ability to iterate on agent capabilities independently

## Related Entities

- [[entities/ramp]] — Parent company
- [[entities/opencode]] — Agent framework used
- [[concepts/background-coding-agent]] — The architectural pattern Inspect embodies
- [[concepts/modal-sandboxes]] — Execution environment
- [[concepts/warm-start-optimization]] — Performance technique used

## Sources

- Ramp Engineering, "Why We Built Our Background Agent", builders.ramp.com, April 2026
