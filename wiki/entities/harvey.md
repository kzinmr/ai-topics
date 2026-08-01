---
title: "Harvey"
type: entity
created: 2026-05-08
updated: 2026-08-01
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
  - raw/articles/2026-06-17_harvey_harvey-copilot-cowork-launch.md
  - raw/articles/2026-07-01_harvey_sonnet-5-in-harvey.md
  - raw/articles/2026-07-17_harvey_y-combinator-backed-benchmark-joins-harvey.md
  - raw/articles/2026-07-28_harvey_scaling-document-processing-across-harvey.md
  - raw/articles/2026-07-31_harvey_ai-trademark-search.md
  - raw/articles/2026-06-19_harvey_legal-operations-management.md
  - raw/articles/2026-08-01_harvey_legal-ai-vs-traditional-legal-research.md
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

### Microsoft 365 Copilot Integration (June 2026)

Harvey launched as an agent inside **Microsoft 365 Copilot** and a plugin inside **Copilot Cowork** on June 16, 2026, bringing legal intelligence directly into the Microsoft 365 productivity environment.

**@Harvey in Copilot:** Legal professionals can @mention Harvey within Microsoft 365 Copilot to get legal answers, research issues, analyze documents, and pull content from Harvey Vault — all without switching platforms. Legal teams can retrieve precedent deals, prior work product, and negotiation positions directly in the Copilot interface via Vault retrieval.

**Deep analysis escalation:** When deeper reasoning is needed, clicking a source link moves the thread into Harvey's web environment for advanced reasoning, memo drafting, and argument development.

**Key use cases:**
- **Contract review under deadline:** Flag non-standard terms with Vault surfacing prior positions taken on similar clauses
- **M&A due diligence:** Issue spotting across a document set directly within Copilot

**Copilot Cowork integration:**
- When Cowork executes multi-step tasks across Microsoft 365, Harvey's legal answers surface automatically
- **Opposition drafting:** Cowork + Harvey runs the full sequence — identify strongest arguments, surface weaknesses, draft counterargument outline as a Word document
- **Document drafting:** Ask Cowork to draft a mutual NDA; Harvey handles the drafting, Cowork delivers it as a .docx

The goal is to eliminate the tool-switching that fragments legal work, bringing Harvey's domain intelligence into the flow of Microsoft 365 where legal professionals already spend their time.

### Model Partnerships (June 2026)

Harvey integrated **Claude Sonnet 5** on June 30, 2026, making Anthropic's latest Sonnet model available in the Harvey platform. Sonnet 5 builds on Sonnet 4.6 with broad gains in legal accuracy and output quality across transactional and litigation work.

**Benchmark results:**
- **Legal Agent Benchmark (LAB):** 5.8% all-pass — a strict evaluation mirroring multi-step legal work end-to-end
- **BigLaw Bench:** 91.3% — the highest recorded across both Sonnet and Opus models at Harvey
- **Strongest practice areas:** Energy and natural resources, real estate, capital markets
- **Strongest task type:** Drafting (LAB), Risk assessment & compliance, case management, transactional drafting (BigLaw Bench)

Sonnet 5's consistent performance across litigation and transactional work, combined with cost efficiency, positions it for high-throughput legal tasks.

Source: raw/articles/2026-07-01_harvey_sonnet-5-in-harvey.md

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

## Legal Research vs Traditional Tools (July 2026)

Harvey published a comparison of AI-native legal research against traditional database research (keyword databases, Boolean strings, citators), arguing the new layer complements rather than replaces the old. The law and its authoritative databases haven't changed — what changed is the layer that finds and reasons over them.

**Three shifts AI introduces (each with a trade):**
1. **From keywords to questions** — The researcher asks in plain language ("How do courts in two states treat a liquidated damages clause...?"); the tool handles translation into searches, removing the most skill-dependent step. Trade: less visibility into what was searched, which makes source transparency a trust requirement.
2. **From result lists to reasoned answers** — Instead of 40 documents to read, the lawyer gets a synthesized answer with reasoning and supporting authority attached. Agentic research extends this: the system runs searches, follows citations, checks treatment, assembles analysis in steps. Caveat: a synthesized answer is only as good as its grounding.
3. **Grounding, citations, and the hallucination question** — General chatbots can invent authority; purpose-built legal AI retrieves from authoritative legal databases and ties every statement to an openable source. Verification remains the lawyer's job, but tools make it fast because every claim carries its citation.

