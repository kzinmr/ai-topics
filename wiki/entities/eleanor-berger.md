---
title: Eleanor Berger
type: entity
created: 2026-05-29
updated: 2026-05-29
tags:
  - person
  - ai-agents
  - agent-skills
  - agentic-engineering
  - education
  - coding-agents
aliases:
  - intellectronica
sources:
  - transcripts/2026-05-21_vanishing-gradients_show-us-your-agent-skills-ep3.md
  - https://maven.com/agentic-ventures/ai-coding
  - https://agentic-ventures.com/
  - https://okigu.com/eleanor
  - https://intellectronica.net/
---

# Eleanor Berger

**Eleanor Berger** is an AI and software engineering expert, creator of **Agentic Ventures** and the *Elite AI-Assisted Coding* course. A former principal engineering lead at **Microsoft** and **Google**, she now works as a Technical Member of Staff at **Jiminy Health** (AI for mental health) and advises companies through **OKIGU**. She is known for teaching technically rigorous, hype-free agentic engineering.

## Overview

| Field | Detail |
|-------|--------|
| **Current Role** | Technical Member of Staff @ Jiminy Health |
| **Previous** | Principal Engineering Lead @ Microsoft, Google |
| **Founded** | Agentic Ventures, OKIGU |
| **Notable Work** | Elite AI-Assisted Coding course, agentic engineering education |
| **Agent** | Hermes harness on Mac Mini (agent named "Fnord") |
| **Stack** | Codex app, GPT-5.5, Warp Terminal, Hermes |
| **Languages** | Tool-agnostic: TypeScript, Go, Rust, Python (increasingly less) |

## Key Contributions

### Elite AI-Assisted Coding (Agentic Ventures)
A course teaching developers and engineering leaders to adopt AI-powered software development with confidence. Covers the full spectrum from inline completions to autonomous multi-step agents, context management, specification-driven development, and background async agents. Testimonials from senior Microsoft engineers attest to its depth and practical rigor.

### OKIGU Advisory
Advises companies on building robust AI capability, integrating advanced AI systems, and delivering solutions that drive business value. Focus: sustainable AI-engineering muscle, opportunity assessment, data-driven delivery frameworks.

### Jiminy Health
Recently joined to work on AI for mental health — applying agentic workflows to sensitive clinical domains.

## Show Us Your (Agent) Skills Episode 3 (2026-05-21)

Eleanor shared her **"letting go" YOLO approach** with Hermes on a Mac Mini and her agent ecosystem:

### Hermes Agent "Fnord" (~157 skills)
- **Infrastructure**: Running on repurposed M1 Mac Mini, connected via Tailscale, segregated from work systems
- **Discord-first interaction**: Uses Discord threads for responsive agent communication; also WhatsApp, CLI, and API server
- **GPT-5.5 as unlock**: GPT-5.5's improved base model made Hermes dramatically more effective — "It's fantastic"
- **Auto-publishing HTML**: Skill integrates with "Here Now" (HTML publishing service like gists for web pages) — creates dozens of HTML pages daily
- **Self-written skills**: Watch-later skill was invented by the agent itself when Eleanor asked for YouTube summaries; the agent designed caching, browser automation, and summary generation autonomously
- **Style without design knowledge**: Uses "Impeccable" design skill to produce polished HTML pages despite having no design expertise — "I'm the main customer, I just look at it"

### The Lethal Trifecta (Simon Willison)
Eleanor actively manages the security triad:
1. Access to private data
2. Ability to externally communicate  
3. Exposure to untrusted content

She limits internet access as much as possible and keeps the agent segregated on a separate Mac Mini, especially critical given her work with clinical data at Jiminy Health.

### Intelligent Steps Inside Deterministic Scripts
- **Cron jobs with judgment**: Hermes excels at knowing when a cron job needs deterministic scripting vs. LLM invocation — not every scheduled task needs to burn tokens
- **One intelligent step**: Pattern of embedding a single LLM call inside otherwise deterministic workflows (e.g., release note drafting for spaCy — deterministic git operations, insert LLM step for prose generation)
- **Verification over code review**: For cloud infrastructure work, verification means inspecting what actually runs (YAML → cloud footprint), not AI-reviewing-AI. "I need to see what it did like the actual cloud footprint"

### Philosophy
- **Agent as exoskeleton**: Works best when she knows "a little bit" — enough to evaluate confidently but not enough to write syntax from memory. In unfamiliar domains, agents don't help.
- **Scope is the unsolved problem**: Agents understand intent well but struggle with scope — write a novel when you want a one-pager, or a paragraph when you need comprehensive review.
- **Tool agnosticism**: Deliberately switches between Codex, Open Code, Copilot to ensure configurations remain tool-agnostic
- **Language agnosticism**: No longer Python-only; agents write in whatever language works — verification is at the output level

### Stack Evolution
- Moved away from VS Code — "I opened it instinctively but never edited files directly"
- Primary: Codex app + GPT-5.5 + Warp Terminal
- Experimenting with Zed for lighter editing
- Python usage dropped significantly — harder to work with agents in Python

## Related
- [[entities/matthew-honnibal]] — spaCy founder; Episode 3 co-guest; security discussion on HTML smuggling in skills
- [[entities/simon-willison]] — Originator of the "lethal trifecta" security concept
- [[entities/hermes-agent]] — Hermes agent harness
- [[entities/hugo-bowne-anderson]] — Vanishing Gradients host
- [[concepts/agentic-engineering]] — Agentic engineering patterns
