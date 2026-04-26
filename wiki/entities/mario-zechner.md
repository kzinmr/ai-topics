---
title: Mario Zechner
type: entity
handle: "@badlogicgames"
created: 2026-04-10
updated: 2026-04-10
tags:
  - person
  - x-account
  - game-development
  - ai
  - local-llm
  - open-source
  - systems-programming
  - kotlin
sources: []
---


# Mario Zechner (@badlogicgames)

| | |
|---|---|
| **X** | [@badlogicgames](https://x.com/badlogicgames) |
| **Blog** | [mariozechner.at](https://mariozechner.at) |
| **GitHub** | [badlogic](https://github.com/badlogic) |
| **Role** | Independent software developer, coach, angel investor; creator of libGDX |
| **Known for** | libGDX (game development framework), Spine runtimes, civic tech projects, local LLM experimentation, pi coding agent |
| **Bio** | Austrian independent software developer with 15+ years of experience in applied machine learning, data science, compiler engineering, and computer graphics. Creator of libGDX, one of the most widely used Java game development frameworks. Also known for civic tech projects (Cards for Ukraine, Heisse Preise price tracker) and his recent work on local LLM engineering and minimal coding agents. |

## Overview

Mario Zechner is one of the most distinctive voices in the tech industry — a veteran game developer, systems programmer, and civic technologist who brings an engineer's pragmatism and a craftsman's eye to everything he builds. His career spans academia (PhD in computer science), commercial game development (libGDX, Spine runtimes), civic technology (Cards for Ukraine, Heisse Preise grocery price tracker), and most recently, local LLM engineering.

Zechner is best known as the creator of **libGDX**, a Java-based game development framework that has been used to ship thousands of games across desktop, mobile, and web platforms. libGDX's design philosophy — cross-platform compatibility, performance, and developer accessibility — reflects Zechner's broader approach to software engineering: build tools that work well, are easy to understand, and solve real problems.

In 2022, Zechner shifted his focus toward civic technology and AI. His projects during this period include:
- **Cards for Ukraine** — Automated €50 grocery voucher distribution for Ukrainian refugees in Austria (€259,000+ donated, 5,269+ families assisted)
- **Heisse Preise** — Open-source grocery price tracker that exposed Austrian inflation patterns and prompted government action
- **AMS Berufsinfomat Replica** — A ~400-line RAG chatbot built in 2 nights that outperformed the government's €464,000 official system

Most recently, Zechner has emerged as a leading voice in **local LLM engineering**. His blog at mariozechner.at features deeply technical analysis of coding agents, prompt engineering, and the practical challenges of running AI models on consumer hardware. His project **pi** (a minimal coding agent) represents his philosophy applied to AI: strip away the bloat, control the context, and treat the LLM as a tool rather than a collaborator.

## Core Ideas

### LLMs as "Shitty General-Purpose Computers"

Zechner's most influential framing is treating LLMs as slow, unreliable computers that you program with natural language. In his essay "Prompts are code, .json/.md files are state" (June 2025), he argues:

> "Thinking of LLMs as Shitty General Purpose Computers — this is a weird form of metaprogramming: we write 'code' in the form of prompts that execute on the LLM to produce the actual code. Prompts are code, .json/.md files are state."

This metaphor is deliberately unflattering but practically useful. It forces engineers to confront the reality that LLMs:
- Are slow (relative to compiled code)
- Are unreliable (they hallucinate, make mistakes, lose context)
- Don't have persistent state between invocations
- Require structured input/output to work effectively

The solution isn't to pretend LLMs are magic — it's to engineer around their limitations with deterministic workflows, structured state, and human checkpoints.

### Context Engineering Over Model Chasing

Zechner is deeply skeptical of the race to larger models and context windows. His approach focuses on **engineering the context** that models receive:

> "What we need when using coding agents on bigger codebases is a structured way to engineer context. By that I mean: keep only the information needed for the task of modifying or generating code, minimize the number of turns the model needs."

His work on the Spine runtime porting project demonstrates this philosophy. Rather than asking an LLM to "port this Java code to C++," he built a structured program (`port.md`) with:
- Pre-generated state (`porting-plan.json`) tracking progress
- Language-specific conventions files
- Human checkpoints after each type port
- Incremental compilation testing
- `jq`-based state updates for resumption

This approach treats the LLM as a function within a larger deterministic system, not as the system itself.

### Minimal Agent Architecture

Zechner's **pi** coding agent (November 2025) embodies his philosophy of minimalism:

> "If I don't need it, it won't be built."

Key design principles:
- **Minimal system prompt** (<1000 tokens total)
- **No arbitrary step limits** — the agent loops until the model stops calling tools
- **Full filesystem access by default** — "security theater is ineffective; if the LLM can read/write/exec/network, isolation (containers) is the only real defense"
- **Complete session observability** — every interaction is logged and post-processable
- **Cross-provider compatibility** — works with OpenAI, Anthropic, Google, and self-hosted models

This stands in sharp contrast to the "spaceship" agents (Claude Code, Cursor, etc.) that Zechner criticizes for bloated system prompts, hidden context injection, and poor observability.

### Civic Technology as Proof of Concept

Zechner's civic projects demonstrate that **small, focused software can have outsized impact**. His AMS Berufsinfomat replica (~400 lines, €30/month server) handled more requests than the government's €464,000 system:

> "Anyone who tells you it's more complex than that is full of shit. Anyone who tells you they will 'train the AI based on your data' is also full of shit."

His Heisse Preise grocery price tracker started as a 70-line script comparing discount store prices. It was cited in Austrian parliament within 2 weeks and prompted the Competition Authority to recommend mandatory retailer APIs, legal frameworks for comparison platforms, and standardized product metadata — none of which have been implemented.

### The RAG Skeptic

Zechner is one of the most clear-eyed critics of RAG (Retrieval-Augmented Generation) hype. His AMS Berufsinfomat replica used a basic RAG architecture:

```
You are a helpful assistant, capable of answering questions about different professions.
You will be given supplementary information and a user question.
You will answer the user questions only based on the supplemental information.
```

His conclusion: RAG works for simple QA tasks but fails on complex reasoning, and its limitations are often hidden by marketing. He advocates for understanding the actual architecture (automated search + prompt injection) rather than treating RAG as a magic solution.

## Key Work

### libGDX
A Java-based game development framework supporting desktop, Android, iOS, and HTML5. Features:
- Cross-platform rendering (OpenGL ES)
- Physics integration (Box2D)
- Audio, input, and file I/O abstractions
- Active community with hundreds of shipped games
- One of the most widely used Java game frameworks

### Spine Runtimes
2D skeletal animation software runtimes for multiple platforms (C, C++, C#, Java, Haxe, TypeScript, etc.). Zechner maintains the runtimes and has used his porting methodology (structured LLM programs with human checkpoints) to migrate between versions efficiently.

### Cards for Ukraine (2022)
Automated grocery voucher distribution for Ukrainian refugees in Austria:
- €259,000+ donated
- 5,269+ families assisted
- 100% transparent financial tracking
- Built in 5 days (May 10–15, 2022)
- Handled association setup, bank negotiations, bulk discounts, web portal, label printing, deduplication

### Heisse Preise (Grocery Price Tracker)
Open-source scraper and comparison tool exposing Austrian grocery inflation:
- Started as a 70-line script
- Cited in Austrian parliament within 2 weeks
- Prompted BWB (Competition Authority) recommendations for mandatory retailer APIs
- Averages ~600 daily unique visitors
- Used strategically to funnel engagement into Cards for Ukraine donations

### pi — Minimal Coding Agent (2025)
A stripped-down coding agent built around four components:
- **pi-ai** — Unified LLM API with multi-provider support, streaming, TypeBox validation
- **pi-agent-core** — Agent loop with tool execution, validation, event streaming
- **pi-tui** — Terminal UI with differential rendering and synchronized output
- **pi-coding-agent** — CLI with session management, AGENTS.md context, custom themes

### AMS Berufsinfomat Replica (2024)
A ~400-line RAG chatbot that replicated the Austrian government's job information system at a fraction of the cost. Demonstrated that the government's €464,000 system could be built in 2 nights on a €30/month server.

## Blog / Recent Posts

- **"I've sold out"** (April 8, 2026) — Personal reflection on selling equity or compromising principles for financial security. Candid discussion of the tension between idealism and pragmatism in software development.
- **"Thoughts on slowing the fuck down"** (March 25, 2026) — Essay on the importance of deliberate, unhurried development. Arguments against the startup hustle culture and in favor of sustainable, long-term building.
- **"What I learned building an opinionated and minimal coding agent"** (November 30, 2025) — Deep technical analysis of the pi coding agent project. Covers provider abstraction realities, TUI design choices, agent architecture, and lessons from building a minimal tool in a bloated ecosystem.
- **"Armin is wrong and here's why"** (November 22, 2025) — Direct response to claims that LLM APIs are secretly a state synchronization problem requiring local-first/CRDT solutions. Argues that messages are a fundamental abstraction and local-first principles only apply client-side.
- **"What if you don't need MCP at all?"** (November 2, 2025) — Critique of the MCP (Model Context Protocol) hype. Argues that simple tool-call patterns are often sufficient and that MCP adds unnecessary complexity for many use cases.
- **"Prompts are code, .json/.md files are state"** (June 2, 2025) — Foundational essay on treating LLMs as slow, unreliable computers. Introduces the structured context engineering methodology that underpins much of Zechner's subsequent work.
- **"Boxie — an always offline audio player for my 3 year old"** (April 26, 2025) — Personal project building a child-safe, offline audio player. Demonstrates Zechner's approach to building practical, privacy-first tools for real-world use cases.
- **"MCP vs CLI: Benchmarking Tools for Coding Agents"** (August 15, 2025) — Comparative analysis of different approaches to giving coding agents access to tools and external systems.
- **"macOS code injection for fun and no profit"** (July 20, 2024) — Technical deep-dive into macOS code injection techniques. Reflects Zechner's ongoing interest in systems-level programming and understanding how software actually works.
- **"Two years in review"** (July 15, 2024) — Comprehensive summary of Zechner's work from May 2022 to July 2024, covering civic tech projects, AI experiments, rapid prototyping, and open-source contributions.

## Related People

- **[[will-mcgugan]]** — Both build terminal-based tools for developer productivity; McGugan's Rich/Textual/Toad and Zechner's pi-tui represent different approaches to the same problem space
- **[[bryan-bischof]]** — Both skeptical of AI hype; Bischof's R.I.P. grep and Zechner's AMS replica critique represent complementary approaches to cutting through marketing claims
- **Antirez (Salvatore Sanfilippo)** — Shared philosophy of minimalism and simplicity in systems design; both advocate for readable, understandable code over complex abstractions
- **Georgi Gerganov** — Creator of llama.cpp; Zechner frequently references and builds on llama.cpp for local LLM inference
- **André Staltz** — Fellow skeptic of protocol hype; Zechner's "What if you don't need MCP at all?" echoes Staltz's critique of over-engineered solutions
- **Spine (Esoteric Software)** — Zechner's employer for the Spine runtime project; 2D skeletal animation software used across games and applications

## X Activity Themes

- **Local LLM engineering** — Practical analysis of running AI models on consumer hardware, quantization, and inference optimization
- **Coding agent critique** — Skeptical examination of tools like Claude Code, Cursor, and OpenClaw; advocacy for minimal, observable architectures
- **Civic technology** — Discussion of projects like Cards for Ukraine and Heisse Preise; advocacy for using technical skills to solve real-world problems
- **Systems programming** — Deep technical posts about macOS internals, code injection, compiler engineering, and low-level optimization
- **Open-source advocacy** — Promotion of transparent, community-driven development; criticism of vendor-locked solutions
- **Anti-hype commentary** — Consistent pushback against overblown AI claims, protocol hype (MCP), and the "next big thing" narrative
- **Personal reflections** — Essays on fatherhood, slowing down, and finding meaning in software development beyond commercial success
