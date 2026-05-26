---
title: OpenClaw Architecture
created: 2026-05-07
updated: 2026-05-07
type: concept
tags:
  - openclaw
  - agentic-engineering
  - architecture
  - ai-agents
  - orchestration
  - context-engineering
  - security
  - sandbox
  - isolation
  - multi-agent
  - protocol
sources:
  - raw/articles/2026-05-07_chatgpt-openclaw-architecture-deep-dive.md
---

## Overview

The architectural essence of OpenClaw is **gateway-first, not agent-first**. Centered around a single long-lived Gateway, it is designed as an **assistant control plane** that bundles channel connections, session management, WebSocket control surface, agent execution, tool execution, node management, and UI. The README positions the Gateway as the control plane, and the architecture documentation explicitly states that "one Gateway owns the entire messaging surface."

Despite having multiple frontends (WhatsApp, Telegram, Slack, Discord, Signal, iMessage, WebChat), internally it follows a model where **a single control plane governs conversation, delivery, and state**. This is a fundamentally different design philosophy from agent-first designs like [[concepts/hermes-agent-architecture]]; see [[comparisons/hermes-vs-openclaw-architecture]] for details.

---

## Overall Architecture

At a high level, it consists of the following layers:

```
Channel/Client/Node → Gateway → embedded agent runtime → tools / sessions / plugins / sandbox / nodes
```

- **Channel layer**: All messaging surfaces — WhatsApp, Telegram, Slack, Discord, Signal, iMessage, WebChat — connect to a single Gateway
- **Client layer**: CLI, macOS app, Web UI, automations, nodes all connect to the same WebSocket surface
- **HTTP surface**: Canvas/A2UI provided on the Gateway side
- **Control surface**: "Which UI spoke to it" is less important than "which session the Gateway routes to"

Even in remote setup, it sits on the same tunnel/auth model, achieving consistent architecture.

---

## Gateway at the Core

The Gateway is a **long-lived daemon** responsible for:

- Maintaining provider connections
- Exposing a **typed WebSocket API**
- Validating inbound frames with JSON Schema
- Emitting `agent`, `chat`, `presence`, `health`, `heartbeat`, `cron` events
- **Single-host invariant** (one Gateway per host; WhatsApp sessions are only opened by the Gateway on that host)

Per the README, OpenClaw is described as running a resident Gateway on top of which all chat surfaces, CLI, WebChat, macOS app, and iOS/Android nodes connect. Therefore, when understanding OpenClaw, rather than focusing on model providers or prompts, it is correct to view it as a **distributed assistant runtime centered on the Gateway**.

---

## WebSocket Protocol

The communication model is designed as a **WebSocket control surface**:

- Transport: WebSocket text JSON frames
- First frame is always `connect`
- Subsequent flow in the form of `req/res` and `event`
- `hello-ok.features.methods/events` serve as discovery metadata
- JSON Schema is generated from TypeBox schemas, and Swift models are generated from them — protocol typing is taken seriously

### Authentication and Device Identity

- In addition to shared secret token/password, Tailscale Serve or trusted proxy identity headers can also be used
- **Device identity and pairing** exist separately: all WS clients should in principle connect with a `device` identity, requiring a signature against a server-provided challenge
- Some loopback cases are auto-approved, but tailnet or LAN connections are treated as remote even from the same machine, requiring pairing approval

Thus OpenClaw's WS is not merely an RPC pipe. It is a **control-plane protocol encompassing authentication, device identification, pairing, and event delivery**. It is also explicitly stated that "events are not replayed; clients must refresh on gaps" — the protocol itself is designed as a **live control channel**, not a durable event log.

---

## Agent Runtime (Embedded)

Agent execution is not external process launching but **embedding the pi SDK**:

- Rather than launching pi as a subprocess or RPC mode, `createAgentSession()` directly imports/instantiates pi's `AgentSession`
- This approach lets OpenClaw control session lifecycle, event handling, tool injection, system prompt customization, session persistence, auth/profile rotation, and provider-agnostic model switching
- `runEmbeddedPiAgent()` is the main entry: receives workspace, session file, provider/model, timeout, runId, block reply callback, etc., and executes the agent run

The **runtime boundary** is also clear: the agent runtime itself depends on Pi core, but documentation states that **session management, discovery, tool wiring, and channel delivery are OpenClaw-owned**. OpenClaw uses pi but carries a substantial amount of upper-level orchestration on its own.

---

## Agent Loop

The Agent Loop is defined as:

**intake → context assembly → model inference → tool execution → streaming replies → persistence**

- The `agent` RPC resolves the session, saves metadata, and immediately returns `{ runId, acceptedAt }`
- Then `agentCommand` resolves model/thinking/skills snapshots and calls `runEmbeddedPiAgent()`
- `agent.wait` is a separate path that waits for that `runId`'s lifecycle end/error

### Unified Streaming and Persistence

`subscribeEmbeddedPiSession` bridges pi-agent-core events to OpenClaw's `assistant`/`tool`/`lifecycle` streams, live-streaming tool start/update/end, assistant deltas, compaction, and errors. The Gateway not only receives final answers but observes the entire run process as an event stream.

