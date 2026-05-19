---
title: shannhk
description: "Shann Holmberg — Head of Product at Espressio AI, co-founder of Lunar Strategy (250+ projects), AI marketer and Hermes Agent operator. Creator of the hermes-agent-control-room template. Co-author of Master Web3 Marketing."
url: "https://espressio.ai"
type: entity
created: 2026-05-19
updated: 2026-05-19
aliases:
  - shann-holmberg
  - "@shannhk"
  - "@shannholmberg"
tags:
  - person
  - content-creator
  - hermes-agent
  - agent-architecture
  - ai-product
  - startup
  - entrepreneur
sources:
  - raw/articles/2026-05-15_shann_hermes-agent-operator.md
  - "https://x.com/i/article/2055317817658900480"
  - "https://espressio.ai"
  - "https://espressio.ai/blog/hermes-agent-guide-2026/"
  - "https://github.com/shannhk/hermes-agent-control-room"
  - "https://github.com/shannhk"
  - "https://growthfolks.io/blogs/shann-holmberg-joins-espressio-ai-to-lead-agent-product-development/"
related:
  - "[[entities/hermes-agent]]"
  - "[[concepts/hermes-agent-use-cases]]"
  - "[[comparisons/hermes-vs-openclaw]]"
---

# Shann Holmberg (shannhk)

**Shann Holmberg** (handles: `@shannhk`, `@shannholmberg`) is an AI marketer and Head of Product at Espressio AI. Co-founder of Lunar Strategy, one of Europe's top Web3 marketing agencies (250+ projects delivered). Co-author of *Master Web3 Marketing*. Based in Lisbon. Creator of the `hermes-agent-control-room` template — the most comprehensive open-source operational framework for running Hermes Agent in production at scale.

## Overview

Shann Holmberg describes himself as a "vibe coder, growth marketer & insanely curious about AI." He spent 7 years building Lunar Strategy from the ground up, running campaigns with real deadlines and real money for tech companies. The internal tools he built at Lunar Strategy eventually became Espressio AI — an AI-powered marketing automation platform that builds agent systems for growth, marketing, and BD teams.

His core philosophy: **"Zero tolerance for demos that don't hold up in production."** Having managed multi-million-dollar marketing budgets and 250+ client projects, Shann brings a practitioner's lens to AI agent tooling — focused on what actually works at scale, not what looks good in a demo.

Currently, Shann is leading AI agent product development at Espressio AI, building systems that close the "strategy-to-execution gap" in marketing teams. His work focuses on **where agents replace work, not just assist with it** — researching content, producing campaigns, running logic, and generating reports autonomously.

## Key Contributions

