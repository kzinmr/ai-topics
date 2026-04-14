---
title: Jason Liu
handle: "@jxnlco"
created: 2026-04-13
updated: 2026-04-13
tags:
  - person
  - x-account
  - ai
  - structured-outputs
  - pydantic
  - instructor
  - llm-engineering
  - developer-tools
  - rag
  - context-engineering
  - evals
---


# Jason Liu (@jxnlco)

| | |
|---|---|
| **X** | [@jxnlco](https://x.com/jxnlco) |
| **Blog** | [jxnl.co](https://jxnl.co) |
| **GitHub** | [jxnl](https://github.com/jxnl) |
| **Role** | Founder, 567 Studios; creator of Instructor; former Staff MLE at Stitch Fix |
| **Known for** | Instructor library (11K+ stars, 6M+ monthly downloads), "Pydantic is all you need" keynote, structured outputs for LLMs |
| **Bio** | Staff ML Engineer and open source creator with 10+ years building AI systems at scale. Creator of Instructor, cited by OpenAI as inspiration for their structured output feature. Works with Seed to Series B companies on AI best practices including RAG, Context Engineering, and Evals. |

## Overview

Jason Liu is one of the most influential practitioners in the space of **structured LLM outputs** — the problem of getting reliable, typed, validated data from language models rather than loose text. His open source library **Instructor** (python.useinstructor.com) has become a de facto standard for this pattern, with 11,000+ GitHub stars, 6M+ monthly downloads, and explicit citation by OpenAI as the inspiration for their Structured Outputs feature.

Liu's career spans the full production ML stack: Data Scientist at Meta (2017), Staff MLE at Stitch Fix (2018–2023) where he built multimodal embedding systems handling 350M+ daily requests, and now Founder of 567 Studios (2023–present) where he consults for companies including Zapier, HubSpot, Limitless, Weights & Biases, Modal Labs, Timescale, and Pydantic. He also runs training programs on Maven attended by engineers from OpenAI, Anthropic, Google, Microsoft, Amazon, and Netflix.

His intellectual signature is the thesis that **"we're not changing the language of programming — we're relearning how to program with data structures."** This positions structured outputs not as a new paradigm but as a return to classical software engineering rigor, making LLM integration backwards-compatible with existing codebases and tooling.

## Core Ideas

### "Pydantic is All You Need" — Structured Outputs as the Foundation

Liu's keynote at the **AI Engineer Summit 2023** ("Pydantic is all you need") crystallized his core philosophy: the problem with LLM integration isn't the models — it's the interface between probabilistic outputs and deterministic software.

> "Imagine hiring an intern to write an API that returns a string you have to JSON load into a dictionary and pray the data is still there. You'd probably fire them and replace them with GPT. Yet, many of us are content using LLMs in the same way."

His argument has three pillars:

1. **Schema-first design** — Define what you want as a Pydantic model, not as a prompt template
2. **Validation as self-correction** — Treat LLM errors as validation failures with clear error messages the model can use to retry
3. **Backwards compatibility** — Make Software 3.0 work with existing paradigms (type hints, dataclasses, ORM patterns)

Instructor's API is intentionally minimal:

```python
from instructor import from_openai
from pydantic import BaseModel
from openai import OpenAI

class User(BaseModel):
    name: str
    age: int

client = from_openai(OpenAI())
response = client.create(model="gpt-4o", response_model=User,
    messages=[{"role": "user", "content": "John is 25 years old"}])
# response is a validated User(name="John", age=25)
```

### Validation Errors as a Feature, Not a Bug

Liu reframes the LLM reliability problem through the lens of **classical software validation**:

> "Instead of framing 'self-critique' or 'self-reflection' in AI as new concepts, we can view them as validation errors with clear error messages that the system can use to self-correct."

Instructor implements a **reasking mechanism** that automatically:
1. Parses the LLM's raw output
2. Validates it against the Pydantic schema
3. On failure, sends the validation error back to the model as context for retry
4. Repeats until valid output is produced or max retries is reached

This turns the probabilistic LLM into a deterministic function from the caller's perspective — a critical requirement for production systems.

### Multi-Language, Multi-Provider Structured Outputs

Since the original Python release, Instructor has expanded to **5 languages** (Python, TypeScript, Ruby, Go, Elixir) plus a **Rust** implementation, and supports every major LLM provider:

- OpenAI, Anthropic, Google, Vertex AI, Cohere
- Ollama, llama-cpp-python (local/offline models)
- Any provider with function calling capabilities

The cross-language strategy reflects Liu's belief that **structured outputs are a universal need**, not a Python-specific convenience.

### Software 3.0 — Classical Engineering Meets LLMs

Liu's vision of "Software 3.0" is that structured outputs allow developers to:
- **Own the objects we define** — typed models, not loose JSON
- **Control the functions we implement** — explicit tool contracts
- **Manage the control flow** — retries, validation, error handling
- **Own the prompts** — declarative schema definitions that generate prompts automatically

> "This approach makes Software 3.0 backwards compatible with existing software, demystifying language models and returning us to a more classical programming structure."

### RAG Philosophy — Data-First, Evaluation-Driven

Through his consulting work with dozens of startups and his free 6-week email course on RAG (improvingrag.com), Liu has developed the most systematic practitioner's framework for building and improving RAG systems. His philosophy manifests in the **RAG Master Series** on jxnl.co — 12+ interconnected articles covering everything from fundamentals to enterprise implementation.

**Core Thesis: "RAG is the feature, not the benefit."**

> "RAG systems suck because the value you derive is time saved from finding an answer. This is a one-dimensional value, and it's very hard to sell any value beyond that. Meanwhile, a report is a higher-value product because it is a decision-making tool that enables better resource allocation."

> "The real advantage is that it's measurable—and measurability kills guesswork. Instead of random hype or endless prompt tinkering, you systematically track your retrieval, refine your segmentation, handle specialized data, pick the best index, and incorporate user feedback."

Jason predicts RAG will shift from question-answering to **report generation** — from delivering answers to enabling decisions.

> "I don't care so much about being able to read a chat transcript of a meeting I had. I care if I can turn that transcript into a format and report that I know will drive my desired business outcomes rather than just save me time."

**The Economic Argument for Report-Driven RAG:**

| Metric | Traditional RAG (Q&A) | Report-Driven RAG |
|:---|:---|:---|
| **Primary Value** | Time savings (one-dimensional) | Strategic decision-making (high-leverage) |
| **ROI Framing** | Percentage of hourly wages saved | Percentage of capital/budget impacted |
| **Output Format** | Raw answers or chat transcripts | Structured templates with objectives, decision criteria, follow-ups |
| **Scalability** | Limited to static queries | Enables standardized company processes (SOPs) |

> "Ultimately, a report's value goes beyond a wage worker answering questions—it supports high-leverage outcomes like strategic decision-making."

**The Twin Biases of RAG Development**

Liu identifies two systematic failures that plague RAG teams:

1. **Absence Bias** — Ignoring the retrieval step because only the final LLM output is visible. Teams tweak prompts and swap models when the real problem is that the right chunks aren't being found.
2. **Intervention Bias** — Chasing every new trick (re-rankers, prompt hacks, hybrid retrieval) without validation, creating brittle "Franken-systems" with high technical debt.

> "The biggest mistake around improving the system is that most people are spending too much time on the actual synthesis without actually understanding whether or not the data is being retrieved correctly."

> "About 90% of the time, teams implement complex retrieval paths and re-ranking systems when the real problem was bad input data."

**The RAG Playbook — Continuous Improvement Flywheel**

From [The RAG Playbook](https://jxnl.co/writing/2024/08/19/rag-flywheel/):

> "Too many teams focus on the wrong things. They obsess over generation before nailing search, implement RAG without understanding user needs, or get lost in complex improvements without clear metrics."

> "Crawl Before You Walk: I've seen teams jump straight to end-to-end evaluations with LLM-generated responses. This is a mistake. Get your retrieval working first."

The 9-step flywheel sequence:
`Iteration → User Feedback Integration → Production Monitoring → System Improvements → Classification and Analysis → Real-World Data Collection → Fast Evaluations → Synthetic Data Generation → Initial Implementation`

1. **Start with Synthetic Data** — Generate Q&A pairs from every chunk. Baseline recall should hit ~97%. "If your recall is 50%, that means half the time you're missing the relevant chunk entirely. No advanced prompt can fix that."
   - Strategic value: Forces clarity on product goals before real data exists, enables lightning-fast evaluations (milliseconds vs. seconds per query), guides optimal embedding model & chunking strategy selection
   - Team impact: Transforms stand-ups from vague updates to metric-driven progress (e.g., *"Improved recall by 5% by tweaking chunking strategy."*)
2. **Avoid the Twin Biases** — Absence Bias and Intervention Bias (see above)
3. **Segmentation & Failure Diagnosis** — Overall averages hide critical failures. A 70% recall might mask 5% recall on high-value multi-hop queries. Segment by topic, complexity, user role.
   - **Inventory Problem vs Capability Problem:** Data missing entirely (uningested subfolder/DB column) vs data exists but can't be surfaced (needs better search, filtering, or metadata)
4. **Structured Extraction & Multimodality** — "Don't rely on the LLM alone to interpret an image on the fly." Tables should not be chunked as raw text — store as actual DBs. Pre-extract image metadata via captioning models.
5. **Query Routing & Specialized Indices** — When multiple searchers exist (vector, SQL, image, lexical), treat each index as a "tool" and use LLM function calling to route.
   - Routing metrics: `Tool Recall` (% of queries correctly routed) and `Tool Precision` (% of tool calls actually necessary)
6. **Fine-Tune Embeddings & Re-Rankers** — Domain-specific fine-tuning yields 10–30% recall boosts. Standard pipeline: quick vector search (Top K) → re-rank (cross-encoder) → pass top results to LLM.
7. **Hybrid Search** — Full-text search (BM25) + vector search. "I found in practice that when I was doing tests against essays, full text search and embeddings basically performed the same, except full text search was about 10 times faster."
8. **Close the Loop** — Deploy user feedback, track implicit signals (frustration patterns) alongside explicit ones (thumbs up/down), and feed back into synthetic data generation.
9. **Leading Metrics Over Lagging Metrics** — Stop tracking overall app quality (lagging). Prioritize leading metrics that predict success: time to run eval suite, precision/recall improvements on synthetic data, number of retrieval experiments per week.

> "Remember, the goal isn't to have a perfect system on day one. It's to build a flywheel of continuous improvement that compounds over time."

**Practical Performance Metrics from Consulting:**
- Multi-step RAG pipelines typically take `2–10 seconds` — streaming & interstitials are mandatory for UX
- Expect `10–30% recall boost` by training embeddings/re-rankers on domain-specific triplets `(query, positive_chunk, negative_chunk)`
- BM25 full-text search is ~10x faster than embeddings for exact-match queries, with comparable quality

**The "Only 6 RAG Evals" Framework**

From [There Are Only 6 RAG Evals](https://jxnl.co/writing/2025/05/19/there-are-only-6-rag-evals/):

> "The power of focusing on Question (Q), Context (C), and Answer (A) is that these three components, and their conditional relationships, cover every possible aspect of RAG evaluation. There are no hidden variables."

| Tier | Metric | Notation | What It Measures |
|------|--------|----------|-------------------|
| 🟢 Foundation | Retrieval Precision & Recall | — | Classic IR metrics. Fast, LLM-free. |
| 🟡 Primary | Context Relevance | C\|Q | Do retrieved chunks address the question? |
| 🟡 Primary | Faithfulness/Groundedness | A\|C | Is the answer supported by context? |
| 🟡 Primary | Answer Relevance | A\|Q | Does the answer address the user's need? |
| 🔴 Advanced | Context Support Coverage | C\|A | Does context support every claim in the answer? |
| 🔴 Advanced | Question Answerability | Q\|C | Can you answer given the context? |
| 🔴 Advanced | Self-Containment | Q\|A | Can the question be inferred from the answer? |

> "When your RAG system fails, it fails along one of these dimensions. Every time. Answer seems wrong? Check faithfulness (A|C). Answer seems irrelevant? Check answer relevance (A|Q). Answer missing key info? Check context relevance (C|Q)."

Implementation strategy:
- **Start with Tier 1** — Use Precision, Recall, MAP@K, MRR@K for retriever tuning. No LLMs required. Daily development cadence.
- **Focus on Tier 2** — Implement C|Q, A|C, A|Q via LLM-based evaluation. Continuous iteration.
- **Extend to Tier 3** — Add C|A, Q|C, Q|A for deeper insights. Monthly/strategic releases.

Domain-specific priorities:
- 🏥 **Medical RAG:** Maximize A|C (Faithfulness) — hallucinations are dangerous
- 🎧 **Customer Service:** Maximize A|Q (Answer Relevance) — user satisfaction
- 📚 **Technical Docs:** Maximize Q|C (Question Answerability) — honest "I don't know" responses build trust

**7-Step Quick-Win Runbook** (from [Low-Hanging Fruit for RAG Search](https://jxnl.co/writing/2024/05/11/low-hanging-fruit-for-rag-search/)):

1. **Synthetic baseline data** — Establish recall metrics before any tuning
2. **Date filters** — Handle temporal queries without complex retrieval
3. **Improved user feedback copy** — "Did we answer correctly?" not just thumbs up/down
4. **Track cosine distance/reranking scores** — Monitor retrieval quality drift
5. **Full-text search as baseline** — BM25 often outperforms embeddings for exact-match queries
6. **Make chunks look like questions at ingestion** — Transform documents into Q&A pairs
7. **Include file/document metadata** — Ownership, dates, status for routing

**RAG Levels of Complexity** (from [Levels of Complexity](https://jxnl.co/writing/2024/02/28/levels-of-complexity-rag-applications/)):

| Level | Capability | Description |
|-------|-----------|-------------|
| 0 | Basic chunk + embed → search | Simple vector similarity |
| 1 | Structured processing | Async, parallel queries |
| 2 | Query enhancement | Rewriting, expansion, summarization |
| 3 | Observability | Wide event tracking, logging |
| 4 | Advanced search/ranking | Re-rankers, hybrid search |
| 5 | Multi-modal content | Image/table processing |
| 6 | Query routing | Specialized indices, metadata lookups |

> "Most teams jump straight to Level 4 complexity and wonder why everything breaks."

**Speaker Series: Systematically Improving RAG Applications**

Jason curated a comprehensive speaker series (originally a cohort-based course, now closed) featuring practitioners from top companies. The series is organized into 5 chapters:

| Chapter | Speaker | Key Insight |
|:--------|:--------|:------------|
| **Foundation & Evals** | Vitor (Zapier) | Simple UX changes increased daily feedback `10→40+` (4x). Specific prompts outperform generic ones. |
| **Foundation & Evals** | Anton (ChromaDB) | Chunking remains essential despite infinite context windows due to embedding model limits. **Rule:** Always manually inspect chunks. |
| **Foundation & Evals** | Kelly Hong | Generative benchmarking: filter chunks → generate realistic queries → evaluate retrieval. Custom benchmarks often contradict MTEB rankings. |
| **Training & Fine-Tuning** | Manav (Glean) | Customer-specific embedding fine-tuning yields **20% performance gains** over 6 months. Smaller fine-tuned models beat larger general-purpose ones for company terminology. |
| **Training & Fine-Tuning** | Ayush (LanceDB) | Re-rankers deliver **12–20% retrieval improvement** with minimal latency. Even 6M parameter models show significant gains. ColBERT is optimal middle ground. |
| **Production & Monitoring** | Ben & Sidhant (Trellis) | Traditional error tracking (Sentry) fails for AI — no exceptions for bad outputs. Framework: discretize infinite outputs → prioritize by impact → recursively refine. |
| **Production & Monitoring** | Skylar Payne | **90% of teams** adding complexity see worse performance. Silent document failures eliminate **20%+ of corpus** undetected. |
| **Production & Monitoring** | Chris Lovejoy (Anterior) | Build expert review loops → generate failure-mode datasets → prioritize fixes by impact → dynamically augment prompts. |
| **Query Analysis & Routing** | Anton (ChromaDB) | Monolithic indexes reduce recall due to ANN limitations. **Solution:** Separate indexes per user/data source outperform filtered large indexes. |
| **Coding Agents** | Nik Pash (Cline) | Leading coding agents abandon embedding-based RAG for direct code exploration. "Narrative integrity" requires coherent thought, not disconnected snippets. |
| **Coding Agents** | Colin Flaherty | Top SWE-Bench performers: simple CLI tools (`grep`, `find`) beat sophisticated embeddings due to agent persistence & course-correction. |
| **Document Processing** | Adit (Reducto) | Hybrid CV + VLM pipelines beat pure text. **1–2° document skews** dramatically degrade extraction quality. |
| **Multi-Modal** | Daniel (Superlinked) | LLMs are "pilots that see the world as strings" — struggle with numerical relationships. Use mixture of specialized encoders (text, numerical, location, graph). |
| **Lexical Search** | John Berryman | Semantic search struggles with exact matching, product IDs, specialized terminology. Use lexical for filtering + metadata, semantic for meaning. |

**Cross-series patterns:**
1. Data quality examination beats algorithmic sophistication
2. Teams iterating fastest on data examination consistently outperform those focused on algorithmic complexity
3. Fine-tuning embeddings and re-rankers are more accessible and impactful than most teams realize
4. Most teams underinvest in document processing, evaluation frameworks, and understanding their specific data distribution
5. Successful RAG systems require a portfolio of techniques, not a single silver bullet

**RAG Anti-Patterns** (with Skylar Payne, ex-Google/ex-LinkedIn):

From the lightning lesson interview, Jason and Skylar identified concrete failure modes with measurable impact:

| Pipeline Stage | Anti-Pattern | Specific Impact | Fix |
|:---------------|:-------------|:----------------|:----|
| **Data Collection** | Silent encoding/format failures | `21%` of medical corpus silently dropped (Latin-1 vs UTF-8 mismatch) | Track document counts at every stage; log failures |
| **Extraction** | Overly aggressive chunking (`~200 char` chunks) | `13%` hallucination rate in e-commerce (no single chunk held complete info) | Chunk by semantic boundaries; leverage modern context windows |
| **Indexing** | Naive embedding usage + stale indexes | Financial news index unrefreshed for 2 weeks returned outdated earnings data | Bridge query/doc form mismatch via query expansion, late chunking, contextual retrieval |
| **Retrieval** | Accepting vague queries; over-engineering simple lookups | Wasted compute on irrelevant nodes in large filtered indexes | Intent classification; route structured queries to direct metadata lookups |
| **Generation** | Multi-hop reasoning failures | Medical chatbot hallucinated drug side effect not in source material | Force inline citations; validate citations exist in retrieved docs; semantic validation |

**Key principles from anti-patterns analysis:**

> *"The teams who can make that loop go as fast as possible are the ones who win, and that is pretty invariable."*

> *"About 90% of the time, teams implement complex retrieval paths and re-ranking systems when the real problem was bad input data."*

- **Quadrant Analysis framework:** Evaluate both **relevance** (is it related?) AND **sufficiency** (does it contain enough info to answer?)
- **Re-ranking pitfalls:** Minimize manual boosting rules (hard to debug); blacklist known poor domains; consider custom cross-encoder re-ranker
- **Metadata tagging reality:** ~40% of clients have indexes too small for metadata to provide meaningful benefits. Value scales with data volume + query diversity.
- **Recommended tooling:** Lilypad (Mirascope) for evaluation & versioning, especially for teams without deep AI engineering backgrounds

**Authority in RAG Systems** (March 2025)

Jason identifies a critical gap: RAG systems over-index on **semantic similarity** while neglecting **authority** and **freshness**.

> *"The newest and shiniest AI technique isn't always the complete solution."*

| Dimension | Traditional Search (Google/Bing) | Semantic Search (Vector DBs) |
|:---|:---|:---|
| **Primary Signal** | Lexical match (BM25) + User engagement + Authority | Embedding similarity only |
| **Authority Handling** | Explicit (PageRank, domain trust, backlinks) | Ignored (treats blogs & peer-reviewed papers identically) |
| **User Visibility** | Sources shown; users can verify | Sources hidden; LLM synthesizes answer directly |
| **Risk** | Lower | High: "Garbage in, garbage out" amplified by confident LLM tone |

**Proposed solution: Learning to Rank (LTR)**

LTR is a supervised ML approach that ranks documents using multi-dimensional features:
- **Feature set:** Source reputation, domain authority, user engagement (clicks, dwell time), freshness/recency, citation count, PageRank, vector similarity score, BM25 score
- **Training pipeline:** Collect query-document pairs with relevance labels → Extract features → Train model (XGBoost/LambdaMART) to optimize NDCG/MAP → Deploy to re-rank candidates
- **Why XGBoost:** Provides feature importance metrics, models complex feature interactions, handles diverse data types, fast inference for production

> *"The click signal is gold... If users consistently click on and spend time with certain documents for particular query types, that's powerful implicit feedback about what's truly useful."*

**Query Routing + Specialized Indices architecture:**
- `Recency Index` → Optimized for timeline/recent event queries
- `High-Authority Index` → Contains only vetted/official sources
- `Hybrid Index` → BM25 + vector search
- **Router** → Analyzes query intent and directs to optimal index

Industry examples: Bing/Google SGE (massive-scale RAG with LTR trained on billions of interactions), Perplexity.ai (explicitly leverages BM25 and domain authority alongside semantic search).

**Context Engineering — The Future of RAG**

From [Beyond Chunks: Context Engineering is the Future of RAG](https://jxnl.co/writing/2025/08/27/facets-context-engineering/) (Aug 2025), Liu extends RAG to agentic systems:

> "The breakthrough came when we realized chunks themselves were the limitation. When search results showed multiple documents, agents couldn't strategically decide which to load or how to explore further."

**Four Levels of Context Engineering:**
1. **Minimal Chunks** — Basic tool responses without metadata
2. **Chunks with Source Metadata** — Enables citations and strategic document loading
3. **Multi-Modal Content** — Optimizes tables, images, structured data for agents
4. **Facets and Query Refinement** — Reveals the complete data landscape for strategic exploration

> "Tool results become prompt engineering — Metadata teaches agents how to use tools in future calls"

**Agent Peripheral Vision:** Providing agents with structured metadata about the broader information space beyond top-k results. This is the key insight: agents need to know what they *don't* know.

From [Context Engineering Series Index](https://jxnl.co/writing/2025/08/28/context-engineering-index/):

> "We've moved far beyond prompt engineering. Now we're designing portfolios of tools (directory listing, file editing, search) and the context engineering that makes them work together."

## Key Work

### Instructor Library
The flagship open source project — a thin wrapper around LLM APIs that adds:
- **response_model parameter** — specify a Pydantic model, get validated objects back
- **Automatic retries** — configurable max retries with validation error feedback
- **Streaming with structure** — partial objects as tokens arrive, maintaining type safety
- **Multi-provider support** — same API across OpenAI, Anthropic, Google, local models
- **Multi-language ports** — TypeScript, Ruby, Go, Elixir, Rust implementations
- **11,000+ GitHub stars, 6M+ monthly PyPI downloads**
- **Cited by OpenAI** as inspiration for their Structured Outputs API feature

### Structured Outputs By Example
A hands-on educational site (github.com/jxnl/structuredoutputsbyexample) showcasing extraction patterns across:
- Basic data extraction
- Classification tasks
- Streaming responses
- Multiple LLM providers
- Real-world use cases (search queries, content moderation, data transformation)

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

### RAG Master Series (jxnl.co)
A comprehensive 11+ article series on RAG, distilling years of consulting experience into a systematic framework:

**Foundation Posts:**
- [What is RAG?](https://jxnl.co/writing/2024/11/07/what-is-retrieval-augmented-generation/) — Core components: knowledge base, retrieval, generation, re-ranking. Key insight: RAG systems must be optimized as interconnected pipelines, not isolated parts
- [Levels of RAG Complexity](https://jxnl.co/writing/2024/02/28/levels-of-complexity-rag-applications/) — 7-tier framework from basic chunk+embed (Level 1) through structured processing with reranking (Level 2), observability and wide event tracking (Level 3), to image/table processing and query routing (Levels 6–7). Core philosophy: *"Most teams jump straight to Level 4 complexity and wonder why everything break*"

**Implementation & Improvement Posts:**
- [Systematically Improving Your RAG](https://jxnl.co/writing/2024/05/22/systematically-improving-your-rag/) — Data-first improvement runbook: synthetic data for baselines, hybrid search (BM25 + vector), metadata utilization, query clustering for capability gap analysis
- [The RAG Playbook: Building a Data Flywheel](https://jxnl.co/writing/2024/08/19/rag-flywheel/) — Continuous improvement cycle: synthetic data → fast evaluations → production monitoring → user feedback → classification → system improvements. *"The teams who can make that loop go as fast as possible are the ones who win"*
- [Low-Hanging Fruit for RAG Search](https://jxnl.co/writing/2024/05/11/low-hanging-fruit-for-rag-search/) — Seven quick wins: date filters, user feedback copy, cosine distance tracking, full-text search, making chunks look like questions at ingestion time, file/document metadata inclusion
- [Six Proven Strategies for Improving RAG](https://jxnl.co/writing/2025/09/11/rag-series-index/) — Portfolio approach: flywheels, query segmentation, specialized indices, routing, feedback loops, response optimization

**Production & Monitoring Posts:**
- [Systematically Improving RAG with Monitoring](https://jxnl.co/writing/2025/09/11/rag-series-index/) — AI monitoring must detect subtle degradation, not just explicit errors. Track implicit signals (frustration patterns) alongside explicit ones (thumbs up/down)
- [RAG Anti-Patterns with Skylar Payne](https://jxnl.co/writing/2025/06/11/rag-anti-patterns-with-skylar-payne/) — Top mistakes: increasing complexity without evaluation (~90% of failures), naive embedding usage, chunking too small, ignoring query routing. *"About 90% of the time, teams implement complex retrieval paths and re-ranking systems when the real problem was bad input data"*

**Evaluation Posts:**
- [The Only 6 RAG Evaluations You Need](https://jxnl.co/writing/2025/09/11/rag-series-index/) — Overcomplicated frameworks fail. Six core evals: retrieval quality, generation accuracy, relevance, citation validation, latency, user satisfaction

**Advanced & Enterprise Posts:**
- [RAG++: The Future Beyond Question Answering](https://jxnl.co/writing/2024/06/05/predictions-for-the-future-of-rag/) — RAG will shift from Q&A to **report generation**. *"A report is a higher-value product because it is a decision-making tool that enables better resource allocation"*
- [Authority in RAG Systems](https://jxnl.co/writing/2025/03/06/authority-in-rag-systems-the-missing-piece-in-your-retrieval-strategy/) — Relevancy, freshness, AND authority are all critical signals. Proposes learning-to-rank approaches combining semantic similarity with PageRank-style authority
- [RAG Enterprise Implementation Process](https://jxnl.co/writing/2025/09/11/rag-series-index/) — Scaling RAG across organizations with governance, compliance, and multi-team coordination
- [Text Chunking Strategies with Anton from ChromaDB](https://jxnl.co/writing/2025/09/11/text-chunking-strategies-for-rag-applications/) — Two rules in tension: (1) fill the embedding model's context window, (2) don't group unrelated information. *"There's no one-size-fits-all chunking strategy"*

## Blog / Key Writings

### Structured Outputs
- **AI Engineer Keynote: Pydantic is all you need** (Nov 2023) — The talk that launched his public profile, arguing that structured outputs via Pydantic solve the fundamental LLM integration problem
- **Pydantic is Still All You Need: Reflections on a Year of Structured Outputs** (Sep 2024) — One-year retrospective: "nothing's really changed in the past year. The core API is still just one function call." Covers 40% month-over-month growth, multi-language expansion, and the case for validation-first design
- **Bridging Language Models with Python with Instructor, Pydantic, and OpenAI's Function Calls** (Medium, 2023) — Technical deep-dive into why Pydantic is the right abstraction between LLMs and traditional software
- **Structured Outputs By Example** (github.com/jxnl/structuredoutputsbyexample) — Living documentation of extraction patterns across providers and use cases

### RAG (Retrieval-Augmented Generation) — 12+ articles

Jason maintains the most comprehensive practitioner's guide to RAG on his blog, organized as a multi-part series with a [RAG Master Series Index](https://jxnl.co/writing/2025/09/11/rag-series-index/). His approach is distinctive for its **data-first, evaluation-driven methodology** rather than architecture-first thinking.

**Core RAG philosophy:**

> "Rag is the feature, not the benefit." — Jason argues that RAG as question-answering delivers only time-saved value, while RAG as report-generation delivers decision-making value, which is fundamentally more valuable to businesses.

> "Look at your data at every step of the pipeline." — His single most repeated principle. Teams that examine data inputs, intermediate results, and outputs, then iterate fast, "are invariably the ones who succeed."

**Key RAG articles:**

- **[What is Retrieval Augmented Generation?](https://jxnl.co/writing/2024/11/07/what-is-retrieval-augmented-generation/)** — Foundational overview of RAG components (query understanding, retrieval, generation, re-ranking) and why RAG matters over pure parametric knowledge
- **[Levels of Complexity: RAG Applications](https://jxnl.co/writing/2024/02/28/levels-of-complexity-rag-applications/)** — Framework classifying RAG systems into levels from basic chunk+embed→search (Level 0) through query enhancement (Level 2), observability/wide events (Level 3), async and caching (Level 4), advanced search/ranking (Level 5), to image/table processing and routing (Level 6+)
- **[Systematically Improving Your RAG](https://jxnl.co/writing/2024/05/22/systematically-improving-your-rag/)** — Comprehensive improvement runbook based on consulting experience. Core thesis: start with synthetic data for baseline metrics, use hybrid search (BM25 + vector), cluster and model topics to find capability gaps
- **[Low-Hanging Fruit for RAG Search](https://jxnl.co/writing/2024/05/11/low-hanging-fruit-for-rag-search/)** — Seven quick wins: synthetic baseline data, date filters, improved user feedback copy, tracking cosine distance/reranking scores, adding full-text search, making chunks look like questions at ingestion time, including file/document metadata
- **[The RAG Playbook](https://jxnl.co/writing/2024/08/19/rag-flywheel/)** — Systematic flywheel: iterate → user feedback → production monitoring → system improvements → classification → real-world data collection → fast evaluations → synthetic data generation
- **[Predictions for the Future of RAG](https://jxnl.co/writing/2024/06/05/predictions-for-the-future-of-rag/)** — RAG will shift from question-answering to report generation. "A report is a higher-value product because it is a decision-making tool that enables better resource allocation." Predicts a marketplace of report-generating templates
- **[Authority in RAG Systems](https://jxnl.co/writing/2025/03/06/authority-in-rag-systems-the-missing-piece-in-your-retrieval-strategy/)** — Relevancy, freshness, AND authority are all critical signals. Embedding search ignores authority; proposes learning-to-rank approaches combining semantic similarity with PageRank-style authority signals
- **[Text Chunking Strategies](https://jxnl.co/writing/2025/09/11/text-chunking-strategies-for-rag-applications/)** — Guest session with Anton from ChromaDB. Two rules of thumb in tension: (1) fill the embedding model's context window, (2) don't group unrelated information. "There's no one-size-fits-all chunking strategy."
- **[RAG Anti-Patterns with Skylar Payne](https://jxnl.co/writing/2025/06/11/rag-anti-patterns-with-skylar-payne/)** — Interview with Skylar (ex-Google, ex-LinkedIn). Top anti-patterns: increasing complexity without evaluation (~90% of mistakes), naive embedding usage (trained for semantic similarity, not Q&A), chunking too small, ignoring query routing (simple metadata lookups instead of full RAG for straightforward queries)
- **[Beyond Chunks: Why Context Engineering is the Future of RAG](https://jxnl.co/writing/2025/08/27/facets-context-engineering/)** — First post in a Context Engineering series. Core thesis: "In agentic systems, how we structure tool responses is as important as the information they contain." Four levels of context engineering: minimal chunks → chunks with source metadata → multi-modal content → facets and query refinement. Predicts tool results become prompt engineering for agents.
- **[There Are Only 6 RAG Evals](https://jxnl.co/writing/2025/05/19/there-are-only-6-rag-evals/)** — Every RAG system reduces to Q, C, A and exactly 6 conditional relationships. Tiered evaluation: Tier 1 (retrieval metrics, no LLM), Tier 2 (C|Q, A|C, A|Q via LLM-judge), Tier 3 (C|A, Q|C, Q|A for deep analysis). Domain-specific priorities: medical → A|C, customer service → A|Q, technical docs → Q|C.
- **[Six Proven Strategies for Improving RAG](https://jxnl.co/writing/2025/09/11/rag-series-index/)** — Portfolio approach: flywheels, query segmentation, specialized indices, routing, feedback loops, response optimization.
- **[Slash Commands vs Subagents](https://jxnl.co/writing/2025/08/29/context-engineering-slash-commands-subagents/)** — Context pollution kills agent performance. "Bad context is cheap but toxic: loading 100k lines of test logs costs almost nothing computationally, but easily pollutes valuable context." Subagent architecture solves this — burn tokens in specialized workers, preserve focus in the main thread.
- **[Agent Frameworks and Form Factors](https://jxnl.co/writing/2025/09/04/context-engineering-agent-frameworks-and-form-factors/)** — Three form factors: chatbot (conversational), workflow (side-effect engines), research artifact (reports/tables). Autonomy spectrum: deterministic system → AI function → human-in-loop → full autonomy. "Ask your team for specific results, not just 'agents.'"
- **[Rapid Agent Prototyping](https://jxnl.co/writing/2025/09/11/rag-series-index/)** — Use Claude Code's project runner as a testing harness. Write instructions in English, expose tools as simple CLI commands, create test folders with real inputs. "Get one passing test before you write any orchestration code."
- **[AI Agent Compaction Experiments](https://jxnl.co/writing/2025/09/11/rag-series-index/)** — "If in-context learning is gradient descent, then compaction is momentum." Two experiments on using compaction for maintaining agent state and reasoning continuity across long sessions.

**RAG 6-week email course:** Jason runs a free 6-week email course on RAG covering everything from his consulting work, available at improvingrag.com.

### Context Engineering — Beyond RAG for Agentic Systems

Jason is developing Context Engineering as a natural evolution beyond RAG for agentic systems. The series started in August 2025 and has grown into a comprehensive framework covering tool response design, agent architecture, and prototyping methodology.

> "The breakthrough came when we realized chunks themselves were the limitation. When search results showed multiple documents, agents couldn't strategically decide which to load or how to explore further."

**Four Levels of Context Engineering:**
1. **Minimal Chunks** — Basic tool responses without metadata
2. **Chunks with Source Metadata** — Enables citations and strategic document loading
3. **Multi-Modal Content** — Optimizes tables, images, structured data for agents
4. **Facets and Query Refinement** — Reveals the complete data landscape for strategic exploration

**Key Concepts:**
- **Tool Response as Prompt Engineering** — Metadata teaches agents how to use tools in future calls
- **Agent Peripheral Vision** — Structured hints about the broader information space beyond top-k results
- **Context Pollution** — Noisy, low-signal outputs (logs, traces) that crowd out useful reasoning context
- **Context Rot** — Performance degradation as input length increases
- **Slash Commands vs Subagents** — "Bad context is cheap but toxic." Use subagents to isolate noisy operations

**Form Factor Decision Framework:**
- **Chatbots** — Conversational, audit trail as experience
- **Workflows** — Side-effect engines, deterministic outcomes
- **Research Artifacts** — Reports, summaries, data tables with consistent quality standards

> "We've moved far beyond prompt engineering. Now we're designing portfolios of tools (directory listing, file editing, search) and the context engineering that makes them work together."

## Related People

- **[[pydantic]]** — Samuel Colvin's data validation library; the foundation of Instructor's approach
- **[[eugene-yan]]** — Fellow practitioner in production ML evaluation; both emphasize systematic validation over benchmarking
- **[[shreya-shankar]]** — Overlapping focus on evaluation and validation rigor in LLM systems
- **[[bryan-bischof]]** — Shared philosophy of production-first ML engineering over demo-centric approaches
- **Weights & Biases** — Consulting client; shared community around ML engineering best practices
- **Modal Labs** — Consulting client; serverless GPU infrastructure for running structured output pipelines
- **Zapier, HubSpot, Limitless, Timescale** — Consulting clients across the AI application stack

## X Activity Themes

- **Structured outputs patterns** — Practical examples of extracting typed data from LLMs
- **Pydantic tips and tricks** — Validation techniques, schema design, error handling
- **Instructor library updates** — New features, multi-language ports, provider support
- **AI engineering best practices** — Production patterns, evaluation frameworks, RAG optimization
- **Conference talks and workshops** — Maven course updates, keynote announcements, community engagement
- **Software 3.0 philosophy** — Arguments for classical engineering rigor in LLM applications
- **Consulting insights** — Real-world patterns observed across startups and enterprises
