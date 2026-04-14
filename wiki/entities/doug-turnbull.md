---
title: Doug Turnbull
created: 2026-04-10
updated: 2026-04-10
tags:
  - person
  - developer
  - ai
  - search
  - information-retrieval
  - relevance
  - open-source
  - author
  - consultant
---


# Doug Turnbull

| | |
|---|---|
| **X/Twitter** | [@softwaredoug](https://x.com/softwaredoug) |
| **Blog** | [softwaredoug.com](https://softwaredoug.com) |
| **GitHub** | [github.com/softwaredoug](https://github.com/softwaredoug) |
| **Role** | Search Relevance Expert, Author, Consultant |
| **Books** | *Relevant Search* (2016), *AI-Powered Search* (2025) |
| **Location** | Charlottesville, VA |

## Overview

Doug Turnbull (known online as **@softwaredoug**) is a **search relevance engineer, author, and consultant** who has been one of the most influential voices in the information retrieval and search engineering community since ~2013. He is the co-author of two landmark books: ***Relevant Search: With Applications for Solr and Elasticsearch*** (Manning, 2016) and ***AI-Powered Search*** (Manning, 2025).

His career spans the full arc of modern search evolution — from traditional lexical search engines (Solr, Elasticsearch) through learning-to-rank, vector/embedding search, and into agentic AI-powered retrieval. He has held senior engineering roles at **Reddit** (Principal Engineer), **Spotify** (Staff Relevance Engineer), **Shopify**, and **Daydream** (Principal Engineer), and spent ~8 years as **CTO of OpenSource Connections**, a search relevance consultancy where he advised dozens of organizations.

Turnbull is also a prolific open-source contributor, creator of tools like **Quepid** (search relevance testing workbench), the **Elasticsearch Learning to Rank plugin**, and **SearchArray** (pandas-based BM25 search library). He currently runs the **"Cheat at Search"** training course on Maven, teaching search professionals how to build effective retrieval systems in the age of LLMs.

His defining philosophy is that **search relevance is an engineering discipline, not magic** — it can be systematically improved through measurement, test collections, and iterative refinement. He frames search quality as a business problem: better search drives conversions, reduces support costs, and improves retention.

## Timeline

| Date | Event |
|------|-------|
| ~2013 | Enters search relevance field; begins consulting and writing about information retrieval |
| ~2013–2021 | **CTO at OpenSource Connections** — search relevance consultancy; advises dozens of organizations; builds open-source tools |
| 2016 | Publishes ***Relevant Search*** with John Berryman (Manning) — becomes the standard practical reference for search practitioners working with Elasticsearch and Solr |
| 2016 | Creates **Quepid** — open-source search relevance testing workbench; later released under Apache 2.0 license with free hosted tier |
| 2016–2022 | Develops and maintains **Elasticsearch Learning to Rank (ES-LTR) plugin** with collaborators; powers search at Yelp, Wikipedia, Snag, and others |
| ~2018 | Begins collaborating with Trey Grainger on what would become *AI-Powered Search* |
| 2021–2023 | **Staff Relevance Engineer at Spotify** — works on music search and recommendation relevance |
| Nov 2022–~2024 | **Principal Engineer at Reddit** — leads machine learning ranking efforts; creates a 2% increase in daily active users (DAU), the largest in Reddit search history |
| 2024 | Speaks at Berlin Buzzwords / Haystack EU on "Learning to Rank for Reddit Search: A Project Retro" |
| ~2024 | **Principal Engineer at Daydream** — builds hybrid search with CLIP models for AI fashion styling; doubles conversion rates (purchases vs. saves) |
| ~2024 | Works at **Shopify** — improves merchant search attributed revenue by 10% year-over-year |
| 2024 | Publishes ***SearchArray*** — open-source pandas extension for BM25 lexical search; makes search relevance experiments possible in Colab notebooks |
| Dec 2024 | ***AI-Powered Search*** published (Manning) — co-authored with Trey Grainger and Max Irwin; covers RAG, semantic search, learning-to-rank, hybrid retrieval, and LLM integration |
| 2025 | Launches **"Cheat at Search"** course on Maven — live, cohort-based training on search with LLMs and agents; rated 4.7/5 from 74+ reviews |
| 2025–2026 | Independent consultant and trainer; maintains the softwaredoug.com blog with daily search tips; explores agentic search workflows |

## Core Ideas

### Search Relevance as Engineering, Not Magic

Turnbull's foundational philosophy is that **search quality is not a mystical property — it is a systematic engineering problem** that can be measured, tested, and improved iteratively. His methodology emphasizes:

1. **Define "relevant"** for your specific use case and users
2. **Build test collections** — curated queries with human judgments (judgment lists)
3. **Measure continuously** — NDCG, precision, recall, and engagement metrics
4. **Iterate on signals** — adjust ranking features based on measurement feedback
5. **Start with naive baselines** — simple keyword search before complex ML

This approach democratized search relevance, making it accessible to organizations without dedicated IR research teams.

### The Judgment List Methodology

One of Turnbull's most influential contributions is the **judgment list** pattern: building curated collections of queries paired with human relevance judgments. These serve simultaneously as:

- **Test suites** — measuring whether configuration changes improve or degrade quality
- **Training data** — feeding learning-to-rank models
- **Communication tools** — aligning cross-functional teams on what "good" search looks like
- **Regression tests** — preventing quality degradation over time

He advocates for what he calls "grug-brained evals": don't spend months building perfect quality metrics. Start with simple 👍/👎 labels from coworkers and iterate.

### From Keyword to Semantic to Agentic Search

Turnbull has tracked and shaped the industry's evolution through search paradigms:

**Phase 1: Keyword Search (BM25, TF-IDF)** — Exact matching via inverted indices; works well for known-item searches; still the foundation of most production systems.

**Phase 2: Semantic Search (Embeddings)** — Vector representations capture meaning beyond keywords; dense retrieval via HNSW/ANN indexes; late-interaction models (ColBERT) score passages dynamically.

**Phase 3: AI-Powered Search (LLMs, RAG)** — Language models understand query intent, generate answers, and power conversational retrieval.

**Phase 4: Agentic Search** — LLM agents that iterate, refine queries, evaluate results, and recover from failures. "Agents put the Resilient in RAG."

In *AI-Powered Search*, he argues the future is **hybrid** — combining keyword precision, semantic understanding, and generative capabilities rather than replacing one with another. He has demonstrated this empirically, benchmarking Elasticsearch hybrid strategies (BM25 + KNN + RRF + boosting) to show that thoughtful hybrid construction outperforms any single approach.

### Learning to Rank (LTR)

Turnbull was an early and sustained advocate of **learning-to-rank**: using ML models (decision trees, XGBoost, LambdaMART) to combine multiple ranking signals (BM25 scores, field boosts, popularity, recency, personalization) into an optimal ranking function. His contributions include:

- The **Elasticsearch LTR plugin** — open-source integration enabling LTR within Elasticsearch
- **hello-ltr** — Jupyter notebook sandbox for learning and experimenting with LTR
- Production LTR systems at Reddit, where he scaled Learning to Rank to thousands of QPS
- Emphasis on the painful realities of LTR: garbage in, garbage out; the need for quality judgment lists; dealing with position bias and presentation bias

### RAG Isn't a Vector Search Problem

A central thesis in Turnbull's recent writing is that **the RAG community over-indexes on embeddings and under-appreciates classical IR**:

- Embeddings alone lack match/non-match awareness — a similarity score doesn't tell you if a document actually answers the query
- "Similarity floors don't work consistently" — a cutoff that works for one query may be disastrous for another
- BM25 and lexical matching remain essential complements to vector retrieval
- User engagement data (clicks, hovers, session behavior) is the most valuable signal for improving RAG quality — yet most RAG teams rely exclusively on human/LLM evaluation

He calls this gap **"RAG's big blindspot"** — the lack of engagement-based evaluation in an era obsessed with LLM judges.

### Query Understanding > Ranking

Turnbull consistently argues that **query understanding matters more than ranking algorithms**:

- "Content understanding IS query understanding"
- LLMs eliminate the excuse for unstructured query handling — all search is structured now
- Manual search management (synonyms, rules, boosts for specific queries) often outperforms algorithmic approaches
- At Shopify, the user segment with the highest conversions was the one with manually controlled results — proving that domain expertise beats generic ranking models
- "The dirty secret of Google and Amazon search is all the manual annotation, rules, etc they manage"

### Bayesian BM25 and Score Calibration

In 2026, Turnbull published work on **Bayesian BM25** — a method for calibrating BM25 scores into probabilities:

> `P(R) = prob(embeddings) × prod(lexical)`

This provides a principled way to combine lexical and embedding scores in hybrid search, treating them as probabilistic signals rather than arbitrary numbers. It addresses a long-standing pain point: BM25 scores are unbounded and hard to interpret (0.5? 5.1? 12.51?), making them difficult to fuse with vector similarity scores.

### Throwaway Code Over Design Docs

Reflecting on the AI coding revolution, Turnbull advocates for **rapid, disposable prototypes** over lengthy architecture documents:

> "If you have discipline to throw away your first idea, draft, throwaway code — you can move faster than any design doc."

With AI generating code, **tests become the most important artifact to maintain**: "The tests are the code now."

### SearchArray: Making Search Less Weird

Turnbull built **SearchArray** (304 GitHub stars) to make search relevance experimentation accessible:

> "Traditional search engines are weird. As my job looks more and more like ML engineering, these backend systems feel even stranger."

SearchArray is a pandas extension array backed by an inverted index. It lets practitioners run full end-to-end search relevance experiments in a single Colab notebook — no Solr or Elasticsearch instance required. Under the hood it uses Cython-optimized roaring bitmap intersections for phrase search.

> "If I had Relevant Search to write over again, I'd use a tool like this. Get lexical search away from the baggage of any one particular giant search stack."

### The Business Case for Search

Turnbull frames search relevance as a **business problem**, not a technical one:

- Better search → higher conversion rates → more revenue
- Better search → fewer support queries → lower costs
- Better search → improved user satisfaction → higher retention

His track record proves this:
- **Reddit**: 2% DAU increase from ML ranking improvements
- **Daydream**: 2× conversion rate improvement from CLIP-based hybrid search
- **Shopify**: 10% YoY revenue improvement from merchant search optimization

### Don't Have F-You Money? Build an F-You Network

Beyond technical work, Turnbull is known for pragmatic career advice:

> "Start with Who, not Why. Work with amazing people you love collaborating with, the rest falls out."

He advocates building a professional network through genuine service and deep expertise — a safety net that provides career resilience independent of any single employer.

## Key Projects & Works

### *Relevant Search* (Manning, 2016)
Co-authored with John Berryman, foreword by Trey Grainger. The definitive practical guide to search relevance engineering using Elasticsearch and Solr. Covers relevance scoring, query parsing, analyzers, synonym handling, learning-to-rank, and evaluation methodologies. 360 pages. Still considered essential reading for search practitioners.

### *AI-Powered Search* (Manning, 2025)
Co-authored with Trey Grainger and Max Irwin, foreword by Grant Ingersoll. 520 pages covering the integration of LLMs into search architectures: RAG, semantic search, hybrid retrieval, learning-to-rank, click models, knowledge graphs, multimodal search, and practical deployment patterns. Turnbull contributed chapters 10–12 on "Learning to Rank," "Automated Learning to Rank with Click Models," and "Overcoming Bias in Learned Relevance Models."

### Quepid (o19s/quepid)
Open-source (Apache 2.0) search relevance testing workbench. 339 stars. Supports Elasticsearch, Solr, OpenSearch, Vectara, Algolia, and custom backends. Features include test cases, human judgment gathering, NDCG calculation, query snapshots, and team collaboration. Originally a closed-source product, Turnbull's team at OpenSource Connections open-sourced it in 2019 with a free hosted tier.

### Elasticsearch Learning to Rank Plugin (o19s/elasticsearch-learning-to-rank)
Open-source plugin enabling machine learning-based ranking within Elasticsearch. Used in production at Yelp, Wikipedia, Snag, and others. Turnbull co-created it with Erik Bernhardson, David Causse, and Daniel Worley. Includes the hello-ltr sandbox for experimentation.

### SearchArray (softwaredoug/searcharray)
Pandas extension array for BM25-powered lexical search. 304 stars. Makes search relevance experiments possible in a single Colab notebook without standing up a search engine. Includes Cython-optimized phrase search with roaring-like bitmap intersections.

### Cheat at Search (Maven Course)
Live, cohort-based training course on search engineering with LLMs and agents. Rated 4.7/5 from 74+ reviews. Covers information retrieval as an agentic process, LLM query understanding, BM25 + lexical retrieval, embedding retrieval, hybrid search, evaluation/NDCG, and agentic search. Priced at $1,300 per student with free "Essentials" lightning lessons available.

### local-llm-judge (softwaredoug/local-llm-judge)
Python project enabling local LLMs to serve as search relevance judges. 28 stars. Runs hundreds of relevance judgment pairs per minute on a MacBook, democratizing search evaluation without cloud API costs.

### Consulting & Training
Turnbull offers $12,000 team training courses (up to 12 participants) covering:
- Traction on Search Relevance at Your Organization
- Lexical + Vector → Hybrid Search
- Generative AI Augmented Retrieval

He describes himself as available as a "fractional search team lead" for organizations needing search expertise.

## Speaking & Community

Turnbull is a regular speaker at search industry conferences:

- **Berlin Buzzwords / Haystack EU** (2024): "Learning to Rank for Reddit Search: A Project Retro" with Charles Njoroge
- **Elastic{ON}16** (2016): "The Ghost in the Search Machine"
- **MICES 2024** (Mix Camp E-Commerce): "Planning of E-Commerce Relevance Work"
- **Relevance Cornucopia** workshops: Intensive small-group training on "Think Like a Relevance Engineer" and "Hello LTR"

He maintains an active blog at softwaredoug.com with regular "daily search tips" — concise, practical observations about search engineering — and a newsletter with thousands of subscribers.

## Key Quotes

> "Agents put the Resilient in RAG."

> "Grug-brained evals: Big brain spend months building perfect quality metrics. Grug brain no trust, and just want dumb labels from coworkers 👍/👎."

> "The tests are the code now."

> "Content understanding IS query understanding."

> "All search is structured now — there's no excuse for unstructured search queries in the age of LLMs."

> "If you have discipline to throw away your first idea, draft, throwaway code — you can move faster than any design doc."

> "Start with Who, not Why. Work with amazing people you love collaborating with, the rest falls out."

> "RAG isn't a vector search problem. Through market forces, embeddings became the singular framework we understood RAG. It's the wrong lens."

## Related

- [[Relevant Search]] — His foundational book on search relevance engineering
- [[AI-Powered Search]] — His 2025 book on LLM integration in search
- [[Elasticsearch]] — Primary search engine in his early work
- [[Apache Solr]] — Search platform he worked with extensively
- [[Learning to Rank]] — ML approach to combining ranking signals
- [[RAG]] — Retrieval-Augmented Generation
- [[BM25]] — Probabilistic ranking function
- [[NDCG]] — Normalized Discounted Cumulative Gain
- [[Quepid]] — Open-source search relevance testing workbench
- [[SearchArray]] — Pandas-based BM25 search library
- [[Trey Grainger]] — Co-author of AI-Powered Search
- [[John Berryman]] — Co-author of Relevant Search
- [[Max Irwin]] — Co-author of AI-Powered Search
- [[OpenSource Connections]] — Search relevance consultancy where he served as CTO
- [[Reddit]] — Platform where he achieved 2% DAU increase with LTR
- [[Shopify]] — Where he improved merchant search revenue 10% YoY
- [[Spotify]] — Where he worked as Staff Relevance Engineer
- [[Daydream]] — AI fashion styling company where he doubled conversions

## Sources

- [softwaredoug.com Blog](https://softwaredoug.com)
- [Speaking Info & Bio](https://softwaredoug.com/speaking-info/)
- [Training Options](https://softwaredoug.com/training/)
- [Cheat at Search on Maven](https://www.maven.com/softwaredoug/cheat-at-search)
- [GitHub: @softwaredoug](https://github.com/softwaredoug)
- [X/Twitter: @softwaredoug](https://x.com/softwaredoug)
- [Relevant Search (Manning)](https://www.manning.com/books/relevant-search)
- [AI-Powered Search (Manning)](https://www.manning.com/books/ai-powered-search)
- [Quepid GitHub](https://github.com/o19s/quepid)
- [Elasticsearch LTR Plugin](https://github.com/o19s/elasticsearch-learning-to-rank)
- [SearchArray GitHub](https://github.com/softwaredoug/searcharray)
- [Berlin Buzzwords 2024 Talk](https://www.youtube.com/watch?v=gUtF1gyHsSM)
- [OpenSource Connections Blog](https://opensourceconnections.com/blog/author/doug-turnbull/)
- [AI-Powered Search Author Page](https://aipoweredsearch.com/people/doug-turnbull/)
- [Elastic Blog Author Page](https://www.elastic.co/blog/author/doug-turnbull)
- [Clay Profile](https://clay.earth/profile/doug-turnbull)
