---
title: "Flue"
created: 2026-05-06
updated: 2026-08-16
type: entity
tags:
  - entity
  - developer-tooling
  - framework
  - ai-agents
  - open-source
aliases:
  - "Flue.js"
related:
  - "entities/anthropic]]"
  - "concepts/harness-engineering]]"
sources:
  - raw/newsletters/2026-05-05-codex-is-gaining-steam.md
  - https://open.substack.com/pub/bensbites/p/codex-is-gaining-steam
  - raw/newsletters/2026-08-15-react-for-agents-astro-creator-brings-hooks-to-his-meta-harness-flue.md
  - https://www.latent.space/p/flue-2
---


# Flue

**Flue** is a **TypeScript framework** for building coding agents in the style of Claude Code. Announced in May 2026, it enables developers to construct agentic workflows that autonomously read, edit, and manage codebases.

## Overview

| Detail | Value |
|--------|-------|
| **Language** | TypeScript |
| **Style** | Claude Code-style agent architecture |
| **Category** | Coding Agent Framework |
| **Announced** | May 2026 (via Ben's Bites) |

## Positioning

Flue enters a rapidly growing ecosystem of agent frameworks:

| Framework | Language | Style |
|-----------|----------|-------|
| **Flue** | TypeScript | Claude Code-style agents |
| **OpenAI Agents SDK** | Python, TypeScript | OpenAI-native agent harness |
| **Claude Code** | TypeScript | Anthropic's CLI coding agent |
| **OpenCode** | Go | Multi-model coding agent CLI |
| **AgentCraft** | TypeScript | RTS-style orchestrator |

### What "Claude Code-Style" Means

Claude Code uses an agent loop where the model:
1. Reads files and codebase context
2. Plans edits (multiple files)
3. Applies changes via tools (bash, edit, write)
4. Iterates based on results and errors

Flue provides this pattern as a reusable framework, allowing developers to build custom coding agents with the same architecture but targeting specific workflows or custom tool integrations.

## Ecosystem Context

The TypeScript coding agent ecosystem is expanding rapidly, driven by:
- **Node.js ecosystem familiarity** among web developers
- **Claude Code** being TypeScript-native (available as both npm package and VS Code extension)
- **OpenAI Agents SDK for TypeScript** launching in May 2026

Flue represents the "framework-ification" of coding agent patterns — moving from proprietary implementations (Claude Code) to reusable building blocks (Flue).

## Flue 2: React-Style "Agent Hooks" (Aug 2026)

Flue 2, released August 2026 as the **first stable release**, is built on React-style **Agent Hooks** as its foundation. The shift came after creator [[entities/fred-schott|Fred Schott]] realized composability — not routing — was the right model: *"I originally tweeted that we were building the Astro for agents or the Next.js for agents. But then I realized: maybe no one has even built the React for agents."*

### Agent = Function That Re-Renders Every Turn

In Flue, an agent is represented by a **JavaScript function** that "re-renders on every turn" (before every model call). Hooks are authored in TypeScript and let agents "manage their own state, listen to agent lifecycle events, and even attach different resources and capabilities dynamically to enhance themselves at runtime."

- **16 built-in hooks** in Flue 2, including `useSkill()`, `useTool()`, `useSubagent()`; custom hooks are supported
- Dynamic configuration enables "real support bots, real triage bots" that cannot be fully configured in advance (e.g., a support agent that attaches an account-management tool after verifying a user)

### Evolution from v1: Routing → Composability

Schott's design thinking evolved after first Flue users (especially larger customers) showed that **"their whole company is one agent"** — file-based routing (ported from web-framework patterns) was irrelevant. The Flue 2 API consequently draws more from React than from Astro/Next.js: "less about routing and these website concepts and more about, at its base level, how do you compose an agent on many different things."

### Built on Pi (Minimal Harness)

Flue 2 is built on **Pi**, an open-source minimal harness — Flue is an opinionated take on Pi, analogous to Vite beneath Astro (hosted agents in Flue 2 are built with Vite). Schott: *"I think Pi can serve that role, where it's the right abstraction — it doesn't do too much, but it gives the right APIs."*

Key commitments:
- **"There is no agent without a harness"** — harness is fundamental, not a feature
- Origins: began as an issue-triage system inside the Astro repo, then transitioned "from just automation in a repo to wanting to take the Claude Code experience, make it headless, make it hostable and run it in the cloud"
- **AI-agent-first onboarding**: docs have markdown support and the whole onboarding flow is "pass this prompt to your agent, it's gonna guide you through it" — Claude Code is a common driver

### Competitive Positioning

- **Vercel's eve** — "the most directly competitive": same built-in-harness take, launched around the same time. Key difference: host portability. Flue is an "open source framework for every host"; eve is optimized for Vercel's platform (the known Next.js playbook). Vercel itself has shown a Flue agent can deploy there.
- **"OG agent frameworks"** (pre-harness): Vercel AI SDK, Cloudflare Agents SDK, Mastra (Gatsby team) — all adding harnesses now, but as an added feature rather than a built-in core.
- **Meta-harnesses** (Databricks Omnigent, self-improving Exo): Schott notes the term is confusing at this stage; one API across all harnesses "would muddle the story" since "the framework and the harness are very intertwined." He has played with Exo but sees it as "a different interest scenario that isn't really related to hosted agents."
- **LangChain Managed Deep Agents**: not on Flue's roadmap — *"It's so early for us, we're just focused on building the best harness."*

Positioning quote: *"The best tools are the ones that float above the host. That opens the door for the most developer adoption and the most innovation."*

Source: [React for Agents: Astro Creator Brings Hooks to his Meta-Harness, Flue](https://www.latent.space/p/flue-2) — Richard MacManus interview with Fred Schott, Latent Space, Aug 15 2026. Connects to the Bret Taylor framing ("jQuery era of agents, not the react era") and the [[concepts/harness-engineering]] / [[concepts/agent-team-swarm|meta-harness]] debates.

## Related Concepts

- [[concepts/harness-engineering]] — Broader agent execution framework philosophy
- [[entities/anthropic]] — Claude Code (the reference architecture Flue emulates)

## Sources

- [Codex is gaining steam (Ben's Bites)](https://open.substack.com/pub/bensbites/p/codex-is-gaining-steam) — May 5, 2026
