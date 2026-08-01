---
title: "qm Multiplayer Agent Harness"
created: 2026-08-01
updated: 2026-08-01
type: concept
tags: [multi-agent, coding-agents, open-source, ai-agents, agent-harness, ycombinator, hn-popular]
sources:
  - raw/articles/2026-07-31_qm_multiplayer-agent-harness.md
  - https://github.com/yc-software/qm
  - https://news.ycombinator.com/item?id=49126604
---

# qm Multiplayer Agent Harness

**qm** is a YC-backed, open-source multiplayer agent harness designed for collaborative work within organizations. Unlike single-user coding agents, qm provides each employee their own isolated agent workspace while enabling team collaboration through shared Slack channels, group messages, and project rooms. It launched to significant community interest on Hacker News, earning **584 points**.

## Overview

Most AI agents are designed as personal assistants — one human, one agent. Scaling this to a company introduces complexity: shared state, permissions, conflicting instructions, and audit requirements. qm addresses this by treating agents as **organizational infrastructure**: each person and each Slack room gets its own scoped memory, files, keychain, permissions, crons, web apps, and durable sandbox, all managed through a unified core.

qm is built with vendor independence as a first principle. It supports multiple harness backends — Pi, OpenCode, Codex, and Claude Code all drive the same core — so a deployment is not tied to any single model provider or agent runtime. The system is written in TypeScript on Node (Fastify for HTTP, Bolt for Slack, Vite+Lit for the web UI) and is available under the **MIT License**.

## Architecture and Features

### Core Architecture

The system has a **headless core** that mediates every turn through a central agent loop, a Postgres persistence layer for sessions, memory, and queue state, and per-scope sandboxes that provide durable filesystems with installed tools and logged-in services:

```
Postgres (sessions, memory, queue)
  |
Headless Core (API, identity, policy, scheduler)
  |
Agent Loop (Pi / OpenCode / Claude Code / Codex)
  |
Per-Scope Sandbox (files, tools, logged-in services)
```

The web UI, admin panel, and public portal are optional plugins over the core's HTTP API. Slack integration runs as an in-process plugin supervised by the core.

### Key Features

- **Personal and shared scopes.** Each employee customizes their agent independently while collaborating in shared channels and projects.
- **Slack and web parity.** The same identity and configuration carries between Slack and the web app.
- **Admin control.** Org-level configuration, security posture, and available harnesses/models are centrally managed.
- **Web apps.** Spin up custom internal apps and publish them to the right people.
- **Shared skills.** Skills are scope-owned, shareable by grant, with admin-gated promotion to the whole org and skill packs imported from git repositories.
- **Background work.** Crons and watches run work while nobody is watching.

### Security Posture

qm follows the same security model as local coding agents: the agent acts as the person it represents, with their credentials and permissions, and everything is audited. Three postures are available:

| Posture | Behavior |
|---|---|
| **Strict** | Every tool call pauses for human approval (except no-effect turn enders) |
| **Auto** (default) | A classifier screens provenance-labelled external data and tool results before they reach the model |
| **Dangerous** | No content screening, no pauses between tool calls |

A predeclared command policy (approval rules and hard denials for destructive operations) applies in every posture.

## Comparison to Agent Frameworks

qm occupies a distinct position in the agent landscape compared to orchestration frameworks like [[concepts/langgraph|LangGraph]] and [[concepts/crewai|CrewAI]].

**LangGraph** is a graph-based state machine for building stateful agent workflows. It gives developers explicit control over state transitions, checkpointing, and durable execution. qm, by contrast, is not a workflow builder — it is a **multiplayer agent harness** that provides scoped workspaces, Slack integration, and operational infrastructure for teams. Where LangGraph asks "how should the agent flow?", qm asks "how should teams of humans and agents work together?"

**CrewAI** is a role-based multi-agent orchestration framework where specialized agents (researcher, writer, reviewer) collaborate as a coordinated crew. qm differs fundamentally: it does not predefine agent roles. Instead, it gives each human their own agent with full access to their scope, and enables collaboration through shared channels. CrewAI orchestrates agents to complete tasks; qm orchestrates humans and agents to work together.

qm is closer in spirit to [[entities/openclaw|OpenClaw]] (multi-channel agent gateway) and [[concepts/agent-harnesses|agent harnesses]] generally: it focuses on the **operational surface** — how agents connect to communication channels, manage state and permissions, and integrate into existing team workflows. See [[comparisons/open-harness-vs-agent-framework|Open Harness vs Agent Framework]] for the broader architectural distinction between runtime-centric harnesses and workflow-centric frameworks.

### Multi-Harness Support

A distinguishing feature of qm is its harness-agnostic design. The core agent loop can be driven by multiple backends: [[entities/pi|Pi]] (extensible harness platform), OpenCode (multi-provider coding harness), [[entities/claude-code|Claude Code]] (Anthropic's coding agent), and Codex (OpenAI's coding agent). This avoids the vendor lock-in that plagues single-backend systems and lets organizations choose the best harness for each use case.

## HN Community Reception

qm's Hacker News launch (July 2026, 584 points) generated strong interest. Key themes from the discussion:

- **Multiplayer as the next frontier.** Commenters noted that most agent tools are built for solo developers, while real work happens in teams. qm's scoped workspaces and Slack-native collaboration were seen as addressing a genuine gap.
- **YC backing as validation.** Y Combinator's involvement signaled that multiplayer agent infrastructure is being taken seriously as an investable category, alongside existing investments in single-user coding agents.
- **Vendor independence.** The multi-harness design (Pi, OpenCode, Codex, Claude Code) was frequently praised as a hedge against model and platform lock-in, aligning with the broader [[concepts/bitter-lesson-agent-harnesses|open harness philosophy]].
- **Security concerns.** Several commenters raised questions about the security implications of agents with broad filesystem and API access operating in shared Slack channels, though qm's posture system and command policy were noted as reasonable mitigations.

## Related Pages

- [[concepts/agent-harnesses]] — Philosophy and architecture of minimal agent harnesses
- [[comparisons/open-harness-vs-agent-framework]] — Harness vs framework architectural distinction
- [[concepts/multi-agents/multi-agent-systems]] — Multi-agent system design patterns
- [[concepts/coding-agents/coding-agents]] — Overview of coding agent landscape
- [[concepts/sandbox]] — Agent sandbox isolation patterns
- [[concepts/langgraph]] — Graph-based agent orchestration (comparison)
- [[concepts/crewai]] — Role-based multi-agent framework (comparison)
- [[entities/pi]] — Pi extensible coding agent harness
- [[entities/openclaw]] — Multi-channel agent gateway with Slack integration
