---
title: "When vectors became an implementation detail"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/when-vectors-became-an-implementation-detail/"
scraped: "2026-10-23T06:00:38.103494+00:00"
lastmod: "2026-10-22T16:52:18Z"
type: "sitemap"
---

# When vectors became an implementation detail

**Source**: [https://www.pinecone.io/blog/when-vectors-became-an-implementation-detail/](https://www.pinecone.io/blog/when-vectors-became-an-implementation-detail/)

←
Blog
When vectors became an implementation detail
How integrated embedding meets full-text search in the Documents API
Silas Smith
Oct 22, 2026
Engineering
Share:
Jump to section:
Bring your own vectors (circa 2021)
Laying the groundwork (2024–2025)
The Records API: proving the pattern (2024)
Full-text search changes the shape (2025–2026)
Integrated embedding as a schema field (2026)
Two kinds of search
How it works
Where this is going: a retrieval pipeline in a single API call
Where to start
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Nobody searches for a vector. People describe what they're looking for and expect to find it. Yet for most of Pinecone's history, you had to turn both your data and every search into vectors yourself, with your own embedding pipeline, before you could search. We first moved embedding inside Pinecone with the Records API in 2024, and now
we’ve added it to the Documents API
alongside full-text search. You just send Pinecone text, and it runs the embedding pipeline for you on every write and every search. This is the story of how we built it.
The Documents API: native vectors, full-text search, and now integrated embedding, with more on the way.
When I joined Pinecone in early 2024, what stood out was how much work our users had to do outside of Pinecone before they could use us. Good search depends on preparing your data ahead of time and orchestrating the queries your application receives. Over the last 2.5 years I’ve kept coming back to the same problem: how to get Pinecone to take on more of that work, so our users can spend more time building their application and less time building retrieval pipelines.
Vectors are a big part of that preparation, and they always seemed to me like an implementation detail. They're essential to how the database finds what you're looking for, but not something you should have to build yourself.
At its heart, this is an API story, so it makes sense to start at the beginning. For us, that’s the Vectors API.
Bring your own vectors (circa 2021)
Pinecone started as a pure vector database, and while we may now call the original API the Vectors API, we used to just call it “the API”. Not surprisingly, it speaks in terms of vectors: it either takes in vectors and stores them, or takes a query vector to search the vector space with. That means wiring a third-party embedding provider into your data pipeline, with all of the usual extra work that comes with it: authentication and key rotation, rate limits and retry with backoff, billing, and monitoring. Most applications are also split in two parts, with one path for loading data and another for queries, so you end up having to build the integration twice, including balancing the need for low-latency queries with high-throughput data loading.
The Vectors API also asks you to conform your data to its request shape: an ID, a vector, and some metadata in a prescribed format. And you're faced with a decision about where to keep the source text behind each vector: either you need to keep it in a separate data store, or you put it in a metadata field in Pinecone, a tradeoff between complexity in your application and cost and performance in your index.
A separate data store means that every search result requires a reverse lookup to find its corresponding text. Putting the text in a metadata field is simpler, but metadata is meant for small values you filter on, like categories. Pinecone indexes it into
roaring bitmaps
, so every block of text you store there adds to your storage and write costs and uses up part of the metadata limit per record. And it doesn’t make the words in it any more searchable.
With the Vectors API, you’re responsible for the embedding integration and often have to build it twice (once for writes and again for queries) and need to decide where to store the related text, with trade-offs involved.
Laying the groundwork (2024–2025)
It quickly became clear that every one of our users was building the same embedding pipeline (often twice). But before we could take on any of that work, two fundamental components had to be in place.
The first was an inference stack.
We started hosting models
ourselves in 2024, adding standalone embed and rerank endpoints. This meant you could use one API key and one provider and begin to simplify some parts of your application. You still had to call the model yourself before every write and every search, but because the models now ran next to the database and under the same API key, that opened the door to combining them directly with the database workloads they supported.
The second was a more flexible storage architecture for the database itself. In early 2025 we shipped the slab architecture:
a new log-structured architecture for serverless indexes
*. With slab, writes land in an in-memory buffer and flush to immutable sets of files we call “slabs”, and background compaction automatically merges small slabs into larger ones when warranted. Each slab is self-describing: it carries its own data, its own index, and a record of what kind of index it holds. Importantly, that made index selection composable for different kinds of indexes beyond just vectors, and full-text search would later become one of them.
🤯 Side note: We invested a lot of time in 2025 in rolling out the slab architecture to our entire customer base, so that we could migrate live indexes from our older clustering architecture to the new slab architecture. Not only could customers keep reading, but they could also keep writing throughout the migration process.
Akin to not just building an airplane while flying, but also transferring the passengers from the old plane to the new one in mid-air!
To learn more about our architecture, see
how Pinecone works
and our
guide to the slab architecture
.
The Records API: proving the pattern (2024)
While we were rebuilding the database architecture, we took our first crack at integrated embedding via the Records API, which
launched in late 2024
. We
wrote about it shortly after
, including how we sped it up by separating latency-sensitive query embedding traffic from slower batch upsert workloads.
With the Records API, you specify a model when creating an index, and then upsert text records and search with text. Pinecone embeds the text on the way in and the query on the way out, using the model configured on the index. This proved the basic request pattern that we wanted. Users just bring text, the embedding happens inside Pinecone, and users never have to see a vector.
👉 Fun fact: we expected the Records API to grow into a “documents” API, so we actually named the new Kubernetes service behind it ‘docs-api’.
But ultimately the Records API was premature: it wasn't a shape we could keep building on. Under the hood, it wraps our Vectors API, and the text still lives in a metadata field, with the same tradeoff costs as before. Each index was tied to one model and one text field, and didn’t give you the option to avoid storing the text. Because it was built directly on the Vectors API, the Records API had no room to evolve to support other kinds of search, like native full-text.
Full-text search changes the shape (2025–2026)
We’d known for a long time that we needed full-text search alongside vector search. It wins on exact string matching, like product codes and error messages, and combining the two is powerful. But full-text search needs the text itself tokenized and indexed by a native text search engine. With the slab architecture we had theoretically made room for a new kind of index, but it was unproven. Our APIs at the time also had no place for it. Making full-text search a reality would mean addressing both.
So in late November 2025 we brought the engineering team together in NYC, locked ourselves in a conference room, and didn’t emerge until we had a whiteboard nobody dared to erase and a clear picture of what we needed to build. It came down to three significant new pieces:
Native full-text search to be supported in our slab architecture
A flexible schema language to drive indexing configuration and query orchestration
A true document API and flexible search API we can continue to build on
We've written about
how full-text search works
,
the architecture behind it
, and
its general availability
. In short, document indexes support a user-defined schema of typed fields, which at the first release were: string fields for full-text search, dense and sparse vector fields for native vector search, and metadata for filtering. And the search API lets you choose how documents are scored: by keyword relevance on text fields, or by semantics on a vector field.
Besides improving retrieval quality in keyword-heavy use cases, full-text search fixes the text-as-metadata storage problem. Metadata indexing is built to filter on exact values, and raw text almost never benefits from exact value-matching. A full-text field is stored differently: Pinecone keeps the raw text once in the slab and builds a Tantivy inverted index next to it, which maps each term to the documents and positions where it appears. The index scores search results with BM25, and it also supports powerful
text-match filters
like $match_phrase, so any query, including a vector search, can require that a document contain a specific word or phrase.
The Documents API fronts an entirely new index mechanism built from the top down, driven by a document schema, with native full-text search and vector search side by side in the same slab architecture. It also inverts the request shape: the Vectors API asks you to conform your data to its shape, while the Documents API is designed to conform to yours. You write documents with your own field names, and the schema says how each field should be indexed.
The first release of document indexes and the Documents API focused on full-text search and native vectors. But integrated embedding was always part of the plan. The Documents API was designed up front to accommodate it and further evolution to support things like hybrid search, integrated reranking, multiple vector fields, and more.
Integrated embedding as a schema field (2026)
You can now configure both integrated embedding and full-text search on a string field:
pc.indexes.create(
    name="space-missions",
    schema={
        "fields": {
            "body": {
                "type": "string",
                "full_text_search": {"stemming": True, "stop_words": True},
                "embed": {"model": "llama-text-embed-v2"},
            }
        }
    }
)
Create a document index with one string field that has both full-text search and integrated embedding.
When you write a document, you send plain text. Pinecone embeds it with the field's model (specified by the schema), stores the vector next to the text, and indexes the text for full-text search—all in the same write. If embedding fails, nothing in the request is written. When you search, you send the query as text, and Pinecone embeds it with the same model. The goal is that loading data should feel less like building a data pipeline and more like configuring one.
With integrated embedding, one string field holds the text, its full-text index, and its vector. Both kinds of search can run against it.
Integrated embedding also makes search faster. When you embed the query yourself, every search takes two round trips: one to an embedding API and another to Pinecone with the vector. With integrated embedding it's one call. In our testing, a search with text in one call was about 3.5 times faster at the median than calling our standalone embedding API and then searching with the vector. Most of the difference comes from the extra network round trip that the single call avoids.
Here’s how the Documents API compares to the APIs that came before it:
Documents API
Vectors API
Records API
You write
JSON documents with your own fields
ID, vector, metadata
ID, text field and metadata, in JSONL format
Who embeds
Pinecone, per field in the schema
You, outside Pinecone
Pinecone, one model per index
Source text lives
In its own string field
Separate store or metadata
Metadata
Search by
Full-text, vector, or text (embedded)
Vector
Text (embedded)
Configured by
Schema
Dimension and metric
Model and text field
Two kinds of search
Here’s an example index with a handful of short descriptions of space missions in a single body field, with both search modes enabled. Each document also carries a year and whether the mission was crewed. The schema doesn’t declare those fields, so they’re stored as metadata you can filter on.
index = pc.index("space-missions")
index.documents.upsert(
    namespace="missions",
    documents=[
        {"_id": "voskhod-2", "body": "Voskhod 2, March 1965. A cosmonaut left the capsule through an inflatable airlock and floated outside for about 12 minutes, then had to let air out of his swollen suit to squeeze back in.", "year": 1965, "crewed": True},
        {"_id": "apollo-11", "body": "Apollo 11, July 1969. Neil Armstrong and Buzz Aldrin landed in the Sea of Tranquility while Michael Collins orbited above in the command module.", "year": 1969, "crewed": True},
        {"_id": "apollo-soyuz", "body": "Apollo-Soyuz, July 1975. An American Apollo spacecraft docked with a Soviet Soyuz in orbit, and the two crews shook hands through the hatch.", "year": 1975, "crewed": True},
        {"_id": "voyager-1", "body": "Voyager 1, launched September 1977. It flew past Jupiter and Saturn, and in 2012 became the first spacecraft to reach interstellar space.", "year": 1977, "crewed": False},
        {"_id": "sts-61", "body": "STS-61, December 1993. Astronauts on the shuttle Endeavour installed corrective optics in the Hubble Space Telescope to fix its flawed primary mirror.", "year": 1993, "crewed": True},
        ...
    ],
)
Upsert documents as plain text, with year and crewed stored as filterable metadata.
Some searches are for an exact string. Someone who types a mission code into a search box wants to find exact references to the mission, and full-text search matches the code itself.
results = index.documents.search(
    namespace="missions",
    score_by=[{"type": "text", "field": "body",
               "query": "STS-61"}],
    top_k=2,
    include_fields=["*"],
)


== search-text results:
[3.3801] sts-61
    STS-61, December 1993. Astronauts on the shuttle Endeavour installed
    corrective optics in the Hubble Space Telescope to fix its flawed primary
    mirror.
Search the body field for the exact mission code.
Other searches are questions, asked in the searcher's own words. The search API embeds the question with the same model that embedded the documents, and matches on meaning. Since the question is about a person, this search also filters on the crewed field, which leaves out uncrewed missions like Voyager 1.
results = index.documents.search(
    namespace="missions",
    score_by=[{"type": "embed", "field": "body",
               "query": "Who was the first person to float outside a spacecraft?"}],
    filter={"crewed": {"$eq": True}},
    top_k=2,
    include_fields=["*"],
)


== search-embed results:
[0.4294] voskhod-2
    Voskhod 2, March 1965. A cosmonaut left the capsule through an inflatable
    airlock and floated outside for about 12 minutes, then had to let air out of
    his swollen suit to squeeze back in.
[0.2319] apollo-soyuz
    Apollo-Soyuz, July 1975. An American Apollo spacecraft docked with a Soviet
    Soyuz in orbit, and the two crews shook hands through the hatch.
Search the same field by meaning, using only crewed missions.
Both searches run against the same field in the same index, and neither one requires the client application to handle a vector.
How it works
When a search arrives with an embed clause, the Documents API embeds the query by calling our embedding service, with the model the field declares. Our embedding client retries with backoff and spreads load across healthy endpoints, where “healthy” means both a low error rate and low latency (
learn more about our load balancing
). Query embeddings go to the embedding service as their own small requests and are isolated from the large batches used for writes, so a latency-sensitive search doesn't wait behind someone else's bulk upsert.
The query router reads the index’s manifest, which is usually cached, to find its slabs, then sends the search directly to the executors that hold them. Every executor keeps the index portion of its slabs on local NVMe SSD and in memory, and new slabs are warmed on the executors before being added to the manifest, so searches never get stuck waiting on a cold slab.
A search with integrated embedding: the Documents API embeds the query in the same region, then the executors score slabs that are already cached on local SSD and in memory.
Bottom line, your search starts executing as soon as the query embedding comes back, and your application makes one call instead of two. That's what's behind the 3.5x from earlier. In our testing, from a client in the same region as the index, an end-to-end search with text on an embedded field took 26 ms at the median and 39 ms at p90. Embedding first and then searching took 92 ms and 109 ms. Your numbers will depend on where your index and application run.
Writes follow a similar path in the other direction. The Documents API embeds each batch of documents, up to 96 at a time. The text and its vector go to the write-ahead log together on the same log sequence number (LSN), land in the memtable, and flush into slabs that hold the full-text index and the vector index side by side. A text clause and an embed clause therefore read the same slabs and have the same consistency guarantees.
Where this is going: a retrieval pipeline in a single API call
On just a handful of documents, either search mode tends to work fine. In a production use case your search application will likely receive both types of queries, so you’ll typically want to run both types of searches, but that's where it gets harder. Today a search scores by one method at a time, so using both means running two searches and merging the results yourself. The scores don't help with the merge: full-text scored ‘sts-61’ at 3.38 with BM25, and integrated embedding scored ‘voskhod-2’ at 0.43 with cosine similarity. The two scales aren't comparable, so you can't just sort the lists together. You end up needing to fuse them by rank, or sending the combined list to one of
Pinecone’s cross-encoder rerank models
.
This is the next piece we want to move inside Pinecone: one search that combines full-text and embedding clauses and fuses the results. Alongside it, we'll be adding a wider choice of popular embedding models. We’re also planning to add integrated reranking, import with integrated embedding, multimodal search, and support for data zone processing.
What's next for the Documents API: more embedding models and fusion are up next, with reranking, bulk import embedding, multimodal search, and data zone processing planned after that.
Where to start
If you're starting something new, start with the Documents API. It is where full-text search, native vectors, and integrated embedding live together, and it is the shape we'll continue to build on. The
integrated embedding guide
walks through creating an index, writing documents, and running your first search.
If you bring your own vectors today, a document index can still hold them as native vectors and can support full-text search on the same documents. If you’re using the Records API, a document index will be more efficient while still providing the same text-in, text-out pattern, along with full-text search. We’re also working to support migrations to a document index.
Preparing your data and orchestrating the query used to be your job. With full-text search and integrated embedding in the Documents API, we’ve taken a step towards making it our job. We're not done yet, and we’re hiring. If you want to help make vectors just one of many implementation details,
come build it with us
.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
Blog
Oct 22, 2026
Integrated embedding on the Documents API
Manish
,
Gavin
Blog
May 7, 2026
Full Text Search: Architecture and Design
Amir
,
Harry
,
Edo
Blog
Mar 12, 2025
Retrieval Inference for scale and performance
Silas
,
Adam
,
Rajat
,
Gareth
