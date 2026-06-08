---
title: "Show Us Your (Agent) Skills Episode 1 — Wes McKinney, Jeremiah Lowin, Randal Olson"
created: 2026-05-08
updated: 2026-05-14
author: Hugo Bowne-Anderson, Thomas Wiecki (hosts)
guests: [Wes McKinney, Jeremiah Lowin, Randy Olson]
source: YouTube (Vanishing Gradients)
url: https://www.youtube.com/live/Pq3xuChdwxQ
type: talk
duration: "103:45"
tags: [ai-agents, agent-skills, coding-agents, verification, developer-tooling, harness-engineering, context-engineering, developer-tooling]
---

# Show Us Your (Agent) Skills — Episode 1

## Video Info

- **Channel**: Vanishing Gradients
- **Published**: 2026-05-08
- **Duration**: 103:45
- **Hosts**: Hugo Bowne-Anderson, Thomas Wiecki (PyMC Labs)
- **Guests**: Wes McKinney (pandas, POSIT), Jeremiah Lowin (Prefect), Randy Olson (Good Eye Labs)
- **GitHub**: https://github.com/hugobowne/show-us-your-agent-skills

## Episode Overview

The premiere of a live series showcasing exact agent skills, workflows, and setups used by practitioners at the top of the field. The format: live demos of real agent workflows, not slides or theory. Think "Excel World Championships meets Eurovision."

## Chapter Summary

| Timestamp | Topic |
|-----------|-------|
| 00:00 | Episode intro — "What are people at the top building with AI agents?" |
| 05:36 | **Wes McKinney** on relief from boilerplate, and dumb-Claude vs smart-Claude days |
| 10:14 | A million lines of code in six months: spicytakes.org and the agentic engineering stack |
| 15:47 | **RoboRev**: a daemon that reviews every commit, with GPT-5.5 as the strongest reviewer |
| 20:30 | **Agents View**, **Middleman**, and **Kata**: the rest of Wes's local-first toolchain |
| 27:40 | Wes barely reads code; RoboRev reads it four or five times before merge |
| 31:02 | Auto mode, judgment turning into intelligence, and the YOLO sandbox tradeoff |
| 36:08 | **Jeremiah Lowin** on agents as a second brain, fed by morning voice memos |
| 39:37 | An open source maintainer's guide to saying no, and FastMCP's issue-first model |
| 46:40 | The **explain skill**: one sentence that changes the tenor of every review |
| 49:03 | Skills vs MCP: steering behavior vs distributing business logic |
| 51:12 | Anatomy of a skill: front matter, progressive disclosure, a polite note |
| 56:30 | Personal software and the Claude Hub power law, then Prefab and Cardboard in action |
| 01:03:42 | OpenClaw for memory, Claude and Codex desktops for parallel coding |
| 01:07:38 | **Randy Olson** on building at the speed of curiosity while touching grass |
| 01:13:08 | Designing the data viz skill: thin drivers, environment setup, reflect-and-improve |
| 01:20:03 | Brain, harness, skills: why minimal harnesses are winning |
| 01:23:44 | Encoding Tufte into an LLM judge, from movie deaths to marble racing |
| 01:27:00 | Live run: marriage and divorce in the US, with the verifier loop in action |
| 01:34:32 | Hugo runs the same skill on Secretariat's 1973 Kentucky Derby record |
| 01:36:40 | Generator-evaluator workflows, and how vigilant to be when agents game the judge |
| 01:43:17 | Wrap up and upcoming guests |

## Key Insights

### Wes McKinney's Agentic Engineering Stack

- **"I almost don't read code now"** — RoboRev (GPT-5.5 daemon) reviews every commit 4-5 times before merge
- 1M+ lines generated in 6 months for spicytakes.org
- Toolchain: RoboRev (reviewer) → Agents View (session DB) → Middleman (dashboard) → Kata
- **dumb-Claude vs smart-Claude**: daily variance in model quality is a real frustration
- Superpowers skills framework as foundation

### Jeremiah Lowin's Context Engineering

- **Second brain architecture**: voice memos → transcribed → fed into agent memory substrate each morning
- **Explain skill** as the anchor: one sentence that changes the tenor of every review
- **Skills vs MCP distinction**: skills steer behavior; MCP distributes business logic
- Skill anatomy: front matter → progressive disclosure → polite note
- **Personal software**: ephemeral tools built with Prefab (Python DSL for generative UIs) and Cardboard (presentations)
- Uses OpenClaw for memory, Claude + Codex desktops for parallel coding

### Randy Olson's Verification-Centric Workflow

- **"Building at the speed of curiosity while touching grass"**
- Data viz verifier skills that encode Tufte's principles as LLM judges
- **Digital twin** thought partner: a prompt that pushes back instead of agreeing
- **Reflect and improve** skill design pattern
- **Generator-evaluator workflow**: one agent generates, another evaluates — need vigilance against judge-gaming
- Live demo: marriage/divorce US data visualization with verifier loop

### Cross-Cutting Themes

- **Skills as thin drivers** — minimal wrappers, not fat abstractions
- **Progressive disclosure** — reveal complexity only when needed
- **Minimal harnesses are winning** — "Brain, harness, skills" framework
- **Ephemeral "just for me" software** — agents making throwaway tools viable

## Upcoming Guests (Episode 2)

- Hilary Mason (CEO, HiddenDoor)
- Bryan Bischof (Theory Ventures)
- Eric Ma (Research DS lead, Moderna Therapeutics)
- Tomasz Tunguz (Theory Ventures)

## Links

- [GitHub: show-us-your-agent-skills](https://github.com/hugobowne/show-us-your-agent-skills)
- [NotebookLM transcript](https://notebooklm.google.com/notebook/95f260ad-6c67-4bbd-9f00-fc3450f07c16)
- [Luma calendar](https://luma.com/calendar/cal-8ImWFDQ3IEIxNWk)
- [Vanishing Gradients Substack](https://hugobowne.substack.com/)
- [Agentic Data Science course](https://vanishinggradients.short.gy/data-science-agentic)
