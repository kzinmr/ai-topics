---
name: Samuel Colvin
aliases: [samuelcolvin, sam-colvin, Sam Colvin]
github: https://github.com/samuelcolvin
twitter: "@samuelcolvin"
linkedin: https://www.linkedin.com/in/samuel-colvin-5383251b8
company: Pydantic (Founder & CEO)
location: London, United Kingdom
type: person
depth: L3
status: complete
created: 2026-04-15
last_updated: 2026-04-15
tags:
  - person
  - pydantic
  - pydantic-ai
  - monty
  - logfire
  - rust
  - python
  - ai-agents
  - observability
  - data-validation
  - type-safety
related:
  - "[[concepts/code-mode]]"
  - "[[concepts/harness-engineering]]"
  - "[[concepts/ai-observability]]"
  - "[[concepts/structured-outputs]]"
  - "[[alex-hall]]"
  - "[[david-montague]]"
  - "[[douwe-maan]]"
---

# Samuel Colvin — Creator of Pydantic, Pioneer of Type-Safe AI Agents

## Basic Profile

| Field | Value |
|-------|-------|
| **Name** | Samuel Colvin |
| **Born** | ~1992-1994 (PhD 2020, implies ~1992-94) |
| **Location** | London, United Kingdom |
| **Education** | MSci Mathematics, Imperial College London (2012-2016, First Class Honours); PhD Mathematics, University of Bristol (2016-2020) |
| **PhD Thesis** | "Minimising Hausdorff Dimension under Hölder Equivalence with applications to Hyperbolic Groups" |
| **PhD Funding** | EPSRC + Heilbronn Excellence Award |
| **Supervisor** | Dr. John Mackay |
| **Fields of Study** | Metric Geometry, Fractal Geometry, Geometric Group Theory |
| **Current Role** | Founder & CEO, Pydantic |
| **GitHub** | @samuelcolvin (6.2K followers, 304 public repos) |

## Timeline

### Academic Background (2012–2020)
- **2012–2016**: MSci Mathematics at Imperial College London (First Class Honours)
- **Oct 2015 – May 2016**: Research internship at University of Cambridge with Dr. Eric Keaveny — computational modeling of undulating micro-swimmers (e.g., parasites moving through blood vessels), adapting the model for complex media
- **Sep 2016 – May 2019**: Mathematics Tutor at University of Bristol — organized and ran weekly small-group tutorials for first-year math undergraduates
- **Sep 2016 – May 2020**: PhD in Mathematics at University of Bristol
- **2019**: Published paper "Minimising Hausdorff Dimension under Hölder Equivalence with applications to Hyperbolic Groups"
- **Feb 2021 – Present**: Quantitative Developer at FINBOURNE Technology (London)

### Pydantic Origins (2017–2022)
- **2017**: Began building Pydantic out of frustration that Python type hints "do nothing at runtime." Noticed existing validation libraries (Marshmallow, Django REST framework, Cerberus) all predated the type hints world. Curiosity: *"can we use type annotations to validate data?"* → Yes.
- **Mar 2017**: First PyPI release of Pydantic
- **2018**: python-devtools released — "Python's missing debug print"
- **2019**: aiohttp-toolbox, pytest-toolbox released
- **2020**: arq (async Redis job queues), watchfiles (fast file watching in Rust) released
- **2021**: dirty-equals, buildpg, aioaws released
- **2022**: dnserver (development DNS server), FastUI (React+FastAPI without JS) released

> *"I was working on some project of my own and I wanted to be able to validate data coming back from an API... none of the existing libraries were using type hints because they all predated the type hint world."* — Samuel Colvin, Scaling DevTools podcast

### Company Formation (2023)
- **Feb 16, 2023**: Company announcement — Sequoia-led seed round with participation from Partech, Irregular Expressions, and angel investors Bryan Helmig (Zapier), Tristan Handy (dbt Labs), David Cramer (Sentry)
- **Mar 2023**: Interviewed on Sourcegraph Podcast — discussed Pydantic's growth to 40M+ monthly downloads
- **Apr 2023**: PyCon 2023 — joint appearance with Sebastián Ramírez (FastAPI creator) on Talk Python To Me
- **Jun 30, 2023**: **Pydantic V2 released** — core rewritten in Rust, ~17x faster than V1
- **Jul 2023**: Harrier (static site generator) released

### AI Pivot (2024–2026)
- **Mar 2024**: samuelcolvin-aicli — "OpenAI powered AI CLI in just a few lines of code"
- **mid-2024**: Pydantic AI development begins
- **Oct 1, 2024**: **Pydantic Logfire launched** + $12M Series A from Sequoia
- **Oct 7, 2024**: Pydantic Open Source Fund announced
- **Mar 2025**: OpenAI Agents Framework instrumentation added to Logfire
- **Apr 2, 2025**: Pydantic Evals launched — open-source evaluation framework for AI models
- **Sep 4, 2025**: **Pydantic AI v1.0 released** — "A Predictable & Robust GenAI Framework"
- **Nov 13, 2025**: Pydantic AI Gateway launched
- **Dec 11, 2025**: mcp-run-python released — MCP server to run Python code in a sandbox
- **Dec 2025**: Monty project begins (built "over Christmas" 2025)
- **Feb 2026**: **Pydantic Monty released** — minimal, secure Python interpreter written in Rust for AI agents
- **Feb 17, 2026**: Talked at Latent Space — "Monty: the ultrafast Python interpreter by Agents for Agents"
- **Feb 27, 2026**: Monty blog post published
- **Mar 23, 2026**: Pydantic AI Gateway moving into Logfire
|- **Mar 28, 2026**: pydantic-monty v0.0.9 released
|- **Apr 2026**: Serializable Agents (TOML-defined agents) in development

