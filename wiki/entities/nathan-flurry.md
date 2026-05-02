---
title: "Nathan Flurry"
created: 2026-04-30
updated: 2026-04-30
tags:
  - person
  - engineer
  - ai-agents
aliases: ["nathanflurry"]
related: [[entities/rivet-dev]], [[concepts/docker-sandbox-microvm-api]], [[concepts/agent-sandboxing]]
sources:
  - "https://github.com/NathanFlurry"
  - "https://www.rivet.dev/blog/2026-02-04-we-reverse-engineered-docker-sandbox-undocumented-microvm-api/"
---

# Nathan Flurry

## Summary

**Nathan Flurry** (@NathanFlurry) is a software engineer, co-founder, and CTO of **Rivet** (rivet.dev), an open-source AI agent infrastructure company. He specializes in sandboxed code execution, agent orchestration, and building universal APIs for coding agent runtimes.

## Background

- **Role:** Co-founder & CTO at Rivet
- **Focus:** Agent infrastructure, sandboxing, distributed systems
- **GitHub:** [NathanFlurry](https://github.com/NathanFlurry)

## Key Contributions

### Sandbox Agent SDK (2026)

- Built a universal API for coding agents that normalizes interfaces across Claude Code, Codex, OpenCode, Cursor, Amp, and Pi
- Lightweight static Rust binary (~15MB) with no runtime dependencies
- Runs inside any sandbox environment (E2B, Daytona, Vercel Sandboxes, Docker, Cloudflare Containers)
- Featured on InfoQ (February 2026)
- Addressed three core challenges: API fragmentation, transient state, and deployment variance across providers

### Docker Sandbox MicroVM Reverse-Engineering (2026-02-04)

- Reverse-engineered Docker's undocumented `sandboxd` API that powers Docker Sandboxes
- Demonstrated how to create and manage per-VM Docker daemon instances via Unix sockets
- Showed networking (filtering proxy with MITM HTTPS) and volume sync mechanisms
- Enabled developers to run arbitrary containerized workloads in kernel-isolated MicroVMs
- Requires Docker Desktop 4.58+ on macOS/Windows; Linux unsupported

### agentOS

- Core contributor to Rivet's agentOS — a WebAssembly/V8 isolate-based runtime for AI agents
- Active on GitHub issues and discussions for the project

## Technical Philosophy

Flurry's work emphasizes:
1. **Sandbox-first security** — Agents should run with zero secrets and disposable state
2. **Universal abstraction layers** — One API to control multiple agent runtimes
3. **Portability** — Static binaries, no runtime dependencies, deploy anywhere
4. **Developer experience** — Visual tooling (Rivet's original product) and SDK-first approach

## Sources

- [We Reverse-Engineered Docker Sandbox's Undocumented MicroVM API](https://www.rivet.dev/blog/2026-02-04-we-reverse-engineered-docker-sandbox-undocumented-microvm-api/) — 2026-02-04
- [Rivet Launches the Sandbox Agent SDK to Solve Agent API Fragmentation](https://www.infoq.com/news/2026/02/rivet-agent-sandbox-sdk/) — InfoQ, 2026-02-23
- [github.com/rivet-dev/sandbox-agent](https://github.com/rivet-dev/sandbox-agent)
- [github.com/rivet-dev/agent-os](https://github.com/rivet-dev/agent-os)
- [github.com/NathanFlurry](https://github.com/NathanFlurry)
