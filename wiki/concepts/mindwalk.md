---
title: "Mindwalk"
created: 2026-07-12
updated: 2026-07-12
type: concept
tags:
  - concept
  - coding-agents
  - agent-observability
  - developer-tooling
  - data-visualization
  - ide
  - ai-agents
  - autonomous-agents
sources:
  - raw/articles/2026-07-12_mindwalk-session-replay.md
  - https://github.com/cosmtrek/mindwalk
---

# Mindwalk

**Mindwalk** is an open-source visualization tool (Go, 129 stars on GitHub, created July 2026) that replays coding-agent sessions on a 3D map of your codebase. It addresses a fundamental observability gap in coding-agent debugging: session logs record what an agent *did*, but not how it *understood* the task — which parts of the repository it treated as relevant, where it explored before acting, and whether its footprint matched the intended scope.

## Problem Statement

Existing coding-agent session logs (e.g., Claude Code JSONL, Codex session traces) capture a chronological record of tool calls, file edits, and terminal commands. Reading these logs line by line reveals *actions* but obscures *intent and context*:

- Which files did the agent explore before settling on a change?
- Did it explore irrelevant parts of the codebase?
- Was the agent's mental model of the task aligned with the developer's?
- Where did the agent spend most of its time — searching, reading, or editing?

Without answering these questions, debugging agent behavior reduces to tedious log archaeology. Mindwalk solves this by translating session traces into spatial, visual patterns that make the agent's exploration footprint immediately legible.

## How It Works

### 3D Night Map Visualization

Mindwalk renders the repository as a **night map** — a dark, city-like 3D landscape where each file is a structure and each directory is a district. The session is played back as **light moving through the map**: files the agent searched, read, or edited glow, while everything the agent never touched stays dark. The agent's understanding of the task becomes a visible shape.

### Two Core Artifacts

Mindwalk separates its pipeline into two independent artifacts, kept deliberately decoupled:

1. **Trace** — The session log normalized into an ordered stream of file-touch events. Adapters (`internal/adapter`) parse per-agent formats (Claude Code, Codex) into a common schema.
2. **Citymap** — A deterministic layout of the repository (`internal/citymap`). The same directory tree always produces the same map, making replays comparable across sessions.

A local Go server (`internal/server`) joins trace and citymap, serving the React/Three.js frontend (`web/`). All processing is fully local — no session data leaves the developer's machine.

### Playback Features

- **Tree / Terrain views** — Repository rendered as a radial tree or treemap plain. Glow intensity is proportional to how deeply and how often a file was touched.
- **Touch states** — Each file retains its deepest touch state: *seen* (moss green), *read* (moon white), *edited* (warm amber), *unvisited* (dark). The HUD surfaces friction signals — error rate, churned files, edits after the last verify — in a review strip.
- **Playback deck** — Scrub or play the session over a bucketed histogram. Bars use a cool/warm spectrum: observation (search, read, exec) stays cool, mutation (edit, verify) glows warm, so editing phases stand out at a glance.
- **Timeline marks** — Context compactions (`◇`), subagent launches (`○`), and user turns (`›`) are marked on the timeline, each a click-to-jump target.
- **Inspector** — Click a file to pin its visit history; click a visit row to jump the playhead to that moment.

## Design

Mindwalk is written in **Go** with a React/Three.js frontend for 3D rendering. The architecture enforces strict separation of concerns:

- Adapters don't know about rendering.
- Citymap generation doesn't depend on playback logic.
- The server only connects trace and citymap — it contains no domain logic of its own.

The exported JSON contracts are mirrored in a `schema/` directory to ensure consistency between the Go backend and the TypeScript frontend.

### Supported Agents

As of initial release (July 2026), Mindwalk supports:
- **Claude Code** — reads from `~/.claude/projects`
- **Codex** — reads from `~/.codex/sessions`

Additional agent adapters can be contributed via the adapter interface in `internal/adapter`.

### Quick Start

```sh
curl -fsSL https://raw.githubusercontent.com/cosmtrek/mindwalk/master/scripts/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
mindwalk
```

With no arguments, Mindwalk scans default session directories, serves the UI on a random local port, and opens a browser. Individual sessions can be opened with `mindwalk open <session.jsonl>`.

## Use Cases

### Debugging Agent Sessions

When a coding agent produces surprising or incorrect output, Mindwalk reveals *why* by showing what context the agent actually considered. A developer can see at a glance whether the agent explored the wrong module, missed a critical file, or spent too long searching before editing.

### Understanding Agent Behavior

Mindwalk transforms the opaque "black box" of agent cognition into a spatial pattern. Developers can compare sessions across different prompts, models, or configurations to understand how agents approach the same task differently.

### Code Review and Quality Assurance

The review strip highlights friction signals — error rates, churn, edits after verification — helping reviewers identify problematic sessions without manually scanning logs.

## Comparison to Other Agent Observability Tools

Mindwalk occupies a unique niche in the agent observability landscape:

| Tool / Approach | Focus | Mindwalk's Distinction |
|---|---|---|
| [[concepts/evaluation/agent-observability\|Agent observability platforms]] (LangSmith, Braintrust) | Trace collection, evaluation, feedback loops | Mindwalk focuses on *spatial intuition* rather than metric dashboards — it answers "what did the agent *think*?" rather than "was the agent *correct*?" |
| Log viewers / JSONL inspectors | Raw event inspection | Mindwalk translates events into spatial patterns that are legible at a glance |
| [[concepts/active-observability]] | Automated trace intelligence via clustering | Mindwalk is manual and visual — designed for human understanding, not automated analysis |

Mindwalk is complementary to these approaches: it addresses the pre-evaluation phase where a developer needs to build intuition about agent behavior before designing metrics or feedback loops.

## Limitations

- **Agent support is narrow** — only Claude Code and Codex at launch. Other coding agents (Cursor, GitHub Copilot, OpenClaw, Devin) are not yet supported.
- **3D rendering is resource-intensive** — large repositories (thousands of files) may produce unwieldy visualizations.
- **No evaluation integration** — Mindwalk does not score or evaluate agent performance; it is purely a visualization and exploration tool.
- **Early-stage project** — 129 stars, less than a week old at time of writing (July 2026). APIs and formats may change rapidly.
- **Subjective interpretation** — what "looks wrong" in a visualization requires human judgment; there is no automated anomaly detection.

## Related Pages

- [[concepts/coding-agents/coding-agents]] — Overview of coding agents and their ecosystem
- [[concepts/evaluation/agent-observability]] — Agent observability as a discipline: traces, evaluation, and feedback loops
- [[concepts/agentic-engineering]] — The discipline of building software with AI agents as primary contributors
- [[entities/claude-code]] — Claude Code, one of the two coding agents Mindwalk supports
- [[entities/cline]] — Cline autonomous coding agent (parallel topic in agent session analysis)

## Sources

- [Mindwalk GitHub Repository](https://github.com/cosmtrek/mindwalk) — cosmtrek/mindwalk, created 2026-07-09
- [Raw article snapshot](raw/articles/2026-07-12_mindwalk-session-replay.md) — fetched 2026-07-12
