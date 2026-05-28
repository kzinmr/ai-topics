---
title: Mastra
created: 2026-05-19
updated: 2026-05-28
type: entity
tags: [product, framework, ai-agents, agent-framework, typescript, open-source, developer-tooling, workflow, voice-ai, enterprise-ai, multi-agent, harness-engineering, slack, discord]
sources: [raw/articles/2026-05-14_mastra-acp-agents.md, https://github.com/mastra-ai/mastra/releases/tag/%40mastra/core%401.34.0, raw/articles/2026-05-28_mastra-multi-user-multi-channel-agents.md, https://x.com/i/article/2059808126468243457]
---

# Mastra

**Mastra** is an open-source TypeScript framework for building AI-powered applications and agents, created by the team behind Gatsby. 24K+ GitHub stars. Provides a modern stack for agent orchestration, workflows, and real-time voice AI.

## Key Capabilities

- **Agent Framework**: Code-first agent definition with supervisor delegation, multi-agent workflows
- **Workflows**: Durable, stateful workflows with Inngest adapter for production deployment
- **ACP Integration** (v1.34.0, May 2026): [[concepts/mastra-acp-agents]] — ACP-compatible coding agents as tools or subagents
- **Voice AI**: Providers for xAI Grok Voice Agent API (`@mastra/voice-xai-realtime`)
- **Observability**: Trace listing API, retry step tracking
- **Enterprise**: RBAC provider extensions, model allowlist/admin policies (EE)

## Channels: Multi-User, Multi-Platform Agents (May 2026)

Mastra's Channels feature connects agents directly to messaging platforms like Slack, Discord, and Telegram — transforming agents from single-user assistants into **multi-user, multi-channel AI coworkers**.

### Platform Adapters

Built on Vercel's chat SDK adapters for normalized data shapes, with platform-agnostic handlers: `onDirectMessage`, `onNewMention`, `onSubscribedMessage`, `onAction` (buttons), `onReaction` (emoji). Mastra owns the full lifecycle: OAuth + programmatic app creation, HMAC-SHA256 request verification, webhook routing, AES+HKDF credential encryption, token rotation, and multi-tenant adapter lifecycle management.

### Multi-User Architecture

| Layer | Mechanism | Description |
|-------|-----------|-------------|
| **Thread Isolation** | 1:1 platform-thread → Mastra-thread mapping | Each DM/channel thread gets its own memory scope and message history |
| **Resource Scoping** | `${platform}:${userId}` | Working memory keyed by user; user X's context follows X across threads, invisible to user Y |
| **Message Attribution** | Signal attributes + system message | Model sees who sent what, plus whether it's in a DM or public channel |
| **Workspace Isolation** | `requestContext`-driven per-thread sandboxes | Each thread gets its own sandbox (E2B, Daytona, Modal, Docker) for Devin-style fanout |

### Context Engineering vs. Harness Engineering

The article explicitly contrasts two philosophies:

- **Context Engineering**: "Give the agent all the context up front" (pre-fetch everything)
- **Harness Engineering**: "Give it the tools to go get the context it needs" (on-demand)

Mastra's approach: by default, only fetches the current thread context (last 10 messages, prepended as a single text block with author attribution). Cross-thread and cross-channel context is available on-demand via `fetchMessages` / `sendDM` / `postToChannel` tools. The channel ID is always passed in `requestContext` so the agent can decide when to pull additional context.

### Concurrent Message Handling (Signal API)

Multiple users posting simultaneously to the same thread is handled via the **Signal API**: every inbound message calls `agent.sendSignal` with potential to interrupt. Four concurrency modes: queue, debounce, batch, skip. Default: queue (one signal at a time per thread, in order).

### Human-in-the-Loop Tool Approval

Tools can declare `requireApproval: true`. The run suspends and waits:
- **Platforms with buttons (Slack, Discord, Telegram)**: Rendered as Block Kit cards with Approve/Deny, action IDs encode the tool call ID
- **Platforms without buttons (WhatsApp, iMessage)**: Falls back to `autoResumeSuspendedTools: true` — user replies "yes"/"no" in natural language, Mastra runs LLM-as-judge classification

### File Attachments & Inline Media

Platform-adaptive attachment handling (Slack: authenticated fetch; Discord: public CDN URLs). Configurable `inlineMedia` filter (default: image/png, image/jpeg, image/webp, application/pdf). `inlineLinks` converts message URLs into model-readable content (e.g., YouTube links become video file parts).

## Architecture

Agents support tools, subagents (including ACP), metadata (static/dynamic), and can be composed into supervisors and workflows. Workspace abstraction handles filesystem, sandbox, and media operations. Channels add a multi-tenant adapter layer on top of the core agent runtime.

## Related

- [[concepts/mastra-acp-agents]] — ACP-compatible agents in Mastra
- [[entities/langchain]] — Alternative agent framework
- [[concepts/agent-development-kit]] — Google's ADK
- [[concepts/acp-agent-communication-protocol]] — ACP protocol
