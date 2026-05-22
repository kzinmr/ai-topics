---
title: "Glean"
type: entity
created: 2026-05-08
updated: 2026-05-22
tags:
  - company
  - search
  - ai-agents
  - rag
aliases: ["Glean Work", "Gleanwork"]
sources:
  - https://www.glean.com/
  - https://www.glean.com/about
  - raw/articles/2026-05-15_glean_cowork-mcp-eval.md
  - raw/articles/2026-05-21_glean_health-agents-2026.md
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


Glean's platform is built on four pillars: Enterprise Context (connectors + knowledge graph), Glean Search (cross-app search), Glean Assistant (personalized AI copilot), and Glean Agents (autonomous task automation). The platform enforces agent behavior at runtime for reliability, and provides an open agent architecture for enterprise extensibility.

## Related

- [[entities/cohere]] — potential embedding/model partner; complementary search vs model layer
- [[entities/anthropic]] — Claude is a supported model within Glean's multi-LLM platform
- [[entities/openai]] — GPT models are available through Glean's multi-LLM approach
- [[entities/hebbia]] — competitor in enterprise AI search for knowledge workers
