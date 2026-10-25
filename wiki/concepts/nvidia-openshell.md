---
title: "NVIDIA OpenShell (agent runtime)"
type: concept
created: 2026-10-25
updated: 2026-10-25
tags: [ai-agents, agent-platform, sandbox, security, open-source, infrastructure, developer-tools]
sources:
  - "https://github.com/NVIDIA/OpenShell"
  - "https://news.ycombinator.com/item?id=50198675"
  - "[[raw/articles/2026-10-22_nvidia-openshell_readme-launch]]"
confidence: medium
related:
  - "[[concepts/agent-sandbox-patterns]]"
  - "[[concepts/sandbox]]"
  - "[[entities/nvidia]]"
  - "[[concepts/defenseclaw]]"
  - "[[entities/e2b]]"
---

# NVIDIA OpenShell

**OpenShell** is NVIDIA's open-source (Apache-2.0, Rust) **safe, private runtime for fleets of autonomous AI agents**, launched on Hacker News on 2026-10-22 (~499 points). Its pitch: give agents the capabilities that make them useful — reading files, installing packages, calling APIs, using credentials — *without* giving them unrestricted access to your data, secrets, or network. You declare what each agent may touch in a **policy**, and OpenShell enforces it at runtime.

At launch the repo carried ~19.7k stars, ~2.0k forks, and 1,861 commits, with the **0.1.x** line introducing a stable release cadence, new isolation primitives, an expanded extension surface, and new APIs. Docs at `docs.nvidia.com/openshell/latest/`.

## Two enforcement mechanisms

OpenShell governs agent behaviour along two complementary axes:

1. **Kernel-level runtime enforcement.** Each agent runs in an isolated sandbox. Kernel controls confine which **files** it can access and which **system calls** it can make, and **every network connection passes a policy check** before it leaves the sandbox. Agents **never see real credentials** — OpenShell injects secrets only onto requests bound for **approved endpoints** (egress credential injection). This is the same "secrets-at-egress" pattern independently surfaced by Google's per-agent microVM work, but implemented as a policy-governed gateway.

2. **Formally verified policy changes.** Before a policy change is approved, OpenShell uses **formal verification** to flag risky new access it would grant — e.g. reaching a new host with credentials, or calling a new API method — so such changes wait for **human review**. The advisor + prover pair in the Policies subsystem performs this review. See [[concepts/formal-methods]].

## Architecture

| Component | Role |
|---|---|
| **Sandboxes** | Images, runtimes, GPUs, lifecycle. Default image is minimal Ubuntu with no agent installed. |
| **Policies** | Filesystem, network, process rules; **advisor** + **prover** for reviewing diffs. |
| **Providers** | Credentials that work only at approved endpoints, including `inference`. |
| **Gateways** | Control plane for sandboxes, policy, and access — **gateway + supervisor + sandbox** split. |
| **Kubernetes** | Deploy the gateway with Helm; your CNI must enforce NetworkPolicy. |
| **Extensibility** | Middleware, interceptors, compute drivers. |

Runs on Linux, macOS (Apple Silicon), or Windows via WSL 2 (experimental), backed by Docker, Podman, or host virtualization. Quickstart is a one-line installer (`install.sh`) then `openshell sandbox create --name demo`.

## Agent-first tooling

- **Skills**: `npx skills add NVIDIA/OpenShell` — teaches a coding agent to drive the OpenShell CLI, write sandbox policies, and debug gateways / inference routing.
- **SDKs**: `@nvidia/openshell-sdk` (npm), Go (`sdk/go`), and Rust (`openshell-sdk` crate). SDKs connect apps to a gateway; they don't install the CLI.
- The repo **dogfoods** agent-first development: it carries `AGENTS.md`, `CLAUDE.md`, `.claude/`, `.opencode/agents`, `skills/`, and an `rfc/` board — i.e. it is built with the same agent-driven workflows it enables. Telemetry is anonymous operational counts only (no sandbox names, paths, prompts, or credentials; disable via `OPENSHELL_TELEMETRY_ENABLED=false`).

## Positioning

OpenShell enters the crowded **agent-sandbox / harness-runtime** category alongside [[entities/e2b]] (Firecracker microVM sandboxes), Modal/Cloudflare agent runtimes, Anthropic's Claude Code sandbox, and OpenAI's Codex sandbox, and NVIDIA's own [[concepts/nvidia-rtx-ai-garage]]. Its distinctive combination is: **kernel syscall-level enforcement + formal verification of policy diffs + egress credential injection so agents never hold raw secrets**. The formal-verification-of-policy angle is unusual — it borrows the formal-methods correctness idea (cf. [[concepts/formal-verification-llm-agents]]) and applies it not to the *code* the agent runs but to the *policy change* that grants the agent access. It is a direct peer to open agent runtimes such as [[concepts/omnara]] but with a stronger isolation/security core.

## See also
- [[concepts/agent-sandbox-patterns]] — the design space
- [[concepts/sandbox]] — isolation primitives
- [[concepts/defenseclaw]] — agent governance/security
- [[entities/e2b]] — competing sandbox runtime
- [[concepts/formal-methods]] — formal verification of policy
- [[entities/nvidia]] — the vendor

## Sources
- [NVIDIA/OpenShell on GitHub](https://github.com/NVIDIA/OpenShell)
- [HN discussion (2026-10-22, ~499 pts)](https://news.ycombinator.com/item?id=50198675)
- Raw: [[raw/articles/2026-10-22_nvidia-openshell_readme-launch]]
