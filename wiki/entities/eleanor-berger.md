---
title: Eleanor Berger
type: entity
created: 2026-05-29
updated: 2026-08-06
tags:
  - person
  - ai-agents
  - agentic-engineering
  - education
  - coding-agents
aliases:
  - intellectronica
sources:
  - transcripts/2026-05-21_vanishing-gradients_show-us-your-agent-skills-ep3.md
  - raw/articles/2026-03-31_hugobowne_top-questions-about-ai-assisted-software.md
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

### "Top Questions About AI-Assisted Software Development" (Mar 2026)

Eleanor authored the canonical course FAQ as a guest post on [[entities/hugo-bowne-anderson|Hugo Bowne-Anderson]]'s Vanishing Gradients (companion to Vanishing Gradients Ep. 67 with Isaac Flath). The post consolidated recurring course questions into **ten practical questions**, each answered with a short answer + "in practice" playbook. The recurring thesis: *"the teams getting real value from AI are not treating it as magic — they are treating it as engineering."*

| # | Question | Core answer / framework |
|---|----------|-------------------------|
| Q1 | Why do demos look magical while real projects feel harder? | Demos run in low-constraint greenfield settings; production carries hidden context, constraints, and accumulated risk. The misdiagnosis is "model got worse" — the real issue is the task got more constrained while the briefing did not. |
| Q2 | How do I make AI reliable? | Reliability = engineering discipline: be specific, curate context, define success/acceptance criteria, bound scope, verify outside the model. Treat failures as specification bugs, not model stupidity. |
| Q3 | How much context does an agent need? | A **portable context stack** in layers: global rules → repo/project context → external docs → living artefacts (ADRs, specs) → validation checks. Capture intent ("why"), manage the context window deliberately, and treat shared context as org infrastructure. |
| Q4 | What makes a good AI coding specification? | The spec is the contract. **Precise incompleteness** — enough detail to define target and boundaries, enough freedom for the model to solve. Spec-driven development is mostly sequence: think before improvising. Agents can write specs for other agents. |
| Q5 | Which mode, tool, or model? | Four hidden decisions: modality (completion → inline → chat → chat-driven → interactive agentic → async background), execution environment (IDE/CLI/hosted/CI), model (per-phase splits; personal test suites > benchmarks), and cost. "Choose the mode for the task, the model for the phase, the tool for the workflow." |
| Q6 | How do I delegate without losing control? | **Control spectrum** — effective autonomy, not maximal autonomy. Boring safety nets (branches, worktrees, checkpoints, small commits), incremental review, human-after-the-loop for async work. "Trust, but verify." |
| Q7 | How can AI help across the SDLC? | Coding is a small slice: planning/discovery, review, QA, operations (commit messages, CI watching, log parsing), maintenance (docs, release notes, issue triage, dependency updates). "Continuous AI" reduces bottlenecks throughout the lifecycle. |
| Q8 | How do async/parallel agents change the workflow? | Background agents shift AI from babysat tool to task-completing system: true parallelism, SDLC fit, and forced discipline (you cannot intervene mid-run). Reusable async job pattern: trigger → environment → context → spec → execution → output handling (PR/report). |
| Q9 | How do I keep AI-assisted development secure? | Security as architecture, not prompt-writing: Simon Willison's **"lethal trifecta"** (private data + untrusted content + external communication), indirect prompt injection, layered restrictions (network/filesystem/execution), approval fatigue awareness. |
| Q10 | How do I know AI is actually helping? | Measure team efficacy, not personal speed. DORA + SPACE as vocabulary, not religion. Measure what AI *delegates* (automated toil), pick 2-3 actionable metrics (review churn, first-pass yield, escaped defects), build a learning loop, and **give context an owner**. |

The FAQ is a direct articulation of Eleanor's course pedagogy: context engineering, spec-first workflows, async agents, security, and team-scale adoption — all vendor-agnostic.

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
- [[entities/chris-fonnesbeck]] — Fellow agentic engineering commentator; shared ai-safety and agent-skills interests
- [[entities/simon-willison]] — Originator of the "lethal trifecta" security concept
- [[entities/hermes-agent]] — Hermes agent harness
- [[entities/hamel-husain]] — Fellow agent-safety commentator; shared ai-safety and coding-agents interests
- [[entities/hugo-bowne-anderson]] — Vanishing Gradients host; published her course FAQ guest post (Mar 2026)
- [[entities/isaac-flath]] — Co-creator of Elite AI Assisted Coding course; Vanishing Gradients Ep. 67 co-guest
- [[concepts/agentic-engineering]] — Agentic engineering patterns
- [[concepts/spec-driven-development]] — Spec-as-contract practice (Q4 of the course FAQ)
- [[concepts/ai-assisted-development]] — AI-assisted development practice (home of the 10-question playbook)
