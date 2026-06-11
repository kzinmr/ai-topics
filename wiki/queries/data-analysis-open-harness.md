---
title: "データ分析に適したOpen Harnessはあるか？"
created: 2026-05-14
updated: 2026-05-14
type: query
tags:
  - query
  - harness-engineering
  - data-science
  - ai-agents
  - coding-agents
sources:
  - comparisons/open-harness-vs-agent-framework
  - concepts/data-analysis-agents
  - concepts/cognition-ai-data-analyst
  - concepts/agent-harness
related:
  - concepts/data-analysis-agents
  - concepts/cognition-ai-data-analyst
  - comparisons/open-harness-vs-agent-framework
  - concepts/agent-harness-comparison
---

# What Open Harness Is Suitable for Data Analysis?

> **Question**: What harnesses are suitable for data analysis, especially Open Harness?
> **Questioner**: kzinmr (Discord #hermes-topic-manager, 2026-05-14)
> **Answer Summary**: True Open Harnesses dedicated to data analysis are still nascent. Currently, the most "Open" option is to use a general-purpose coding harness (OpenCode/Pi) with a DB MCP connector attached.

---

## Premise: Defining "Open Harness"

First, let us confirm the scope of "Open Harness" as used in this Wiki (from [[comparisons/open-harness-vs-agent-framework]]):

| Category | Open Harness | Agent Framework / Runtime |
|---|---|---|
| **Investment Target** | Operational surface for **using** AI Agents | Control surface for **embedding** AI Agents into systems |
| **Primary Users** | Developers, operators, individuals, small teams | Product development teams, enterprise system teams |
| **Representative Tools** | OpenClaw, Hermes Agent, OpenCode, Pi | LangGraph, Pydantic AI, OpenAI Agents SDK, Claude Agent SDK |
| **Evaluation Axis** | Operator Workbench Readiness | Untrusted Product Runtime Readiness |

**Key point**: Open Harnesses are "ready-to-use finished products," while Frameworks are "parts that require assembly." This distinction matters in the data analysis context as well.

---

## Options Matrix

### A. Repurposing General-Purpose Coding Harnesses for Data Analysis

| Harness | Data Analysis Suitability | Model Freedom | Key Constraints |
|---|---|---|---|
| **OpenCode** | ★★★★☆ | 75+ providers | Default permissive (hardened config recommended). DB connection via MCP/custom tools. Maximum model selection freedom |
| **Pi** | ★★★★☆ | 20+ providers + local (MLX/GGUF) | Minimal overhead (<1K system prompt). DB tools added via extension. Has Anthropic wall |
| **Claude Code** | ★★★☆☆ | Anthropic models only | DB connection via MCP. Subscription $20/mo. Anthropic wall |
| **Codex CLI** | ★★★☆☆ | GPT-5.5 recommended + custom providers (DeepSeek, etc.) | Apache-2.0 OSS. Dual MCP support. Split via sub-agents |
| **Aider** | ★★★☆☆ | BYOM (all models) | Best token efficiency (1/4.2 of Claude Code). Git-first design |

**Common challenge**: These are designed for code generation, so for data analysis tasks you need to build the "SQL generation → execution → verification → visualization" loop yourself. Adding an MCP DB connector enables basic DB connectivity, but schema exploration and semantic ambiguity resolution are not provided by the harness side.

### B. Data-Analysis-Specialized Agents / Products

| Tool | Approach | Is it an Open Harness? |
|---|---|---|
| **Cognition DANA / Devin** | SWE agent data-analysis-specific persona. Connects to Redshift/Snowflake/BQ via MCP. Team sharing via Knowledge settings. DANA-specific persona (`/dana`). End-to-end (data anomaly → code cause → fix PR) | ❌ Product-type Closed Harness |
| **OpenAI Internal Data Agent** | GPT-5.2 + Codex pipeline crawling + 6-layer context grounding (Table Usage → Human Annotation → Codex Enrichment → Institutional Knowledge → Memory → Runtime Context). 600+PB, 70k+ datasets | ❌ Internal Bespoke (not public) |
| **Anthropic Claude Code Analytics** | Skills-first agentic analytics. 4-layer stack (Data Foundations → Sources of Truth → Skills → Validation). Semantic layer mandatory first path. 95% automation / ~95% accuracy. Skills skeleton shared publicly | △ Internal but patterns transferable |
| **Hex Technologies** | Agentic Notebooks — AI agent embedded in polyglot (SQL/Python/R) notebooks | ❌ Product-type Notebook Harness |
| **OpenAI Agents SDK (April 2026 evolved version)** | Configurable memory + sandbox-aware orchestration + filesystem tools + MCP. Approaching Open Harness | △ Evolving from Framework |

### C. Architecture Classification of Data Analysis Agents

The design space of data analysis agents can be organized along two axes (from [[concepts/data-analysis-agents]]):

|  | Approach A: Internal Bespoke | Approach B: SWE as Data Analyst | Approach C: Skills-First Analytics |
|---|---|---|---|
| **Representative** | OpenAI Internal Data Agent | Cognition DANA / Devin | Anthropic Claude Code Analytics |
| **Core Insight** | "The meaning of data lives inside pipeline code" | "SWE Agents make better analysts than SQL-only tools" | "Accuracy is a context + verification problem, not code gen" |
| **Context** | 6-layer grounding context | Full codebase search + git history | Skills + semantic layer + business knowledge graph |
| **Verification** | Evals API golden SQL pairs | Final SQL + Metabase playground link | Adversarial sub-agents + provenance footer + offline evals |

---

## Conclusion

### Current Best Practices

```
Individual/small-scale data analysis:
  Pi or OpenCode + MCP DB connector
  → Model freedom, BYOK, can be restricted to read-only via permission settings

Team-shared data analysis workbench:
  OpenClaw + OpenCode backend
  → Natural language DB queries from Slack/Discord, controlled via gateway

Productized/SaaS data analysis agent:
  Agent Framework (LangGraph / Pydantic AI) is appropriate
  → Because tenant isolation, audit, SLA, and state management are required
```

### Unresolved Issues

1. **A true Open Harness dedicated to data analysis does not yet exist** — Cognition DANA is powerful but Closed. Hex is a notebook product.
2. **Repurposing general-purpose coding harnesses has limitations** — Schema exploration, semantic ambiguity resolution, and verification loops require custom implementation.
3. **The evolution of the OpenAI Agents SDK** suggests convergence from Framework toward Open Harness, but is still in development.
4. **Standardization of DB connections via MCP** is progressing, but no harness covers the entire data analysis workflow (discovery → schema understanding → query → verify → visualize → report).

### Alignment with Karpathy's Insight

> "good answers can be filed back into the wiki as new pages"

This query itself is a practical example: this Q&A cross-references the investment target classification from [[comparisons/open-harness-vs-agent-framework]] with the architecture analysis from [[concepts/data-analysis-agents]], visualizing the previously uncovered intersection of **data analysis × Open Harness**.

---

## Related Pages

- [[concepts/data-analysis-agents]] — Comprehensive concept of AI data analysis agents
- [[concepts/cognition-ai-data-analyst]] — Design for turning Devin into a data analysis agent
- [[comparisons/open-harness-vs-agent-framework]] — The essential difference between Open Harness and Agent Framework
- [[concepts/harness-engineering/agent-harness]] — Agent Harness concept definition
- [[concepts/agent-harness-comparison]] — 9-harness comparison portal
