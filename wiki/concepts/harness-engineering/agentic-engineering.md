---
title: Agentic Engineering
type: concept
slug: agentic-engineering
created: 2026-04-12
updated: 2026-05-26
status: complete
tags:
  - model
  - methodology
  - ai-agents
aliases:
  - ai-coding-agents
  - agentic-workflow
source: https://simonwillison.net/2025/Apr/11/agentic-engineering/
sources:
  - https://paulhoekstra.substack.com/p/agentic-engineering-the-configuration
  - https://paulhoekstra.substack.com/p/agentic-engineering-the-interface
  - https://paulhoekstra.substack.com/p/agentic-engineering-the-orchestration
  - https://paulhoekstra.substack.com/p/agentic-engineering-the-guardrails
  - raw/articles/simonwillison.net--2026-may-11-james-shore--ec8c78b4.md
  - raw/articles/simonwillison.net--2026-may-11-learning-on-the-shop-floor--4f735c2f.md
  - raw/articles/simonwillison.net--2026-may-11-llm-shebang--34efae05.md
---

# Agentic Engineering

> **Definition:** Agentic engineering is the practice of treating AI coding agents (Claude Code, Codex, etc.) as junior team members on a development project. Humans act as supervisors — providing context, direction, and quality review — while AI handles first drafts, repetitive work, and heavy lifting. The goal is not just to produce code faster, but to produce **better** code through systematic workflows.

Based on the concept popularized by Simon Willison's [Agentic Engineering guide](https://simonwillison.net/2025/Apr/11/agentic-engineering/).

---

## Core Principles

### 1. Humans as Supervisors, Not Typists
The engineer's role shifts from writing every line to directing, reviewing, and curating AI output. You provide:
- **Context** — project goals, architecture decisions, constraints
- **Direction** — task breakdown, prioritization, acceptance criteria
- **Quality review** — critical evaluation of every AI-generated change

### 2. AI as a Junior Team Member
Treat the coding agent like a skilled but inexperienced colleague:
- It can draft code quickly but may make subtle mistakes
- It needs clear instructions and good context
- It benefits from examples, style guides, and test cases
- It should be trusted but verified

### 3. Produce Better Code, Not Just More Code
The metric of success is code quality and maintainability, not velocity alone. Agentic workflows should raise the bar — better test coverage, cleaner architecture, more thorough documentation.

### 4. Compound Engineering Loop
Work happens in tight, iterative cycles:
1. Write a failing test (human)
2. Ask agent to make it pass (AI)
3. Review the implementation (human)
4. Iterate or accept (human)
5. Repeat

### 5. Hoard Your Skills
Don't let critical knowledge live only in the agent's context window. Document decisions, save patterns, and maintain human-understandable artifacts. The agent is replaceable; your engineering judgment is not.

---

---

## Paul Hoekstra's 4-Layer Framework (March 2026)

Data engineer [[entities/paul-hoekstra|Paul Hoekstra]] proposed a complementary, more granular framework for agentic engineering organized into four operational layers:

| Layer | Focus | Key Components |
|-------|-------|---------------|
| **1. Configuration** | Behavioral baseline | CLAUDE.md, Skills, `<HARD-GATE>` tags, pre-commit hooks |
| **2. Capability** | Tools & memory | MCP with deferred loading, live docs (Context7, Exa), 3-layer memory |
| **3. Orchestration** | Multi-agent scaling | Subagents, Git worktrees, context compression, Ralph Loop |
| **4. Guardrails** | Security & quality | Permissions system, sandboxing, AST-grep, homoglyph detection |

While Simon Willison's framing focuses on *philosophy and human-side patterns*, Hoekstra's framework is **implementation-focused** — providing concrete file paths, CLI commands, and configuration snippets for each layer.

### Key Distinctions from Willison's Framework
- **Configuration > Vibes:** Hoekstra highlights that *configuration* (not just "good engineering practice") is the critical difference — agents without structured instructions default to "defensive sludge"
- **Layered architecture:** Explicit layer separation mirrors infrastructure design patterns (networking OSI model), making the framework teachable and scalable
- **Security-first:** The Guardrails Layer reflects lessons from the 2026 "OpenClaw" scenario that's largely absent from earlier agentic engineering discourse

