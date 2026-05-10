---
title: "Simplifying Vector Embeddings with Pinecone Integrated Inference Capabilities"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/simplifying-vector-embeddings-with-pinecone-integrated-inference/"
scraped: "2026-05-10T01:27:11.742480+00:00"
lastmod: "2025-10-13T17:00:51Z"
type: "sitemap"
---

# Simplifying Vector Embeddings with Pinecone Integrated Inference Capabilities

**Source**: [https://www.pinecone.io/blog/simplifying-vector-embeddings-with-pinecone-integrated-inference/](https://www.pinecone.io/blog/simplifying-vector-embeddings-with-pinecone-integrated-inference/)

←
Blog
Simplifying Vector Embeddings with Pinecone Integrated Inference Capabilities
John Ward
Oct 9, 2025
Company
Product
Share:
Jump to section:
What is Integrated Inference?
A Simple Example
The Customer’s Challenge
The Workaround: Using the Inference API Directly
Key Takeaways
Final Thoughts
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Recently, one of my customers ran into an issue using Pinecone’s integrated inference capabilities. It was a great reminder of how powerful this feature can be, but also of the small edge cases we need to watch out for. In this post, I’ll explain what integrated inference is, what happened with my customer, and how we solved it with a simple workaround.
What is Integrated Inference?
Integrated inference is Pinecone’s built-in offering of embedding models that generate vector embeddings inline. Normally, creating embeddings requires a chain of extra steps: choosing and hosting a model, provisioning GPUs or servers, managing scaling, and wiring in code to call the model separately from your database. Even if you use an external API, you still need to make multiple calls, handle retries, and pass results from the embedding service into your vector database. With integrated inference, Pinecone collapses all of these steps into a single API call, letting you index and query with embeddings without managing any of the complexity yourself.
Traditionally, embedding for Retrieval Augmented Generation (RAG) or search pipelines looks like this:
Take your corpus of text: paragraphs, documents, even books.
Break the text into chunks that fit into the input size of your chosen embedding model.
Pass each chunk through the embedding model to generate vectors.
Store those vectors in your vector database.
When querying, embed the query text and search for nearest neighbors in the database.
Conceptually, embedding is simple: text in, vector out. In practice, though, it adds friction to every workflow. Most teams today call an external API like OpenAI or Cohere to generate embeddings. That means every time you want to index data, you have to call one API to create vectors, then call your vector database to store them. You also need to keep track of model compatibility, embedding dimensions, scaling limits, and API retries. If you choose to self-host, the burden grows even heavier with GPU provisioning, monitoring, and scaling. And no matter which path you take, you still have to glue it all together with frameworks like LangChain, Langflow, or your own custom code.
With integrated inference, you skip all that. You can send your data to Pinecone and let the platform generate embeddings automatically as part of the upsert. That means less infrastructure, fewer moving parts, and more time spent building valuable applications instead of plumbing.
A Simple Example
Here’s what it looks like in practice using the upsert_records() method, which handles embeddings behind the scenes:
# Import the Pinecone library
from pinecone import Pinecone
from datasets import load_dataset
from typing import List
import json

# --- Load Config ---
with open("config.json", "r") as f:
   CONFIG = json.load(f)

PINECONE_API_KEY = CONFIG["API_KEY"]
INDEX_NAME = "integrated-test"

#load sample from datasets
def load_ccnews(n: int = 200) -> List[dict]:
   ds = load_dataset("cc_news", split="train")
   ds_small = ds.select(range(min(n, len(ds))))
   items = []
   for i, row in enumerate(ds_small):
       text = (row.get("title") or "").strip()
       body = (row.get("text") or "").strip()
       if text and body:
           content = f"{body}"
       else:
           content = text or body
       items.append(
           {
               "id": f"ccnews-{i}",
               "text": content,
               "metadata": {
                   "title": row.get("title") or "",
                   "publisher": row.get("publisher") or "",
                   "ccnews_id": i,
               },
           }
       )
   return items

# 1) Load some sample documents
chunks = load_ccnews()

# 2) Pinecone client and Inference
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

# 3) build sample records
vectors = []
batch = 65
cnt = 0
for text in chunks:
   metadata = text["metadata"]

   vectors.append(
       {
           "_id": text["id"],
           "text": text["text"],
           "title": metadata["title"],
           "publisher": metadata["publisher"],
           "ccnews_id": metadata["ccnews_id"]
       }
   )
   cnt = cnt + 1
   if cnt > batch:
       break

# 3) Upsert into pinecone
index.upsert_records(records=vectors, namespace="test")
With just a few lines, you have embeddings generated and stored in your Pinecone index.
The Customer’s Challenge
My customer was embedding a large data source that wasn’t text-based. The problem was that the upsert_records() method automatically includes the full text field as metadata. Combine that with the large amount of metadata they were already attaching, and they quickly exceeded Pinecone’s
40KB metadata size limit
.
The kicker: you cannot disable the automatic inclusion of the text field when using upsert_records().
At first glance, this looked like a dealbreaker. But we quickly realized there was a straightforward workaround.
The Workaround: Using the Inference API Directly
Instead of relying on the automatic embedding inside upsert_records(), you can call Pinecone’s integrated inference API directly through the SDK. This gives you embeddings without adding the original text into metadata automatically.
Here’s what that looks like:
from typing import List
from datasets import load_dataset
from pinecone.grpc import PineconeGRPC as Pinecone
import json

# --- Load Config ---
with open("config.json", "r") as f:
   CONFIG = json.load(f)

PINECONE_API_KEY = CONFIG["API_KEY"]
INDEX_NAME = "integrated-test"

def load_ccnews(n: int = 200) -> List[dict]:
   ds = load_dataset("cc_news", split="train")
   ds_small = ds.select(range(min(n, len(ds))))
   items = []
   for i, row in enumerate(ds_small):
       text = (row.get("title") or "").strip()
       body = (row.get("text") or "").strip()
       if text and body:
           content = f"{text}\n\n{body}"
       else:
           content = text or body
       items.append(
           {
               "id": f"ccnews-{i}",
               "text": content,
               "metadata": {
                   "title": row.get("title") or "",
                   "publisher": row.get("publisher") or "",
                   "ccnews_id": i,
               },
           }
       )
   return items

# 1) Load some sample documents
chunks = load_ccnews()

# 2) Pinecone client and Inference
pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

vectors = []
batch = 0
batch_size = 65
cnt = 0
for text in chunks:
   if cnt > 100:
       metadata = text["metadata"]

       embeddings = pc.inference.embed(
           model="llama-text-embed-v2",
           inputs=text['text'],
           parameters={"input_type": "passage", "truncate": "END"}
       )

       embedding = embeddings[0]

       vectors.append(
           {
               "id": text["id"],
               "values": embedding["values"],
               "metadata": {
                   "title": metadata["title"],
                   "publisher": metadata["publisher"],
                   "ccnews_id": metadata["ccnews_id"]
               }
           }
       )
       batch = batch + 1

   cnt = cnt + 1
   if batch > batch_size:
       break

# Upsert
index.upsert(vectors=vectors, namespace="test")
This approach requires one extra step: you call the inference endpoint explicitly, get the embedding back, and then upsert it. But the tradeoff is that you have full control over what gets stored in metadata. No unexpected bloat, no 40KB errors.
Key Takeaways
Integrated inference dramatically simplifies embedding pipelines.
The upsert_records() method is the fastest way to get started, but it auto-includes the text field in metadata.
For workloads with heavy metadata, call the Inference API directly to avoid hitting metadata limits.
Either way, you never have to worry about hosting or scaling embedding models yourself.
Final Thoughts
Vector embeddings are at the heart of modern AI applications, but managing embedding models is a hassle most developers would rather skip. Pinecone integrated inference capabilities remove that friction by baking embeddings into the workflow.
If you’re just starting out, use upsert_records() for speed and simplicity. If you’re running large-scale, metadata-heavy workloads, use the Inference API for greater control. Either way, Pinecone has your back so you can focus on building intelligent systems rather than babysitting infrastructure.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
