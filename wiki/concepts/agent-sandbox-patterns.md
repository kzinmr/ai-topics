---
title: "Agent Sandboxing Patterns: Architectural Approaches for Isolated Agent Execution"
type: concept
created: 2026-04-30
updated: 2026-05-02
tags:
  - concept
  - ai-agents
  - agent-sandboxing
  - infrastructure
  - security
status: active
sources:
  - url: "https://browser-use.com/posts/two-ways-to-sandbox-agents"
    title: "How We Built Secure, Scalable Agent Sandbox Infrastructure"
---

# Agent Sandboxing Patterns: Architectural Approaches for Isolated Agent Execution

**Source:** [browser-use.com/posts/two-ways-to-sandbox-agents](https://browser-use.com/posts/two-ways-to-sandbox-agents)
**Author:** Larsen Cundric
**Date:** 2026-02-25
**Company:** Browser Use

---

## Summary

When AI agents execute arbitrary code (Python, shell commands, file I/O), sandboxing strategy must balance security, scalability, and operational simplicity. This page catalogs **two primary architectural patterns** for agent sandboxing, with production experience from Browser Use (millions of concurrent web agents).

## Two Patterns

### Pattern 1: Isolate the Tool
- **Description:** Agent runs on main infrastructure. Dangerous operations (code execution, terminal access) run in a separate sandbox via HTTP calls.
- **Pros:** Simpler setup (single backend process).
- **Cons:** Agent still shares backend resources & secrets with code execution.

### Pattern 2: Isolate the Agent
- **Description:** Entire agent runs in a sandbox with **zero secrets**. Communicates externally through a **control plane** that holds all credentials.
- **Pros:** Agent becomes fully disposable. Independent scaling. Zero secret leakage.
- **Cons:** Adds one network hop per operation. More services to deploy.
- **Production Decision:** Browser Use migrated from Pattern 1 → **Pattern 2**.

## Control Plane Architecture (Pattern 2)

Core principle: *"Your agent should have nothing worth stealing and nothing worth preserving."*

### Sandbox Receives Only 3 Environment Variables
1. `SESSION_TOKEN` — authentication token
2. `CONTROL_PLANE_URL` — control plane endpoint
3. `SESSION_ID` — unique session identifier

### Control Plane Responsibilities
- **LLM Proxying:** Sandbox sends only new messages. Control plane stores history in DB, reconstructs context, forwards to providers. Handles cost caps & billing.
- **Auth:** `Bearer: {session_token}` header. Validates session & executes operations with real credentials.
- **File Sync:** Uses **presigned URLs**. Sandbox detects changes in `/workspace`, requests scoped URLs from control plane, uploads directly to S3. No AWS credentials in sandbox.
- **Stateless:** No session state in control plane — keeps it horizontally scalable.

### Gateway Protocol (Agent-agnostic)
```python
class AgentGateway(Protocol):
    async def invoke_llm(self, new_messages, tools, tool_choice) -> LLMResponse: ...
    async def persist_messages(self, messages) -> None: ...
```

`ControlPlaneGateway` (prod, HTTP-based) vs `DirectGateway` (dev/evals, in-memory history). Agent code remains agnostic.

## Sandbox Hardening

1. **Bytecode-Only Execution:** `.py` → `.pyc` during Docker build. Source files deleted. Framework loads as root, then source disappears.
2. **Privilege Drop:** Entrypoint starts as `root` (to read root-owned bytecode), immediately drops to `sandbox` user via `setuid`/`setgid`.
3. **Environment Stripping:** Reads env vars into Python variables, then deletes from `os.environ`. Token useless outside private VPC.

## Scaling Architecture

| Component | Runtime | Scaling Mechanism |
|-----------|---------|-------------------|
| Control Plane | Stateless FastAPI proxy | ECS Fargate (auto-scale by CPU, behind ALB) |
| Sandboxes | Unikraft micro-VM (prod) / Docker (dev) | Unikraft handles scheduling across metros. Scale-to-zero, suspend idle. |
| Result | Each layer scales independently | No resource contention between API, agent loop, code execution |

## Tradeoffs

| Aspect | Cost |
|--------|------|
| Operational complexity | +3 services to deploy (vs 1) |
| Latency | +1 network hop per operation (negligible vs LLM response times) |
| Security | Zero secrets in sandbox, zero state, disposable agents |
| Developer experience | Same image everywhere (prod/dev/evals), same protocol |

## Related Concepts
- [[concepts/agent-sandboxing]] — general sandboxing technology spectrum
- [[concepts/process-supervision]] — managing long-running agent processes
- [[concepts/agentic-security]] — broader security patterns
- [[entities/larsen-cundric]] — author, Browser Use engineer
