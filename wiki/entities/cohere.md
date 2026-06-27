---
title: "Cohere"
type: entity
created: 2026-05-08
updated: 2026-06-27
tags:
  - company
  - model
  - nlp
  - mcp
  - enterprise-saas
  - code-model
aliases: ["Cohere Inc.", "Cohere AI"]
sources:
  - https://cohere.com/
  - https://cohere.com/blog
  - raw/articles/2026-05-20_cohere_cohere-acquires-reliant-ai-expand-sovereign-enterprise-ai.md
  - raw/newsletters/2026-05-22-ainews-openai-gpt-next-disproves.md
  - raw/articles/2026-05-21_cohere_cohere-announces-strategic-mous-with-indragroup-and-multiverse-computing.md
  - https://huggingface.co/blog/CohereLabs/introducing-north-mini-code
  - https://x.com/cohere/status/2064378058329526556
  - raw/articles/2026-06-18_cohere_serving-fairness.md
  - raw/articles/2026-06-26_cohere_automating-fork-maintenance-with-ai-agents.md
  - raw/articles/2026-06-26_cohere_cohere-security-ai-agent-north-wiz.md
---

# Cohere

Cohere is a Canadian-American enterprise AI company founded in 2019 by former Google Brain researchers. It builds large language models and retrieval systems designed for private, secure, and customizable enterprise deployment — including Command (text generation), Embed (semantic search), Rerank, and the North workplace platform.

