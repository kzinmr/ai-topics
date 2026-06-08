---
title: "OpenClaw, Pi, and Hermes Agent State Management"
created: 2026-05-27
updated: 2026-05-27
type: comparison
tags:
  - comparison
  - ai-agents
  - architecture
  - state-management
  - data-flow
  - agent-runtime
  - harness-engineering
  - openclaw
  - context-engineering
  - memory-systems
  - orchestration
  - durable-execution
  - control-plane
  - sqlite
  - streaming
sources:
  - concepts/ai-native-state-management.md
  - concepts/openclaw-architecture.md
  - concepts/hermes-agent-architecture.md
  - comparisons/hermes-vs-openclaw-architecture.md
  - openclaw/docs/concepts/agent-loop.md
  - openclaw/docs/concepts/agent-runtimes.md
  - openclaw/docs/concepts/session.md
  - openclaw/docs/concepts/agent-workspace.md
  - openclaw/docs/plugins/sdk-agent-harness.md
  - openclaw/src/agents/pi-embedded-runner/run.ts
  - openclaw/src/config/sessions/types.ts
  - pi/packages/agent/README.md
  - pi/packages/agent/src/agent-loop.ts
  - pi/packages/agent/src/agent.ts
  - pi/packages/agent/src/harness/session/session.ts
  - pi/packages/agent/src/harness/agent-harness.ts
  - hermes-agent/AGENTS.md
  - hermes-agent/hermes_state.py
  - hermes-agent/run_agent.py
  - hermes-agent/agent/conversation_loop.py
  - hermes-agent/agent/conversation_compression.py
  - hermes-agent/agent/memory_provider.py
  - hermes-agent/gateway/session.py
---

# OpenClaw, Pi, and Hermes Agent State Management

This report compares `openclaw/`, `pi/`, and `hermes-agent/` through the "Data Flow and State Management in AI-Native Applications" lens in [[concepts/ai-native-state-management]]. It builds on [[concepts/openclaw-architecture]], [[concepts/hermes-agent-architecture]], [[comparisons/hermes-vs-openclaw-architecture]], and [[comparisons/agent-memory-systems-comparison]]. The focus is not just where state is stored, but who owns the authoritative state transition.

## Core Thesis

All three systems implement agentic loops, but their state centers are different.

| System | State Management Type | Canonical Owner | Strongest Fit |
|---|---|---|---|
| **OpenClaw** | Control-plane state management | Gateway + per-agent session store | Multi-channel, multi-runtime, long-lived observable orchestration |
| **Pi** | Runtime-substrate state management | In-process `Agent` + harness JSONL session tree | Agent SDKs, turn execution, event streams, fork/compaction primitives |
| **Hermes Agent** | Capability-accumulation state management | `AIAgent` + SQLite/FTS5 + memory/skill files | Personal assistant continuity, long-term conversation search, self-improving skills |

OpenClaw is designed around a Gateway that governs the world while Pi, Codex, and CLI-style harnesses are plugged in as executors. Pi is an SDK for running one turn correctly and reducing events back into message state, not a product control plane. Hermes is oriented toward an agent that becomes more useful by accumulating memory, skills, and conversation history.

## AI-Native State Lens

Mapped onto the 8-State Model from [[concepts/ai-native-state-management]], the systems differ as follows.

