---
title: Juggler
created: 2026-07-15
updated: 2026-07-15
type: concept
tags: [coding-agents, open-source, juggler, gui, developer-tooling, plugins, extensibility]
sources:
  - raw/articles/2026-07-15_juggler-gui-coding-agent.md
---

# Juggler

**Juggler** is an open-source GUI [[concepts/coding-agents/coding-agents|coding agent]] created by Julian Storer (creator of JUCE, Tracktion, and Cmajor). It provides a native desktop workbench for interacting with LLM-powered coding agents, featuring a Miller-column interface, branching conversation trees via CRDT (Yjs), and a full plugin system.

Posted as Show HN on July 12, 2026, reaching 247 points and becoming #1 on Hacker News.

## Key Features

- **Miller-column UI**: Finder-style column layout where tool calls, properties, and sub-threads are visually laid out for inspection — unlike linear chat transcripts in [[entities/claude-code|Claude Code]] or [[entities/codex|Codex]].
- **Branching conversation tree**: Sessions are Yjs CRDT documents. Any point can branch into sub-threads for exploration and comparison.
- **Plugin SDK**: Context items, LLM loop strategies, slash commands, and their UIs are all JavaScript plugins. Even built-in tools (`read`, `write`, `bash`) are sample plugins.
- **Multi-client**: Headless Go server + desktop app means multiple clients (native app, browser tabs) can view and control the same session simultaneously.
- **No Electron**: ~40MB Go binary using Wails (Go → WebView).

## Architecture

**Two binaries:** `cmd/juggler` (headless Go server with HTTP/WebSocket and hidden WebView for JS execution) and `cmd/juggler-app` (desktop viewer). The server can run on a dev box while the UI connects from anywhere.

**Tech stack:** Go backend, plain JavaScript frontend (no TypeScript, no build step), Yjs CRDT for session storage, Wails for desktop windowing.

## Supported Providers

BYOK (Bring Your Own Key): [[entities/anthropic|Claude]] API, [[entities/openai|OpenAI]], [[entities/google|Gemini]], Ollama, OpenRouter, [[entities/deepseek|Deepseek]], and more via plugins.

## License

Dual: **AGPL-3.0-or-later** (core app), **Apache-2.0** (extension SDK and bundled extensions). Extensions can be closed-source.

## Related Projects

- [[entities/claude-code|Claude Code]] — Terminal-based coding agent from Anthropic
- [[entities/codex|Codex]] — Terminal-based coding agent from OpenAI
- [[entities/cursor-ai|Cursor]] — VS Code fork with AI coding features
- [[entities/opencode|OpenCode]] — Open-source terminal coding agent
- [[concepts/cline|Cline]] — VS Code extension AI coding agent

## External Links
- [GitHub Repository](https://github.com/juggler-ai/juggler)
- [Website](https://juggler.studio)
- [HN Discussion (247 points)](https://news.ycombinator.com/item?id=48883305)
