---
title: Jason Liu — Career & RAG Master Series
type: entity-subpage
parent: jason-liu
created: 2026-04-27
updated: 2026-04-27
tags:
  - career
  - stitch-fix
  - meta
  - consulting
  - rag
  - maven
---

# Jason Liu: Career & RAG Master Series

## Career

### Stitch Fix — Multimodal Embedding System (2018–2023)
As Staff MLE, Liu:
- Built multimodal embedding systems using ResNet-50 and CLIP+GPT-3 integration
- Designed the **Flight framework** handling 350M+ daily requests with 80% internal adoption
- Led a team of 6–7 engineers and data scientists
- Applied structured output patterns to product recommendation and personalization pipelines

### Meta (Facebook) — Data Scientist (2017)
- Built real-time monitoring dashboards, reducing escalation time by 50%
- Early work on production ML systems at scale

### Maven Training Programs
Liu runs advanced training courses on Maven for engineers from top AI companies, covering:
- RAG architecture and implementation
- Context engineering patterns
- Evaluation frameworks for LLM systems
- Structured outputs and validation

### Consulting Practice (567 Studios)
Works with Seed to Series B companies on AI best practices:
- RAG system design and optimization
- Context engineering strategies
- Evaluation framework construction
- Developer adoption and tooling

## RAG Master Series (jxnl.co)

A comprehensive 11+ article series on RAG, distilling years of consulting experience into a systematic framework.

### Foundation Posts
- **[What is RAG?](https://jxnl.co/writing/2024/11/07/what-is-retrieval-augmented-generation/)** — Core components: knowledge base, retrieval, generation, re-ranking. Key insight: RAG systems must be optimized as interconnected pipelines, not isolated parts
- **[Levels of RAG Complexity](https://jxnl.co/writing/2024/02/28/levels-of-complexity-rag-applications/)** — 7-tier framework from basic chunk+embed through query routing. *\"Most teams jump straight to Level 4 complexity and wonder why everything breaks\"*

### Implementation & Improvement Posts
- **[Systematically Improving Your RAG](https://jxnl.co/writing/2024/05/22/systematically-improving-your-rag/)** — Data-first improvement runbook: synthetic data for baselines, hybrid search (BM25 + vector), metadata utilization, query clustering
- **[The RAG Playbook: Building a Data Flywheel](https://jxnl.co/writing/2024/08/19/rag-flywheel/)** — Continuous improvement cycle
- **[Low-Hanging Fruit for RAG Search](https://jxnl.co/writing/2024/05/11/low-hanging-fruit-for-rag-search/)** — Seven quick wins
- **[Six Proven Strategies for Improving RAG](https://jxnl.co/writing/2025/09/11/rag-series-index/)** — Portfolio approach: flywheels, query segmentation, specialized indices, routing, feedback loops, response optimization

### Production & Monitoring Posts
- **[Systematically Improving RAG with Monitoring](https://jxnl.co/writing/2025/09/11/rag-series-index/)** — Track implicit signals alongside explicit ones
- **[RAG Anti-Patterns with Skylar Payne](https://jxnl.co/writing/2025/06/11/rag-anti-patterns-with-skylar-payne/)** — Top mistakes: increasing complexity without evaluation (~90% of failures), naive embedding usage, chunking too small

### Evaluation Posts
- **[The Only 6 RAG Evaluations You Need](https://jxnl.co/writing/2025/09/11/rag-series-index/)** — Six core evals: retrieval quality, generation accuracy, relevance, citation validation, latency, user satisfaction

### Advanced & Enterprise Posts
- **[RAG++: The Future Beyond Question Answering](https://jxnl.co/writing/2024/06/05/predictions-for-the-future-of-rag/)** — RAG will shift from Q&A to report generation
- **[Authority in RAG Systems](https://jxnl.co/writing/2025/03/06/authority-in-rag-systems-the-missing-piece-in-your-retrieval-strategy/)** — Proposes learning-to-rank approaches
- **[RAG Enterprise Implementation Process](https://jxnl.co/writing/2025/09/11/rag-series-index/)** — Scaling RAG across organizations
- **[Text Chunking Strategies with Anton from ChromaDB](https://jxnl.co/writing/2025/09/11/text-chunking-strategies-for-rag-applications/)** — Two rules in tension

## Speaker Series Details

Jason curated a comprehensive speaker series featuring practitioners from top companies, organized into 5 chapters:

| Chapter | Speaker | Key Insight |
|:--------|:--------|:------------|
| **Foundation & Evals** | Vitor (Zapier) | Simple UX changes increased daily feedback `10→40+` (4x) |
| **Foundation & Evals** | Anton (ChromaDB) | Chunking remains essential despite infinite context windows |
| **Foundation & Evals** | Kelly Hong | Custom benchmarks often contradict MTEB rankings |
| **Training & Fine-Tuning** | Manav (Glean) | Customer-specific embedding fine-tuning yields **20% gains** |
| **Training & Fine-Tuning** | Ayush (LanceDB) | Re-rankers deliver **12–20% retrieval improvement** |
| **Production & Monitoring** | Ben & Sidhant (Trellis) | Discretize infinite outputs → prioritize by impact → recursively refine |
| **Production & Monitoring** | Skylar Payne | **90% of teams** adding complexity see worse performance |
| **Production & Monitoring** | Chris Lovejoy (Anterior) | Build expert review loops → generate failure-mode datasets |
| **Query Analysis & Routing** | Anton (ChromaDB) | Separate indexes per user/data source outperform filtered large indexes |
| **Coding Agents** | Nik Pash (Cline) | Leading coding agents abandon embedding-based RAG for direct code exploration |
| **Coding Agents** | Colin Flaherty | Top SWE-Bench performers: simple CLI tools beat sophisticated embeddings |
| **Document Processing** | Adit (Reducto) | Hybrid CV + VLM pipelines beat pure text |
| **Multi-Modal** | Daniel (Superlinked) | Use mixture of specialized encoders (text, numerical, location, graph) |
| **Lexical Search** | John Berryman | Use lexical for filtering + metadata, semantic for meaning |

## RAG Anti-Patterns (with Skylar Payne)

| Pipeline Stage | Anti-Pattern | Specific Impact | Fix |
|:---------------|:-------------|:----------------|:----|
| **Data Collection** | Silent encoding/format failures | `21%` of medical corpus silently dropped | Track document counts at every stage |
| **Extraction** | Overly aggressive chunking (`~200 char`) | `13%` hallucination rate in e-commerce | Chunk by semantic boundaries |
| **Indexing** | Naive embedding usage + stale indexes | Financial news index unrefreshed for 2 weeks | Use query expansion, late chunking, contextual retrieval |
| **Retrieval** | Accepting vague queries; over-engineering | Wasted compute on irrelevant nodes | Intent classification; route to direct metadata lookups |
| **Generation** | Multi-hop reasoning failures | Medical chatbot hallucinated drug side effect | Force inline citations; validate citations exist |

**Key principles:**
- **Quadrant Analysis framework:** Evaluate both **relevance** AND **sufficiency**
- **Metadata tagging reality:** ~40% of clients have indexes too small for metadata to provide meaningful benefits
- **Recommended tooling:** Lilypad (Mirascope) for evaluation & versioning

## See Also

- [[jason-liu--instructor]] — Structured outputs library by Jason Liu using Pydantic validation.
- [[jason-liu--context-engineering]] — Beyond chunks: context engineering for RAG and agentic systems.
- [[retrieval-augmented-generation]] — Core RAG concepts and architecture patterns.
- [[context-engineering]] — Designing information environments for AI agents.
- [[structured-outputs]] — Schema-first design for LLM integration.
