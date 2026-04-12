---
title: Agentic Engineering
slug: agentic-engineering
status: complete
tags:
  - ai
  - engineering
  - workflows
  - agents
aliases:
  - ai-coding-agents
  - agentic-workflow
created: 2026-04-12
updated: 2026-04-12
source: https://simonwillison.net/2025/Apr/11/agentic-engineering/
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

## Further Reading

- [Agentic Engineering](https://simonwillison.net/2025/Apr/11/agentic-engineering/) — Simon Willison
- Related concepts: [[test-driven-development]], [[ai-pair-programming]], [[compound-engineering]]

---

*Page created: 2026-04-12 | Status: Complete*
