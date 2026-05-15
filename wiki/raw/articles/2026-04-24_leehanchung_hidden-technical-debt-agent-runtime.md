---
title: "Hidden Technical Debt of AI Systems: Agent Runtime"
source: "https://leehanchung.github.io/blogs/2026/04/24/hidden-technical-debt-agent-runtime/"
author: "Han Lee (Hanchung Lee)"
published: "2026-04-24"
type: blog_post
tags: [agent-runtime, agent-harness, technical-debt, sandbox, isolation, infrastructure]
---

Eleven years ago, Sculley et al. drew the diagram everyone in MLOps has seen: a tiny black box labeled "ML Code" surrounded by a sprawl of much larger boxes — data collection, feature extraction, configuration, monitoring, serving infrastructure. The point of the diagram was that the model code is the smallest piece of a real ML system, and that everything else is where the technical debt accumulates.

The same diagram is being redrawn for agents. The agentic model call is the small box. The largest box to the right that is currently driving most of the spend and influencing how system architecture will be done in the future is the **agent runtime**, or agent serving infrastructure.

The agent is not the model. The agent is the harness plus the model, running inside the runtime. And almost nobody is treating it that way.

## What an Agent Runtime Actually Is

An agent runtime is the union of:
- **compute substrate** — a container, microVM, or full VM where code runs
- **filesystem** — the agent can read and write, often with snapshot and rollback semantics
- **tools** — shell, code interpreter, browser, file editor, MCP servers — exposed to the model as callable interfaces
- **network boundary** — that defines what the agent can reach and what can reach it
- **state model** — that decides what persists across turns, across episodes, and across users
- **lifecycle controller** — that starts, suspends, snapshots, resumes, and tears down environments

In the taxonomy of RL environments for LLM agents, these are the H (harness) and S (state) components. In production, this is the part that decides whether your agent finishes a task in eight seconds or eight minutes, whether two users can share an environment safely, and whether a malicious prompt can read your secrets.

## Why Sandboxing Is Not Optional

Models hallucinate code. They run `rm -rf`. They paste credentials into curl commands. They follow instructions embedded in untrusted documents. They retry the same failing command in a tight loop and burn through a quota.

Four reasons sandboxing must exist as a first-class layer:

1. **Isolation against the model's mistakes** — Filesystem isolation, copy-on-write snapshots, and per-session ephemerality turn destructive actions into recoverable ones.
2. **Isolation against prompt injection** — Tool outputs are attacker-controlled the moment the agent visits a webpage, opens a PDF, or processes a customer email. This is the agent-systems version of the SQL injection lesson, and we are at roughly the 2003 stage of learning it.
3. **Multi-tenancy at training scale** — RL training spins up thousands of concurrent rollouts. Each rollout needs its own filesystem, process tree, and network namespace.
4. **Reproducibility** — A sandbox you can snapshot is a sandbox you can replay. Replay is how you debug a six-hour agent trajectory without re-running the whole thing.

Cognition team's post-mortem: containerized agents share a kernel, and a single compromised session can reach every other container's filesystem, credentials, and network connections. Their conclusion after more than a year of hypervisor engineering: **VM-level isolation, where each session gets its own kernel**.

## The Isolation Primitive Stack

| Primitive | Isolation model | Cold start | Workload fit | Notable users |
|---|---|---|---|---|
| Linux containers (runc, Podman) | Shared host kernel, namespaces + cgroups + seccomp | ~100ms | Trusted code, internal CI | Docker, Kubernetes default |
| Firecracker | KVM-based microVM, dedicated kernel per VM | ~125ms boot, sub-second from snapshot | Untrusted code at high density | AWS Lambda, Fargate, E2B, Fly.io |
| gVisor | Userspace kernel intercepting syscalls; runc-compatible | Container-class | Defense in depth | Google Cloud Run, App Engine, Modal |
| Kata Containers | Lightweight VM per pod, OCI-compatible | Few hundred ms | Multi-tenant Kubernetes | Confidential Containers |
| V8 isolates | Per-tenant JS heap inside a single process | Sub-millisecond | JavaScript-only, no arbitrary binaries | Cloudflare Workers, Deno Deploy |

Key takeaways:
- **Containers are not a sandbox for agent code** — shared kernel means a kernel exploit takes down the isolation boundary
- **Firecracker is the de facto industry primitive** — strong isolation, fast boot, high density
- **gVisor is the middle path** — stronger isolation than namespaces without full VM cost
- **V8 isolates are the wrong primitive for general agent workloads** — cannot run arbitrary Python, install packages, or execute compiled binaries

