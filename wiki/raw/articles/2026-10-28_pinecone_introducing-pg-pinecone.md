---
title: "Introducing pg_pinecone: Open-Source Search for Your Postgres Data"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/introducing-pg-pinecone/"
scraped: "2026-10-28T06:00:34.879600+00:00"
lastmod: "2026-10-27T13:17:13Z"
type: "sitemap"
---

# Introducing pg_pinecone: Open-Source Search for Your Postgres Data

**Source**: [https://www.pinecone.io/blog/introducing-pg-pinecone/](https://www.pinecone.io/blog/introducing-pg-pinecone/)

←
Blog
Introducing pg_pinecone: Open-Source Search for Your Postgres Data
Harshita Daddala
,
Anthony Mahanna
Oct 27, 2026
Product
Share:
Jump to section:
How pg_pinecone works
Benchmarks
More scale and more features, same SQL queries
Try it
Help us shape pg_pinecone
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
TL;DR
pg_pinecone is an open-source (Apache 2.0) Postgres extension for search on the data you already store, built on the search engine Pinecone runs at scale. Filters apply during search, which keeps narrow queries returning a full set of results, all inside your Postgres database.
AI that knows your business starts with your own data, and for many teams that data lives in Postgres. A support assistant, product recommendations engine or an agent that remembers past work, each depends on finding the most relevant records fast and accurately. That gets harder as the data size grows. The common way to run vector search in Postgres today is a graph index like HNSW and graphs get expensive to scale. They need increasing amount of memory to maintain performance and take a long time to build. Filtered search also degrades accuracy; when a query is scoped to one user or one tenant, a graph index can return fewer results leading the application to miss the answers it should have found.
Today we’re releasing pg_pinecone, an open-source Postgres extension under Apache 2.0, built on the search engine Pinecone runs at scale. It indexes the vector columns you already have. Rather than a graph, its index stores a compact summary of each vector, so search stays fast on a small memory footprint and indexes build quickly. It applies the filter during search, not after, so a narrow scope still returns a full set of results. It runs inside your Postgres database, so the data never leaves Postgres. The result is fast, accurate, filtered search on data you already store, with no second system to run.
How pg_pinecone works
pg_pinecone is a Postgres extension that works with the vector columns you already have in pgvector. Your application connects to Postgres the same way and sends the same SQL, such as
ORDER BY embedding <=> $1 LIMIT 10
. Your tables, including the full vectors, stay where they are, and Postgres remains the system of record.
Each table uses one of three engines:
native
(the default): pg_pinecone’s own engine, which builds and searches its index entirely inside your Postgres database, with no Pinecone account, API key, or network calls
pgvector
: searches pgvector’s HNSW index, the one you may already run
remote
: sends search to an index in Pinecone’s managed service
Switching between them takes one call to
pinecone.set_engine()
, and your queries don’t change.
Like pgvector’s HNSW, pg_pinecone’s native engine uses an ANN (approximate nearest neighbor) algorithm. Its index stores compressed vector codes (using RaBitQ) in clusters instead of a graph, and the engine filters during the search instead of after it. Together, these keep the index small, search fast, and filtered results accurate.
A smaller index
pgvector’s HNSW index stores a full copy of every vector plus links to its nearest neighbors. A search walks that graph and compares full vectors at each hop, so the whole graph needs to stay in memory to be fast.
Instead of a graph index (which performs well at static unfiltered high QPS workloads), the native engine groups similar vectors into clusters using an
inverted file index (IVF)
. The index stores a quantized copy of each vector as a RaBitQ code (
Gao and Long, SIGMOD 2024
): about one bit per dimension, plus a few correction values. The codes for each cluster are packed together, so a search reads a few contiguous pages instead of hopping across a graph. To see how RaBitQ compares with other quantization methods, try
VQ-Bench
or read
how we built it
.
For 1 million 768-dimension vectors, the native engine builds a 136 MB index, compared with 2.0 GB for HNSW on halfvec and 4.1 GB on full-size vectors.
Faster search
Most of the work in a search is cheap. Comparing the query vector with a RaBitQ code takes a few bit operations instead of full floating-point math, and only a shortlist of candidates is scored with full vectors:
Probe the nearest clusters
by comparing the query vector with each cluster’s centroid.
Compute an estimated distance
for each row from its RaBitQ code, and keep the best candidates.
Rerank the candidates
using their full vectors from your table.
At 0.95 recall, a query takes 1.3 ms, compared with 1.7 ms for HNSW on halfvec and 2.7 ms on full-size vectors. At 0.99 recall, it’s 2.3 ms vs. 4.7 ms and 6.7 ms.
Accurate filtered results
pgvector’s HNSW post-filters: it finds the nearest neighbors first, then applies the
WHERE
clause. With a narrow filter, like one tenant out of a hundred, most candidates are discarded, and a query can return fewer rows than its
LIMIT
. pgvector’s iterative scans fill the list by searching further, at a cost in time, and in accuracy if
relaxed_order
is used.
The native engine filters during the search, and picks its strategy based on selectivity. It stores the value of one filter column next to each row’s RaBitQ code and, at build time, counts how many rows carry each value:
Narrow filter
(3% of rows or fewer, by default):
pre-filtering.
It scans every matching row across all clusters and scores each one with its full vector, so results are exact.
Wide filter
(more than 3% of rows):
single-stage filtering.
It searches more of the nearest clusters than an unfiltered search (up to half), and checks the filter inside each cluster before scoring.
With 10% of rows matching, the native engine uses single-stage filtering and reaches 1.000 recall in 12.3 ms. HNSW with iterative scans reaches 0.920 recall at best, in 5.9 ms.
Keeping the index current
When you insert new rows, each vector joins the nearest cluster and is searchable immediately. Centroids stay where the build placed them, so after large changes, like a bulk load that doubles the table or new data unlike what the index was built on, run
REINDEX
or enable automatic maintenance to rebalance the clusters.
Benchmarks
We compared
pg_pinecone
's native engine with
pgvector
's HNSW index, using both full-size vectors and halfvec, on the same data: 1M vectors with 768 dimensions (wiki_dpr). Each table is from an AWS
r6id.4xlarge
(16 vCPUs, 128 GB RAM). Unfiltered latency, build time, and index size are one session (PostgreSQL 17); filtered search is another (PostgreSQL 18); the 4 GB memory cap is a third. Latency is median (p50) at k=10 with one client unless noted. The full setup and the commands to rerun the tests can be found in
the benchmark harness README
. Here's where pg_pinecone's native engine stands out.
Faster unfiltered search
At k=10 with one client, unfiltered search is faster than HNSW at the same recall.
Table 1: Unfiltered search latency at the same recall (1M vectors, 768 dimensions)
More accurate filtered search, and faster when the filter is narrow
Most real searches filter by tenant, user or category. When the filter is narrow, HNSW returns fewer of the true closest matches.
pg_pinecone
filters during the search, so it finds them.
Performance when the filter keeps 1% or 10% of rows and a query’s closest matches mostly fall outside it, the hard case for post-filtering:
Table 2: Filtered search recall and latency (1% and 10% of rows matching)
Faster to index
pg_pinecone builds its index faster than pgvector HNSW on the same data, so you can index a large table and start searching sooner.
Table 3: Index build time (1M vectors, 768 dimensions)
An index that fits in memory
pgvector's HNSW index stores every vector plus links between neighbors, so it grows fast and competes with the rest of your database for memory. pg_pinecone native stores a compact summary of each vector instead, so the index is much smaller and stays in memory as your data grows. In our tests:
Table 4 (two benchmarks):
Index size
and
search with memory capped at 4 GB
More scale and more features, same SQL queries
The native engine covers search for many apps, and you can stay on it as long as it works for you. With a Pinecone API key, the same extension gives you a few more tools. Each one is optional, and you can add them one at a time. Here's what each one adds and when it's worth turning on.
Scale beyond one server.
As your data grows, a larger index uses more memory and competes with the rest of your database. When that happens, the remote engine moves search to Pinecone with one SQL command:
SELECT pinecone.set_engine('docs', 'remote');
Your embeddings sync to a Pinecone index in the background, and searches keep running in Postgres until the copy finishes. Your SQL queries don't change, Postgres stays your source of truth, and you can switch back to the native engine the same way.
Turn text into embeddings in SQL.
If your table has text but no embeddings yet,
embed()
calls Pinecone's inference service. You don't need to host a model or manage another provider's key, and Pinecone's free tier covers a first build. Use it when you're starting from text and want to get to search quickly. It works with both the native and remote engines. It does not change where search runs: only the embed call needs Pinecone.
UPDATE docs SET embedding = pinecone.embed(content, input_type => 'passage')::vector;
Search by keyword and by meaning.
Without switching the vector engine, you can also use Pinecone's full-text search (BM25) on the same table, alongside vector search. Use it when people search with exact terms, like product names or error codes, as well as by meaning.
SELECT pinecone.track_docs('docs', text_columns => '["content"]');
SELECT id, score FROM pinecone.search_docs('docs', 'error 42P01', k => 10);
Put the best results first with rerank().
rerank()
reorders your top results with Pinecone's reranking models, so the most relevant ones come first. It helps when only the top few results matter, as in RAG, or when you merge keyword and vector results into one list.
SELECT * FROM pinecone.rerank(
  'which database stores vectors?',
  ARRAY(
    SELECT content FROM docs
    ORDER BY embedding <=> $1
    LIMIT 20
  )
);
Our mission is to make AI knowledgeable, everywhere. Pinecone runs in our cloud, in yours with
BYOC
, and now inside your Postgres database with pg_pinecone.
Try it
Ready to give it a try?
Install
pg_pinecone from a pre-built release on GitHub
or with the
pineconeteam/pg_pinecone
image on Docker Hub
.
Use an existing vector column or create a new one. You can even fill the column with
embed()
and a free Pinecone API key.
CREATE TABLE docs (
    id        bigint PRIMARY KEY,
    tenant_id bigint,
    body      text,
    embedding vector(768)
);
Index your vector column:
CREATE EXTENSION pg_pinecone;
SELECT pinecone.create_index('docs', 'embedding', filter_column => 'tenant_id');
Query the way you already do, filter by tenant_id and order by embedding:
SELECT id, body
FROM docs
WHERE tenant_id = $1
ORDER BY embedding <=> $2
LIMIT 10;
Full setup steps are in the
README
.
Help us shape pg_pinecone
This is our first release, and we want your input on where it goes next.
Pinecone maintains pg_pinecone and reviews every pull request. We'll build the public roadmap from your feedback shared on
GitHub
, in
Discord
, and at
our monthly office hours
.
Get involved
Open a
feature request on GitHub
or
upvote one
that's already there
Share your benchmark results, setups, and what you built in the pg_pinecone channel on
Discord
Ask questions in the pg_pinecone channel on
Discord
Run into an issue? Submit a
bug
on GitHub
pg_pinecone is ready for your data today. Install it, index a Postgres table you already have, and show us what you build!
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
