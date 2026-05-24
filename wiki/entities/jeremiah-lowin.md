---
title: Jeremiah Lowin
type: entity
entity_type: person
status: L2
created: 2026-05-14
updated: 2026-05-24
tags:
  - person
  - ai-agents
  - agent-skills
  - context-engineering
  - developer-tooling
  - open-source
  - mcp
  - prefect
sources:
  - https://www.jlowin.dev/about
  - https://github.com/jlowin
  - https://jlowin.dev/blog/fastmcp-3
  - https://jlowin.dev/blog/fastmcp-3-launch
  - https://jlowin.dev/blog/fastmcp-3-2
  - https://github.com/PrefectHQ/fastmcp/releases/tag/v3.3.0
  - https://jlowin.dev/blog/prefab
  - https://jlowin.dev/blog/ten-years-of-real-good-coffee
  - https://hugobowne.substack.com/p/agentic-engineering-and-the-lost
  - https://www.prefect.io/blog/how-jeremiah-lowin-turned-a-life-long-question-into-an-industry-leading-startup
  - https://news.ycombinator.com/item?id=47697566
  - https://www.youtube.com/watch?v=oVopa_3uZdo
  - https://softwareengineeringdaily.com/2026/04/07/fastmcp-with-adam-azzam-and-jeremiah-lowin/
description: "Founder & CEO of Prefect (data/AI workflow orchestration). Creator of FastMCP (standard Python MCP framework). Built Prefab (generative UI DSL), Cardboard (ephemeral presentation tool). Strategic adviser to Spotify, Positive Sum, OSV. Global Ambassador of Compass Coffee."
---

# Jeremiah Lowin

**Jeremiah Lowin** (@jlowin) is the Founder & CEO of **Prefect**, a data and AI workflow orchestration platform. He is the creator of **FastMCP**, the most popular Python framework for building [[concepts/model-context-protocol-mcp|Model Context Protocol (MCP)]] servers and clients (~25K GitHub stars). He is a leading voice in [[concepts/agent-skills|agent skills]], [[concepts/context-engineering|context engineering]], and [[concepts/generative-ui|generative UI]].

Based in Washington, DC, Lowin's work sits at the intersection of data engineering, AI agents, and developer tooling. His tagline: *"Mostly harmless."*

## Career

### Early Career & Risk Management
Before founding Prefect, Lowin spent his career overseeing risk and data for some of the largest buy-side investment firms in the world. His background is in **statistics and machine learning**. He attended **Harvard University**.

He was a **founding PMC member of Apache Airflow**, the widely-used open-source workflow scheduler, giving him deep insight into the limitations of existing orchestration tools — and the motivation to build something better.

### Prefect (2018–present)
In 2018, Lowin founded **Prefect** (Prefect Technologies, Inc.), a Python-based orchestration platform that empowers data teams to build resilient, adaptable data pipelines and workflows. Key aspects:

- **Philosophy**: Prefect was founded with an obsession on *failure*. Lowin argued that "when an automated workflow fails, it can be catastrophic" — so Prefect was designed to be maximally helpful when code crashes, not just when it succeeds.
- **Co-founder**: Chris White, introduced by a mutual friend, became Prefect's first employee and now serves as CTO.
- **Scale**: Prefect orchestrates *a millennium* of compute every month.
- **FastMCP integration**: In February 2026, FastMCP moved from Lowin's personal GitHub (`jlowin/fastmcp`) to `PrefectHQ/fastmcp`, becoming a core pillar of Prefect's **Horizon** platform.
- **Advisory**: Lowin serves as a strategic adviser to **Spotify**, **Positive Sum** (Prefect investor), and **OSV**.

### Marvin (2023)
Lowin open-sourced **Marvin** (~6K GitHub stars), a framework for AI engineering that introduced *AI Functions* — minimalist functions with no source code that generate typed outputs using AI. Described as "no-code... in your code."

