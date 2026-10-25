---
title: "NVIDIA OpenShell — safe, private runtime for autonomous AI agents (README)"
url: https://github.com/NVIDIA/OpenShell
source: nvidia-openshell
source_name: NVIDIA OpenShell
date: 2026-10-23
fetched_at: 2026-10-25
type: article
tags: [ai-agents, agent-platform, sandbox, security, open-source, infrastructure]
license: Apache-2.0
status: complete
note: "Date is approximate (repo Last-Modified not exposed); HN discussion 2026-10-22, 0.1.x stable release cadence announced around that window."
---

# NVIDIA OpenShell

**OpenShell is the safe, private runtime for fleets of autonomous AI agents.** NVIDIA, Apache-2.0, Rust codebase. HN launch 2026-10-22 (~499 points / 217 comments). Repo: `github.com/NVIDIA/OpenShell`, ~19.7k stars, ~2.0k forks, 1,861 commits. Docs: `docs.nvidia.com/openshell/latest/`.

## Core premise

Agents are most useful when they can read files, install packages, call APIs, and use credentials. OpenShell gives them that capability **without giving them unrestricted access to your data, secrets, or network**. You declare what each agent can touch in a **policy**, and OpenShell enforces it.

## Two enforcement mechanisms

1. **Kernel-level enforcement.** Each agent runs in an isolated sandbox. Kernel controls confine which files it can access and which system calls it can make; every network connection passes through a policy check before leaving the sandbox. Agents never see real credentials — OpenShell injects them **only on requests bound for approved endpoints** (egress credential injection).
2. **Formally verified policy changes.** Before a policy change is approved, OpenShell uses **formal verification** to flag risky new access it would grant (e.g., reaching a new host with credentials, or calling a new API method) so those changes wait for human review.

## New in 0.1.x

A stable release cadence, new isolation primitives, an expanded extension surface, and new APIs. (0.1.0 upgrade guide provided.)

## Architecture components

- **Sandboxes** — images, runtimes, GPUs, lifecycle. Default sandbox image is minimal Ubuntu with no agent installed.
- **Policies** — filesystem, network, and process rules, with the **advisor** and **prover** for reviewing changes.
- **Providers** — credentials that work only at approved endpoints, including `inference`.
- **Gateways** — the control plane for sandboxes, policy, and access (gateway + supervisor + sandbox split; see Architecture doc).
- **Kubernetes** — deploy the gateway with Helm; your CNI must enforce NetworkPolicy.
- **Extensibility** — middleware, interceptors, and compute drivers.

## Install / quickstart

```
curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh
openshell sandbox create --name demo
```

Requires Linux, macOS on Apple Silicon, or Windows with WSL 2 (experimental), plus Docker, Podman, or host virtualization.

## Skills & SDKs

- Agent skills: `npx skills add NVIDIA/OpenShell` — teaches a coding agent to drive the OpenShell CLI, write sandbox policies, debug gateways and inference routing.
- SDKs: `@nvidia/openshell-sdk` (npm), `github.com/NVIDIA/OpenShell/sdk/go`, `openshell-sdk` (cargo). SDKs connect applications to a gateway; they don't install the CLI.
- Example first agent: runs OpenCode against a free OpenRouter model, demonstrating approval of new access as the agent needs it.

## Telemetry

Anonymous operational categories/counts only. Does NOT collect sandbox names, hostnames, file paths, prompts, credentials, provider/model names, or user content. Disable with `OPENSHELL_TELEMETRY_ENABLED=false` / `server.telemetryEnabled=false`.

## Agent-first development

Built agent-first: developed with the same agent-driven workflows it enables. Repo carries AGENTS.md, CLAUDE.md, .claude/, .opencode/agents, skills/, rfc/ — i.e., dogfoods coding-agent workflows for its own development.

## Positioning

A direct competitor/peer to agent sandbox runtimes (E2B, Modal sandboxes, Cloudflare agents, Anthropic's Claude Code sandbox, OpenAI's Codex sandbox) and to the broader "harness + isolation" category. Distinctives vs peers: kernel syscall-level enforcement + formal verification of policy diffs + egress credential injection so agents never hold raw secrets.
