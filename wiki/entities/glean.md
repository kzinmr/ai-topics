---
title: "Glean"
type: entity
created: 2026-05-08
updated: 2026-06-06
tags:
  - company
  - search
  - ai-agents
  - rag
  - enterprise-ai
aliases: ["Glean Work", "Gleanwork"]
sources:
  - https://www.glean.com/
  - https://www.glean.com/about
  - raw/articles/2026-05-15_glean_cowork-mcp-eval.md
  - raw/articles/2026-05-21_glean_health-agents-2026.md
  - raw/articles/2026-06-02_glean_generative-ai-stack-for-software-engineers.md
  - raw/articles/2026-06-03_glean_query-snowflake-data-in-glean-assistant.md
  - "[[raw/articles/2026-06-03_glean_token-yield-architecture]]"
  - raw/articles/2026-06-04_glean_introducing-glean-mcp-gateway.md
  - raw/articles/2026-06-05_glean_generative-ai-for-software-engineers-is-more-than-code-completion.md
|---

# Glean

Glean is an AI-powered work assistant and enterprise search platform that connects across all company applications to deliver unified search, an AI assistant, and autonomous agents. Founded by former Google search engineers, it provides a horizontal AI platform for enterprise knowledge retrieval and task automation.

| | |
|---|---|
| **Type** | Enterprise AI Platform |
| **Founded** | 2019 (Palo Alto, CA) |
| **Leadership** | Arvind Jain (Founder & CEO, ex-Google Distinguished Engineer), T.R. Vishwanath (Co-founder & CTO), Tony Gentilcore (Co-founder) |
| **Key Products** | Glean Search, Glean Assistant, Glean Agents |
| **Website** | [glean.com](https://www.glean.com) |
| **Tech Blog** | [glean.com/blog](https://www.glean.com/blog) |

## Key Facts

- Founded by Arvind Jain (previously co-founded Rubrik, spent 10+ years at Google leading Search, Maps, YouTube)
- Raised over $260M Series E; total funding exceeds $600M
- Users average queries per day; platform saves employees hours per year
- Uses enterprise context layer with connectors, Enterprise Graph, and retrieval-augmented generation (RAG)
- Supports multi-LLM approach including Gemini, Claude, and GPT models

## Products & Technology

### MCP vs Cowork Benchmark (May 2026)

Glean benchmarked its MCP server against off-the-shelf MCP tools (Atlassian Rovo, GCP, GitHub, Gmail, Slack, Salesforce) using Claude Sonnet 4.6 in Claude Cowork as the harness across ~175 enterprise queries.

**Key Results:**
- **Preferred ~2.5x more often** than off-the-shelf MCP tools across utility, correctness, completeness, and tool fidelity
- **30% fewer tokens**: Glean averaged ~43k tokens vs ~83k for off-the-shelf tools when both produced correct responses
- **Complexity scales the gap**: 66% win rate on simple tasks → 73% on complex, multi-step queries
- **Federated search token tax**: Off-the-shelf tools relied on brute-force search (more tool calls, more reasoning loops) to compensate for missing centralized indexing

**Authors**: Neil Dhruva (Engineering), Karthik Rajkumar (Applied Scientist), Chenhao Yang (Software Engineer), Julie Mills (PMM)

The benchmark demonstrates that **context layer quality** (centralized indexing + knowledge graph) directly determines both output quality and token cost — a finding with direct ROI implications as enterprise token consumption accelerates.

### Glean MCP Gateway (June 2026)

Glean announced **MCP Gateway**, an enterprise-grade context layer built on top of the Model Context Protocol (MCP). While standard MCP servers provide a protocol for AI-to-tool communication, MCP Gateway adds the enterprise context — precomputed indexes, permission-enforced access, knowledge graph connections — that turns generic tool access into secure, actionable enterprise AI.

**Three Pillars of MCP Gateway:**

1. **Context** — Precomputed indexes + knowledge graph enable Glean's MCP server to be preferred ~2.5x over off-the-shelf MCP tools while consuming 30% fewer tokens. Instead of joining enterprise data at runtime (burning tokens on repeated retrieval), Glean precomputes joins across the Enterprise Graph.

2. **Secure access** — Permission-enforced connectors with IdP-backed authorization (OAuth via Glean Auth Server), granular access controls, and AI security checks including prompt injection detection, malicious code scanning, and toxic content filtering.

3. **Centralized rollout via MDM** — Auto-deploy to managed devices, auto-updates, configuration-only on-device (server runs on Glean's side), enabling IT teams to deploy MCP access without endpoint configuration burden.

**Concrete example**: A customer support engineer asks about the Agent Library UI showing an old 2-tab layout. Glean's MCP Gateway identifies the owner, flag state, tenant override, and ranked checklist — delivering a complete, actionable answer. An off-the-shelf MCP stack declines to name the owner and asks permission to start investigating.

**Insights dashboard**: Active users, MCP calls, tools used, period-over-period deltas, top host apps, and a Usage Breakdown table by user/application/tool/server.

Available now via request.

**Authors**: Aditya Kumar, David Hamilton, Harshi Murthy, Mohit Gupta, Roshan Dheram, Daniel Martinho

Source: raw/articles/2026-06-04_glean_introducing-glean-mcp-gateway.md

Glean's platform is built on four pillars: Enterprise Context (connectors + knowledge graph), Glean Search (cross-app search), Glean Assistant (personalized AI copilot), and Glean Agents (autonomous task automation). The platform enforces agent behavior at runtime for reliability, and provides an open agent architecture for enterprise extensibility.

### Token Yield Framework (June 2026)

Glean published a thought leadership piece framing enterprise AI economics around **token yield** — useful outcome per token consumed. The core argument: rising token consumption without proportional business value is an architecture problem, not a model problem. Four architectural levers determine token efficiency:

1. **Context quality** — Centralized indexing cuts token waste by eliminating noisy retrieval and redundant tool calls
2. **Model routing** — Right-sizing model intelligence per step; not every step needs frontier reasoning
3. **Continual learning** — Systems should learn from prior execution to avoid paying the same exploratory cost repeatedly
4. **Harness design** — Context should be managed (scoped, distributed, externalized) rather than accumulated

The article reframes the competitive landscape: "The real AI moat is execution efficiency" — not model access, but architecture that extracts more useful work per token.

Source: [[raw/articles/2026-06-03_glean_token-yield-architecture]]

## AI Stack Architecture (June 2026)

Glean published a comprehensive overview of its AI stack for software engineers, detailing the component architecture:

| Component | Function |
|-----------|----------|
| **Agent Builder** | Low-code agent creation with firm-specific playbooks and guardrails |
| **Agent Governance** | Policy enforcement, access control, and audit trails for agent actions |
| **Agent Orchestration** | Multi-step execution planning across enterprise tools and data sources |
| **Agent Library** | Pre-built agents (500+) for common enterprise workflows |
| **Enterprise Graph** | System of context connecting people, documents, conversations, and code |
| **Personal Graph** | Per-user relevance ranking based on individual work patterns |
| **Hybrid Search** | Combines keyword, vector, and knowledge graph retrieval |
| **Model Hub** | Multi-LLM support (Gemini, Claude, GPT) with model selection routing |
| **Agentic Engine** | Plan-and-adapt execution layer that decomposes tasks and retrieves context in real-time |

The architecture emphasizes **context layer quality** as the primary determinant of output quality and cost — a finding consistent with Glean's MCP benchmark results (30% fewer tokens vs off-the-shelf tools). The platform is built on the principle that enterprise AI must "plan & adapt over company context" rather than relying on general-purpose reasoning alone.

### Research: AI Productivity Paradox for Software Engineers

Glean published research examining the gap between perceived and actual AI productivity gains for software engineers, authored by **Trevor Gile**, Agentic systems solutions architect.

**The AI Productivity Paradox:** A randomized controlled trial of experienced developers found that AI tools took **19% LONGER** to complete tasks, even though the same developers believed AI sped them up by 20%.

**Three Gaps:**

1. **Outcome gap** — Time saved on typing is consumed by rework and integration effort. Code generation speed increases, but code comprehension and debugging overhead also increase.
2. **Trust gap** — Only 33% of developers trust AI code accuracy; 46% actively distrust it. 66% say "almost right, but not quite" is their biggest frustration with AI-generated code. 45% report debugging AI code takes longer than writing it from scratch.
3. **Safety gap** — 45% of AI-generated code contains high-severity vulnerabilities (XSS, SQL injection), requiring additional security review layers.

**Two-layer model:** The research frames the solution as a two-layer architecture — coding surfaces above a shared context layer — which aligns with Glean's existing AI stack design. The bottleneck has shifted from code creation to **context assembly**: understanding existing codebases, ownership, intent, and integration points before writing new code.

**Customer examples:** LinkedIn reported $2.4M in savings in the first year using Glean's context layer for developer onboarding; Uber saw 20% faster onboarding for new engineering hires.

Source: raw/articles/2026-06-05_glean_generative-ai-for-software-engineers-is-more-than-code-completion.md

### Snowflake Data Integration (June 2026)

Glean Assistant gained the ability to **query Snowflake data warehouses directly via natural language**, bridging enterprise search with structured data analytics. Users can ask questions about sales, customer, or operational data stored in Snowflake without SQL knowledge. The integration follows Glean's enterprise context layer pattern — Snowflake tables and views are indexed through the Enterprise Graph, enabling cross-source queries that combine documents, chat logs, and database records in a single interaction.

Source: raw/articles/2026-06-03_glean_query-snowflake-data-in-glean-assistant.md

## Related

- [[entities/cohere]] — potential embedding/model partner; complementary search vs model layer
- [[entities/anthropic]] — Claude is a supported model within Glean's multi-LLM platform
- [[entities/openai]] — GPT models are available through Glean's multi-LLM approach
- [[entities/hebbia]] — competitor in enterprise AI search for knowledge workers
