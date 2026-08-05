---
title: "Hebbia"
type: entity
created: 2026-05-08
updated: 2026-08-05
tags:
  - company
  - search
  - ai-agents
  - fintech
aliases: ["Hebbia Inc.", "Hebbia AI"]
sources:
  - https://www.hebbia.ai/
  - https://www.hebbia.ai/blog
  - raw/articles/2026-06-06_hebbia_whats-new-june-disclosure-2026.md
  - raw/articles/2026-07-11_hebbia_every-data-integration-one-view.md
  - raw/articles/2026-07-31_hebbia_introducing-max.md
  - raw/articles/2026-08-05_hebbia_rethinking-control-in-the-age-of-ai-delivery.md
---

# Hebbia

Hebbia is an AI platform for knowledge work, designed to transform how professionals in finance, law, and consulting search, analyze, and synthesize information across large volumes of documents. Its flagship product, Matrix, enables users to query unlimited documents and get structured, spreadsheet-like answers to complex, multi-step questions.

| | |
|---|---|
| **Type** | AI Platform / Enterprise Search |
| **Founded** | 2020 (New York, NY) |
| **Leadership** | George Sivulka (Founder & CEO) |
| **Key Products** | Matrix (AI analyst), Max (AI team member), Hebbia Chat, Hebbia Skills, Hebbia Agents, Hebbia API, Hebbia MCP |
| **Website** | [hebbia.ai](https://www.hebbia.ai) |
| **Tech Blog** | [hebbia.ai/blog](https://www.hebbia.ai/blog) |

## Key Facts

- Founded by George Sivulka, a Stanford PhD dropout who worked at NASA as a teenager and finished a math bachelor's in 2.5 years
- Raised $130M Series B at a $700M valuation in July 2024, led by Andreessen Horowitz
- Revenue grew 15x in 18 months to $13M ARR, profitable at time of Series B
- Serves 30%+ of the top 50 asset managers; used by Centerview Partners, Charlesbank, Fenwick
- Expanding from financial services into legal and other regulated professional verticals

## Products & Technology

Matrix can ingest multiple files of unlimited length (PDFs, presentations, emails, spreadsheets, images) and respond to complex queries in a tabular format. Skills encode institutional workflows into reusable instructions. Hebbia Agents execute multi-step tasks autonomously. The platform emphasizes security for highly regulated industries and augmenting (not replacing) knowledge workers.

### Hebbia API & MCP (June 2026)

- **Hebbia API**: Connects Hebbia directly to any internal system to power real-time insights and automate critical workflows with intelligence from the platform.
- **Hebbia MCP** (Model Context Protocol): Allows users to ask natural-language questions over Hebbia projects and data sources directly within Claude and ChatGPT. Answers are returned with inline citations without leaving the host environment.

### Data Integrations (July 2026)

Hebbia's data integration library expanded to a comprehensive ecosystem of **12+ data sources** for financial, dealmaking, and CRM workflows, accessible from a single view within the platform:

**Public filings & financials:** SEC, CapIQ, FactSet
**Private market data:** PitchBook, Preqin
**Expert networks:** Third Bridge, Guidepoint
**Ratings & pricing:** Fitch, Intercontinental Exchange (ICE)
**Firm systems:** Snowflake, Databricks, SharePoint
**CRM:** Salesforce

Some sources are available from day one; others connect via the user's own subscription or are set up across the firm. Users can request access to unavailable sources in one click.

**Earlier integrations (June 2026)** — Four integrations originally added:
1. **Fitch** — Global credit rating agency; ratings and rationale for upgrades/downgrades grounded in source material
2. **ICE** — Near-real-time equity and ETF market data; chart prices directly within conversations
3. **Intralinks** — AI-enabled dealmaking; continuous workflow from data room to analysis
4. **Salesforce** — CRM data alongside financial and market research; pipeline status, account coverage, client activity

**Source:** [[raw/articles/2026-07-11_hebbia_every-data-integration-one-view]]

### Workflow & Agent Improvements (June 2026)

- **Project Controls** — New controls for managing and navigating shared work across teams. Publish or unpublish items directly from project history, track activity alongside history in the home tab, and follow breadcrumbs back to the originating project from any open Chat or Matrix session.
- **Citations in Slides** — PowerPoint presentations generated in Chat now include inline citation markers with source references in the slide footer, ensuring every claim is traceable to its origin.
- **Tick-and-Tie Agent** — A purpose-built agent that verifies figures in a presentation against a source file. Users upload reference data and the document to check; Hebbia extracts every metric and cross-references it page by page. Designed for financial analysts and deal teams who need to ensure numerical accuracy in deliverables.
- **Agent Run Controls** — Chat agents now prompt users to review and adjust sources before running. It is possible to add documents, attach projects, or swap in additional sources at the moment of execution. The step can be disabled entirely from Agent settings.
- **Expandable Tables** — Tables in Chat can now be expanded or collapsed, making it easier to read dense data and manage screen space within a response.
- **CSV File Uploads** — Upload CSV files directly into Chat alongside documents. Users can ask questions about the data, filter and summarize it, or combine it with other sources for cross-referenced analysis.

### Max — AI Team Member (July 2026)

**Max** is Hebbia's first "AI team member" product, introduced July 30, 2026 and positioned as built for the way financial institutions actually work. It marks a deliberate move past chat-first AI: ask Max a question and it pulls from the firm's data, reasons through agents and skills built for financial workflows, and returns a **finished set of slides, report, or financial model**.

Key positioning and capabilities:

- **Institutional workflow shape**: Slides in the firm's house style, responses structured the way finance professionals present information, agents and skills encoding the institution's own workflows — running on the firm's data alongside leading financial data providers.
- **Email-native**: The most senior people at a firm work with Max over email while moving between client meetings and board calls — work is not limited to the desk.
- **Emergent use cases**: Customers have built performance dashboards they check every morning and turned a daily update into something listenable on the commute.
- **Rollout**: Initially rolling out to a small set of firms via preview request.

**Source:** [[raw/articles/2026-07-31_hebbia_introducing-max]]

### Rethinking Control in AI Delivery (August 2026)

Hebbia engineer **Nikita Knyazev** published "Rethinking Control in the Age of AI Delivery" (Aug 4, 2026), arguing most AI programs are **over-controlled in the wrong places and under-controlled in the ones that matter**. Drawing on his late-2020 experience in UK vaccination logistics planning, he contrasts traditional delivery controls (multi-level plans, governance, phased delivery, peer review) with what a multi-thousand-user AI rollout actually needs.

**What should stay fixed**: an assured L1 top-level plan, AI platform ownership (what agile calls product ownership), delivery governance, and architectural/design authority over how new agents get built.

**What should loosen**: everything else. Because AI is a personal instrument — a tokenized digital worker applying institutional knowledge to a workflow — an institutional AI platform must serve both the enterprise and each individual employee. Knyazev frames the AI delivery team as **gardeners rather than architects**, cultivating each prompt, agent, and use case.

**Case study**: a global insurance client scoped the initial deployment tightly with defined use cases and approvals over organization-wide shared workflows; after the program ended, business departments kept building new agentic workflows on their own. What prevented drift was unchanged platform ownership and architectural authority — departments could build in parallel without the whole thing falling apart. The rollout matured to the point where formal program delivery controls were no longer needed.

**Source:** [[raw/articles/2026-08-05_hebbia_rethinking-control-in-the-age-of-ai-delivery]]

## Related

- [[entities/glean]] — competitor in AI-powered enterprise search for knowledge workers
- [[entities/harvey]] — overlapping customer base in legal and professional services
- [[entities/rogo]] — competitor in AI for financial services workflows
- [[entities/decagon]] — fellow enterprise AI agent platform, different vertical focus
