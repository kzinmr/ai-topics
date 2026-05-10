---
title: "Full Text Search in Pinecone, Now in Public Preview"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/full-text-search/"
scraped: "2026-05-10T01:27:40.189744+00:00"
lastmod: "2026-05-07T12:11:22Z"
type: "sitemap"
---

# Full Text Search in Pinecone, Now in Public Preview

**Source**: [https://www.pinecone.io/blog/full-text-search/](https://www.pinecone.io/blog/full-text-search/)

←
Blog
Full Text Search in Pinecone, Now in Public Preview
Lea Wang-Tomic
,
Harry Scholes
May 7, 2026
Product
Share:
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
For the technical deep dive into how FTS is built, see
Full Text Search: Architecture and Design
When semantic search hit production scale, the default move for retrieval was to embed text and search by meaning. As such, the surface area of what a query could match expanded: the same corpus, searched semantically, contained more retrievable signal than it had before.
But expanded coverage cuts both ways. The same property that lets a vague query find a relevant document also makes it harder to pin down an exact one. Precision for searching on specifics (i.e. a product SKU, a legal citation, a person's name, an error code) doesn't live in embedding space. So as retrieval systems matured, keyword matching came back into purview, not as a replacement for semantic search but as the natural complement.
Full text search is now available in Pinecone, in Public Preview.
BM25 scoring across multiple text fields per index, Lucene query syntax, and multi-language tokenization are all built in.
One index, text and vectors together
A single index now holds text fields, dense vectors, sparse vectors, and filterable metadata, defined together in a schema set at index creation. Each text field takes a language setting that controls tokenization, stemming, and optional stop word removal. Stemming reduces words to their root form, so "running" and "runs" all match a query for "run." Eighteen languages are supported.
Multiple text fields can be configured per index, which removes the modeling workaround of routing every searchable string through a single field. Title, body, and tags can each be independent text fields, scored or filtered on their own terms.
Keyword search and vector search run in the same query against that schema. There is no separate keyword index to maintain, no results from two systems to reconcile.
# Query: keyword search across title/body using Lucene query syntax (BM25 ranking)
index = pc.preview.index(name="articles-multi")

response = index.documents.search(
    namespace="errors",
    score_by=[
        {
            "type": "query_string",
            "query": 'title:("error code 4092") OR body:("error code 4092")'
        }
    ],
    top_k=10,
    include_fields=["title", "body", "category"],
)
Text match: text fields as filters
Text match filters narrow the candidate set by keyword logic before vector ranking runs. Three modes are supported: exact phrase, all tokens present, any token present. The vector search then operates only over documents that already satisfy the keyword condition.
Consider a legal document retrieval system. A lawyer searching for precedents needs two things: the document must contain a specific clause or citation verbatim, and among those, the most semantically relevant to their argument should rank highest. A text match filter handles the first condition, dense ranking handles the second, in a single query.
This composes with metadata filters too. A single query can require an exact phrase in a text field, filter on a date range, and rank by vector similarity.
# Filter by exact phrase first, then rank remaining docs by dense similarity
index = pc.preview.index(name="articles-multi")
query_vector = [...]  # 1536-dim query embedding

response = index.documents.search(
    namespace="default",
    filter={
        "$and": [
            {"body": {"$match_phrase": "force majeure clause"}},
            {"category": {"$eq": "legal"}}
        ]
    },
    score_by=[
        {
            "type": "dense_vector",
            "field": "embedding",
            "values": query_vector,
        }
    ],
    top_k=5,
    include_fields=["title", "body"],
)
What's supported in Public Preview
Upsert, fetch, and delete are supported for documents. Within a single query, scoring operates on one type at a time: BM25, dense, or sparse. For workloads that need to combine scores across modalities, the queries can be issued separately and merged client-side. Schema is fixed at index creation, which means existing indexes cannot be converted to use full text search until mutable schema lands.
Get started
Full text search is available now on under API version
. The
documentation
covers schema definition, query syntax, filter operators, and the Python SDK end to end. The
Google Colab notebook
has a runnable example using a Wikipedia dataset.
For a fuller walkthrough, this
Bird Search demo
combines full text search with multimodal vector search over ~2,079 North American bird Wikipedia articles, embedded with Gemini Embedding 2.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