### Hook System

Two systems — Gateway hooks and plugin hooks — allow intervention at the following points in the agent loop:

- `agent:bootstrap`, command hooks
- `before_model_resolve`, `before_prompt_build`, `before_agent_reply`
- `before_tool_call`, `after_tool_call`, `tool_result_persist`
- `session_start/end`

OpenClaw is not a "model caller" but an **extensible execution platform for the agent lifecycle**.

---

## Session Management

"**Source of truth: the Gateway**" — UIs should query the Gateway for session lists and token counts; in remote mode, looking at the local machine won't show the actual state.

### Two-Layer Persistence

1. **`sessions.json`**: A small mutable store `sessionKey -> SessionEntry`. Holds metadata like current session ID, last activity, toggles, token counters
2. **`<sessionId>.jsonl`**: Append-only transcript. Tree structure with `id` and `parentId`, storing message/toolResult/compaction/branch summary, etc.

This separates a **light session registry** from **heavy transcript persistence**. Transcripts use Pi's `SessionManager` while OpenClaw layers on guard/caching/history limiting/compaction. Per-agent transcript paths are also fixed at `~/.openclaw/agents/<agentId>/sessions/...`.

---

## Workspace

Each agent has a workspace serving as `cwd` for tools and context. `agents.defaults.workspace` is required.

### Bootstrap Files