## The Startup Sandbox Landscape

| Vendor | Isolation | Snapshot model | Cold start | Notable |
|---|---|---|---|---|
| Modal | gVisor | Filesystem diffs from base image | Sub-second | GPU support |
| E2B | Firecracker microVM | Full VM snapshot | ~150ms | Open-source SDK, language-agnostic |
| Daytona | Containers / VMs | Forkable workspaces | Few seconds | Forked dev environments |
| Northflank | Containers, GPU-aware | Persistent volumes | Container-class | GPU sandboxes |
| Browserbase / Steel / Hyperbrowser | Containerized browsers | Session replay | Seconds | Browser-only runtimes |
| Cloudflare Workers Sandbox | V8 isolates + containers | Object snapshots | Milliseconds | Edge-first |
| Vercel Sandbox | Firecracker | Snapshot from build | Sub-second | Tied to Vercel deploy/preview |

Reference case: **Ramp Inspect** — background coding agent writes >50% of Ramp's merged PRs, each session in its own Modal sandbox containing Postgres, Redis, Temporal, RabbitMQ, VS Code server, and VNC/Chromium. Filesystem snapshots refreshed every 30 minutes by cron.

## Hyperscaler Sandbox Landscape

- **AWS Bedrock AgentCore** — Code Interpreter + Browser Tool. MicroVM-class. Per-session pricing. Limited heterogeneous workload support.
- **Azure Container Apps Dynamic Sessions** — Hyper-V isolation, sub-second start for code interpreter. Strongest if on Azure OpenAI + AKS.
- **GCP Cloud Run Sandboxes** — Ahead of pack in usability. Built on Cloud Run (gVisor). Supports heterogeneous workloads.

Lambda, Fargate, App Runner, Cloud Run are **not suitable** as agent sandboxes — designed for stateless, request-response workloads with strict execution-time limits, no native snapshot model.

## Experimentation and Production Want Different Runtimes

| Dimension | Experimentation / Training | Production / Serving |
|---|---|---|
| Concurrency shape | Thousands of parallel rollouts, bursty | One session per user, steady-state |
| Cold start tolerance | Critical — 5s × 10k rollouts is real money | Forgivable — users wait |
| State model | Fork, branch, replay, snapshot | Durable, per-user, auditable |
| Network policy | Often offline or recorded for determinism | Open internet, real APIs |
| Failure model | Drop the rollout, sample more | Retry, degrade, page someone |
| Observability | Full trace, every token, replayable | SLOs, error budgets, sampling |
| Cost model | Spot, preemptible, batch | Reserved, predictable, latency-bound |
| Optimizing the same runtime for both is how you end up too slow for training and too brittle for production.

## Dev/Prod Parity: Runtime Shift

The agent learns the runtime — tool latencies, failure modes, shell quirks, filesystem layout. Move to a different runtime and behavior shifts. This is **runtime shift**: a new flavor of distributional shift where silent quality regressions occur that no eval catches because the eval runs in the training runtime.

Three honest paths:
1. **Co-locate train and prod on the same runtime** — pick one sandbox provider, accept the lock-in
2. **Define a runtime contract** — versioned interface covering API surface, timing, and failure semantics
3. **Train against production noise** — inject latency, errors, and tool failures during training (Step-DeepResearch reports tangible gains from 5-10% tool errors)

## The Bill That Is Coming Due: Runtime Debt

Runtime debt: team picks the sandbox easiest at prototype time → production exposes different failure modes → patches with retries, longer timeouts, prompt-engineered apologies → agent behavior gets entangled with that runtime's quirks → switching runtimes becomes a six-month migration.

The agent has to live on a runtime. The teams that internalize that early will spend the next two years compounding the advantage.

## References
- Sculley et al. (2015). Hidden Technical Debt in Machine Learning Systems. NeurIPS.
- Wiggins, A. (2011). The Twelve-Factor App.
- Lee, H. (2026). A Taxonomy of RL Environments for LLM Agents.
- Workman, G. (2026). How Ramp built a full-context background coding agent on Modal.
- Lopopolo, R. (2026). Harness engineering: leveraging Codex in an agent-first world. OpenAI.
- Cognition. (2026). What We Learned Building Cloud Agents.
- Northflank. (2026). Top Modal Sandboxes Alternatives for Secure AI Code Execution.
- Step-DeepResearch (2025). arXiv:2512.20491.
