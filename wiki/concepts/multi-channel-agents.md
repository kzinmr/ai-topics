---
title: "Multi-Channel Agents — Multi-User Engineering for Slack, Discord, and Telegram"
type: concept
created: 2026-05-29
updated: 2026-05-29
tags:
  - concept
  - ai-agents
  - multi-agent
  - orchestration
  - platform
  - communication
  - security
  - architecture
  - context-engineering
  - sandbox
sources:
  - raw/articles/2026-05-28_mastra-multi-user-multi-channel-agents.md
  - https://x.com/i/article/2059808126468243457
related:
  - "[[entities/mastra]]"
  - "[[entities/slack]]"
  - "[[concepts/security-and-governance/agent-containment]]"
  - "[[concepts/security-and-governance/agent-sandboxing-patterns]]"
  - "[[concepts/harness-engineering/agentic-loop]]"
  - "[[entities/hermes-agent]]"
  - "[[concepts/mcp]]"
---

# Multi-Channel Agents — Multi-User Engineering for Slack, Discord, and Telegram

> An agent in 2025 was single-player: it lived in a browser, your local CLI or code editor. Agents today are multi-player: built for Slack, Discord, and Telegram. When an agent stops talking to one user 1:1 and starts talking to a room full of users all typing at once, every layer of the stack needs a rethink.

## The Multi-User Challenge

The transition from single-user to multi-user agents touches **concurrency, attribution, permissions, memory scoping, tool approval, and sandbox isolation** — every architectural layer.

### Thread Isolation

Each platform conversation maps 1:1 to an agent thread:

| Platform | Thread Identity | Notes |
|----------|-----------------|-------|
| **Slack** | `channel_timestamp` (thread) | Direct messages, channel threads, top-level mentions each get their own memory scope |
| **Discord** | Thread ID | Per-server channel threads |
| **Telegram** | Chat ID | Individual and group chats |
| **Teams** | Bot framework thread | OAuth + bot framework auth model |

Each DM, each channel thread, each top-level mention gets its own independent memory scope and message history.

### Resource-Based Memory Boundaries

Memory is scoped by **resource identity**: `${platform}:${userId}` (e.g., `slack:U06CK1E9HN2`). Working memory is keyed by resource, so user X's context follows X across threads and stays invisible to user Y.

In multi-user threads (a Slack channel with five participants), the resource ID is bound to whoever started the thread. Other participants' messages land in the same thread, so the agent reads the full conversation.

### Prior Thread Context

On first non-DM mention in a thread, the agent pulls up to `threadContext.maxMessages` (default 10) prior messages. These are prepended as a single text block (not separate user messages — some providers reject consecutive user roles like DeepSeek). Each line is prefixed with the author's name and platform message ID so the model can reference specific messages.

## Platform Auth Diversity

While the wire protocol is uniform across platforms, auth models are wildly different:

| Platform | Auth Mechanism |
|----------|---------------|
| **Slack** | HMAC-SHA256 signature verification + Manifest API for programmatic app creation |
| **Discord** | Interactions endpoint |
| **Telegram** | Long-polling |
| **Teams** | OAuth + Bot Framework |

### Slack-Specific Infrastructure

Mastra's implementation (with equivalents on all platforms):

1. **OAuth + Programmatic App Creation**: `SlackManifestClient` calls Slack's Apps Configuration API (refresh-token-based) to create the app, set scopes, register event subscriptions
2. **Request Signature Verification**: HMAC-SHA256 with 5-minute replay window, run before events reach the adapter
3. **Webhook Routes**: `/slack/events/:webhookId`, `/slack/oauth/callback`, `/slack/connect` surfaced via `provider.getRoutes()`
4. **Credential Storage + Encryption**: AES + HKDF. Every credential encrypted at rest in `ChannelInstallation` records
5. **Token Rotation**: Slack rotates config tokens; `onTokenRotation` fires; agent re-encrypts and re-persists
6. **Multi-Tenant Adapter Lifecycle**: `Map<installationId, SlackAdapter>` restored and re-registered on startup via `__registerAdapter`

## Architectural Layers Impacted

### Memory Scoping
- Per-thread message history (1:1 mapping with stable thread IDs)
- Per-user resource isolation (`platform:userId` keyed working memory)
- Cross-thread visibility only for the agent (reads full conversation in shared channels)

### Tool Approval
Multi-user agents need **per-user tool approval** — unlike single-user agents where the developer always owns the terminal. In Slack, who approves a destructive action?

### Sandbox Isolation
Multi-tenant agents require **per-installation sandbox isolation** — data from one organization's Slack installation must never leak into another's.

### Permissions & Attribution
- Which user triggered which action?
- Can user A see user B's results?
- Role-based access control for agent capabilities

## Related Concepts
- [[entities/mastra]] — Mastra agent framework
- [[concepts/security-and-governance/agent-containment]] — Blast radius reduction through environmental isolation
- [[concepts/security-and-governance/agent-sandboxing-patterns]] — Sandbox isolation patterns for AI agents
- [[entities/hermes-agent]] — Single-user agent architecture (contrast point)
- [[concepts/mcp]] — Model Context Protocol for tool integration
- [[concepts/harness-engineering/agentic-loop]] — The canonical agent execution cycle
