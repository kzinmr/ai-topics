---
title: "Amp Neo"
type: concept
created: 2026-05-09
updated: 2026-05-09
tags:
  - concept
  - coding-agents
  - agent-harness
  - context-management
  - developer-tooling
  - cli
aliases:
  - neo
  - amp-neo
  - amp-rebuilt
related:
  - "[[entities/amp]]"
  - "[[concepts/harness-commoditization]]"
  - "[[concepts/agent-harness]]"
  - "[[entities/thorsten-ball]]"
sources:
  - raw/articles/2026-05-06_ampcode-neo-rebuilt.md
---

# Amp Neo

**Amp Neo** (codename "Neo") is the May 2026 ground-up rebuild of the [[entities/amp|Amp]] coding agent CLI. It embodies the [[concepts/harness-commoditization|harness commoditization]] philosophy — a deliberately thin agent layer designed for models that no longer need handholding.

## Architecture Principles

1. **Remote-controllable** — Agent threads can be monitored and controlled from amcode.com web UI
2. **Compaction-first** — Automatic context compaction at 90% fill, replacing manual Handoff
3. **Plugin-powered** — Extensibility via TypeScript plugins in `.amp/plugins/`
4. **Allow-all default** — Permissions moved to Plugin API; destructive operations are inherently hard to statically analyze
5. **Queue-native** — Messages queue by default; steering for fast-track

## Key Features

### Auto-Compaction
When the context window reaches 90% capacity, Amp automatically summarizes the current context, starts a fresh window with that summary, and continues. No user intervention needed. This replaces the old Handoff system entirely.

### Plugin API
```typescript
// .amp/plugins/example.ts
import type { PluginAPI } from '@ampcode/plugin'

export default function(amp: PluginAPI) {
  // Register tools the agent can call
  amp.registerTool({ name, description, inputSchema, execute })

  // Handle lifecycle events
  amp.on('tool_call', (event) => { ... })
  amp.on('tool_result', (event) => { ... })

  // Show UI
  ctx.ui.notify(...)
  ctx.ui.confirm(...)
  ctx.ui.input(...)

  // AI-powered classification
  const result = await amp.ai.ask("Is this safe?", { confidence: true })
}
```

### Queuing & Steering
- Messages sent while the agent is busy are queued (not interrupting)
- **Steer** (⏎ on selected queued message) fast-tracks it for the next tool result
- **Esc Esc** interrupts and sends immediately

### Remote Control
Threads running in the CLI can be observed and controlled from amcode.com — send messages, queue/dequeue, cancel operations.

## Performance (5000-message thread)

| Metric | Old CLI | Neo | Change |
|--------|---------|-----|--------|
| CPU% (mean ± sd) | 84.1% ± 1.6% | 17.4% ± 8.8% | −79% |
| CPU% (peak) | 86.3% | 25.8% | − |
| Memory (idle) | 1814 MB | 540 MB | −70% |

## Design Philosophy

Neo is explicitly built for "what frontier models can do now, in 2026, and what they will be able to do in the future" — not for what once was. Features that made sense when models needed babysitting (manual Handoff, permission dialogs, rollback on message edit) are removed. The CLI itself is described as "a ladder: we use it to climb up to the next level and then we might not need it."

## Comparison with Other Harnesses

| Feature | Amp Neo | Claude Code | OpenCode |
|---------|---------|-------------|----------|
| Architecture | Compaction-first | Session-based | Session-based |
| Permissions | Plugin-based (default: allow-all) | Built-in ask/allow/deny | Configurable |
| Extensibility | Plugin API (TypeScript) | Hooks | Extensions |
| Context Management | Auto-compaction | Manual `/compact` | Auto/manual |
| Remote Control | Web UI (ampcode.com) | No | No |
| Editor Integration | None (deliberately removed) | VS Code extension | IDE-agnostic |
