---
title: "Tim Kraska"
type: concept
aliases:
  - tim-kraska
  - Tim Kraska
created: 2026-04-25
updated: 2026-11-26
tags:
  - concept
  - person
  - researcher
  - research
  - ai-research
  - mit
related:
  - "[[concepts/rlm-recursive-language-models]]"
  - "[[entities/omar-khattab]]"
  - "[[entities/alex-zhang]]"
  - "[[concepts/ai-agent-memory-middleware]]"
sources:
  - https://people.csail.mit.edu/kraska/
  - https://dsail.csail.mit.edu/
  - https://arxiv.org/abs/2504.01833
---

# Tim Kraska

**Tim Kraska** is a Professor of Electrical Engineering and Computer Science at MIT (CSAIL Data Systems Group), and one of the most influential figures in the "AI for systems / systems for AI" intersection. In this wiki he appears primarily as the **senior author and PhD co-advisor** behind [[concepts/rlm-recursive-language-models|Recursive Language Models (RLMs)]] and the **context rot** observation (with [[entities/alex-zhang|Alex Zhang]] and [[entities/omar-khattab|Omar Khattab]]).

## Profile

- **Title:** Professor, EECS, MIT CSAIL — Data Systems Group (DSG)
- **Also:** Director of Applied Science at **AWS** (concurrent); former Assistant Professor at Brown University; former time at Google Brain
- **Consortiums:** Co-directs MIT's **Generative AI Impact Consortium (MGAIC)**, **DSAIL@CSAIL**, and the **Everest@CSAIL** initiative
- **Entrepreneurship:** Co-founded **Instancio** and **Einblick Analytics** — both acquired (Einblick by Databricks)
- **Awards:** Sloan Research Fellow; VLDB Early Career Research Contribution Award; Intel Outstanding Researcher Award; VMware Systems Research Award; NSF CAREER Award; multiple best-paper/demo awards at VLDB, SIGMOD, ICDE

## Research Themes (2025–2026)

| Theme | Project | Idea |
|---|---|---|
| Agentic systems / LLMs for data | **RLMs**, deep-research & data-science agents | Programmatic, recursive examination of near-infinite contexts (see [[concepts/rlm-recursive-language-models]]) |
| AI for complex systems development | **G5** | "How should we build software when most code is AI-written or co-written?" |
| Declarative AI pipelines | **Palimpzest** (open source) | Introduced **semantic operators** optimized as part of an AI-enabled query plan |
| Data-science agents | **KramaBench** | First benchmark for data-science agents |
| ML for systems | **BRAD**, SageDB, learned indexes | Virtualize and auto-optimize data infrastructure |

## Why He Matters to This Wiki

Kraska's group supplies a recurring line of wiki-critical ideas:

- **Context rot** — the empirical finding (Zhang/Kraska/Khattab) that output quality degrades as prompts grow even within the nominal window; the motivating observation for RLMs and, by extension, much of [[concepts/context-engineering/_index|context engineering]] and [[concepts/ai-agent-memory-middleware]].
- **RLMs** — proposed by Alex Zhang, Tim Kraska, and Omar Khattab; MIT CSAIL/OASYS Lab.
- **Learned indexes (2018)** — his earlier "Algorithms with Predictions" / ML-enhanced-data-structures wave spawned 100+ variants (sorting, routing, genomics) and directly informed **Amazon Redshift** features (AI-driven scaling from SageDB; Multi-Dimensional Data Layouts from learned multi-dimensional indexing).
- **AWS Applied Science** — led science teams behind **AgentCore**, **Q SQL**, and **Bedrock Structured Knowledge Bases**: production deployments of AI agents.

## Students & Collaborators (wiki-tracked)

- [[entities/alex-zhang]] — PhD student (co-advised with Omar Khattab); RLM/LongCoT work
- [[entities/omar-khattab]] — PhD co-advisor on RLMs; DSPy / dspyrlm lineage

## Related

- [[concepts/rlm-recursive-language-models]] — his group's flagship LLM-era contribution
- [[concepts/dspy-rlm]] / [[concepts/dspyrlm]] — companion implementations
- [[concepts/agent-orchestration-runtime]] — cites his agentic-systems framing

## Sources

- [MIT CSAIL home page](https://people.csail.mit.edu/kraska/) — scraped 2026-11-26
- [DSAIL@CSAIL](https://dsail.csail.mit.edu/)
- [Learned Indexes (CIDR 2019)](https://dl.acm.org/doi/10.1145/3183713.3196909)
- YourBench paper co-authorship (arXiv:2504.01833) — with clem (HF) and UIUC group
