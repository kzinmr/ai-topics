---
title: "Generating Test Data for Pinecone"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/generating-test-data-for-pinecone/"
scraped: "2026-07-02T06:00:03.983854+00:00"
lastmod: "2026-06-29T19:13:20Z"
type: "sitemap"
---

# Generating Test Data for Pinecone

**Source**: [https://www.pinecone.io/blog/generating-test-data-for-pinecone/](https://www.pinecone.io/blog/generating-test-data-for-pinecone/)

←
Blog
Generating Test Data for Pinecone
John Ward
Jun 29, 2026
Engineering
Share:
Jump to section:
Why Test Data Generation Matters
Requirements for the Dataset
First Version: Stream, Embed, and Upsert Directly
Why I Split the Workflow
Second Version: Generate Parquet Without Embeddings
Third Version: Generate Embeddings From Parquet
Bulk Import Into Pinecone
Lessons Learned
Wrapping Up
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
I joined Pinecone as a Solutions Engineer about a year ago. Since then, several of my projects have turned into internal tools and examples for testing different parts of the platform. This article is the first in a series walking through them; later posts will cover my Pinecone Index Migrator, a GPU benchmarking utility, a dense vector embedding generator, and examples for querying dense, sparse, and hybrid indexes.
It starts with something that sounds simple but matters more at scale: generating test data. For most of my work I need a repeatable way to create datasets that are large enough to be useful, realistic enough to support recall and accuracy testing, and flexible enough to reuse across experiments. That led to a small collection of utilities for generating Parquet files, creating embeddings, preparing metadata, and importing the data into Pinecone.
The utilities are broken into a few parts:
Parquet file generator
Vector embedding generator
Parquet categorizer using a local LLM
Parquet repartitioner that uses categories as namespaces for Pinecone bulk import
This article focuses on the first part of that workflow: generating the source data and preparing it for embedding and import. The full, runnable scripts live in the
companion notebook
; the snippets below are the parts worth discussing in line.
Why Test Data Generation Matters
One of the first things I ran into when I started working with Pinecone was the need to create different datasets for different types of tests. Not all test data is the same, and not all dataset sizes are the same.
It is easy to say that a platform works "at scale," but that phrase means different things depending on the workload. A test with 500,000 vectors isn't the same as one with 15 million — or 100 million, 500 million, or a billion. Each size introduces its own set of problems around ingestion, storage, latency, filtering, cost, and operational workflow.
There are some great sources of raw data out there, including Hugging Face datasets and Kaggle datasets. Those are a good starting point, but they are only part of the problem. For vector search testing, I still need to generate vectors. That leads to an important question:
Do the vectors need to be real?
Sometimes no. If I am only testing write throughput, storage behavior, or query latency, random vectors are good enough — I've had use cases where speed was the only thing under evaluation and the meaning of the vector did not matter. But for most tests, recall and accuracy do matter, and that means the embeddings have to represent the actual text. Random vectors will not help there.
So for this project, I wanted to generate a realistic dataset from real text, create real embeddings, and store everything in a format that could be imported into Pinecone efficiently.
Requirements for the Dataset
For this first utility, I wanted a reference dataset that I could regenerate as needed. I also wanted the data to be familiar enough that I could reason about the results when testing search behavior.
My requirements were pretty straightforward:
Use a real text dataset with broad coverage
Use Python, partly for more hands-on practice with it
Store the output in Parquet
Make the output compatible with Pinecone bulk import
Support local embedding generation
Make it possible to split the embedding work across multiple machines later
I landed on the
stanford-oval/ccnews
dataset from Hugging Face. It gives me a broad set of news articles, and it includes useful metadata fields like title, author, source URL, published date, and category information.
For the Pinecone import format, the structure is simple:
The
field is the unique vector ID. I generally prefer structured IDs because they make debugging and operational tasks easier later. In this example, UUIDs are used, but this could easily be adjusted to include prefixes, document IDs, chunk numbers, or other identifiers.
The values field contains the dense vector.
The metadata field contains the JSON metadata associated with the vector. One thing to watch out for when writing Parquet for bulk import is that the metadata field should be written as a JSON string, not as a nested JSON object. That is a small detail, but it matters when you are preparing files for import.
Choosing an Embedding Model
For this example, I used
BAAI/bge-large-en-v1.5
, accessed through the
registry name in
.
This model produces 1024-dimensional dense vectors. I could have used
Pinecone-hosted embedding models
, but for this project I wanted to experiment with local embedding generation. I also wanted to simulate a workflow I see frequently in the field, where customers generate embeddings themselves and then load the resulting vectors into Pinecone.
There are tradeoffs here. Higher-dimensional vectors can improve retrieval quality in some workloads, but they also increase storage size and can affect speed and cost. Pinecone can support many different embedding models, so the right choice depends on what you are testing. If I were testing multimodal search, for example, I might use a model like CLIP instead.
The model isn't a fixed choice here; what matters is that the workflow stays flexible enough to swap models later.
First Version: Stream, Embed, and Upsert Directly
The first version of the script is the easiest one to understand. It streams the CC News dataset from Hugging Face, chunks the article text, generates embeddings locally, and upserts the vectors directly into a Pinecone index.
This is useful for smaller tests because there are fewer moving parts. The script does everything in one flow: create the index if it does not exist, stream records, skip unusable or non-English records, chunk the text, generate embeddings, attach metadata, and upsert. The full script is in the notebook (
section 1
). A few details are worth calling out.
First, the script checks the metadata size. Pinecone enforces a 40 KB limit on the metadata payload per vector, and since I am storing the original text in metadata for these tests, a long article can blow past it. The chunker trims iteratively until the serialized metadata fits:
while sys.getsizeof(json.dumps({"text": chunk})) >= MAX_JSON_BYTES and len(chunk) > 1000:
  chunk = chunk[: int(len(chunk) * 0.9)]
Second, the script drops null metadata values. Pinecone rejects null values, and the source dataset has missing fields, so I filter them out before upserting:
batch_metadata.append({k: v for k, v in meta.items() if v is not None})
Third, the script batches upserts. Sending one vector at a time is not a great pattern for performance, especially once the dataset gets larger, so vectors accumulate until they reach
and flush together.
For a small test, this direct approach works well. But it starts to break down once the dataset gets bigger.
Why I Split the Workflow
The direct upsert script is simple, but it is not the approach I would use for tens or hundreds of millions of vectors.
The reason is time. When rows, chunking, embedding, and upserting all run in one process, the embedding step becomes the bottleneck. That's fine for a few thousand vectors, but at millions it becomes a problem, and at hundreds of millions, doing everything inline could take an unreasonable amount of time.
So I separated the work into two stages: the first writes the text records to Parquet, and the second reads those files, generates embeddings, and writes new Parquet files with the values column populated.
That gives me more flexibility. I can generate the source files once, then spread the embedding work across multiple machines. I do not have to worry as much about state tracking because each machine can process a separate set of Parquet files.
In my case, I had several machines available, including Apple M-Series machines and ASUS ROG laptops with NVIDIA GPUs. But the same idea works whether you run locally, use cloud GPU instances, or use a service like RunPod.
Second Version: Generate Parquet Without Embeddings
The second script streams the same CC News dataset, chunks the article text, and writes Parquet files. The difference is that it does not generate embeddings yet. The values column is written as an empty list, and that placeholder gets filled in later by the embedding script.
I used PyArrow instead of Pandas here because I wanted the Parquet schema to be explicit. In particular, the values field has to be written as LIST<FLOAT>. If Pandas infers that column as a generic object type, that breaks the Pinecone bulk import later:
PARQUET_SCHEMA = pa.schema([
  pa.field("id", pa.string()),
  pa.field("values", pa.list_(pa.float32())), # empty for now; filled offline
  pa.field("metadata", pa.string()), # JSON string, nullable per spec
])
Each record is written with the placeholder in place, and the metadata is already a JSON string so it matches the import format:
buffer.append({
  "id": str(uuid.uuid4()),
  "values": [], # placeholder — filled by the offline embedding step
  "metadata": metadata_str, # Pinecone parquet import expects a JSON string
})
The full script is in the notebook (
section 2
). It is intentionally boring, which is a good thing — it does one job: turn raw dataset records into chunked, metadata-rich Parquet files.
The partition size is configurable. I usually keep partitions around 10,000 to 20,000 records because that fits the way I tend to work with data files. You can go larger, and in some cases much larger, but smaller partitions make it easier to split work across machines and rerun failed chunks if something goes wrong.
For this stage, I do not need a Pinecone API key, index name, or embedding dimension. The script is only preparing files.
Third Version: Generate Embeddings From Parquet
Once I have the text-only Parquet files, I can run a separate embedding script. It reads each Parquet file, pulls the text out of the metadata, generates embeddings, and writes a new Parquet file with the values column populated. That output is ready for Pinecone bulk import.
The script detects the device at runtime, so the same file runs across different machines without a separate version for each environment. On Apple Silicon it uses mlx_embedding_models to run on the Mac GPU or Neural Engine; on NVIDIA it falls back to sentence-transformers on CUDA; otherwise it falls back to CPU:
if torch.backends.mps.is_available():
  DEVICE = "mps" # Apple Silicon — MLX on the Mac GPU / Neural Engine
elif torch.cuda.is_available():
  DEVICE = "cuda" # sentence-transformers on CUDA
else:
  DEVICE = "cpu" # CPU fallback
The full script is in the notebook (
section 3
). The main thing I need to tune is batch size. On CUDA and CPU paths, batch size can make a big difference, and the right value depends on available memory and the model being used.
Bulk Import Into Pinecone
After the embedding script finishes, I have Parquet files with IDs, dense vectors, and metadata — which is the whole reason for structuring the output this way. The next step is to copy them to object storage such as Amazon S3 and run Pinecone bulk import. For small tests, direct upsert is fine; for larger ones, bulk import is faster, more operationally convenient, and better suited to large datasets.
The overall workflow looks like this:
This gives me a repeatable process for different test sizes, models, and hardware setups.
Lessons Learned
A few practical lessons came out of this work.
First, keep the workflow modular. The direct upsert version is helpful for learning and smaller tests, but the separated Parquet workflow is much better once scale starts to matter.
Second, be clear about what you are testing. If you are only testing latency or write throughput, random vectors may be enough. If you are testing recall or answer quality, you need real embeddings created from real content.
Third, pay attention to metadata early. Metadata is easy to treat as an afterthought, but it affects filtering, debugging, import format, and storage limits. In this example, I stored the original text in metadata because it made later testing easier, but that also meant I had to watch metadata size.
Fourth, use explicit schemas when writing Parquet. It is much better to be precise up front than to find out later that a column was inferred incorrectly.
Finally, hardware matters. Local embedding generation can be surprisingly practical if you have the right hardware. Apple Silicon, NVIDIA GPUs, cloud GPU instances, and CPU fallback can all fit into the same workflow, but they will not perform the same.
Wrapping Up
Test data generation for vector search is not just about creating rows. It means thinking about the source text, the embedding model, the vector dimensions, the metadata, the file format, and the import path — and structuring the workflow so the embedding step can scale across machines instead of bottlenecking a single process.
In the next article, I'll go deeper into the embedding generation side of the workflow, including how I split the work across multiple machines and how Apple Silicon compared with NVIDIA GPUs for this type of task.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
