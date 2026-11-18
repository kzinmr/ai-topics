---
title: "Agent Sandbox Architecture Patterns"
type: concept
created: 2026-04-30
updated: 2026-11-18
tags:
  - concept
  - ai-agents
  - sandbox
  - infrastructure
  - security
status: active
sources:
  - url: "https://browser-use.com/posts/two-ways-to-sandbox-agents"
    title: "How We Built Secure, Scalable Agent Sandbox Infrastructure"
  - raw/articles/simonwillison.net--2026-nov-17-external-sandboxes-for-coding-agents--1f643769.md
---

# Agent Sandbox Architecture Patterns

**Source:** [How We Built Secure, Scalable Agent Sandbox Infrastructure](https://browser-use.com/posts/two-ways-to-sandbox-agents) by Larsen Cundric (Browser Use, 2026-02-25)

---

## Summary

Production-grade agent sandboxing from Browser Use (millions of concurrent web agents). Core pattern: **isolate the agent** rather than just the tool, using a control plane architecture with zero-secret sandboxes.

## Two Patterns

| Pattern | Description | Pros | Cons |
|---------|-------------|------|------|
| **1. Isolate the Tool** | Agent on backend, code exec in separate sandbox via HTTP | Simple setup | Agent shares backend resources & secrets |
| **2. Isolate the Agent** ⭐ | Entire agent in sandbox, zero secrets. Talks to world via control plane. | Disposable, independent scaling, zero secrets | Extra network hop; 3 services instead of 1 |

> *"Your agent should have nothing worth stealing and nothing worth preserving."*

Browser Use migrated from Pattern 1 → Pattern 2 for production.

## Control Plane Architecture

### Minimal Sandbox Environment
Only 3 env vars in sandbox: `SESSION_TOKEN`, `CONTROL_PLANE_URL`, `SESSION_ID`. No AWS keys, DB creds, or API tokens.

### Architecture
- **Stateless FastAPI proxy** behind ALB on ECS Fargate
- **LLM Proxying:** Sandbox sends only new messages; control plane stores history in DB, reconstructs context, forwards to providers. Handles cost caps & billing.
- **Auth:** `Bearer: {session_token}` header
- **File Sync:** Presigned URLs — sandbox uploads directly to S3, no AWS creds in sandbox
- **Gateway Protocol:** `ControlPlaneGateway` (prod) vs `DirectGateway` (dev/evals). Agent code remains agnostic.

### Security Hardening
1. **Bytecode-only:** `.py` → `.pyc` during build, source deleted
2. **Privilege drop:** Starts as `root`, drops to `sandbox` via `setuid`/`setgid`
3. **Env stripping:** Reads 3 env vars, deletes from `os.environ`

## Scaling

| Layer | Runtime | Scaling |
|-------|---------|---------|
| Control Plane | Stateless FastAPI | ECS Fargate, auto-scale by CPU |
| Sandboxes | Unikraft micro-VMs (prod) / Docker (dev) | Unikraft schedules across AWS metros, scale-to-zero, <1s boot |

Config switch: `sandbox_mode: 'docker' | 'ukc'` — same image everywhere.

## Tradeoffs

| Dimension | Cost | Impact |
|-----------|------|--------|
| Operational complexity | +3 services | Standard for modern infra teams |
| Latency | +1 network hop per op | Negligible vs LLM response times |
| Security | Zero secrets in sandbox | Fully disposable, stateless agents |

## Pattern 3: The External Sandbox (Simon Willison × Prime Radiant, Nov 2026)

A third, distinct placement of the sandbox boundary, published November 17, 2026 by [[entities/simon-willison|Simon Willison]] together with **Prime Radiant** (the AI research lab behind Superpowers, also behind the [[#related|smevals]] eval framework). Where Browser Use's two patterns move the *agent* or the *tool* into a sandbox, the **external sandbox** pattern keeps **the agent itself on the host** and puts **only the code the agent executes** inside a dedicated sandbox:

| Aspect | Design |
|--------|--------|
| Agent location | **Outside** the sandbox (on the developer's machine / host) |
| Executed code location | **Inside** a dedicated sandbox server |
| Interface | Three released sandbox-server implementations all expose the **same localhost API**; configure Pi / Claude Code / Codex to route code-execution calls to it |
| Egress control | Optional **HTTP/HTTPS allow-list proxy** — restrict exactly which hosts the agent's code may reach |
| Secrets | **Credential replacement mechanism** — make authenticated API calls *without* handing a secret to the agent |
| Operability | A UI lets you **reconfigure the running proxy** without restarting the sandbox |

**Motivation**: making it safe to run *local models* — where a mistake or a [[concepts/prompt-injection|prompt-injection]] attack could otherwise make the model take damaging actions directly on the machine. This is the local-model analogue of Browser Use's "agent should have nothing worth stealing": here the sandbox isolates the *consequences* of untrusted generated code while leaving the (trusted, host-resident) agent in control.

**How it relates to the two Browser Use patterns**:
- Like **Isolate the Tool** (Pattern 1), the agent stays on the backend and only code execution is sandboxed — but unlike Pattern 1, this design adds explicit *egress* (allow-list proxy) and *credential* controls so the agent still shares no secrets with the executed code.
- It is **not** Isolate the Agent (Pattern 2): the agent is *not* disposable or zero-secret; it lives on the host. The trade-off is reversed — simplicity of keeping the agent native (so it can use the host's normal coding-agent tooling) versus a hardened, disposable agent.

This makes three points on a spectrum from "sandbox everything but the host" to "sandbox only execution," useful when choosing a harness for local or untrusted models.

Source: [[raw/articles/simonwillison.net--2026-nov-17-external-sandboxes-for-coding-agents--1f643769.md]] (Simon Willison, 17 Nov 2026).

## Related Concepts
- [[concepts/security-and-governance/agent-sandboxing]] — General sandboxing technologies (gVisor, Firecracker, WASM)
- [[concepts/security-and-governance/agentic-security]] — Broader agent security patterns
- [[entities/larsen-cundric]] — Browser Use engineer, author
