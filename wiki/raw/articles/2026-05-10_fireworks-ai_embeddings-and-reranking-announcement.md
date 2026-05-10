---
title: "Fireworks AI"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/embeddings-and-reranking-announcement"
scraped: "2026-05-10T01:27:17.581921+00:00"
lastmod: "2026-02-12T18:51:22.000Z"
type: "sitemap"
---

# Fireworks AI

**Source**: [https://fireworks.ai/blog/embeddings-and-reranking-announcement](https://fireworks.ai/blog/embeddings-and-reranking-announcement)

DeepSeek V4 Pro is Live → Try it now.
Platform
Models
Developers
Pricing
Training
Partners
Resources
Company
Log In
Get Started
Blog
Embeddings And Reranking Announcement
Announcing Embeddings and Reranking On Fireworks AI
PUBLISHED
10/9/2025
Today, we're announcing a major upgrade to Fireworks for RAG workloads – we’re bringing the state-of-the-art
Qwen3 8B Embeddings
and
Reranking
models to serverless, and are introducing
two new API endpoints
to make it all easily accessible.
Now, whether you're building semantic search, recommendation systems, or agents powered by enterprise data, Fireworks makes it easier than ever to build scalable RAG applications with open models.
Fireworks AI: Your End‑to‑End Platform for RAG Workloads
At a glance, a RAG pipeline consists of five core stages:
•
Embed:
Split documents into chunks and turn each chunk into a high‑dimensional vector with an embedding model.
•
Index:
Persist those vectors in a vector store (MongoDB, Chroma, pgvector, etc.).
•
Retrieve:
Convert the user query into a vector, run an Approximate‑Nearest‑Neighbor (ANN) search, and pull the most relevant chunks.
•
Rerank:
Apply a dedicated reranker model to the retrieved set, scoring each query‑chunk pair more precisely and selecting the top candidates.
•
Synthesize:
Feed the final context to an LLM, which generates the answer.
The problem:
Until now, teams have had to cobble together different providers for embeddings, reranking, and generation. The result is a pipeline that is complex, inconsistent, and hard to scale. Even though open models are
crushing the leaderboards
on embeddings and reranking tasks, AI teams are forced to choose between the operational pain of self‑hosting these models and the cost of closed‑source model APIs.
Now, with native support for embeddings and reranking, Fireworks lets you run every step of the RAG workflow on open models–efficiently, at scale, and on the same virtual cloud that powers mission‑critical workloads for customers like Cursor, Notion, and Cresta.
In particular, RAG workloads on Fireworks benefit from
•
Top-tier performance, from the moment a document is embedded to the final answer you generate
•
Frictionless scalability with global availability through our distributed infrastructure across 8 CSPs
•
Consistent developer experience across embedding, reranking, and generation tasks
•
Unified, pay‑as‑you‑go billing across all model workloads
New: Expanded model library with support for embeddings and reranking models
We are excited to launch serverless support for the state-of-the-art Qwen3 Embeddings 8B and Qwen3 Reranker 8B models, with their 4B and 0.6B variants available via on-demand deployments.
We also support the following BERT-based embeddings models on serverless
•
nomic-ai/nomic-embed-text-v1.5
and
nomic-ai/nomic-embed-text-v1
•
WhereIsAI/UAE-Large-V1
•
thenlper/gte-large
and
thenlper/gte-base
•
BAAI/bge-base-en-v1.5 and BAAI/bge-small-en-v1.5
•
mixedbread-ai/mxbai-embed-large-v1
•
sentence-transformers/all-MiniLM-L6-v2
•
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
In addition, any LLM on Fireworks can be queried for embeddings, including models you bring yourself through custom model upload (as long as the architecture is
supported by Fireworks
).
New: Support for embeddings and rerank endpoints
We’re excited to be unveiling two new endpoints for interacting with embeddings and reranking models
/v1/embeddings
and
/v1/rerank.
(Note: Qwen3 Reranker only)
Here’s an example of querying an embedding model. Simply pass the text you want to embed as an input and the resulting vector can be passed to a downstream storage solution like a vector database.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
import
requests
url
=
"https://api.fireworks.ai/inference/v1/embeddings"
payload
=
{
"input"
:
"The quick brown fox jumped over the lazy dog"
,
"model"
:
"fireworks/qwen3-embedding-8b"
,
}
headers
=
{
"Authorization"
:
"Bearer <FIREWORKS-API-KEY>"
,
"Content-Type"
:
"application/json"
}
response
=
requests
.
post
(
url
,
json
=
payload
,
headers
=
headers
)
print
(
response
.
json
(
)
)
And here is an example of querying the Qwen3 Reranker model
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
import
requests
url
=
"https://api.fireworks.ai/inference/v1/rerank"
payload
=
{
"model"
:
"fireworks/qwen3-reranker-8b"
,
"query"
:
"What was the primary objective of the Apollo 10 mission?"
,
"documents"
:
[
"The Apollo 10 mission was launched in May 1969 and served as a 'dress rehearsal' for the Apollo 11 lunar landing."
,
"The crew of Apollo 10 consisted of astronauts Thomas Stafford, John Young, and Eugene Cernan."
,
"The command module for Apollo 10 was nicknamed 'Charlie Brown' and the lunar module was called 'Snoopy', after characters from the Peanuts comics."
,
"The Apollo program was a series of NASA missions that successfully landed the first humans on the Moon and returned them safely to Earth."
]
,
"top_n"
:
3
,
"return_documents"
:
True
}
headers
=
{
"Authorization"
:
"Bearer <FIREWORKS-API-KEY>"
,
"Content-Type"
:
"application/json"
}
response
=
requests
.
post
(
url
,
json
=
payload
,
headers
=
headers
)
print
(
response
.
json
(
)
)
What’s next
To get started with embeddings and reranking on Fireworks, check out our
docs
! For a deeper dive into scaling embeddings and reranking, check out our For a deeper dive into scaling embeddings and reranking, check out our
previous blog post
.
We’re excited to continue building out more features for embeddings and reranking on Fireworks over the coming months. If you have a model you’d love to see enabled or a feature that would supercharge your RAG agent, we want to hear from you -- reach out via
[email protected]
. Your feedback directly helps us shape the roadmap.
Platform
AI Native
Enterprise
Customers
Use Cases
Code Assistance
Conversational AI
Agentic Systems
Search
Multimodal
Enterprise RAG
Developers
Model Library
Docs
CLI
API
Changelog
Pricing
Serverless
On-Demand
Fine Tuning
Enterprise
Partners
Cloud and Infrastructure
Consulting and Services
Technology
Fireworks for Startups
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
© 2026 Fireworks AI, Inc. All rights reserved.
