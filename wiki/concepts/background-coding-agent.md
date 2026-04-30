---
title: Background Coding Agent
created: 2026-04-30
updated: 2026-04-30
type: concept
tags: [coding-agents, ai-agents, architecture, infrastructure]
sources: [raw/articles/2026-04-30_ramp-inspect-background-agent.md]
---

# Background Coding Agent

## Definition

A **Background Coding Agent** is an AI-powered coding assistant that runs in the cloud asynchronously, rather than in a local developer's IDE. It is given a task, spins up its own execution environment, works independently, and produces a verified pull request — all without requiring the developer to stay online or keep a session open.

## Core Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Cloud execution** | Runs on server infrastructure, not local hardware |
| **Unlimited concurrency** | Multiple sessions can run in parallel without resource contention |
| **Asynchronous workflow** | Developer submits a task, agent works independently, results delivered later |
| **Verification-first** | Built-in testing, code review, and QA capabilities |
| **Multiplayer** | Sessions are shareable; colleagues can join for live QA or review |
| **Zero-setup speed** | Environments pre-cloned and pre-installed |

## Ramp Inspect Architecture

The **Inspect** agent by Ramp demonstrates the full background agent pattern:
- **Sandbox**: Modal-based VMs with pre-built images rebuilt every 30 minutes
- **Agent framework**: [[opencode]] (open-source, server-first, typed SDK)
- **State management**: Cloudflare Durable Objects (per-session SQLite)
- **Real-time**: Cloudflare Agents SDK with WebSocket hibernation
- **Interfaces**: Slack bot, web UI (hosted VS Code), Chrome extension (visual editing)
- **Security**: PRs opened using user's GitHub token, not an app-owned bot

## Performance Optimization

- **Warm starts**: Sandbox begins pre-warming as user types the prompt
- **Immediate research**: Agent reads files immediately; edits blocked only until git sync completes
- **Build-step heavy**: Dependencies installed and test caches populated during image build

## When Background Agents Beat Local Agents

> "When background agents are fast, they're strictly better than local: same intelligence, more power, and unlimited concurrency." — Ramp Engineering

Background agents excel when:
1. Tasks require heavy infrastructure (databases, test suites, multiple services)
2. Developers need to parallelize work
3. Verification requires access to production telemetry or monitoring
4. Collaboration is needed (shared sessions, multiplayer review)

## Related Concepts

- [[modal-sandboxes]] — cloud execution environments for background agents
- [[warm-start-optimization]] — pre-warming technique for reducing latency
- [[s3-first-architecture]] — persistent storage pattern for agent state
- [[opencode]] — agent framework used by Ramp Inspect

## Sources

- Ramp Engineering, "Why We Built Our Background Agent", builders.ramp.com, April 2026
