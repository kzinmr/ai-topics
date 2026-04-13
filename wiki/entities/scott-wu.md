---
title: "Scott Wu"
type: entity
tags: [cognition, devin, ceo, agentic-engineering, competitive-programming]
aliases: ["scott-wu-cognition"]
related:
  - "concepts/cognition-devin-philosophy"
  - "concepts/closing-agent-loop"
  - "entities/walden-yan"
  - "entities/nader-dabit"
sources:
  - "https://cognition.ai/blog/introducing-devin"
  - "https://cognition.ai/blog/devin-2-2"
  - "https://cognition.ai/blog/dont-build-multi-agents"
  - "https://sfstandard.com/2026/03/24/grind-sf-startup-racing-build-ai-software-engineer/"
  - "https://www.dwarkesh.com/p/dylan-patel"
  - "https://www.youtube.com/watch?v=YwmQzWGyrRQ"
  - "https://nader.substack.com/p/how-cognition-uses-devin-to-build"
  - "https://x.com/scottwu46"
updated: 2026-04-13
---

# Scott Wu (@scottwu46) — Cognition CEO & Co-Founder

| | |
|---|---|
| **Role** | CEO & Co-Founder, Cognition AI |
| **Organization** | Cognition AI (formerly Cognition Labs) — applied AI lab building autonomous AI software engineers |
| **Location** | San Francisco Bay Area |
| **Born** | ~1996 (age 29 as of 2025) |
| **Education** | Harvard University (Computer Science, dropped out after 2 years) |
| **Notable Achievements** | 3× IOI Gold Medalist, Forbes 30 Under 30 (2019, for Lunchclub) |
| **X/Twitter** | [@scottwu46](https://x.com/scottwu46) |
| **LinkedIn** | [scottwu](https://linkedin.com/in/scottwu) |
| **Years Active** | 2014 – Present |

## Overview

Scott Wu is the CEO and co-founder of **Cognition AI**, the company behind Devin — widely recognized as the first production-grade autonomous AI software engineer. Wu is a former competitive programming prodigy who won **three gold medals at the International Olympiad in Informatics (IOI)**, and has built a company culture centered around elite technical talent and extreme execution speed.

Under Wu's leadership, Cognition grew from a 10-person "nerdy group project" to a $10B+ company with offices in San Francisco, New York, Austin, and London, serving enterprise customers including Goldman Sachs, Citi, NASA, and Ramp.

Wu dropped out of Harvard after two years to pursue startup building, first co-founding the social platform **Lunchclub** (2019) before pivoting to AI with Cognition in late 2023.

## Timeline

| Date | Event |
|------|-------|
| ~2011–2014 | Wins 3 gold medals at International Olympiad in Informatics (IOI) |
| 2014–2016 | Works at Addepar as a young software engineer |
| 2016–2017 | Brief hiatus from competitive programming |
| 2019 | Co-founds Lunchclub (social platform), recognized in Forbes 30 Under 30 |
| Late 2023 | Co-founds Cognition AI with Steven Hao and Walden Yan |
| Mar 2024 | Launches Devin 1.0 — first AI software engineer; achieves 13.86% on SWE-bench |
| Apr 2024 | Raises $21M Series A led by Founders Fund |
| 2025 | Grows to 40+ employees; publishes "Don't Build Multi-Agents" (Walden Yan) |
| Nov 2025 | Wu publicly evaluates Claude Opus 4.5 — "stronger results on our hardest evals" |
| Late 2025 | Cognition raises $400M at $10B+ valuation (Founders Fund-led) |
| Feb 2026 | Nader Dabit joins Cognition as Growth Engineer |
| Mar 2026 | Cognition merges 659 Devin PRs/week (up from 154 in 2025); profiled in SF Standard |
| Apr 2026 | Acquires Codeium/Windsurf; Devin reaches general availability |

## Core Philosophy

### "The Future of Software Engineering Is Telling Your Computer What to Build"

Wu's philosophy centers on the belief that **AI should augment human engineers, not replace them**. He frames Devin as a "tireless, skilled teammate" rather than a replacement for developers:

> *"This would be a lot less fun for us to do if we thought that we were making ourselves irrelevant. We're working toward giving everyone their own buddy, Devin, who can go and build out their ideas for them into real software."* — SF Standard interview (Mar 2026)

### Extreme Performance Culture

Cognition operates with what Wu describes as an **"extreme performance culture."** The company attracts competitive programming champions — the founding team collectively holds 10 IOI gold medals. Wu has said:

> *"It's been a hackathon for like the last year and a half... one of the crazy things is we have a lot of people who came from this Olympiad background in math."* — American Optimist podcast

### Closing the Agent Loop

Wu enagents that handle the **full software development lifecycle** autonomously:

1. Write code
2. Run tests and catch CI failures
3. Autofix review comments
4. Merge PRs without human intervention

> *"Devin can now close the loop — no human needed for PR reviews."* — Devin 2.2 announcement

> *"Eventually, the future comes."* — Devin 2.2 release tweet

### Alignment with Multi-Agent Skepticism

Wu's public statements align closely with Walden Yan's "Don't Build Multi-Agents" thesis. The company favors **single-threaded agents with context continuity** over naive parallel agent architectures, though Cognition has developed a "conditional multi-agent" system ("Managed Devins") where a primary agent orchestrates subagents with full context traces.

## Background: Competitive Programming to AI

Wu's path to AI was unconventional. Growing up in **Baton Rouge, Louisiana** as the son of Chinese immigrants, he first gained attention with a national **Mathcounts championship** before dominating in competitive programming. His trajectory:

1. **Mathcounts national champion** → **3× IOI Gold** (one of the most decorated American competitive programmers)
2. **Addepar** (2014–2016): Early professional experience at a fintech startup
3. **Harvard University** (2016–2018): Studied Computer Science, but dropped out to build Lunchclub
4. **Lunchclub** (2019–2023): Social networking platform, Forbes 30 Under 30 recognition
5. **Cognition AI** (2023–present): Full-time focus on autonomous AI software engineering

The competitive programming background deeply influences Cognition's engineering culture. Wu has repeatedly stated that the same skills that win IOI medals — **deep problem-solving, algorithmic thinking, and rapid iteration under constraints** — are the exact skills needed for building reliable AI agents.

## Cognition AI

### Founding Story

Cognition began in late 2023 when Wu and two friends (Steven Hao, Walden Yan) recognized that two technological advances had converged:

1. **AlphaGo-style reinforcement learning** — showing AI could master complex tasks through trial and error
2. **Transformer architecture** — enabling training on vast code and text corpora

They asked: *"Could a machine not just answer questions but take on tasks and complete them on its own?"*

### Devin: The AI Software Engineer

Devin is Cognition's flagship product — an autonomous AI agent that can:
- Plan and execute complex engineering tasks requiring thousands of decisions
- Recall relevant context at every step and learn over time
- Use a full sandboxed compute environment (shell, code editor, browser)
- Collaborate with humans through real-time progress reporting and feedback

**SWE-bench Performance:** In March 2024, Devin achieved **13.86%** on SWE-bench (unassisted), far exceeding the previous state-of-the-art of 1.96%. Even when given the exact files to edit, the best previous models resolved only 4.80%.

### Enterprise Adoption

By April 2026, Devin is deployed at:
- **Goldman Sachs** — piloting autonomous coding agents
- **Citi** — rolling out Devin to 40,000+ developers
- **Ramp** — using Devin for internal tooling
- **Cal.com** — production use for feature development
- **NASA** — research and prototyping
- **Stripe** — 1,000+ agent-written PRs merged per week (with internal systems)

### Company Growth

| Metric | 2024 | 2025 | 2026 |
|--------|------|------|------|
| Employees | ~10 | ~40 | 100+ |
| Weekly PRs (Cognition internal) | — | 154 | 659 |
| Valuation | ~$500M | ~$2B | $10B+ |
| Offices | 1 (SF) | 2 (SF, NYC) | 4 (SF, NYC, Austin, London) |

## Key Quotes

> *"This would be a lot less fun for us to do if we thought that we were making ourselves irrelevant."* — On why AI agents won't make human engineers obsolete

> *"Eventually, the future comes."* — Devin 2.2 announcement

> *"Devin can now close the loop — no human needed for PR reviews."* — On autonomous development cycles

> *"If you're not using AI, you are just slower."* — American Optimist podcast

## Related

- [[cognition-devin-philosophy]] — Cognition's approach to building AI agents
- [[managed-devins]] — Conditional multi-agent architecture
- [[closing-agent-loop]] — Full development cycle automation
- [[entities/walden-yan]] — Cognition co-founder, context engineering advocate
- [[entities/nader-dabit]] — Cognition growth engineer, cloud agent thesis

## Sources

- [Introducing Devin](https://cognition.ai/blog/introducing-devin) — Cognition AI (Mar 2024)
- [Devin 2.2](https://cognition.ai/blog/devin-2-2) — Cognition AI (Sep 2025)
- [Don't Build Multi-Agents](https://cognition.ai/blog/dont-build-multi-agents) — Walden Yan, Cognition AI (Jun 2025)
- [Inside the grind: The SF startup racing to build an AI software engineer](https://sfstandard.com/2026/03/24/grind-sf-startup-racing-build-ai-software-engineer/) — SF Standard (Mar 2026)
- [From Math Prodigy to AI Genius: How Scott Wu Built Devin](https://www.youtube.com/watch?v=YwmQzWGyrRQ) — American Optimist Podcast
- [How Cognition Uses Devin to Build Devin](https://nader.substack.com/p/how-cognition-uses-devin-to-build) — Nader Dabit (Feb 2026)
- [Engineering for Agents That Never Sleep](https://nader.substack.com/p/engineering-for-agents-that-never) — Nader Dabit (Mar 2026)
- [The Cloud Agent Thesis](https://nader.substack.com/p/the-cloud-agent-thesis) — Nader Dabit (Feb 2026)
