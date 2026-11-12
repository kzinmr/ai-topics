---
title: "Factory"
type: entity
created: 2026-05-08
updated: 2026-11-12
tags:
  - company
  - coding-agents
  - ai-agents
  - developer-tooling
  - software-engineering
  - partnership
  - databricks
aliases: ["Factory AI", "Factory.ai", "droids"]
sources:
  - https://www.factory.ai
  - https://github.com/factory-ai/factory
  - https://tech-insider.org/factory-ai-150-million-series-c-khosla-coding-droids-2026/
  - raw/articles/2026-04-03-free-droid-for-all.md
  - https://www.businessinsider.com/coinbase-layoffs-ai-brian-armstrong-job-cuts-letter-2026-5
  - raw/newsletters/2026-05-22-bens-bites-googles-take-on-openclaw.md
  - raw/articles/2026-08-25_factory_model-routing-belongs-in-the-harness.md
  - raw/articles/2026-10-20_factory_databricks-partnership.md
  - raw/articles/2026-11-05_factory_humanlayer.md
related:
  - [[concepts/subagent-patterns]]
  - [[entities/cursor-ai]]
  - [[entities/cognition]]
  - [[entities/linear]]
  - [[entities/anthropic]]
  - raw/articles/2026-11-11_factory_security-factory.md
description: "San Francisco-based startup building autonomous AI coding agents ('Droids') for enterprise software development. $1.5B valuation after $150M Series C (April 2026). Led by CEO Matan Grinberg and CTO Eno Reyes, backed by Khosla Ventures, Sequoia Capital, Blackstone, and McKinsey partnership."
---

# Factory (Factory AI)

**Factory** (also known as Factory AI) is a San Francisco-based AI research lab and startup bringing autonomy to software engineering through **"Droids"** — autonomous AI coding agents that integrate into existing development workflows. Unlike IDE assistants (GitHub Copilot, Cursor) that focus on code completion, Factory Droids execute long-horizon autonomous tasks: feature development across multiple repositories, testing, code review, documentation, and deployment.

## Company Profile

