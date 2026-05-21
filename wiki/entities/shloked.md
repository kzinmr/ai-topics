---
title: "Shlok Khemani (@shloked)"
created: 2026-05-21
updated: 2026-05-21
type: entity
tags: [person, tool, indie-maker, open-source, cli, browser-automation, coding-agents, typescript, memory-systems, agent-tooling]
sources: [https://github.com/shlokkhemani, https://github.com/shlokkhemani/chatferry, https://www.shloked.com/, raw/articles/2026-05-20_shloked_chatferry.md]
---

# Shlok Khemani (@shloked)

Indie developer and open-source creator known for building developer tooling at the intersection of AI agents and browser automation. Creator of **ChatFerry**, a CLI tool that lets coding agents use ChatGPT and Claude web UIs without API keys. Based in Gurgaon, India. Writes at [shloked.com](https://www.shloked.com/). See also: [[entities/shlok-khemani]] for broader coverage of his writing and memory-systems research.

## Quick Facts

| Category | Detail |
|----------|--------|
| **X / Twitter** | [@shloked](https://x.com/shloked) |
| **GitHub** | [shlokkhemani](https://github.com/shlokkhemani) (54 followers, 17 public repos, joined 2016) |
| **Location** | Gurgaon, India |
| **Role** | Indie developer, open-source creator |
| **Key Project** | ChatFerry — TypeScript CLI for browser-based AI agent prompting |
| **Notable Repos** | openpoke (465★), claude-memory-tools (53★), chatferry, conjure, centaur, gpt2pdf |
| **Languages** | TypeScript, JavaScript, Python |
| **Domain** | AI agent tooling, browser automation, CLI development |

## Overview

Shlok Khemani is an indie developer who builds practical tools for the AI coding agent ecosystem. His most notable recent project is **[[concepts/chatferry]]** — a TypeScript CLI that opens a real Chromium browser, logs into ChatGPT or Claude using the user's existing paid subscription, sends prompts, waits for streaming completion, and saves responses as structured markdown files. This approach eliminates the need for API keys and per-token costs, instead leveraging existing browser sessions and subscriptions.

Khemani's work spans two complementary domains: **(1) agent infrastructure tooling** (ChatFerry, Conjure) and **(2) AI memory architecture analysis** (reverse-engineering ChatGPT Memory, analyzing Anthropic's file-based memory philosophy). His broader body of work is documented at [[entities/shlok-khemani]].

> "Talk to ChatGPT and Claude from your terminal. No API keys — uses your existing browser sessions." — ChatFerry README

## Core Ideas

### Browser-as-API Pattern
Khemani's ChatFerry embodies the **browser-as-API** pattern: instead of using official REST APIs (which incur per-token costs), run a headful Chromium browser with persistent login profiles. The browser becomes the API surface, and the user's existing ChatGPT Plus / Claude Pro subscription handles all usage costs.

### No-API-Key Architecture
ChatFerry is designed explicitly for scenarios where API keys are unavailable or undesirable: coding agents running on local machines, CLI tools that need web UI features (canvas, artifacts, extended thinking), and users who already pay for web subscriptions and want to avoid additional API billing.

### Filesystem-First Persistence
Consistent with Khemani's broader philosophy (see [[entities/shlok-khemani#Filesystem-First Memory (Claude vs. ChatGPT)]]), ChatFerry stores browser profiles, run state, and debug artifacts on the filesystem under `~/.chatferry/`. Markdown exports land in the user's working directory with `.meta.json` sidecars.

## Key Work

| Project | Description | Stars | Language |
|---------|-------------|-------|----------|
| **[[concepts/chatferry]]** | CLI for coding agents to prompt ChatGPT/Claude via browser sessions | 5 | TypeScript |
| **openpoke** | Open-source multi-agent assistant replicating Poke's architecture | 465 | Python |
| **claude-memory-tools** | Reference implementations for Claude's Memory Tool API (Next.js + Python CLI) | 53 | TypeScript |
| **conjure** | Headless AI agents from terminal — skill for Codex, Claude Code, and pi | 3 | — |
| **centaur** | (private repo) | — | — |

## Writing & Activity

Khemani publishes technical analysis at [shloked.com](https://www.shloked.com/), covering AI memory architecture, agent tooling, and reverse-engineering of production AI systems:

- **2026-05-18** — Last push to ChatFerry (maintenance)
- **2026-04-13** — "What I Found Interesting in Claude Code's Source" — cache-first architecture analysis
- **2026-04-12** — "Why Cognition is Copying Claude's Memory" — filesystem-based memory validation
- **2026-03-26** — ChatFerry v0.1.0 released (MIT license)
- **2025-10-14** — "Anthropic's Opinionated Memory Bet" — six-operation file-based memory analysis
- **2025-09-22** — OpenPoke: open-source replication of Poke's multi-agent architecture

## X Activity Themes

- **Agent infrastructure**: CLI tools, browser automation, coding agent workflows
- **Memory systems**: filesystem-based approaches, Claude vs. ChatGPT memory philosophy
- **Open-source releases**: announcing new tools (ChatFerry, Conjure, Vajra)
- **Technical deep dives**: reverse-engineering production AI systems, source code analysis

## Related People

- [[entities/shlok-khemani]] — Broader entity page covering his writing, memory research, and full project history
- [[entities/peter-steinberger]] — Creator of OpenClaw, also builds personal AI agent infrastructure
- [[entities/simon-willison]] — Django co-creator, CLI-first tooling for coding agents (Rodney, Showboat, LLM)
- [[entities/boris-cherny]] — Creator of [[entities/claude-code]], one of the platforms ChatFerry targets
- [[entities/thariq-shihipar]] — Claude Code team at Anthropic; both build agent-facing CLI tools
