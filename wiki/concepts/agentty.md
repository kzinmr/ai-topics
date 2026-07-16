---
title: "Agentty"
type: concept
created: 2026-07-16
tags:
  - coding-agents
  - tool
  - open-source
  - terminal
  - cpp
sources:
  - raw/articles/2026-07-16_github_agentty-cpp26-coding-agent.md
  - https://github.com/1ay1/agentty
---

# Agentty

**Agentty** is a drop-in alternative to [[entities/claude-code|Claude Code]] written in C++26 — a single 11 MB fully-static binary with sub-millisecond startup, MIT licensed. It occupies a growing niche of native-compiled coding agent clients that reject the Node.js/Python runtime overhead of mainstream tools.

## Overview

While most terminal-based coding agents ([[entities/claude-code|Claude Code]], [[concepts/cline|Cline]], Codex CLI) run on JavaScript or Python runtimes requiring hundreds of megabytes of dependencies and multi-second cold starts, Agentty compiles to a single static binary (~11 MB) that starts in under 1 ms. It drops into any workflow that already uses Claude Code — same tool suite, same `.claude/skills/` format, same conversational patterns — but with drastically lower resource overhead and a sandbox-first security model.

The project was posted to Hacker News in July 2026, earning 37 points and sparking discussion about the C++/Rust trend in agent client engineering.

## Key Features

- **Sub-millisecond startup**: Cold start under 1 ms. No Node.js, no Python, no `npm install`. A single static binary for x86_64 and aarch64 on Linux, plus Intel and Apple Silicon on macOS.
- **Any model backend**: Claude, GPT, Groq, OpenRouter, Ollama, or any OpenAI-compatible endpoint. Switch providers live with `^P` during a session.
- **Sandboxed by default**: Every shell call executes inside `bwrap` (Linux) or `sandbox-exec` (macOS). File tools reject paths outside the workspace. This is architectural, not opt-in — contrasting with [[entities/claude-code|Claude Code]]'s opt-in sandboxing (and subsequent sandbox-escape CVEs).
- **Air-gapped mode**: Run on a machine with no internet connection. A laptop relays bytes over SSH with TLS pinned end-to-end, enabling offline or high-security environments.
- **Agent Skills compatibility**: Reads and executes skills in Claude Code's `.claude/skills/` format — the [[concepts/agent-skills|Agent Skills]] open standard. Also supports `remember`/`forget` memory persistence.
- **ACP protocol**: Speaks the [[concepts/harness-engineering/agent-client-protocol|Agent Client Protocol (ACP)]], making it compatible with the Zed editor and other ACP-supporting surfaces.
- **Full tool suite**: `read`, `write`, `edit`, `bash`, `grep`, `glob`, `git`, `web`, `search_docs`, and `task` tools. Code blocks from the last reply can be listed and run interactively via `^G`.
- **Package availability**: brew (macOS), apt/dnf/zypper/apk (Linux), scoop/winget (Windows), AUR (Arch). Single-command install via `curl | sh`.

## Architecture

Agentty follows a **pure-functional update loop** inspired by the Elm Architecture:

```
(Model, Msg) -> (Model, Cmd)
```

The view layer (`Model -> Element`) is rendered by **maya**, a retained-mode terminal UI library. Process management uses `posix_spawn` + `poll(2)` rather than higher-level subprocess abstractions. All file writes are atomic (`write` + `fsync` + `rename`), ensuring crash safety.

This architecture eliminates the event-loop complexity and GC pauses that characterize Node.js-based agents, while the C++26 standard brings modern ergonomics (`std::expected`, coroutines, ranges) without sacrificing performance.

## Comparison to Claude Code and Grok Build

| Dimension | Agentty | [[entities/claude-code\|Claude Code]] | [[entities/grok-build\|Grok Build]] |
|-----------|---------|-------------|----------|
| **Language** | C++26 | TypeScript (Node.js) | Rust |
| **Binary size** | ~11 MB static | Hundreds of MB (npm) | ~30 MB (estimated) |
| **Startup** | <1 ms | 1–5 seconds | <100 ms |
| **Sandbox** | Default on (bwrap/sandbox-exec) | Opt-in | File-system only |
| **Model backend** | Any (Claude, GPT, Groq, Ollama, OpenRouter) | Anthropic-only (Claude) | xAI-only (Grok) |
| **License** | MIT | Proprietary | Proprietary |
| **ACP support** | Yes | No | No |
| **Agent Skills** | Yes (`.claude/skills/` compatible) | Yes (native) | No |
| **Air-gapped** | Yes | No | No |

Agentty competes most directly with Claude Code on features (same tool suite, same skills format) while competing with [[entities/grok-build|Grok Build]] on the "native binary, low overhead" axis. Unlike Grok Build, which is tied to xAI's Grok models, Agentty is fully model-agnostic — and unlike Claude Code, it is fully open-source (MIT).

## Ecosystem Significance

Agentty is part of a broader **C++/Rust trend in coding agent clients** that pushes back against the JavaScript/Python monoculture dominating the space:

- **Claude Code** (TypeScript, Node.js) — the incumbent, hundreds of MB
- **Codex CLI** (Python) — the largest user base
- **Grok Build** (Rust) — proprietary, model-locked
- **Agentty** (C++26) — open-source, model-agnostic, smallest footprint

This trend reflects a growing recognition that coding agents are infrastructure software — they should be small, fast, sandboxed, and auditable. A static 11 MB binary is trivially distributable, verifiable (single hash), and runs anywhere from CI runners to air-gapped servers. The [[concepts/coding-agents/coding-agents|coding agent landscape]] is diversifying beyond "just pick an editor plugin" into a rich ecosystem of CLI-native, language-diverse clients.

## Open Questions

- **Ecosystem depth**: Can a solo C++ project maintain parity with Claude Code's rapid feature velocity (backed by Anthropic's engineering team)?
- **Model quality vs. client quality**: Agentty's value proposition is the client, not the model. Does sub-ms startup matter if the underlying LLM takes seconds to respond?
- **Adoption path**: Claude Code users must trust a third-party reimplementation. How does Agentty build that trust?
- **Windows support**: scoop/winget packaging is listed but the sandbox model (`bwrap`/`sandbox-exec`) has no Windows equivalent — what is the security story on Windows?

## Related Pages

- [[entities/claude-code]] — The incumbent Claude Code entity
- [[entities/grok-build]] — xAI's Rust-based terminal coding agent
- [[concepts/coding-agents/coding-agents]] — Broader coding agent landscape
- [[concepts/agent-skills]] — Agent Skills open standard format
- [[concepts/harness-engineering/agent-client-protocol]] — Agent Client Protocol (ACP)
- [[concepts/cline]] — Open-source, model-agnostic autonomous coding agent
