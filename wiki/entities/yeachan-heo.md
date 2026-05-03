---
title: "Yeachan Heo (Bellman)"
type: entity
created: 2026-05-03
updated: 2026-05-03
tags: [person, developer-tooling, coding-agents, open-source, multi-agent]
aliases: ["Bellman", "bellman_ych", "Yeachan-Heo"]
sources:
  - https://github.com/Yeachan-Heo
  - https://github.com/Yeachan-Heo/oh-my-codex
  - https://github.com/Yeachan-Heo/oh-my-claudecode
---

# Yeachan Heo (Bellman)

Yeachan Heo (@bellman_ych) is a developer and algorithmic trader based in Seoul, South Korea. Known for creating the **OmX ecosystem** — workflow and orchestration layers for AI coding agents. He is a primary collaborator on the **[[claw-code]]** project and serves as a key maintainer of its Rust implementation.

## Key Projects

### oh-my-codex (OmX)
- **GitHub**: https://github.com/Yeachan-Heo/oh-my-codex
- **Stars**: 24K+
- **Language**: TypeScript
- A workflow/plugin layer on top of OpenAI Codex CLI. Provides planning modes, parallel multi-agent execution (`$architect`, `$explore`, `$ralph`, `$security-reviewer`), persistent verification loops, notification routing, and HUDs.

### oh-my-claudecode (OMC)
- **GitHub**: https://github.com/Yeachan-Heo/oh-my-claudecode
- **Stars**: 29.9K+
- **Language**: TypeScript
- Multi-agent orchestration for Claude Code. Same core philosophy as OmX but for the Anthropic ecosystem.

### clawhip
- **GitHub**: https://github.com/Yeachan-Heo/clawhip
- **Language**: Rust
- Event-to-channel notification router that bypasses gateway sessions to avoid context pollution.

### Other Projects
- **My-Jogyo** — One-click scientific research lab for OpenCode with .ipynb and REPL integration
- **Certis** — High-quality backtesting engine (Python)
- **ultraworkers/claw-code** — Primary collaborator on the Claw Code Rust implementation

## Philosophy

Heo's work follows the same "humans set direction, agents execute" paradigm as Sigrid Jin's. The OmX ecosystem is designed to enable multi-agent coding workflows where:
- **$team mode** enables coordinated parallel review and architectural feedback
- **$ralph mode** provides persistent execution, verification, and completion discipline
- The bottleneck is human judgment, not coding speed

## Related
- [[claw-code]] — Rust implementation co-developed with Heo
- [[sigrid-jin]] — Creator of claw-code and collaborator
- [[ultraworkers]] — GitHub organization
