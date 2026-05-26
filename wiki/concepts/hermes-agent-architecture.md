---
title: "Hermes Agent Architecture"
created: 2026-05-07
updated: 2026-05-07
type: concept
tags:
  - agentic-engineering
  - architecture
  - harness-engineering
  - ai-agents
  - multi-agent
  - orchestration
  - context-engineering
  - memory-systems
  - coding-agents
sources:
  - raw/articles/2026-05-07_chatgpt-hermes-agent-architecture-deep-dive.md
---

# Hermes Agent Architecture

> **Core Definition:** Hermes Agent (v0.9.0) adopts an **agent-core-first** architecture centered on `AIAgent`, bundling memory, session search, compression, and skill management. It treats CLI as merely one interface, with the agent runtime itself at the design center. In contrast, [[concepts/openclaw-architecture]] takes a gateway-first design with a long-lived Gateway as the control plane.

## 1. Overview — Architectural Positioning

Hermes Agent is an open-source, self-hosted AI agent developed by Nous Research. Its greatest architectural feature is that the **AIAgent class serves as a single central core** integrating all subsystems. This means it's designed as a "persistently running, self-improving agent runtime" rather than a "CLI that can call tools."

The architectural philosophy in one phrase: **capability accumulation system**. The more the agent is used, the more procedural knowledge (skills) and environmental memory it accumulates, becoming stronger over time. This is a fundamentally different design philosophy from OpenClaw, which aims for a scope-controlled assistant control plane. For detailed comparison, see [[comparisons/hermes-vs-openclaw-architecture]].

