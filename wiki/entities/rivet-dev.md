---
title: "Rivet"
created: 2026-04-30
updated: 2026-04-30
tags:
  - company
  - ai-agents
  - sandbox
  - open-source
aliases: ["rivet-dev", "rivet.gg"]
related: [[concepts/agent-sandboxing]], [[concepts/docker-sandbox-microvm-api]], [[entities/nathan-flurry]], [[concepts/agent-sandboxing-patterns]]
sources:
  - "https://www.rivet.dev"
  - "https://github.com/rivet-dev"
  - "https://www.rivet.dev/blog/2026-02-04-we-reverse-engineered-docker-sandbox-undocumented-microvm-api/"
---

# Rivet (rivet.dev)

## Summary

**Rivet** is an open-source AI agent infrastructure company founded by Nathan Flurry (CTO). They build products for running, managing, and scaling AI agents in production — with a focus on sandboxed code execution and agent orchestration. Notable products: **agentOS** (WebAssembly/V8 isolate-based agent runtime) and **Sandbox Agent SDK** (universal API for coding agents).

*Not to be confused with Ironclad's "Rivet" visual AI programming environment (rivet.ironcladapp.com).*

## Products

### agentOS

- Open-source operating system for AI agents powered by **WebAssembly** and **V8 isolates**
- GitHub: [github.com/rivet-dev/agent-os](https://github.com/rivet-dev/agent-os) (2,541+ stars)
- Actor-based architecture designed for serverless/cloud-native deployment
- Supports Cloudflare Workers, and other edge compute platforms
- [[entities/sankalp-sinha]] is a known contributor

### Sandbox Agent SDK

- Universal API for coding agents — write one integration, swap agents with a config change
- Supports **Claude Code**, **Codex**, **OpenCode**, **Cursor**, **Amp**, and **Pi**
- Lightweight static Rust binary (~15MB), no runtime dependencies
- Runs inside any sandbox environment: E2B, Daytona, Vercel Sandboxes, Docker, Cloudflare Containers
- GitHub: [github.com/rivet-dev/sandbox-agent](https://github.com/rivet-dev/sandbox-agent)
- Normalizes all agent event formats into a universal session schema for storage and replay
- Announced: 2026-01-28

## Technical Philosophy

Rivet's approach to agent infrastructure centers on:

1. **Sandbox-first design:** Agents should run in isolated environments with zero secrets
2. **Universal APIs:** One interface to control multiple agent runtimes
3. **Portable binaries:** Lightweight, no-runtime-dependency deployments
4. **Event-driven architecture:** Actor-based models for scaling agent sessions

## Key People

- **Nathan Flurry** — Co-founder & CTO. Active GitHub contributor on rivet-dev repos. Built the Sandbox Agent SDK and authored research on Docker Sandbox's undocumented MicroVM API.

## Company Info

- **Website:** https://www.rivet.dev
- **GitHub:** https://github.com/rivet-dev
- **Twitter/X:** @rivet_dev
- **Bluesky:** @rivet.dev
- **Discord:** https://discord.gg/aXYfyNxYVn
- **YouTube:** https://www.youtube.com/@rivet-dev
- **LinkedIn:** https://www.linkedin.com/company/72072261/
- **Changelog:** https://www.rivet.dev/changelog/

## Sources

- [Rivet Official Website](https://www.rivet.dev)
- [agentOS Landing Page](https://rivet.dev/agent-os)
- [We Reverse-Engineered Docker Sandbox's Undocumented MicroVM API](https://www.rivet.dev/blog/2026-02-04-we-reverse-engineered-docker-sandbox-undocumented-microvm-api/) — Nathan Flurry, 2026-02-04
- [Rivet Launches the Sandbox Agent SDK to Solve Agent API Fragmentation](https://www.infoq.com/news/2026/02/rivet-agent-sandbox-sdk/) — InfoQ / Sergio De Simone, 2026-02-23
- [github.com/rivet-dev/sandbox-agent](https://github.com/rivet-dev/sandbox-agent)
- [github.com/rivet-dev/agent-os](https://github.com/rivet-dev/agent-os)

## References

- 2026-02-04_rivet-docker-sandbox-microvm-api
