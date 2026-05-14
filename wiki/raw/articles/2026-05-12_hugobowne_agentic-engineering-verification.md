---
title: "Agentic Engineering and the Lost Art of Verification"
created: 2026-05-12
updated: 2026-05-14
author: Hugo Bowne-Anderson
source: Substack (Vanishing Gradients)
url: https://hugobowne.substack.com/p/agentic-engineering-and-the-lost
type: newsletter-article
tags: [ai-agents, agent-skills, code-review, verification, developer-tooling, harness-engineering, context-engineering]
---

# Agentic Engineering and the Lost Art of Verification

> **Stop reading code and start testing software agentically**

## Overview

Hugo Bowne-Anderson's article, published May 12, 2026, summarizes the premiere episode of *Show Us Your Agent Skills* — a live session where guests walk through their exact agent skills, workflows, and setups. The central thesis: the industry is shifting from "vibe coding" to **agentic engineering**, where verification (not reading code) is the critical skill.

## Key Quote

> "I almost don't read code now. My approach with Roborev is it's like my code reader. The mantra is: Roborev reads every line of code that is generated. It gets read multiple times. And so, whenever I push up a pull request, the branch gets re-reviewed. And so by the time I'm merging a pull request into a repository, the code has all been read by agents four or five times minimum. I look at the code in terms of structural detail: does it look right?"
> — **Wes McKinney** (creator of pandas, POSIT)

## Participants

- **Wes McKinney** — creator of pandas, POSIT. Built [[entities/roborev]], [[entities/agents-view]], [[entities/middleman]], and [[entities/kata]].
- **Jeremiah Lowin** — founder/CEO of Prefect. Building [[entities/fastmcp]], [[entities/prefab]], [[entities/cardboard]].
- **Randy Olson** — co-founder/CTO of Good Eye Labs. Data viz expert, subreddit moderator.
- **Hugo Bowne-Anderson** — host, Vanishing Gradients newsletter/podcast.
- **Thomas Wiecki** — co-host, PyMC Labs.

## Key Themes

### 1. From Vibe Coding to Agentic Engineering

Wes McKinney describes a "software factory" of parallel agents. He barely writes or reads code anymore — RoboRev (background daemon using GPT-5.5) reviews every commit 4-5 times before merge. His stack: spicytakes.org (1M+ lines in 6 months), Agents View (agent session database), Middleman (local GitHub dashboard), and Kata.

### 2. Verification, Not Reading

The core insight: agents should handle verification. This isn't about reading code faster — it's about delegating verification entirely to agent systems that run in background, continuously re-reviewing every line.

### 3. Context Engineering as "Second Brain"

Jeremiah Lowin's approach: years of feeding voice memos, recorded meetings, and morning briefs into his agent's **memory substrate**. He chose OpenCode specifically for deep memory customization. His skill hierarchy starts with an "explain" skill that anchors everything else.

### 4. Encoding Human Judgment into Agent Skills

Randy Olson encodes Tufte's data visualization rules directly into agent skills, so agents themselves perform verification. His "digital twin" prompt acts as a thought partner that pushes back instead of agreeing. He also uses cron job reports for colleagues and a "reflect and improve" design pattern.

### 5. Skills Architecture

- **Skills as thin drivers** — minimal wrappers that call tools
- **Progressive disclosure** — skills reveal complexity only when needed
- **Managing context rot** — strategies for extended agent sessions
- **"Just for me" software** — ephemeral tools agents make viable

## Tools and Projects Mentioned

| Tool | Creator | Description |
|------|---------|-------------|
| [[entities/roborev]] | Wes McKinney | Background code reviewer daemon (GPT-5.5) |
| [[entities/agents-view]] | Wes McKinney | Agent session database |
| [[entities/middleman]] | Wes McKinney | Local GitHub dashboard |
| [[entities/superpowers]] | Jesse Vincent | Skills framework Wes builds on |
| [[entities/fastmcp]] | Jeremiah Lowin | MCP tooling |
| [[entities/prefab]] | Jeremiah Lowin | Python DSL for generative UIs |
| [[entities/cardboard]] | Jeremiah Lowin | Ephemeral presentation tool |
| [[entities/opencode]] | — | Agent harness Jeremiah customized |

## Links

- [spicytakes.org](https://www.spicytakes.org/) — Wes McKinney's website
- [RoboRev](https://www.roborev.io/)
- [Agents View](https://www.agentsview.io/)
- [Middleman](https://github.com/wesm/middleman)
- [Superpowers](https://github.com/obra/superpowers)
- [FastMCP](https://github.com/jlowin/fastmcp)
- [Show Us Your Agent Skills GitHub repo](https://github.com/hugobowne/show-us-your-agent-skills)
- [Full episode on YouTube](https://youtube.com/live/Pq3xuChdwxQ)
- [NotebookLM transcript](https://notebooklm.google.com/notebook/95f260ad-6c67-4bbd-9f00-fc3450f07c16)