From public documentation and source code analysis (elvis's 9-hour parallel study, April 2026), Hermes has been confirmed to feature a built-in learning loop with a three-layer structure of agent-managed skills, pre-compression memory flush, and bounded curated memory.

## 2. Core Architecture — AIAgent-Centric Design

Hermes's architecture integrates the following subsystems radially around the `AIAgent` class as the central core:

```
                    ┌──────────────────┐
                    │   Gateway Layer   │
                    │  (14+ platforms)  │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
     ┌────────▼────────┐ ┌──▼───┐ ┌───────▼──────┐
     │  Prompt Assembly │ │AIAgent│ │ Provider     │
     │  (cached+ephem.) │ │ CORE │ │ Runtime      │
     └────────┬────────┘ │      │ └──────┬───────┘
              │          └──┬───┘        │
     ┌────────▼────────┐    │    ┌───────▼──────┐
     │  Persistent      │    │    │  Tool         │
     │  State (SQLite)  │    │    │  Runtime      │
     └─────────────────┘    │    └──────────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
     ┌────────▼────────┐ ┌──▼──────┐ ┌─────▼───────┐
     │  Subagent        │ │Skills   │ │ Extension   │
     │  Delegation      │ │Registry │ │ Model       │
     └─────────────────┘ └────────┘ └─────────────┘
```

**3 API Execution Modes:**
- **Interactive Mode:** Real-time dialogue with users. Receives messages via Gateway, AIAgent generates responses.
- **Cron Mode (Scheduled):** Periodic execution via natural-language cron. Unsupervised autonomous execution like morning GitHub scan summaries.
- **Watchdog Mode (Reactive):** Detects external events or other agent failures for automatic intervention. Example: deploying Hermes to monitor OpenClaw, auto-recovery within 15 seconds of failure detection.

**Callback Surface** consists of mechanisms for each subsystem to notify the AIAgent core of events, handling lifecycle events such as tool execution completion, skill creation triggers, memory flush signals, and gateway message arrivals.

## 3. Agent Loop — Turn Lifecycle

Hermes's agent loop extends the [[concepts/agent-loop-orchestration|standard ReAct pattern]] with these features:

**Turn Lifecycle:**
1. **Context Collection:** Assemble cached system prompt + ephemeral layer (latest messages, tool results)
2. **Reasoning:** LLM decides next action (text response or tool_call)
3. **Tool Execution:** Multiple tools can execute simultaneously at maximum parallelism
4. **Result Evaluation:** Add tool output to context, determine continuation or termination
5. **Iteration:** Loop within iteration budget (default limit)

**Interruptible Calls:** Long-running tools can be interrupted via Gateway-mediated user intervention (approve/reject/abort). Cron mode follows pre-approved policies.

**Tool Execution Parallelism:** Independent tool calls (e.g., simultaneous multi-file reads, parallel web searches) execute in parallel within a single turn, minimizing latency.

**Iteration Budget:** Maximum tool call count per task is capped to prevent infinite loops. Auto skill generation triggers fire upon completion of complex tasks (5+ tool calls).

## 4. Prompt Assembly — Cache and Ephemeral Layers

Prompt assembly adopts **cache-aware design** to minimize token costs:

**Assembly Order (top to bottom):**
1. **Cache Layer (Cached / Deterministic):**
   - `SOUL.md` — Agent persona and behavioral guidelines (nearly immutable)
   - System prompt core — Tool definitions, basic instructions (stable across versions)
2. **Session-Stable Layer:**
   - `MEMORY.md` — Environmental facts, conventions, accumulated experience
   - `USER.md` — User settings, communication style, expectations
   - Project context files — Project-specific context
3. **Ephemeral Layer (Turn-variable):**
   - Recent conversation history (bounded window)
   - Latest tool execution results
   - Active skill bodies (progressive disclosure: full body loaded only when needed)

**Cache Design Key Points:** Cache and session-stable layers leverage provider API prompt caching to reduce retransmission costs between turns. Only the ephemeral layer changes each turn. Skill bodies primarily have only name/description in the prompt; full text is fetched via `read` tool when needed (progressive disclosure).

## 5. Persistent State — Session DB and JSONL Transcripts

Hermes's persistent state management is based on the **bounded memory** philosophy:

**Session Database (SQLite + FTS5):**
- All conversation history stored in local SQLite
- Full-text search enabled via FTS5 (Full-Text Search 5)
- Past conversations can be searched, summarized, retrieved, and injected into current context

**JSONL Transcripts:**
- Human-readable and machine-readable transcripts in JSONL format alongside
- Used for debugging, auditing, and external tool integration

**Bounded Memory Design:**
- Two core memory files (`MEMORY.md` and `USER.md`) loaded as frozen snapshots across all sessions
- Memory doesn't grow unboundedly; only important information is retained via pre-compression flush
- Memory is flushed during context compression, triggering new skill generation and memory updates

**External Memory Providers:**
- Honcho integration (optional) for extended memory backend
- Plugin mechanism enables connecting additional memory/context providers

Also see [[concepts/ai-memory-systems|AI memory system design philosophy comparison]].

## 6. Tool Runtime — Self-Registering Registry

**Tool Registry:**
- Self-registering: Tool definitions auto-register upon declaration
- MCP (Model Context Protocol) support for external tool server integration
- Toolset management: Active toolsets switchable per session/profile

**Approval Flow:**
- Destructive operations (file deletion, external API calls, code execution) require user approval
- Gateway presents 3 choices: approve/reject/always-approve
- Cron mode follows predefined approval policies

**Terminal Backend:**
- Persistent machine access
- Multiple terminal sessions managed concurrently
- Independent terminal environments per sub-agent

## 7. Subagent Delegation vs execute_code

Hermes provides two distinct execution primitives:

**Subagent Delegation:**
- Main agent launches independent child agents
- Each sub-agent has isolated context and terminal session
- Multiple sub-agents can execute in parallel
- Parent agent aggregates and integrates results
- Use cases: Large task decomposition, independent investigation, parallel code generation

**execute_code:**
- Single code block executed directly in current session context
- No sub-agent launch overhead
- Use cases: Small calculations, data transformations, quick scripts

**Selection Criteria:**
| Characteristic | Subagent | execute_code |
|------|----------|-------------|
| Context | Isolated (blank-slate) | Shared with parent session |
| Parallelism | Multi-agent parallel | Single execution |
| Overhead | High | Low |
| Suitable tasks | Complex, independent, large-scale | Simple, dependent, small-scale |

## 8. Gateway Layer — Long-Running Process

**Gateway Role:**
Hermes communicates externally through a single long-lived Gateway process. This process runs 24/7, uniformly processing messages from multiple platforms.

**14+ Platform Integrations:**
- Telegram, Discord, Slack, WhatsApp, Signal, Email
- Web UI, CLI, HTTP API
- 5+ other platforms

**Message Flow:**
```
[User on Telegram] → Gateway → AIAgent Loop → Tool Execution → Gateway → [Response to Telegram]
                                   ↓
                            [Cron Trigger] → Gateway → AIAgent Loop → ...
```

**Two-Level Guard:**
1. **Gateway Level:** Message authentication, rate limiting, platform-specific validation
2. **AIAgent Level:** Pre-tool-execution approval checks, destructive operation guards

This two-layer structure separates platform-level security from agent-level action control.

## 9. Provider Runtime — Shared Resolver and Fallback

**Shared Resolver:**
- Abstraction layer uniformly handling multiple LLM providers (OpenAI, Anthropic, Google, local models, etc.)
- Absorbs provider-specific API differences

**Auxiliary Task Model Routing:**
- Main tasks (complex reasoning, code generation) use high-capability models
- Auxiliary tasks (summarization, classification, lightweight judgments) routed to lightweight models
- Purpose: Cost optimization and latency reduction

**Fallback Mechanism:**
- Automatic fallback on primary provider failure
- Per-provider rate limiting and quota management
- Also supports fallback to local models (via Ollama)

## 10. Extension Model — Plugins, Hooks, Providers

**Plugin Mechanism:**
- Extension management via configuration under `~/.hermes/` directory
- Third-party plugin installation supported

**Hooks:**
- Hooks attachable at each agent lifecycle stage
- Main hook points: pre-prompt assembly, post-tool execution, pre-memory flush, post-skill creation

**Memory/Context Providers:**
- Provider interface connecting external memory backends (Honcho, etc.)
- Additional context injection via custom context providers
- Extension point for [[concepts/context-engineering|context engineering]]

## 11. Key Architectural Characteristics — 4 Defining Properties

**1. Agent-Core-First:**
AIAgent is the design center. CLI is merely one interface. Contrasts with OpenClaw's gateway-first design.

**2. Capability Accumulation:**
System that grows stronger with use. Auto skill generation after task success, procedural knowledge patched in-place after error recovery, learning from user corrections. Growing procedural memory, not a static toolset.

**3. Bundled-by-Default:**
123+ bundled/optional skills catalog. A fairly complete agent from the start, not a blank framework. Rails-style "opinionated defaults."

**4. Self-Improving Loop:**
4-stage process: Prompt nudges (encourage skill saving every N tool calls) → Background review (scan after task completion) → Pre-compression flush (save before context compression) → Blunt rule (modify existing skill if present, create new if not).

## 12. Trade-offs — Architectural Trade-offs

**Core Complexity:**
Agent-core-first design creates tight coupling where all subsystems depend on the core. Compared to OpenClaw's gateway-centered loose coupling, internal dependencies tend to become more complex.

**Memory Immediacy vs Consistency:**
Bounded memory (`MEMORY.md` + `USER.md`) is immediately available but requires waiting for pre-compression flush to update. A trade-off exists between real-time memory updates and consistency.

**Sub-agent Blank-Slate Problem:**
Sub-agents launch in isolated contexts, so they don't inherit parent memory or learned skills. This is intentional design (guaranteeing independence) but creates additional overhead for knowledge transfer.

**Skill Explosion Problem:**
Unlike [[concepts/openclaw-architecture]], Hermes's self-generated skills continuously accumulate in `~/.hermes/skills/`. Long-term operation faces structural challenges requiring taxonomy, deduplication, and metrics. However, progressive disclosure means full skill bodies are only loaded when needed, so prompt tokens don't immediately break down. This is a **discoverability and corpus governance problem**.

## 13. Code Reading Order — Recommended Exploration Path

Recommended exploration order for understanding the Hermes Agent codebase (as of v0.9.0):

1. **`AIAgent` Class (entry point):** Grasp core initialization and wiring of all subsystems
2. **Agent Loop (`loop/` or `agent/loop`):** Turn lifecycle, tool execution, iteration control
3. **Prompt Assembly (`prompt/` or `context/`):** Cache strategy, layer structure, progressive disclosure
4. **Persistent State (`memory/` or `session/`):** SQLite+FTS5 schema, JSONL transcripts, memory flush
5. **Tool Runtime (`tools/`):** Self-registering registry, MCP integration, approval flow
6. **Skills System (`skills/`):** Skill generation, update, deletion lifecycle; fallback/request mechanism
7. **Gateway Layer (`gateway/`):** Multi-platform message routing, two-level guard
8. **Provider Runtime (`providers/`):** Shared resolver, model routing, fallback
9. **Subagent / Sandbox (`subagents/` or `exec/`):** Sub-agent delegation and code execution separation
10. **Extensions (`plugins/` or `hooks/`):** Extension points and external provider integration

## 14. References

- [Hermes Agent — Agent Loop Internals (official docs)](https://hermes-agent.nousresearch.com/docs/developer-guide/agent-loop)
- [Hermes Agent — Skills System (official docs)](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
- [GitHub — NousResearch/hermes-agent](https://github.com/nousresearch/hermes-agent)
- [[entities/hermes-agent]] — Hermes Agent entity page (features, use cases, 3-layer model)
- [[comparisons/hermes-vs-openclaw-architecture]] — Hermes vs OpenClaw architecture comparison
- [[concepts/openclaw-architecture]] — OpenClaw architecture details (contrasted with Hermes's agent-core-first)
- [[concepts/openclaw/_index]] — OpenClaw concept cluster index
- [[concepts/self-evolving-agents]] — 5-level classification of self-evolving agents (Hermes is Level 3–4: Capability Expansion, Pi is Level 5: Self-Modification)
- [[concepts/agents-that-build-themselves]] — Hugo+Ivan workshop: Pure Python reconstruction of self-extending agents
- [[concepts/agent-loop-orchestration]] — General patterns of agent loop orchestration
- [[concepts/agent-harness-primitives]] — 6 fundamental primitives of agent harnesses
- [[concepts/ai-memory-systems]] — AI memory system design philosophy comparison (OpenAI/Anthropic/Cognition)
- [[concepts/context-engineering]] — Systematic approach to context engineering
