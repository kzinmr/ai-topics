---
title: "NVIDIA OpenShell"
type: entity
tags:
  - nvidia
  - agent-runtime
  - sandbox
  - security
  - open-source
status: complete
description: "NVIDIA's open-source secure runtime for autonomous AI agents. Provides sandboxed execution with kernel-level isolation and declarative YAML policy enforcement."
created: 2026-04-30
updated: 2026-11-02
sources:
  - "https://github.com/NVIDIA/OpenShell"
  - "https://developer.nvidia.com/blog/run-autonomous-self-evolving-agents-more-safely-with-nvidia-openshell"
  - "https://docs.nvidia.com/openshell/about/overview"
  - "https://x.com/hwchase17/status/2034297125417460044"
related:
  - "[[entities/nvidia]]"
  - "[[entities/nvidia-nemoclaw]]"
  - "[[concepts/security-and-governance/agent-sandboxing]]"
  - "[[concepts/harness-engineering]]"
---

# NVIDIA OpenShell

**OpenShell** is an open-source runtime (Apache 2.0) developed by NVIDIA for executing autonomous AI agents in sandboxed environments with kernel-level isolation. It is the **"Open Runtime"** in Harrison Chase's Model + Runtime + Harness architecture decomposition.

## Core Thesis

> "AI agents are most useful when they can read files, install packages, call APIs, and use credentials. That same access can create material risk. OpenShell is designed for this tradeoff: preserve agent capability while enforcing explicit controls over what the agent can access." — NVIDIA OpenShell Docs

OpenShell sits **between the agent and the infrastructure**, governing:
- **How** the agent executes
- **What** the agent can see and do
- **Where** inference goes (model routing)

## Architecture

### Three-Layer Protection

| Layer | Protection | Enforcement Timing |
|---|---|---|
| **Filesystem** | Prevents reads/writes outside allowed paths | Locked at sandbox creation |
| **Network** | Blocks unauthorized outbound connections | Hot-reloadable at runtime |
| **Process** | Blocks privilege escalation and dangerous syscalls | Locked at sandbox creation |
| **Inference** | Reroutes model API calls to controlled backends | Hot-reloadable at runtime |

### Key Components

| Component | Role |
|---|---|
| **Gateway** | Control-plane API coordinating sandbox lifecycle, acting as auth boundary |
| **Sandbox** | Isolated container with policy-enforced egress routing |
| **Policy Engine** | Enforces filesystem, network, and process constraints from application to kernel level |
| **Privacy Router** | Privacy-aware LLM routing — strips caller credentials, injects backend credentials, forwards to managed model |

### Sandbox Lifecycle

```
Provisioning → Ready → (Execution) → Deleting
                        ↑
                      Error (check logs)
```

## Quick Start

```bash
# Create a sandbox with default agent
openshell sandbox create -- claude  # or opencode, codex, copilot

# Deploy on remote host
openshell sandbox create --remote spark --from openclaw
```

### Default Sandbox Tools

| Category | Tools |
|---|---|
| Agent | `claude`, `opencode`, `codex`, `copilot` |
| Language | `python` (3.13), `node` (22) |
| Developer | `gh`, `git`, `vim`, `nano` |
| Networking | `ping`, `dig`, `nslookup`, `nc`, `traceroute`, `netstat` |

## Deployment Models

| Type | Where | Best For |
|---|---|---|
| **Local** | Docker on workstation | Solo development, quick iteration |
| **Remote** | Docker on remote host via SSH | DGX Spark, powerful machines |
| **Cloud** | Behind reverse proxy (Cloudflare Access) | Individual users behind cloud VM |

## Connection to Agent Runtime Theory

OpenShell validates the user's insight about **runtime determining native tool-use patterns**:

- **Agent on bash** → OpenShell provides CLI as the native execution environment → tools are shell commands
- **Agent on Python REPL** → OpenShell provides python3 in the sandbox → tools are Python functions
- **Heterogeneous agents** → OpenShell's Gateway abstracts the runtime differences → agents communicate via MCP/A2A protocols

The runtime **is** the interface contract. Different runtimes naturally select different tool-use patterns, and MCP serves as the universal adapter between them.

## Integration with NemoClaw

OpenShell is the runtime component of **NVIDIA NemoClaw**, the reference stack for "always-on" personal assistants (claws). NemoClaw bundles:
- OpenShell (sandbox runtime)
- OpenClaw-compatible agent framework
- NVIDIA Nemotron models

## Launch (October 2026)

OpenShell's README launch reached Hacker News on 2026-10-22 at ~499 points. At launch the repo carried ~19.7k stars, ~2.0k forks and 1,861 commits; the **0.1.x** line introduced a stable release cadence, new isolation primitives, an expanded extension surface, and new APIs. Docs: `docs.nvidia.com/openshell/latest/`.

- **Implementation**: Apache-2.0 licensed, written in **Rust**.
- **Two enforcement axes**: (1) kernel-level runtime enforcement — file/syscall confinement plus a policy check on *every* outbound connection; (2) **formally verified policy changes** — an advisor + prover pair in the Policies subsystem flags risky new access (new host with credentials, new API method) so such changes wait for human review. See [[concepts/formal-methods]].
- **Egress credential injection**: agents never see real credentials; OpenShell injects secrets only onto requests bound for approved endpoints — the same "secrets-at-egress" pattern independently surfaced by Google's per-agent microVM work, implemented here as a policy-governed gateway.
- **Platform**: Linux, macOS (Apple Silicon), Windows via WSL 2 (experimental); Docker, Podman or host virtualization. One-line `install.sh`, then `openshell sandbox create --name demo`.
- **Agent-first tooling**: `npx skills add NVIDIA/OpenShell` skill, plus `@nvidia/openshell-sdk` (npm), Go and Rust SDKs. The repo dogfoods agent-driven development (`AGENTS.md`, `CLAUDE.md`, `.opencode/agents`, `skills/`, `rfc/` board). Telemetry is anonymous operational counts only (disable via `OPENSHELL_TELEMETRY_ENABLED=false`).
- **Positioning**: peer to [[entities/e2b]], Modal/Cloudflare agent runtimes, the Claude Code sandbox, OpenAI's Codex sandbox and [[concepts/omnara]] — distinguished by kernel syscall-level enforcement + formal verification of *policy diffs* (not of the code the agent runs) + egress credential injection.

## Related Concepts

- [[concepts/security-and-governance/agent-sandboxing]] — OpenShell implements Level 2-3 sandboxing (container/microVM)
- [[concepts/harness-engineering]] — OpenShell is the "Open Runtime" layer
- [[concepts/deep-agents]] — LangChain's harness runs inside OpenShell's runtime
- [[concepts/security-and-governance/agent-governance]] — Policy engine enforces governance at infrastructure level
- [[concepts/security-and-governance/agent-iam]] — Gateway serves as authentication/authorization boundary
