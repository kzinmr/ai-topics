---
title: "Factory"
type: entity
created: 2026-05-08
updated: 2026-05-22
tags:
  - company
  - coding-agents
  - ai-agents
  - developer-tooling
  - software-engineering
aliases: ["Factory AI", "Factory.ai", "droids"]
sources:
  - https://www.factory.ai
  - https://github.com/factory-ai/factory
  - https://tech-insider.org/factory-ai-150-million-series-c-khosla-coding-droids-2026/
  - raw/articles/2026-04-03-free-droid-for-all.md
  - https://www.businessinsider.com/coinbase-layoffs-ai-brian-armstrong-job-cuts-letter-2026-5
  - raw/newsletters/2026-05-22-bens-bites-googles-take-on-openclaw.md
related:
  - [[concepts/subagent-patterns]]
  - [[entities/cursor-ai]]
  - [[entities/cognition]]
  - [[entities/linear]]
  - [[entities/anthropic]]
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
