---
title: Ramp
created: 2026-04-30
updated: 2026-05-21
type: entity
tags:
  - company
  - ai-agents
  - coding-agents
  - fintech
sources:
  - raw/articles/2026-04-30_ramp-inspect-background-agent.md
  - https://builders.ramp.com
  - https://techcrunch.com/2026/05/07/ramp-in-talks-to-hit-40b-valuation-6-months-after-reaching-32b/
related:
  - "entities/openai]]"
  - "entities/anthropic]]"
---


# Ramp

## Overview

**Ramp** is a financial operations platform designed to save companies time and money. Founded in 2019 and headquartered in New York, Ramp combines corporate cards, expense management, bill payments, procurement, travel booking, treasury, and automated bookkeeping into an all-in-one solution — with built-in AI intelligence to maximize the impact of every dollar and hour spent. As of 2026, Ramp serves over 50,000 customers (from family farms to space startups), powers over $100 billion in annualized purchase volume, and has saved customers $10 billion and 27.5 million hours.

Ramp is also known for its strong engineering culture and has developed **Inspect**, a custom background coding agent for internal software development that handles approximately **30% of all merged pull requests**.

## Key Facts

| Detail | Value |
|--------|-------|
| **Category** | Financial Operations / Corporate Spend Management |
| **Founded** | 2019 |
| **CEO** | Eric Glyman |
| **Employees** | — |
| **Revenue** | $1B+ (doubled year-over-year, Nov 2025) |
| **Customers** | 50,000+ |
| **Annual Purchase Volume** | $100B+ |
| **Valuation** | $32B (Series E-3, Nov 2025); in talks for $40B+ (May 2026) |
| **Total Funding** | ~$2.1B+ |
| **Key Investors** | Lightspeed, Founders Fund, D1 Capital, Coatue, GIC, Thrive Capital, Khosla Ventures, Iconiq, General Catalyst, Bessemer |
| **Tech Blog** | [builders.ramp.com](https://builders.ramp.com) |

## Engineering Culture & Blog

Ramp maintains a dedicated engineering blog at **[builders.ramp.com](https://builders.ramp.com)** (RSS: [builders.ramp.com/feed.xml](https://builders.ramp.com/feed.xml)), where the engineering team publishes deep-dives on infrastructure, AI/ML systems, developer tooling, and their approach to building financial technology. The blog exemplifies Ramp's philosophy of "build your own" — owning internal tooling to create something significantly more powerful than off-the-shelf alternatives.

## Funding & Valuation Timeline

| Round | Date | Amount | Valuation |
|-------|------|--------|-----------|
| Secondary | Mar 2025 | — | $13B |
| Series E | Jun 2025 | $200M | $16B |
| Series E-2 | Jul 2025 | $500M | $22.5B |
| Series E-3 | Nov 2025 | $300M | $32B |
| Series E-4 (in talks) | May 2026 | $750M | $40B+ |

Ramp raised four rounds in 2025 alone, with its valuation compounding rapidly. CEO Eric Glyman has evangelized a vision of AI embedded throughout Ramp's spend management products — including agents that automatically block out-of-policy purchases, detect fraud, and move funds to interest-bearing investments.

## Key Products

### Corporate Spend Management Platform

- **Corporate Cards**: Physical and virtual cards with built-in spend controls
- **Expense Management**: Automated receipt matching, policy enforcement, and approvals
- **Bill Payments**: AP automation with vendor management
- **Procurement**: Purchase order management and approval workflows
- **Travel Booking**: Integrated travel management with policy controls
- **Treasury**: Automated cash management and yield optimization
- **Bookkeeping**: AI-powered transaction categorization and accounting integrations

### Inspect (Background Coding Agent)

Ramp's internal AI agent for software development that:
- Runs asynchronously in the cloud
- Verifies its own work with production context
- Integrates with Slack, web UI, and Chrome extension
- Uses the user's GitHub token for PRs (not an app-owned bot)

## Architecture

### Infrastructure Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Sandbox** | [[concepts/modal-sandboxes]] | Isolated VMs with pre-built images |
| **Agent Framework** | [[entities/opencode]] | Open-source, server-first, typed SDK |
| **State Management** | Cloudflare Durable Objects | Per-session SQLite databases |
| **Real-time** | Cloudflare Agents SDK | Streaming with WebSocket hibernation |
| **Authentication** | GitHub OAuth | User-based PR creation |
| **Image Registry** | Modal | Per-repo images rebuilt every 30 min |

### Design Principles

1. **Build your own**: "Owning the tooling lets you build something significantly more powerful than an off-the-shelf tool will ever be."
2. **Fast starts matter**: "When background agents are fast, they're strictly better than local: same intelligence, more power, and unlimited concurrency."
3. **Verification is core**: Agent proves its work with tests, telemetry, and visual QA
4. **Multiplayer by design**: Sessions are shareable for collaboration and review

## Client Interfaces

| Interface | Key Feature |
|-----------|-------------|
| **Slack Bot** | Auto-classification of repos, public-channel virality, Block Kit updates |
| **Web UI** | Hosted VS Code (`code-server`), streamed desktop for computer use |
| **Chrome Extension** | Visual editing for non-engineers, DOM/React internals extraction, MDM deployment |

## Key Metrics

- ~30% of all merged PRs handled by Inspect
- 30-minute image rebuild cycle
- Unlimited concurrency via Modal
- Customers save 5% on spend on average and grow 12% faster
- $10B cumulative customer savings
- 27.5M hours saved

## Related Entities

- [[entities/inspect]] — Ramp's background coding agent
- [[entities/opencode]] — Agent framework used by Ramp
- [[concepts/coding-agents/background-coding-agent]] — Concept pioneered by Inspect
- [[concepts/modal-sandboxes]] — Execution layer
- [[entities/openai]] — AI model provider (GPT models used in Inspect)
- [[entities/anthropic]] — AI model provider (Claude models used in Inspect)

## Codex with GPT-5.5 Adoption (May 2026)

In a May 2026 case study, Ramp's AI DevEx lead **Austin Ray** detailed how Ramp uses [[openai-codex-cli|Codex]] with GPT-5.5:

- **Code review acceleration**: Engineers who previously waited hours for reviews now receive "substantive, codebase-aware feedback in minutes." Codex provides a "level of thoroughness that most human reviewers don't have time for."
- **Industry gold standard**: "Codex code review catches things that I miss and that other engineers miss and that other AI code reviewers definitely miss. [...] It's become a mandatory part of a lot of code review flows."
- **On-Call Assistant**: Ramp built an agentic tool with Codex that offloads bulk on-call rotation work. Codex with GPT-5.5 handles Ramp's "immense product surface area" effortlessly.
- **Engineers as orchestrators**: "The skill is no longer writing every line of code yourself. It's knowing how to direct AI tools like Codex, when to trust them, and when to push back."
- **Adoption advice**: Demonstrate first-hand, build trust through guided sessions, invest in the vendor feedback loop.

This represents a significant endorsement of Codex over [[entities/inspect]] for certain workflows — Ramp uses both its own background agent (Inspect) and OpenAI's Codex for different parts of the development pipeline.

## Sources

- Ramp Engineering, "Why We Built Our Background Agent", builders.ramp.com, April 2026
- [TechCrunch: Ramp in talks to hit $40B+ valuation](https://techcrunch.com/2026/05/07/ramp-in-talks-to-hit-40b-valuation-6-months-after-reaching-32b/) — May 7, 2026
- [Ramp reaches $32B valuation (PR Newswire)](https://finance.yahoo.com/news/ramp-reaches-32-billion-valuation-150000798.html) — November 17, 2025
- [PYMNTS: Ramp Eyes $40 Billion Valuation](https://www.pymnts.com/back-office/2026/ramp-eyes-40-billion-valuation-in-new-funding-round/) — May 7, 2026
- [OpenAI: How Ramp engineers accelerate code review with Codex](https://openai.com/index/ramp) — May 20, 2026
