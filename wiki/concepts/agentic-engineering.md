---
title: "Agentic Engineering"
created: 2026-04-09
updated: 2026-04-10
tags: [concept, agentic-engineering, ai-agents, software-engineering]
aliases: ["agentic-coding", "agent-first-development"]
related: [[harness-engineering]], [[vibe-coding]], [[multi-agent-autonomy-scale]], [[context-engineering]]
---

# Agentic Engineering

**Agentic Engineering** is the practice of using AI agents as collaborative development partners — delegating substantial portions of the software development lifecycle to autonomous or semi-autonomous agents while the human engineer shifts from writing code to directing, reviewing, and orchestrating.

The term has been used by multiple influential figures in the AI space, each with slightly different emphases:

## Key Voices & Perspectives

### Andrej Karpathy (@karpathy) — "Agentic Engineering" Coined (Feb 2026)

Karpathy popularized the term in February 2026, describing his transition from "vibe coding" (individual AI assistance) to **managing multiple AI agents in parallel** — giving them tasks, reviewing outputs, and orchestrating workflows.

**Key quotes:**
- "I really am mostly programming in English now, a bit sheepishly telling the LLM what code to write... in words."
- Described the shift as a "magnitude 9 earthquake" for software engineering
- No longer writes handwritten code; delegates entirely to agents

**Karpathy's core observations about agents:**
- **Tenacity**: AI agents never get tired or demoralized
- **Leverage**: "Don't tell it what to do, give it success criteria and watch it go"
- **Fallibility**: Agents make subtle conceptual errors, not syntax errors — they need human oversight
- **Sycophancy**: Agents don't push back when they should
- **Bloat**: Agents tend to overcomplicate code and APIs

**Key questions Karpathy explores:**
1. What happens to the "10X engineer"? — The productivity gap between mean and max engineer may grow enormously
2. Do generalists outperform specialists? — LLMs fill in micro-details; strategy matters more
3. What does LLM coding feel like? — Like playing StarCraft or Factorio?
4. How much of society is bottlenecked by digital knowledge work?
5. What happens when intelligence is ahead of tools, workflows, and organizations?

