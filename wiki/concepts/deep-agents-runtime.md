---
title: "Deep Agents Runtime"
type: concept
aliases:
  - deep-agents
  - agent-runtime
  - durable-execution
tags:
  - concept
  - agent-runtime
  - durable-execution
  - langchain
  - orchestration
status: complete
description: "Production runtime primitives for deep AI agents — durable execution, memory, multi-tenancy, HITL, guardrails, observability, sandbox, and cron."
created: 2026-04-27
updated: 2026-05-26
sources:
  - "https://x.com/i/article/2046277232537256002"
related:
  - "[[concepts/harness-engineering]]"
  - "[[concepts/agent-loop-orchestration]]"
  - "[[concepts/durable-execution]]"
  - "[[concepts/human-in-the-loop]]"
---

# Deep Agents Runtime

> **Definition:** Deep Agents is a production-grade agent runtime built by LangChain/Anthropic. It packages durable execution, memory, multi-tenancy, guardrails, HITL, observability, sandboxed code execution, and scheduled cron.

## Production Runtime Requirements

### 1. Durable Execution
Agent loops (prompt → reasoning → tool call → observe → repeat) can span minutes to hours. A single execution may involve dozens of model calls or sub-agent spawns.

**Two core requirements:**
- **Long runs survive infrastructure failures** — If a worker process dies, don't waste token costs and tool calls. Resume from the last completed step.
- **Agents can stop and wait** — When waiting for human approval, don't hold a worker process/client connection open. Free resources and resume later.

**Implementation:**
- Managed task queue + automatic checkpointing
- Each super-step writes a checkpoint to PostgreSQL (default), keyed by thread_id
- On worker failure, the lease is released and another worker resumes from the latest checkpoint
- Configurable retry policies (backoff, max attempts, per-node exception)

### 2. Memory — Two-Layer Memory Structure
- **Short-term memory** — Accumulated within a single conversation. Saved to checkpoints, scoped by thread_id. Disappears after conversation ends.
- **Long-term memory** — Crosses conversations. User settings, project conventions, knowledge bases. Organized by namespace tuples (e.g., `(user_id, "memories")`)

**Long-term Memory Storage:**
- Agent Server's built-in store (key-value interface)
- PostgreSQL backed, semantic search via embeddings
- Scopable per user/assistant/org via namespaces
- Directly queryable via API

### 3. Multi-tenancy — Three-Layer Isolation
1. **Data isolation** — Custom auth middleware (`@auth.authenticate`). Tags resources with ownership metadata.
2. **Agent acting on behalf of user** — Agent Auth handles OAuth dance and token storage. User authenticates once, agent acts on their behalf afterward.
3. **Operator-level access control** — RBAC manages team member permissions for deployment, configuration, and tracing.

### 4. Human-in-the-Loop (HITL)
Two scenarios:
- **Tool call review** — Human approval before critical actions (email sending, financial transactions, file deletion)
- **Clarifying question** — Decision points that depend on human judgment/preferences

**Implementation:**
- `interrupt()` — Pauses execution and surfaces payload to the caller
- `Command(resume=...)` — Resumes with the human's response
- Checkpoint saved to durable storage. Resume can be any JSON-serializable value (not just approve/reject — edited drafts, missing context, computed results)

### 5. Real-time Interaction
- **Streaming** — Flows partial output to the client in real-time. 4 modes: full state snapshots, state updates only, token-by-token LLM output, custom events.
- **Thread streaming** — Long-lived connection, delivering follow-ups/background/HITL-resumption all on the same thread. Resume with `Last-Event-ID`.
- **Double-texting** — When a new message arrives while an old run is in progress:
  - `enqueue` (default): Queue and process sequentially
  - `reject`: Reject the new input
  - `interrupt`: Halt the current run, process new input from that state
  - `rollback`: Halt the current run, revert all progress, process as a fresh run

### 6. Guardrails (Middleware)
Two main cases:
- **PII Redaction** — Redacts sensitive data before the model sees it. Runs deterministically on every model call.
- **Cap expensive operations** — Caps the number of paid external API calls per run.

**LangChain built-in middleware:**
PIIRedactionMiddleware, ModelRetryMiddleware, ModelFallbackMiddleware, ToolCallLimitMiddleware, SummarizationMiddleware, HumanInTheLoopMiddleware, OpenAIModerationMiddleware

**Hooks:** `before_model`, `wrap_model_call`, `wrap_tool_call`, `after_model`

### 7. Observability & Time Travel
- Execution tree available out of the box (model calls, tool calls, subagent runs, middleware hooks)
- Filter by cost/errors/users/custom tags
- **Polly** — LangSmith AI assistant analyzes traces and surfaces common failure modes, slow tool calls, repeated patterns
- **Online Evals** — LLM-as-judge or custom scorers for production traces
- **Time Travel** — Rewind from a checkpoint, modify state, and branch. The original fork thread is preserved. All LLM/tool call/interrupts are re-triggered

### 8. Sandboxed Code Execution
- **Sandbox backends:** Daytona, Modal, Runloop, LangSmith Sandboxes (private preview)
- LangSmith Sandboxes: templates for container images/resource limits/volumes, warm pools for cold start elimination, auth proxy sidecar ensures credentials never enter the sandbox

### 9. Integrations
- **MCP** — Model Context Protocol (standardized agent-tool/data connection)
- **A2A** — Agent-to-Agent standard (multi-agent architectures across deployments)
- **Webhooks** — Kick off downstream processes on run completion
- **Cron** — Scheduled runs (stateful: tied to threads; stateless: fresh thread per execution)

### 10. Open Harness (Lock-in Avoidance)
- MIT licensed harness + fully open source
- AGENTS.md (open standard) for agent instructions
- Open protocols: MCP, A2A, Agent Protocol
- Every layer can be inspected/customized/extended (rate limits, retry logic, model fallback, PII detection, file permissions)

## Related Resources
- [Going to Production Guide](https://docs.deepagents.ai) — credential management, async patterns, frontend integration
- [LangSmith Deployment & Agent Server docs](https://docs.langchain.com)
- [Deep Agents deploy docs](https://docs.deepagents.ai/deploy)

## Sources
- [The runtime behind production deep agents](https://x.com/i/article/2046277232537256002) (2026-04-26, X article) — durable execution, HITL, double-texting, guardrails, observability, time travel, sandbox, cron
