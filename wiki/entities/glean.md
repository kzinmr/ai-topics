---
title: "Glean"
type: entity
created: 2026-05-08
updated: 2026-08-05
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
  - raw/articles/2026-05-10_glean_the-definitive-guide-to-ai-based-enterprise-search-for-2025.md
  - raw/articles/2026-05-15_glean_cowork-mcp-eval.md
  - raw/articles/2026-05-21_glean_health-agents-2026.md
  - raw/articles/2026-06-02_glean_generative-ai-stack-for-software-engineers.md
  - raw/articles/2026-06-03_glean_query-snowflake-data-in-glean-assistant.md
  - "[[raw/articles/2026-06-03_glean_token-yield-architecture]]"
  - raw/articles/2026-06-04_glean_introducing-glean-mcp-gateway.md
  - raw/articles/2026-06-05_glean_generative-ai-for-software-engineers-is-more-than-code-completion.md
  - raw/articles/2026-06-22_glean_what-is-no-code-automation.md
  - raw/articles/2026-07-01_glean_introducing-independent-agents.md
  - raw/articles/2026-08-01_glean_agent-orchestration-platforms-compared.md
  - raw/articles/2026-08-01_glean_glean-information-retrieval.md
  - raw/articles/2026-08-01_glean_work-ai-index-uk.md
  - raw/articles/2026-05-10_glean_knowledge-graph-agentic-engine.md
  - raw/articles/2026-07-28_glean_enterprise-knowledge-graph-cases-7-applications-that-deliver-roi.md
  - raw/articles/2026-07-09_glean_the-enterprise-ai-copilot-playbook-for-business-leaders.md
---

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

### Knowledge Graph & Agentic Engine (Jun 2025)

Glean's technical deep-dive (authors Rob Stets, Pradeep Vaghela, Julie Mills) explains why the **knowledge graph is the foundation of its agent reasoning engine**: enterprise AI needs context that reflects how the organization actually works — triplets connecting people, documents, tools, projects, and systems.

**KG mechanics:**
- **Triplet structure** (subject, predicate, object): e.g., (engineer A, owns, Jira ticket B), (doc X, references, project Y) — the graph's edges enable inference and complex queries across organizational silos.
- **Edge properties**: timestamps, access control, confidence scores, and provenance attach to each relation, letting the system reason with governance-critical metadata (e.g., when a reporting relationship started, whether info came from calendar vs email).
- **Fine-grained access control**: the whole graph is designed so employees only see data already shared with them in source systems.

**Documented LLM failure modes that the KG addresses:**
1. **Proximity over precision** — LLM misassigned a marketing manager's title based on a Slack message about an event she hosted.
2. **Entity confusion** — Claude 3.7 Sonnet vs Claude 3.5 Sonnet v2 are distinct models but LLMs merge them into one wrong answer.
3. **Deterministic queries** — "list all account executives in Asia" requires mapping query terms to specific job titles/locations, then an exhaustive structured query.
4. **Multi-hop relationship reasoning** — "where do I file feature requests for Reddit?" needs disambiguation (social platform vs customer) plus process knowledge (Jira involved).

**Three-phase KG construction** (first two phases now LLM-enhanced): (1) entity annotation from natural language, (2) intent understanding via seeded query patterns expanded from query logs, (3) fulfillment — structured queries traversing the graph.

**Enterprise KG difficulty:** Unlike public graphs (Google/Bing), enterprise graphs cannot rely on manual review — privacy and scale forbid it. Glean's automated pipeline: noun phrase extraction → frequency/prominence filtering → entity-prominence evidence (titles, link frequency, shared files) → predicate identification → continuous algorithmic refinement. Built on the same real-time crawler architecture as its search index, refined over 6 years.

**Personal Graph:** a new dimension capturing individual digital activity streams (atomic actions → sub-tasks → context-labeled tasks → themed clusters mapped to OKRs). Unlike chat-session memory, it synthesizes activity across tools, systems, and time — enabled by LLM reasoning over sparse, cross-source signals. Already powering "what I worked on last week" and performance-review quick-start agents.

**Context System thesis:** data + people + **process** (how work actually happens) form a third context layer. Closing claim: "the cognition of agent systems is not just the LLM — it is also the context system."

Source: [[raw/articles/2026-05-10_glean_knowledge-graph-agentic-engine]]

### Enterprise Knowledge Graph Cases (July 2026)

