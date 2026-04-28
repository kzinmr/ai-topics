---
title: Doug Turnbull - Key Projects & Works
type: entity-sub
parent: doug-turnbull
created: 2026-04-10
updated: 2026-04-10
tags:
  - person
  - projects
  - open-source
  - books
sources: []
---

# Doug Turnbull: Key Projects & Works

## Books

### *Relevant Search* (Manning, 2016)
Co-authored with John Berryman, foreword by Trey Grainger. The definitive practical guide to search relevance engineering using Elasticsearch and Solr. Covers relevance scoring, query parsing, analyzers, synonym handling, learning-to-rank, and evaluation methodologies. 360 pages. Still considered essential reading for search practitioners.

### *AI-Powered Search* (Manning, 2025)
Co-authored with Trey Grainger and Max Irwin, foreword by Grant Ingersoll. 520 pages covering the integration of LLMs into search architectures: RAG, semantic search, hybrid retrieval, learning-to-rank, click models, knowledge graphs, multimodal search, and practical deployment patterns. Turnbull contributed chapters 10–12 on "Learning to Rank," "Automated Learning to Rank with Click Models," and "Overcoming Bias in Learned Relevance Models."

## Open-Source Projects

### Quepid (o19s/quepid)
Open-source (Apache 2.0) search relevance testing workbench. 339 stars. Supports Elasticsearch, Solr, OpenSearch, Vectara, Algolia, and custom backends. Features include test cases, human judgment gathering, NDCG calculation, query snapshots, and team collaboration. Originally a closed-source product, Turnbull's team at OpenSource Connections open-sourced it in 2019 with a free hosted tier.

### Elasticsearch Learning to Rank Plugin (o19s/elasticsearch-learning-to-rank)
Open-source plugin enabling machine learning-based ranking within Elasticsearch. Used in production at Yelp, Wikipedia, Snag, and others. Turnbull co-created it with Erik Bernhardson, David Causse, and Daniel Worley. Includes the hello-ltr sandbox for experimentation.

### SearchArray (softwaredoug/searcharray)
Pandas extension array for BM25-powered lexical search. 304 stars. Makes search relevance experiments possible in a single Colab notebook without standing up a search engine. Includes Cython-optimized phrase search with roaring-like bitmap intersections.

### local-llm-judge (softwaredoug/local-llm-judge)
Python project enabling local LLMs to serve as search relevance judges. 28 stars. Runs hundreds of relevance judgment pairs per minute on a MacBook, democratizing search evaluation without cloud API costs.

## Training & Consulting

### Cheat at Search (Maven Course)
Live, cohort-based training course on search engineering with LLMs and agents. Rated 4.7/5 from 74+ reviews. Covers information retrieval as an agentic process, LLM query understanding, BM25 + lexical retrieval, embedding retrieval, hybrid search, evaluation/NDCG, and agentic search. Priced at $1,300 per student with free "Essentials" lightning lessons available.

### Consulting & Training
Turnbull offers $12,000 team training courses (up to 12 participants) covering:
- Traction on Search Relevance at Your Organization
- Lexical + Vector → Hybrid Search
- Generative AI Augmented Retrieval

He describes himself as available as a "fractional search team lead" for organizations needing search expertise.

## Related

- [[doug-turnbull]] — Main entity page
- [[concepts/quepid]] — Search relevance testing workbench
- [[concepts/searcharray]] — Pandas-based BM25 search library
