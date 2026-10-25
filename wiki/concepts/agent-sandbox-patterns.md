---
title: "Agent Sandbox Patterns (Isolate-the-Tool vs Isolate-the-Agent)"
created: 2026-08-29
updated: 2026-10-25
type: concept
tags: [concept, ai-agents, agent-safety, sandbox, isolation, security, infrastructure]
sources:
  - raw/articles/2026-08-29_browser-use_two-ways-to-sandbox-agents.md
  - raw/articles/2026-10-16_mlejva_sandboxes-are-dead.md
  - raw/articles/martinalderson.com--posts-interesting-systemd-features--ef189b6f.md
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

## Sandbox → Platform (2026-10)

E2B CEO Vasek Mlejnsky's "Sandboxes are dead" thesis marks the security-adjacent framing ("isolated box for untrusted code") colliding with the production-operations framing: for long-running wave-three agents, the isolation boundary must come bundled with a full operating environment (dedicated storage, firewall, inter-sandbox networking, observability, elastic compute, browsers, secrets management). In Browser Use's terms this is what the control plane grows into once it also owns provisioning, policy, *and* the agent's whole runtime environment — the sandbox becomes a per-agent private cloud. The two framings are complementary, not contradictory: the "nothing worth stealing/preserving" principle governs what the platform gives the agent; the platform thesis governs what the agent can ask for. See [[entities/e2b]] and [[concepts/sandbox/infrastructure]].

## The hobbyist-tier third option: systemd user scopes (2026-10)

Martin Alderson's survey of "interesting systemd features you may not know about" is the desktop/local counterpart to the patterns above: for a single machine running **agent-written throwaway code**, container or micro-VM isolation is often overkill, and the kernel primitives those tools use are already exposed by systemd user scopes. His framing — systemd is "the plumbing you need without having to roll your own, especially for the huge amount of almost 'disposable' software you tend to end up with these days" — is Pattern-1 thinking at personal scale: cap the dangerous process, don't rebuild the world around it.^[raw/articles/martinalderson.com--posts-interesting-systemd-features--ef189b6f.md]

The primitives that matter for agents (Linux only; `launchd` covers cron-style scheduling on macOS but not resource limits):

| Primitive | Agent use |
|---|---|
| `systemd-run --user --scope -p MemoryMax=4G -p CPUQuota=200% claude` | Bound a leaky agent-written script before it OOM-kills the machine. **Same cgroup limits Docker uses**, so the cap is real, not advisory. `systemd-cgtop` gives per-cgroup visibility instead of `top`. |
| `-p RuntimeMaxSec=30m` | Hard wall-clock ceiling on an autonomous run. Alderson's OpenCode example needs `--standalone`, because OpenCode otherwise dispatches work to an already-running background server that **bypasses the time limit** — a general pitfall for any agent with a daemon mode. |
| `systemd-inhibit --what=sleep:idle:handle-lid-switch` | Keep a laptop-lidded agent run alive; combine with `RuntimeMaxSec` so it can't drain the battery. |
| `Persistent=true` | Catch-up execution when the machine was off/sleeping — the difference between "ran at 9am" and "ran at 9am *whenever the laptop next woke*", which is what scheduled personal agents actually need. |
| `OnSuccess=` / `OnFailure=` | Wire results to a Slack/email unit, and hang a **dead man's handle** off the unit (Healthchecks.io-style) — the notification path becomes part of the unit, not the script. |
| `RandomizedDelaySec=` | Jitter to avoid a fleet of machines hitting a service simultaneously. |
| `.path` units (`DirectoryNotEmpty=%h/agent-inbox`) | Event-driven agent triggering without a cron daemon: drop a file in a folder (expenses, invoices) and a scoped service categorises it, with `RuntimeMaxSec` + `MemoryMax` baked into the paired unit. |

**The caveat Alderson flags is the important one for safety**: systemd also ships sandboxing directives (`ProtectHome`, `ReadWritePaths`, and friends) that "you'd think would be perfect for agents. But there are so many footguns with it that's too long to explain in this article." That is exactly the Pattern-1 failure mode — cgroup **limits** are hard guarantees from the kernel, while systemd's **filesystem/network sandboxing** directives are opt-in, default-open, and easy to under-specify, so treating "it's in a systemd unit" as equivalent to "it's isolated" is a mistake. Limits contain a misbehaving agent's *resource* damage; they do nothing about credential access or egress, which is why the control-plane model above still wins wherever secrets are in reach.

## Related
- [[entities/e2b]] — "Sandboxes are dead" / agent-driven private cloud thesis
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