> [Projects](https://github.com/karpathy) · [Blog](https://karpathy.bearblog.dev/) · [X](https://x.com/karpathy)

### Simon Willison (@simonw) — Agentic Collaboration

Simon Willison discussed agentic engineering on Lenny's Podcast — framing AI agents as **persistent team members** rather than one-off tools.

**Key perspective:**
- Agents as collaborators in the software development process
- Beyond code completion — agents that can plan, execute, and verify tasks
- Human-in-the-loop workflows where agents handle complex multi-step work
- Iterative development with agent feedback loops
- Quality assurance through agent-driven testing

> [Blog](https://simonwillison.net/) · [X](https://x.com/simonw) · [Wiki](../../entities/simon-willison.md)

### Ryan Lopopolo (@_lopopolo) — Harness Engineering

Ryan Lopopolo at OpenAI Frontier popularized **Harness Engineering** — the complementary approach focused on building the systems, structures, and constraints around AI agents to maximize autonomous productivity.

**Key results from OpenAI internal experiment:**
- 5-month experiment building internal beta with **zero human-written code**
- >1,000,000 LOC codebase, thousands of PRs merged
- >1B tokens/day (~$2-3K/day) spent
- 3-person team using GPT-5.0 → 5.4 model progression

**Harness Engineering principles:**
- Zero human-written code (deliberately refuse to write; build structure instead)
- 1-minute build rule (inner loop capped at 1 minute)
- Agent-legible software (optimize codebase for model readability)
- Humans become the bottleneck (shift from reviewing code to building systems and observability)
- Spec-driven development (reasoning-model-led workflows)
- On-code is disposable (no emotional attachment; trash and restart if needed)

Lopopolo also built **Symphony** — an Elixir-based orchestration layer for spinning up, supervising, reworking, and coordinating multiple agents.

> [Blog post on Harness Engineering](https://www.latent.space/p/harness-eng) · [GitHub](https://github.com/lopopolo) · [X](https://x.com/_lopopolo)

### Boris Cherny (@bcherny) — Claude Code, Post-Coding World

Boris Cherny is the creator and head of **Claude Code** at Anthropic. He believes **coding is "solved"** and the focus should shift to what comes next.

**Key perspective:**
- Claude Code grew from terminal prototype to 4% of public GitHub commits
- Advocates for moving beyond individual code writing to agent orchestration
- Emphasizes verification and quality assurance as the new bottleneck
- "Coding is solved" — the challenge shifts to directing and validating agent output

> [Blog](https://borischerny.com/) · [GitHub](https://github.com/bcherny) · [X](https://x.com/bcherny)

### Mike Krieger (@mikeyk) — Anthropic CPO, 90%+ AI-Generated Code

Mike Krieger (Instagram co-founder, now CPO at Anthropic) discussed how Anthropic uses AI to write **90-95% of code** for some products.

**Key observations:**
- AI writes the majority of code at Anthropic
- New bottlenecks emerge: verification, product strategy, and user empathy
- Focus on differentiation rather than competing on raw coding speed
- The role of the engineer shifts from implementation to oversight and product thinking

> [X](https://x.com/mikeyk) · [LinkedIn](https://www.linkedin.com/in/mikekrieger/)

### Addy Osmani (@addyosmani) — Conductors to Orchestrators

Addy Osmani (Engineering Lead at Google, Chrome & Web Platform) has written extensively on the evolution from **conductor to orchestrator** in AI-assisted coding.

**Key articles:**
- "The future of agentic coding: conductors to orchestrators" — explores the distinction between working with a single AI agent (conductor) vs. coordinating multiple agents (orchestrator)
- "Self-Improving Coding Agents" — covers autonomous agent loops (the "Ralph Wiggum technique") for continuous development while sleeping
- "The Code Agent Orchestra" — what makes multi-agent coding work
- "Comprehension Debt" — the hidden cost of AI-generated code
- "Claude Code Swarms" — scaling agent coordination
- "Your AI coding agents need a manager" — the importance of human oversight

**Osmani's key frameworks:**
- **Conductor mode**: Working closely with a single AI agent on a specific task (Claude Code CLI, Gemini CLI, Cursor inline)
- **Orchestrator mode**: Coordinating multiple agents working in parallel (GitHub Copilot Coding Agent, Jules)
- **AGENTS.md**: Persistent context files that carry knowledge across agent sessions
- **Continuous coding loops**: Break development into small tasks, run AI iteratively, validate with tests

> [Blog](https://addyosmani.com/blog/) · [GitHub](https://github.com/addyosmani) · [X](https://x.com/addyosmani)

### Vinci Rufus — "Orchestration > Automation"

Vinci Rufus (tech executive) emphasizes that **"Vibe coding speeds things up 30-70%, while Agentic engineering speeds things up 300-700%."**

**Key principles:**
- "Orchestration > Automation" — system design matters more than raw automation
- Each agent should be specialized (single responsibility principle)
- These two factions are not contradictory but represent different phases of maturity

## The Spectrum: Vibe Coding → Agentic Engineering → Harness Engineering

These approaches form a progression:

| Phase | Human Role | Agent Role | Key Activity |
|-------|-----------|------------|-------------|
| **Vibe Coding** | Writer + reviewer | Assistant | Describe intent, iterate on output |
| **Agentic Engineering** | Director + orchestrator | Collaborator | Delegate tasks, manage multiple agents in parallel |
| **Harness Engineering** | Architect + systems builder | Autonomous worker | Build constraints, evals, and feedback loops for full autonomy |

As Karpathy noted, vibe coding is "past" — the industry is moving toward agentic and harness engineering.

## Common Patterns Across All Voices

1. **Humans shift from writing to directing** — The bottleneck moves from code production to judgment, taste, and verification
2. **Generalists outperform specialists** — LLMs fill in micro-details; strategic thinking matters more
3. **Verification is critical** — Without verification, higher capability is just more confident wrongness
4. **Agent legibility matters** — Code, docs, and workflows should be optimized for model understanding
5. **Multi-agent coordination is the frontier** — Managing fleets of agents, not just one
6. **Disposable code** — No emotional attachment; trash bad output and restart

## Related Concepts

- [[harness-engineering]] — Building systems and constraints around agents
- [[vibe-coding]] — Earlier phase: coding by describing intent in natural language
- [[multi-agent-autonomy-scale]] — Framework for scaling agent coordination
- [[context-engineering]] — Structuring context for effective agent behavior
- [[agentic-coding-swarms]] — Coordinating multiple agents working in parallel

## Sources

- [Karpathy on Agentic Engineering](https://karpathy.bearblog.dev/) (Feb 2026)
- [Simon Willison on Lenny's Podcast](https://www.lennysnewsletter.com/) (2026)
- [Ryan Lopopolo on Harness Engineering](https://www.latent.space/p/harness-eng) (Apr 2026)
- [Boris Cherny on Lenny's Podcast](https://open.substack.com/pub/lenny/p/head-of-claude-code-what-happens) (Feb 2026)
- [Mike Krieger on Lenny's Podcast](https://www.lennysnewsletter.com/p/anthropics-cpo-heres-what-comes-next) (Jun 2025)
- [Addy Osmani: The Future of Agentic Coding](https://addyosmani.com/blog/future-agentic-coding/) (2026)
- [Addy Osmani: Self-Improving Coding Agents](https://addyosmani.com/blog/self-improving-agents/) (2026)
