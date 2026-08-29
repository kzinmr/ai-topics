---
title: "Agent Sandbox Patterns (Isolate-the-Tool vs Isolate-the-Agent)"
created: 2026-08-29
updated: 2026-08-29
type: concept
tags: [concept, ai-agents, agent-safety, sandbox, isolation, security, infrastructure]
sources:
  - raw/articles/2026-08-29_browser-use_two-ways-to-sandbox-agents.md
confidence: high
---

# Agent Sandbox Patterns

A taxonomy for isolating an AI agent that can **execute arbitrary code**, drawn from Browser Use's production writeup of running millions of web agents. The framing question: once an agent can run code, it can reach anything on the machine — env vars, API keys, DB credentials, internal services. How do you cut that off?^[raw/articles/2026-08-29_browser-use_two-ways-to-sandbox-agents.md]

## The two patterns

| | Pattern 1: Isolate the **tool** | Pattern 2: Isolate the **agent** |
|---|---|---|
| What's sandboxed | Only dangerous ops (code exec, terminal) | The **entire** agent process |
| Where the agent loop runs | On your infrastructure | Inside the sandbox (zero secrets) |
| How it reaches the world | Calls the sandbox over HTTP | Talks **only** to a **control plane** that holds all credentials |
| Secrets exposure | Agent process can still hold secrets | Agent has nothing worth stealing |
| State | Tied to backend; redeploy kills running agents | Disposable — kill/restart/scale freely |
| Deploy count | One service | Three (sandbox + control plane + backend) |

Browser Use started with Pattern 1 and **migrated to Pattern 2**. The motivating pain under Pattern 1: the agent loop shared a process with the REST API — a redeploy killed all running agents, and a memory-hungry agent slowed the API. Two fundamentally different workloads in one process.

## Pattern 2 anatomy (control-plane model)

- **Zero-secret sandbox**: receives exactly three env vars — `SESSION_TOKEN`, `CONTROL_PLANE_URL`, `SESSION_ID` — nothing else (no AWS keys, no DB creds).
- **Control plane as proxy**: the sandbox has no direct internet. Every operation (LLM call, S3 upload, billing) hops through a stateless control plane that looks up the session by bearer token and executes with real credentials.
- **Server-side conversation state**: the sandbox sends only new messages; the control plane owns and reconstructs full history — so the sandbox is stateless and disposable.
- **Presigned-URL file access**: sandbox gets scoped S3 access without ever holding an AWS credential.
- **Gateway interface** (`invoke_llm`, `persist_messages`) with production (`ControlPlaneGateway`) and local (`DirectGateway`) implementations — same agent code, swappable backend.

### Hardening (Browser Use specifics)
1. **Bytecode-only** — compile Python to `.pyc`, delete all `.py`; framework loaded as root, source gone.
2. **Privilege drop** — root entrypoint → `setuid`/`setgid` to unprivileged `sandbox` user before agent code runs.
3. **Env stripping** — read the 3 vars into memory, then `del` from `os.environ`; VM in a private VPC with no egress except the control plane.

### Runtime substrate
Same image everywhere: **Unikraft micro-VM** in production (boots <1s, scale-to-zero, distributed across metros) vs **Docker container** in dev/evals. One `sandbox_mode` switch. The tradeoff is an extra network hop per op + 3 services instead of 1 — negligible vs LLM latency.

## The governing principle

> **Your agent should have nothing worth stealing and nothing worth preserving.**

This reframes agent isolation from "guard the model's behavior" to "make a compromised agent worthless." It is the **out-of-band** counterpart to model-layer defenses: a stolen agent holds no live secrets, and a hijacked agent that does something unwanted has already lost control of its own process, network, and cost caps.

## Relation to in-band vs out-of-band

Micah Lee's agent-safety framing is that LLMs, unlike normal programs, must **receive and obey control signals in-band** — the same channel carries instruction and data, so there is no clean boundary between "data" and "structural token." A control-plane sandbox closes that gap **outside** the model: the agent literally has no permission to touch its own process, network, or cost cap. Prompt-injection can still change what the agent *does inside the sandbox*, but it can't escalate privileges. See [[concepts/prompt-injection]].

## Open questions

- Cost of the extra network hop at the *tool-call* layer vs LLM latency (Browser Use says noise; unproven for sub-second tool loops).
- Where the control plane becomes a single point of failure / scaling bottleneck.
- How far the same-image/dev-parity guarantee degrades as the substrate (micro-VM vs container) diverges in filesystem/permission semantics.

## Related
- [[concepts/sandbox]] — sandbox technology landscape (gVisor, MicroVM, WASM)
- [[concepts/security-and-governance/agent-containment]] — limiting blast radius via environmental isolation
- [[concepts/vm-containment-ai-agents]] — Trail of Bits research on VM containment of cyber-capable agents
- [[concepts/ai-containment-escape]] — when containment fails
- [[concepts/prompt-injection]] — the in-band attack this out-of-band defense blunts
- [[entities/micahflee]] — "in-band" vs "out-of-band" framing for agent control
- [[entities/browser-use]] — the company behind this architecture
- [[concepts/agent-runtime-infrastructure]] — the substrate agents run on

## Sources
- [[raw/articles/2026-08-29_browser-use_two-ways-to-sandbox-agents]] — Browser Use, "How We Built Secure, Scalable Agent Sandbox Infrastructure" (2026-02-25)
