---
title: Agentic Engineering Patterns
type: concept
status: active
created: 2026-02-23
updated: 2026-04-12
related:
  - concepts/evals
  - concepts/harness-engineering
  - concepts/ai-agent-traps
  - entities/simon-willison
  - entities/andrej-karpathy
tags:
  - agentic-engineering
  - coding-agents
  - anthropic
  - testing
  - developer-tooling
  - person
source: https://simonwillison.net/guides/agentic-engineering-patterns/
sources: []
---

# Agentic Engineering Patterns

A guide project launched by Simon Willison on February 23, 2026. It systematizes practical patterns for getting the best results from coding agents (Claude Code, OpenAI Codex, Gemini CLI, etc.).

> "I use the term **agentic engineering** to describe the practice of developing software with the assistance of coding agents."
> — Simon Willison

Originally mentioned in the December 2025 article "2025 in AI: The Year Everything Changed", the term was developed into an independent guide in February 2026. Structured as 15 chapters across 6 sections.

## Definitions

**Coding Agent**: An agent capable of both generating and executing code. Examples: Claude Code, OpenAI Codex, Gemini CLI.

**Agent**: "Agents run tools in a loop to achieve a goal" — a loop where prompts and tool definitions are given to an LLM, the LLM requests tool calls, and results are returned to the LLM.

**Agentic Engineering**: The practice of developing software with the assistance of coding agents. Unlike Vibe coding (coined by Karpathy in February 2025), it aims for **reviewed, production-quality code**.

---

## Section 1: Principles

### 1. What is agentic engineering?
- Writing code is not the only activity of a software engineer
- The essence is deciding "**which code to write**"
- Every problem has multiple solutions, each with trade-offs
- LLMs don't learn from past mistakes, but **coding agents can learn** — by intentionally updating instructions and tool harnesses
- Agents are a means to amplify human ambition

### 2. Writing code is cheap now
- The cost of writing code has approached near-zero, but "**good code**" still costs
- Definition of good code:
  - Works correctly, executes intended behavior without bugs
  - Is verified to work (tests, etc.)
  - Solves the right problem
  - Handles error cases properly (not just happy paths)
  - Is simple and minimal (YAGNI principle)
  - Is protected by tests
  - Is properly documented
  - Is designed to withstand future changes
  - Satisfies relevant "-ilities" (accessibility, testability, reliability, security, maintainability, observability, scalability, usability)
- New personal and organizational habits must be built
- Before following the intuition that "it's not worth the time," try prompting in an async agent session first

### 3. Hoard things you know how to do
- Know what is possible, what is not, and how to achieve it
- Working code demonstrations are the strongest asset
- Simon's assets: Blog, TIL, 1000+ GitHub repos, tools.simonwillison.net (HTML tools collection), simonw/research
- **Recombining Pattern**: Combine 2+ existing working examples to build something new
  - Example: PDF.js + Tesseract.js → browser-based OCR tool
- Coding agents make this pattern even more powerful

### 4. AI should help us produce better code
- AI is not just for writing code faster, but for producing **better code**
- Avoid technical debt
- Delegate tedious work (tests, documentation, refactoring) to coding agents
- AI tools enable evaluating more options
- **Compound Engineering Loop**: Prototype → Test → Refactor → Document → Improve

### 5. Anti-patterns
- **Inflicting unreviewed code on collaborators**: Imposing unreviewed code on team members
- Prevent degradation of quality standards

---

## Section 2: Working with coding agents

### 1. How coding agents work
- **Large Language Models**: Foundation technology
- **Chat templated prompts**: Prompt structuring
- **Token caching**: Cost optimization
- **Calling tools**: Tool invocation mechanism
- **The system prompt**: Agent behavior definition
- **Reasoning**: Leveraging reasoning capabilities
- **LLM + system prompt + tools in a loop**: The complete agent loop picture

### 2. Using Git with coding agents
- **Git essentials**: Integrating agents with Git
- **Core concepts and prompts**: Git prompt patterns for agents
- **Rewriting history**: Safe history rewriting

### 3. Subagents
- **Claude Code's Explore subagent**: Delegating research tasks
- **Parallel subagents**: Efficiency through parallel execution
- **Specialist subagents**: Leveraging specialized agents
- **Official documentation**: Reference official docs for each agent

---

## Section 3: Testing and QA

### 1. Red/green TDD
Do test-driven development with agents. The test-first approach leads agents to write more concise and reliable code.

### 2. First run the tests
Run existing tests first to establish a baseline before making changes.

### 3. Agentic manual testing
- **Mechanisms for agentic manual testing**: How agents can perform manual testing
- **Using browser automation for web UIs**: UI testing with browser automation
- **Have them take notes with Showboat**: Record test results with Showboat

---

## Section 4: Understanding code

### 1. Linear walkthroughs
Linear code explanations. Examples using Showboat and Present.

### 2. Interactive explanations
Interactive code explanations. Understanding via word clouds example.

---

## Section 5: Annotated prompts

### GIF optimization tool using WebAssembly and Gifsicle
Annotated real-world prompt examples, including follow-up prompt patterns.

---

## Section 6: Appendix

### Prompts I use
Simon Willison's actual prompt collection:
- **Artifacts**: Artifact generation prompts
- **Proofreader**: Proofreading prompts
- **Alt text**: Alt text generation prompts
- **Podcast highlights**: Podcast highlight extraction prompts

---

## Guide Format

Simon implemented a new content type "**Guide**" on his Django site for this project:
- A Guide is a collection of chapters
- Each chapter is essentially a blog post, but with date de-emphasized
- Intended to be **updated** over time (not fixed at initial publication)
- The Guide/Chapter/ChapterChange models and Django views were written with **Claude Opus 4.6 + Claude Code for web** (via iPhone)

## Related Projects

- **simonw/research**: A repository for having coding agents research problems and produce working code + reports
- **tools.simonwillison.net**: Collection of LLM-assisted tools and prototypes
- **HTML tools**: Single HTML pages with embedded JavaScript and CSS that solve specific problems

## References

- [Agentic Engineering Patterns Guide](https://simonwillison.net/guides/agentic-engineering-patterns/)
- [Writing about Agentic Engineering Patterns](https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/)
- [2025 in AI: The Year Everything Changed](https://simonwillison.net/2025/Dec/31/2025-in-ai/) — First mention of the term
- [Hoard things you know how to do](https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/)

## See Also

- [[concepts/harness-engineering]]
- [[concepts/agentic-rag]]
- [[concepts/chaos-engineering]]
- [[concepts/memory-systems-design-patterns]]
- [[concepts/meta-harness]]
