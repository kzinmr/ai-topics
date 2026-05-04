---
title: Zed
type: entity
created: 2026-05-04
updated: 2026-05-04
tags:
  - product
  - platform
  - developer-tooling
  - editor
  - rust
  - coding-agents
  - acp
aliases:
  - Zed editor
  - Zed Industries
  - zed-code
sources:
  - raw/articles/2026-05-04_thorsten-ball-joy-and-curiosity-84.md
---

# Zed

Zed is a high-performance, open-source code editor built in **Rust** by **Zed Industries** — founded by Nathan Sobo, Antonio Scandurra, and Max Brunsfeld (the team behind **Atom**, **Electron**, and **Tree-sitter** at GitHub). It reached version 1.0 on April 29, 2026.

## Key Facts

- **Language**: Written in Rust with a custom GPU-accelerated UI framework called GPUI (Apache 2.0)
- **Platforms**: macOS, Linux, Windows
- **License**: Open source (Apache 2.0)
- **Version 1.0**: April 29, 2026 — described as "a tipping point where most developers can feel quickly at home"
- **Extensions**: ~1,000 extensions (vs. 100,000+ in VS Code marketplace)
- **Team**: Nathan Sobo (CEO), Antonio Scandurra, Max Brunsfeld — all former Atom/GitHub engineers

## AI Features

Zed was designed as an **AI-native editor** from the ground up:

- **Parallel agent orchestration**: Run multiple AI agents simultaneously to edit files, navigate code, and run tools at native speed
- **Zeta LLM**: Zed's own open-source model for AI edit predictions at the keystroke level
- **External model support**: Integrates with Claude, GPT, DeepSeek, and custom providers
- **ACP (Agent Client Protocol)**: Co-developed with Google and JetBrains to standardize agent-editor communication
- **Zed AI**: Partnership with Anthropic (announced August 2024) for deep Claude integration
- **"Disable all AI features" setting**: Includes a toggle for developers who want a pure code editor experience

## Technical Architecture

- **GPUI**: Custom GPU-accelerated UI framework (Rust, runs on GPU via custom renderer)
- **Tree-sitter**: Used for syntax trees and incremental parsing (by team co-creator Max Brunsfeld)
- **DeltaDB** (in development): A CRDT-based synchronization engine for character-level change tracking and real-time collaboration among humans and agents
- **Built-in LSPs**: C, C++, CSS, JavaScript, TypeScript, Markdown, Python

## Version 1.0 Highlights

- Bookmarks for quick navigation
- "View commit" command palette action
- Side-by-side diffs
- GIF animation support in Markdown preview
- DeepSeek-V4-Pro and DeepSeek-V4-Flash model support
- SSH remoting
- Debugging support

## Business

Zed is freemium — free for individual use with planned **Zed for Business** tier (centralized billing, role-based access, team management).

## Related

- [[entities/mitchell-hashimoto]] — Also discussed GitHub/AI stability concerns in the same period
- [[entities/thorsten-ball]] — Former Zed employee, featured Zed 1.0 in newsletter
- [[entities/claude-code]] — Coding agent ecosystem
- [[entities/cursor-3]] — Competing AI-native editor
- [[concepts/local-first-software]] — The Forge movement toward local-first development
