---
source_url: https://browser-use.com/posts/two-ways-to-sandbox-agents
title: "How We Built Secure, Scalable Agent Sandbox Infrastructure"
site: Browser Use
published: 2026-02-25
author: Browser Use
source_type: newsletter
fetched_via: r.jina.ai (SPA-rendered page; curl returns empty shell)
ingested: 2026-08-29
---

# How We Built Secure, Scalable Agent Sandbox Infrastructure

Source: https://browser-use.com/posts/two-ways-to-sandbox-agents (published 2026-02-25)

## How we got here

Browser Use runs millions of web agents. They started with **browser-only agents on AWS Lambda** (each invocation isolated, instant scaling, no secrets to worry about). Then they added **code execution** — agents could write/run Python, execute shell, create files — built as an isolated sandbox the agent calls as a tool. Security was fine: code ran in the sandbox, not on the backend.

But the **agent loop still ran on the same backend as the REST API**. Redeploy → all running agents die. Memory-hungry agent → API slows down. Two fundamentally different workloads sharing one process.

## The two patterns

When an agent can run arbitrary code, it can reach anything on the machine: env vars, API keys, DB creds, internal services. It must be isolated from infra + secrets. Two ways:

**Pattern 1: Isolate the tool.** Agent runs on your infrastructure. Dangerous ops (code execution, terminal) run in a separate sandbox the agent calls over HTTP. Code runs somewhere with nothing to leak.

**Pattern 2: Isolate the agent.** The *entire* agent runs in a sandbox with **zero secrets**. It talks to the outside world through a **control plane** that holds all credentials. The agent becomes disposable — no secrets to steal, no state to preserve; kill/restart/scale independently. The control plane holds the truth.

> "We started with Pattern 1 and moved to Pattern 2."

## The sandbox

Same container image runs everywhere. Production = **Unikraft micro-VM** (boots <1s, provisioned via Unikraft Cloud REST API on dedicated bare metal in AWS). Dev/evals = **Docker container**. One config switch (`sandbox_mode: 'docker' | 'ukc'`).

- Sandbox receives only **three env vars**: `SESSION_TOKEN`, `CONTROL_PLANE_URL`, `SESSION_ID`. No AWS keys, no DB creds, no API tokens.
- **Scale-to-zero** from Unikraft: idle VM suspends; resumes on next request. A sandbox between queries costs ~nothing but wakes instantly.
- Sandboxes distributed across multiple Unikraft **metros** to avoid a single-metro bottleneck.
- **Same image, same entrypoint, same control-plane protocol** across laptop / parallel evals / production.

### Hardening (before any agent code runs)
1. **Bytecode-only execution** — compile all Python to `.pyc` at build, delete every `.py`; framework loaded into memory as root, then source is gone.
2. **Privilege drop** — entrypoint starts as root (to read root-owned bytecode), then `setuid`/`setgid` drop to a `sandbox` user; everything after runs unprivileged.
3. **Environment stripping** — after reading the 3 vars into Python, delete them from `os.environ`; agent-inspecting-env finds nothing. Token useless outside the sandbox anyway — VM sits in a private VPC with no permissions except talking to the control plane.

## How the control plane works

A **proxy service**: the sandbox has no direct internet access; every request hops through the control plane (LLM calls, S3 uploads, everything). Stateless FastAPI; each request carries `Bearer: {session_token}`; control plane looks up session, validates active, executes with real credentials.

- **LLM proxying** — sandbox sends only *new messages*; control plane owns full conversation history in DB, reconstructs each call, forwards full context. Keeps the sandbox stateless → kill it, spin up a new one, conversation resumes. Also enforces cost caps + billing.
- **File sync via presigned URLs** — sandbox `/workspace` watched, changes synced to S3, but sandbox never holds AWS creds: asks control plane for `POST /presigned-urls` (scoped to session), uploads directly to S3. Downloads reverse the same way.
- **Gateway protocol** — `AgentGateway` interface (`invoke_llm`, `persist_messages`). Production = `ControlPlaneGateway` (HTTP to control plane); dev/evals = `DirectGateway` (calls LLM directly, history in memory). Agent code doesn't know which backend — same interface, same behavior.

## Scaling

Control plane stateless (validate token, do work, return). More agents → more sandboxes. More throughput → more control-plane instances behind an LB. Backend on **ECS Fargate** in private subnets behind an ALB; control plane auto-scales on CPU; sandboxes scale independently via Unikraft (each session = its own VM, scheduled across metros).

## Wrapping up

Two ways to sandbox a code-executing agent: **isolate the tool** (Pattern 1) or **isolate the agent** (Pattern 2). Browser Use chose Pattern 2: control plane holds all credentials and proxies everything (LLM, file storage, billing); sandbox gets 3 env vars and nothing else; Unikraft micro-VM in prod, Docker in dev/evals; same image everywhere.

Tradeoff: an extra network hop per operation + three services to deploy instead of one. In practice latency is noise vs LLM response times; operational complexity is the kind ops teams already handle.

**Key takeaway: your agent should have nothing worth stealing and nothing worth preserving.**
