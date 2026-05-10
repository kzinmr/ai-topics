---
title: "Introducing integrated inference: Embed, rerank, and retrieve your data with a single API"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/integrated-inference/"
scraped: "2026-05-10T01:27:13.599089+00:00"
lastmod: "2026-03-18T19:45:10Z"
type: "sitemap"
---

# Introducing integrated inference: Embed, rerank, and retrieve your data with a single API

**Source**: [https://www.pinecone.io/blog/integrated-inference/](https://www.pinecone.io/blog/integrated-inference/)

←
Blog
Introducing integrated inference: Embed, rerank, and retrieve your data with a single API
Gibbs Cullen
,
Gareth Jones
Dec 2, 2024
Product
Share:
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
We’re excited to announce expanded inference capabilities alongside our core vector database to make it even easier and faster to build high-quality, knowledgeable AI applications with Pinecone.
We introduced
embedding
and
reranking
earlier this year. Today, we’re announcing the GA of those capabilities and bringing inference closer to the database with a native integration and fully managed support for new models developed by Pinecone and Cohere so you can now embed, rerank, and query your data with a single API.
Tl;dr: What’s new
Database endpoints that integrate embedding and reranking
More models, fully hosted alongside our database:
Pinecone reranking model,
pinecone-rerank-v0
Pinecone sparse embedding model,
pinecone-sparse-english-v0
Cohere’s Rerank 3.5 model,
cohere-rerank-v3.5
Streamline AI development with fast, easy access to leading models
To help you unlock the full value of your unstructured data, Pinecone has expanded its knowledge platform with native access to leading embedding and reranking models, all accessible through
new database endpoints
. Building AI applications often involves juggling multiple tools and models for inference, retrieval, and database management. Pinecone simplifies this process by integrating these capabilities directly into its secure, fully managed platform. With this unified approach, you can focus on solving problems instead of managing infrastructure with:
Simplified integration:
Accelerate AI development with unified access to inference, retrieval, and database management. Skip the hassle of managing multiple tools and vendors and get started with minimal setup and a few lines of code.
Seamless scaling:
Pinecone’s serverless infrastructure scales automatically, handling workloads without manual provisioning. With separate read/write quotas and token-based pricing, we ensure predictable costs and uninterrupted performance.
Secure, private networking
: Eliminate the security risks associated with cross-network communication. Add a layer of protection with Private Endpoints for AWS PrivateLink, and leverage our expanded security suite with CMEK, RBAC, and Audit Logs for more granular control and visibility into your data across the platform.
{
  "query": {
    "top_k": 10,
    "inputs": {
      "text": "hello world"
    }
  },
  "rerank": {
    "model": "pinecone-rerank-v0",
    "rerank_fields": ["chunk_text"],
    "top_n": 5
  },
  "fields": ["title", "chunk_text"]
}
Easily input or update your integrated model of choice via a simple API configuration.
Best-in-class OSS and proprietary models
Pinecone’s unified platform offers powerful retrieval and reranking with access to top models, including new sparse embedding and reranking options, to meet diverse application needs. Fully hosted alongside our database, our new integrated inference capabilities make it even easier to achieve high-quality results within your same Pinecone environment. No AI or domain expertise is needed.
Embed
Dense embeddings and retrieval are excellent at understanding the meaning and semantics of your unstructured data, enabling you to search the way you think (e.g. semantic search). Dense retrieval alone, however, can lead to suboptimal results when queries are searching for certain entities or proper nouns (e.g. keyword or lexical search). With support for both sparse and dense embeddings and retrieval, you get the best of both worlds: high recall and relevance.
Our sparse embedding model —
pinecone-sparse-english-v0
— boosts performance for keyword-based queries, delivering up to 44% and on average 23% better NDCG@10 than BM25 on TREC (
source
). Easily leverage our new sparse index type (
early access
) to store and manage your sparse embeddings.
The multilingual dense embedding model—
multilingual-e5-large
—balances latency and quality. It works well on messy data and is good for short queries expected to return medium-length passages of text (e.g., 1-2 paragraphs).
Rerank
Using reranking in workflow has
many benefits
, including increased accuracy and reduced token waste for lower costs. Combining both sparse and dense vectors, reranking models calculate a relevance score using each query document pair before reordering them from most to least relevant. This ensures only the most relevant documents are passed along as context to the LLM.
Our new reranking model —
pinecone-rerank-v0
— improves search accuracy by up to 60% and on average 9% over industry-leading models on the BEIR benchmark (
source
).
Cohere’s leading reranking model —
cohere-rerank-v3.5
— is fully managed on Pinecone’s infrastructure, balancing performance and latency for a wide range of enterprise search applications.
A popular, open-source multilingual reranking model —
bge-reranker-v2-m3
— that balances latency and performance
While integrated inference can help accelerate your AI development, Pinecone also supports dense embeddings with up to 20k dimensions from any embedding model or model provider. Choose the model that works best for your workload, regardless of the source, or fill out
our request form
to provide us with feedback on additional models to host.
Start building today
With our new integrated inference capabilities, you can easily manage embedding and reranking with new database endpoints via the Python SDK, Pinecone API, or within the console.
pip install --upgrade pinecone pinecone-plugin-records
Prepare data
We are introducing a new DocDB-style format for rows. The limitations that apply to vector metadata also apply to record fields. You must include an id and the field you want to embed, we’ll use `chunk_text` in this example
{
   "id": "doc1#chunk1", 
   "title": "Apple Facts",
   "chunk_text": "Apples are a popular fruit known for their sweetness",
}
Create an index
Using the new
‘create_for_model’
endpoint we will create a new serverless index and specify one of Pinecone’s
hosted embedding models
. We use the field_map parameter to specify which field in the record to embed.
from pinecone import Pinecone

pc = Pinecone(api_key="<<PINECONE_API_KEY>>")

# Create an index for your embedding model
index_model = pc.create_index_for_model(
    name="my-model-index",
    cloud="aws",
    region="us-east-1",
    embed={
       "model":"multilingual-e5-large", 
       "field_map": {
          "text": "chunk_text" # which field to embed
       } 
    }
)

# establish an index connection
index = pc.Index(host=index_model.host)
Upsert data
The
/records/upsert
endpoint converts your source data to vector embeddings and then upserts them into a single namespace.
# upsert records
# upsert records
index.upsert_records(
    "my-namespace",
    [
        {
            "_id": "test1",
            "chunk_text": "Apple is a popular fruit known for its sweetness and crisp texture.",
        },
        {
            "_id": "test2",
            "chunk_text": "The tech company Apple is known for its innovative products like the iPhone.",
        },
        {
            "_id": "test3",
            "chunk_text": "Many people enjoy eating apples as a healthy snack.",
        },
        {
            "_id": "test4",
            "chunk_text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces.",
        },
        {
            "_id": "test5",
            "chunk_text": "An apple a day keeps the doctor away, as the saying goes.",
        },
        {
            "_id": "test6",
            "chunk_text": "Apple Computer Company was founded on April 1, 1976, by Steve Jobs, Steve Wozniak, and Ronald Wayne as a partnership.",
        },
    ],
)
Query and rerank
Once complete, you’re ready to start querying documents using the
/records/search
endpoint and just a few lines of code.
{
  "query": {
    "top_k": 10,
    "inputs": {
      "text": "hello world"
    }
  },
  "rerank": {
    "model": "pinecone-rerank-v0",
    "rerank_fields": ["chunk_text"],
    "top_n": 5
  },
  "fields": ["title", "chunk_text"]
}
Our new models —
pinecone-rerank-v0
and
pinecone-sparse-english-v0
—
are now available in public preview for all users.
Contact us
to see how Pinecone can accelerate your time to value with AI.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
