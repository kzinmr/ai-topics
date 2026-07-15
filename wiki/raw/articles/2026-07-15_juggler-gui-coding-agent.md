---
title: "Juggler — Open-Source GUI Coding Agent by JUCE Creator"
created: 2026-07-15
updated: 2026-07-15
type: article
source: "https://github.com/juggler-ai/juggler"
status: complete
sources:
  - "https://github.com/juggler-ai/juggler"
  - "https://juggler.studio"
  - "https://news.ycombinator.com/item?id=48883305"
  - "https://github.com/juggler-ai/juggler/blob/develop/AGENTS.md"
  - "https://github.com/juggler-ai/juggler/blob/develop/docs/extension_guide.md"
---

# Juggler — Open-Source GUI Coding Agent

## Summary

Juggler is an open-source GUI coding agent — a native desktop application providing a visual workbench for interacting with LLM-powered coding agents. Created by Julian Storer (julesrms), creator of JUCE (C++ framework for audio), Tracktion (DAW), and Cmajor (DSP language). Posted as Show HN on July 12, 2026, reaching 247 points — #1 story that day.

## Key Features

1. **Miller-column UI (Finder-style)**: Root on left, selected items expanding into properties and children to the right. Tool calls, properties, and nested sub-threads visually laid out.
2. **Branching conversation tree**: Session is a Yjs CRDT document. Any point can branch into a sub-thread. Navigate, inspect, edit, duplicate, delete, undo/redo, re-open, or branch.
3. **Plugin system**: Context items, LLM loop strategies, slash commands, and UIs are all JavaScript plugins via the SDK. Built-in tools are sample plugins — fork or replace them.
4. **Multi-client architecture**: Server (headless Go) + desktop app means multiple clients (native app, browser tabs) can view/control the same session simultaneously.
5. **All context visible**: Tool calls, approvals, thread structure, item properties, raw context JSON — everything exposed.

## Architecture

**Two binaries:**
- `cmd/juggler` (server): Headless Go process. HTTP/WebSocket, session store, hidden engine WebView for backend JS execution.
- `cmd/juggler-app` (desktop): One process owning many visible windows, each a viewer pointed at a server.

**Tech stack:**
- Backend: Go (Wails fork — NO Electron)
- Frontend: Plain JavaScript with JSDoc typing (no build step)
- Session: Yjs (CRDT)
- Desktop: Wails (Go → WebView)
- Engine: Hidden WebView running backend JS

## Supported Providers

BYOK (Bring Your Own Key): Claude Code, OpenAI, Gemini, Ollama, OpenRouter, Z.AI, Deepseek. Easy to add more via plugins.

## License

Dual: AGPL-3.0-or-later (core app), Apache-2.0 (extension SDK + bundled extensions). Extensions can be closed-source.

## Comparison

Compared to Cursor/Codex/Windsurf: Native GUI (Miller columns), editable tree (CRDT) vs linear chat, plugin SDK, multi-client, ~40MB binary, no Electron. Early alpha (v0.3.7). One-man side-project.

## HN Discussion

247 points, 106 comments. Praised for being non-VC-backed FOSS from a well-known developer. Common compliments: UI concept, no Electron, branching threads, plugin system, 40MB size. Criticisms: early alpha with bugs, no ACP support yet, requires WebKitGTK on Linux.
