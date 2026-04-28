---
title: Jason Liu — RAG Philosophy & Framework
type: entity-subpage
parent: jason-liu
created: 2026-04-27
updated: 2026-04-27
tags:
  - rag
  - retrieval-augmented-generation
  - evals
  - llm-engineering
---

# Jason Liu: RAG Philosophy & Framework

Through his consulting work with dozens of startups and his free 6-week email course on RAG (improvingrag.com), Liu has developed the most systematic practitioner's framework for building and improving RAG systems. His philosophy manifests in the **RAG Master Series** on jxnl.co — 12+ interconnected articles covering everything from fundamentals to enterprise implementation.

## Core Thesis: \"RAG is the feature, not the benefit.\"

> \"RAG systems suck because the value you derive is time saved from finding an answer. This is a one-dimensional value, and it's very hard to sell any value beyond that. Meanwhile, a report is a higher-value product because it is a decision-making tool that enables better resource allocation.\"

> \"The real advantage is that it's measurable—and measurability kills guesswork. Instead of random hype or endless prompt tinkering, you systematically track your retrieval, refine your segmentation, handle specialized data, pick the best index, and incorporate user feedback.\"

Jason predicts RAG will shift from question-answering to **report generation** — from delivering answers to enabling decisions.

### The Economic Argument for Report-Driven RAG

| Metric | Traditional RAG (Q&A) | Report-Driven RAG |
|:---|:---|:---|
| **Primary Value** | Time savings (one-dimensional) | Strategic decision-making (high-leverage) |
| **ROI Framing** | Percentage of hourly wages saved | Percentage of capital/budget impacted |
| **Output Format** | Raw answers or chat transcripts | Structured templates with objectives, decision criteria, follow-ups |
| **Scalability** | Limited to static queries | Enables standardized company processes (SOPs) |

## The Twin Biases of RAG Development

Liu identifies two systematic failures that plague RAG teams:

1. **Absence Bias** — Ignoring the retrieval step because only the final LLM output is visible. Teams tweak prompts and swap models when the real problem is that the right chunks aren't being found.
2. **Intervention Bias** — Chasing every new trick (re-rankers, prompt hacks, hybrid retrieval) without validation, creating brittle \"Franken-systems\" with high technical debt.

> \"The biggest mistake around improving the system is that most people are spending too much time on the actual synthesis without actually understanding whether or not the data is being retrieved correctly.\"

> \"About 90% of the time, teams implement complex retrieval paths and re-ranking systems when the real problem was bad input data.\"

## The RAG Playbook — Continuous Improvement Flywheel

