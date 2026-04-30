---
title: Tim Sh (timsh.org)
type: entity
created: 2026-04-29
updated: 2026-04-30
tags:
  - person
  - blogger
  - agentic-engineering
  - developer-tooling
sources:
  - "raw/articles/timsh.org--how-i-created-an-ethereum-proof-of-stake-demo-entirely-with---3d132b24.md"
  - "raw/articles/timsh.org--claude-inside-docker--6842418e.md"
---

# Tim Sh (timsh.org)

| | |
|---|---|
| **Blog** | [timsh.org](https://timsh.org) |
| **GitHub** | [tim-sha256](https://github.com/tim-sha256) |
| **Bluesky** | [@timsh.org](https://bsky.app/profile/timsh.org) |
| **Email** | hello@timsh.org |
| **Identity** | Product manager, startup builder, former CTO, self-hosting / cybersecurity / AI coding practitioner |
| **Active** | 2020s–present |
| **Themes** | AI-assisted development, multi-LLM workflows, Docker isolation, self-hosting, privacy, cybersecurity |

> **Note:** Not to be confused with [[entities/tim-sherratt]] — a different Tim Sherratt who is a historian and GLAM hacker at timsherratt.au.

## Overview

**Tim Sh** is a product manager by day who also built startups and served as a CTO (mostly by night). He writes extensively about **self-hosting, cybersecurity, privacy, and AI-assisted software development**. His blog at timsh.org (hosted on Ghost) covers practical, hands-on experiments with AI coding tools.

Tim Sh represents a significant emerging archetype: the **non-developer practitioner** who uses AI tools to build production-quality applications despite having no formal software engineering background. His workflows and patterns are documented in [[concepts/ai-coding-workflows]].

## Key Contributions

### Multi-LLM Role Separation Pattern

In "How I created an Ethereum Proof of Stake demo entirely with ChatGPT and Cursor" (April 2026), Tim Sh documents a now-canonical workflow pattern:

- **ChatGPT-4o as Project Manager**: Handles architecture, design, requirements, and instruction generation
- **Cursor as Coder**: Executes the implementation based on ChatGPT's instructions
- **Key techniques**: Always commit (100+ commits), localStorage.json for data structure tracking, SVG over external chart libraries, debug with Cursor, design with ChatGPT, template-first approach, single chat context, re-send reference on context degradation

This is documented as a core pattern in [[concepts/ai-coding-workflows#Multi-LLM Role Separation Pattern]].

### Claude Inside Docker

In "Switching to Claude Code + VSCode inside Docker" (April 2026), he demonstrates using **Docker containers as security boundaries** for AI coding agents — isolating the agent from the host filesystem, secrets, and SSH keys. Includes a reference `.devcontainer` template at `github.com/tim-sha256/claude-in-docker`.

This is the basis for the Dev Container pattern documented in [[concepts/ai-coding-workflows#Docker Dev Container Pattern]].

## Working Context

Tim Sh works with a **two-LLM ecosystem**: ChatGPT-4o (for planning, design, debugging bugs) and Cursor (for implementation). He uses Python for backend prototyping and React for frontend applications.

Key tools and practices:
- Docker Dev Containers for AI agent isolation
- Fine-grained GitHub PATs (scoped to single repos) over SSH keys
- Commits every meaningful change (100+ per project)
- Externalizes data structures in `localStorage.json` for cross-LLM reference
- Uses SVG for data visualization (both LLMs can reason about SVG code natively)
- Templates everything — defines layout structure before filling in content

## Projects

- **[claude-in-docker](https://github.com/tim-sha256/claude-in-docker)** — Reference template for running Claude Code inside a VSCode Dev Container with security isolation
- **Ethereum PoS Demo** — Real-time blockchain explorer built with ChatGPT + Cursor (April 2026)

## Related

- [[concepts/ai-coding-workflows]] — Documents the Multi-LLM Role Separation Pattern
- [[concepts/vibe-coding]] — Related high-level pattern
- [[concepts/cognitive-debt]] — Risk pattern that isolation addresses
- [[entities/tim-sherratt]] — Different person, historian and GLAM hacker

## Sources

- [About | timsh.org](https://timsh.org/about/)
- [How I created an Ethereum Proof of Stake demo entirely with ChatGPT and Cursor](https://timsh.org/how-i-created-an-ethereum-proof-of-stake-demo-entirely-with-chatgpt-and-cursor/) — April 2026
- [Switching to Claude Code + VSCode inside Docker](https://timsh.org/claude-inside-docker/) — April 2026

## References

- timsh.org--2m-laundered-the-youtube-crypto-tutorials-huge-scam-investig--d749b749
- timsh.org--everyone-knows-your-location-part-2-try-it-yourself--cfc88813
- timsh.org--github-scam-investigation-thousands-of-mods-and-cracks-steal--e1a40b6a
- timsh.org--i-made-a-chrome-extension-to-help-avoid-playing-cheaters-in---392e26df
- timsh.org--scam-telegram-investigation--d507827d
- timsh.org--tracking-myself-down-through-in-app-ads--205a3798
- timsh.org--why-i-created-ethereum-proof-of-stake-demo--708fbf2f
- timsh.org--why-you-should-self-host--bff25172