**Evaluation framework — five questions for a skeptical buyer:** What sources ground the answers (and can you see them)? Is every statement traceable to an opinion or statute you can open? How does the system handle negative treatment? Has performance been measured on realistic legal tasks rather than demos? How is client data handled? Harvey points to its published results on **BigLaw Bench** (realistic legal tasks) and the **Legal Agent Bench** (agentic work) as the standard any platform should meet, and recommends the cheapest test: bring a real matter already researched by your team to the demo and compare the grounded answer.

Source: raw/articles/2026-08-01_harvey_legal-ai-vs-traditional-legal-research.md

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

## Training a Legal Agent — Applied Compute Methodology (June 2026)

Harvey published its methodology for training domain-specific legal AI agents under the concept of **Applied Compute** — a framework that goes beyond generic fine-tuning to produce agents capable of complex, multi-step legal reasoning.

### Approach

- **Domain-specific agent training**: Rather than relying on prompt engineering alone, Harvey trains agents on legal-specific workflows — contract analysis, due diligence, regulatory compliance — with behavioral traces that capture the full reasoning chain
- **End-to-end agent platform**: Harvey Agents now integrate Contract Intelligence, Knowledge, Vault, and Command Center into a unified legal agent infrastructure
- **Behavioral evaluation**: Agents are evaluated not just on final outputs but on action sequences (research → analyze → draft → validate → revise), with LAB rubrics requiring every criterion to pass
- **Applied Compute = domain expertise + compute**: The thesis is that legal AI requires domain experts who understand the workflows combined with compute resources to train specialized models — not just general-purpose models with legal prompts

### Significance

This represents a broader trend of **vertical AI agent training** — companies with deep domain expertise building their own agent training pipelines rather than relying on frontier model APIs alone. Harvey's approach mirrors what coding agent companies (Cognition, Cursor) have done for software engineering, but applied to legal reasoning.

