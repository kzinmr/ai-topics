---
title: "Dax Raad"
created: 2026-04-10
updated: 2026-04-10
tags: [person, developer-tools, ai-coding-agents, open-source, serverless, aws, typescript]
aliases: ["@thdxr", "thdxr"]
source: x-account
---

# Dax Raad (@thdxr)

| | |
|---|---|
| **X/Twitter** | [@thdxr](https://x.com/thdxr) |
| **Blog** | [thdxr.com](https://thdxr.com/) |
| **GitHub** | [github.com/thdxr](https://github.com/thdxr) |
| **Role** | Co-founder & Core Maintainer at Anomaly Innovations (SST, OpenCode) |
| **Location** | NYC |
| **Known for** | SST (Serverless Stack), OpenCode AI coding agent, TUI-first developer tools |

## Overview

**Dax Raad** is a co-founder and core maintainer at **Anomaly Innovations**, the company behind **SST** (Serverless Stack) and **OpenCode**, an open-source AI coding agent for the terminal. With over a decade of software engineering experience, Dax has held leadership roles at Boulevard (Director of Engineering) and Ride Health (Head of Engineering), and founded projects including Bumi and Ironbay. His career spans full-stack development, CSS-in-JS (co-creator of **Stitches**), and cloud infrastructure.

Dax joined SST as an early user in 2021 before becoming a co-founder and core maintainer. He has been vocal about **pragmatic developer experience** — favoring tools that solve real problems over architectural purity. His perspective on AWS ("competitors have a hard time catching up because of AWS' head start") shapes SST's provider-first philosophy.

## Key Projects

### OpenCode (2025–present)
- **Open-source AI coding agent** for the terminal, built by Anomaly Innovations
- Reached **650,000 monthly active users** and **50,000+ GitHub stars** within five months of launch
- TUI-first (terminal user interface) developer experience — designed for keyboard-driven workflows
- Supports **multi-agent parallel sessions** — developers can run multiple coding agents concurrently on different tasks
- Built on the same ethos as Claude Code and Codex CLI but with a terminal-native, open-source approach
- Integrates with **Bumi** (a notes/documentation tool also by Dax)

### SST / Serverless Stack (2021–present)
- Full-stack serverless framework built on top of **AWS CDK**
- Over **140 npm packages** published under the `@serverless-stack` namespace
- Provides `sst` CLI, `create-sst`, Lambda utilities, and adapters for Next.js, Astro, Solid
- Dax was instrumental in SST's community-building approach — prioritizing developer needs over maintainer convenience
- Featured on the **Real-World Serverless podcast** (#75) discussing open-source community building around SST

### Stitches (2021)
- CSS-in-JS library with near-zero runtime, SSR support, and multi-variant design
- Co-created with the intention of providing a better developer experience for styling React components
- 3k+ GitHub stars; influenced the broader CSS-in-JS ecosystem
- Later evolved into **Tempest** (type-safe React components with Tailwind utilities)

### Other Projects
- **Bumi** — notes and documentation tool
- **Ironbay/Riptide** — real-time data synchronization framework
- **OpenAPI TypeScript code generator** (`openapi-ts`)
- **environment** — personal Neovim/Lua configuration (147 stars)

## Core Ideas

### TUI-First Developer Experience
Dax believes that terminal-based interfaces remain the most efficient way for experienced developers to interact with tools. OpenCode's design philosophy centers on **keyboard-driven workflows** rather than GUI-heavy experiences, contrasting with IDE-centric coding agents like Cursor.

### Open Source as Community Infrastructure
In his Real-World Serverless interview, Dax emphasized that SST's success came from putting **user needs ahead of maintainer convenience** — a deliberate inversion of typical open-source project governance. This philosophy carries into OpenCode, which ships as fully open-source rather than using open-core or BSL licensing.

### Pragmatic AWS Architecture
Dax takes a realistic view of cloud providers: AWS's first-mover advantage and ecosystem lock-in make it the pragmatic default for most teams, despite competition. SST's design reflects this — it embraces AWS CDK rather than abstracting it away.

### AI Coding Agent Honesty
In a March 2026 interview with Codacy, Dax offered a contrarian take on AI coding productivity: *"You start to think if I do better on these benchmarks, I'll get more users. But people can't tell. They literally cannot tell."* He argued that benchmark performance doesn't correlate with user-perceived value, and that the real test is whether agents can handle complex, multi-file engineering tasks end-to-end.

### Multi-Agent Parallelism
OpenCode's architecture supports running **multiple agent sessions in parallel**, each handling different aspects of a codebase. This reflects a broader industry shift from single-agent assistants to orchestrated multi-agent workflows.

## X/Twitter Activity

Dax is active on X/Twitter where he shares:
- OpenCode development updates and design decisions
- SST release notes and community discussions
- Commentary on AI coding agent benchmarks and real-world effectiveness
- AWS/CDK architecture patterns
- Developer tool philosophy (TUI vs GUI, open source licensing)

His GitHub profile shows recent contributions to `anomalyco/opencode`, `oven-sh/bun`, and `nexusrootlab/incident`.

## Related

- [[andrej-karpathy]] — Shared interest in agentic engineering and practical AI workflows
- [[agentic-engineering]] — Multi-agent parallel coding paradigm
- [[simon-willison]] — Open-source tooling philosophy
- [[entities/sst]] — Serverless Stack framework
- [[entities/opencode]] — OpenCode AI coding agent
- [[coding-agents]] — AI-powered software development tools

## Sources

- [Real-World Serverless Podcast #75](https://dev.to/realworldserverless/75-building-open-source-community-around-sst-with-dax-raad) — Building open-source community around SST
- [Codacy Blog](https://blog.codacy.com/the-creator-of-opencode-thinks-youre-fooling-yourself-about-ai-productivity) — "You're Fooling Yourself About AI Productivity"
- [Zread: About Contributors](https://zread.ai/anomalyco/sst/8-about-contributors) — Anomaly Innovations team profiles
- [GitHub: thdxr](https://github.com/thdxr) — 43 public repos, 4,100+ followers
- [npm: @thdxr](https://www.npmjs.com/~thdxr) — 140 published packages
- [OpenCode GitHub](https://github.com/anomalyco/opencode) — 141k stars
- [The Org](https://theorg.com/org/serverless-stack/org-chart/dax-raad) — Professional background