| State Layer | OpenClaw | Pi | Hermes Agent |
|---|---|---|---|
| Client/UI State | WebSocket clients, channels, nodes are Gateway projections; events are typed but not replayed | Subscribers consume `AgentEvent` stream | CLI/TUI/Gateway adapters wrap the same `AIAgent` turn |
| Server State | Gateway is source of truth; `sessions.json` tracks metadata, queue mode, runtime, cost, compaction, delivery | SDK has no server plane; `AgentState` is process-local | Gateway `SessionStore` maps platform keys to session IDs; `state.db` stores durable sessions |
| Session State | `~/.openclaw/agents/<agentId>/sessions/sessions.json` + `<sessionId>.jsonl` | harness `Session` has append-only JSONL entries and leaf pointer | SQLite `sessions` table plus gateway `sessions.json` index/fallback |
| Conversation Memory | JSONL transcript, workspace memory files, compaction and memory flush | `AgentMessage[]`, session tree entries, compaction summaries | SQLite `messages` + FTS5/trigram search; optional JSON snapshots |
| Tool/Workflow State | runId, lanes, tool policy, sandbox, approvals, lifecycle/tool/assistant streams | `pendingToolCalls`, sequential/parallel tool execution, event reducer | loop-local `messages`, checkpoint manager, tool callbacks, guardrails |
| Retrieval State | context engines, workspace memory, memory search/dreaming surfaces | `transformContext` is extension point; retrieval policy is external | `session_search` over SQLite FTS5; memory provider prefetch |
| Episodic/Semantic Memory | `MEMORY.md`, daily memory, pre-compaction flush, dreaming | outside core unless built by harness/user | `MEMORY.md`, `USER.md`, providers, post-turn sync, background reviews |
| Agent Identity | workspace bootstrap files: `SOUL.md`, `IDENTITY.md`, `USER.md`, `TOOLS.md`, `AGENTS.md` | `systemPrompt`, tools, resources resolved per turn | `SOUL.md`, system prompt cache, memory/user files, active skills |

## OpenClaw

OpenClaw is Gateway-first. Channels, WebSocket clients, nodes, cron, webhooks, and agent runtimes are coordinated through the Gateway. The Gateway owns session resolution, queueing, runtime selection, tool policy, delivery, and metadata persistence.

The data flow is roughly:

```text
Channel / Client / Node
  -> Gateway RPC / WS
  -> session resolution in sessions.json
  -> session lane + global lane
  -> runEmbeddedPiAgent or other harness backend
  -> Pi/Codex/CLI runtime attempt
  -> subscribeEmbeddedPiSession event bridge
  -> assistant/tool/lifecycle streams + transcript/metadata writes
```

OpenClaw's canonical state is split into two layers. `sessions.json` is the source of truth for session metadata: session ID, status, queue mode, spawn lineage, runtime/model/provider/auth overrides, compaction and memory-flush counters, context budget, delivery origin, and skills snapshot. The actual conversation is an append-only `<sessionId>.jsonl` transcript. A session-store writer queue protects metadata updates, while a separate transcript file lock protects message writes.

Even when Pi is used as the embedded runtime, OpenClaw does not hand over full authority. OpenClaw assembles provider/model/auth, workspace, sandbox, tool policy, session file, context engine, skills snapshot, channel metadata, client tools, and runtime plan. Pi executes the prepared attempt. The `sdk-agent-harness.md` contract makes this boundary explicit: the harness must treat `runtimePlan` as OpenClaw-owned.

Streaming is strong as a projection layer. Pi events such as `message_update`, `tool_execution_start/end`, and `agent_start/end` are mapped to `assistant`, `tool`, and `lifecycle` streams. But Gateway docs state that events are not replayed, so the event stream itself is not the durable source of truth. On gaps, clients refresh from session metadata and transcript state.

From an ai-native state-management view, OpenClaw is strongest at isolation and orchestration. DM, group, room, cron, and webhook sources resolve to different session shapes. Subagents are tracked as background session trees such as `agent:<agentId>:subagent:<uuid>`. Queue lanes, interrupt/followup/steer behavior, subagent registry, and tool policy all live at the Gateway layer, which makes multiple runtimes governable.

The weakness is state-surface breadth. `sessions.json`, transcript JSONL, workspace memory, plugin state, subagent registry, context-engine state, and node presence are distributed. This is a reasonable control-plane split, but debugging requires constant awareness of which layer is canonical for the observed behavior.

## Pi

Pi is used as OpenClaw's agent core SDK, but architecturally it is a runtime substrate rather than a product control plane. Its center is mutable `Agent` state, the low-level `runAgentLoop`, the event stream, and the harness append-only session tree.

The core data flow is:

