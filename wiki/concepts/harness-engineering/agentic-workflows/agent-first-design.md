---
title: "Agent-First Codebase Design"
type: concept
aliases:
  - agent-first-design
  - agent-friendly-code
  - ai-first-architecture
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - agentic-engineering
  - architecture
status: draft
sources:
  - "https://steipete.me/posts/2025/shipping-at-inference-speed"
---

# Agent-First Codebase Design

A philosophy of designing codebases for **"AI agents to work in efficiently"** rather than for "humans to navigate easily."

## Core Principles

> *"I don't design codebases to be easy to navigate for me, I engineer them so agents can work in it efficiently. Fighting the model is often a waste of time and tokens."*
> — Peter Steinberger

Traditional code design prioritized "being easy for humans to read and understand." In the agent era, **"being precisely operable by agents"** becomes equally or more important.

## Why Agent-First

| Dimension | Human-Centered Design | Agent-Centered Design |
|------|------------|-------------------|
| Primary Goal | Readability & expressiveness | Operational reliability |
| Navigation | Relies on IDE search & jump features | Guided by file structure & naming conventions |
| Refactoring | Large-scale changes in one go | Split small, step-by-step |
| Testing | Coverage-focused | Emphasized as agent self-verification mechanism |
| Documentation | Comprehensive README | Structured `CLAUDE.md`/`AGENTS.md` |

## Practical Patterns

### 1. Clear File Structure

Agents infer context from file hierarchy and naming conventions.

```
project/
├── CLAUDE.md          # Project-wide instructions and constraints
├── AGENTS.md          # Agent development guide
├── docs/
│   ├── architecture.md # System design intent
│   └── patterns.md    # Usage patterns collection
├── src/
│   ├── core/          # Stable core logic
│   ├── features/      # Feature-specific modules
│   └── utils/         # Utilities
└── tests/
```

### 2. Self-Descriptive Naming

> *"Good naming is better than comments for agents."*

- Function name: `fetchUserById()` → `fetchUserById_orReturnNull()`
- File name: `auth.ts` → `auth-middleware.ts`
- Variable name: `data` → `userProfileResponse`

### 3. Small, Independent Modules

Reading a large file at once consumes agent context. Splitting into small modules:
- Reduces token usage
- Makes impact scope identification easier
- Makes delegation to sub-agents easier

### 4. Executable Tests

For agents, tests are "documentation" and "safety nets."

- Tests passing = changes are safe
- Tests failing = something broke
- Writing tests = clarifying specifications

### 5. Structured Instruction Files

Provide structured information in `CLAUDE.md` or `AGENTS.md`:
- Project purpose
- Technology stack
- Coding conventions
- Patterns to avoid
- References to existing solutions

## Steipete's Practical Examples

Peter Steinberger designs codebases for agents as follows:

- **Go for CLI**: Type system is simple and easy for agents to handle
- **TypeScript for Web**: Ecosystem is mature, abundant training data for agents
- **Maintain `docs/` per project**: Context source for agents to read
- **Force-load relevant docs via scripts**: Ensure agents obtain necessary information before working

## Differences from Human-Centered Design

Agent-First design is **not a rejection** of human-centered design. The two are complementary:

| | Human-Centered | Agent-First | Common Ground |
|---|---------|------------|--------|
| Naming | Emphasizes meaning | Makes operation results explicit | Both pursue clarity |
| Structure | Separation of concerns | Token efficiency | Modularity is key |
| Documentation | Background & intent | Procedures & constraints | Both are needed |
| Testing | Quality assurance | Self-verification mechanism | Automation is assumed |

## Related Concepts

- [[concepts/context-engineering/context-window-management|Context Window Management]] — Understanding agent context constraints
- [[concepts/harness-engineering/agentic-workflows/how-agents-work]] — How agents work internally
- [[concepts/harness-engineering/agentic-workflows/cli-first-development]] — CLI-first development pattern
- [[concepts/agentic-engineering]] — Higher-level concept

## References

-  — Proponent of Agent-First Design- [Shipping at Inference-Speed](https://steipete.me/posts/2025/shipping-at-inference-speed)
