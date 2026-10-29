---
title: "Pinecone"
type: entity
created: 2026-05-08
updated: 2026-10-28
tags:
  - company
  - search
  - model
  - infrastructure
aliases:
  - "Pinecone.io"
  - "Pinecone Vector Database"
sources:
  - https://www.pinecone.io/
  - https://www.pinecone.io/blog/
  - raw/articles/2026-06-06_pinecone_nexus-ea-benchmarks.md
  - raw/articles/2026-07-17_pinecone_sparse-v3.md
  - raw/articles/2026-07-17_pinecone_text-match-filters.md
  - raw/articles/2026-08-11_pinecone_the-ceiling-was-never-the-model.md
  - raw/articles/2026-08-11_pinecone_pinecone-nexus-generally-available.md
  - raw/articles/2026-10-23_pinecone_when-vectors-became-an-implementation-detail.md
  - raw/articles/2026-10-28_pinecone_introducing-pg-pinecone.md
---

# Pinecone

**Pinecone** (pinecone.io) is a vector database company that provides managed vector search infrastructure for AI applications, LLM embeddings, and semantic search. Founded by Edo Liberty, Pinecone's platform enables developers to store, search, and retrieve high-dimensional vector embeddings at scale.

> **Note:** Pinecone (pinecone.io) is a vector database company. It is **not** to be confused with [[entities/pi|Pi]], the minimal AI coding harness created by Mario Zechner.