### ControlFlow (2024, archived)
A Python framework for building agentic AI workflows, later archived as focus shifted to FastMCP and Prefect's Horizon platform.

## Key Agentic Work

### FastMCP
**FastMCP** is Lowin's most impactful open-source contribution to the AI agent ecosystem. Built "over a weekend in late 2024," it has become the *standard Python framework* for working with the [[concepts/model-context-protocol-mcp|MCP protocol]]:

- **v2.6 (Jun 2025)**: Introduced Bearer token authentication for MCP servers and clients
- **v3.0 (Jan 2026)**: Major re-architecture — support for custom providers (filesystems, REST APIs), component-level authorization, agent skills over MCP, composable servers, CLI tooling (`fastmcp list`, `fastmcp call`, `fastmcp discover`, `fastmcp generate-cli`), hot reload, and more
- **v3.0 GA (Feb 2026)**: Moved from `jlowin/fastmcp` to `PrefectHQ/fastmcp`; FastMCP Cloud launched for MCP-native deployment
- **v3.2 (Apr 2026)**: Introduced **MCP Apps** — a second protocol channel returning interactive applications (charts, dashboards, forms) instead of plain structured data. Integrated **Prefab** (generative Python UI framework) natively. Added five built-in providers: FileUpload, FormInput, Approval, Choice, GenerativeUI. Security hardening pass (SSRF, JWT alg restrictions, OAuth scope enforcement). Dev server with browser-based app preview and MCP message inspector. Install: `pip install "fastmcp[apps]"`.
- **v3.3 "Slim Reaper" (May 2026)**: Shipped `fastmcp-slim` — a lightweight client-only distribution for CI/agent environments (`pip install fastmcp-slim[client]`). OAuth silent consent hardening, redirect URI allowlist matching, cache partitioned by access token. AzureB2CProvider. OTEL compliance with MCP semantic conventions. Thread affinity control (`run_in_thread=False`). 13 new contributors this release.
- **v3.4.0b1 "Remote Possibility" (May 2026)**: Beta release for `fastmcp-remote` package, host compatibility, and remote authentication behavior.
- **Key talks**: "Your MCP Server is Bad (and you should feel bad)" at AI Engineer Code Summit (2025) and ODSC AI East (2026); "Model Context Pragmatism" at MCP Dev Summit (2026)

Lowin describes the MCP era as moving past "tool servers" toward the **context era**: source from anywhere, compose and transform freely, personalize per-user, track state across sessions, control access, run long operations, version APIs, observe everything.

### Prefab
Announced at the MCP Dev Summit (April 2026), **Prefab** is a generative UI framework that enables building interactive applications in Python:

- **100+ shadcn components** composed using Python context managers
- **Python DSL**: Context managers express component hierarchy — indentation *is* the layout
- **Reactive state**: `Rx` variables handle live bindings (even through f-strings)
- **Agent-friendly**: Python is token-efficient and streaming-compatible; LLMs already know Python, so they grok the DSL quickly
- **JSON protocol**: Serializes to a JSON format that renders as a real React application with full client-side interactivity and no JavaScript required
- **FastMCP integration**: Built into FastMCP 3.2 for MCP Apps — agents write Prefab code, it executes in a sandbox, and renders UIs on the fly
- **Show HN**: Featured on Hacker News (April 2026) as "the generative UI framework that even humans can use"

### Cardboard
An ephemeral presentation tool — part of Lowin's "just for me" software philosophy. Agents create temporary, throwaway presentations for immediate communication needs rather than polished, persistent artifacts.

### Copychat
A utility for copying multiple files into an LLM-compatible format, reflecting Lowin's focus on practical developer tooling.

## Agent Philosophy: "Second Brain"

Lowin is a prominent practitioner of **agent engineering as context engineering**. His personal agent workflow, detailed on the *Vanishing Gradients* podcast (May 2026), treats his agent as a **"second brain"**:

