---
title: Keep
type: entity
created: 2026-11-17
updated: 2026-11-17
tags: [tool, agent-native, knowledge-management, mcp, developer-tooling]
aliases:
  - keep.md
description: "Capture tool by Ian Nuttall that saves pages, posts, files, notes, images, video, PDFs and audio as clean Markdown an AI agent can search, read and update; iOS app plus web app and MCP setup for Claude Code, Codex, Cursor, Hermes and others."
sources:
  - "https://keep.md"
  - "https://x.com/iannuttall/status/2119721859302535604"
---

# Keep

**Keep** ([keep.md](https://keep.md)) is **Ian Nuttall**'s ([@iannuttall](https://x.com/iannuttall))
capture tool: "Save everything you read, write, watch, and hear as clean Markdown your AI
agents can search, read, and update." Its premise is that Markdown is the interchange
format agents actually consume well, so the read-later layer should be agent-readable by
default rather than a human-only bookmark pile.

## What it does

- **Capture surface:** pages, posts, files, notes — plus images, videos, PDFs and audio —
  normalized to plain Markdown. Framing: "Everything you save, in one place you own.
  Organise them your way and take them anywhere."
- **Agent integration:** the site ships a copyable **setup prompt** wired for **Claude,
  Claude Code, ChatGPT, Codex, Cursor, Hermes, OpenClaw and Grok Bot**, covering both CLI
  and MCP hookup. The prompt text itself is notably strict about verification: "Stop and
  explain the exact failing step if any command, permission, or authentication check
  fails. Do not skip a failed check or claim the setup is complete without verifying both
  CLI and MCP."
- **Platforms:** web app plus a free **iPhone app** (App Store), distributed with QR-code
  and text-yourself handoff.

## Author's own use case

Nuttall, on getting the iOS app approved (Nov 9, 2026, after roughly two months in review):

> "it took about 2 months to get approval but keep.md finally has an iOS app 😅 I use this
> to save anything I think I'll need my agents to use later as Markdown. Examples: -
> SEO/AEO/ASO tips - design inspiration - competitor research - product ideas - viral tweets"
> — [tweet](https://x.com/iannuttall/status/2119721859302535604)

That list is the product thesis in miniature: Keep is positioned as the **human-curated
context store that gets handed to an agent later**, not as a note-taking app for reading
back yourself.

## Positioning / related pattern

- Same "agent-native" thesis as Nuttall's [[entities/seo-skill]] — expose a real data or
  content surface as a tool the coding agent calls, instead of a dashboard a human reads.
- Overlaps with the "save for agents" cluster (read-later tools repositioned as agent
  context stores); contrast with note tools that ship Markdown but no agent setup path.
- The multi-client setup-prompt distribution (one prompt, per-agent variants, MCP + CLI)
  is the same convention several agent-tool vendors have converged on.

## Notes / gaps

- Pricing tiers, export format guarantees, and whether the store is truly user-owned
  (local files vs hosted) were not verified this run — "one place you own" is a first-party
  claim.
- Team/collaboration features and the MCP server's data-access scope are unverified.
- Vendor: Ian Nuttall / Practical Programmatic. See [[entities/ian-nuttall]].

## See Also

- [[entities/ian-nuttall]] — author
- [[entities/seo-skill]] — companion agent-native tool
- [[concepts/model-context-protocol-mcp]] — the integration surface Keep ships