| | |
|---|---|
| **Type** | Enterprise AI Platform |
| **Founded** | 2019 (Toronto, Canada / San Francisco, CA) |
| **Leadership** | Aidan Gomez (Co-founder & CEO), Nick Frosst (Co-founder), Ivan Zhang (Co-founder) |
| **Key Products** | Command (LLM family), Embed (multimodal embeddings), Rerank, North (workplace AI), Compass (enterprise search), Aya (multilingual research models) |
| **Website** | [cohere.com](https://cohere.com) |
| **Tech Blog** | [cohere.com/blog](https://cohere.com/blog) |

## Key Facts

- Founded by Aidan Gomez (co-author of the "Attention Is All You Need" transformer paper at age 20), Nick Frosst, and Ivan Zhang
- Raised $500M Series D in mid-2024 at $5.5B valuation; additional $500M in 2025, valuing at $6.8B
- Annual recurring revenue reached $100M in 2025, targeting $200M
- Strong focus on private deployments for highly regulated industries (finance, healthcare, defense)
- Cohere Labs is the company's dedicated AI research arm


## Acquisitions & Expansion

### Reliant AI Acquisition (May 2026)

### Command A+ Open Release (May 2026)

Cohere released **Command A+** under **Apache 2.0** — its first fully permissive open-source model.

| Detail | Value |
|--------|-------|
| **Parameters** | 218B MoE / 25B active |
| **License** | Apache 2.0 |
| **Capabilities** | Multimodal, 48 languages |
| **Hardware** | 2xH100 with W4A4 quantization |
| **Inference** | vLLM day-0 support |
| **Benchmark** | AA AI Index: 37 points |
| **Architecture** | Parallel Transformer blocks, LayerNorm to RMSNorm |

This marks a strategic shift for Cohere — from proprietary enterprise deployments to open-source community engagement.


In May 2026, Cohere acquired **Reliant AI**, a Montreal/Berlin-based biopharma AI company, to expand its sovereign enterprise AI platform into healthcare and life sciences. The acquisition brings Reliant AI's research team, proprietary biomedical datasets, and domain-optimized technology into Cohere's enterprise-grade sovereign AI platform.

**Transaction details:**
| Field | Detail |
|-------|--------|
| **Target** | Reliant AI (founded 2023, Montreal & Berlin) |
| **Founders** | Karl Moritz Hermann (CEO, joined Cohere as VP of AI Verticalizations), Richard Schlegel, Marc G. Bellemare (Canada CIFAR AI Chair, Mila; joined Cohere as VP of Modelling) |
| **Product** | Intelligent research workbench for biopharma — automated literature reviews, competitive landscaping, extraction of unstructured scientific/regulatory data |
| **Customers assumed** | GSK, Medicus Pharma, Kyowa Kirin |
| **Strategic rationale** | Deepen healthcare/biopharma capabilities for sovereign AI deployments in regulated environments |

### North for Pharma

Cohere announced **North for Pharma**, an agentic AI system purpose-built for biopharma teams working across R&D, clinical development, and scientific analytics. This extends Cohere's North platform offerings for regulated industries (alongside finance and telecoms).

The acquisition positions Cohere as a leader in sovereign enterprise AI for healthcare, building on its established presence in Canada and Germany.

### Strategic MOUs: Indra Group & Multiverse Computing (May 2026)

On May 20, 2026, Cohere announced two strategic MOUs expanding its sovereign AI footprint:

**Indra Group (Spain)**: Through IndraMind (Indra's sovereign intelligence initiative), Cohere will:
- Develop sovereign LLMs adapted to Castilian Spanish, Catalan, Valencian, Basque, and Galician
- Integrate Cohere into IndraMind's intelligence ecosystem for critical-asset protection
- Build an enterprise AI platform targeting new commercial opportunities between Spain and Canada
- Develop defense-sector solutions for analysis, mission-planning, and interoperability in multinational operations
- Signed during the institutional visit of Spain's King Felipe VI to Canada, under the Canada-Spain bilateral cooperation framework

**Multiverse Computing (Spain/Canada)**: A quantum-inspired AI optimization company, Cohere will:
- Explore commercial collaboration opportunities in Europe and Canada
- Leverage the Canada-Spain bilateral framework for jointly pursued projects
- Drive revenue growth across each other's home markets

> "Enterprises no longer want to rent AI — they want to own it. Our partnerships with Indra Group and Multiverse Computing are designed to deliver true digital sovereignty." — Aidan Gomez, CEO

These MOUs extend Cohere's sovereign AI strategy beyond acquisitions (Reliant AI) into international government-backed partnerships, positioning Cohere as the infrastructure layer for sovereign enterprise AI across Europe and Canada.


## Products & Technology

Cohere's platform centers on three model families: Command for text generation and chat, Embed for vector embeddings and semantic retrieval, and Rerank for search quality improvement. The North platform brings AI productivity into the workplace. Aya is an open multilingual research initiative covering 70+ languages. Cohere emphasizes deployment flexibility including private cloud and on-premise.

### AI Agent Fork Maintenance (June 2026)

Cohere published a blog post describing their AI agent system for automating vLLM fork maintenance. The system uses a **control theory framework**: the reference signal (upstream commits) → disturbance (breaking changes) → controller (AI agent) → feedback (test suite). This compressed upstream release absorption from weeks to days.

Five skills were open-sourced at [`cohere-ai/vllm-skills`](https://github.com/cohere-ai/vllm-skills): `install-vllm`, `local-test-runner`, `detect-upstream-base`, `rebase-assistant`, and `auto-rebase`. Skills are markdown documents that coding agents read and execute interactively.

In a concrete case, the vLLM v0.19.1 release broke the Cohere Transcribe ASR model (WER=100%); the agent diagnosed a transformers version issue and restored WER to ~11.92. The fix was upstreamed as [vLLM PR #40582](https://github.com/vllm-project/vllm/pull/40582). The approach was also applied to the HuggingFace [[concepts/transformers]] fork for Command A+ pre-release testing.

[[concepts/ai-agents]] | [[concepts/control-theory]] | [[concepts/fork-maintenance]]

## MCP Guide (May 2026)

Cohere published a comprehensive **[What Is Model Context Protocol (MCP)](https://cohere.com/blog/guide-to-mcp)** guide positioning itself as the enterprise authority on MCP adoption. Key points:

- **MCP is not a model or agent framework** — it's an application/integration layer protocol connecting AI apps to enterprise systems
- **Client-server architecture**: Host (AI app) → Client → Server (exposes Resources, Tools, Prompts)
- **Three feature types**: Resources (context/data), Tools (callable functions), Prompts (reusable templates)
- **Transport mechanisms**: stdio for local, Streamable HTTP for remote connections
- **Enterprise use cases**: customer support, sales, financial reporting, IT incident management
- **Security considerations**: access control, authentication, server trust, tool safety, logging, deployment architecture

The guide reinforces Cohere's North platform positioning: "North helps organizations bring agents, tools, permissions, and monitoring into one governed workspace, including RBAC and tool usage visibility."

[[concepts/mcp]] | [[concepts/agent-tooling]] | [[concepts/enterprise-ai]]

### Security Agent with North and Wiz (June 2026)

Cohere built a security agent by connecting **North** (their agent platform) to **Wiz** (cloud security) via a custom MCP server. The architecture follows: North → Custom MCP server → Wiz GraphQL API. Authentication uses a shared secret between North and the MCP server, with OAuth2 client credentials for Wiz.

The MCP server exposes **8 tools**: `wiz_list_issues`, `wiz_get_issue_details`, `wiz_list_toxic_combinations`, `wiz_search_vulnerabilities`, `wiz_get_security_posture`, `wiz_query_assets`, `wiz_get_compliance_status`, and `wiz_update_issue`.

Three use cases showcase the system:

1. **Toxic combination blast radius analysis** — completes in ~20 seconds versus half a morning manually
2. **Assisted incident response** — drafts full incident response reports, creates Linear tickets, and updates Wiz statuses automatically
3. **Autonomous weekly posture brief** — automatically generated report every Monday at 3am

The implementation is open-sourced at [`cohere-ai/cohere-security-toolkit`](https://github.com/cohere-ai/cohere-security-toolkit).

[[concepts/mcp]] | [[concepts/ai-agents]] | [[concepts/security-automation]] | [[tools/wiz]]

## co/plot: Research Visualization Tool (June 2026)

Cohere Labs built co/plot, a research visualization prototyping tool. It addresses Matplotlib's slow iteration cycle and Figma's inability to faithfully render data.

- **Validated during Tiny Aya model development**: used for 70+ language evaluation visualizations
- **Design philosophy**: "The process of making the plot matters as much as the plot itself"
- **Open-source release**: published for the research community
- **Author**: Thomas Euyang (Research Visual Storyteller, Cohere Labs)

[[concepts/open-science]] | [[concepts/data-visualization]]

## North Family — Developer-Focused Models (June 2026)

Cohere launched the "North" model family, targeting developers and agentic coding workflows.

### North Mini Code (June 2026)

Cohere's first open-source coding model. A 30B-parameter sparse MoE (3B active) trained specifically for agentic software engineering tasks.

| Detail | Value |
|--------|-------|
| **Parameters** | 30B MoE / 3B active (128 experts, 8 per token) |
| **License** | Apache 2.0 |
| **Training** | Two-stage SFT + async RLVR (CISPO algorithm) |
| **Context** | 128K tokens |
| **Benchmark** | AA Coding Index 33.4 — outperforms models 4-40× larger |
| **Harness** | Cross-harness robustness (SWE-Agent, mini-SWE-Agent, OpenCode, Terminus 2) |
| **Weights** | [BF16](https://huggingface.co/CohereLabs/North-Mini-Code-1.0), [FP8](https://huggingface.co/CohereLabs/North-Mini-Code-1.0-fp8) |

See [[entities/north-mini-code]] for full details.

## LLM Serving Fairness (June 2026)

In June 2026, Cohere published **"LLM Serving Fairness"**, detailing a 4-layer scheduling architecture designed to solve the noisy-neighbor problem in multi-tenant LLM serving — where one large tenant's request load degrades latency for all other tenants sharing the same GPU infrastructure. The system is now enabled for all Cohere SaaS API and AWS Marketplace customers.

The four layers operate in sequence to govern request admission and GPU selection:

1. **Rate Limiter (admission control)**: Caps the maximum number of requests per tenant per timeframe at the endpoint level. Real-time throttling rejects requests when the queue backlog exceeds latency targets, preventing any single tenant from overwhelming the system on the way in.

2. **Performance Tier (first selector)**: Compute resources are prioritized based on SLAs — higher-paid tiers receive greater priority. Tiering determines which tenant goes first, but does not prevent a single large tenant within a tier from dominating.

3. **Deficit Round Robin — DRR (second selector, heart of the system)**: Each tenant gets its own queue line with a quantum budget. The scheduler takes turns between tenants, debiting each request's cost. The scheduler is work-conserving and weighted — cheap requests let a tenant come up more often, expensive ones less. Two cost models are supported:
   - **Request-based budgeting**: cost = 1 per request, quantum = request count. Simple and suitable for generative/streaming endpoints where requests are broadly similar.
   - **Token-based budgeting**: cost = token count, quantum = token allowance. A natural fit for batched endpoints (embeddings, rerankers). Large requests consume more budget, preventing monopolization of GPU capacity.

4. **Priority (third selector)**: Within a tenant's turn, requests are ordered by **Priority → Deadline → Arrival time**, ensuring critical or time-sensitive requests are served first.

The complete flow integrates admission control (Rate Limiter) on the way in, and three selectors (Tiering → DRR → Priority) on the way out as each batch is assembled. DRR is the architectural centerpiece: by ensuring each tenant receives fair turns proportional to their quantum, it eliminates the noisy-neighbor problem and guarantees predictable latency across tenants regardless of load imbalances.

[[concepts/llm-serving]] | [[concepts/multi-tenant-architecture]] | [[concepts/scheduling]]

## Related

- [[entities/north-mini-code]] — first North family model (coding MoE)
- [[entities/openai]] — competitor in enterprise LLM APIs
- [[entities/anthropic]] — competitor in enterprise-safe AI deployment
- [[entities/voyage-ai]] — competitor in embedding/rerank models
- [[entities/glean]] — complementary enterprise AI; Cohere provides models, Glean provides the search layer
- [[entities/fireworks-ai]] — open-weight inference platform; Fireworks ran LAB post-training experiments
- [[concepts/ai-benchmarks/legal-agent-benchmark]] — Harvey LAB; Fireworks used Kimi K2.6 post-training (Cohere connection via shared ecosystem)
