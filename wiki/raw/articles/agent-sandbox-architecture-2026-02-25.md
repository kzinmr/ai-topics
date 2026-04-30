# Agent Sandboxing Architecture Patterns

**Source:** [browser-use.com/posts/two-ways-to-sandbox-agents](https://browser-use.com/posts/two-ways-to-sandbox-agents)
**Author:** Larsen Cundric
**Date:** 2026-02-25
**Company:** Browser Use

---

## Summary

Production-grade agent sandboxing architecture from Browser Use, which runs millions of concurrent web agents. Key insight: when agents can execute arbitrary code (Python, shell, file I/O), sandboxing strategy must address both security and scaling independently.

## Two Sandboxing Patterns

| Pattern | Description | Pros | Cons |
|---------|-------------|------|------|
| **1. Isolate the Tool** | Agent runs on backend. Dangerous ops (code/terminal) in separate sandbox via HTTP. | Simpler setup, single backend | Agent still shares backend resources & secrets; redeploy kills agents |
| **2. Isolate the Agent** ⭐ | Entire agent runs in sandbox with zero secrets. Talks to world through control plane. | Agent is disposable; independent scaling; zero secret leakage | Extra network hop; 3 services to deploy instead of 1 |

**Decision:** Browser Use migrated from Pattern 1 → Pattern 2 for production.

> *"Your agent should have nothing worth stealing and nothing worth preserving."*

## Architecture Details (Pattern 2)

### Environment
Only 3 env vars reach the sandbox:
- `SESSION_TOKEN`
- `CONTROL_PLANE_URL`
- `SESSION_ID`

### Control Plane Architecture
- **Stateless FastAPI proxy** behind ALB on ECS Fargate
- **LLM Proxying:** Sandbox sends only new messages; control plane stores history in DB, reconstructs context, forwards to providers. Enforces cost caps & billing.
- **Auth:** `Bearer: {session_token}` header validates session.
- **File Sync:** Presigned URLs — sandbox detects file changes in `/workspace`, requests scoped URLs from control plane, uploads directly to S3 (no AWS creds in sandbox).
- **Gateway Protocol:** Agent-agnostic interface with `ControlPlaneGateway` (prod) and `DirectGateway` (dev/evals).

### Hardening
1. **Bytecode-only:** `.py` → `.pyc` during build, source files deleted
2. **Privilege drop:** Entrypoint starts as root, drops to `sandbox` user via `setuid`/`setgid`
3. **Env stripping:** Reads 3 env vars into Python variables, deletes from `os.environ`

### Scaling
- **Control Plane:** Auto-scales via CPU on ECS Fargate
- **Sandboxes:** Unikraft micro-VMs (prod) — scale-to-zero, boot <1s, suspend when idle, distributed across AWS metros
- **Dev/Evals:** Docker containers (same image, same protocol as prod)
- Each layer scales independently based on its own bottleneck

### Tradeoffs
- **Cost:** +3 services, +1 network hop per operation
- **Impact:** Latency negligible vs LLM response times; operational complexity standard for modern infra teams
- **Benefit:** Zero secrets in sandbox, fully disposable agents, independent scaling

## Related Concepts
- [[concepts/agent-sandboxing]] — General sandboxing technology spectrum
- [[concepts/agentic-security]] — Broader agent security patterns
- [[entities/larsen-cundric]] — Browser Use's founding engineer
