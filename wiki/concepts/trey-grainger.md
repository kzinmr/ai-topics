---
title: "Trey Grainger"
type: concept
aliases:
  - trey-grainger
created: 2026-04-25
updated: 2026-11-15
tags:
  - concept
  - person
  - information-retrieval
  - search
  - relevance
sources:
  - https://www.treygrainger.com/
  - https://github.com/treygrainger
  - https://aipoweredsearch.com/
---

# Trey Grainger

**Trey Grainger** is a search and information-retrieval practitioner, author, and founder — one of the most cited bridge figures between classic search relevance engineering and the LLM-era RAG/hybrid-retrieval wave. His book *AI-Powered Search* (Manning, 2024) with [[entities/doug-turnbull|Doug Turnbull]] and Max Irwin is a standard reference for integrating LLMs into production search architectures.

## Career

| Period | Role |
|--------|------|
| 2010s | Co-founder/CTO era at Lucidworks — **Chief Algorithms Officer / SVP of Engineering** (SolrCloud-based search products, Fusion ranking platform) |
| ~2021–2023 | CTO at **Presearch** (decentralized search-engine startup) |
| 2023 | Co-founded **Vectorize.io** — RAG consulting/product house focused on retrieval quality for LLM applications |
| Current | **Founder @ Searchkernel** (per treygrainger.com / GitHub bio, verified 2026-11-15); advisor to the Southern Data Science Conference; startup investor (blockchain, AI, healthcare, education) |

## Books & Teaching

- **AI-Powered Search** (Manning, Dec 2024) — with Doug Turnbull and Max Irwin; foreword by Grant Ingersoll. ~520 pages on RAG, semantic search, hybrid retrieval, learning-to-rank, click models, knowledge graphs, multimodal search, and deployment patterns. Codebase: `treygrainger/ai-powered-search` on GitHub.
- **Solr in Action** (Manning) — the definitive practical Solr guide, cementing his pre-LLM reputation in enterprise search.
- Teaches the **"AI-Powered Search" cohort course on Maven** (e.g., Nov–Dec cohort series) — hands-on labs on embedding pipelines, hybrid BM25+vector retrieval, and reranking.

## Why He Matters to This Wiki

Grainger is the recurring authority node connecting several wiki search topics: *learning-to-rank*, *hybrid retrieval*, *agentic search*, and the vector-DB ecosystem. His framing — **relevance engineering discipline applied to RAG** — is the counterweight to naive "embed and pray" retrieval: hybrid lexical+vector recall, rerankers, click-model supervision, and evaluation harnesses carry over from classic IR into LLM systems unchanged.

- Appeared via [[entities/softwaredoug]] and [[entities/doug-turnbull]] pages as co-author and Search School instructor.
- His Vectorize.io work sits alongside wiki pages like [[concepts/elasticsearch]], retrieval infra like [[entities/turbopuffer]], and [[concepts/learning-to-rank]].

## Related Pages

- [[entities/doug-turnbull]] — co-author, *AI-Powered Search*
- [[entities/softwaredoug]] — cites Grainger's book; search-relevance community
- [[concepts/learning-to-rank]] — core technique area
- [[concepts/agentic-search]] — the agent-era evolution of his beat

## Sources

- [treygrainger.com](https://www.treygrainger.com/) — About/Career sections (scraped 2026-11-15)
- [GitHub @treygrainger](https://github.com/treygrainger) — bio: "Founder @searchkernel. Author: AI-Powered Search"
- [aipoweredsearch.com](https://aipoweredsearch.com/) — book site
