---
title: "Vector-to-document index conversion is now available"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/index-conversion/"
scraped: "2026-11-20T06:00:37.342041+00:00"
lastmod: "2026-11-17T16:00:01Z"
type: "sitemap"
---

# Vector-to-document index conversion is now available

**Source**: [https://www.pinecone.io/blog/index-conversion/](https://www.pinecone.io/blog/index-conversion/)

←
Blog
Vector-to-document index conversion is now available
Gavin Johnson
Nov 17, 2026
Product
Share:
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Until now, adding
full-text search
to a
legacy vector index
meant re-importing every record into a
document index
. At hundreds of millions of records, that re-import became a project that took planning and effort to execute. With
vector-to-document index conversion
, Pinecone builds a new document index in one conversion job while the legacy vector index keeps serving traffic. Teams can now run full-text search on the data already in Pinecone without a re-import.
Start a conversion job from the Pinecone console or API, and choose which metadata fields become full-text search fields. Vectors, record IDs, namespaces, and all other metadata fields copy over unchanged. Nothing is re-embedded. In an internal test, 100 million records were converted from a legacy vector index to a document index in under 20 minutes. The document index serves both full-text search and vector search queries, with no second search system needed. To switch to a document index: 1) run the index conversion, 2) replay any writes made during the job (or pause writes until you switch), and 3) update your code so that all search and write calls use the Documents API.
Index conversion is available on the Standard and Enterprise plans for serverless vector indexes. Legacy vector indexes that use integrated embedding can be converted to a document index that uses
integrated embedding
. Conversion is billed at the bulk import rate of $0.25 per GB of data in the legacy vector index.
To get started, convert an index from the console, or read the
index conversion docs
.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