```text
Agent.prompt()
  -> createContextSnapshot(messages, tools, systemPrompt, model)
  -> runAgentLoop()
  -> transformContext()
  -> convertToLlm()
  -> LLM stream
  -> message/tool/turn events
  -> Agent state reducer
  -> optional harness session append + save_point
```

Pi core `AgentState` contains `systemPrompt`, `model`, `thinkingLevel`, `tools`, `messages`, `isStreaming`, `streamingMessage`, `pendingToolCalls`, and `errorMessage`. `prompt()` rejects or queues while a run is active, and the loop drains steering/follow-up queues at turn boundaries. Pi's state model is focused on keeping the current turn coherent.

Its event model is smaller than OpenClaw's and clear as an SDK contract. `agent_start`, `turn_start`, `message_start/update/end`, `tool_execution_start/update/end`, `turn_end`, and `agent_end` are reduced into state by `Agent.processEvents`. Parallel tool execution performs preflight sequentially, runs allowed tools concurrently, and emits tool-result messages back in assistant source order, preserving LLM protocol ordering.

At the harness layer, Pi provides durable session primitives. The JSONL header stores session version, cwd, and parent session. Entries append messages, thinking/model changes, compaction, custom records, and branch summaries. `buildSessionContext()` reconstructs context from the leaf path; compaction entries insert summaries and kept ranges. Forks are represented as new JSONL sessions with a parent session path.

Pi's `transformContext` and `convertToLlm` are the hooks where [[concepts/context-engineering]] style Select and Compress behavior can be inserted. Pi itself does not decide which memory to search, how to isolate sessions by channel, or which sandbox policy applies. Those decisions belong to OpenClaw or another higher-level harness.

Pi's strength is that it defines the minimal state kernel well: turn lifecycle, tool lifecycle, message history, event stream, session replay, fork, and compaction. Multi-tenant server state, delivery state, agent identity, and long-term memory governance are intentionally out of scope.

## Hermes Agent

Hermes is AIAgent-first. CLI, TUI, Gateway, and cron are entrypoints; the center is `AIAgent.run_conversation()` plus the surrounding memory, skill, and tool system. State management is not only about continuing a conversation correctly, but also about accumulating memory, skills, and a user model from the conversation.

Its data flow is:

```text
CLI / Gateway / Cron
  -> AIAgent.run_conversation()
  -> restore/build cached system prompt
  -> append user message to loop-local messages
  -> inject ephemeral memory/provider/plugin context into API copy
  -> streaming model call
  -> sequential/concurrent tool execution
  -> context compression if needed
  -> persist messages to SQLite + optional JSON snapshot
  -> external memory sync + next-turn prefetch
```

The center of durable state is `~/.hermes/state.db`. `SessionDB` stores `sessions` and `messages`; message rows include tool calls, tool result IDs, reasoning fields, and platform message IDs. FTS5 and trigram FTS5 triggers power `session_search` discovery, scroll, and browse modes. Hermes defaults to WAL but falls back to DELETE journaling on WAL-incompatible filesystems, which reflects its long-running personal-agent operating model.

The Gateway side has a separate `SessionStore` that builds deterministic session keys from platform/chat/user/thread metadata. It tracks token counters, cost, `resume_pending`, `suspended`, and auto-reset flags. If SQLite is unavailable it can fall back to legacy JSONL, so Hermes also separates routing/index state from conversation truth; unlike OpenClaw, conversation truth is primarily SQLite.

Hermes' context strategy is close to Bounded Snapshot plus live retrieval. The system prompt is stored in the session DB to preserve prefix-cache stability, while memory-provider prefetch and plugin context are injected into the user message only in the API-call copy. Durable transcripts stay clean. On compression, Hermes closes the old session with `end_reason='compression'`, creates a child session, and carries title and lineage forward.

The memory-provider lifecycle captures Hermes' distinctive direction. `initialize`, `prefetch`, `sync_turn`, `on_pre_compress`, `on_session_switch`, and `on_delegation` support pre-compression insight extraction, post-turn external memory sync, and next-turn prefetch queues. Background memory/skill review runs after the user-facing turn, so long-term state accumulates not only in the transcript but also in memory files, external providers, and the skill corpus.