## Core Philosophy

### 1. Developer Experience as North Star
> *"We've always made developer experience the first priority. And we've leveraged technologies which developers already understand — most notably, Python type annotations."*

Pydantic's success (27.3K GitHub stars, 46M+ monthly PyPI downloads) stems from applying this principle to data validation. The same principle drives Logfire (observability with developer-friendly SQL queries, not vendor dashboards) and Pydantic AI (type-safe agent framework, not another "black box" orchestration layer).

### 2. Type Safety as a Foundation for Reliability
Colvin's mathematical background (geometric group theory, Hölder equivalence) translates into a deep appreciation for **formal structure**. Just as mathematical proofs require rigorous type constraints, he believes AI systems should too:

> *"LLMs work faster, cheaper and more reliably when they write code instead of making sequential tool calls."*

Pydantic AI validates **all** agent inputs, outputs, tool parameters, and dependencies through Pydantic models — the same type annotations that made Pydantic famous now constrain AI agent behavior.

### 3. "Start from Nothing" Security (Monty Philosophy)
Traditional sandboxing starts with a full VM/container and restricts down (whack-a-mole, massive attack surface). Monty inverts this:

> *"Start from nothing, then selectively grant capabilities. The default is zero access — no filesystem, no network, no environment variables, strict resource limits. You explicitly opt in to each capability via external functions that you wrote, you control, and you can audit."*

> *"This is the difference between a firewall that blocks known-bad ports and one that blocks everything, then allowlists specific traffic."*

This is a **capabilities-based security** approach — closer to formal methods in his mathematical training than traditional devops practice.

### 4. Open Source as Strategic Foundation
> *"Pydantic, the open source project, will be a cornerstone of the company... It'll be a key technical component in what we build. It will remain open source and MIT licenced."*

Unlike "open core" companies that withhold critical functionality, Pydantic keeps its core library truly open source (MIT) while building commercial offerings (Logfire platform) on top. This transparency is intentional:

> *"Too many observability companies are abusing the open source label... These products are often missing critical functionality, forcing users onto closed source paid plans once they're locked in. We're different."*

### 5. Graphs for Agent Orchestration
Colvin recognized early that single-agent workflows are insufficient for complex applications:

> *"We were compelled enough by graphs once we got them right, that we actually merged the PR this morning. That means our agent implementation without changing its API at all is now [backed by graphs]. Our agents are technically one of the many graphs you could go and build."* — Latent Space Podcast (Feb 2025)

