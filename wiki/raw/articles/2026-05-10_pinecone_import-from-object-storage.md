---
title: "Introducing import from object storage for more efficient data transfer to Pinecone serverless"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/import-from-object-storage/"
scraped: "2026-05-10T01:27:37.737388+00:00"
lastmod: "2024-10-29T14:16:30Z"
type: "sitemap"
---

# Introducing import from object storage for more efficient data transfer to Pinecone serverless

**Source**: [https://www.pinecone.io/blog/import-from-object-storage/](https://www.pinecone.io/blog/import-from-object-storage/)

←
Blog
Introducing import from object storage for more efficient data transfer to Pinecone serverless
Ben Esh
,
Gibbs Cullen
Sep 24, 2024
Product
Share:
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Today we are introducing the ability to bulk import from object storage for Pinecone’s serverless infrastructure. This new capability makes ingesting large amounts of data more efficient for developers building accurate, secure, and scalable AI applications.
Build knowledgeable AI
Get started
Simplifying large scale data ingestion
I
mport from object storage
provides a simple and efficient way of transferring and indexing your initial workload into Pinecone. This streamlines development if you want to run a POC at a large scale (e.g. 100M records), onboard a known or new tenant, experiment with new embedding models, or migrate an entire production workload from another data store to Pinecone.
With import from object storage, you get:
Up to 6x lower cost
: Save up to 6x in initial ingest costs compared to the equivalent upsert-based process. Experiment at production-scale knowing you won’t break the bank. For example, ingesting 10M records of 768-dimension will cost $30 with bulk import.
Streamlined development
: Ingest up to billions of
records
with significantly less overhead than the equivalent upsert-based process. As an asynchronous, long-running operation, there’s no need for performance tuning or monitoring the status of your import operation. Just set it and forget it; Pinecone will handle the rest.
Note: Imports are limited to 100M records at a time during public preview.
Easier experimentation
: Import from object storage enables your team to iterate faster and focus on ways to optimize performance. Experiment with new models, continuously fine-tune existing embedding models, or test out index configurations with minimal setup and operational overhead.
Secure access and control:
Data is read from a secure bucket in your object storage. This means you have control over who has access to your data, and you can revoke Pinecone’s access at any time.
from pinecone import Pinecone
pc = Pinecone(api_key='YOUR_API_KEY')

index = pc.Index("target_index") 
index.start_import(
  integration_id="secure-integration-id",
  url="s3://bucket/path/to/dir/"
)
Initiate a new import request
from object storage (e.g. Amazon S3) with a few lines of code.
Experiment and build at production scale today
To get started, you first need to
integrate your object store
(e.g. Amazon S3) with Pinecone. Pinecone’s storage integrations let you store IAM credentials for your object store and can be set up or managed via the Pinecone console.
Import is done from a
new API endpoint
that supports Parquet source files. This makes it easy to ingest large datasets stored in object storage. These import operations are restricted to writing records into a new serverless namespace; you cannot import data into an existing namespace.
Easily set up the storage integration in the Pinecone console, then send an import request. Import requests are asynchronous, long-running operations so you can set it and forget it.
Import from object storage is now available in public preview for Standard and Enterprise users at a flat rate of $1.00/GB. It is
currently limited to Amazon S3
for serverless AWS regions. Support for Google Cloud Storage (GCS) and Azure Blob Storage will follow in the coming months. See our
documentation
to learn more, test it out in our
example notebook
, and
start building today
.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
