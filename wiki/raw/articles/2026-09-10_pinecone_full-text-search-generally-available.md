---
title: "Full-Text Search is Now Generally Available In Pinecone Database"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/full-text-search-generally-available/"
scraped: "2026-09-10T06:00:29.020754+00:00"
lastmod: "2026-09-09T12:28:04Z"
type: "sitemap"
---

# Full-Text Search is Now Generally Available In Pinecone Database

**Source**: [https://www.pinecone.io/blog/full-text-search-generally-available/](https://www.pinecone.io/blog/full-text-search-generally-available/)

←
Blog
Full-Text Search is Now Generally Available In Pinecone Database
Manish Talreja
,
Gavin Johnson
Sep 9, 2026
Product
Share:
Jump to section:
TL;DR
The queries vector embeddings get wrong
Where exact-match precision matters
How full-text search works in Pinecone
Search that finds what you mean and exactly what you say
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
If you run search, recommendations, RAG, or agents, the queries hitting your retrieval system come in more than one kind. Semantic search was built for when you need to search by meaning. The embedding captures what the user meant, and a question finds the right data even when its wording differs from the text.
Identifiers and exact phrases are a different kind of query. SKUs, part numbers, error codes, case numbers, and order IDs are literal strings. The literal string is the query, and embeddings rarely match literal strings. In a best case scenario, an embedding model splits PROD-001 into subword tokens (if the token was present in the embedding model's training data) and places it beside every other SKU. So, a search for the part number a customer provided, PROD-001 for this example, returns PROD-002 and PROD-003 alongside the correct part. The result is confidently close when the user needs exactly correct. Nothing throws an error. The agent answers from the wrong documentation, and nothing in the response indicates that there's a problem at all.
Matching exact words has usually meant running a node-based search system. These engines are built for the job, and they are good at matching exact words, but running one is its own project that your team owns: nodes to size, capacity to plan as the corpus grows, shards, memory, merge cycles to tune, and version upgrades to run. The engine is good at the job, but keeping it running requires your team's time and effort.
After months of private preview validation with our user partners, today, we're announcing that
full-text search is generally available in Pinecone Database
. It adds BM25 keyword ranking and text-match filters to the same index as your dense vectors, so agents get the exact order number or error code embeddings miss, with no separate system to tune and maintain.
TL;DR
If your search, recommendation, RAG, or agent workload mixes questions with identifiers and exact phrases, Full-Text Search gives you:
Exactly correct instead of confidently close
on the queries embeddings get wrong: SKUs, error codes, case numbers, order IDs, and exact quoted phrases.
BM25 keyword ranking
across multiple text fields per index, with Lucene query syntax, fuzzy matching, and tokenization and stemming in 18 languages.
Text-match filters
that restrict the results of a semantic search to the documents matching the filter. One query both retrieves based on the identifier and ranks the rest by meaning.
One index and one schema
for text fields, dense vectors, and sparse vectors, queried through the Documents API, with no cluster to tune, patch, or upgrade.
Usage-based capacity
by default, metered in the same read units and write units as vector indexes.
Dedicated Read Nodes
are available for provisioned read capacity, and
BYOC
for running inside your own cloud.
The queries vector embeddings get wrong
Semantic search works on the queries it was designed for, where meaning is the signal. A literal string is a different test, and a vector-only index fails it the same way every time.
Lookalikes rank as well as the right record. Every SKU with the same pattern shares most of its subword tokens with PROD-001, and the ranking has no way to tell which one the customer meant.
The failure is silent. A vector search always returns its nearest neighbors. There is no empty result to check for and no error to catch. A wrong answer looks the same as a right one until a customer notices.
The alternative is a node-based lexical engine. A lexical engine handles the exact word queries well, but it comes with nodes your team sizes, tunes, and upgrades.
Those failures have a business cost:
Wrong actions that look right. An agent that retrieves the lookalike ships the wrong part or applies the wrong policy, and each one erodes users' trust.
An ongoing cost of ownership. Someone sizes the nodes, plans capacity as the corpus grows, and runs the upgrades, and that work continues for as long as the system is in production.
Slower delivery. Engineers spend their time maintaining search infrastructure instead of building the product.
Full-text search is built for the queries where the answer depends on a literal string, and it runs in the same index as the semantic search that handles all of your other queries.
Where exact-match precision matters
Identifier-heavy retrieval.
SKUs, part numbers, error codes, and case numbers are where embedding models fail most visibly, and where full-text search shines. BM25 ranks the term itself, and a text-match filter returns nothing when no document carries the identifier. So, a miss reads as a miss instead of a lookalike.
Recommendations with hard constraints.
A customer who names a specific model or a compatible part number expects every recommendation to honor it, and embeddings alone can't do that (e.g., accessories for PROD-001 land next to the ones for PROD-002). A text-match filter pins the candidate set to items whose text carries the literal term, and the dense vector query ranks within it, so similarity never overrides a constraint the user stated. This is also true for content recommendations keyed to a ticker symbol, regulation number, or a streaming video ID.
RAG over enterprise documents.
A conceptual question needs semantic search. A query for a specific clause or an error code requires the exact term, and only lexical search reliably returns it. With full-text search and semantic search in the same index, the RAG system retrieves the clause the question depends on instead of a passage that resembles it.
Agent tool use over structured data.
Agents often need to look up data using a value from an earlier step, like an order number or a status string. Full-text search matches the value itself, so every step after that builds on the right data.
How full-text search works in Pinecone
Pinecone Database indexes created with the Documents API now run on a document schema. You declare text fields, dense vector fields, and sparse vector fields in one schema, and one index holds all of them.
You keep:
The same Pinecone APIs and SDKs
The same index lifecycle
The same usage-based capacity model, metered in storage, read units, and write units
The same serverless architecture, with no nodes for your team to maintain
The same deployment options, including Dedicated Read Nodes and Bring Your Own Cloud
You add:
BM25 keyword ranking across multiple text fields per index
Lucene query syntax, including boolean operators and phrase queries
Text-match filters that restrict any search, including a semantic one, to documents matching the filter
Fuzzy matching with the ~ operator for typo tolerance
Tokenization and stemming in 18 languages, plus language-agnostic n-gram tokenization for substring- and prefix-matching
Search that finds what you mean and exactly what you say
An agent that retrieves a lookalike record fails quietly. It ships the wrong part or cites the wrong clause, and the error shows up later as a support ticket or a lost customer. Putting a node-based lexical engine behind those queries trades the risk for a cluster your team owns.
Full-text search, now generally available, closes both gaps inside the vector database you already run. The queries that embeddings get wrong now return the right records, and semantic search keeps handling everything else. One index and one schema sit behind both, with no cluster to tune and maintain.
Create an index
and start using full-text search today, or
contact us
if you have questions about full-text search or want help sizing an instance.
Learn more about full-text search
Read the docs.
The
full-text search guide
covers schemas, analyzers, query syntax, current limits, and more.
Run an example.
Searching for Birds with Pinecone Full-Text Search
walks through schemas, filters, and query syntax, and the Bird Search demo combines full-text search with multimodal vector search over a Wikipedia bird dataset.
Go deeper.
Full Text Search: Architecture and Design
covers how it's built, for anyone who wants the mechanism behind the API.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
