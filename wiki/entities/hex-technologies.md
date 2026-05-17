---
title: "Hex Technologies"
type: entity
created: 2026-05-08
updated: 2026-05-17
tags:
  - company
aliases: ["Hex", "Hex Tech"]
sources:
  - https://hex.tech
---

# Hex Technologies

Hex is an AI analytics platform that combines collaborative notebooks, conversational self-serve analytics, and data apps in one connected workspace. It unifies the traditionally fragmented data stack — notebooks, BI, and dashboards — with AI woven throughout.

| | |
|---|---|
| **Type** | AI Analytics Platform |
| **Founded** | 2020 |
| **Leadership** | Barry McCardel (Co-Founder & CEO), Caitlin Colgrove (Co-Founder & CTO), Glen Takahashi (Co-Founder & Chief Architect) |
| **Key Products** | Hex platform (agentic notebooks, conversational analytics, Context Studio, Hex CLI) |
| **Website** | [hex.tech](https://hex.tech) |
| **Tech Blog** | [hex.tech/blog](https://hex.tech/blog) |

## Key Facts
- Founded in 2020 by former Palantir engineers frustrated with fragmented data tools.
- Raised $70M in May 2025; total funding ~$172M.
- Trusted by Reddit, StubHub, HubSpot, Cisco, Figma, Anthropic, Rivian, and the NBA.
- Acquired Hashboard (BI platform) to expand analytics capabilities.

## Products & Technology
- **Agentic Notebooks**: Polyglot notebooks (SQL, Python, R) with a built-in AI agent for deeper analysis.
- **Conversational Self-Serve**: Business users ask questions in plain language against a shared semantic layer.
- **Context Studio**: AI governance and semantic models for trusted, consistent answers.
- **Hex CLI**: Terminal-based analytics control.
- Graph-based execution model for reproducibility at scale.



### Repos as Agent Context (May 2026)

Hex added the ability to attach Git repos to workspaces, enabling the Hex Agent to analyze dbt models and application code. This bridges the gap between data warehouse context and code-level understanding.

- **dbt repo use case**: Self-service users can query high-level tables while the agent crawls upstream dbt logic to understand filtering, collapsing, and category definitions
- **Application repo use case**: Answers questions about tracking implementation, untracked events, and how features relate in the codebase
- **Compounding context**: Repos, projects, warehouse metadata, guides, and semantic models are synthesized by the agent to answer questions that previously only the data team could address
- **Customers**: Underdog (Camden Willeford), Stubhub (Alan Peters) report significantly improved ability to handle "nebulous" queries

Authored by Andrew Lee (May 15, 2026).


## Related
- [[entities/anthropic]] — customer using Hex for data analytics
- [[entities/palantir]] — founders' previous employer
- [[concepts/data-notebooks]] — notebook paradigm evolution
