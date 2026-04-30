---
title: AgentCraft
type: entity
created: 2026-04-30
updated: 2026-04-30
tags:
  - devtools
  - ai-agent
  - orchestrator
  - open-source
aliases:
  - getagentcraft
  - agent-craft
  - @idosal/agentcraft
sources:
  - raw/articles/2026-04-25-agentcraft-rts-agent-orchestration.md
  - https://www.getagentcraft.com/
  - https://www.getagentcraft.com/docs
---

# AgentCraft

**AgentCraft** is an open-source AI agent orchestrator with an RTS (Real-Time Strategy) game interface. Built by [[entities/ido-salomon|Ido Salomon]] (@idosal1), it provides a single-pane-of-glass command center where each AI agent appears as a hero unit on a 3D map, complete with missions, fog of war, skill scrolls, and achievements.

AgentCraft works by installing lightweight hooks into supported agent CLIs (Claude Code, OpenCode, Cursor). These hooks report session events to the AgentCraft server, which renders everything in a browser-based game UI on **port 2468**.

## Getting Started

```bash
npx @idosal/agentcraft
```

This runs the guided setup: detects installed agent CLIs, installs hooks, starts the server, and opens the browser UI.

## Key Features

### Single Pane of Glass
All agents in one place. See agents working, launch new agents, and manage their lifecycle from a unified RTS-style map view.

### Total Control
RTS-inspired interface designed for developers managing 20+ agents simultaneously. Uses the same muscle memory as real-time strategy games for quick reaction to events.

### Multi-Agent Heroes
Each AI agent appears as a hero on the map with real-time status tracking. Supports agent teams with grouped parties (Claude Code team configurations).

### Game-like UI
A full RTS-style command center with:
- **Fog of War** — Toggle with **V** to visualize which areas have active heroes
- **Skill Scrolls** — Collectible scrolls on the map that install real agent skills from skills.sh
- **Achievements** — Tiered unlock system with shareable trophy cards
- **Race Skins** — Choose between Orc, Human, Elf, and Undead factions with unique buildings, heroes, terrain, and portraits
- **Ambient Music** — Soundtrack toggle
- **Mission Tracking** — Completed missions persist across restarts with AI-generated summaries

### Command from Anywhere
Secure remote tunnels, installable mobile PWA, push notifications with quick-reply, and Telegram/Discord channels. Approve plans, grant permissions, and message agents from phone or chat apps.

### Isolated Agent Containers
Run agents inside Docker or Apple Containers with full network isolation. Multiple agents can run dev servers on the same port with separate browser sessions.

### Alliance Hall
Collaborative multiplayer for developers. Create shared rooms, see remote agents from other machines on your map, and coordinate through the Notice Board.

### Additional Features
- **Scheduled Tasks** — Create recurring agent tasks with cron-like intervals
- **Integrated Terminal** — Full PTY terminal in the bottom HUD with multi-tab support
- **File Explorer** — Browse project files in the side panel with search and IDE integration
- **Git Worktrees** — Spawn heroes in different worktrees directly from the UI
- **Git Management** — Built-in stash and branch management
- **Voice Input** — Speech-to-text in the composer with auto-send on silence

## Supported Agents

| Agent | Status | Description |
|-------|--------|-------------|
| **Claude Code** | Primary | Full integration with Anthropic's CLI agent |
| **OpenCode** | Supported | 75+ models from multiple providers |
| **Cursor** | Supported | Cursor's agent mode via CLI |
| **OpenClaw** | Experimental | Experimental agent support |

## Architecture

AgentCraft follows a client-server architecture:

1. **Hooks Layer** — Lightweight hooks installed into supported agent CLIs that capture session events (commands, outputs, lifecycle changes)
2. **Server** — Node.js server running on port 2468 that collects and processes hook events, manages agent state, and serves the browser UI
3. **Browser UI** — Three.js/WebGL-based RTS game interface rendered in the browser, displaying agents as hero units on a 3D terrain map

```
┌─────────────────────────────────────────────────────┐
│                  Browser UI (Port 2468)              │
│           RTS Game Interface (Three.js/WebGL)        │
└────────────────────────┬────────────────────────────┘
                         │ WebSocket / REST
┌────────────────────────▼────────────────────────────┐
│              AgentCraft Server (Node.js)              │
│         Event Processing · State Management · UI      │
└──┬──────────────┬───────────────┬───────────────────┘
   │              │               │
   ▼              ▼               ▼
┌──────┐    ┌──────────┐    ┌────────┐
│Claude│    │ OpenCode │    │ Cursor │
│ Code │    │          │    │        │
└──────┘    └──────────┘    └────────┘
```

## Related Tools

- [[entities/claude-code]] — Primary supported agent (Anthropic's CLI coding agent)
- [[entities/opencode]] — Open-source AI coding agent framework (75+ models)
- [[entities/cursor-3]] — Agent-driven IDE with agent mode support
- [[entities/openclaw]] — Open-source always-on AI assistant framework (experimental support)

## Creator

Built by **Ido Salomon** (@idosal1), AI Lead at Monday.com's CEO Office. Ido is also the creator of [[entities/mcp-ui]] (UI over MCP protocol), co-creator of GitMCP (remote MCP server for GitHub), and co-creator of the MCP Apps workgroup in the MCP Steering Committee. Previously led enterprise browser architecture and end-user AI at Palo Alto Networks.

## Community

- **Website**: https://www.getagentcraft.com/
- **Docs**: https://www.getagentcraft.com/docs
- **App**: https://app.agentcraft.gg
- **Discord**: https://discord.gg/nEaZAH7C7F
- **X/Twitter**: https://x.com/idosal1

## Sources

- AgentCraft website (https://www.getagentcraft.com/) — Scraped 2026-04-25
- AgentCraft Documentation (https://www.getagentcraft.com/docs)
- Google Cloud Next 2026 — Ido Salomon speaker profile
- X/Twitter — @idosal1 pinned post (Feb 11, 2026): "AgentCraft v1 is live"
- Pinter Computing — Installing AgentCraft guide (Feb 19, 2026)
- ClawHub — AgentCraft package listing (@idosal/agentcraft v1.0.0)