### Integration
Willison's patterns (TDD-first, Compound Engineering Loop, Git Integration) complement Hoekstra's layers — they are the *what* while Hoekstra provides the *how* and *where*.

---

## Agentic Engineering vs. Vibe Coding

| Dimension | Agentic Engineering | Vibe Coding |
|---|---|---|
| **Review discipline** | Every line reviewed before merge | Trust the agent, ship it |
| **Testing** | TDD-first, tests written before implementation | Tests skipped or generated as afterthought |
| **Version control** | Frequent commits, clear messages, branch hygiene | Large undifferentiated diffs |
| **Context management** | Systematic — architecture docs, specs, examples | Ad hoc — prompting in isolation |
| **Role of human** | Supervisor, architect, reviewer | Passenger |
| **Goal** | Better code through collaboration | Faster code through automation |
| **Sustainability** | Scales to complex, long-lived projects | Works for prototypes, breaks at scale |

**Key insight:** Vibe coding is what happens when you use AI tools without professional engineering discipline. Agentic engineering applies those same tools *with* the full weight of software engineering practice.

---

## Key Patterns

### TDD-First with AI
The most reliable pattern for agentic work:
1. **Human writes the test** — defines the expected behavior
2. **Agent implements the code** — passes the test
3. **Human reviews** — checks for correctness, edge cases, clarity
4. **Agent refactors** — guided by human feedback

This keeps the human in the driver's seat and the agent focused on well-defined goals.

### Git Integration
- Commit after every meaningful change, no matter how small
- Use descriptive commit messages (agents can draft these for review)
- Review diffs before accepting — don't blindly merge agent output
- Use branches to isolate experimental agent work

### Context Loading
Prime the agent with the right information:
- Project architecture documents
- Coding standards and style guides
- Relevant code examples
- Test patterns already in use
- Known pitfalls and "how we do things here"

### Compound Loops
Chain multiple agent interactions together within a single task:
- Draft → Review → Refine → Test → Review again
- Each loop compounds quality
- Don't accept first-pass output as final

### Spec-Driven Development
Write specifications before asking agents to code:
- Human defines the spec (requirements, interfaces, constraints)
- Agent implements against the spec
- Human validates the implementation matches the spec

This mirrors how good engineering teams work with human developers.

---

## When to Use Agentic Engineering

**Best for:**
- Repetitive but skilled work (boilerplate, migrations, test writing)
- Exploring unfamiliar APIs or libraries
- Refactoring with safety nets (tests catch regressions)
- Documentation generation and maintenance
- Learning new patterns through examples

**Less appropriate for:**
- Novel algorithm design (requires deep domain expertise)
- Architectural decisions (human judgment is irreplaceable)
- Security-critical code (review overhead negates speed gains)
- Projects with zero existing tests (agent output is ungrounded)

---

## The Cost of Abstraction (Xe Iaso Perspective)

