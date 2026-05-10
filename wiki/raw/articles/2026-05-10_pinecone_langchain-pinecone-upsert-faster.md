---
title: "LangChain's Pinecone upsert speed increased by 5X"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/langchain-pinecone-upsert-faster/"
scraped: "2026-05-10T01:27:12.499484+00:00"
lastmod: "2023-09-12T19:08:49Z"
type: "sitemap"
---

# LangChain's Pinecone upsert speed increased by 5X

**Source**: [https://www.pinecone.io/blog/langchain-pinecone-upsert-faster/](https://www.pinecone.io/blog/langchain-pinecone-upsert-faster/)

←
Blog
LangChain's Pinecone upsert speed increased by 5X
Zachary Proser
Sep 12, 2023
Engineering
Share:
Jump to section:
Benchmarking improvements
Quality of life improvements
Give it a shot!
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
In release
v0.0.281
of the LangChain Python client, we’ve increased the speed of upserts to Pinecone indexes by up to 5 times, using asynchronous calls to reduce the time required to process large batches of vectors.
You can view
the pull request itself here
.
Benchmarking improvements
Using pyinstrument to benchmark our changes, we saw a speed increase of up to 5X for jobs with many embeddings to upsert.
Before,
chunk_size
and
batch_size
were the only values you could tweak to fine-tune LangChain methods that perform a Pinecone upsert.
We've added
embeddings_chunk_size
, which is helpful when you spend most of your time waiting on your embedding model.
Before optimization, using a
chunk_size
of 32 and a
batch_size
of 32, we saw:
4,000 documents took between 4-5 minutes to upsert
42,000 documents took around 30 minutes to upsert
Following optimization, using the newly added parameter
embeddings_chunk_size
of 1000 and a
batch_size
of 32, we saw:
4,000 documents took around 1 minute to upsert
42,000 documents took between 8-10 minutes to upsert
OpenAI's
text-embedding-ada-002
model was used to provide embeddings.
Quality of life improvements
We also made a few other quality-of-life improvements for users of the Pinecone integration:
Consolidating from_texts and add_texts
The
from_texts
method now calls
add_texts
under the hood for more consistent performance, so both methods take advantage of the new asynchronous pattern. This will also make both methods easier to maintain going forward.
Separating batching of embeddings and index upsert
In our pre-optimization testing of Jupyter Notebooks and integrations that wrap Pinecone, such as LangChain, we found that one of the primary bottlenecks is waiting on the conversion of inputs into embeddings, which is done by whichever embedding model you choose, completely separately from your interactions with Pinecone.
One of the more commonly used embedding models is OpenAI’s
text-embedding-ada-002
model.
Part of our upsert optimization involves chunking the embeddings before upserting them.
If you are using OpenAI for your embedding model, we recommend a
pool_threads
value of greater than 4 when constructing your Pinecone index and using an
emedding_chunk_size
of at least 1000 and a
batch_size
of 64 for ideal performance.
Automatically setting thread_pool size when instantiating Pinecone index
The
pool_threads
setting determines the number of threads to use for asynchronous requests. More threads means more concurrent API requests.
In general, increasing
pool_threads
should increase performance for asynchronous workloads, but setting this value too high could lead to API rate limits or memory issues.
By default, the Pinecone Python client now passes a
pool_threads
value of 4 when connecting to an Index.
The default embedding_chunk_size value of 1000 is passed to add_texts and from_texts methods
You can override this value as desired to fine-tune performance for your specific use case, but in our testing, this is a good default for most use cases.
Give it a shot!
You can try out the latest and greatest by installing the Python LangChain package of version v0.0.281 or later. If you have any feedback or encounter any issues, please file an issue against either the
LangChain
or
Pinecone Python client
repository as appropriate.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