| | |
|---|---|
| **Type** | Vector Database / AI Infrastructure |
| **Founded** | 2019 |
| **Leadership** | Edo Liberty (CEO, ex-AWS SageMaker) |
| **Key Products** | Pinecone vector database, Pinecone Serverless |
| **Funding** | $138M Series B at $750M valuation (2023), $100M Series B-1 |
| **Website** | [pinecone.io](https://www.pinecone.io) |
| **Tech Blog** | [pinecone.io/blog](https://www.pinecone.io/blog/) (sitemap monitoring added) |

## Key Facts

- Founded 2019 by Edo Liberty, former head of Amazon SageMaker
- Purpose-built vector database optimized for AI/LLM embeddings and semantic search
- Raised $138M Series B at $750M valuation (2023), led by Andreessen Horowitz
- Additional $100M Series B-1 round
- Pinecone Serverless offers cost-efficient, auto-scaling vector storage
- Widely used in RAG (Retrieval-Augmented Generation) pipelines and AI agent memory architectures

## Products

- **Pinecone Vector Database** — Managed, cloud-native vector database for high-dimensional embeddings. Supports real-time similarity search, metadata filtering, and hybrid search.
- **Pinecone Serverless** — Auto-scaling vector database that separates compute and storage, reducing costs for variable workloads.

## Nexus: Context Compiler Platform (June 2026)

Pinecone launched **Nexus**, a "Context Compiler" that transforms how AI agents interact with data. Rather than requiring agents to search across multiple retrieval surfaces on every query, Nexus compiles structured, semi-structured, and unstructured sources into task-specific knowledge artifacts that agents consume in a single call.

### The Problem: Agent "Orientation Tax"

Before Nexus, Pinecone's internal AskData analytics agent faced significant inefficiency:
- **22 tools** across two agents (DataAgent + Curator)
- **6 dedicated retrieval surfaces** (Pinecone Assistant + three indexes + dbt file reads + SQL search)
- **1,300 lines of Airflow code** syncing Slack, Gong, and BigQuery logs daily
- **2,200 lines of Curator code** maintaining 18,000 lines of hand-curated markdown across 234 files
- A multi-part question took **9 steps and ~240,000 tokens** — with 7 of 9 steps spent just orienting (finding tables, columns, filters) before actual analysis

### Nexus Architecture

Nexus introduces several key primitives:
- **Context Compiler**: Takes multiple sources and produces focused, task-specific briefs (~1,200 tokens vs. 10,000+ raw chunks)
- **KnowQL**: Query language for accessing compiled knowledge
- **Nexus Contexts**: Managed knowledge representations that evolve organically based on task and eval signals

### Quantitative Results (AskData V1 → V2 Migration)

| Metric | V0 (Claude Code raw) | V1 (Classic RAG) | V2 (Nexus) | V1→V2 Improvement |
|--------|---------------------|-----------------|------------|-------------------|
| Avg input tokens/question | ~625,287 | 64,008 | 39,595 | **-38%** |
| Avg turns/question | ~21 | 4.5 | 4.6 | ≈ same |
| Avg cost/question | $0.35 | $0.20 | $0.07 | **-80%** |
| Code complexity | 25,000+ lines | 25,000+ lines | 1,000 lines (Nexus glue) | **-96%** |
| Tools exposed to agent | N/A | 22 | 10 | **-55%** |

**Key insights:**
1. **Compile once, read many**: Nexus spends ~8,000 tokens once to give the agent a brief that saves ~24,000 downstream (3:1 ratio)
2. **Fewer tools, better agents**: Collapsing 6 tools to 2 cut input-token spread by ~4×
3. **Structured data tells you *what*, unstructured tells you *why***: The warehouse gives numbers, but business rationale lives in Slack threads, Gong transcripts, runbooks
4. **Same accuracy, fraction of the budget**: V2 matched V1's 68.3% accuracy on the 101-question regression set

### Nexus Customer Benchmark Results (June 2026)

Three customer benchmarks from Nexus's early-access program demonstrate consistent improvements across different domains:

**1. Melange Technologies (Patent Search/SEP)**
- **Domain**: IP/Patent Litigation, Standard Essential Patent (SEP) claim validation against 3GPP standards
- **Corpus**: 3GPP Release 18, ~1,800 .docx/.doc files, ~2.3 GB (pilot: 29-spec 5G NR slice, ~31 MB)
- **Eval**: 30 SEP-candidacy questions
- **Nexus vs Agentic RAG**: Accuracy 52.7% → 66% (25% more accurate), Latency 187s → 44s (77% faster), Token cost 201K → 5.9K (97% fewer tokens)
- **Quote (Joshua Beck, CEO Melange)**: "These early results are genuinely exciting: a 34x reduction in token cost..."
- **Business impact**: cost-prohibitive autonomous patent search becomes viable; sub-minute latency fits litigation timelines

**2. FinTech (M&A Due Diligence)**
- **Domain**: Financial Technology / Investment Management
- **Corpus**: 90 documents across 10 category folders (PDFs, XLSX, markdown) — full synthetic M&A dataroom for a $42M ARR SaaS company
- **Eval**: 30 multi-hop M&A diligence queries
- **Nexus vs Agentic RAG**: Accuracy 57% → 65% (14% more accurate), Latency 61s → 32s (48% faster), Token cost 66K → 5K (92% fewer tokens)
- **Nexus resolved each question in a single retrieval vs ~10 iterative steps**
- **Business impact**: workflows requiring analyst hours now complete in seconds

**3. SMS/E-commerce SaaS (Revenue Intelligence from Gong Transcripts)**
- **Domain**: SMS Marketing / E-commerce SaaS
- **Corpus**: 217 Gong call transcripts, ~45 MB structured JSON
- **Eval**: 40 revenue intelligence queries requiring cross-call synthesis
- **Nexus vs Agentic RAG**: Accuracy 36% → 70% (94% more accurate), Latency 28s → 23s (18% faster), Token cost 27K → 4K (85% fewer tokens)
- **Key insight**: Agentic RAG cannot see across the full corpus simultaneously; Nexus derives structured representations making cross-call patterns directly addressable
- **Business impact**: largest accuracy improvement across all benchmarks

**Summary Table**

| Customer/Domain | Use Case | Outcome |
|---|---|---|
| Melange / IP & Patent Litigation | SEP claim validation | 97% fewer tokens, 77% faster, 25% more accurate |
| FinTech / Investment Mgmt | M&A due diligence | 92% fewer tokens, 48% faster, 14% more accurate |
| SMS SaaS / E-commerce | Revenue intelligence | 85% fewer tokens, 18% faster, 94% more accurate |

**Key Insight**: Across all three cases, the same architectural dynamic appears — Nexus compiles structured artifacts before queries arrive, eliminating the agentic RAG retrieval loop that burns tokens and latency.

### Demo

Pinecone published a [Nexus Analyst Demo](https://nexus-analyst-web.vercel.app/) comparing classic RAG (multi-tool, manual chunking) vs Nexus (single `nexus_query` tool, compiled briefs) side-by-side on the same fictional SaaS company data.

Source: raw/articles/2026-06-03_pinecone_inside-askdata.md

## Sparse V3 — Term-Major Index Layout (July 2026)

Pinecone announced **Sparse V3**, a major redesign of their sparse index architecture. V3 reorganizes the index around **terms** instead of document-major blocks. Each term owns its posting blocks; queries only load blocks for referenced terms. Disk I/O reduction: **151×** for SPLADE, **1,428×** for BM25 with identical recall.

The architecture uses metadata blocks for pre-load skip decisions (MaxScore pruning), delta compression, and term-specific score quantization. Heuristics were tuned via property-based tests combined with Claude-driven iteration over hundreds of combinations.

This is significant for [[concepts/lexical-search|lexical search]] pipelines and hybrid retrieval strategies.

Source: raw/articles/2026-07-17_pinecone_sparse-v3.md

## Text Match Filters for Agents (July 2026)

Pinecone introduced **Full Text Search filters** designed specifically for AI agents. The lexical query restricts the candidate pool before semantic search, solving the **"unstated context" problem** — for example, "top presidential candidates" no longer returns French election results when the user's context is US politics.

No pre-labeling is required. This is critical for [[concepts/agentic-rag|agentic pipelines]] where bad retrievals compound wasted tool calls. In **public preview**.

Source: raw/articles/2026-07-17_pinecone_text-match-filters.md

## Nexus GA — "It's the Knowledge, Not the Models" (August 2026)

Pinecone announced **Nexus GA** (Aug 6, 2026) — generally available for deployment in a customer's own cloud, five weeks after Public Preview opened. Two companion posts ("[The Ceiling Was Never the Model](https://www.pinecone.io/blog/the-ceiling-was-never-the-model/)" and "[Nexus GA: It's the Knowledge, Not the Models](https://www.pinecone.io/blog/pinecone-nexus-generally-available/)") frame the launch around a shared industry conclusion: in enterprise production, **it is the knowledge, not the model, that decides whether AI works**.

**The Sierra connection**: Sierra AI (Bret Taylor's company) "AI-pilled" its whole company with an internal agent named **Pinecone**. On τ-Knowledge, the benchmark Sierra itself built, an agent using Pinecone Nexus posted the top score — ahead of agents running on frontier models alone. Both companies landed on the same thesis independently.

**τ-Knowledge benchmark results** (agent + Nexus layer vs same frontier models with the benchmark's own tools):
- GPT-5.2 + Nexus: **+12% accuracy at 80% lower cost** (tool calls 42.5→17.7, model calls 81.7→42.6)
- GPT-5.5 + Nexus: held accuracy at **77% lower cost** (tool calls 28.6→16.0, model calls 60.9→39.4)
- Task cost fell from **$1.45 to $0.53**; the advantage held on 96 of 97 tasks
- Across the full benchmark: agent with Nexus posted **47.4% vs best frontier model 46.4%, at 74% less cost per task**

**Retrieval is the cost driver**: Blended inference prices fell ~67% YoY, but enterprise AI budgets kept climbing because one task fans out into dozens of model calls. More than **85% of an agent's effort** goes to fetching knowledge before it reasons; Goldman Sachs projects token consumption to **multiply 24x by 2030**; 68% of teams cap agents at ten steps before human intervention. A bigger model doesn't fix a bill that scales with retrieval.

**Moat argument (Nadella/Karp)**: Models are becoming interchangeable commodities; the durable enterprise advantage is its own knowledge and working practices. Satya Nadella: the moat that lasts is enterprise data/context/memory under its own control. Alex Karp (Palantir): frontier labs oversold their models while absorbing the proprietary edge of paying companies — "the moat leaks out one API call at a time."

**Pinecone's own support queue**: After pointing Nexus at its own support queue (July 17), ticket resolution rose from **24.6% to 55.1%** — more than half of tickets close without a person touching them.

**Scale of early adoption**: 800+ organizations signed up for early access; 100+ enterprises (many among the largest in the world) ran their data through it; engagements compiled **3.5M source chunks into ~26,000 structured knowledge artifacts**. Nexus curates incrementally so only what changes gets recompiled.

**Key architecture**: Nexus compiles data once, ahead of time, into governed domain-specific knowledge; agents query it via **KnowQL** (a query language built for agents) and get typed, cited answers in a single call. Every field carries a citation + confidence score; access control is applied at retrieval time, not prompt time. Runs in your own cloud on the models you choose with no standing Pinecone access to customer data.

Source: raw/articles/2026-08-11_pinecone_the-ceiling-was-never-the-model.md, raw/articles/2026-08-11_pinecone_pinecone-nexus-generally-available.md

## Vectors as an Implementation Detail — Integrated Embedding on the Documents API (October 2026)

Pinecone's engineering history post frames the company's 2.5-year API arc as one goal: **take preparation work off the user**, with vectors being "an implementation detail" essential to how the database finds things but not something a developer should build.

**Lineage:** BYO-vectors via the Vectors API (2021) → slab storage (in-memory buffer, immutable self-describing slab files, background compaction; made index selection composable across index *kinds*) → **Records API** integrated embedding (2024) → **Documents API** with native full-text search (2025-26) → **integrated embedding as a per-field schema option** (2026).

The Records API turned out to be **premature**: it wrapped the Vectors API, so text still lived in a metadata field, one index was locked to one model and one text field, and there was no room to add native full-text. The Documents API rebuilt from the top down around a typed document schema (string / dense vector / sparse vector / metadata) and **inverted the request shape** — the Vectors API made your data conform to it; the Documents API conforms to yours. Full-text fields keep the raw text once in the slab plus a **Tantivy inverted index** scored with BM25, fixing the "text-as-metadata" problem (metadata indexes are built for exact-value filtering, which raw prose never benefits from).

**Now shipping:** a single string field can carry `full_text_search` (stemming, stop words) *and* `embed: {model: ...}` simultaneously. Writes take plain text — Pinecone embeds with the field's model, stores the vector beside the text, and builds the text index in one write; **if embedding fails nothing in the request is written**. Queries also go in as text and are embedded with the same model.

**Latency win**: self-embedding costs two round trips per search (embedding API, then Pinecone); integrated embedding collapses it to one. Pinecone measured **~3.5× faster at the median** versus calling its standalone embedding API then searching with the vector — most of the gap is simply the avoided network hop. Roadmap: hybrid search, integrated reranking, multiple vector fields per document.

Source: [[raw/articles/2026-10-23_pinecone_when-vectors-became-an-implementation-detail]]

## pg_pinecone — Open-Source Postgres Extension on Pinecone's Engine (October 2026)

Pinecone released **pg_pinecone**, an Apache-2.0 Postgres extension that runs the same search engine Pinecone operates at scale *inside* Postgres, over the `pgvector` vector columns already in the database. It is Pinecone's first open-source in-database play and a direct architectural challenge to pgvector's HNSW default. ([blog](https://www.pinecone.io/blog/introducing-pg-pinecone/), Oct 27 2026)

**Three engines, one SQL surface** — `pinecone.set_engine()` switches between them without changing queries (`ORDER BY embedding <=> $1 LIMIT 10`):
- `native` (default): builds and searches its own index entirely inside Postgres — no Pinecone account, API key, or network call
- `pgvector`: delegates to the HNSW index the user may already run
- `remote`: pushes search to Pinecone's managed service

**Why not a graph.** The native engine replaces the proximity graph with an **inverted-file (IVF) index over compressed vector codes** — each vector stored as a **RaBitQ** code (~1 bit/dimension plus correction values; Gao and Long, SIGMOD 2024 — the same quantizer family benchmarked in [[concepts/vq-bench]]), packed per cluster so a search reads a few contiguous pages instead of hopping a graph that must stay resident in RAM.

**Benchmarks** (1M × 768-dim wiki_dpr, AWS r6id.4xlarge, 16 vCPU / 128 GB, PostgreSQL 17/18, p50 at k=10):

| Metric | pg_pinecone native | HNSW (halfvec) | HNSW (full) |
|---|---|---|---|
| Index size | **136 MB** | 2.0 GB | 4.1 GB |
| Latency @ 0.95 recall | **1.3 ms** | 1.7 ms | 2.7 ms |
| Latency @ 0.99 recall | **2.3 ms** | 4.7 ms | 6.7 ms |
| Filtered (10% match) | **1.000 recall / 12.3 ms** | 0.920 recall / 5.9 ms (iterative) | — |

**The filtered-search claim is the sharpest one.** pgvector HNSW *post*-filters — it finds nearest neighbours then applies `WHERE`, so a narrow scope (one tenant in a hundred) discards most candidates and a query can return fewer rows than its `LIMIT`. The native engine filters *during* search and picks a strategy by selectivity: **pre-filtering** (exact, full-vector scoring across all clusters) when ≤3% of rows match, **single-stage filtering** (probe up to half the nearest clusters, check the filter inside each before scoring) above that. The filter column's value is stored beside each RaBitQ code and row-counts per value are precomputed at build time.

**Operational caveats stated in the post**: inserts join the nearest cluster and are immediately searchable, but centroids are fixed at build time — after a bulk load that doubles the table or introduces off-distribution data, `REINDEX` or automatic maintenance is needed to rebalance clusters.

**Strategic read.** Pinecone's commercial interest is in its managed engine, so `native` being free and networkless is a developer-ecosystem/mindshare play rather than a hosting play; the benchmark table is vendor-run and unpublished outside its own harness README. The substantive, falsifiable contribution independent of that is the **IVF + RaBitQ + filter-during-search** combination beating HNSW on memory and *filtered* recall — the workload class where graph indexes are weakest. Related: [[concepts/vector-search]], [[concepts/vector-databases]], [[concepts/vq-bench]].

Source: [[raw/articles/2026-10-28_pinecone_introducing-pg-pinecone]]

## Related

- [[entities/voyage-ai]] — Embedding model provider; commonly paired with Pinecone for RAG pipelines
- [[entities/openai]] — Embedding models (text-embedding-3, Ada) often stored and queried via Pinecone
- [[entities/anthropic]] — Claude models integrated with Pinecone for long-term memory and RAG
- [[entities/langchain]] — LangChain provides native Pinecone integration for vector store components
