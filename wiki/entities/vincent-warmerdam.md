---
title: Vincent Warmerdam
type: entity
created: 2026-05-20
updated: 2026-05-29
tags:
  - person
  - open-source
  - developer-tooling
  - harness-engineering
  - ai-agents
  - agent-skills
  - notebook-agents
aliases:
  - Koaning
  - @koaning
sources:
  - raw/newsletters/2026-05-20-agent-harness-ipynb.md
  - https://open.substack.com/pub/hugobowne/p/agent-harnessipynb
  - transcripts/2026-05-21_vanishing-gradients_show-us-your-agent-skills-ep3.md
---

# Vincent Warmerdam (@koaning)

**Vincent Warmerdam** is an Engineer at **marimo** (the reactive Python notebook platform) and a prominent voice in agentic notebook workflows. He previously worked as a Research Scientist at Rasa and created the popular "Calm Code" philosophy for building with AI agents.

## Overview

Warmerdam operates at the intersection of data science tooling, notebook environments, and AI agent workflows. His work at marimo focuses on building a reactive notebook platform that natively supports agent collaboration — where agents and humans share a live editing canvas.

## Key Contributions

### Agent-Harness.ipynb (May 2026)

In conversation with Hugo Bowne-Anderson (Vanishing Gradients podcast), Warmerdam shared deep insights on agent notebook workflows:

| Insight | Detail |
|---------|--------|
| **Shared notebook canvas** | marimo as agent-human co-existence environment — agents and humans edit the same cells |
| **marimo linter fix rate** | Dedicated linter solved ~60% of agent errors overnight |
| **Incremental generation** | Agents generate one to two cells at a time, not entire notebooks |
| **Speed models for exploration** | Faster open-weight models (Kimi K2) enhance exploratory flow, reducing iteration friction |
| **Pi agent harness** | Agents extend themselves rather than reaching for MCP — harness-first philosophy |
| **Calm as a tool** | "Calm is the most underrated tool for building well" |

### marimo Platform

marimo is an open-source reactive notebook for Python — reproducible, Git-friendly, deployable as interactive apps. Key features for agent workflows:
- Cells automatically rerun when dependencies change
- No hidden state — every cell's output reflects its current code
- Native support for collaborative editing via agents

### Rasa Research

At Rasa, Warmerdam worked on conversational AI and dialogue systems — foundational experience that informs his perspective on agent-human interaction patterns.

## Philosophy

Warmerdam advocates for:
- **Calm engineering** — building with intention, not velocity
- **Incrementalism** — agents should make small, verifiable changes
- **Co-existence over replacement** — agents augment, not replace, the developer's cognitive process

## Show Us Your (Agent) Skills Episode 3 (2026-05-21)

Vincent demonstrated **notebook-as-canvas** with marimo and shared his philosophy on agent collaboration, widgets, and careful science:

### Wiggly Stuff Widgets
- Maintains a library of interactive Python widgets ("Wiggly Stuff") — 3D, graphs, drawing — that turn notebooks into playful, explorable canvases
- **Composable by design**: Every widget is a Lego brick — "If you have a library full of Lego bricks that have rules on how things should click together, it's easier for Claude to figure out what the next brick should be"
- **Agent-readable docs**: Every widget has markdown documentation and an llms.txt file — agents (Open Code, Claude) can discover and learn the library automatically
- **Notebook as shared canvas**: Human edits Python cells, agent reads Python variables, agent makes changes — bidirectional collaboration surface

### marimo Pair (Agent Reads All Python Variables)
- **Pair feature**: Opens a scratch pad where Claude/Codex can write into the notebook, read every Python variable in memory, and interact with UI elements
- **Agent sets slider to 5**: Demonstrated the agent moving UI widgets — not just reading state but *manipulating* the interface
- **Eliminates debugging friction**: Agent doesn't need to print pipeline steps to debug — it can directly inspect variables at any stage
- **Conductor integration**: Automatically runs notebooks on workspace setup, opens browser to see agent-generated demos
- **Marimo sandbox (Moab)**: Cloud execution so agents never touch local files; Pi-based skill system for secure agent-notebook workflows

### Dumber Faster Models Keep You in the Loop
- Uses Kimi K2.5 (faster, open-weight) for interactive pairing — speed matters more than capability for exploratory flow
- "Brain farts" satisfied within 30 minutes → artifacts that lead to interesting downstream work
- Game of Life widget example: quick experiment → asynchronous Python/frontend interaction → understanding through play

### Composable Libraries Beat Skill Files
- **Example-driven learning**: Claude learns to create new widgets by finding similar existing widgets in the library and following the pattern — effectively self-training from codebase examples
- **Unix philosophy**: Componentized libraries with clear composition rules do more than any CLAUDE.md file — the agent can fix its own problems by analogy
- **Conductor setup**: JSON config bootstraps dependencies, runs demo notebooks automatically, gives agent full library context before first prompt

### Boring Careful Science Over Confident Quackery
- **19th-century weather prediction analogy**: In the 1800s, high demand for weather prediction + low supply of real science = alchemists and quacks flooding the market. One guy convinced Congress to fund dynamite balloons to *cause* rain.
- **Modern parallel**: The hype around AI agents creates the same dynamic — "don't choose the life of imitation"
- **Solution**: Boring, careful science. Check "does it work? Yes/No." Share data. The telegraph enabled meteorology; the internet sometimes hinders it.
- **Go slow if it means understanding better**: Watch the boring person, not the person with the ridiculous thumbnail
- **Calm Code philosophy**: "Calm is the most underrated tool for building well" — sustained through the hype cycle

### Frustrations
- YouTube/algorithm hype makes it impossible to find calm, educational content — "I just want normal boring people exchanging notes"
- The "guru" performance around AI tools creates an intellectual laziness that impedes real progress

## Related

- [[entities/hugo-bowne-anderson]] — Host of Vanishing Gradients podcast; conversation partner for Agent-Harness.ipynb
- [[entities/marimo]] — Marimo reactive notebook platform
- [[entities/nico-gerold]] — Amp engineer; Pi-inspired plugin system; Episode 3 co-guest
- [[entities/matthew-honnibal]] — spaCy founder; former colleague; Episode 3 co-guest
- [[entities/alan-nichol]] — Rasa CTO; former colleague; Episode 3 co-guest
- [[entities/eleanor-berger]] — Hermes agent + design pattern discussion; Episode 3 co-guest
- [[concepts/agent-harness]] — Agent harness engineering
- [[concepts/notebook-agents]] — Notebook-native agent workflows
