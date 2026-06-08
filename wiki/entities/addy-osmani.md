---
title: Addy Osmani
type: entity
created: 2026-04-10
updated: 2026-06-03
source: "x-account"
tags:
  - person
  - x-account
  - model
  - coding-agents
  - web-development
  - developer-experience
  - google
sources: []
---


# Addy Osmani

| | |
|---|---|
| **X/Twitter** | [@addyosmani](https://x.com/addyosmani) |
| **Blog** | [addyosmani.com](https://addyosmani.com/) |
| **Role** | Director, Google Cloud AI (Gemini & Vertex AI) |
| **Previously** | Engineering Lead, Google Chrome & Web Platform |

## Bio

Addy Osmani is a Director at Google Cloud AI, working on Gemini and Vertex AI. Previously, he was Engineering Lead for Chrome & Web Platform at Google, where he became one of the most prolific writers and speakers on web performance, developer experience, and AI-assisted coding. He has 86K+ followers on Medium and regularly speaks at major conferences including O'Reilly CodeCon.

Osmani is the most **prolific systematizer** of agentic coding patterns — he doesn't just use AI coding tools, he builds frameworks, taxonomies, and playbooks for how teams should adopt them.

## Core Ideas

### Conductor → Orchestrator Framework

Osmani's signature contribution is the distinction between two modes of AI-assisted development:

| Mode | Description | Tools |
|------|-------------|-------|
| **Conductor** | Working closely with a *single* AI agent on a specific task. Synchronous, real-time guidance. Micro-level control. | Claude Code CLI, Gemini CLI, Cursor inline |
| **Orchestrator** | Coordinating *multiple* AI agents working in parallel. Asynchronous, macro-level oversight. Planning, task decomposition, output verification. | Agent Teams, Conductor by Melty Labs, Codex Web, Jules |

> "You used to pair with one AI. Now you manage an agent team."

### 8 Levels of AI-Assisted Coding

Adapted from Steve Yegge's developer evolution framework, Osmani maps the progression:

- **L1-L4 (IDE Era)**: No AI → Agent with permissions → YOLO mode → Agent-assisted
- **L5-L8 (Agentic Era)**: Subagents → Agent teams → Orchestration at scale → Full autonomous pipelines

Most developers are stuck at L3-L4. The orchestration tier starts at L6.

### Agent Teams (Swarms)

Osmani was an early advocate of **multi-agent coordination patterns** and documented Claude Code's Agent Teams feature when it launched:

- **Core insight**: LLMs perform worse as context expands — splitting work across specialized agents is more effective than one giant context window
- **Sweet spot**: 3-5 teammates per task; beyond that, coordination overhead dominates
- **Quality gates**: Plan approval → hooks → token budgets → human review
- **Pattern**: Dedicated @reviewer agent per 3-4 builders; lead only sees green-reviewed code

### The Factory Model

Osmani's production-line approach to agentic development:

1. **Plan** — Write specs, define acceptance criteria
2. **Decompose** — Break into self-contained units with clear boundaries
3. **Assign** — Delegate to specialized agents (frontend, backend, tests)
4. **Review** — Automated quality gates + human oversight
5. **Compound** — Learnings feed back into the system for continuous improvement

### Self-Improving Coding Agents

Osmani documented the "Ralph Wiggum technique" — setting up agents to iteratively improve code while the human sleeps:

- Break development into small, self-contained tasks
- Run AI agents asynchronously in parallel
- Validate outputs with automated tests
- Feed failures back as new tasks

### AGENTS.md Critique

In "Stop Using /init for AGENTS.md" (Mar 2026), Osmani argued that:

- Auto-generated AGENTS.md files **hurt agent performance** and inflate costs by 20%+
- They encode noise as signal — directory structures and file listings are redundant with what agents can read
- AGENTS.md should be a **living list of codebase smells you haven't fixed yet**, not permanent configuration
- Before adding any line: "Can the agent find this by reading the code? If yes, don't write it"
- Treat context engineering as **agile** — prune aggressively, encode only non-obvious conventions

### The 70% Problem

Osmani identified a critical limitation of AI-generated code, popularized in Tim O'Reilly's landmark 2025 article: AI can handle the first 70% of a project (scaffolding, documentation, initial prototype) but the final 30% requires "hard-won engineering wisdom" to prevent "house of cards code" that collapses under real-world pressure.

This framing has become a widely cited cautionary concept in the vibe coding debate — the gap between AI's impressive initial output and production-grade quality.

| Phase | AI's Role | Human's Role |
|-------|-----------|-------------|
| First 70% | Scaffolding, documentation, prototyping | Direction setting, requirements |
| Final 30% | Limited (edge cases struggle) | Engineering judgment, architecture decisions, quality assurance |

### Comprehension Debt

Osmani identified a hidden cost of AI-generated code:

- **Comprehension debt** accumulates when developers can't understand code they didn't write
- The risk of multi-agent systems is producing large quantities of code *very quickly* — but that code still needs to be right, maintainable, and actually solving the problem
- **Activity ≠ value** — commits per minute is a vanity metric
- "Let the problem guide the tooling, not the other way around"

### The High-Leverage Developer of 2026

> "The high-leverage developer of 2026 is an async-first manager running parallel AI agents. The developers who will be most productive aren't the ones who write the most code — they're the ones who best decompose problems, specify intent, and verify outcomes."

## Agent Harness Engineering (April 2026)

Osmani published a comprehensive synthesis of the harness engineering movement in "[Agent Harness Engineering](https://addyosmani.com/blog/agent-harness-engineering/)" (April 2026), pulling together threads from multiple voices (Vivek Trivedy, Dex Horthy, HumanLayer, Anthropic Engineering, Birgitta Böckeler) into a unified framework.

Key contributions from this article:

| Concept | Description |
|---------|-------------|
| **The Ratchet** | Every agent mistake becomes a permanent fix — constraints are added on real failures, removed when models internalize the capability |
| **Working Backwards from Behavior** | Design methodology: "Behavior we want → Harness design to achieve it" — every component must trace to a specific behavioral requirement |
| **Hooks as Enforcement Layer** | Before-tool-call, after-file-edit, and before-commit hooks that block destructive actions silently but inject errors verbosely |
| **Tool Discipline** | Ten focused tools beat fifty overlapping ones — sloppy external integrations (unverified MCP servers) inject bad prompts before the agent starts |
| **Harness-as-a-Service (HaaS)** | Industry transition from LLM APIs (completions) to Harness APIs (runtimes) — select, configure, focus on domain logic |
| **Convergence Dynamic** | Top coding agents look more like each other than their underlying models do — harness patterns are converging on load-bearing scaffolding |
| **Harnesses Don't Shrink, They Move** | Better models don't eliminate scaffolding — outdated complexity is replaced with new scaffolding for newly-reachable tasks |
| **Post-Training Feedback Loop** | Models are post-trained with specific harnesses, creating tight coupling between model and harness design |

## Key Publications

| Title | Date | Platform |
|-------|------|----------|
| Agent Harness Engineering | Apr 2026 | addyosmani.com |
| The Future of Agentic Coding: Conductors to Orchestrators | Nov 2025 | O'Reilly Radar + addyosmani.com |
| Claude Code Swarms | Feb 2026 | addyosmani.com |
| The Code Agent Orchestra | Mar 2026 | O'Reilly CodeCon + addyosmani.com |
| Self-Improving Coding Agents | 2026 | addyosmani.com |
| Your AI Coding Agents Need a Manager | 2026 | addyosmani.com |
| Stop Using /init for AGENTS.md | Mar 2026 | Medium + addyosmani.com |
| Orchestrating Coding Agents (talk) | Mar 2026 | O'Reilly CodeCon 2026 |
| 2026 Agentic Coding Trends Guide | 2026 | addyosmani.com |

## Speaking

- **O'Reilly CodeCon 2026** (Mar 26) — "Orchestrating Coding Agents: Patterns for Coordinating Agents in Real-World Software Workflows"
- Regular speaker on AI-assisted development, web performance, and developer experience

## X/Twitter Activity Pattern

Osmani uses X to:
- Announce new **frameworks and patterns** for agentic coding
- Share **practical tips** from his daily work with Claude Code, Gemini, and other tools
- Engage with the **developer community** on tool adoption, quality concerns, and productivity metrics
- Cross-post his **blog articles** with distilled takeaways
- Respond to **emerging trends** (agent swarms, AGENTS.md debate, multi-agent coordination)

His posting style is **educational and systematic** — he builds frameworks, creates cheat sheets, and produces structured guides rather than hot takes.

## Open Source & Projects

- Extensive contributions to **Chrome DevTools** and web performance tooling
- Author of **Learning JavaScript Design Patterns** (O'Reilly)
- Contributor to numerous open-source web development tools

## Related

- [[lester-solbakken]] — Search infrastructure researcher; HORNET founder
- [[concepts/harness-engineering]]
- [[concepts/multi-agent-autonomy-scale]]
- [[concepts/context-engineering]]
- [[entities/boris-cherny]]
- [[entities/ryan-lopopolo]]
- [[concepts/karpathy]]
- [[entities/simon-willison]]

## Sources

- [The Future of Agentic Coding](https://addyosmani.com/blog/future-agentic-coding/) (Nov 2025)
- [Claude Code Swarms](https://addyosmani.com/blog/claude-code-agent-teams/) (Feb 2026)
- [The Code Agent Orchestra](https://addyosmani.com/blog/code-agent-orchestra/) (Mar 2026)
- [Stop Using /init for AGENTS.md](https://medium.com/@addyosmani/stop-using-init-for-agents-md-3086a333f380) (Mar 2026)
- [O'Reilly CodeCon 2026 Talk Slides](https://talks.addy.ie/oreilly-codecon-march-2026/) (Mar 2026)
- [Addy Osmani's Blog](https://addyosmani.com/)