Glean's vendor-education piece frames enterprise knowledge graphs as company data modeled as a **connected network** (customers, products, contracts, employees, systems and the relationships between them) "so queries traverse meaning rather than match columns." Core claim: most enterprise data is "broken because it is disconnected" — McKinsey: employees spend 20% of the working day searching for information; 2024 Pyron report: 47% of professionals spend 1–5 hours/day on the same search problem. Market: **$2.89B in 2025, 21–33% CAGR**; Gartner expects cloud platforms to integrate KG services as standard infrastructure.

**Seven ROI use cases:**

| Use case | Core idea |
|----------|-----------|
| Content as structure | NLP entity extraction + automated metadata enrichment turn content management into a self-enriching index; semantic tagging links documents to product/segment/regulation/owner nodes |
| Institutional knowledge | Unified expertise profiles (employee nodes → projects, documents, systems, decisions); offboarding returns a structured transfer brief; 60% say crucial info is hard to get, 90% say retirees cause serious knowledge loss |
| AI grounding (GraphRAG) | "The most urgent KG use case in 2025 isn't search — it's making generative AI safe enough to deploy"; 77% of businesses concerned about hallucinations, 47% of enterprise AI users made a major decision on hallucinated content in 2024 |
| Drug discovery / life sciences | Compounds→targets→pathways→diseases→cohorts as one graph; drug repurposing via evidence traversal; regulatory submission lineage |
| Fraud & risk | Property-graph modeling + Jaccard similarity / community detection surfaces fraud rings relational DBs miss; AML pathfinding across dozens of hops |
| Workflow automation | Inferred relationships fire events (churn-risk sales alerts, cross-team approval orchestration, inventory/resource allocation as traversal) |
| Security/compliance/governance | Graph-based access controls (permissions as edges), provenance/audit trails on every node, regulatory taxonomies as graph nodes |

