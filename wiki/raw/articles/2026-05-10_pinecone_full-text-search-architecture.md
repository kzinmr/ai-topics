---
title: "Full Text Search: Architecture and Design"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/full-text-search-architecture/"
scraped: "2026-05-10T01:27:40.827005+00:00"
lastmod: "2026-05-07T18:58:00Z"
type: "sitemap"
---

# Full Text Search: Architecture and Design

**Source**: [https://www.pinecone.io/blog/full-text-search-architecture/](https://www.pinecone.io/blog/full-text-search-architecture/)

←
Blog
Full Text Search: Architecture and Design
Amir Ingber
,
Harry Scholes
,
Edo Liberty
May 7, 2026
Engineering
Share:
Jump to section:
Try Full Text Search
References
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Pinecone now supports full text search with a broad set of features: full Lucene-syntax queries, multi-field schemas, BM25 scoring, tokenization in 18 languages, stemming and stop-word removal, phrase matching search, new filters based on text match for vector search, and more.
# Query: keyword search across title/body using Lucene query syntax (BM25 ranking)
index = pc.preview.index(name="transcripts")

response = index.documents.search(
    namespace="animal-kingdom",
    score_by=[
        {
            "type": "query_string",
            "query": 'body:("nice marmot")'
        }
    ],
    top_k=10,
    include_fields=["title"],
)
Why this matters: agents
Agents need to complete tasks, write code, and answer questions. To retrieve the exact data needed, they have to combine different kinds of filters and scoring. Text is a big part of that.
For example, an agent might search through customer support transcriptions for new insights. It looks for user interactions that indicate frustration with wait times — but it has already flagged interactions that contain the words "wait" or "waiting" and wants to exclude those. And, it needs to consider only a specific geographic and time period. Coding agents are great at composing complex queries like this. What they need is an engine that can execute them — one that internally links semantic (vector), text, and metadata filtering in a single API. See below for a detailed API example.
How this enhances Pinecone's search capabilities
Since 2023, Pinecone has supported text search via optimized sparse indexes. Under the hood, sparse indexes encode documents as a list of token IDs and weights — IDs typically come from a tokenizer, weights from a heuristic like BM25. We exposed this as a general mechanism so developers could plug in non-standard tokenizers, train their own lexical models, or use
Pinecone's sparse models
instead of naive token weight heuristics.
So, sparse indexes let you do more. But they also
require
you to do more!
Users (and agents) had to deal with tokenization, weighting, maintaining word counts, and ranking heuristics themselves. They needed something that feels more like a search text box and less like a data science project. Full text search is that.
Under the hood: Tantivy
We integrated the
Tantivy
library for advanced text functionality alongside vectors and metadata. We considered building it in-house and decided against it, for four reasons — ordered by what we think matters most to a developer using this:
Familiar Lucene syntax.
Most search experts already know it, and
agents know it too
. When we ask a coding agent to add a text search clause to a Pinecone query, it usually gets it right on the first try.
18 languages out of the box.
Mature, community-maintained tokenization and stemming for the languages listed below. Getting this right from scratch is hard and never finishes.
Tuned for RAG-shaped queries.
Our testing showed Tantivy performs well on long queries and large
values — the regimes that dominate RAG and agent workloads, and the regimes Lucene is least optimized for.
Rust and slabs.
Tantivy is a Rust library (so are we), and Tantivy segments map cleanly onto Pinecone slabs.
Advanced text search features
Query syntax
Pinecone supports
Lucene query syntax
via Tantivy's query parser. The most common operators are below; see the
docs
for the full list.
Feature
Syntax
Included docs
Scoring
Single term
fox
Docs containing the term
BM25 for the term
Phrase
"quick brown"
Docs containing the exact adjacent phrase
BM25 over the phrase as a single term
Boolean AND
quick AND dog
Docs matching every clause
Sum of clause BM25 scores
Boolean OR
fox OR dog
Docs matching at least one clause
Sum of BM25 scores from clauses that matched
Boolean NOT
science NOT algorithms
Docs matching the positive clause and not the negated one
BM25 for the positive clause; the negated clause contributes nothing
Phrase slop
"quick fox"~2
Docs where the terms appear within ~N positions of each other
BM25 over the phrase; every in-window occurrence counts equally toward TF
Term boost
fox^3
Same as the unboosted clause
Clause BM25 multiplied by the boost factor
Field scoping is written into the query itself:
or
. For the full request and response reference, including other ranker types and more query syntax details, see the
public preview docs
. All control- and data-plane calls require the header
while document search is in public preview.
Text match: new filter operations
Pinecone's metadata filter language is already rich —
/
,
/
/
/
,
/
,
, and the boolean combinators
/
/
— and the engine evaluates it efficiently alongside vector search. Full text search adds three new filter operators that work against any text-searchable field:
,
, and
. Each one tokenizes the operand the same way the field is tokenized at index time, then includes or excludes a record based on whether the field matches.
# Each text predicate is a filter clause: it returns true (keep the record)
# or false (drop it). Score comes from score_by, never from the filter.
filter = {"body": {"$match_phrase": "machine learning"}}    # exact adjacent phrase
filter = {"body": {"$match_all":    "machine learning"}}    # all terms, any order
filter = {"body": {"$match_any":    "ml ai neural"}}        # any term
These compose with the existing metadata operators via
,
, and
, so a single
block can mix text-match and metadata predicates. The next section pairs that with vector ranking.
Combining vector ranking with a text-match filter
A document either passes the filter or it doesn't; if it passes, its score comes entirely from
. The same
block works with every ranker —
,
,
(BM25 on a single field), or
(multi-field BM25 with Lucene query syntax).
Returning to the agent example from the intro — "find new frustration signals about wait times, but exclude records that already mention
or
, restrict to EU customers, and only look at recent records" — that becomes a single search:
Public preview is BYO-vector for hybrid: you compute the embedding (or sparse vector) yourself, then pass it in
alongside any text-match filters. There is no
/ integrated-inference field on document-shaped indexes today.
from pinecone import Pinecone
pc = Pinecone(api_key="YOUR_API_KEY")
# Index schema (set when the index was created):
#   from pinecone.preview import SchemaBuilder
#   schema = (
#       SchemaBuilder()
#       .add_dense_vector_field("embedding", dimension=1536, metric="cosine")
#       .add_string_field("body", full_text_search={"language": "en"})
#       .add_string_field("geo", filterable=True)
#       .add_float_field("timestamp", filterable=True)  # epoch seconds
#       .build()
#   )

# 1. Embed the natural-language search intent.
query_embedding = compute_embedding("your wait times are too long")

# 2. Run a single search: the dense vector ranks the surviving documents.
index = pc.preview.index(name="support-conversations")

response = index.documents.search(
    namespace="__default__",
    filter={
        "$and": [
            {"$not": {"body": {"$match_any": "wait waiting"}}},
            {"geo": {"$eq":  "EU"}},
            {"timestamp": {"$gte": 1767225600}}  # 2026-01-01T00:00:00Z
        ]
    },
    
    score_by=[{
        "type": "dense_vector",
        "field": "embedding",
        "values": query_embedding,
    }],
    
    top_k=10,
    include_fields=["body", "geo", "timestamp"],
)
tokenizes its operand the same way the indexed field was tokenized, so the "
" filter will match any document containing any of these tokens in the
field.
Tokenizer pipeline
Stemming and stop-word filtering are opt-in per text field — both off by default. Configure them on the field's
block at index creation (for example,
). When omitted, server defaults apply and the field is tokenized and lowercased only.
Stemming is available for 18 languages: Arabic, Danish, German, Greek, English, Spanish, Finnish, French, Hungarian, Italian, Dutch, Norwegian, Portuguese, Romanian, Russian, Swedish, Tamil, and Turkish.
Stop-word filtering is available for English, Danish, German, Finnish, French, Hungarian, Italian, Dutch, Norwegian, Portuguese, Russian, and Swedish. There is no stop word support for Arabic, Greek, Romanian, Tamil, and Turkish
The analysis chain applied to each field at index and query time, when both filters are enabled, is:
SimpleTokenizer
→
RemoveLongFilter(max_term_len)
→
LowerCaser
→
StopWordFilter
(when
stop_words
is enabled)
→
Stemmer
(when
stemming
is enabled)
BM25 scoring
Pinecone uses the common
BM25
algorithm for text ranking. For each (query, document) pair, the score is computed from the term frequencies (TF) and inverse document frequencies (IDF) of the terms common to both. TFs are simple counts of the terms in the document. The canonical IDF is global to the searched corpus, given by
where
is the total number of documents and
is the number of documents containing term
.
Ideally, we want to store these document-level statistics so that when we answer queries we simply retrieve the IDF values. We describe below how we make this work with a growing and dynamic dataset in our slab-based architecture.
Design choices
Document ordering
Document order matters a lot in text search. It controls how posting lists compress, how queries traverse the index, and which optimizations are possible. Common choices include time of insertion, cluster or topic, and authority or popularity — each optimizing for a different goal: insertion throughput, index size, or query latency.
Slabs are built offline from immutable batches, so we are free to pick any order. There is no streaming-insertion constraint to preserve, so the reordering costs are low at write time.
When both vectors and text exist per record, we take advantage of the geometric location of vectors in space to inform the ordering of text records. Vectors are grouped by IVF clusters for fast vector search, so nearby vectors belong to semantically similar records. Vector search, metadata filtering, and text search then share the same ordering — scores and predicates from one stage feed the next without translation.
This ordering also compresses posting lists well. When similar documents land on nearby IDs, the gaps between consecutive document IDs in each posting list shrink, and delta-encoded lists become smaller. The effect is well established in the information retrieval literature [
1
,
2
,
3
,
4
]. Our IVF-based ordering is a cheap approximation of the clustering those papers recommend: we get the compression benefit as a side effect of the ordering we already need for vector search.
BM25 statistics for growing and dynamic data
Exact BM25 needs global term statistics across the whole index. The dataset is growing and changing, though, and Pinecone's
slab-based architecture
serves queries by partitioning data across slabs and merging slab-level results at query time. To score consistently across slabs, we merge slab-level term statistics for the terms in the query into a single statistics object, then pass that object to every slab as it scores. The merge is fast because it only touches statistics for the query terms.
When all slabs of an index reside on a single query executor, the merged statistics cover the entire index — scores match the canonical global-BM25 ranking. For indexes whose slabs span multiple executors, we avoid the costly scatter-gather across machines and merge statistics only at the executor level. The resulting scores are approximate relative to a single global corpus, but BM25 is logarithmic in term frequencies, so the perturbation barely moves rankings. The tradeoff between local and global statistics in distributed retrieval has been studied since the mid-1990s [
5
], and per-shard statistics are standard practice in production search engines [
6
]. Meaningful distortions only show up on very small samples.
Example benchmarks
Dataset.
Wikipedia (English, 20231101 dump), every article reduced to a two-field record of
title
(avg ~3 words) and
body
(avg ~470 words). We ran the same query suite against five corpus sizes — 1k, 10k, 100k, 1M, and the full 6.4M articles.
Queries.
BM25 set:
5,000 Lucene-syntax queries spanning 20 categories — single terms, phrases, slop, term boosts, cross-field AND/OR, complex booleans combining 4–8 clauses. Generated to mirror the long, multi-clause queries that RAG and agent workloads produce.
Filtered set:
500 BM25 queries each paired with a text-match filter (
$match_phrase
/
$match_all
/
$match_any
over
title
and/or
body
, some combined with metadata predicates). Filter selectivity ranges from ~1 doc to ~60% of the corpus, exercising both the highly-selective and the broadly-permissive ends of the curve.
Setup.
A single Pinecone index per corpus size, b1 dedicated node type, 1 shard / 1 replica. Latency is measured client side. Client and index are in the same region (AWS us-east-1). Top-k = 100. Queries are sent sequentially, one at a time. Latency reflects end-to-end per-query latency, not batching throughput.
Size
BM25 p50 (ms)
BM25 p99
Filter p50 (ms)
Filter p99
1k
6.0
9.6
6.1
9.6
10k
6.0
9.7
6.2
52.3
100k
6.6
12.2
6.6
50.3
1M
9.1
28.3
9.4
60.0
6.4M
22.7
84.0
15.8
136.0
As a benchmark methodology — not a public-API guarantee — we measure accuracy against an external brute-force baseline that scores every (query, doc) pair with the canonical (single-machine, global) BM25 formula and ranks them exactly. Recall is the standard
at top-k = 100.
Across our benchmark corpora, both plain BM25 and BM25-with-text-match-filter queries deliver mean recall well above 95% on indexes from 1k up to millions of documents. The small gap is concentrated in queries where many documents share an identical BM25 score at the top-k boundary. In such cases, the identity of the documents ending in the top-k depends on the scan order between slabs that can be arbitrary, and potentially different than the brute-force scan order.
Try Full Text Search
Document search is in public preview. The Python SDK exposes it under
, and every request must include the header
.
pip install --upgrade pinecone
from pinecone import Pinecone
from pinecone.preview import SchemaBuilder

pc = Pinecone(api_key="YOUR_API_KEY")

# 1. Define the index schema: two FTS string fields.
schema = (
    SchemaBuilder()
    .add_string_field("title", full_text_search={"language": "en"})
    .add_string_field("body",  full_text_search={"language": "en"})
    .build()
)

# 2. Create a serverless preview index. Wait for status.ready before continuing.
pc.preview.indexes.create(
    name="quickstart",
    schema=schema,
    read_capacity={"mode": "OnDemand"},
)

# 3. Upsert documents to the default namespace.
index = pc.preview.index(name="quickstart")
index.documents.batch_upsert(
    namespace="__default__",
    documents=[
        {"_id": "1", "title": "The Big Lebowski", "body": "nice marmot"},
        {"_id": "2", "title": "Fargo",            "body": "wood chipper"},
    ],
)

# 4. Search across both fields with Lucene query syntax.
response = index.documents.search(
    namespace="__default__",
    top_k=10,
    score_by=[{"type": "query_string", "query": 'body:("nice marmot")'}],
    include_fields=["title"],
)
For the full reference, see the
docs
.
References
Blandford and Blelloch,
Index Compression through Document Reordering
, DCC 2002.
Silvestri,
Sorting Out the Document Identifier Assignment Problem
, ECIR 2007.
Yan, Ding, and Suel,
Inverted Index Compression and Query Processing with Optimized Document Ordering
, WWW 2009.
Dhulipala et al.,
Compressing Graphs and Indexes with Recursive Graph Bisection
, KDD 2016.
Viles and French,
Dissemination of Collection Wide Information in a Distributed Information Retrieval System
, SIGIR 1995.
Elastic,
Practical BM25 — Part 1: How Shards Affect Relevance Scoring in Elasticsearch
.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
