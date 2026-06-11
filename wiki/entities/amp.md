---
title: Amp
type: entity
created: 2026-05-09
updated: 2026-05-09
tags:
  - entity
  - product
  - developer-tooling
  - coding-agents
  - harness-engineering
  - sourcegraph
aliases:
  - ampcode
  - Amp CLI
  - Amp Neo
related:
  - "[[entities/thorsten-ball]]"
  - "[[entities/sourcegraph]]"
  - "[[concepts/harness-commoditization]]"
  - "[[concepts/coding-agents/amp-neo]]"
  - "[[concepts/coding-agents/minimal-coding-agent]]"
sources:
  - raw/articles/2026-02-19_ampcode-coding-agent-is-dead.md
  - raw/articles/2026-05-06_ampcode-neo-rebuilt.md
  - raw/articles/2025-04-15_ampcode-how-to-build-a-code-editing-agent.md
---

# Amp

Amp is a coding agent CLI tool developed at [[entities/sourcegraph]] by [[entities/thorsten-ball]] and team. It represents a deliberately opinionated and continuously evolving approach to AI-assisted software development — one that aggressively moves with the frontier of model capability, shedding features and assumptions as models advance.

Amp's philosophy: **the agent is not a fixed product but an arrow pointing at the frontier.** When models change, Amp changes — even if that means self-destructing its own extensions.

## Key Facts

- **Website**: [ampcode.com](https://ampcode.com)
- **Creator**: [[entities/thorsten-ball]] at [[entities/sourcegraph]]
- **Type**: CLI-first coding agent (previously had VS Code / Cursor extensions)
- **Pricing**: Freemium / subscription-based (historically offered token-heavy usage at low price)
- **Key Philosophy**: "Everything is changing" — frontier-chasing, not feature-stacking

## Product Evolution

### Original Amp (2024–Feb 2026)
- VS Code and Cursor editor extensions
- CLI available as alternative interface
- Manual context management via Handoff
- Permission-based tool execution (opt-in dangerous operations)

### Amp Neo (May 2026)
In February 2026, Amp announced "The Coding Agent Is Dead" — arguing that frontier models had become so capable that the agent harness itself was no longer the differentiator. This triggered a complete rebuild:

- **Editor extensions killed** (self-destructed March 5, 2026)
- **CLI rebuilt from scratch** (codename: Neo) — remote-controllable, compaction-first, plugin-powered
- **Auto-compaction** replaces manual Handoff (runs at 90% context fill)
- **Plugin API** — TypeScript plugins for tools, commands, events, UI, AI classification
- **Queuing & Steering** — non-disruptive message queuing with fast-track capability
- **Permissions moved to Plugin API** — default is allow-all, custom policies via plugins
- **79% less CPU, 70% less memory** compared to old CLI (5000-message thread benchmark)

## Architecture

| Aspect | Old Amp | Neo (May 2026) |
|--------|---------|-----------------|
| Interface | Editor + CLI | CLI-only |
| Context Management | Manual Handoff | Auto-compaction at 90% |
| Permissions | Built-in opt-in | Plugin-based (allow-all default) |
| Extensibility | Internal | Public Plugin API |
| Remote Access | No | Remote control from amcode.com |
| Message Flow | Interrupt-on-send | Queue with steering |

## Key Writings

- **"How to Build a Code-Editing Agent"** (April 2025) — Articulated the [[concepts/coding-agents/minimal-coding-agent]] pattern: ~400 lines of Go, three tools, heartbeat loop
- **"The Coding Agent Is Dead"** (February 2026) — Argued that [[concepts/harness-commoditization|model capability has commoditized agent harnesses]]; announced editor extension shutdown
- **"Amp, Rebuilt"** (May 2026) — Neo launch: remote control, auto-compaction, Plugin API, performance overhaul
- **"Software After Software"** (May 2026) — [[concepts/software-after-software|Amp Labs manifesto]]: 12 theses on how AI transforms the software industry. Code is no longer scarce; software shifts to agent-facing; value moves to data/permissions/trust; winners reorganize around models; institutions need frontier teams.

## Related Tools

Amp competes in the coding agent space alongside [[entities/claude-code|Claude Code]], Cursor, OpenCode, and other CLI agents. Compared to Claude Code's session-based approach, Amp emphasizes continuous evolution and deliberately minimal scaffolding — keeping the harness thin so it doesn't become a bottleneck.