From [The RAG Playbook](https://jxnl.co/writing/2024/08/19/rag-flywheel/):

> \"Too many teams focus on the wrong things. They obsess over generation before nailing search, implement RAG without understanding user needs, or get lost in complex improvements without clear metrics.\"

The 9-step flywheel sequence:
`Iteration → User Feedback Integration → Production Monitoring → System Improvements → Classification and Analysis → Real-World Data Collection → Fast Evaluations → Synthetic Data Generation → Initial Implementation`

1. **Start with Synthetic Data** — Generate Q&A pairs from every chunk. Baseline recall should hit ~97%. \"If your recall is 50%, that means half the time you're missing the relevant chunk entirely. No advanced prompt can fix that.\"
2. **Avoid the Twin Biases**
3. **Segmentation & Failure Diagnosis** — Overall averages hide critical failures. Segment by topic, complexity, user role.
4. **Structured Extraction & Multimodality** — Tables should not be chunked as raw text — store as actual DBs. Pre-extract image metadata via captioning models.
5. **Query Routing & Specialized Indices** — Treat each index as a \"tool\" and use LLM function calling to route.
6. **Fine-Tune Embeddings & Re-Rankers** — Domain-specific fine-tuning yields 10–30% recall boosts.
7. **Hybrid Search** — Full-text search (BM25) + vector search. BM25 is ~10x faster for exact-match queries.
8. **Close the Loop** — Deploy user feedback, track implicit signals alongside explicit ones.
9. **Leading Metrics Over Lagging Metrics** — Prioritize metrics that predict success.

## The \"Only 6 RAG Evals\" Framework

From [There Are Only 6 RAG Evals](https://jxnl.co/writing/2025/05/19/there-are-only-6-rag-evals/):

> \"The power of focusing on Question (Q), Context (C), and Answer (A) is that these three components, and their conditional relationships, cover every possible aspect of RAG evaluation.\"

| Tier | Metric | Notation | What It Measures |
|------|--------|----------|-------------------|
| 🟢 Foundation | Retrieval Precision & Recall | — | Classic IR metrics. Fast, LLM-free. |
| 🟡 Primary | Context Relevance | C\|Q | Do retrieved chunks address the question? |
| 🟡 Primary | Faithfulness/Groundedness | A\|C | Is the answer supported by context? |
| 🟡 Primary | Answer Relevance | A\|Q | Does the answer address the user's need? |
| 🔴 Advanced | Context Support Coverage | C\|A | Does context support every claim in the answer? |
| 🔴 Advanced | Question Answerability | Q\|C | Can you answer given the context? |
| 🔴 Advanced | Self-Containment | Q\|A | Can the question be inferred from the answer? |

Domain-specific priorities:
- 🏥 **Medical RAG:** Maximize A\|C (Faithfulness) — hallucinations are dangerous
- 🎧 **Customer Service:** Maximize A\|Q (Answer Relevance) — user satisfaction
- 📚 **Technical Docs:** Maximize Q\|C (Question Answerability) — honest \"I don't know\" responses

## 7-Step Quick-Win Runbook

1. **Synthetic baseline data** — Establish recall metrics before any tuning
2. **Date filters** — Handle temporal queries without complex retrieval
3. **Improved user feedback copy** — \"Did we answer correctly?\" not just thumbs up/down
4. **Track cosine distance/reranking scores** — Monitor retrieval quality drift
5. **Full-text search as baseline** — BM25 often outperforms embeddings for exact-match queries
6. **Make chunks look like questions at ingestion** — Transform documents into Q&A pairs
7. **Include file/document metadata** — Ownership, dates, status for routing

## RAG Levels of Complexity

| Level | Capability | Description |
|-------|-----------|-------------|
| 0 | Basic chunk + embed → search | Simple vector similarity |
| 1 | Structured processing | Async, parallel queries |
| 2 | Query enhancement | Rewriting, expansion, summarization |
| 3 | Observability | Wide event tracking, logging |
| 4 | Advanced search/ranking | Re-rankers, hybrid search |
| 5 | Multi-modal content | Image/table processing |
| 6 | Query routing | Specialized indices, metadata lookups |

> \"Most teams jump straight to Level 4 complexity and wonder why everything breaks.\"

## Speaker Series: Systematically Improving RAG Applications

See the full [[jason-liu--key-work]] page for the complete speaker series table featuring practitioners from Zapier, ChromaDB, Glean, LanceDB, Trellis, Cline, and others.

**Cross-series patterns:**
1. Data quality examination beats algorithmic sophistication
2. Teams iterating fastest on data examination consistently outperform those focused on algorithmic complexity
3. Fine-tuning embeddings and re-rankers are more accessible and impactful than most teams realize
4. Most teams underinvest in document processing, evaluation frameworks, and understanding their specific data distribution
5. Successful RAG systems require a portfolio of techniques, not a single silver bullet

## RAG Anti-Patterns

See the full anti-patterns analysis on the [[jason-liu--key-work]] page, covering anti-patterns across Data Collection, Extraction, Indexing, Retrieval, and Generation stages.

**Key principles:**
> *\"The teams who can make that loop go as fast as possible are the ones who win, and that is pretty invariable.\"*

> *\"About 90% of the time, teams implement complex retrieval paths and re-ranking systems when the real problem was bad input data.\"*

## Authority in RAG Systems

Liu identifies a critical gap: RAG systems over-index on **semantic similarity** while neglecting **authority** and **freshness**.

| Dimension | Traditional Search (Google/Bing) | Semantic Search (Vector DBs) |
|:---|:---|:---|
| **Primary Signal** | Lexical match (BM25) + User engagement + Authority | Embedding similarity only |
| **Authority Handling** | Explicit (PageRank, domain trust, backlinks) | Ignored (treats blogs & peer-reviewed papers identically) |
| **User Visibility** | Sources shown; users can verify | Sources hidden; LLM synthesizes answer directly |
| **Risk** | Lower | High: \"Garbage in, garbage out\" amplified by confident LLM tone |

**Proposed solution: Learning to Rank (LTR)** — supervised ML that ranks documents using multi-dimensional features (source reputation, domain authority, user engagement, freshness, citation count, PageRank, vector similarity, BM25 score). Uses XGBoost/LambdaMART to optimize NDCG/MAP.