Source: [Training a Legal Agent — Harvey Blog](https://www.harvey.ai/blog/training-a-legal-agent-with-applied-compute)

## Legal Operations Management Guide (June 2026)

Harvey published a comprehensive guide to **legal operations management** — the discipline of running the legal function like any other business unit — positioning its platform for the operational layer where legal ops teams select, deploy, and govern AI. The guide is aimed at both law firms and in-house teams, and is one of Harvey's most strategy-oriented blog pieces (vs. product announcements).

### Core Framework

- **Five core functions of legal ops**: (1) financial management (budget, spend analytics, CFO conversation), (2) outside counsel and provider management (panel programs, billing guidelines, performance reviews), (3) contract operations (lifecycle from intake to renewal), (4) technology and data (tech stack, integrations, reporting), (5) strategic planning and governance (multi-year direction, AI policy)
- **When to invest**: first dedicated legal ops hire when in-house headcount reaches ~5-10 lawyers, or annual legal spend crosses $5-10M; law firms typically at 50-100 lawyers, often triggered externally by client demand for alternative fee arrangements or pricing transparency
- **Four signals of threshold**: no central view of legal spend; invoices arrive unpredictably with anecdotal variance; contracts scattered across email/shared drives; legal team can't produce usable KPIs on request
- **Implementation tiers**: small departments assign legal ops part-time to senior counsel/paralegal; mid-sized make first dedicated Manager/Director hire to centralize spend data; large departments run multi-person functions led by a Head of Legal Operations reporting to the GC

### AI Governance as Legal Ops Responsibility

The guide argues **AI governance is the new responsibility that didn't exist five years ago** and the area where legal ops adds its most distinctive value:

- Which AI platforms the team is approved to use, and on which data
- Human-in-the-loop review checkpoints built into workflows
- Accuracy benchmarking with measurable standards before deployment and on recurring cadence after
- Acceptable use guidelines covering confidentiality, privilege, and matter-level isolation
- Audit logs producible for clients, regulators, or internal compliance reviews

**Key thesis**: "AI amplifies the maturity that already exists rather than replacing the need for it" — teams with weak templates and ad hoc processes get AI outputs that reflect those weaknesses; teams with strong playbooks, clean data, and documented workflows get AI outputs that compound. "Get the process right, then deploy the AI on top of it."

### AI Use Case Categories

1. **Contract review and clause extraction** — first-pass review of high-volume agreements (NDAs, vendor terms, standard order forms), flagging deviations from playbook, extracting key terms into structured data
2. **Drafting assistance** — first drafts of templated documents, proposed redlines based on firm standard positions, lawyer reviews/refines rather than starting from blank page
3. **Research and matter analysis** — synthesizing case law, regulatory guidance, and internal precedent into citation-grounded, verifiable answers

### Maturity Assessment & Implementation

- Uses **CLOC's Core 12 Maturity Assessment Playbook** with four-stage model: Reactive → Emerging → Developing → Leading (AI deployed with governance + predictive analytics at Leading)
- Five-phase implementation: assess maturity → prioritize 2-3 initiatives GC+CFO both recognize → secure executive sponsorship → pilot in defined scope → scale on pilot results
- Typical 12-18 month roadmap: months 1-4 centralize spend data (e-billing, intake portal); months 5-10 pilot CLM in one region; months 11-18 roll out CLM globally + deploy AI-assisted drafting with governance
- "Start narrow" principle: pick one focused use case (spend visibility or contract intake), prove value within 90 days

### Role of Domain-Specific Legal AI

The guide explicitly contrasts **general-purpose AI tools** (require lawyer to do most framing/verification) with **platforms built specifically for legal work** (ground outputs in cited sources lawyers can verify) — positioning Harvey in the latter category. Scale signal cited: 142,000+ legal professionals, 1,500+ customers in 60+ countries, 60%+ of AmLaw 100.

Source: raw/articles/2026-06-19_harvey_legal-operations-management.md

## Related

- [[entities/openai]] — early investor via OpenAI Startup Fund; built on GPT technology
- [[entities/voyage-ai]] — partnered to build custom legal embedding models
- [[entities/anthropic]] — competitor in the enterprise AI deployment space
- [[entities/hebbia]] — serves overlapping legal/financial professional services customers
- [[entities/courtlistener]] — provides the 9M+ US case law opinions database powering Harvey's Knowledge feature

## Benchmark Acquisition (July 2026)

Harvey acquired **Benchmark**, a Y Combinator-backed decision infrastructure platform for asset management based in New York City. Benchmark helps investors capture institutional knowledge and apply it to new deals, extending Harvey's platform across the full deal process — from first screen to investment committee.

Benchmark co-founders **Alec Dunn** and **Connor Janson**, along with their team, are joining Harvey's product and engineering organization. This marks Harvey's **3rd acquisition of 2026** and follows a record Q2 in which Harvey added **$100M+ in net-new ARR**.

Harvey already works with **50+ asset management firms**, including Blue Owl Capital, Bridgewater Associates, and KKR, on workflows such as investment due diligence, data room analysis, and deal document review. Benchmark's platform is trusted by firms representing **$2T+ in assets under management**.

Benchmark's investors include [[concepts/ai-industry-financial-sustainability|Y Combinator]] and the Outsiders Fund. The acquisition extends Harvey's capabilities into asset management decision infrastructure, overlapping with the [[entities/hebbia|Hebbia]] customer base in financial professional services.

### Growth Milestones Timeline

| Date | Milestone |
|------|-----------|
| 2022 | Founded by Winston Weinberg and Gabriel Pereyra |
| 2025 | $190M revenue; $8B valuation |
| May 2026 | Agentic SOC launched; Legal Agent Benchmark (LAB) released |
| June 2026 | Microsoft 365 Copilot integration; Claude Sonnet 5 integration; US Case Law Knowledge Source launched |
| **July 2026** | **Acquires Benchmark — 3rd acquisition of 2026 — expanding into asset management decision infrastructure** |

Source: raw/articles/2026-07-17_harvey_y-combinator-backed-benchmark-joins-harvey.md

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

## Document Processing Infrastructure (July 2026)

Document processing sits under Vault, Assistant, and every workflow — almost every lawyer query involves documents. Over the past year, Harvey scaled from ~0.94M documents/week (1.44 TB) to ~24.8M/week (56 TB) — a 26× increase in documents and 39× increase in data volume.

### Job Framework Rebuild

Harvey replaced the original job queue with a new Job Framework featuring durable workflow state. A worker crash or deploy mid-batch resumes instead of restarting the whole batch. Each activity has explicit timeout and retry behavior. File-level failures are isolated: corrupt, password-protected, unsupported, or empty files are marked and processing continues for the rest of the batch.

### Pipeline Splitting by Bottleneck

The extraction/chunk-embed/index pipeline was split into separate stages with dedicated capacity. Each stage retries independently, scales independently, and fails partially. OCR-heavy uploads can slow the extraction lane without starving indexing. Vector-store rate limits can back off the indexing lane without forcing extraction to retry.

### UDF Format

The Unified Document Format replaced monolithic Pydantic document objects with a versioned internal format using typed pieces (page text, tables, images, lightweight navigation view). Latency improved by p50 -19%, p90 -17%, and p99 -11%, with no quality regression.

### Live Vector DB Migration

Harvey initiated a live migration to a new vector database using dual-writing to both old and new systems simultaneously, with shadow reads and backfills for validation. Dual-writing created new memory pressure on indexing workers. To mitigate this, JSON serialization was replaced with Arrow IPC, reducing payload size, memory footprint, and serialization/deserialization time.

### Backpressure Architecture

Extraction uses ordered fallback chains (primary → Harvey-operated → deterministic local). Vector DB rate limits trigger explicit backoff and retry accounting, oversized writes are split, and long-running activities persist state to avoid losing progress on retry. Stage-level metrics track blob read/write durations, task-slot saturation, and failure taxonomies.

**Authors:** Tom McCormick, Jin Zhang, Shunrang Cao, Jinfeng Zhuang, Anna Zhang, Adam Shen, Gary Lam (Jul 27, 2026)

See also: [[concepts/ai-agent-engineering]] [[concepts/infrastructure-scaling]] [[concepts/document-processing]] [[concepts/vector-database]]

**Source:** [[raw/articles/2026-07-28_harvey_scaling-document-processing-across-harvey]]

## AI Trademark Search & IP Workflows (July 2026)

Harvey published an editorial walkthrough (Jul 30, 2026) positioning legal AI in the **trademark lifecycle** — from clearance search to enforcement — and clarifying where Harvey sits in that stack. The article's framing: *"the search is data; clearance is judgment."*

### The Search Layer (what Harvey does NOT do)

Modern trademark search software matches on three dimensions at once — **phonetic models** (sound-alikes like NOVVA/KNOVA), **semantic models** (marks translating to the same idea), and **image models** (visual similarity of logos/design marks) — plus goods-and-services **class coverage**. Systems run comparisons across national/international registries plus state and common-law sources; the USPTO itself now offers AI-assisted image search and classification. Harvey explicitly does **not** search trademark registries — it works with what the search returns.

### Harvey's Role: The Legal AI Layer

Harvey picks up where the search ends for IP teams:

- **Analyze search reports and file histories** — a comprehensive clearance search can run a hundred pages; legal AI digests the report, organizes closest marks by risk, maps each against likelihood-of-confusion factors, and produces a first draft of the **clearance opinion memo** for counsel to refine and sign.
- **Office action responses** — read the examiner's reasoning, pull precedent and prosecution history, draft a structured argument on the factors rather than a form letter. Counsel owns the filing; a response that once consumed a week of associate time can be reviewed inside a few days.
- **Enforcement** — sort genuine threats from watch-service noise, then draft the opposition analysis, cease-and-desist letters, and coexistence terms. Watch notices arrive continuously; a team that assesses and responds in days rather than weeks stops small conflicts from maturing.
- **Portfolio consistency** — the same platform drafts the clearance memo, office action response, and enforcement letter, so risk advice stays consistent across the life of the mark rather than varying by drafter.
- **Security**: client and brand data stay protected under enterprise-grade security — critical when the documents describe an unlaunched product.

The clear division of tools: a **search database** finds what exists; **counsel supported by legal AI** carries the legal work that follows.

**Source:** [[raw/articles/2026-07-31_harvey_ai-trademark-search]]
