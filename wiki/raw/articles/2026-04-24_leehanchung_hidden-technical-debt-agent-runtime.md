---
title: "Hidden Technical Debt of AI Systems: Agent Runtime"
source: "https://leehanchung.github.io/blogs/2026/04/24/hidden-technical-debt-agent-runtime/"
author: "Hanchung Lee (Han Lee)"
date: 2026-04-24
source_type: blog
source_domain: leehanchung.github.io
tags: [agent-runtime, sandboxing, agent-architecture, technical-debt, isolation, firecracker, gvisor]
---

# Hidden Technical Debt of AI Systems: Agent Runtime

> **"The agent is not the model. The agent is the harness plus the model, running inside the runtime. And almost nobody is treating it that way."**

*A re-drawing of the famous "Hidden Technical Debt" diagram (Sculley et al., 2015): the agentic model call is the small black box; the largest, most expensive, and most impactful surrounding box is the **agent runtime**.*

---

## 1. What an Agent Runtime Actually Is

An agent runtime is the environment where the agent model + harness execute, encompassing:

- **Compute substrate** – container, microVM, or full VM
- **Filesystem** – with snapshot/rollback semantics
- **Tools** – shell, code interpreter, browser, file editor, MCP servers
- **Network boundary** – defines reachability both ways
- **State model** – persistence across turns, episodes, users
- **Lifecycle controller** – start, suspend, snapshot, resume, tear down

In the RL taxonomy for LLM agents, these are the **H** (harness) and **S** (state) components.

---

## 2. Why Sandboxing Is Not Optional

Models hallucinate, run `rm -rf`, paste credentials into `curl`, follow instructions embedded in untrusted documents, and retry failures in tight loops that burn quotas.

> **"A sandbox is the only thing standing between an injected instruction and your production database. This is the agent-systems version of the SQL injection lesson, and we are at roughly the 2003 stage of learning it."**

Four first-class reasons for a sandbox layer:

1. **Isolation against the model's mistakes** – Filesystem isolation, copy-on-write snapshots, per-session ephemerality
2. **Isolation against prompt injection** – Tool outputs are attacker-controlled; sandbox prevents compromised output from reaching production data
3. **Multi-tenancy at training scale** – Thousands of concurrent RL rollouts each need their own filesystem, process tree, network namespace
4. **Reproducibility** – Snapshotted sandboxes enable replay for debugging and regression testing

> **"A web app's runtime can be sloppy because the user is the one driving and a refresh fixes most things. An agent's runtime cannot, because the agent will keep going long after a human would have stopped to ask a question."**

**Cognition's conclusion** (after a year of hypervisor engineering for Devin): **VM-level isolation is mandatory** — container-shared kernels allow a single compromised session to reach all others. **Manus** famously snapshotted all agent runtimes for future replay.

---

## 3. The Isolation Primitive Stack

| Primitive | Isolation model | Cold start | Workload fit | Notable users |
|---|---|---|---|---|
| **Linux containers** | Shared host kernel | ~100 ms | Trusted code, internal CI | Docker, Kubernetes default |
| **Firecracker** | KVM-based microVM, dedicated kernel per VM | ~125 ms boot, sub-second from snapshot | Untrusted code at high density | AWS Lambda, Fargate, E2B, Fly.io, Vercel Sandbox |
| **gVisor** | Userspace kernel intercepting syscalls; runc-compatible | Container-class | Defense in depth where microVM is overkill | Google Cloud Run, App Engine, Modal |
| **Kata Containers** | Lightweight VM per pod, OCI-compatible | Few hundred ms | Multi-tenant Kubernetes | Confidential Containers, some managed K8s |
| **V8 isolates** | Per-tenant JS heap inside a single process | Sub-millisecond | JavaScript-only, no arbitrary binaries | Cloudflare Workers, Deno Deploy |

**Key judgments:**
- **Containers are not a sandbox for agent code.** They are packaging + resource control; a kernel exploit breaks isolation completely.
- **Firecracker is the de facto industry primitive.** Strong isolation, ~5 MB VMM, boots a stripped-down Linux kernel in ~125 ms.
- **gVisor** offers stronger isolation than namespaces without full VM cost, but some syscalls are slower/unsupported.
- **Kata Containers** enables untrusted workloads on Kubernetes but inherits pod-lifetime assumptions.
- **V8 isolates are wrong for general agent workloads** that need arbitrary Python, package installs, browsers, or compiled binaries.

---

## 4. The State Model: Snapshot, Replay, Rollback

State management primitives:
- **Filesystem snapshots** (copy-on-write)
- **Memory snapshots** (CRIU, VM snapshots)
- **Session replay** (deterministic re-execution)
- **State export/import** (checkpoint-restore)

> "The ability to snapshot and replay agent sessions is not a nice-to-have. It is the foundation of debugging, evaluation, and iterative improvement of agent behavior."

---

## 5. Network Boundary Design

Six patterns:
1. **No network** – air-gapped sandbox
2. **Egress-only allowlist** – explicit domains only
3. **Proxy-mediated** – all traffic through controllable proxy
4. **Credential brokering** – sandbox never sees secrets
5. **VPN/VPC peering** – private network access
6. **Full internet** – unrestricted (dangerous)

---

## 6. Lifecycle Management

- **Cold start** – provision new sandbox from image
- **Warm start** – resume from snapshot
- **Suspend** – pause and save state
- **Resume** – restore from suspend
- **Teardown** – destroy sandbox, archive artifacts

---

## 7. The Startup/Runtime Cost Distribution

> "For a typical agent task that takes 30 minutes: 15 seconds is model inference, 30 seconds is tool execution, and 29 minutes is waiting for the runtime to do its job. The runtime is where the time goes."

---

## Summary Table

| Concern | Web App Runtime | Agent Runtime |
|---|---|---|
| User drives interaction | Yes | No – agent is autonomous |
| Refresh fixes most things | Yes | No – state must persist correctly |
| Session isolation | Nice to have | Mandatory |
| Network boundary | Firewall rules | Per-session network policy |
| State snapshot | Rarely needed | Foundation of debugging |
| Multi-tenancy | Request-level | Session-level with complete isolation |

> **"The agent runtime is the single most under-invested layer of the AI stack. It will determine which agent products work and which ones fail at scale."**
