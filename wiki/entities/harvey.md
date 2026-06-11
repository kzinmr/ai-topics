---
title: "Harvey"
type: entity
created: 2026-05-08
updated: 2026-06-03
tags:
  - security
  - company
  - ai-adoption
  - model
  - evaluation
  - benchmark
  - harness-engineering
aliases:
  - "Harvey Agentic SOC" ["Harvey AI", "Counsel AI Corporation"]
sources:
  - https://www.harvey.ai/
  - https://www.harvey.ai/blog
  - raw/articles/2026-05-26_harvey-ai-initial-results-legal-agent-benchmark.md
  - raw/articles/2026-06-02_harvey_why-we-built-our-own-cloud-agent-infrastructure.md
  - raw/articles/2026-06-02_harvey_how-ai-is-transforming-contract-review-software.md
---

# Harvey

Harvey is a domain-specific AI platform for the legal and professional services industry. Built on customized large language models, it provides tools for contract analysis, legal research, due diligence, drafting, and end-to-end legal workflow automation for law firms and corporate legal departments.

| | |
|---|---|
| **Type** | AI Platform / Vertical SaaS (Legal) |
| **Founded** | 2022 (San Francisco, CA) |
| **Leadership** | Winston Weinberg (Co-founder & CEO), Gabriel Pereyra (Co-founder & President) |
| **Key Products** | Harvey Assistant, Harvey Vault, Harvey Knowledge, Harvey Workflow Agents, Harvey Mobile, Contract Intelligence |
| **Website** | [harvey.ai](https://www.harvey.ai) |
| **Blog** | [harvey.ai/blog](https://www.harvey.ai/blog) |
| **Tech Blog** | [harvey.ai/blog](https://www.harvey.ai/blog) |

## Key Facts

- Founded by Winston Weinberg (former O'Melveny litigator) and Gabriel Pereyra (former DeepMind/Google Brain research scientist)
- One of the first recipients of investment from the OpenAI Startup Fund
- Valuation reached $8 billion by October 2025; backed by Sequoia, Andreessen Horowitz, GV, Kleiner Perkins, Coatue
- Adopted by 100,000+ lawyers across 1,400+ customers in 60 countries; 60%+ of AmLaw 100 firms
- Revenue reached ~$190M in 2025

## Products & Technology

Harvey's platform includes: Assistant for document Q&A and drafting, Vault for secure document storage and bulk analysis, Knowledge for complex legal research, and Workflow Agents for end-to-end legal task execution (e.g., due diligence, compliance reviews). Named after Harvey Specter from the TV show *Suits*. Integrates with law firm workflows and existing practice management tools.

## Cloud Agent Infrastructure (June 2026)

Harvey built its own cloud agent runtime rather than relying on managed platforms from frontier labs or cloud providers. Co-founder **Gabe Pereyra** published a detailed rationale covering three core requirements the team believes no general-purpose runtime meets today.

### Multi-Model Routing

Law firms face a novel constraint: **client conflicts over model providers**. A firm that represents a model-provider client (e.g., a company building its own models) cannot send that client's matters through a competitor's model. As more enterprises train their own models, the set of firms caught by this constraint grows quickly.

Beyond conflicts, quality and cost optimization demand multi-model access. Harvey's [[concepts/ai-benchmarks/legal-agent-benchmark]] shows clear separation by practice area and task type — different models lead in different domains. The industry is shifting from "Which model is best?" to "Which model is most efficient for this specific task?"

Platform risk is another driver. Committing to a single managed runtime means lock-in at the agent-workforce level — agents built in one provider's format cannot be moved. Pereyra distinguishes between frontier-lab runtimes (maximum lock-in, tied to one model family) and cloud-provider runtimes (model-flexible but lag on newest models). Harvey operates an **abstraction layer** that normalizes the harness, sandbox, and behavioral differences beneath a single interface, making the choice of model a routing decision.

### Zero Data Retention (ZDR)

Every law firm and enterprise contract requires ZDR — customer data cannot sit on a third party's servers. This is a **gate requirement**, not a negotiable feature, because legal data is privileged and confidential.

Pereyra makes a critical architectural distinction: ZDR cannot be achieved by storing data during execution and calling a deletion endpoint afterward. That is "retention followed by deletion," which is architecturally different from true ZDR. True ZDR means designing the runtime so customer data is **not written into durable application storage by default**. Agent sandboxes use a transient working disk lifecycle-bound to the sandbox, automatically cleaned up on teardown.

Because Harvey owns the runtime, the agent's entire lifecycle runs inside its security boundary. State is scoped to the session and purged, making the ZDR guarantee cover the whole workflow rather than just the final model call.

### Cost Optimization

A single agent run can involve hundreds of model and tool calls over large corpora. Routing everything to the best frontier model is not sustainable at scale. Harvey's LAB benchmark confirms that for many task types, open-source models match frontier quality at a fraction of the cost.

Owning the runtime enables fine-grained control over both model routing and the execution sandbox:
- Route each task to the most efficient model meeting the quality threshold
- Optimize sandbox behavior (file loading, parallelization, compute sizing) around legal workloads
- Host open-source models internally

The combined effect: **3-5x cost reductions** versus a frontier-only approach, depending on model and workload. This level of optimization is structurally unavailable to teams building on top of someone else's runtime.

### Sovereign Deployments

Harvey's largest and most regulated customers increasingly want **sovereign deployments** — the option to self-host their cloud agent infrastructure inside their own boundary. This requires conflict-aware governance that encodes which models a given matter is even allowed to touch, plus a complete inspectable record of every agent action for work-product and privilege purposes.

### Design Principle

Pereyra frames the runtime ownership as temporary — many gaps will close as cloud providers improve — but durable for the legal-specific layer: multi-cloud resilience, data residency, conflict governance, and audit trails are not problems a general-purpose runtime will solve for the legal industry.

See also: [[concepts/harness-engineering/agent-harness]] (runtime abstraction, tool-call normalization), [[concepts/security-and-governance/agent-sandboxing]] (ZDR, transient disk, lifecycle-bound state), [[concepts/multi-agents/agent-team-swarm]] (agent workforce lock-in risk).

## Contract Review Platform (June 2026)

Harvey's contract review software evolved from single-shot prompts to a full platform model with **500+ pre-built agents** and an **Agent Builder** that lets teams codify their own playbooks — customers have built over **25,000 custom workflows**.

### Five Shifts Reshaping AI Contract Review

**Shift 1: From Single-Shot Prompts to Agentic Workflows.** First-generation tools were prompt-and-answer: useful for one-off questions but not for the multi-step, contextual shape of legal work. Harvey Workflow Agents decompose a review objective into stages (ingest → classify → extract → flag → compile → draft), running the full pipeline without per-step prompting.

**Shift 2: Citation Grounding as the Defensibility Bar.** ABA Formal Opinion 512 makes lawyers responsible for verifying AI-generated work product. Every clause extraction links to the source paragraph; every comparison shows underlying language side-by-side; every drafted redline cites the playbook or precedent that informed it. This is the line separating platforms built for legal work from general-purpose models repurposed for it.

**Shift 3: Bulk Review at Platform Scale.** Harvey Vault handles up to **100,000 documents** per project with structured review tables that extract data across the full agreement set in one query. The reviewer's time shifts from "did I get to every document" to working through structured exceptions.

**Shift 4: AI Meets You Where You Already Work.** Harvey integrates with Microsoft Word (in-context drafting, redlining), Outlook (inbox analysis and response), DMS platforms (iManage, NetDocuments, SharePoint — maintaining access controls), and Microsoft 365 Copilot. The adoption-critical insight: "where the AI lives is now a primary evaluation dimension."

**Shift 5: Firm-Specific Playbooks Scale Across Every Matter.** Agent Builder lets partners and legal ops teams codify firm precedent into reusable agents deployed across every relevant matter. The 25,000+ custom workflows running on Harvey are evidence that this is how firms want to operationalize AI. The playbook is the asset — the platform that lets a firm scale it across every matter compounds the firm's value over time.

### Customers and Results

- 142,000+ legal professionals across 1,500+ organizations in 60+ countries
- Customers include GSK Stockmann and PwC
- Up to **75% time savings** on unstructured data rooms (GSK Stockmann)
- Vault supports up to 100,000 documents with structured review tables
- Redlining time: minutes per document with firm playbook applied
- Custom workflows reduce 3-4 hour tasks to 3-4 minutes

See also: [[entities/claude]] (ABA Opinion 512 compliance via citation grounding), [[concepts/ai-agent-engineering]] (multi-step decomposition, agent classification/document extraction pipelines).

## Agentic Security Operations Center (May 2026)

Harvey's security team, led by **Mike Parowski**, built an agentic SOC — a system of always-on AI agents that hunt, triage, investigate, author detections, and learn from one another. Built on a persistent, machine-readable **security world model** of Harvey's threat surface.

### Architecture

- **Security world model**: Petabytes of historic data, ~5,300 persistent memories, 2,500+ investigations/30 days, 400+ production detections. Comprises: (1) a raw analytics corpus (TBs/day telemetry in optimized ClickHouse tables), (2) an MCP server via RunReveal for agent-accessible tools, (3) a threat model system prompt structured as paths to crown jewels, (4) a self-improving intelligence layer of hunting/alerting agents.
- **Data layer first**: Semantically-enriched, column-pruned ClickHouse tables with normalized fields (e.g., `isProdCluster` derived from raw JSON). "Invest in your log warehouse before you invest in your agents" — the difference between 200ms and 2s per query is the difference between 3 and 30 hypotheses explored.
- **Round-the-clock operation**: Daily reports (alert volume, detection performance), hourly alert triage (semantic clustering + auto-escalation), threat-watch workflow ingesting CISA KEV and cross-referencing against deployed coverage.
- **Persistent memory**: Postgres-backed knowledge base with categorized facts (entity, finding, baseline), TTLs, Jaccard dedup, per-profile injection budgets. Human analyst annotations persist as agent memories with `source='analyst'`.

### Results
- Coverage expanded from 75 → **400+ deployments** (5.7x increase)
- Weekly alert volume reduced from ~300,000 → **~20,000** (95% reduction)
- CVE/breach response from hours/days → **minutes** (one-button push investigation)
- Detection pipeline uses four-phase agent pipeline: research → consolidate → validate → finalize with human review on every PR

### Design Principle
The agentic SOC operates on top of Harvey's trust boundary, separate from Spectre (product agent platform), to prevent privilege escalation — SOC knowledge of detections/internal topology is isolated from product agent access.

## Legal Agent Benchmark (LAB) — May 2026

Harvey released the **Legal Agent Benchmark (LAB)**, an open-source benchmark for evaluating AI agents on complex, long-horizon legal tasks. See [[concepts/ai-benchmarks/legal-agent-benchmark]] for full details.

### Key Highlights
- **All-pass grading**: Expert-curated rubrics require every criterion to pass — mirroring strict legal review standards
- **Behavioral traces**: LAB captures agent action sequences (Read → Search → Execute → Write → Validate → Edit) for behavioral analysis
- **Initial results**: Frontier models complete <10% of legal tasks end-to-end (Opus 4.7 leads at 7.1%)
- **Jagged intelligence**: Different models lead different practice areas — GPT-5.5 in research-heavy groups, Opus 4.7 in analytical work, Sonnet 4.6 in structured comparison
- **Cost at frontier**: Opus 4.7 costs ~$50.90/task at ~22 min latency; GPT-5.5 is ~3x cheaper
- **Self-correction is the strongest signal**: Agents that verify AND revise after drafting improve by +1.5 points on all-pass
- **Partnership with Artificial Analysis** for a regularly-updated leaderboard
- **Kimi 2.6 agent (June 2026)**: Harvey deployed a [[entities/kimi|Kimi 2.6]]-powered agent that beat Opus 4.7 on Harvey's internal legal benchmark at ~11x lower cost — demonstrating the cost-efficiency advantage of routing to specialized models

### Behavioral Findings
- **Positive behaviors**: Thorough research (+0.4), post-draft validation (+0.8), verifying and revising (+1.5), targeted retrieval (+0.3), structured analysis (+0.3)
- **Negative behaviors**: Noisy tool fan-out (-0.5), drafting without review (-1.2)
- Opus 4.7: Most self-corrective (more drafting + validation). GPT-5.5: Heaviest search user (wider document coverage)

## Related

- [[entities/openai]] — early investor via OpenAI Startup Fund; built on GPT technology
- [[entities/voyage-ai]] — partnered to build custom legal embedding models
- [[entities/anthropic]] — competitor in the enterprise AI deployment space
- [[entities/hebbia]] — serves overlapping legal/financial professional services customers
- [[entities/courtlistener]] — provides the 9M+ US case law opinions database powering Harvey's Knowledge feature

## US Case Law Knowledge Source (June 2026)

Harvey integrated **9 million+ US case law opinions** from [[entities/courtlistener]] directly into the platform, enabling lawyers to research, analyze, and draft with case law citations in one place. Lawyers spend **19% of their time** on case law research; fragmented tools multiply that cost through context-switching.

### Key Capabilities

- **Direct case law access**: Millions of opinions searchable within Harvey — no separate window or tool needed
- **Citation-grounded responses**: Harvey's answers include direct citations to source material for validation
- **Side-by-side viewing**: Case content displayed alongside results for quick verification
- **Cross-source search**: Lawyers can search across case law AND uploaded files in a single prompt (e.g., pulling evidence from a vault and analyzing against existing precedent)
- **Word Add-In integration**: Pull case law insights directly into Word documents for drafting motions and briefs
- **Agent Builder workflows**: Embed US Case Law knowledge source into custom agents for repeatable workflows (e.g., employment investigations, trial prep connecting witness testimony to legal doctrine)

### Availability

Available from June 3, 2026 on a rolling basis to Harvey customers. The knowledge source includes over 9 million opinions sourced from CourtListener.

Source: raw/articles/2026-06-03_harvey_us-case-law-source.md
