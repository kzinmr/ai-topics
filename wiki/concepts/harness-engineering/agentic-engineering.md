---
title: Agentic Engineering
type: concept
slug: agentic-engineering
created: 2026-04-12
updated: 2026-05-02
status: complete
tags:
  - ai
  - engineering
  - workflows
  - agents
aliases:
  - ai-coding-agents
  - agentic-workflow
source: https://simonwillison.net/2025/Apr/11/agentic-engineering/
sources:
  - https://paulhoekstra.substack.com/p/agentic-engineering-the-configuration
  - https://paulhoekstra.substack.com/p/agentic-engineering-the-interface
  - https://paulhoekstra.substack.com/p/agentic-engineering-the-orchestration
  - https://paulhoekstra.substack.com/p/agentic-engineering-the-guardrails
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

## 抽象化コストの考察（Xe Iasoの視点）

[Xe Iaso](https://xeiaso.net/blog/2026/ai-abstraction/)はAIによる抽象化レベルの上昇について、開発者視点での重要な批判的考察を提供している。

### 「Fine is the Enemy of Good」

AIが出力するコードや文章は常に「まあまあ良い（fine）」レベルで安定している。問題は、この「fine」が人間の基準を静かに低下させること。「fine」が当たり前になると、本当に「良い（good）」ものを見分ける能力が萎える。

> AIに慣れすぎると、平均的な出力に免疫ができ、本当に優れたものを見極める目が曇る。

### 声の喪失（Voice as Non-Negotiable）

AIによるコミュニケーションが一般化すると、**人間らしい「声」**が非対称に貴重になる。大量のAI生成メッセージの中で、本物の人間の文章は持つ独特のテクスチャー、不完全さ、個性がむしろ価値を増す。

### 抽象化と責任のトレードオフ

高い抽象化レベルで開発することの代償：
- **理解の希薄化** — 生成されたコードの内部動作を理解しないまま進む
- **デバッグ困難** — 問題が起きた時、何層もの抽象化を剥がす必要がある
- **スキルの空洞化** — 抽象化に依存しすぎると、低レベルの問題を自力で解決できなくなる

Agentic Engineeringの文脈では、このトレードオフを意識し、抽象化と理解のバランスを取ることが持続可能なエンジニアリングの鍵となる。[[concepts/harness-engineering/agentic-workflows/linear-walkthroughs]]（コード解説の生成）は、この問題への一つの対処法である。

---

## Further Reading

- [Agentic Engineering](https://simonwillison.net/2025/Apr/11/agentic-engineering/) — Simon Willison
- [My Experience with Claude Code 2.0](https://sankalp.bearblog.dev/my-experience-with-claude-code-20-and-how-to-get-better-at-using-coding-agents/) — Sankalp
- [Shipping at Inference Speed](https://steipete.me/posts/2025/shipping-at-inference-speed) — Peter Steinberger (@steipete)
- [Agentic Engineering, Part 1: The Configuration Layer](https://paulhoekstra.substack.com/p/agentic-engineering-the-configuration) — Paul Hoekstra
- [Agentic Engineering, Part 2: The Capability Layer](https://paulhoekstra.substack.com/p/agentic-engineering-the-interface) — Paul Hoekstra
- [Agentic Engineering, Part 3: The Orchestration Layer](https://paulhoekstra.substack.com/p/agentic-engineering-the-orchestration) — Paul Hoekstra
- [Agentic Engineering, Part 4: The Guardrails Layer](https://paulhoekstra.substack.com/p/agentic-engineering-the-guardrails) — Paul Hoekstra
- Related concepts: [[concepts/harness-engineering]], [[concepts/harness-engineering/agentic-workflows/compound-engineering-loop]], [[concepts/inference-speed-development]], [[concepts/claude-code-best-practices]], [[concepts/context-window-management]], [[concepts/claude-code-source-patterns]], [[concepts/ai-coding-reliability]], [[concepts/harness-engineering/agentic-engineering-configuration-layer]], [[concepts/harness-engineering/agentic-engineering-capability-layer]], [[concepts/harness-engineering/agentic-engineering-orchestration-layer]], [[concepts/harness-engineering/agentic-engineering-guardrails-layer]]

---

*Page created: 2026-04-12 | Status: Complete*
