---
title: "Agentic Engineering"
created: 2026-05-14
updated: 2026-05-14
type: concept
tags:
  - concept
  - agentic-engineering
  - ai-agents
  - agent-skills
  - verification
  - coding-agents
  - developer-tooling
sources:
  - raw/articles/2026-05-12_hugobowne_agentic-engineering-verification.md
  - raw/articles/2026-05-08_vanishing-gradients_show-us-your-agent-skills-ep1.md
---

# Agentic Engineering

**Agentic engineering** is the disciplined practice of building software using AI agents as primary contributors, with verification — not manual code reading or writing — as the critical skill. It represents the evolution from "vibe coding" (ad-hoc, unverified agent output) to systematic, quality-assured agent-driven development.

## Definition

Agentic engineering treats AI agents as software factory workers that generate, review, test, and verify code continuously. The human engineer's role shifts from **writing code** to **designing verification systems** and **orchestrating agent workflows**.

As [[entities/wes-mckinney]] describes it:

> "I almost don't read code now... Roborev reads every line of code that is generated. It gets read multiple times. And so, whenever I push up a pull request, the branch gets re-reviewed. By the time I'm merging a pull request into a repository, the code has all been read by agents four or five times minimum."

## Core Principles

### 1. Verification over Reading

The central shift: stop reading code manually and start building agentic verification pipelines. This includes:

- **Background code reviewers** (e.g., [[entities/roborev]] — a GPT-5.5 daemon that reviews every commit)
- **Generator-evaluator workflows** — one agent generates, another evaluates
- **Verifier skills** — embedding domain-specific quality rules (e.g., Tufte's data viz principles) as LLM-evaluable checks

### 2. Skills as Thin Drivers

Skills are minimal wrappers that call tools, not fat abstractions. Key design patterns:

- **Progressive disclosure** — reveal complexity only when needed
- **Explain skill as anchor** — a meta-skill that sets tone and expectations
- **Reflect and improve** — skills that self-evaluate and iterate

### 3. Software Factories, Not Solo Coding

[[entities/wes-mckinney]]'s setup: parallel agents running RoboRev (reviewer), Agents View (session DB), Middleman (dashboard), Kata — generating 1M+ lines in 6 months for spicytakes.org.

### 4. Context Engineering as "Second Brain"

[[entities/jeremiah-lowin]]'s approach: voice memos → transcribed → fed into agent memory substrate each morning. The "memory substrate" is what makes agents consistently useful across sessions.

### 5. Ephemeral "Just-for-Me" Software

Agents make throwaway tools viable — tools built for a single task, used once, and discarded. This was previously economically infeasible.

## Contrast with Vibe Coding

| Dimension | Vibe Coding | Agentic Engineering |
|-----------|-------------|---------------------|
| Code reading | Human reads everything | Agents read everything (4-5x) |
| Verification | Manual, spot-checked | Systematic, agentic, continuous |
| Code writing | Human still writes | Agents generate, humans architect |
| Quality | Variable, ad-hoc | Built into workflow via verifier skills |
| Scale | One person, one agent | Software factory with parallel agents |
| Memory | Ephemeral chat context | Persistent memory substrate |

## Key Practitioners

- **[[entities/wes-mckinney]]** — Software factory with RoboRev, Agents View, Middleman. 1M+ lines generated.
- **[[entities/jeremiah-lowin]]** — Second brain architecture, voice memo pipeline, explain skill anchor
- **[[entities/randy-olson]]** — Tufte-encoding verifier skills, digital twin thought partner, generator-evaluator workflows
- **[[entities/garry-tan]]** — "Fat Skills, Fat Code, Thin Harness" architecture
- **[[entities/hugo-bowne-anderson]]** — Documenting and teaching agentic engineering through Vanishing Gradients

## Key Tools and Projects

- [[entities/roborev]] — Background code reviewer daemon (GPT-5.5)
- [[entities/superpowers]] — Skills framework (Jesse Vincent)
- [[entities/fastmcp]] — MCP tooling framework
- [[entities/prefab]] — Generative UI DSL in Python
- [[entities/opencode]] — Agent harness with deep memory customization
- [[entities/openclaw]] — Agent harness for memory management

## Related Concepts

- [[concepts/agent-skills]] — Reusable patterns for coding agents
- [[concepts/code-review-agents]] — Background verification daemons
- [[concepts/context-engineering]] — Building agent memory substrates
- [[concepts/harness-engineering]] — Building thin agent harnesses
- [[concepts/generator-evaluator-workflow]] — Generator-evaluator architecture