- **Voice memo pipeline**: Voice notes and recorded meetings are transcribed and trickled into the agent's memory substrate
- **Morning briefs**: Daily briefs are fed into the agent, building a persistent, evolving knowledge base
- **Context engineering over prompt engineering**: Lowin has spent years engineering the context that his agents operate within, treating memory as a durable substrate rather than a per-session prompt
- **OpenCode**: Chosen specifically for how deeply he can customize its memory system
- **OpenClaw**: Used alongside OpenCode as part of his multi-agent workflow, routing agent interactions through [[entities/openclaw|OpenClaw]]'s gateway architecture

### The "Explain" Skill
Lowin's anchor skill is an **"explain" skill** — a meta-skill that anchors every other skill he uses. When an agent encounters something new or unclear, the explain skill activates first, ensuring the agent builds understanding before taking action. This pattern exemplifies the [[concepts/agent-skills|progressive disclosure]] architecture of agent skills.

## Other Affiliations

### Compass Coffee
Lowin is the self-described **"Global Ambassador" of Compass Coffee**, a Washington, DC-based coffee chain founded by two Marine officers. His involvement spans over a decade of "cheerful, unpaid labor" — from being the guinea pig for the founders' first latte to negotiating leases, troubleshooting IT, and filling in as a baker. The relationship between Compass and Prefect deepened over time: at Prefect's first conference in 2018, they had "no product to show — just 9 gallons of Compass Coffee and a banner." Today, Compass has 20+ cafes and a wholesale business on Whole Foods shelves.

### Strategic Advisory
Lowin serves as a strategic adviser to:
- **Spotify** — audio streaming platform
- **Positive Sum** — venture capital firm and Prefect investor
- **OSV** — venture capital firm

## Selected Talks & Keynotes

| Year | Event | Talk |
|------|-------|------|
| 2026 | PyData London | Keynote |
| 2026 | ODSC AI East | Keynote — "Your MCP Server is Bad (and you should feel bad)" |
| 2026 | MCP Dev Summit | "Model Context Pragmatism" |
| 2026 | PyAI | Keynote — "Build Reasonable Software" |
| 2026 | Software Engineering Daily | "FastMCP with Adam Azzam and Jeremiah Lowin" — MCP origin story, 3 pillars, 3.0 architecture |
| 2025 | AI Engineer Code Summit | "Your MCP Server is Bad (and you should feel bad)" |
| 2025 | First Commit with Nina | MCP as a standardized handshake for the AI era |

## Open-Source Projects

| Project | Stars | Description |
|---------|-------|-------------|
| [FastMCP](https://github.com/PrefectHQ/fastmcp) | ~25K | Pythonic way to build MCP servers and clients |
| [Prefect](https://github.com/PrefectHQ/prefect) | ~22K | Dynamic workflow automation for data pipelines |
| [Marvin](https://github.com/PrefectHQ/marvin) | ~6K | AI engineering framework with AI Functions |
| [ControlFlow](https://github.com/PrefectHQ/controlflow) | ~1.4K | Agentic AI workflows (archived) |
| [Prefab](https://github.com/PrefectHQ/prefab) | ~430 | Generative UI framework in Python |
| [Copychat](https://github.com/jlowin/copychat) | ~60 | Multi-file copy utility for LLMs |

## Related Pages

- [[entities/opencode]] — OpenCode, Lowin's primary coding agent
- [[entities/openclaw]] — OpenClaw, used in his multi-agent workflow
- [[concepts/model-context-protocol-mcp]] — The MCP protocol that FastMCP implements
- [[concepts/agent-skills]] — The agent skills standard; Lowin's "explain" skill pattern
- [[concepts/context-engineering]] — The discipline Lowin has practiced for years
- [[concepts/generative-ui]] — Generative UI, the domain of Prefab
- [[entities/chris-white-prefect]] — Chris White, Prefect co-founder & CTO
- [[entities/wes-mckinney]] — Wes McKinney, fellow panelist on Show Us Your Agent Skills