Seeds user-editable files such as `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `BOOTSTRAP.md`, `IDENTITY.md`, `USER.md`.

### Prompt Injection

Workspace files are automatically injected into the prompt. Bootstrap files are trimmed/truncated and injected every turn as Project Context in the system prompt. `MEMORY.md` is also injected, but `memory/*.md` daily files are on-demand via tools.

- Per-file / total character limits exist
- Load can be checked via `/context list` or `/context detail`

In other words, the workspace is a **method of managing persona, working conventions, owner information, and local memory as prompt-resident files**.

---

## System Prompt

OpenClaw **assembles a custom system prompt for every agent run**. It is **OpenClaw-owned** and does not use the pi-coding-agent default prompt.

### Provider Plugin Intervention

Provider plugins do not hijack the entire prompt but replace core sections or add stable prefix/dynamic suffix with awareness of cache boundaries:
- `interaction_style`
- `tool_call_style`
- `execution_bias`

### Platform-Oriented Composition

It has fixed sections like Tooling, Safety, Skills, Self-Update, Workspace, Documentation, Workspace Files, Sandbox, Time, Reply Tags, Heartbeats, Runtime, Reasoning — embedding details like cron usage, background process handling, avoiding subagent wait polls, and approval UI priority. The prompt is less of a persona statement and more of a **runtime operations manual cum policy hint**.

### Minimal Mode for Sub-agents

In `promptMode=minimal`, Skills, Memory Recall, Self-Update, User Identity, Messaging, Heartbeats, etc. are dropped to shrink size. Bootstrap file injection is also limited to `AGENTS.md` and `TOOLS.md`. **Prompt size and cache stability are explicitly optimized**.

---

## Tool Execution (Sandbox / Tool Policy / Elevated Separation)

Execution safety is not determined by a single switch. **Sandbox, Tool Policy, and Elevated are separate concerns**:

| Concept | What It Controls |
|------|----------|
| Sandbox | "Where to execute" |
| Tool Policy | "What to allow use of" |
| Elevated | "Whether to escape from sandbox to host" |

### exec tool

- `host=auto|sandbox|gateway|node`
- `security=deny|allowlist|full`
- `ask=off|on-miss|always`

In sandbox, defaults to sandbox execution; can get out to gateway/node host as needed. When approval is required, immediately returns `approval-pending`, then `Exec finished`/`Exec denied` system events flow to the session.

### Sandboxing

Not a simple Docker jail:
- mode: `off|non-main|all`
- scope: `agent|session|shared`
- backend: `docker|ssh|openshell`
- workspace access: `none|ro|rw`
- Browser can also run on the sandbox side

Elevated is an exec-only escape hatch out of the sandbox, controllable per-session via `/elevated on|ask|full|off`. OpenClaw explicitly states it does not rely solely on prompt-based safety — **hard stops are done via tool policy, exec approvals, sandbox, and channel allowlists**.

---

## Nodes

Nodes connect to the same WS server with `role: node` and advertise capabilities:

- `canvas.*`, `camera.*`, `screen.record`, `location.get`
- Headless node hosts can expose `system.run`/`system.which` on that machine
- Browser proxy also auto-advertised

### Device Identity and Pairing

The Gateway is the source of truth for membership, with a flow of pending request → approval → token issuance. Since 2026.3.31, declared node commands are disabled before node pairing approval, and device pairing alone doesn't expose the command surface.

Nodes are not mere remote shells but **capability surfaces where the Gateway mediates device identity and command trust**. Exec approvals also exist on the node host side, combined with per-agent allowlists.

---

## Queueing

OpenClaw's queue is not an afterthought but **part of the agent architecture**:

- Inbound auto-reply runs enter a tiny in-process queue
- Serialized via **session lane** and **global lane**
- `runEmbeddedPiAgent` is enqueued into `session:<key>` and also passes through the `main` lane
- Prevents races within the same session while also constraining overall parallelism via `agents.defaults.maxConcurrent`

### Queue Mode

`collect`, `followup`, `steer`, `steer-backlog`, `interrupt` switchable per-channel/per-session:

- `collect`: Aggregate via follow-up
- `steer`: Inject into current run at next tool boundary/model boundary

This is not a simple message buffer but an **orchestration policy for reconciling a running agent run with new incoming messages**.

---

## Sub-agents

Background agent runs spawned from an existing run:

- Has its own session `agent:<agentId>:subagent:<uuid>`
- Announces to requester chat on completion
- Each sub-agent run is tracked as a background task with a dedicated queue lane `subagent`

### Spawn Control

- By default, sub-agents cannot spawn further children
- `maxSpawnDepth: 2` enables main → orchestrator sub-agent → worker sub-sub-agents
- Tool policy also varies by depth: regular sub-agents have no session/system tools; only depth-1 orchestrators get additional session tools

Design philosophy is Gateway-first: managed as **background run / session tree / announce chain** rather than parent context inheritance like Claude Code's fork. Announces are best-effort and Gateways may lose pending announce work on restart.

---

## Plugin System

Composed of a 4-layer architecture:

1. **Manifest + discovery**
2. **Enablement + validation**
3. **Runtime loading**
4. **Surface consumption**

Discovery and config validation can be done with manifest/schema alone, with native runtime behavior delegated to `register(api)` — the boundary is clear.

### Execution Model

Native plugins are loaded within the **same process** as the Gateway via `jiti` and are not sandboxed — in trust boundary terms, they are on par with core code.

### Capability Register API

Capability register APIs for text inference, speech, media understanding, image generation, etc. are available, with plugin shapes classified as:
- plain-capability
- hybrid-capability
- hook-only
- non-capability

For provider plugins, the generic agent loop, failover, transcript handling, and tool policy are held by the core, with only provider-specific differences passed through the hook surface. The plugin system is not a "convenient add-on" but closer to a **platform's public extension ABI**.

---

## Skills

AgentSkills-compatible `SKILL.md` folders, loaded from multiple sources including bundled, managed, and workspace.

**Index injection pattern**: Rather than injecting skill instruction bodies into the system prompt, only a **compact list of name / description / location** is injected, with the expectation that the model will `read` the `SKILL.md` as needed.

This is excellent from a token design perspective — skills are not all stuffed into the prompt at all times; **only metadata is resident, body is demand-loaded**. OpenClaw's docs even explain the deterministic overhead of the skill list, showing strong awareness of context pressure.

---

## Security

OpenClaw assumes a **personal assistant trust model**, not a hostile multi-tenant boundary:

- Assumes 1 trusted operator boundary per Gateway
- Configurations with multiple adversarial users on the same gateway/agent are not recommended
- Anyone who can touch the host and `~/.openclaw` is considered a trusted operator

This assumption permeates the entire architecture:
- Native plugins are unsandboxed
- Gateway is source of truth for state
- Exec can get out to host/node
- Channel surface connects to real messaging

OpenClaw is not a "SaaS platform with strong tenant isolation" but closer to a **self-managed assistant OS for personal use**. This is less a flaw than a difference in design goals.

---

## Summary

If the OpenClaw architecture were to be summarized in a single phrase:

> **"An assistant control plane centered on a long-lived Gateway, bundling embedded agent runtime, typed WS protocol, session/transcript persistence, sandbox/approvals, nodes, and plugins"**

Strengths:
- Control plane is clear, protocol and plugin boundaries are typed
- Queue, session, sandbox, and approvals are operationally organized

Tradeoffs:
- Gateway host is a large trust bottleneck
- Native plugins are treated as high-trust code
- Workspace/bootstrap injection increases token pressure

Recommended reading order for architectural understanding: `Gateway protocol` → `Agent loop` → `Pi integration architecture` → `System prompt` → `Command queue` → `Plugin architecture` → `Sandboxing / Security`

### Related Pages

- [[concepts/hermes-agent-architecture]] — Hermes Agent's contrasting architecture (agent-first design)
- [[comparisons/hermes-vs-openclaw-architecture]] — agent-first vs gateway-first design philosophy comparison
- [[concepts/openclaw/_index]] — OpenClaw concept cluster index
- [[concepts/openclaw/philosophy]] — OpenClaw design philosophy
- [[concepts/openclaw/five-tier-precedence]] — OpenClaw 5-tier precedence model
- [[entities/openclaw]] — OpenClaw project overview
- [[entities/peter-steinberger]] — OpenClaw author
- [[entities/nvidia-nemoclaw]] — NVIDIA's secure agent framework bundling OpenClaw
- [[entities/pi-coding-agent]] — pi-agent-core embedded by OpenClaw
