---
title: "New Bulk Data Operations: Update, Delete, and Fetch by Metadata"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/update-delete-and-fetch-by-metadata/"
scraped: "2026-05-10T01:27:17.120199+00:00"
lastmod: "2025-10-30T16:09:03Z"
type: "sitemap"
---

# New Bulk Data Operations: Update, Delete, and Fetch by Metadata

**Source**: [https://www.pinecone.io/blog/update-delete-and-fetch-by-metadata/](https://www.pinecone.io/blog/update-delete-and-fetch-by-metadata/)

←
Blog
New Bulk Data Operations: Update, Delete, and Fetch by Metadata
Lea Wang-Tomic
,
Gavin Johnson
Oct 30, 2025
Product
Share:
Jump to section:
Manage Your Data by Metadata
Common Use Cases
Getting Started
Our New by Metadata Operations Today
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Today, we’re announcing the addition of three bulk data operations to Pinecone Database:
Update
by Metadata,
Delete
by Metadata,
and
Fetch
by Metadata
. Instead of collecting record IDs first, you can target any subset of data using the same filter syntax you use in queries, making everyday tasks such as bulk updates, data purges, and selective fetches simpler and more efficient.
As data scales, metadata becomes essential for enabling functionality and maintaining performance. A recommendation isn’t very good if you can’t filter down to the specific data that’s relevant to the user, and the ability to filter your data accurately and efficiently is almost always reliant on metadata. A single attribute, such as
,
, or
, can identify the exact corpus of relevant records precisely in a much easier way than collecting vector IDs. Update, delete, and fetch by metadata bring scalability to data management, allowing you to modify or retrieve millions of records accurately and efficiently using the metadata you already maintain.
Manage Your Data by Metadata
The new operations leverage the same familiar filter syntax used in metadata-based queries. You define a filter based on your record’s metadata and pass it directly to the
,
, or
methods.
Pinecone then performs the requested action on all records matching the filter, making bulk data operations incredibly easy and efficient, even if you’re modifying millions of records at once.
Common Use Cases
Filtering by metadata allows you to target subsets of data based on attributes. As your data scales, this becomes a very effective way to organize and manage your data. These new operations – update, delete, and fetch by metadata – are designed for common data management scenarios, including:
Bulk Updates:
Replace multi-step update scripts with a single command. Instantly backfill new embeddings by targeting metadata like model_version: "
" without fetching IDs first.
Data Purges:
Honor Right to be Forgotten requests (GDPR) with one API or SDK call. Reliably purge all data for a specific
to ensure compliance, simplifying an increasingly common and important operation.
Selective Fetches:
Stop over-fetching. Retrieve specific subsets of vectors, such as those matching a
, with a single filtered fetch. This means smaller payloads, lower latency, and more accurate fetches.
Data Cleanup:
Easily prune stale records. A single command can delete all data from a deprecated source or a finished A/B test by filtering on metadata like source: "
", making index cleanup fast and scriptable.
Getting Started
Integrating these new operations into your existing pipeline is simple. Since they use the same filter syntax as queries, there’s no new query language to learn.
Here’s a quick example of how to use update, delete, and fetch by metadata:
# pip install "pinecone"
from pinecone.grpc import PineconeGRPC as Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")

# Get the unique host for an index
index = pc.Index(host="INDEX_HOST")

# Delete records from your index by metadata
index.delete(
    namespace="example-namespace",
    filter={
        "genre": {"$eq": "documentary"}
    }
)
Note:
update and fetch are not fully launched for General Availability yet and require direct API calls with specific version headers (
and
respectively). They don't yet have Python SDK support.
# To get the unique host for an index,
# see https://docs.pinecone.io/guides/manage-data/target-an-index
PINECONE_API_KEY="YOUR_API_KEY"
INDEX_HOST="INDEX_HOST"

# Update by metadata
curl "https://$INDEX_HOST/vectors/update" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H 'Content-Type: application/json' \
    -H "X-Pinecone-API-Version: unstable" \
    -d '{
            "dry_run": true,
            "namespace": "example-namespace",
            "filter": {
                "document_title": {"$eq": "Introduction to Vector Databases"}
            },
            "setMetadata": {
                "author": "Del Klein"
            } 
        }'


# Fetch by Metadata 
curl -X POST "https://$INDEX_HOST/vectors/fetch_by_metadata" \
  -H 'Api-Key: $PINECONE_API_KEY' \
  -H 'Content-Type: application/json' \
  -H "X-Pinecone-API-Version: 2025-10" \
  -d '{
    "namespace": "example-namespace",
    "filter": {"rating": {"$lt": 5}},
    "limit": 2
  }'
Our New by Metadata Operations Today
Update, delete, and fetch by metadata bring a new level of scalability and efficiency to your data management. It isn’t just a quality-of-life improvement; it’s a fundamental enhancement to how you can interact with and control your data at scale.
Delete by metadata
is generally available,
update by metadata
is available in public preview, and
fetch by metadata
is available in early access (i.e., we will be adding additional functionality to fetch, including pagination, in the upcoming months).
Read the
update
,
delete
, and
fetch
by metadata documentation for more information on how to get started with each.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
