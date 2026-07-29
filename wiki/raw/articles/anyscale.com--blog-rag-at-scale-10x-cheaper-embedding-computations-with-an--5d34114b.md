---
title: "RAG at Scale: 10x Cheaper Embedding Computations with Anyscale and Pinecone"
url: "https://anyscale.com/blog/rag-at-scale-10x-cheaper-embedding-computations-with-anyscale-and-pinecone"
fetched_at: 2026-07-29T10:11:53.129694+00:00
source: "Anyscale Blog"
tags: [blog, raw]
---

# RAG at Scale: 10x Cheaper Embedding Computations with Anyscale and Pinecone

Source: https://anyscale.com/blog/rag-at-scale-10x-cheaper-embedding-computations-with-anyscale-and-pinecone

Check out our updated RAG blog
For the most up-to-date content on how to run the best RAG pipelines with Ray,
read our updated blog
.
Previously, we showed how Ray Data is highly efficient on batch inference compared to other solutions (see the
blog post
for more details). In this blog, we demonstrate this on a large-scale production workload with Pinecone.
The first steps in building a
Retrieval-Augmented Generation (RAG)
application is to create embeddings of your data. These are representations of meaning and context that vector databases use for search and retrieval. Creating embeddings presents several challenges.
Scale:
Terabyte-sized datasets are common, and the workloads are memory-intensive. With scale comes cost.
Heterogeneous compute:
Embedding computations involve data ingest, preprocessing, chunking, and inference. This requires a mix of CPU and GPU compute. Adding to the challenge, a mixture of GPU types may be needed.
Multimodal data:
RAG applications work with documents, images, and an increasing variety of data modalities.
We are excited to announce that with
Anyscale
and
Pinecone
, users can now generate embeddings for use in a distributed vector database at 10% of the cost of other popular offerings!
Link
Breakthrough vector database delivers up to 50x cost savings
With this launch, Pinecone is extending its lead as the technology and market leader by completely re-inventing the vector database. This groundbreaking serverless vector database lets companies add unlimited knowledge to their GenAI apps at 2% of the prior cost. With Pinecone serverless, you can store billions of vectors and only pay for what you search
.
Key innovations that lead to the cost-savings and high performance include the following.
The separation of reads, writes, and storage significantly reduces costs for all types and sizes of workloads.
A pioneering architecture, with vector clustering on top of blob storage, provides low latency and always-fresh vector search over practically unlimited data sizes at a low cost.
Novel indexing and retrieval algorithms enable fast and memory-efficient vector search from blob storage without sacrificing retrieval quality.
A multi-tenant compute layer provides powerful and efficient retrieval for thousands of users, on demand. This enables a serverless experience in which developers don’t need to provision, manage, or even think about infrastructure, as well as usage-based billing that lets companies pay only for what they use.
Link
Comparing to other embedding computation approaches
When computing embeddings, there are a handful of common approaches.
OpenAI:
API providers like OpenAI can handle embeddings computation, but require a separate solution for scalable data ingest and preprocessing. Flexibility in model choice is limited.
Spark:
Distributed frameworks like Spark can scale data ingest and preprocessing, but need a separate solution for efficient embeddings computation.
Vertex AI:
Google Cloud can handle data ingest and preprocessing, and Vertex AI can handle embedding computations. Like OpenAI, flexibility in model choice is limited.
The approaches above do not comprise an all-in-one solution that handles both data ingestion and embedding computations at scale, while allowing for flexibility in the preprocessing step and embedding model.
The Overall RAG Stack
Zooming out, embedding computations are just part of the picture. To build a RAG application, there are many pieces.
A high-performance, distributed vector database such as
Pinecone
is necessary to support efficient inserts and queries with the computed embeddings.
Hugging Face
and
LangChain
provide open source models and utilities used for computing embeddings.
Finally, a distributed computation engine such as
Ray
ties all of these elements together and seamlessly manages the end-to-end workflow.
Link
Using Ray Data and the Pinecone API
The following example outlines how to use Ray Data and the Pinecone API to compute and upsert embeddings to Pinecone:
import
ray
from
pinecone
import
Pinecone
from
langchain.text_splitter
import
RecursiveCharacterTextSplitter
import
numpy
as
np
from
transformers
import
AutoTokenizer, AutoModel
import
uuid
def
chunk_row
(
row
):
# Chunk each input row
splitter = RecursiveCharacterTextSplitter(...)
chunks = splitter.split_text(row[
"text"
])
return
[
{
"id"
:
str
(uuid.uuid4()),
"text"
: chunk,
}
for
chunk
in
chunks
]
class
ComputeEmbeddings
:
def
__init__
(
self, model_name=
"thenlper/gte-large"
):
# To use a different embedding model, update the default name
# above, or pass the new model name in the map_batches() call:
# chunked_ds.map_batches(
# 	ComputeEmbeddings, fn_constructor_args=(new_model_name,)
# )
self.model = AutoModel.from_pretrained(model_name)
self.tokenizer = AutoTokenizer.from_pretrained(model_name)
def
__call__
(
self, batch
):
batch_text = batch[
"text"
]
tokenize_results = self.tokenizer(batch_text)
model_input = {
"input_ids"
: tokenize_results[
"input_ids"
],
"token_type_ids"
: tokenize_results[
"token_type_ids"
],
"attention_mask"
: tokenize_results[
"attention_mask"
],
}
embeddings = self.model(**model_input)
embeddings = self._average_pool(outputs.last_hidden_state, model_input[
'attention_mask'
])
embeddings = F.normalize(embeddings)
batch[
"values"
] = embeddings.numpy().astype(np.float32)
return
batch
def
_average_pool
(
self, last_hidden_states, attention_mask
):
last_hidden = last_hidden_states.masked_fill(~attention_mask[...,
None
].
bool
(),
0.0
)
return
last_hidden.
sum
(dim=
1
) / attention_mask.
sum
(dim=
1
)[...,
None
]
def
pinecone_upsert
(
batch
):
client = Pinecone(api_key=...)
index = client.Index(index_name)
result = index.upsert(vectors=batch)
return
{
"num_success"
: np.array([result.upserted_count])}
# replace with read API corresponding to your input file type
ds = ray.data.read_parquet(
"s3://bucket-raw-text"
)
# chunk the input text
chunked_ds = ds.flat_map(chunk_row)
# compute embeddings with a class that calls the embeddings model
embeddings_ds = chunked_ds.map_batches(ComputeEmbeddings)
# replace with write API corresponding to your desired output file type
embeddings_ds.write_parquet(
"s3://output-embeddings"
)
# upsert embeddings to Pinecone with the Pinecone API
upsert_results = embeddings_ds.map_batches(pinecone_upsert).materialize()
For more details and additional examples on how to best leverage the Ray Data API, please refer to the
Ray Data documentation
.
Link
Cost comparison
To compare the price-performance of Anyscale to other solutions, we generated embeddings for the
falcon-refinedweb dataset
, which has over 600 billion tokens using Amazon Web Services EC2 service
g5.xlarge
machines, pre-processing was done on CPU-only machines. The following table compares cost estimates for Anyscale and several popular alternatives to generate the 1 billion embeddings (prices as of January 2024):
Note that for the alternatives listed here, these costs do not include data ingest and preprocessing costs, so Anyscale is even more cost-efficient than the above estimates suggest!
Link
Conclusion
Generating embeddings is a critical task for developing successful RAG applications, and Anyscale is the most cost-efficient solution for this workflow. To fully take advantage of the scale that Anyscale enables,
check out Pinecone’s distributed vector database service
and try out the
Anyscale Platform
.
