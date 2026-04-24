---
title: Sheshansh Agrawal
type: entity
created: 2026-04-17
updated: 2026-04-17
tags:
  - person
  - researcher
  - engineer
  - search
  - information-retrieval
  - agentic-search
  - retrieval
  - reranking
  - rl
  - ai
related:
  - agentic-retrieval
  - graphrag
  - agentic-alternative-to-graphrag
  - cer-c-metric
  - contextual-ai
  - microsoft-research
  - iit-bombay
sources: []
---


# Sheshansh Agrawal

| | |
|---|---|
| **X/Twitter** | [@sheshansh_agrawal](https://x.com/sheshansh_agrawal) |
| **Blog** | [contextual.ai/blog](https://contextual.ai/blog) (with team) |
| **LinkedIn** | [linkedin.com/in/sheshansh-agrawal](https://linkedin.com/in/sheshansh-agrawal) |
| **Google Scholar** | [openreview.net/~Sheshansh_Agrawal1](https://openreview.net/profile?id=%7ESheshansh_Agrawal1) |
| **Role** | Director of Research at Contextual AI |
| **Education** | B.Tech Computer Science, IIT Bombay (2015–2019) |
| **Location** | United States |

## Overview

Sheshansh Agrawal is a **search and retrieval researcher** at the intersection of academic IR research and applied agentic AI. He currently serves as **Director of Research at Contextual AI** (Jun 2024–), where he leads work on agentic search, reranking, and structured data retrieval.

Before Contextual AI, he spent **5 years at Microsoft Research** (2019–2024) building the infrastructure behind Bing Ads — developing embedding algorithms that served **hundreds of millions of users daily** and generated **hundreds of millions in revenue**. His work scaled to **trillions of training tokens across hundreds of GPUs**.

Agrawal's research profile is distinct from Turnbull's practitioner wisdom or Solbakken's infrastructure focus: he is a **peer-reviewed IR researcher** whose papers appear at top conferences (SIGIR, WSDM, WWW), combined with a practitioner who has built and deployed retrieval systems at Microsoft scale. This dual position — **academic rigor + production scale** — gives his agentic search research a unique credibility.

## Career Timeline

| Period | Role | Organization |
|--------|------|--------------|
| 2015–2019 | B.Tech Computer Science | IIT Bombay (thesis with Prof. Soumen Chakrabarti) |
| 2019–2021 | Research SDE (LLM & NLP team) | Microsoft Research Bengaluru |
| 2021–2022 | Research SDE II | Microsoft Research Bengaluru |
| 2022–2024 | Member of Technical Staff | Microsoft Research (Bing Ads embeddings, extreme classification, personalized retrieval) |
| 2024–Present | Director of Research | Contextual AI |

## Research Publications (Selected)

| Paper | Venue | Contribution |
|-------|-------|-------------|
| **XPERT** | SIGIR 2023 | First personalized dense retrieval algorithm at scale |
| **DECAF** | WSDM 2021 | Improved out-of-domain generalization for ANN search |
| **ECLARE** | WWW 2021 | Extended extreme classification to richer metadata |
| **OOD-DiskANN** | — | Out-of-disk approximate nearest neighbor search |
| **BlitzRank** | — | First instruction-following reranker; 25-40% fewer tokens |
| **Text-to-SQL** | BIRD-Bench | Topped leaderboard with local models |
| **COR-GEE** | — | Scalable training method for embeddings (trillions of tokens) |

## Core Ideas & Research

### The Search Agent Bottleneck

In his March 2026 paper "Making Search Agents Faster and Smarter" (with Abdallah Bashir, Bo Han, Fanhai Lu), Agrawal identifies the fundamental bottleneck in agentic search:

> *"Search agents spend most of their compute in the research loop: query, search, reason, repeat."*

The paper optimizes on **two axes**: the search tool (retrieval stack) and the planner (the agent's decision-making). The key insight is that **both must be optimized jointly** — optimizing only one axis yields diminishing returns.

### CER-C: A Metric for Trajectory-Level Efficiency

Agrawal's most significant methodological contribution is **Cumulative Evidence Recall (CER-C)**, a new metric designed specifically for agentic retrieval evaluation.

Standard IR metrics (nDCG@K, Recall@K) evaluate **single-call retrieval quality**. But agentic systems make **multiple sequential calls**, and what matters is **how quickly evidence accumulates**. CER-C:

- Records the fraction of known relevant documents found after each **10K-token bucket** of context
- Computes the **Area Under the Curve (AUC)** — higher = better
- Captures **trajectory-level efficiency**: does the agent front-load relevant evidence, or waste context on dead ends?

> *"CER-C is a single scalar that captures how quickly an agent accumulates relevant evidence per token of context... The area under this curve is the score: higher is better."*

This is a **methodological innovation** for the agentic search evaluation space. It fills a gap that Turnbull identified ("RAG's big blindspot" — lack of engagement-based evaluation) but from an algorithmic research perspective.

### The Reranker is Everything

In their search tool sweep, the Contextual AI team found that the **reranker dominates agentic performance**:

| Component | nDCG@5 Impact | Latency |
|-----------|---------------|---------|
| **No reranker** | 0.089 | Baseline |
| **2B reranker** | 0.203 | 421ms |
| **6B reranker** | 0.500 | 795ms |
| **4096-dim + 6B** | 0.516 | 2x latency |

The jump from no reranker (0.089) to 2B reranker (0.203) is massive — **2.3x improvement** with only 421ms overhead. This suggests that **reranking quality matters far more than embedding dimension or retrieval method**.

### On-Policy Distillation + RL for Search Planners

The paper evaluates two training approaches for the search planner (built on Qwen3-30B-A3B):

1. **On-policy distillation** (50 steps): Teacher model (Qwen3-235B-A22B) provides dense per-token supervision via reverse KL. The student learns from states it actually visits. KL dropped 39%, search calls rose 1.4 → 2.06 (learned to calibrate effort).

2. **GRPO with CLP** (30 steps): RL fine-tuning with a novel **Conditional Log-Penalty (CLP)** reward function:
   ```
   R = em × max(0, 1 - ε·log(1+tc))
   ```
   Where `em` = correctness, `tc` = tool calls, `ε` = 0.15. The log penalty makes the first call expensive and additional calls cheap — teaching **disciplined tool usage**.

The best combination (on-policy distillation + CLP) reached **50.1% accuracy on BrowseComp-Plus** with fewer tool calls than untrained variants.

### An Agentic Alternative to GraphRAG

In November 2025, Agrawal published "An Agentic Alternative to GraphRAG" (with George Halal, Jackie Zhang), proposing a **leaner approach to reference traversal** in complex domains (law, compliance):

Instead of pre-computing static knowledge graphs with their heuristics and brittleness:

1. **Index structured metadata** (aliases, section hierarchies, citation keys) alongside raw text
2. **Let the agent decide** which index to query (content vs. metadata)
3. **Agent handles "edges"** via tool selection, not hard-coded graph traversal

Results: **75.43% accuracy** (content + metadata) vs **67.81%** (content only) in 5 turns. In 10 turns, content-only catches up (80.58% vs 81.85%) but at significantly higher cost (more tool calls, tokens, latency).

> *"By treating metadata extraction as prompt-engineering and traversal as an agentic tool-use problem, we achieve the flexibility of GraphRAG without the complexity."*

This is philosophically adjacent to your [[cli-over-mcp-pattern]] — **let the agent decide the path rather than hard-coding the topology**.

### Instruction-Following Rerankers

Agrawal also developed **BlitzRank**, the world's first instruction-following reranker, using **25–40% fewer tokens** than comparable methods. This directly addresses the cost-latency tradeoff that plagues agentic search: better quality at lower token cost.

## Engineering Philosophy

### On Small Model Fine-Tuning

Agrawal's research consistently demonstrates that **domain-specific fine-tuning of smaller models** outperforms relying on larger generalist models. This aligns with your [[reasoning-models]] research and the local-first AI trend — the alpha is in specialization, not scale.

### On Code Quality Standards

From his LinkedIn activity:
> *"Your job is to deliver code you have proven. I see a lot of complaints about untested AI slop in pull requests. Submitting those is a dereliction of duty as a software engineer."*

Despite working at the frontier of AI, he maintains **traditional software engineering rigor** — a perspective reinforced by his Microsoft Research background where systems serve millions of users.

### On Agent Builder's Art

> *"Agent building is an art, here's a canvas for all the artists out there."*

Agrawal recognizes that beyond the algorithms and metrics, building effective agents requires **intuition and craft** — not just optimization.

## Comparison with Turnbull and Solbakken

| Dimension | Turnbull | Solbakken | Agrawal |
|-----------|----------|-----------|---------|
| **Role** | Search consultant/author | Search infrastructure engineer | IR researcher |
| **Scale** | Reddit (2% DAU), Shopify, Daydream | Yahoo (13yr), Vespa, HORNET | Bing Ads (100M+ users), Contextual AI |
| **Output** | Books, blog posts, courses | Blog posts, HORNET engine | Peer-reviewed papers + research blog |
| **Focus** | Query understanding > ranking | Infrastructure for agents | Algorithmic optimization of search agents |
| **Key thesis** | Simple BM25 > thick APIs | Schema-first APIs for agents | Joint optimization of tool + planner |
| **New metric** | Judgment lists, NDCG | — | CER-C (trajectory-level efficiency) |

All three converge on: **agents need different search than humans**. But they approach from orthogonal angles.

## Key Quotes

> *"Faster, more accurate research lets agents answer harder questions at lower cost."*

> *"CER-C is a single scalar that captures how quickly an agent accumulates relevant evidence per token of context."*

> *"Distillation gives you a strong starting point... RL with CLP then fine-tunes the efficiency, teaching the model to be disciplined about unnecessary calls."*

> *"By treating metadata extraction as prompt-engineering and traversal as an agentic tool-use problem, we achieve the flexibility of GraphRAG without the complexity."*

> *"Agent building is an art, here's a canvas for all the artists out there."*

## Key Projects & Works

### Contextual AI — Agent Composer & Research (2024–Present)

As Director of Research, leads work on:
- **Agent Composer** — Contextual AI's agentic orchestration product (dynamic agent loops, tool integration)
- **Agentic Alternative to GraphRAG** — Metadata Search Tool for reference traversal
- **BlitzRank** — Instruction-following reranker (25-40% token reduction)
- **COR-GEE** — Scalable embedding training infrastructure (trillions of tokens)
- **CER-C** — New metric for agentic retrieval efficiency

### Microsoft Research — Bing Ads Infrastructure (2019–2024)

- Built scalable training methods and infrastructure for Bing Ads embeddings
- Developed XPERT, the first personalized dense retrieval algorithm at scale
- Extended extreme classification with DECAF and ECLARE
- Systems served 100s of millions of users daily, generating O($100M) in revenue

## Related

- [[agentic-retrieval]] — Agentic search and retrieval patterns
- [[agentic-alternative-to-graphrag]] — GraphRAG alternative via metadata search
-  — Cumulative Evidence Recall metric
-  — Reranking in retrieval pipelines
- [[doug-turnbull]] — Search relevance engineering perspective
- [[lester-solbakken]] — Search infrastructure perspective
-  — Contextual AI company

## Sources

- [Contextual AI Blog — Making Search Agents Faster and Smarter](https://contextual.ai/blog/making-search-agents-faster-and-smarter) (Mar 2026)
- [Contextual AI Blog — An Agentic Alternative to GraphRAG](https://contextual.ai/blog/an-agentic-alternative-to-graphrag) (Nov 2025)
- [Google Scholar — Sheshansh Agrawal](https://scholar.google.com)
- [OpenReview — Sheshansh Agrawal](https://openreview.net/profile?id=%7ESheshansh_Agrawal1)
- [LinkedIn — Sheshansh Agrawal](https://linkedin.com/in/sheshansh-agrawal-b5a79b97)
- [Contextual AI](https://contextual.ai/)
