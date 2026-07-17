---
title: "Sierra"
created: 2026-05-05
updated: 2026-07-17
type: entity
tags:
  - company
  - ai-agents
  - product
  - platform
  - valuation
  - benchmark
  - evaluation
  - lab
sources:
  - raw/newsletters/2026-05-04-ainews-the-other-vs-the-utility.md
  - https://www.cnbc.com/2026/05/04/bret-taylor-sierra-fundraise-openai.html
  - https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/
  - raw/articles/sierra.ai--blog-tau-knowledge--5dda7a09.md
  - raw/articles/sierra.ai--blog-outcomemaxxing--0bc34aec.md
  - raw/articles/sierra.ai--blog-discovering-what-s-possible-with-ai-for-cx--904ecc1f.md
  - raw/articles/2025-08-19_sierra_simulations-the-secret-behind-every-great-agent.md
  - raw/articles/sierra.ai--blog-ai-pilling-our-company-lessons-learned--168c9b80.md
  - raw/articles/sierra.ai--blog-announcing-our-partnership-with-softbank-corp--4a150bd0.md
  - raw/articles/sierra.ai--blog-pinecone-harnessing-the-wisdom-of-the-workforce--93ed8565.md
  - raw/articles/2026-07-14_sohmray_icml-2026-research-trends.md
  - raw/articles/2026-07-16_sierra_horizon-long-horizon-agents.md
---

# Sierra

## Overview

Sierra is an AI-powered customer service platform that deploys conversational AI agents for enterprise customer support. Founded by former Salesforce executives **Bret Taylor** (Salesforce co-CEO, former Twitter chairman) and **Clay Bavor** (former Google VP), Sierra represents one of the fastest-growing AI-native enterprise companies.

## Key Metrics (May 2026)

- **Valuation**: $15.8B (Series E, May 4 2026 — up from $10B in Fall 2025)
- **Funding**: $950M Series E led by Tiger Global and Google's GV, with Benchmark, Sequoia, Greenoaks
- **ARR**: $150M+ in 8 quarters — fastest growth in enterprise software history
- **Customers**: Fortune 50's 40%+, Prudential, Cigna, Blue Cross Blue Shield, Rocket Mortgage
- **Revenue multiple**: 50-75x — reflecting AI agent premium in enterprise

### Ghostwriter (Agent as a Service, April 2026)

Sierra launched **Ghostwriter**, an "agent as a service" tool. Users describe what they need in natural language, and Ghostwriter autonomously creates and deploys a specialized agent. This extends Sierra's platform beyond customer-facing agents into internal business process automation.

### Outcomemaxxing / Outcome-Based Pricing (June 2026)