The weakness is that canonicality can spread across conversation, memory, skill, and identity state. `AIAgent` bundles many responsibilities while the Gateway supports the edges. This is powerful for a personal agent, but heavier for control-plane debugging or multi-runtime governance than OpenClaw.

## Comparative Axes

- **Source of Truth** - OpenClaw's source of truth is Gateway session/control-plane state. Pi is the runtime substrate beneath it, with OpenClaw owning session files and runtime plans. Hermes is canonical around `AIAgent` plus SQLite session DB, while Gateway owns platform routing and cached-agent lifecycle.
- **Recovery Shape** - OpenClaw refreshes from Gateway store and transcript after client event gaps. Pi rebuilds context from the harness JSONL leaf. Hermes reconstructs resume/search/compression continuation from SQLite messages and parent-session lineage.
- **Event vs Snapshot** - Pi has the smallest clean event stream and state reducer. OpenClaw expands Pi events into platform streams and adds delivery/liveness/replay-invalid projection state, but WS events are not a durable replay log. Hermes is closer to loop-local snapshot plus SQLite append.
- **Context Lifecycle** - OpenClaw folds workspace bootstrap, skills snapshot, context engine, memory flush, and compaction into the prepared Gateway attempt. Pi exposes `transformContext` and `prepareNextTurn` hooks. Hermes stabilizes the cached system prompt, injects ephemeral provider/plugin context into the user message, and splits sessions on compression.
- **Long-Term Memory** - OpenClaw separates governed workspace memory from session transcript and relies on pre-compaction flush. Pi core has no long-term memory, only JSONL and compaction primitives. Hermes treats SQLite/FTS5 conversation memory, `MEMORY.md`/`USER.md`, external providers, and skill self-improvement as one continuity system.
- **Tool and Workflow State** - OpenClaw binds tool execution to security and control-plane state. Pi manages `pendingToolCalls`, parallel/sequential lifecycle, tool updates, and terminate hints. Hermes keeps checkpointing, file-state coordination, tool guardrails, interrupt propagation, and concurrent workers inside AIAgent runtime.
- **Subagents and Isolation** - OpenClaw subagents are background tasks with parent/child session lineage, registry rows, queue lanes, and announce chains. Pi provides fork/session-tree primitives but no product-level subagent semantics. Hermes `delegate_task` runs child agents in isolated context, reports delegation observations to parent memory providers, and uses file-state checks for sibling edits.
- **Durable Execution** - OpenClaw leans on session lanes, global lanes, transcript locks, store writer queues, and metadata/transcript separation. Pi's durable core is append-only JSONL, save points, pending-write flush, and turn-boundary abort/steer/followup handling. Hermes uses SQLite write retry, WAL fallback, checkpoints, compression session splits, and `resume_pending`/`suspended` flags.

## Design Implications

OpenClaw assumes that the hard part of an ai-native application is the control plane, not just the agent runtime. It is the best fit when multi-channel operation, multiple runtimes, governance, and observable orchestration matter. The source of truth stays outside the agent, so runtimes can be swapped.

Pi assumes that the runtime's internal state should stay small and precise. For SDKs and embedded runtimes, the valuable work is to handle message history, tool lifecycle, streaming events, compaction, and fork semantics without absorbing product-specific state.

Hermes assumes that a personal AI gains value by accumulating memory, skills, and identity. It is the best fit for personal assistants, long-term conversation search, self-improvement, and memory-rich UX. Canonical state sits closer to the agent core, and information flows from conversation into memory and skills.

The key comparison is that these systems live at different layers rather than merely competing. Pi is a runtime substrate, OpenClaw is an orchestration/control plane, and Hermes is a capability-accumulating personal agent. Through the [[concepts/ai-native-state-management]] lens, the difference is not primarily where state is stored, but where the authority boundary for state transitions is drawn.
