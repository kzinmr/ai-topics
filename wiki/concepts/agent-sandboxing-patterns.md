---
title: "Agent Sandbox Architecture Patterns"
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

## Related Concepts
- [[concepts/agent-sandboxing]] — General sandboxing technologies (gVisor, Firecracker, WASM)
- [[concepts/agentic-security]] — Broader agent security patterns
- [[entities/larsen-cundric]] — Browser Use engineer, author
