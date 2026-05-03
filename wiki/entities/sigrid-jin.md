---
title: "Sigrid Jin"
type: entity
created: 2026-05-03
updated: 2026-05-03
tags: [person, developer-tooling, coding-agents, open-source]
aliases: ["realsigridjin", "sigrid jin", "instructkr"]
sources:
  - https://github.com/ultraworkers/claw-code
  - https://www.businessinsider.com/claude-code-leak-what-happened-recreated-python-features-revealed-2026-4
  - https://cybernews.com/tech/claude-code-leak-spawns-fastest-github-repo/
---

# Sigrid Jin

Sigrid Jin (@realsigridjin) is the creator of **[[claw-code]]**, the open-source clean-room reimplementation of Claude Code's agent harness that became the fastest repository in GitHub history to surpass 100K stars (March 2026).

## Background

- **Nationality**: Korean-Canadian
- **Education**: University of British Columbia (UBC)
- **Known aliases**: instructkr, realsigridjin
- **Featured in**: The Wall Street Journal (March 20, 2026) for using 25 billion Claude Code tokens as one of the most active power users

## Creation of Claw Code

On March 31, 2026, after Anthropic accidentally leaked the entire internal Claude Code TypeScript source via a `.map` file in the npm package, Jin ported the core architecture to **Python from scratch** within hours. The project, later rewritten in Rust, became `claw-code` — a clean-room implementation capturing architectural patterns without copying proprietary source.

Key details:
- Woke up at 4 a.m. to a "blowing up" phone
- Built the initial Python port with **1 human helper + 10 OpenClaw instances**
- Described the event as a "workflow revelation" — using AI agents to recreate an entire tool in a new language
- Called it a "demo" rather than a product, emphasizing that the code is evidence and the coordination system is the product lesson

## Philosophy

Jin's core thesis (expressed in Claw Code's PHILOSOPHY.md):
- "If you only look at the generated files, you are looking at the wrong layer. The real thing worth studying is the **system that produced them**."
- Humans set direction; "claws" (autonomous coding agents) execute
- The bottleneck has shifted from typing speed to architectural clarity, task decomposition, and judgment

## Related
- [[claw-code]] — Claw Code concept page
- [[yeachan-heo]] — Bellman, collaborator and creator of oh-my-codex
- [[ultraworkers]] — GitHub organization hosting claw-code