### Hermes Agent Control Room Template
Shann created the [hermes-agent-control-room](https://github.com/shannhk/hermes-agent-control-room) — an open-source template for managing Hermes agents from a single VPS to specialist teams and orchestrated workflows. Key features:
- **4-level setup model**: Single agent → Specialists → Orchestrator + Task Bus → Automated Team
- **Control Room pattern**: Side control plane (`/root/vps-agents/`) separate from agent runtime (`/srv/<agent-name>/data/`)
- **Bundled skills**: VPS creation, control room setup, agent registration, task routing, backup management, security auditing, cron planning
- **Mermaid architecture diagrams**: Visual documentation of fleet topology

### How to Become a Hermes Agent Operator (May 2026)
Shann's flagship article on Hermes Agent operations, covering:
- The 3-component model (Brain/Memory + Personality + Skillset)
- 4-level setup progression with decision frameworks for scaling
- SEO agent 21-step pipeline (real-world case study)
- Prototype → Production methodology (grow agents, don't build them)
- "Rails vs Linux" philosophical framing (Hermes vs OpenClaw)
- Model strategy: Claude Opus 4.7 for creative work, Codex (GPT 5.5) for structured work

### 7 Marketing Agents Running on Hermes
Shann operates a full fleet of Hermes agents at Espressio, including:
- Personal assistant (Telegram, email triage, reminders, meeting summaries)
- Marketing workflow prototyping bench
- Specialized agents: SEO, Outbound/BD, Design Review, Content Writing
- Company brain (Slack, chat, email, transcript, voice memo integration)
- Content distribution agent (cross-platform atomization)
- Orchestrator agent (routing only)

## Writing Style & Philosophy

Shann's writing is **practitioner-first and anti-hype**. Key characteristics:
- **Production-grounded**: Every claim is backed by systems he runs daily
- **Anti-demo**: Explicit rejection of "automation with better branding" — demands real workflow value
- **Operational transparency**: Shares exact folder structures, Docker commands, and SSH workflows
- **Strategic heuristics**: Distills complex operational patterns into memorable rules (e.g., "you cannot write a production agent from scratch. you have to grow one")
- **Philosophical framing**: Uses evocative comparisons (Rails vs Linux, Brains make workers disposable)

## Professional Background

### Lunar Strategy (Co-founder)
Co-founded Lunar Strategy, one of Europe's top Web3 marketing agencies. Key metrics:
- **250+ projects** delivered across Web3 ecosystem
- Managed multi-million-dollar marketing budgets
- Built internal tools that became the foundation for Espressio AI
- Co-authored *Master Web3 Marketing*

### Espressio AI (Head of Product)
Leading agent product development at Espressio AI, an AI-powered marketing automation platform. The company builds AI agent systems for growth, marketing, and BD teams — content engines, lead gen pipelines, and competitive intel. Core thesis: most marketing teams know what they want to do but can't move fast enough — agents close that execution gap.

## Key Theses

- **"You cannot write a production agent from scratch. You have to grow one."** — Shann's prototype → production methodology reflects this. Start messy in Hermes, iterate 2-3 times on real work, fine-tune in a dedicated workspace, then deploy on VPS with cron.
- **"The bundled defaults compound."** — His preference for Hermes over OpenClaw is driven by the 123 pre-built skills that give a head start before any configuration.
- **"Campaign operations gap is a process problem, not a talent problem."** — Teams know strategy but can't execute fast enough. Agent layers close that gap.
- **"Deciding where agents replace work, not just assist with it."** — Distinguishing genuine agent automation from "automation with better branding."
- **"The brain layers make the worker disposable."** — In his SEO agent architecture, the company brain stays stable while worker agents iterate. Workers are replaceable; institutional knowledge is preserved.

## Cross-References

- **[[entities/hermes-agent]]** — Primary agent framework Shann operates at scale. His 4-level fleet model adds operational depth to Hermes Agent documentation
- **[[concepts/hermes-agent-use-cases]]** — Shann's 7-agent fleet provides complementary use cases to the 7 canonical workflows
- **[[comparisons/hermes-vs-openclaw]]** — Shann's "Rails vs Linux" framing captures the philosophical distinction succinctly
- **Nous Research** — Hosted Nous Research at EspressioAI HQ in Lisbon for a Hermes Agent evening (Q&A with @yeahfortommy)

## Community & Links

- **X/Twitter**: [@shannholmberg](https://x.com/shannholmberg)
- **GitHub**: [github.com/shannhk](https://github.com/shannhk) (6 public repos, joined 2023)
- **Company**: [espressio.ai](https://espressio.ai)
- **Control Room Template**: [github.com/shannhk/hermes-agent-control-room](https://github.com/shannhk/hermes-agent-control-room)
- **Guide**: [The Complete Hermes Agent Guide for 2026](https://espressio.ai/blog/hermes-agent-guide-2026/)
- **Joining announcement**: [Growth Folks interview](https://growthfolks.io/blogs/shann-holmberg-joins-espressio-ai-to-lead-agent-product-development/)
- **Location**: Lisbon, Portugal

## References

- 2026-05-15_shann_hermes-agent-operator.md
