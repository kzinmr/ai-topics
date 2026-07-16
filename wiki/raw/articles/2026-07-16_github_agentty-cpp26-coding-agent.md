---
title: "agentty: AI pair programming in your terminal — C++26, 11MB static binary"
url: "https://github.com/1ay1/agentty"
source: "GitHub (1ay1/agentty)"
author: "1ay1"
date: 2026-07-16
tags: [raw, coding-agents, tools, open-source]
fetched_at: 2026-07-16T12:00:00Z
---

# Agentty — AI pair programming in your terminal

Agentty is a drop-in alternative to Claude Code, written in C++26. One static binary, sub-millisecond startup, any model. MIT licensed.

- **GitHub**: https://github.com/1ay1/agentty
- **HN Discussion**: 37 points, 5 comments (July 2026)
- **Binary size**: ~11 MB fully-static executable (x86_64 + aarch64 on Linux, Intel + Apple Silicon on macOS)

## Features

- **Instant startup**: Cold start under 1ms. No Node, no Python, no npm install.
- **Any model**: Claude, GPT, Groq, OpenRouter, Ollama, or any OpenAI-compatible endpoint. Switch live with `^P`.
- **Sandboxed by default**: Every shell call runs inside bwrap (Linux) / sandbox-exec (macOS). File tools refuse paths outside your workspace.
- **Air-gapped mode**: Run on a box with no internet. Laptop relays bytes over SSH with TLS pinned end-to-end.
- **Full tool suite**: read · write · edit · bash · grep · glob · git · web · search_docs · task
- **Learns your codebase**: Agent Skills + remember/forget memory. Compatible with Claude Code's `.claude/skills/` format.
- **ACP protocol support**: Speaks the Agent Client Protocol — compatible with Zed editor.
- **Run code blocks**: `^G` lists code blocks from the last reply; runs interactively on your real terminal.

## Architecture

Pure-functional update loop: `(Model, Msg) -> (Model, Cmd)`. View is `Model -> Element`, rendered by maya. Process management via `posix_spawn` + `poll(2)`. File writes are atomic (`write` + `fsync` + `rename`).

## Installation

```bash
curl -fsSL https://raw.githubusercontent.com/1ay1/agentty/master/install.sh | sh
```

Package managers: brew (macOS), apt/dnf/zypper/apk (Linux), scoop/winget (Windows), AUR (Arch).

## Providers

```bash
agentty                                    # Claude (default)
agentty --provider openai -m gpt-4o        # GPT
agentty --provider groq -m llama-3.3-70b   # Groq
agentty --provider ollama -m qwen2.5-coder # Local model
agentty --provider openrouter              # Any model via OpenRouter
```
