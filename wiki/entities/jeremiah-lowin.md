---
title: Jeremiah Lowin
type: entity
aliases: [jeremiahlowin, jlowin]
created: 2026-06-05
updated: 2026-08-14
tags:
  - person
  - ai-agents
  - memory-systems
  - personal-software
  - mcp
  - open-source
  - prefect
  - orchestration
  - workflow
  - ceo
sources:
  - raw/articles/2026-05-27_hugobowne_the-agentic-software-factory.md
  - transcripts/2026-05-08_vanishing-gradients_show-us-your-agent-skills-ep1.md
  - https://hugobowne.substack.com/p/the-agentic-software-factory
  - https://jlowin.dev/about
  - https://www.prefect.io/blog/how-jeremiah-lowin-turned-a-life-long-question-into-an-industry-leading-startup
  - https://www.prefect.io/prefect-acquires-dagster
  - https://github.com/PrefectHQ/fastmcp
---

# Jeremiah Lowin

**Founder and CEO of Prefect, core maintainer of FastMCP, builder of personal software with AI agents.** Jeremiah is a practitioner who uses AI agents as a "second brain," feeding context through voice memos into an editable memory substrate (OpenClaw) and building bespoke tools for his own workflow.

## Quick Facts

| | |
|---|---|
| **X/Twitter** | [@jeremiahlowin](https://x.com/jeremiahlowin) |
| **GitHub** | [jlowin](https://github.com/jlowin) |
| **Role** | Founder/CEO, [Prefect](https://prefect.io) |
| **Notable projects** | FastMCP (core maintainer), Cardboard, Prefab, OpenClaw skills |

## Career History

### Early Life & Education

Jeremiah grew up near New York City, known for his relentless questioning and interest in the mechanics of systems. During his sophomore year at Harvard, a contradiction sparked his defining moment: his introductory statistics class claimed the stock market is normally distributed, which contradicted what he had just read in *The Misbehavior of Markets*. After a few weeks of learning statistical tools, he proved to himself that markets are *not* normally distributed — and brought the conclusion to his professor, who replied:

> "It's true, stock markets aren't normally distributed. But they're normally distributed enough for Stats 101."

This "good enough" framing became central to his philosophy (he often quotes George Box: "all models are wrong — but some are useful"). He completed a **master's degree in statistics while still an undergraduate**, writing a thesis on a new class of models for measuring dependencies between stock prices — which won top prizes from both his department and the university.

### Wall Street: King Street Capital (2007–2011)

After graduating, Lowin joined the hedge fund **King Street Capital** in 2007 as the first member of the firm's new risk team — landing in a hot seat as the firm navigated the 2008 financial crisis. He eventually oversaw market risk and built tools for a huge number of strategies and stakeholders. The experience reinforced his belief that a tool is "good enough" when it delivers value to its user.

### Machine Learning Consulting (2011–2013)

Captivated by the nascent field of ML in 2011, Lowin spent two years as an ML consultant building software for clients across industries. One client hired him as **Director of Risk** for a large investment firm, where his mandate was building technology that made the team's decision-making observable. The stakeholder pressure he experienced there — everyone wanting tools before knowing their own problems — is what he considers the moment he became a tech founder in spirit.

### Apache Airflow & the Birth of Prefect

Lowin became one of the first developers to join the **Apache Airflow** team (he is a founding PMC member), and one of its top contributors. But when he tried to automate his data science work, Airflow couldn't keep up: Dask (an early user) could spin up thousands of concurrent tasks, while Airflow could only kick off a new task every few seconds. His attempts to convince the Airflow team to modernize failed.

So he built his own tool: **Tin Man**, designed to perform repeated mechanical tasks (his ML library was called Scarecrow — he was on a Wizard of Oz kick). Two chance conversations in fall 2017 — with the head of engineering at a large counterparty and the head of data science at another investment firm — both ended with: "If this was a product, I'd buy it." In **2018, he founded Prefect**.

### Prefect Timeline

| Year | Milestone |
|------|-----------|
| 2018 | Founded Prefect; Chris White (ex-Capital One) joins as first employee, later CTO |
| Mar 2019 | Prefect open-sourced — 500+ GitHub stars in the first few days (expectation was 100) |
| 2019 | First enterprise customer (Fortune 100) |
| 2020 | Prefect Cloud GA; Covid kills Series A, company pivots to mindshare → open-sources most of the commercial product; raises Series A from Positive Sum (Patrick O'Shaughnessy), Valor Equity Partners, Atreides |
| 2021 | $32M Series B from Tiger Global and Bessemer Venture Partners; second-generation workflow engine; becomes strategic advisor to Spotify |
| 2022 | Prefect 2 released — handles any code, not just code written for Prefect |
| 2023 | Enterprise version; year of efficiency and profitable growth |
| 2024–2025 | Operating as profitable, fast-growing business; FastMCP 1.0 incorporated into official MCP Python SDK |
| 2026 | **Prefect acquires Dagster Labs** (three open-source product families: Prefect + Dagster + FastMCP); Prefect Horizon (enterprise MCP gateway) launched |

### Advisory Roles

Lowin serves as a strategic advisor to **Spotify**, **Positive Sum** (the VC firm that led Prefect's Series A), and **OSV**. He is also the Global Ambassador of **Compass Coffee** in Washington, DC, where he lives.

## Workflow Philosophy

### Agent as Second Brain

Jeremiah's central practice is **pouring information into agents and extracting it when needed**. He starts each workday with a voice memo — recorded during his commute or at his desk — talking through what he's thinking, what he wants to do, and what's on the horizon. The transcript drops into OpenClaw's memory substrate, where agents read from it asynchronously.

> *"That's what I really love, is just pouring information in and then working to get it out."* — Show Us Your Agent Skills, Ep. 1

The leverage comes from **feeding context for weeks or months before the moment you need an answer**:

> *"There's a talk I'm giving in three weeks for PyData London, so I can feed in something tonight, close it, don't worry about it, talk to the agent about 1,000 other things, and then I can come back and we can actually pick right up because of the memory substrate there."*

### Three Daily States

1. **Morning** — Voice memo recorded during commute or at home. Talk through the day. Drop into OpenClaw.
2. **Through the day** — Agents work in background, reading from the same memory layer.
3. **When you come back** — Threads pick up via memory substrate; conversations resume where they left off.

### Editable Memory as Key Criterion

Jeremiah chose OpenClaw specifically because he can **reach into the agent's memory and change what it remembers**:

> *"This is one of the reasons that I use an OpenClaw, for example, so that I can go muck around with its memory, in a way that works for me."*

If the operator can't edit what the agent remembers, the second brain is the vendor's, not theirs.

### Separate Tools for Thinking vs. Coding

- **OpenClaw** — main personal interface for thinking, planning, and accumulated context
- **Claude Desktop / Codex Desktop** — for writing code

> *"I use OpenClaw as my main personal interface because of how I've customized its memory. When I'm working on code, I use Claude Desktop and Codex Desktop, which I migrated to from the CLIs mostly because of how much better it is at managing parallel sessions."*

## Agent Skills Design

### Anatomy of a Skill

A skill is a markdown file with two pieces of frontmatter: **name** (used to invoke it) and **description** (always visible to the agent). The body is hidden until the agent decides to invoke the skill — this **progressive disclosure** is the key mechanism.

> *"Skills are shockingly simple for how effective they are. They have two front matter: a name, that's really important, that's how you invoke it; and a description. And the description is always going to be seen by the agent."*

### Key Skills

| Skill | Purpose |
|-------|---------|
| **ship-it** | Polite note telling Claude that "ship it" means *open a pull request*, not merge |
| **explain** | Referenced by every other skill; produces a guided tour (conceptual model → formal behavior → what changed → future work), explicitly bans line-level diff narration |
| **skill-creator** | Meta-skill for creating new skills |
| **github-reply** | Uses explain as a building block for responding to PRs |

> *"This skill has become my workhorse. It is referenced in every other skill I have."* — on `explain`

### Skills vs. MCPs

> *"Skills are awesome ways to steer behavior. They go into the agent's brain in the exact same way that a message from you does... MCPs are great ways to distribute business logic from a central place."*

## Personal Software Projects

### Cardboard
Custom slide software that lays out talks as **acts → beats → slides** with a fixed colour scheme for speaker notes. The screen is read-only by design — Jeremiah interacts entirely via API or MCP server from any agent.

> *"Purely for me, like no one else should use it."*

### Prefab
Python front-end framework for MCP apps, no backend required. Spun out of FastMCP. For building dashboards rather than one-off tools.

> *"I desperately wanted to create MCP apps in Python, and that meant I needed a Python front-end framework that didn't require a backend."*

## FastMCP

Jeremiah is the **core maintainer of FastMCP**, the dominant Python framework for building MCP servers and clients, now maintained under the **PrefectHQ** organization. FastMCP 1.0 was incorporated into the official MCP Python SDK in 2024. By 2026 the standalone project is **downloaded a million times a day**, and "some version of FastMCP powers 70% of MCP servers across all languages" (per the project README). A TypeScript counterpart (`@prefecthq/fastmcp-ts`) is built and maintained by the same team.

FastMCP's three pillars: **Servers** (wrap Python functions into MCP-compliant tools/resources/prompts), **Clients** (connect to any server with full protocol support), and **Apps** (interactive UIs rendered directly in the conversation).

He manages the volume of open-source contributions by running 10+ agents in parallel:

> *"Code is so cheap and it's just kind of getting lobbed over. There's this real imbalance as a maintainer."*

### Prefect Horizon

FastMCP handles the MCP application layer; **Prefect Horizon** is the enterprise MCP gateway built by the same team — for scaling servers and tools across teams with centralized governance: GitHub deployments with branch previews and rollback, private MCP registries, SSO + tool-level RBAC, audit logs, and remixing approved tools into purpose-built endpoints.

### Prefect Acquires Dagster Labs (2026)

In 2026 Prefect acquired **Dagster Labs**, bringing together three major open-source product families — **Prefect** (execution), **Dagster** (outcomes), and **FastMCP** (access). Lowin's framing: "When software makes its own decisions, trust depends on three things: the outcomes it aims for, how it runs its work, and what it can access." The combined portfolio is being woven into a next-generation platform for agent orchestration.

## Related People

| Person | Connection |
|--------|-----------|
| **[[entities/wes-mckinney\|Wes McKinney]]** | Fellow guest on Show Us Your Agent Skills Ep. 1 |
| **[[entities/randy-olson\|Randy Olson]]** | Fellow guest; generator-evaluator pattern |
| **[[entities/hugo-bowne-anderson\|Hugo Bowne-Anderson]]** | Host of Show Us Your Agent Skills |
| **Peter Steinberger** | OpenClaw creator (Jeremiah's memory substrate) |

## See Also

- [[entities/wes-mckinney]]
- [[entities/randy-olson]]
- [[entities/openclaw]]
- [[entities/fastmcp]]
- [[entities/nvidia-nemoclaw]] — NVIDIA's secure agent sandbox stack, another OpenClaw ecosystem player
- [[concepts/personal-software]]
- [[concepts/evaluation/generator-evaluator-pattern]]
- [[concepts/mcp]] — Model Context Protocol, the standard FastMCP implements

## References

- [The Agentic Software Factory](https://hugobowne.substack.com/p/the-agentic-software-factory) (Vanishing Gradients, May 2026)
- Show Us Your Agent Skills, Episode 1 (May 2026)
- [How Jeremiah Lowin Turned a Life-Long Question Into an Industry-Leading Startup](https://www.prefect.io/blog/how-jeremiah-lowin-turned-a-life-long-question-into-an-industry-leading-startup) (Prefect Blog, Feb 2024)
- [jlowin.dev/about](https://jlowin.dev/about) — personal about page
- [Prefect acquires Dagster Labs](https://www.prefect.io/prefect-acquires-dagster) (Prefect, 2026)

## Log

- **2026-08-14**: Enriched L2→L3 — added career history (Harvard statistics, King Street Capital, ML consulting, Apache Airflow PMC, Tin Man → Prefect origin), Prefect company timeline (2018→2026), advisory roles, FastMCP current state (70% of MCP servers, million downloads/day, TypeScript counterpart), Prefect Horizon, and the 2026 Prefect × Dagster Labs acquisition.
- **2026-06-05**: Initial entity page created from "The Agentic Software Factory" article.