[Xe Iaso](https://xeiaso.net/blog/2026/ai-abstraction/) offers a critical examination from the developer perspective on the rising level of abstraction driven by AI.

### 「Fine is the Enemy of Good」

AI-generated code and writing consistently settle at a "fine" level. The problem is that this "fine" quietly lowers human standards. When "fine" becomes the norm, our ability to recognize what is truly "good" atrophies.

> Over-reliance on AI builds immunity to average output and clouds the discernment needed to recognize truly excellent work.

### Loss of Voice (Voice as Non-Negotiable)

As AI-generated communication becomes widespread, **authentic human voice** becomes asymmetrically valuable. Amidst a sea of AI-generated messages, the unique texture, imperfection, and personality of real human writing actually increases in value.

### The Abstraction-Responsibility Trade-off

The cost of developing at high levels of abstraction:
- **Thinning understanding** — Proceeding without understanding how generated code works internally
- **Debugging difficulty** — When problems arise, multiple layers of abstraction must be peeled back
- **Skill hollowing** — Over-reliance on abstraction erodes the ability to solve low-level problems independently

In the context of Agentic Engineering, being mindful of this trade-off and balancing abstraction with understanding is key to sustainable engineering. [[concepts/harness-engineering/agentic-workflows/linear-walkthroughs]] (code explanation generation) is one approach to addressing this issue.

---

## Emerging Practices (May 2026)

### Maintenance Cost Economics — James Shore

Software design expert [James Shore](https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-maintenance-costs) identifies a fundamental economic tension in agentic engineering: **the maintenance-cost multiplier**.

> "Your AI coding agent needs to reduce your maintenance costs. Not by a little bit, either. If you double your output and your cost of maintaining that output stays the same, two times one means you've still doubled your maintenance costs."

This reframes agentic engineering's quality imperative as pure economics — not just "produce better code" but "produce code that's cheaper to maintain." The math is unforgiving: velocity gains must be matched by inverse maintenance cost reductions, or the total cost of ownership increases exponentially ([You Need AI That Reduces Maintenance Costs](https://www.jamesshore.com/v2/blog/2026/you-need-ai-that-reduces-maintenance-costs), via [[entities/simon-willison|Simon Willison]]).

### Case Study: Shopify River (Lehrwerkstatt)

CEO [Tobias Lütke](https://x.com/tobi) describes Shopify's internal coding agent **River**, which operates with a radical public-by-default model in Slack:

- **Public by default**: River refuses DMs. All agent interactions happen in public channels, searchable by any Shopify employee.
- **Lehrwerkstatt (Teaching Workshop)**: The entire shop floor becomes a classroom. 100+ people follow active coding sessions, reacting, adding context, and learning by observation.
- **Osmosis learning**: No curriculum, training plan, or manager needed — just maximum visibility into how colleagues work with AI agents.

This extends agentic engineering to **public agent interactions** — not just sharing code, but sharing the process. [[entities/simon-willison|Simon Willison]] compares it to Midjourney's early success via public Discord channels, where shared prompts compensated for finicky tool interfaces.

### LLM Shebang: Plain-Text as Executable Agent Scripts

A lightweight agentic engineering pattern using `llm` CLI with shebang lines:

```
#!/usr/bin/env -S llm -f
Generate an SVG of a pelican riding a bicycle
```

With tool integration (`-T` flag) and YAML templates defining Python functions inline, plain English text files become executable agent scripts. This represents the simplest possible agentic interface — no harness, no loop, just a natural language prompt as executable code.

Source: [Using LLM in the shebang line of a script](https://simonwillison.net/2026/May/11/llm-shebang/) ([[entities/simon-willison|Simon Willison]])

---

## Further Reading

- [Agentic Engineering](https://simonwillison.net/2025/Apr/11/agentic-engineering/) — Simon Willison
- [My Experience with Claude Code 2.0](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/) — Sankalp
- [Shipping at Inference Speed](https://steipete.me/posts/2025/shipping-at-inference-speed) — Peter Steinberger (@steipete)
- [Agentic Engineering, Part 1: The Configuration Layer](https://paulhoekstra.substack.com/p/agentic-engineering-the-configuration) — Paul Hoekstra
- [Agentic Engineering, Part 2: The Capability Layer](https://paulhoekstra.substack.com/p/agentic-engineering-the-interface) — Paul Hoekstra
- [Agentic Engineering, Part 3: The Orchestration Layer](https://paulhoekstra.substack.com/p/agentic-engineering-the-orchestration) — Paul Hoekstra
- [Agentic Engineering, Part 4: The Guardrails Layer](https://paulhoekstra.substack.com/p/agentic-engineering-the-guardrails) — Paul Hoekstra
- Related concepts: [[concepts/harness-engineering]], [[concepts/harness-engineering/agentic-workflows/compound-engineering-loop]], [[concepts/inference-speed-development]], [[concepts/claude-code/claude-code-best-practices]], [[concepts/context-engineering/context-window-management|Context Window Management]], [[concepts/claude-code/claude-code-source-patterns]], [[concepts/ai-coding-reliability]], [[concepts/harness-engineering/agentic-engineering-configuration-layer]], [[concepts/harness-engineering/agentic-engineering-capability-layer]], [[concepts/harness-engineering/agentic-engineering-orchestration-layer]], [[concepts/harness-engineering/agentic-engineering-guardrails-layer]]

---

*Page created: 2026-04-12 | Status: Complete*
