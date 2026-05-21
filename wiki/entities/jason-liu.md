---
title: Jason Liu
description: "Creator of Instructor library and Staff ML Engineer; formerly Stitch Fix and Meta, currently at OpenAI on Codex team"
url: https://jxnl.co
type: entity
created: 2026-04-13
updated: 2026-05-21
tags:
  - person
  - open-source
  - structured-outputs
  - developer-tooling
  - context-engineering
  - evaluation
  - rag
  - coding-agents
  - agent-harness
  - workflow
  - human-in-the-loop
aliases:
  - jxnl
  - jxnlco
  - Jason Liu
sources:
  - https://jxnl.co/
  - https://github.com/jxnl
  - https://python.useinstructor.com/
  - https://x.com/jxnlco
  - raw/newsletters/2026-05-19-can-i-get-my-agents-on-the-phone.md
  - raw/articles/2026-05-18_jxnl-six-levels-codex-morning-brief.md
  - raw/articles/2026-05-20_jxnlco_getting-the-most-out-of-codex.md
---

# Jason Liu (@jxnlco)

**Jason Liu** is a Developer Experience Engineer at **OpenAI** (Codex team), creator of the **Instructor** library for structured LLM outputs, and founder of 567 Studios. He has built AI systems driving $50M+ annual revenue and is a prominent voice in the RAG, context engineering, and evaluation space.

## Overview

Liu brings over 10 years of experience building AI and ML systems at scale. Before OpenAI, he was a Staff ML Engineer at **Stitch Fix** (2018–2023) and earlier a Data Scientist at **Meta/Facebook** (2017). He founded **567 Studios** in 2023, through which he provided AI consulting, training, and open-source development before joining OpenAI.

He is a graduate of the University of Waterloo (Bachelor of Mathematics, Computational Mathematics & Statistics, 2012–2017).

## Open Source

### Instructor
Instructor is a Python library for structured outputs from LLMs, achieving **6M+ monthly downloads** and **11,000+ GitHub stars**. OpenAI cited Instructor as inspiration for their structured output feature. The library provides:
- Pydantic-based output validation and structuring
- Support for multiple LLM providers (OpenAI, Anthropic, Cohere, etc.)
- Streaming, retrying, and validation patterns
- TypeScript port: instructor-js (794 stars)

## Career Timeline

| Period | Role | Organization |
|--------|------|-------------|
| 2025–Present | DX Engineer, Codex Team | OpenAI |
| 2023–2025 | Founder / AI Consultant | 567 Studios |
| 2018–2023 | Staff ML Engineer | Stitch Fix |
| 2017 | Data Scientist | Meta / Facebook |

### Consulting Clients (567 Studios)
Through 567 Studios, Liu consulted for Seed to Series B companies on AI best practices: RAG, Context Engineering, and Evaluations. Clients included:
- Zapier, HubSpot, Limitless
- Weights & Biases, Modal Labs
- Timescale, Pydantic

## Training & Education

Liu runs intensive training programs through **Maven** (Applied LLMs):
- **Systematically Improving RAG Applications** — 400+ engineers trained, practical production RAG framework
- **3-Day AI Coding Accelerator** (with Vignesh Mohankumar)

Students from OpenAI, Anthropic, Google, Microsoft, Amazon, and Netflix have attended his courses.

## Key Theses & Philosophy

Liu advocates for:
- **Outcomes over tasks** — focus on system-level results rather than individual model outputs
- **Simplicity over complexity** — avoid over-engineering; prefer minimal, well-understood pipelines
- **Speed over perfection** — iterate rapidly on evaluations and feedback loops
- **Systematic evaluation** — RAG systems need structured, repeatable evaluation frameworks; demos don't equal production readiness
- **Context Engineering as infrastructure** — treating context construction as a first-class engineering discipline

## Writing

Liu writes at **jxnl.co** about:
- RAG system design and evaluation
- Structured output techniques
- Agent architectures and harness engineering
- Developer tooling for LLMs
- Personal essays on productivity, RSI, ambition, and self-worth

## Angel Investing

Liu is an angel investor and a16z scout, backing companies including:
- Pydantic (Logfire), Modal, Exa, Shaped, Rork, Lovable, Browserbase, Raindrop, Julius, Extend, Vantager

## Publications

