---
title: "Self-Hosted Vector Search: What You Run Before You Ship"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/self-hosted-vector-search/"
scraped: "2026-11-10T06:00:25.326144+00:00"
lastmod: "2026-11-06T22:20:03Z"
type: "sitemap"
---

# Self-Hosted Vector Search: What You Run Before You Ship

**Source**: [https://www.pinecone.io/blog/self-hosted-vector-search/](https://www.pinecone.io/blog/self-hosted-vector-search/)

←
Blog
Self-Hosted Vector Search: What You Run Before You Ship
Team Pinecone
Aug 20, 2026
Events
Share:
Jump to section:
The Parts Every Retrieval Stack Has
What You Run Before Writing Application Code
Why Index Tuning Doesn't Stay Done
Scaling Past One Node
Where That Work Goes in a Serverless Database
When Self-Hosting Is Still the Right Call
Getting to a First Query
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
A user asks an AI assistant, "What's my API rate limit?" It answers, "You have unlimited requests!" The product has a rate limit. The model doesn't know it, because a model knows the data it was trained on and nothing about your documentation, product catalog, customer history or internal knowledge base.
When a fact isn't in its context, it takes a best guess, and confident wrong answers like that one erode trust in the product. The fix is grounding: retrieve the right facts from your own data and hand them to the model.
On August 20, 2026, Gavin Johnson, Pinecone's Technical Product Marketing Manager, presented "Vector Search for Agentic AI: A Hands-On Introduction to Pinecone." The 30-minute session covered why AI applications need a vector database and what it takes to get one running, from a stack a team operates itself to a first query on Pinecone.
Every retrieval stack has the same parts, and the choice of stack decides how much of the work of running them lands on your team before any application code exists.
This post was adapted from Gavin Johnson's webinar
Vector Search for Agentic AI
. Here's the full replay:
Watch "
Youtube Video Player
" on YouTube
Watch
The Parts Every Retrieval Stack Has
Grounding needs a pipeline. Raw data goes in: docs, knowledge base articles and anything else the model should know. An embedding model turns each chunk into a vector. A vector database stores those vectors and searches them. A semantic query finds the closest matches, and the LLM answers from what comes back.
The embedding model is where text becomes something you can search by meaning. It reads a chunk of text (or an image, or audio, though most models today are text-to-vector) and returns one vector. For example, a model might return 1,024 floats in a single array, a point in a 1,024-dimension space.
Five stages: ingest, embed, store and search, query, respond.
A user who types
can't log in
gets the article titled
Password Reset Instructions
, though the two share no words. That match is semantic search, which works on meaning. Lexical search, or running grep over a docs folder, can't make it. A vector search can, so the LLM gets context grounded in your data where it would otherwise guess.
What You Run Before Writing Application Code
Say the team picks an open-source vector database, or builds its own vector store. Before the first feature ships, it owns this list:
Provision the database.
Pick one and run the infrastructure under it.
Find an embedding model.
Use one that someone else already serves, or run your own.
Tune the indexes.
Once data is going in and queries are coming back, expect manual tuning unless someone on the team already knows the product deeply.
Debug recall.
When the right answers don't come back, find out why. Maybe the chunking is off. Maybe the embedding model isn't a good one. There are plenty of other causes, and each one is yours to chase.
Scale past one node.
When the data outgrows a single machine, work out how to run two.
"This is all work that you have to do before you build an application." - Gavin Johnson
Every item on the list is infrastructure work, and all of it lands before anyone writes the feature the project exists for. On a small team without dedicated MLOps or infrastructure engineers, the people doing that work are the ones who would otherwise build the feature.
None of this makes building your own wrong. If the workload is small enough, it may make sense. But the list splits differently once a serverless database takes part of it. On Pinecone, we take these:
You run it yourself
Pinecone handles it
Choose and provision a database
Server provisioning
Run and manage embedding models
Embedding and reranking models through Pinecone Inference (optional)
Configure and tune indexing by hand
Index tuning
Handle scaling
Auto-scaling
Why Index Tuning Doesn't Stay Done
Most open-source vector databases use
HNSW
(Hierarchical Navigable Small World), a graph-based index.
Graph indexes
tend to be the fastest algorithms for in-memory vector search. HNSW also comes with a dial. Things get slower when you get more accurate, and things get less accurate when you get faster. Tuning means finding the point on that dial that gives your application the speed and recall it needs.
So once it's tuned, is it done? Not for long. Pinecone's
comparison with pgvector
, the vector extension for Postgres, lists where that work comes back after launch:
Memory.
pgvector builds its HNSW graph in memory, and to keep builds and queries fast, that graph needs to fit in the memory you have provisioned. No simple formula tells you how big it will be before you load the data.
Latency.
An application ships with acceptable latency, data accumulates, the index outgrows its memory, and query latency degrades sharply.
Filters.
Postgres searches the vector index first, then applies the WHERE clause to what comes back. With a selective filter, the query returns fewer results than you asked for. pgvector 0.8.0 added iterative scans that help, though they are opt-in and capped.
Drift.
pgvector's other index type, IVFFlat, draws its partitions from the data that existed at build time. Vectors added later land in partitions drawn without them, and getting recall back means rebuilding the index.
Contention.
Adding a vector to an HNSW graph means running approximate searches through its layers, so writes compete with queries for memory and CPU. On one Postgres instance, queries, ingest, index rebuilds and autovacuum all contend for the same machine.
HNSW itself performs very well on benchmarks. We don't use graph-based indexes such as HNSW in Pinecone serverless because, in a dynamic setting with constant writes and filtered queries, we found
other algorithms work better
.
Scaling Past One Node
The last item on the list is the one nobody can size in advance. Once the data outgrows one node, getting a second one up may be straightforward, or may be incredibly difficult, depending on the situation.
Why not plan for it on day one? On pgvector, the limit is the memory of one instance, and that memory has to hold an index whose size depends on data you haven't loaded yet. So the ceiling usually arrives after launch, when the choices are a bigger instance or sharding you build yourself.
Where That Work Goes in a Serverless Database
Pinecone is fully serverless. You create an index, and nobody re-indexes or tunes it afterward. Here's where most of that list goes.
Writes and reads.
Separating compute from storage is a familiar design. We go further and split compute into separate read and write paths, so writes never block reads. A new vector is searchable within seconds, without waiting for an index rebuild or an optimization to finish. You upsert, and it's good to go.
Index tuning.
We compact data into slabs and choose the indexing algorithm for each slab automatically, applying more sophisticated indexing as slabs get larger. That reorganization runs in the background as the dataset grows, without interrupting reads or writes. Nobody picks or tunes an algorithm. The
slab architecture
post walks through how compaction works.
Scaling.
We keep data on object storage, separate from the machines that serve queries, so
storage can grow without adding compute
, and the reverse. Your data is never resharded as it grows, and on the on-demand tier you never pick a shard or replica count.
Embedding.
We run embedding and reranking models on Pinecone through
Pinecone Inference
, so there is no separate model to go find. It is optional. Bring your own if you already have one.
Recall.
Chunking and the choice of embedding model still decide what comes back. On Pinecone Database, recall problems that start there are still yours to debug. Pinecone Assistant handles chunking and embedding for you.
Capacity is still a choice in one place. On the on-demand tier, a large workload can start to hit rate limits, as it will in any shared system. Dedicated Read Nodes reserve query nodes and storage for a specific index, and the way you query is unchanged. That is capacity you provision, and its shards and replicas are set by hand today.
When Self-Hosting Is Still the Right Call
Stay on pgvector when the corpus is small and mostly static, with an index that fits in memory you already pay for. HNSW on Postgres performs well there and is simple to operate.
Postgres brings decades of operational maturity: point-in-time recovery, streaming replication, mature backup tooling, extensive access controls and a hiring pool that already knows how to run all of it. Moving vectors out means running a second system with its own approach to each of those. A Pinecone query also runs outside Postgres, so it cannot join against your tables in one statement. For some teams, that trade doesn't pay off.
Which way the corpus is headed decides it. If it will keep growing and changing under filtered queries, the tuning and scaling work comes back.
Getting to a First Query
Sign up at pinecone.io. The free tier doesn't need a credit card.
Pick a path.
Pinecone Database
gives full control of the pipeline: chunk and embed your data, upsert, query with filters and metadata, and rerank, all from one API.
Pinecone Assistant
takes uploaded documents and handles chunking, embedding and indexing, then answers through an LLM or returns the snippets alone. The more control you need, the more likely Database is the right fit.
Run the
quickstart
, in the docs or through the Pinecone skill for your coding assistant. The skill ships with sample data and runs the whole quickstart in your terminal.
Swap in your own data. Once it's in an index and you can query it, you're live.
The assistant that promised unlimited requests needs those five stages whoever runs them. The choice is how much of their operation your team carries before the first feature ships. To go further,
watch the full replay
or
run the quickstart
.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