Sierra published a detailed framework for **outcome-based pricing** centered on an **Agency × Attribution 2×2 matrix** (from Madhavan Ramanujam's *Charging for Intelligence*):

- **Bottom-Left (Low Agency, Low Attribution)**: Classic seat-based SaaS (Salesforce, Office 365) — users log in, software assists, attribution is fuzzy
- **Top-Left (High Agency, Low Attribution)**: API pricing (OpenAI, AWS) — autonomous work but no clean outcome attribution
- **Bottom-Right (Low Agency, High Attribution)**: Seat + consumption hybrids (Cursor) — human-managed, AI consumption informs pricing
- **Top-Right (High Agency, High Attribution)**: Sierra's position — agents deliver complete outcomes (resolved cases, processed claims) directly attributable to the software

Sierra also coined the **"Saaspocalypse"** concept: since December 2024 the S&P 500 is up ~30% while WCLD (SaaS index) is down ~15%, reflecting market recognition that AI agents delivering outcomes will displace productivity tools for teams. Key operational insight: outcome-based pricing rewires the entire company around delivering results, since customer success is baked into the P&L — sales, product, support, and marketing all share the same incentive.

## Product

Sierra deploys conversational AI agents that handle customer service interactions end-to-end, including:
- Natural language understanding of customer issues
- Integration with enterprise systems (CRM, order management)
- Agentic problem resolution (not just FAQ lookup)
- Designed to replace or augment traditional contact center operations

### Customer Success Case Studies

**Vivid Seats**: Resolved in under 4 weeks from kickoff to live. Resolution rates increased 40%, customer satisfaction 35%. CX team shifted from queue handling to root-cause fixes and product development.

> "We're able to think really big about what's possible. Things we would have said were pie-in-the-sky a couple of years ago. We're on the other side of that now."
> — Katy Smith, Director of CX Agent Experience, Vivid Seats

> "If we're seeing people ask us 10,000 times a month about a specific feature, we're able to prioritize that at scale, quickly. The best moments are when a pattern leads to a change that eliminates the need for support entirely."
> — Janelle Pacheco, Director of Product, Vivid Seats

**Wilson (sporting goods)**: AI agent enables personalized product discovery (e.g., recommending glove size for a child based on follow-up questions). Every conversation becomes a source of intelligence for continuous improvement.

> "It's like every customer having access to a knowledgeable agent 24/7. We can now identify what information our consumers need and add it directly and easily into the system. It helps us continuously improve how we answer their questions — a benefit we didn't anticipate but now see as critical."
> — Mary Craven, Director of Consumer Experience, Wilson

**Minted (design marketplace)**: Peak season handling with seamless platform integration. CX team identifies trends, spots emerging issues, routes insights across the business.

> "Our focus is on long-term transformation. The insights we're gaining now are shaping how we serve customers tomorrow."
> — Sarah Wallis, Chief Operating Officer, Minted

## Competitive Context

Sierra operates in the rapidly growing **AI customer service agent** space:
- Competes with traditional contact center software (Zendesk, Salesforce Service Cloud)
- Part of the broader "Service-as-Software" thesis — selling outcomes, not tools
- Represents the enterprise AI agent deployment model: specialized agents with clear business metrics

## Research & Benchmarks

Sierra develops and maintains evaluation benchmarks for conversational AI agents, notably **[[concepts/ai-benchmarks/tau-knowledge|τ-Knowledge]]**, an extension of [[concepts/ai-benchmarks/tau-bench|τ-Bench]] that evaluates agents on realistic knowledge work.

### ICML 2026 — tau-bench Presentations (July 2026)

Sierra researchers presented **three tau-bench papers** at ICML 2026 in Seoul, including:

- **tau2-bench** — Received an **oral presentation** (top 0.7% of ~24,000 submissions, one of 168 orals)
- **tau-bench** — Core conversational agent benchmark
- **tau-Knowledge** — Knowledge-grounded agent evaluation
- **tau-Voice** — Voice interaction agent evaluation

The tau-bench suite was cited in invited talks and papers throughout the conference. Presenting team included [[entities/soham-ray|Soham Ray]], Ola Zytek, Ben Shi, Pedram Razavi, and Victor Barres.

### τ-Knowledge / τ-Banking

τ-Knowledge evaluates agents on their ability to search a realistic knowledge base (698 documents, ~195K tokens across 21 product categories), reason over findings, and execute multi-step tool calls — all while handling live customer conversations in a fintech-inspired **τ-Banking** domain.

Key findings (May 2026 leaderboard):
- **GPT-5.5 + xhigh reasoning** leads at **37.4% pass^1**, **20.6% pass^4** — up 11.9pt pass^1 from GPT-5.2 (25.5%)
- ~63 percentage points of pass^1 headroom remain → not close to saturation
- Strong agents search **smarter, not harder**: GPT-5.5 issues 9.1 queries/task vs 19.4 for GPT-5.2, with more surgical targeting
- Agents must self-discover tools from documents (no explicit API specs given) — a fundamentally harder setting than traditional benchmarks

Sierra open-sources τ-Knowledge and invites model providers to evaluate against it as a measure of real-world knowledge-grounded agent capability.

### Agent Simulation Platform

Sierra's Agent OS includes a **deployment simulation** system ([[concepts/deployment-simulation]]) where simulated conversations between agents and mock personas ensure reliability at scale. Key capabilities:

- **Automatic test generation** from SOPs, knowledge bases, coaching transcripts, and conversation flows
- **Persona diversity** — users who speak different languages, vary in tech comfort, adopt many tones
- **Judge agent** evaluates goal achievement, SOP compliance, brand guidelines, and accuracy
- **CI/CD integration** — simulations gate releases via GitHub Actions or CLI, like unit tests for agent behavior
- **Scale**: customers run 35,000+ tests/day, achieving 90% resolution rates and 4.5/5.0 CSAT

See also: [[comparisons/openai-vs-sierra-agent-simulation]] for comparison with OpenAI's research framework approach.

### "AI-Pilling Our Company" — Internal AI Adoption (July 2026)

Sierra published a detailed account of how they internally deployed AI across their entire company, not just engineering. Key insights:

**1. Agent, Singular** — Sierra collapsed role-specific agents (support agent "PINE", data analyst "Pinewood", engineer "Pinecone", sales agent "Reggie Jr") into a single agent called **Pinecone**. The lesson: the most important work happens *across* teams, not within them. One agent with one Slack handle, one URL, and one unbroken thread from question to finished result.

**2. Proactive, Not Reactive** — Pinecone persists across entire workflows, carrying context forward and picking threads back up. Instead of waiting to be asked, it acts when the next step is ready (webhooks, Linear tasks, reviews). The goal: less work arriving unfinished.

**3. Business Context Is the Bottleneck, Not Intelligence** — Frontier models are now capable enough for most business needs. The bottleneck has shifted to company-specific context: workflows, history, judgment calls. An agent with complete context can prepare meetings, research accounts, review contracts, and trace product decisions.

**4. The Agent Is the UI, the System of Record the Backend** — Artifacts (PRs, decks, contracts) are both input and output. The agent works *across* systems of record (GitHub, Salesforce, Linear) rather than replacing them. Replacing those systems means recreating decades of mature software.

**5. Outcomes, Not Just Activity** — Since March, Pinecone has run 75,000+ sessions for 600+ people. 70% of PRs are opened through it. But Sierra warns against measuring activity (sessions, tool calls) instead of outcomes (deal cycle time, first-pass resolution, work-life balance).

**Pinecone Architecture** (from July 2026 follow-up article):
- **Three-layer architecture**: App server (frontend/API/persistence/integrations), Agency (manages isolated K8s runner pods via Redis Streams for live communication), Runner (Go process supervising Codex/Claude Code, managing dev services, brokering privileged operations)
- **Durable sessions**: Sessions persist across harness/pod/node failures via Agency recording continuous state — replacement runners resume exactly where previous left off
- **Multiplayer**: Sessions can be shared, branched, and forked with their own MCP authorization. Coding sessions expose live previews that hot-reload as agents implement feedback. Users can point-and-click in the preview to describe UI changes
- **Privileged operations**: Network proxy intercepts all external requests, swaps in appropriate credentials without the agent ever seeing them — "the agent assumes it can do everything, trusts nothing"
- **Intent-based routing**: Classifier reads the prompt and selects repo, environment, harness, model, reasoning budget. If task changes mid-session, Pinecone provisions a new environment with same context
- **Brokered PRs**: Sessions open their own PRs, watch CI checks, auto-fix failing tests, rebase on conflicts, only ping humans when judgment required
- **Skills**: Reusable playbooks (private, sharable, or default-on) — from "prepare meeting brief" to "stabilize flaky CI"
- **Build primitives, not workflows**: Pinecone provides building blocks (sessions, branching, automations, skills) rather than predefined workflows, letting emergent uses evolve

**Technical stack**: Built on Claude Code and Codex, with an MCP Gateway for security (inherits each employee's access, enforces policy at every tool call, isolates customer data, audit trail). Routing layer lets them direct tasks to the best model for each job.

> *"The 1968 study found a 10X gap between the best and the rest — and for fifty years, the only answer was to go hunt for those rare people. Now there's a better one: give everyone an agent so they have the advantages of the few."*

### SoftBank Partnership — Japan Market Entry (July 2026)

Sierra announced a strategic partnership with **SoftBank Corp.**, Japan's leading telecommunications and IT operator, making SoftBank its **exclusive sales partner in Japan**. Key details:

- **LINEMO deployment**: SoftBank's online-exclusive mobile brand already uses Sierra. Results: **97% inquiry resolution rate**, **93% customer satisfaction** (vs previous solution)
- **Expansion plans**: SoftBank plans to extend Sierra across its flagship SoftBank and Y!mobile brands, plus additional group company services
- **Opera Tech acquisition**: Sierra acquired Opera Tech earlier in 2026 and opened its first Tokyo office, establishing physical presence in Japan
- **SoftBank Vision Fund 2** is also an investor in Sierra

The partnership reflects Sierra's strategy of entering markets with high customer service expectations through local partners. Japan's *omotenashi* (anticipating customer needs with genuine care) philosophy directly influenced Sierra's product design. This marks Sierra's first major international expansion beyond its US base, targeting Japan's sophisticated enterprise market.

Source: [[raw/articles/sierra.ai--blog-announcing-our-partnership-with-softbank-corp--4a150bd0]]

### Horizon — Long-Horizon Agent Platform (July 2026)

Sierra announced **Horizon**, a platform that extends [[concepts/ai-agents|AI agents]] beyond single conversations into **long-horizon goals** that span days, weeks, or months. Announced as "the most significant expansion of Sierra since we launched in 2024," Horizon enables agents to pursue complex outcomes like originating loans, getting prior authorization for healthcare procedures, closing sales, and upgrading subscription plans.

**Key capabilities:**

- **Long-horizon planning**: Agents reason between engagements about what actions to take to maximize the odds of an outcome (e.g., scheduling a specialist referral across dozens of texts and phone calls with patient, specialist, and referring physician)
- **Context engine**: Stitches together interactions across time, making agent behavior intelligent rather than hard-coded. Agents learn from previous customer interactions to make the offer most likely to be accepted
- **Proactive engagement**: Agents proactively reach out to customers over days, weeks, or months rather than waiting for inbound contact
- **Outcome-based pricing**: Customers pay for business outcomes delivered, not tokens — Sierra bears the burden of managing token spend
- **Learning loop**: Each closed sale (or rejection) automatically improves the agent's decision-making for future conversations

Bret Taylor frames Horizon's two key theses:

1. **Differentiation moat**: Customer relationship data becomes a durable, defensible moat that deepens as AI improves. Proprietary context remains the company's — enabling differentiation without fear that frontier model progress helps competitors.
2. **Tokenomics**: Outcome-based pricing abstracts token costs away from the customer. This extends Sierra's earlier "Outcomemaxxing" framework into a concrete product.

Horizon represents a shift from customer *experience* agents to customer *outcome* agents — the difference between answering a question and closing a sale.

Source: [[raw/articles/2026-07-16_sierra_horizon-long-horizon-agents]]

## Significance

Sierra's valuation ($15B+) and ARR growth ($200M+) make it one of the highest-valued AI application companies, demonstrating that the enterprise AI agent market has reached material scale. Its 50-75x revenue multiple reflects investor expectations that AI agents will capture significant market share from traditional SaaS and human-staffed services.

## Related

- [[entities/bret-taylor]] — Co-founder, former Salesforce co-CEO
- [[entities/clay-bavor]] — Co-founder, former Google VP
- [[entities/soham-ray]] — Researcher; presented tau-bench at ICML 2026
- [[concepts/service-as-software]] — Business model thesis
- [[concepts/ai-agents]] — Core technology
- [[concepts/ai-benchmarks/tau-knowledge]] — Sierra's knowledge-grounded agent benchmark
- [[concepts/ai-benchmarks/tau-bench]] — Sierra's conversational agent benchmark
- [[concepts/multi-agents/agent-team-swarm]] — Related agent deployment patterns
- [[concepts/long-horizon-agents]] — Sierra Horizon platform concept
- [[entities/anthropic]] — Claude powers enterprise agent deployments in the same market

## Links

- **Website**: [sierra.ai](https://sierra.ai)
