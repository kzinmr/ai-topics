---
title: "The Agentic Software Factory"
author: Hugo Bowne-Anderson
date: 2026-05-27
source_url: https://hugobowne.substack.com/p/the-agentic-software-factory
newsletter: Vanishing Gradients (Substack)
type: article
tags: [agentic-engineering, agent-skills, verification, personal-software, code-review, memory-systems]
---

# The Agentic Software Factory

**Planning, memory, verification, and personal software from builders using agents every day.**

By Hugo Bowne-Anderson, May 27, 2026

> "The difference between vibe coding and agentic engineering is planning, architecture, and caring about the output." — Wes McKinney riffing on Jesse Vincent, ep-1 @ 11:51

## Overview

First episode of **Show Us Your Agent Skills** live show featuring:
- **Wes McKinney** (creator of pandas, POSIT) — automated code review with RoboRev, parallel project management
- **Jeremiah Lowin** (Prefect) — second brain workflow with OpenClaw, personal software (Cardboard, Prefab)
- **Randy Olson** (Good Eye Labs) — generator-evaluator pattern for data visualization

Hosts: Thomas Wiecki and Hugo Bowne-Anderson

## Two Key Themes

1. **Verification** — Once agents produce more work than you can personally inspect, how do you check it? Wes automates code review; Randy encodes visual judgment into a self-critiquing skill.
2. **Personal software** — Jeremiah's Cardboard, OpenClaw memory, and Wes's local tooling are all built for one user's workflow. Agents make bespoke software newly cheap.

## Wes McKinney — How to Review a Million Lines of AI-Generated Code

- Generates ~1M lines of code every 6 months across ~12 projects, 1.3-1.4B tokens/day
- **RoboRev** daemon runs as post-commit hook, reviews every commit via Codex (GPT 5.5, reasoning xHigh)
- Code read by agents 4-5 times minimum before PR merge
- Generates with ~3:1 mix of Claude Code and Codex
- Usage: $21,765.80/month at API rates

### Stack
- **RoboRev**: post-commit code review daemon
- **Agents View**: search across hundreds of sessions
- **Middleman**: local GitHub replacement ("GitHub is in leagues with big scroll")
- **Kata**: local issue tracker (after Beads "destroyed some of my Git repositories")
- **Superpowers**: spec interviews in parallel across git worktrees

### Principles
- **Slow plan, long implement** — detailed spec interview before coding; single plan ran 14 hours with 45 tasks
- **Commit every turn** — hard rule in CLAUDE.md and AGENTS.md
- **RoboRev reads every line; you read for structure** — "I almost don't read code now"
- **Drain the ledger inline** — invoke roborev-fix every 5 tasks in long plans

### Key Quotes
- "I'm thinking about ideas for how I could turn this into more of an automated software factory... but I'm bandwidth limited in terms of my ability to make decisions throughout the day."
- "It's sort of this balance between, do you want to be productive or do you want to be safe? And I think right now, to be maximally productive with agents requires you to be a little bit unsafe."

## Jeremiah Lowin — Using an Agent as a Second Brain

- Starts workdays with a voice memo (commute or home office)
- Drops transcript into **OpenClaw** memory substrate
- Agents work in background reading from same memory layer
- Picks up threads via memory substrate weeks later

### Principles
- **Feed the brain before you need it** — morning voice memo as daily system prompt
- **Pick a substrate whose memory you can edit** — chose OpenClaw specifically for editable memory
- **Pick one tool for thinking, another for coding** — OpenClaw for thinking/planning, Claude Desktop and Codex Desktop for coding

### Skills Architecture
- Skills are markdown files with frontmatter: name + description
- Description always visible to agent; body hidden until invoked
- Progressive disclosure is "the magic of skills"
- **ship-it**: polite note saying "ship it" means open a PR, not merge
- **explain**: 80-line markdown skill, referenced by every other skill; asks for guided tour, rules out failure modes

### MCP vs CLI
- "Skills are awesome ways to steer behavior... MCPs are great ways to distribute business logic from a central place"
- "Overwhelmingly, the use case for MCP is distributing internal business logic to internal teams in enterprises"

### Personal Software
- **Cardboard**: slide software (acts → beats → slides), read-only UI, driven via MCP from OpenClaw voice memos
- **Prefab**: Python front-end framework for MCP apps, no backend required, spun out of FastMCP

## Randy Olson — Building a Skill That Grades Its Own Work

- Publishes a data-viz post every morning from a single high-signal chart workflow
- Skill pulls data, sketches variants, grades output against Tuftean criteria
- **Generator-evaluator pattern**: deterministic Python verifier + LLM-as-Tuftean-judge

### Principles
- "You don't want to just tell it what to do, you also want to tell it how to check it"
- Deterministic checks (DPI, file integrity) in scripts; judgment calls (annotation placement, data-to-ink ratio) to LLM
- "Even still, if an eval flips or is wrong 80% of the time, it's still directionally valuable"

### Three Skill Design Principles
1. **Skills are polite notes, not programs** (Jeremiah's framing)
2. **Deterministic in scripts, ambiguous to the LLM** (Randy's framing) — "A skill plus an LLM is kind of a program"
3. **Skills are living documents** — "The skills are really the thing that can evolve with you"

## Links
- Show website: https://showusyouragent.com
- Companion repo with skills, configs, workflows
- Full episode: ~2 hours