- Liu, J., Weitzman, E.R., & Chunara, R. (2017). Assessing behavior stage progression from social media data. *CSCW 2017*, 1320-1333.
- Rehman, N., Liu, J., & Chunara, R. (2016). Propensity score matching for vaccination sentiment analysis. *AAAI Spring Symposium*.



### Codex Maxxing (May 2026)

Liu published his "Codex maxxing" daily primitives, a set of practices for keeping Codex useful across workflows:

| Practice | Description |
|----------|-------------|
| **Durable threads** | Maintaining persistent conversation threads that survive across sessions |
| **Shared memory** | Using Codex's memory capabilities across multiple workflows |
| **Daily primitives** | Repeating patterns that keep Codex productive over extended use |

This builds on Liu's broader philosophy of treating AI tools as **infrastructure for daily work** rather than one-off problem solvers — consistent with his context engineering perspective.

### Six Levels of Codex Morning Brief (May 2026)

Liu published a progressive complexity ladder for teaching Codex through a morning brief workflow:

| Level | Capability | What It Teaches |
|-------|-----------|----------------|
| **1** | Ask what's going on today | Connectors (Slack, Gmail, Calendar) |
| **2** | Add an agents file | Persistent defaults and preferences |
| **3** | "Keep an eye on this" | Recurring automations |
| **4** | Split into project threads | Durable, project-scoped briefs |
| **5** | Draft the work, don't send | Trust boundary: draft but don't impersonate |
| **6** | Memory vault | Durable context that compounds across sessions |

The framework starts with a simple morning brief and ends with a miniature operating system. Key principles:
- Each level teaches one real capability
- The thread carries preference forward (improves as you complain about it)
- Level 6 introduces a file-based vault (`TODO.md`, `people/`, `projects/`, `daily/`, `notes/`, `AGENTS.md`)
- Subagents can parallelize searches once the brief has enough moving parts

Source: [[raw/articles/2026-05-18_jxnl-six-levels-codex-morning-brief.md]]

### Getting the Most Out of Codex (May 2026)

Liu published a comprehensive guide to Codex's expanding surface area, arguing that Codex is evolving from a narrow coding assistant into **"a system for getting computer work done."** The article catalogs the full Codex app capability set:

| Capability | Description |
|-----------|-------------|
| **Durable threads** | Persistent workspaces that survive across sessions; pinned threads with Command-1~9 shortcuts for recurring workflows (Chief of Staff, release, docs review) |
| **Voice input** | Built-in voice for rough, unpolished thoughts and meeting transcripts that preserve uncertainty and emphasis better than summaries |
| **Steering** | Interrupting in-flight tasks with corrections before the current step finishes |
| **Queuing** | Adding next-task instructions without interrupting current work |
| **$browser / @chrome / @computer** | Layered reach: in-app browser, signed-in Chrome, desktop GUI — extending Codex beyond the repo |
| **MCP + Connectors** | Slack, Gmail, Calendar integration — tasks often arrive as messages before they become code |
| **Skills** | Reusable packaged workflows Codex can replay without relearning |
| **Mobile** | Continue threads from phone while local environment stays on Mac |
| **Thread automations** | Heartbeat-style recurring wake-up calls returning to the same thread on a schedule |
| **Goals** | Long-running tasks with measurable finish lines and verifiers (test suites, benchmarks, E2E workflows) |
| **Side panel** | In-place artifact review for code, decks, PDFs, browser pages, spreadsheets — inspect, annotate, revise without context switch |
| **Shared memory** | Obsidian vault (file-based durable context) + Codex Memories + Chronicle for recall across threads |

Key architectural insight: **Human-in-the-loop isn't a fallback — it's the design surface.** Steering, queuing, side panel annotation, and "draft but don't send" are all explicit control primitives that keep the user close to the work while it unfolds. Thread automations and Goals provide async execution that continues while the user is away, but always with the human as the final decision-maker.

Source: [[raw/articles/2026-05-20_jxnlco_getting-the-most-out-of-codex.md]]

## Cross-References

- **[[entities/rahul]]** — Related via shared interest in structured outputs and developer tooling
- **OpenAI Codex** — Liu currently works on the Codex team at OpenAI
- **Pydantic** — Instructor is built on Pydantic; Liu is an investor in Pydantic Logfire
- **Instructor** — Liu's primary open-source project; canonically a tool/entity