The Pydantic Graph API (PR #2982, merged Oct 2025 by Douwe Maan and David Montague) provides:
- **Parallel execution**: `g.map()` for fan-out operations on iterables
- **Conditional branching**: Decision nodes with dynamic routing
- **Step-by-step execution**: `graph.iter()` for fine-grained control
- **State persistence**: Serialize execution state for durable workflows

### 6. Serializable Agents (Upcoming)
Colvin announced work on serializing entire agent definitions to TOML files — model, system prompt, tools, dependencies, everything. This enables:
- **Configuration-driven agents**: Define agents without code
- **Portability**: Share agent definitions across environments
- **Version control**: Track agent changes in git

> *"We're about to introduce... serializable agents. So basically you can define an agent entirely in a TOML file. Everything from the model to the system prompt to all of the tools."* — Latent Space (Feb 2026)

## Key Projects

### Pydantic (27.3K ★)
Python data validation using type hints. The library that started it all. Used by FastAPI, SQLModel, LangChain, and virtually every modern Python framework that needs structured data validation.

### Pydantic AI (15.9K ★)
Type-safe Python agent framework. Released Sep 2025, v1.70+ by Mar 2026. Key features:
- Model agnostic (OpenAI, Anthropic, Gemini, DeepSeek, Grok, Cohere, Mistral, Ollama — 15+ providers)
- Structured outputs validated against Pydantic schemas
- Type-safe function tools with automatic parameter validation
- Pydantic AI Graph for complex multi-step agent pipelines
- MCP & A2A protocol support
- Logfire integration (OpenTelemetry-native observability)
- CodeMode support (via Monty)

### Pydantic Monty (6.6K ★, Rust)
Minimal, secure Python interpreter written in Rust for AI agent code execution:
- **Start latency**: 0.004ms (vs Docker 195ms, Sandbox services ~1000ms+)
- **Binary size**: ~4.5MB
- **Memory overhead**: ~5MB when embedded in CPython
- **Security model**: Zero default access, explicit capability grants
- **Language support**: Python (via Rust bytecode VM), TypeScript/JS bindings, Go bindings (in PR), Dart/Kotlin support (in PR)
- **Features**: sync/async functions, closures, comprehensions, f-strings, type hints, dataclasses, pathlib, asyncio
- **State snapshot**: Serialize execution state mid-flight to bytes (single-digit KBs), resume later/elsewhere

### Pydantic Logfire (4.1K ★)
AI observability platform. Python SDK (MIT licensed), platform (closed source). Features:
- OpenTelemetry-native
- Arbitrary SQL queries for data exploration
- AI-specific monitoring (LLM calls, agent traces) + traditional observability
- MCP server support
- Dashboards and metrics
- EU region availability (Mar 2025)

### watchfiles (2.5K ★, Rust)
Simple, modern and fast file watching and code reload for Python, written in Rust.

### python-devtools (1.1K ★)
Development tools for Python — debug prints, formatting, etc.

## The Execution Continuum

Colvin articulates a clear spectrum for AI code execution:

| Approach | Control | Capability | Latency | Cost |
|----------|---------|------------|---------|------|
| **Tool Calling** | High | Low | Sequential round-trips | Per-token |
| **Monty / CodeMode** | High-Medium | Medium | 0.004ms start | In-process |
| **Sandbox Services** (Modal, E2B, Daytona) | Medium | High | ~1000ms+ start | Per-execution |
| **Coding Agents** (Claude Code, Cursor) | Low | Very High | Minutes | High |
| **Full Computer Use** | None | Maximum | Minutes | Very high |

> *"Monty attempts to slot in between simple tool calling which is very safe and relatively easy to implement, doesn't require external infrastructure, but isn't that expressive for the LLM, and sandboxes which are much more expressive, you can do much more powerful things, but they require... the cost is [high]."*

## Connections to Other Leaders

### Andrej Karpathy
Both advocate for **CodeMode** — Karpathy popularized the concept (Anthropic's "computer use" and "code mode" approaches), Colvin built the implementation (Monty). They converge on: LLMs write code → code executes → results return, rather than sequential tool calls.

### Sebastián Ramírez (FastAPI)
Pydantic is FastAPI's validation backbone. The two creators appeared together on Talk Python To Me (Apr 2023) discussing Pydantic V2's Rust rewrite and its impact on FastAPI. Colvin: *"We may have to pause and move, but we'll find out... FastAPI is by far our biggest dependent."*

### Ryan Lopopolo (Harness Engineering)
Colvin's approach to AI agents mirrors Harness Engineering principles: define the environment (Monty), constrain the agent (type safety), observe the results (Logfire), and iterate. Both emphasize developer experience over theoretical purity.

### David Cramer (Sentry)
Angel investor in Pydantic's seed round. Cramer's experience building developer observability tools (Sentry) directly influenced Colvin's thinking on Logfire: *"I've been frustrated by existing logging and monitoring tools for years."*

## Related Wiki Pages

- **Concepts**: [[concepts/code-mode]], [[concepts/harness-engineering]], [[concepts/structured-outputs]], [[concepts/ai-observability]], [[concepts/capabilities-based-security]]
- **Entities**: [[alex-hall]] (Python Dev at Pydantic, Logfire), [[david-montague]] (CTO, Pydantic), [[douwe-maan]] (Pydantic AI Lead), [[sebastián-ramírez]] (FastAPI), [[bryan-helmig]] (Zapier, angel investor)
- **Technologies**: [[concepts/pydantic]], [[concepts/monty-sandbox]], [[concepts/logfire]], [[concepts/pydantic-ai]]

## Sources

- [Pydantic Company Announcement (Feb 2023)](https://pydantic.dev/articles/company-announcement)
- [Pydantic Monty blog post (Feb 2026)](https://pydantic.dev/articles/pydantic-monty)
- [Why is Pydantic building an Observability Platform? (Oct 2024)](https://pydantic.dev/articles/why-logfire)
- [Latent Space: Monty talk (Feb 2026)](https://www.youtube.com/watch?v=nxnQl4AcqFg)
- [Sourcegraph Podcast: Samuel Colvin (Mar 2023)](https://www.buzzsprout.com/1097978/episodes/12479687)
- [Talk Python To Me #415: Future of Pydantic and FastAPI (May 2023)](https://talkpython.fm/episodes/show/415/future-of-pydantic-and-fastapi)
- [Scaling DevTools: Jack Bridger interview with Samuel Colvin](https://www.linkedin.com/posts/jack-bridger-047bb445)
- [StartupHub.ai: Pydantic AI's Samuel Colvin on Building Better LLM Agents](https://www.startuphub.ai/ai-news/artificial-intelligence/2026/pydantic-ai-s-samuel-colvin-on-building-better-llm-agents)
- [Pydantic About Page](https://pydantic.dev/about)
- [GitHub: pydantic/monty](https://github.com/pydantic/monty)
- [LinkedIn: Samuel Colvin](https://linkedin.com/in/samuel-colvin-5383251b8)
