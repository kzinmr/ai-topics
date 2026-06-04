---
title: "Bulk Import Is Now Free Up to 1 TB"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/bulk-import-promo/"
scraped: "2026-06-04T06:00:24.323576+00:00"
lastmod: "2026-06-04T04:01:01Z"
type: "sitemap"
---

# Bulk Import Is Now Free Up to 1 TB

**Source**: [https://www.pinecone.io/blog/bulk-import-promo/](https://www.pinecone.io/blog/bulk-import-promo/)

←
Blog
Bulk Import Is Now Free Up to 1 TB
Lea Wang-Tomic
Jun 1, 2026
Product
Share:
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Starting June 1, bulk import is free up to 1 TB. Standard and Enterprise plans get a $250 credit applied automatically. After 1 TB, import runs at $0.25/GB – down 75% from $1/GB.
How bulk import works
Bulk import is already the fastest way to get a large dataset into Pinecone because it skips the standard write path entirely. Upsert acknowledges every request, sequences it, holds it in the memtable, and flushes before the index builder picks it up -- guarantees that matter for continuous writes, but overhead for a large one-time load. Bulk import reads directly from object storage into the index builder. The result is the same populated index through a more efficient path.
Semantic search over 200 bird species in a few lines
A terabyte of bulk import covers roughly 130 million records at 1024 dimensions with typical metadata. That's enough to load a substantial evaluation corpus, stand up a semantic search prototype against real data instead of a toy slice, or seed a production index before incremental writes take over.
The workflow has three steps regardless of scale: turn raw data into embeddings, write those embeddings as Parquet files in object storage, then call
. The example below uses the
bird search corpus
-- ~200 North American bird Wikipedia articles -- because it runs end-to-end in a few minutes. The same code handles a 1 TB load with a larger input dataset.
Generate the embeddings
(Note:
If you already have Parquet files with vectors you can skip this step.)
Bulk import expects vectors, not raw text, so the first step is converting each bird article into a 1024-dimensional embedding. The loop below batches articles into groups of 96 and sends each batch to Pinecone's hosted inference API using the
model.
tells the model these are documents being indexed (as opposed to queries), and
handles articles that exceed the model's context window.
EMBED_MODEL = "multilingual-e5-large"
EMBED_DIM = 1024
BATCH_SIZE = 96

embeddings = []
for i in tqdm(range(0, len(df), BATCH_SIZE), desc="Embedding"):
    batch = df["text"].iloc[i : i + BATCH_SIZE].tolist()
    res = pc.inference.embed(
        model=EMBED_MODEL,
        inputs=batch,
        parameters={"input_type": "passage", "truncate": "END"},
    )
    embeddings.extend([item["values"] for item in res.data])
Write Parquet files to S3, partitioned by namespace:
def upload_to_s3(df, bucket, folder, chunk_size=10):
    s3_client = boto3.client("s3")
    for i, start in enumerate(range(0, len(df), chunk_size)):
        chunk = df.iloc[start : start + chunk_size]
        buf = BytesIO()
        chunk.to_parquet(buf, index=False)
        buf.seek(0)
        key = f"{folder}/part-{i}.parquet"
        s3_client.put_object(Body=buf, Bucket=bucket, Key=key)
Each Parquet file contains three columns:
,
(the embedding), and
(a JSON object). The S3 folder structure maps directly to namespaces -- files under
load into
.
Start the import:
op = index.start_import(
    uri=f"s3://{bucket_name}/{folder_name}",
    integration_id="<your-integration-id>",
    error_mode="ABORT"
)
print(f"Import started: {op.id}")
The job runs asynchronously. Check status in the console or via
:
index.describe_import(id=op.id)
Once complete, query as normal:
query_response = pc.inference.embed(
    model=EMBED_MODEL,
    inputs=["birds that migrate south in winter"],
    parameters={"input_type": "query", "truncate": "END"},
)
results = index.query(
    namespace="namespace1",
    vector=query_response.data[0]["values"],
    top_k=3,
    include_metadata=True
)
for match in results.matches:
    print(f"{match.score:.4f}  {match.metadata['bird_name']}")
What this scales to
The bird corpus is small by design -- it's a runnable example. The same pattern handles datasets that are orders of magnitude larger. A single import operation supports up to 1 TB of data or 100 million records across up to 100 namespaces. The setup is identical regardless of scale: configure a storage integration for S3, GCS, or Azure Blob Storage, format data as Parquet files organized by namespace, and call
.
One constraint: bulk import doesn't work on indexes with a schema definition, including full-text search and integrated embedding indexes. Use the documents upsert API for those.
Get started
Full pricing, limits, and storage integration setup are in the
docs
.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
