---
title: Warp Terminal
created: 2026-05-01
updated: 2026-05-01
type: entity
tags: [product, tool, coding-agents, open-source, platform]
sources:
  - https://www.warp.dev/blog/warp-is-now-open-source
  - https://open.substack.com/pub/bensbites/p/building-gets-easier
---

# Warp Terminal

**Warp** is an AI-native terminal and **Agentic Development Environment (ADE)** used by nearly a million developers. Built in Rust, it combines a modern terminal UX with integrated AI agents. In April 2026, Warp open-sourced its client under AGPLv3 with OpenAI as the founding sponsor.

## Products

### Warp Terminal

The core terminal client with:
- **Terminal and Agent modes**: Switch between clean command-line and dedicated agent conversation view
- **Modern UX**: Block-based navigation, multi-line editing, syntax highlighting, rich completions
- **Code editor**: File tree, LSP support, interactive code review
- **Third-party CLI agents**: Run Claude Code, Codex, OpenCode with Warp's agent toolbelt

### Oz

**Oz** is Warp's cloud agent orchestration platform, powering the agent-first contribution model for the open-source repository. It provides:
- Skills and verification loops baked in for Warp development
- Multi-agent orchestration for code review, testing, and deployment
- Rules and context management for consistent agent behavior

## Open Source (April 2026)

On April 28, 2026, Warp open-sourced its client at [github.com/warpdotdev/warp](https://github.com/warpdotdev/warp):

- **License**: AGPLv3 for core, MIT for UI framework (warpui_core, warpui crates)
- **Founding sponsor**: OpenAI
- **Agent workflows**: Powered by GPT models (GPT-5.5)
- **Contribution model**: Agent-first — agents handle implementation; humans focus on speccing, direction, and verification

> "Open source has long been central to how developers learn, build, and push the field forward. We're excited to support experiments that explore how AI can help maintainers and contributors collaborate more effectively at scale." — Thibault Sottiaux, Engineering Lead, OpenAI

## Agent-First Contribution Model

Warp's open-source process inverts traditional contribution:
- GitHub issues are the source of truth for feature tracking
- Oz agents handle implementation (coding, planning, testing)
- Human contributors focus on ideas, direction, and verifying agent output
- Public roadmap and technical discussions happen in the open

This model exemplifies the [[concepts/agentic-engineering]] thesis: humans provide taste and direction, agents handle implementation.

## Strategic Context

Warp's open-sourcing is framed as "how software will be built in the future" — humans managing agents at scale to build production-grade software. The founding sponsorship by OpenAI signals alignment with GPT models as the underlying agent runtime.

Warp is competing in the **agentic development environment** space alongside:
- [[entities/cursor-3]] — IDE-native agent platform
- [[entities/openai-codex]] — OpenAI's coding agent platform
- [[entities/claude-code]] — Anthropic's CLI coding agent

## Relationships

- [[entities/openai]] — Founding sponsor; GPT-5.5 powers agent workflows
- [[entities/cursor-3]] — Competitor in agentic development environments
- [[concepts/agentic-engineering]] — Embodies the agent-first workflow pattern
- [[concepts/harness-engineering]] — Oz provides the orchestration harness
- [[entities/ghostty]] — Mitchell Hashimoto's terminal; Ghostty left GitHub as Warp went open-source

## Sources

- [Warp: Warp is now open-source](https://www.warp.dev/blog/warp-is-now-open-source)
- [Warp Documentation](https://docs.warp.dev/)
- [Ben's Bites: Building gets easier (Apr 30, 2026)](https://open.substack.com/pub/bensbites/p/building-gets-easier)
