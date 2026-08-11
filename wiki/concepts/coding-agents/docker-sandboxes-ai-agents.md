---
title: "Docker Sandboxes — Disposable Isolated Environments for AI Agents"
created: 2026-08-11
updated: 2026-08-11
type: concept
tags:
  - coding-agents
  - sandbox
  - docker
  - ai-safety
  - isolation
  - microvm
  - agent-safety
  - product
  - developer-tooling
status: active
sources:
  - raw/articles/2026-08-10_docker-sandboxes-ai-agents.md
---

# Docker Sandboxes — Disposable Isolated Environments for AI Agents

## Overview

**Docker Sandboxes** is a Docker product (launched mid-2026) that provides **disposable, microVM-isolated execution environments** for AI coding agents. Each agent runs inside a dedicated microVM with the developer's project workspace mounted in, allowing agents to install packages, modify configs, and even spin up their own Docker containers — all without touching the host filesystem or network.

The product is distributed as a standalone CLI (`sbx`) available on macOS, Windows, and Linux (Ubuntu). It integrates with Docker's broader **AI Governance** platform for centralized policy enforcement across teams.

## Key Capabilities

| Capability | Description |
|---|---|
| **MicroVM Isolation** | Each agent gets a dedicated microVM with a separate kernel — a hard security boundary from the host |
| **Filesystem Safety** | Only the project workspace is mounted into the sandbox; the host filesystem is never exposed |
| **Network Controls** | Configurable network access policies — restrict or allow outbound connections per sandbox |
| **Credential Protection** | Credentials are kept out of the sandbox by default; agents cannot exfiltrate secrets |
| **Ephemeral by Default** | Sandboxes are disposable — tear down in one command, no lingering state |
| **Nested Docker** | Agents can spin up containers within the sandbox for service dependencies |
| **Fast Spin-Up** | Starts faster than traditional VMs; uses lightweight microVM technology |
| **YOLO Mode Safe** | Agents run with `--dangerously-skip-permissions` inside the sandbox, giving full autonomy without host risk |

## How It Works

### Architecture

Docker Sandboxes uses a microVM hypervisor layer (Apple Virtualization.framework on macOS, Hyper-V on Windows) to create lightweight, kernel-isolated environments. Each sandbox:

1. **Boots a dedicated microVM** with its own kernel and Docker daemon
2. **Mounts the project workspace** via bidirectional file sync (not direct bind mount)
3. **Routes network traffic** through a filtering proxy for policy enforcement
4. **Provides a per-VM Docker socket** so agents can run nested containers
5. **Disposes cleanly** — `sbx dispose` tears down the entire VM

The underlying daemon (`sandboxd`) communicates over a local Unix socket and manages VM lifecycle, file sync, and network proxy configuration. The reverse-engineered internals of this API are documented at [[concepts/docker-sandbox-microvm-api]].

### CLI Quick Start

```bash
# macOS
brew trust docker/tap && brew install docker/tap/sbx

# Windows
winget install Docker.sbx

# Linux (Ubuntu)
curl -fsSL https://get.docker.com | sudo REPO_ONLY=1 sh
sudo apt-get install docker-sbx
```

## Supported AI Coding Agents

Docker Sandboxes works out of the box with leading coding agents:

- **Claude Code** — Anthropic's agentic coding CLI
- **Codex** — OpenAI's coding agent
- **GitHub Copilot CLI** — GitHub's terminal-native agent
- **OpenCode** — Open-source coding agent
- **Kiro** — Agentic coding tool
- **Gemini CLI** — Google's coding agent

Custom agent configurations are also supported through the Sandbox Agent SDK. Agents run in "YOLO mode" (`--dangerously-skip-permissions`) by default inside the sandbox — full autonomy, no permission prompts, no manual review required.

## Security Model

### Defense in Depth

Docker Sandboxes implements a layered security model:

| Layer | Mechanism |
|---|---|
| **Kernel Isolation** | Separate microVM kernel — no shared kernel attack surface |
| **Filesystem Boundary** | Only workspace directory mounted; host FS inaccessible |
| **Network Filtering** | MITM-capable proxy enforces egress policies |
| **Credential Separation** | Agent never sees host credentials or environment variables |
| **Ephemeral Lifecycle** | Disposable VMs prevent state accumulation attacks |
| **Org-Wide Governance** | Centralized policy enforcement via Docker AI Governance |