| | |
|---|---|
| **Type** | Private (VC-backed, Unicorn) |
| **Founded** | April 2023 |
| **Headquarters** | San Francisco, CA |
| **Leadership** | Matan Grinberg (Co-Founder & CEO), Eno Reyes (Co-Founder & CTO) |
| **Valuation** | $1.5B (April 2026, post-Series C) |
| **Funding** | $150M Series C led by Khosla Ventures (Keith Rabois joining board) |
| **Investors** | Khosla Ventures, Sequoia Capital, Insight Partners, Blackstone, NEA, 20VC, Mantis VC, Evantic Capital, Abstract Ventures |
| **Revenue Growth** | Doubled every month for six months leading to Series C |
| **Website** | [factory.ai](https://factory.ai) |
| **GitHub** | [github.com/factory-ai/factory](https://github.com/factory-ai/factory) |
| **Tech Blog** | [factory.ai/news](https://factory.ai/news) |

**Founders background:**
- **Matan Grinberg** — ex-theoretical physicist, UC Berkeley PhD dropout
- **Eno Reyes** — ex-Hugging Face ML engineer

Factory is backed by a **McKinsey partnership** for enterprise AI transformation, targeting legacy codebase migrations — "code bases older than the people working on them."

## The Droids Platform

### Core Capabilities

- **Missions:** Users describe business outcomes in natural language (e.g., "migrate the billing service from Python 2 to Kotlin microservice") and Droids plan, execute, and verify the work over hours or days
- **Model-Agnostic Routing:** Droids route tasks to different LLMs (Claude 4.5 Sonnet, DeepSeek V3, etc.) based on task requirements — planning vs. routine test authoring
- **Enterprise Integration:** Deep CI/CD, internal APIs, compliance tooling, and documentation system integration. Droids have read/write access to repos, participate in Slack/GitHub discussions, submit PRs.
- **Desktop App:** Grants Droids supervised access to local filesystems, browsers, and command lines
- **Multi-Interface Support:** VS Code, JetBrains, Vim, terminal, web browser, Slack, Jira, Microsoft Teams, GitHub, Linear

### Key Products

| Product | Description |
|---------|-------------|
| **Factory IDE** | Droids in your editor — VS Code, JetBrains, Vim native support |
| **Factory Desktop** | Droids on your desktop — supervised local filesystem/browser/CLI access |
| **Factory CLI** | Droids at scale — command-line automation |
| **Factory Slack** | Droids in the war room — collaborative agent workflows |
| **Factory Jira** | Droids in your backlog — automated issue-to-PR pipeline |
| **Factory Web** | Droids in the browser — no-setup-required agent delegation |
| **Droid Action** | AI-powered code reviews, security scans, PR descriptions on pull requests |

### Adjustable Autonomy

Fine-tune how independently agents operate:
- Allow certain changes automatically while requiring approval for others
- Ranges from fully supervised to fully autonomous execution
- Developer sets the boundaries

## Factory Router: Model Routing in the Harness (Aug 2026)

In August 2026, Factory published a position paper (Abhay Singhal) arguing that model routing belongs in the **agent harness**, not the gateway or model-serving layer. Their production **Factory Router** has routed customer work for 2+ months:

- **58% aggregate cost cut** vs all-frontier pricing; median routed session saved **76%**, 9/10+ sessions saved ≥50%
- Routed sessions **matched frontier-pinned sessions on 8 production measures**; **median turn latency 81s → 49s**
- Benchmarks: **99% of frontier pass rate on Terminal-Bench 2**, **96% on Legacy-Bench**, ~20% lower cost per successful run

The core argument: only the harness owns **session cache state** and **task outcomes**. Switching models discards the warm prefix (next call reprocesses the transcript at 5–10× the cached rate), so the harness decides whether a switch is worth the cache miss based on whether work has stalled. A cache-blind gateway's fully-uncached cost hits **2.12× the all-frontier baseline at turns 61–150** (vs **0.19–0.28×** for cache-aware routing). The harness also assembles the request around the chosen model before the request exists, and uses task-outcome signals to refine the routing policy. Related: [[concepts/coding-agents/model-routing]].

## Enterprise Customers

Factory claims 3x to 5x throughput gains by removing humans from routine loops. Notable customers include:

- **Nvidia** — CUDA library maintenance and documentation
- **Morgan Stanley** — Risk-modeling codebase updates
- **Palo Alto Networks** — Accelerating security review cycles
- **Others:** Adobe, EY, Adyen, MongoDB, Bayer, Zapier

## "Free Droid for All" (April 2026)

Announced by @0xSero on X/Twitter (April 3, 2026), Factory made their Droids available as a free tier, marking a significant shift from paid-only enterprise access. The announcement received 1,500 bookmarks and 134K impressions. This strategy mirrors the freemium growth model used by Vercel, Supabase, and other developer tools.

## Competitive Landscape

| Company | Valuation | Primary Use Case | Differentiator |
|---------|-----------|-----------------|----------------|
| **Factory AI** | $1.5B | Enterprise Droids | Model-agnostic routing, deep infra integration |
| **Cursor** | ~$60B | IDE Assistant | Fast in-editor edits, agent mode |
| **Cognition** | Multi-Billion | Autonomous Engineer | End-to-end task execution |
| **Claude Code** | Part of Anthropic | CLI Agent | Deep Claude integration |

## The SWE-Bench Debate

Factory has notably **not published official SWE-Bench Verified scores**. While competitors like Anthropic (80.8%) and OpenAI (77.2%) lead public benchmarks, Factory argues that synthetic benchmarks don't reflect the "high-context" reality of enterprise systems. Their value proposition is measured in throughput gains on real enterprise codebases, not benchmark scores.

## Strategic Outlook

### Predictions (as of April 2026)
1. **Series D:** Expected at $5B+ valuation within 18 months
2. **Consolidation:** Second-tier startups (Lovable, Magic) likely to be acquired by hyperscalers by late 2026
3. **Global Expansion:** London office (Q2 2026), Tokyo office (Q3 2026)
4. **Pricing Shifts:** Market moving toward "Outcome-based" (Missions) and "Agent-as-a-Service" models

### Risks
- **Model Dependency:** As a model-agnostic layer, vulnerable if foundation model labs build their own orchestration layers
- **Customer Concentration:** Large portions of revenue tied to few multi-million-dollar contracts
- **Execution Risk:** Long-horizon autonomous coding has history of being over-promised (cf. Devin 2024)

## Use of Series C Proceeds

The $150M will fund:
- **Research:** Doubling the team to solve "long-horizon agent reliability"
- **Product:** Enhancing model routing and always-on background agents
- **Go-to-Market:** Scaling headcount from ~80 to ~250 by end of 2027

### Deferred Context Engine (May 2026)

Factory introduced the **Deferred Context Engine** — Droid loads tools selectively rather than loading all definitions into context:

- Reduces context size by **~40%**
- Droid dynamically determines which tools to load based on task
- Addresses context window bloat in multi-tool agent systems

## Databricks Partnership (Oct 2026)

Factory announced a partnership with [[entities/databricks]] (Oct 19, 2026): customers can use the data and models in the **Databricks Data + AI Platform** to power software built or migrated by Factory Droids. The announcement is anchored on a live engagement migrating one of the largest global enterprises' data platform — **petabytes of data, hundreds of thousands of tables, hundreds of business applications** (UIs, app services, integration/API layers, business logic, security) — to Databricks.

**The thesis**: data modernization and software modernization must happen together. Moving tables to the lakehouse is the easy half; the applications and workflows that consume them still need rebuilding, and historically that required separate data-engineering and application-development teams with different tools and handoffs, where a single pipeline change cascades downstream. Factory + Databricks collapses it into **one engineering workflow** — agents understand the existing system, plan the migration, build, and validate — with Databricks as the open, governed data/analytics/AI foundation and Factory supplying agentic software engineering.

**Mechanics**:
- **Understanding**: Droids work across application code, data pipelines, SQL, tests and docs, tracing how an app depends on a stored procedure, which pipeline feeds it, and where a change propagates. Databricks **Unity Catalog**-governed assets and Factory's context integrations connect app dependencies to the data foundation.
- **Planning**: Droids identify dependencies, propose an implementation sequence and compatibility checks; **Missions** provide planning, milestones and coordinated multi-component execution; engineers review the plan and resolve ambiguous business rules before implementation.
- **Execution**: Droids use Databricks API access to create/run jobs, validate results and deploy apps — e.g., moving an app from legacy Postgres to **Databricks Lakebase**, rewriting transformations in Python, building/scheduling a **Lakeflow** pipeline, creating an **AI/BI** dashboard, then diffing the new app against the legacy one.

**Three use-case categories**: (1) **PDLC Automation** — requirement through planning, development, testing, security, docs, monitoring on Databricks-powered apps; (2) **Migration and Modernization** — data platform migrations plus dependent applications; (3) **Cybersecurity** — remediating vulnerabilities flagged by **Databricks Lakewatch**.

**Go-to-market signal**: qualifying customers can buy Factory through the **Databricks Marketplace using up to 10% of their existing Databricks commitment** — a consumption-commitment burn-down channel. Integration surface: a Databricks connector under Settings → Connectors, managed MCP servers, running Droids on Databricks-served models, and webhook automations.

> Read: this is the coding-agent vendor moving up-stack from "write code" to "own a data-platform migration," using a hyperscaler-adjacent data platform as both distribution and governed context source. Compare [[concepts/enterprise-agents]] and Factory's [[#Factory Router: Model Routing in the Harness (Aug 2026)|harness-side model routing]].

Source: raw/articles/2026-10-20_factory_databricks-partnership.md

## Factory × HumanLayer acquisition (Nov 4, 2026)

Factory announced on **November 4, 2026** that **[[entities/humanlayer]] is joining Factory** — Dex Horthy and Kyle Mistele (HumanLayer's founders, previously known for 12-Factor Agents and the Research/Plan/Implement "skill pack") bring their multiplayer coding-agent workspace into Factory's software-factory platform ([announcement](https://factory.com/news/humanlayer)).

**What Factory said**:
- HumanLayer's team has "been regularly **6-9 months ahead of the zeitgeist** on best practices for working with coding agents and software factories, especially for larger teams with hundreds or thousands of engineers."
- **HumanLayer will be open sourced**, and existing HumanLayer users are invited to Factory. The current hosted platform stays up through a transition period supporting **data export, migration to Factory, or self-hosting the open-source HumanLayer**.
- Near-term roadmap ports HumanLayer's most-used features into Factory: **multiplayer tasks/workstreams and in-app collaboration on agent-written plans, product specs, and design docs**.

**Why it matters**: this is the consolidation of the two most visible "software factory" toolchains — Factory's governed, model-independent Droids platform (see [[#The Droids Platform]]) plus HumanLayer's human-in-the-loop review layer over agent sessions, plan artifacts and diffs. HumanLayer's positioning ("bring your own compute, development environment, and agent harness") made it the natural control plane for teams that did not want to adopt a single vendor's harness; folding it into Factory moves that control-plane layer **in-house for the first time** and narrows the neutral-HITL option set for enterprise agent fleets. Compare the independent-control-plane framing in [[concepts/harness-engineering/agent-harness]] and the multi-harness orchestration of [[entities/warp-terminal]].

Sources:
- [HumanLayer is joining Factory — Factory News](https://factory.com/news/humanlayer) (Nov 4, 2026)
- raw/articles/2026-11-05_factory_humanlayer.md

## Security Factory — continuous signals → triage → remediation (November 2026)

Factory announced **Security Factory** (November 10, 2026, **Private Preview**): a product that turns security *findings* into tested fixes by connecting investigation, remediation and verification in one workflow. Framing: "Frontier models are becoming exceptionally capable at finding vulnerabilities. The next opportunity lies in fixing them."

**Three-stage pipeline**, built on Factory's existing agent primitives:

1. **Signals** — Connectors consolidate findings from static-analysis, dependency/secret scanners and infrastructure security tools, plus context from threat intelligence, asset inventories, Jira tickets and Slack threads. Combined with **Security Review**, which applies STRIDE, OWASP and supply-chain methodologies to PRs and full-codebase audits.
2. **Triage** — agents assess reachability, validate exploitability, and trace attack paths that *chain* vulnerabilities and misconfigurations (their example: an internet-facing service plus an overprivileged service account — investigating either in isolation misses the combined exposure). **Workstreams** divide investigations into specialized parallel tasks with durable state and shared context; exploit hypotheses are reproduced in controlled environments on Droid Computers, an OS-level sandbox, or the customer's own cloud via OpenCompute. Output: evidence-backed prioritized backlog — "demonstrated risk, not scanner severity alone."
3. **Remediation** — triage evidence is carried straight into Factory's coding workflows (Automations, SDK, Droid CLI, desktop app): agents develop fixes, test against the original exploit conditions, check regressions, and open PRs. **Configurable autonomy levels**, from presenting remediation plans for human approval up to auto-creating PRs and deploying fixes within approved policies.

**Strategic read.** This is Factory generalizing its coding-agent harness into security operations — the argument is that security investigations have become *software engineering workloads* (navigating codebases, tracing attacker-controlled inputs, examining dependencies/permissions/deploy configs). It extends the Databricks Lakewatch cybersecurity use case documented above from a partner workload to a named product line, and it sits on the detection→remediation frontier alongside [[concepts/autonomous-security-agents]] and [[concepts/vulnhunter-agentic-code-security]], with the distinguishing bet being the *fix* half (verified patches) rather than finding bugs.

**Source:** [[raw/articles/2026-11-11_factory_security-factory]]