**GraphRAG vs vector RAG:** GraphRAG wins on **multi-hop reasoning** (Microsoft's GraphRAG uses community detection for hierarchical summaries enabling global reasoning); production teams converge on **hybrid vector + graph retrieval** with the graph acting as a verification layer. Cited data: LinkedIn cut support ticket resolution 40h→15h (63%) via GraphRAG routing; FalkorDB's GraphRAG SDK claims 90% hallucination reduction vs traditional RAG with sub-50ms latency; ACL Anthology research confirms KG-augmented LLMs beat ungrounded models on factual accuracy in healthcare/finance/legal. ROI example: a global IT services firm's graph-backed knowledge assistant across 300 support agents saved 15,000+ agent hours, shortened implementation timelines 11%, and lifted customer retention 3.8%.

**Adoption guidance:** start with one domain + a pragmatic ontology ("model only what you'll actually query"), measure baseline then at 30/60/90 days; KG sits as a semantic layer above existing systems — no migration required. FAQ distinguishes a **knowledge graph** (stable domain facts) from a **context graph** (user intent, role, workflow state, recent activity — "especially useful for personalization and agentic AI"). Related skeptical view: [[concepts/graph-db-overengineering-rag|"You Don't Need a Graph DB for RAG (Probably)"]].

Source: raw/articles/2026-07-28_glean_enterprise-knowledge-graph-cases-7-applications-that-deliver-roi.md

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

### No-Code Automation Guide (June 2026)

Glean published a no-code automation guide positioning **Agent Builder** and the **Agent Library** (500+ pre-built agents) as enabling business users to build AI-powered workflows without coding. Authored by **Trevor Gile** (Agentic systems solutions architect), the guide compares no-code, low-code, and traditional development approaches, highlighting Glean's visual workflow builder, triggers, actions, conditional logic, and enterprise governance controls as key differentiators.

Source: raw/articles/2026-06-22_glean_what-is-no-code-automation.md

### Independent Agents (June 2026)

Glean launched **Independent Agents**, a new class of AI coworkers built on Glean's context layer that work autonomously across enterprise tools. Unlike channel-specific assistants, these agents act across surfaces (Slack, Jira, Teams) with context carrying seamlessly between them.

**Four key characteristics:**
1. **Identity with context** — Each agent operates with its own identity and provisioned access, independent of any user's permissions. Traceable and controllable.
2. **Memory** — Learns from company documentation and every interaction, extracting best practices and avoiding repeated mistakes.
3. **Proactivity** — Acts without being asked: suggests solutions, tags stakeholders, provides regular summaries of key learnings.
4. **Accountability** — Every run is auditable (tool calls, decisions, outputs). Inherits Glean's security model. Emergency stop button for admin disable.

**OnCall Assistant (first agent, beta):** When an alert fires, the agent reads the escalation, pulls relevant context, pursues multiple root-cause theories simultaneously, drafts a fix for review, and tags the right owner. By the time a human steps in, the first ~30 minutes of investigation are already done.

Source: raw/articles/2026-07-01_glean_introducing-independent-agents.md

### Agent Orchestration Platforms Compared (August 2026)

Glean published a six-platform comparison of agent orchestration options, sorting by product type — developer frameworks, no-code automation, and enterprise/cloud platforms — evaluated on seven criteria (workflow control, state/retries/recovery, multi-agent coordination, security/permissions, observability, integrations/openness, ease of use).

| Platform | Type | Position |
|----------|------|----------|
| **Glean** | Enterprise platform | Cross-department orchestration over company knowledge; durable execution, branching/looping, routing, approvals, permission-aware context, trace-level debugging |
| **Gemini Enterprise Agent Platform** (formerly Vertex AI) | Cloud-native | ADK code-first multi-agent dev, Agent Studio, Model Garden (200+ models), A2A + MCP |
| **LangChain/LangGraph** | Framework + LangSmith platform | Graph-based workflows, durable execution with checkpointing; you supply retrieval/permissions |
| **CrewAI** | Framework + AMP | Crews/flows, sequential & hierarchical processes, guardrails; open-source core, hyperscaler-agnostic |
| **Lindy AI** | No-code automation | Visual builder, natural-language agent setup; department-scale |
| **Microsoft Agent Framework + Foundry** | Framework + cloud | Graph workflow engine, deterministic branching; MCP + A2A, portability outside Microsoft needs testing |

Key thesis: the category has blurred because every vendor uses "agent orchestration," but buyers differ by who owns workflows and where context lives. The article's rough test — "if the job fits one prompt and one tool call, skip the platform; if it needs routing, conditional logic, parallel work, human approval, or a durable record, orchestration belongs in production architecture." Context cites Glean's Work AI Index finding that while 87% use AI at work and 75% save ~11 hours/week, only 13% say their organizations perform significantly better — framing the gap as "an orchestration and governance problem." Also cites 36% of AI sessions failing outright, motivating checkpointing/durable-execution requirements.

### Comprehensive Guide to Information Retrieval (August 2026)

Glean published an educational IR guide explaining retrieval fundamentals as applied across its 250+ connected enterprise applications:

- **IR model families**: Boolean model (logical operators AND/OR/NOT), vector space model (documents/queries as vectors), probabilistic model (relevance as probability), language model (documents as sequences from a generative language model). Modern systems combine sparse keyword retrieval with dense neural retrieval in a hybrid approach.
- **System components**: document collection, indexing, query processor, ranking algorithm, user interface.
- **Five enterprise use cases**: document management, customer service (knowledge base retrieval), data analytics, e-discovery (legal), and enterprise search — Glean Search brings these together with permission-aware, cited results across email, documents, tickets, and chat.

### Definitive Guide to AI-Based Enterprise Search (May 2026)

Glean's long-form educational guide ("The definitive guide to AI-based enterprise search for 2025", scraped 2026-05-10) frames AI enterprise search as a shift from keyword matching to intent/context understanding, and surveys the vendor landscape:

- **Traditional vs AI-powered search**: keyword matching → intent & context understanding; generic results → personalized role-based results; limited cross-platform → unified search across all business tools; manual relevance sorting → intelligent ranking.
- **Enterprise Graph**: dynamic knowledge model linking people, data, and processes, continuously updated; maps relationships between employees, projects, documents, and business processes.
- **Code intelligence**: AI-driven understanding/summarization/navigation of code repositories — automatic function discovery, dependency mapping, code summarization, cross-reference generation between code and documentation. Glean's AI Assistant provides instant document summaries, dependency analysis, code quality assessments, change-impact analysis, and automated documentation generation.
- **Integration scale**: Glean integrates with 100+ SaaS apps and enterprise data repositories with real-time indexing.
- **Platform comparison table** (5 vendors):

| Platform | Key Strengths | AI Innovation | Integration Focus |
|----------|---------------|---------------|-------------------|
| **Glean** | Enterprise Graph, comprehensive security | Advanced LLMs, code intelligence | 100+ SaaS applications |
| **Moveworks** | Agentic AI, employee experience | Reasoning Engine, intent detection | IT service management |
| **Coveo** | Personalized recommendations | AI-powered relevance | E-commerce, digital experience |
| **Elastic** | Customizable, open-source | Security analytics, observability | Technical infrastructure |
| **Guru** | Governed knowledge management | Content verification, trust scoring | Knowledge management |

- Notes Glean's $150M Series F funding round and Glean Protect (real-time permission checks, audit logging, GDPR/SOC 2 compliance support).
- Future trends: democratization of AI across the workforce, advances in RAG (citation-backed answers grounded in organizational knowledge), AI agents automating multi-step cross-application processes (onboarding, compliance checking).

### UK Work AI Index — Policy vs Verification Gap (August 2026)

Glean's Work AI Institute surveyed 1,500 UK digital workers as part of a global study of 6,000 (US, UK, Australia). The UK shows the strongest institutional AI environment — 65% have read their organization's AI policy in full (vs 57% US), 73% express confidence in AI at work, and 42% say AI is embedded in core workflows (vs 32% US) — yet the productivity gap persists:

- UK workers report saving **12 hours/week** via AI automation, but only **18%** say gains translated into significantly better organizational performance.
- **38% of AI-related time** is "botsitting" (supplying context, reviewing outputs, debugging, rerunning prompts) vs 36% producing work.
- **37%** sometimes ship AI-assisted work they haven't fully checked (36% US); **70%** report at least one "botshitting" behavior; 40% deliver work they couldn't explain; 34% use unapproved tools; 24% blamed AI for their own mistakes.
- **77%** corrected or redid AI-assisted work in the past month (26% weekly).
- Half of UK workers say important information isn't accessible through their AI tools; 60% rerun the same prompt across multiple AI tools.

The report argues institutional policy confidence creates a blind spot: policy establishes permission, but verification happens inside the work. It cites the 2025 High Court warning that solicitors/barristers could face contempt proceedings for AI-generated fabricated citations, with the SRA and Bar Standards Board reinforcing that responsibility sits with the lawyer. Recommendation: set review standards by risk, name the accountable person, build checks into workflows, and give approved tools the context they need.

### Enterprise AI Copilot Playbook (July 2026)

Glean published a vendor playbook for business leaders on deploying an **enterprise AI copilot** — a platform that connects to internal systems (documents, conversations, tickets, CRM, code repos) and delivers cited, permission-aware answers through a conversational interface. Key definitions and guidance:

- **Copilot vs chatbot vs general-purpose AI assistant**: a chatbot is a phone tree (scripted); a copilot is a knowledgeable colleague that handles messy questions ("What did we decide about the EMEA pricing change in last week's Slack thread?"); general-purpose AI assistants (consumer ChatGPT) don't know your company.
- **Assistants vs agents vs agentic AI**: assistants are reactive (you ask, it answers, grounded in company data); agents work best for repeatable, rule-based, high-volume workflows (ticket routing, CRM updates, compliance checks); agentic AI is the orchestration + governance layer underneath (multi-step planning, enforced approvals, audit trails). Shortcut: "If you'd explain the task to a new hire in a conversation, use an assistant. If you'd hand them an SOP and a checklist, build an agent."
- **RAG grounding**: connectors pull data → index/chunk → knowledge graph maps relationships → retrieval finds relevant content → LLM generates cited answers. Glean positions its Enterprise Graph (100+ connected apps) as real-time permission-aware indexing rather than nightly batch sync.
- **Deployment models**: Cloud SaaS (weeks to value; TIME magazine live in 3 weeks), Hybrid (2–4 months, regulated industries), On-premise (4–6+ months, government/defense).
- **Governance non-negotiables**: RBAC, audit trails, SOC 2/HIPAA/GDPR/FedRAMP compliance built in from day one.
- **Phased rollout roadmap**: Foundation (weeks 1–4, 50–100 pilot users across 2 departments) → Expansion (weeks 5–12, 2–3 agents live) → Scale (weeks 13–24, org-wide) → Optimize (ongoing, quarterly ROI reporting).

**Adoption case studies cited:**
- **Confluent**: support engineers burned 5–10 min/ticket finding context → dropped to near zero after copilot deployment
- **TIME magazine**: CIO Sharon Milz reported live in 3 weeks on cloud SaaS
- **Zillow**: "AI Days" sessions where employees built agents in small pods → **80% adoption**
- **GCash**: word-of-mouth drove **90%+ adoption** in some departments (colleagues saving 2–3 hours/week)
- **Super.com**: new hires ramped **20% faster** using search + org chart
- **Forrester TEI**: one telecom firm estimated **$8M annual savings** from call center alone (faster access to release notes/customer info)

Context: employees spend one full workday/week searching for information; the enterprise copilot market crossed a double-digit-billion-dollar run rate in 2025.

## Related

- [[entities/cohere]] — potential embedding/model partner; complementary search vs model layer
- [[entities/anthropic]] — Claude is a supported model within Glean's multi-LLM platform
- [[entities/openai]] — GPT models are available through Glean's multi-LLM approach
- [[entities/hebbia]] — competitor in enterprise AI search for knowledge workers