### Comparison with Standard Docker Containers

| Feature | Docker Container | Docker Sandbox |
|---|---|---|
| **Kernel** | Shared with host | Separate (microVM) |
| **Untrusted code** | Not safe | Safe |
| **Network** | Direct access | Filtering proxy |
| **Filesystem** | Direct bind mount | Bidirectional sync |
| **Platform** | Linux, macOS, Windows | macOS, Windows, Linux (Ubuntu) |
| **Isolation Level** | Process-level (namespaces) | Hardware-level (microVM) |

Standard Docker containers share the host kernel and are unsuitable for running untrusted AI-generated code. Sandboxes provide the strong isolation boundary that agent workloads demand.

## Use Cases

### Unattended Agent Execution
Agents can run long-duration tasks without supervision — code generation, test suite execution, dependency installation, service orchestration — all safely contained.

### Multi-Agent Development
Multiple agents can work on different parts of a codebase simultaneously, each in its own isolated sandbox, without interfering with each other or the host.

### Untrusted Repository Work
Clone and explore third-party repositories safely. Even if the repo contains malicious code or the agent is prompt-injected, the sandbox boundary prevents host compromise.

### CI/CD Agent Pipelines
Run AI coding agents as part of CI/CD pipelines with VM-level isolation — agents can modify code, run tests, and create commits inside the sandbox, with results synced back only after validation.

## Comparison with Other Sandboxing Approaches

| Approach | Isolation Type | Startup | Platform | Agent-Ready | Pricing |
|---|---|---|---|---|---|
| **Docker Sandboxes** | microVM | ~seconds | macOS, Windows, Linux | Yes (native CLI) | Free (Personal) / Included in subscriptions |
| **Modal Sandboxes** | Cloud VM | ~1-2s warm | Cloud (Linux) | Yes (via SDK) | Per-second billing |
| **Firecracker** | microVM | ~125ms | Linux (KVM) | Requires integration | Open source / AWS |
| **gVisor** | User-space kernel | ~seconds | Linux | Requires integration | Open source |
| **E2B** | Cloud VM | ~seconds | Cloud | Yes (SDK) | Per-use pricing |

See also: [[concepts/security-and-governance/agent-sandboxing]] for a comprehensive survey of isolation technologies, [[concepts/firecracker]] for Firecracker microVM details, and [[concepts/modal-sandboxes]] for Modal's cloud sandbox approach.

## Pricing Model

Docker Sandboxes is included in Docker subscriptions:

| Tier | Price | Sandbox Access |
|---|---|---|
| **Docker Personal** | Free | Included |
| **Docker Pro** | $9/user/month (annual) | Included |
| **Docker Team** | $15/user/month (annual) | Included |
| **Docker Business** | $24/user/month (annual) | Included |

**Docker AI Governance** (additional enterprise tier) adds centralized admin controls: network access policies, filesystem rules, MCP governance, and audit logging — defined once, enforced across all developer machines. This is sold separately; contact Docker for pricing.

Docker Desktop is **not required** to use Sandboxes — the `sbx` CLI works standalone.

## Ecosystem Partnerships

Docker Sandboxes has been endorsed and integrated by:

- **NanoClaw** — Creator Gavriel Cohen: "Docker Sandboxes is what [agent safety through infrastructure walls] looks like at the infrastructure level"
- **Warp** — Engineering Lead Ben Navetta: integrating Sandboxes so agents run consistently whether local or cloud
- **NVIDIA Open Secure AI Alliance** — Docker joined (July 2026) to help build security, governance, and trust frameworks for agentic AI

## Related Pages

- [[concepts/docker-sandbox-microvm-api]] — Reverse-engineered internals of the `sandboxd` MicroVM API
- [[concepts/security-and-governance/agent-sandboxing]] — Comprehensive survey of agent sandboxing technologies (gVisor, Firecracker, WASM, etc.)
- [[concepts/security-and-governance/ai-safety]] — AI safety overview and alignment strategies
- [[concepts/security-and-governance/agent-governance]] — Agent governance policies and enforcement
- [[concepts/firecracker]] — Firecracker microVM technology (powers AWS Lambda/Fargate)
- [[concepts/modal-sandboxes]] — Modal's cloud-hosted sandbox approach for coding agents
- [[concepts/coding-agents/coding-agents]] — Coding agents overview and ecosystem
