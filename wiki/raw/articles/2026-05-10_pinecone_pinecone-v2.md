---
title: "Pinecone 2.0: Take Vector Search from the Lab to Production"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/pinecone-v2/"
scraped: "2026-05-10T01:27:14.272459+00:00"
lastmod: "2023-08-09T15:11:24Z"
type: "sitemap"
---

# Pinecone 2.0: Take Vector Search from the Lab to Production

**Source**: [https://www.pinecone.io/blog/pinecone-v2/](https://www.pinecone.io/blog/pinecone-v2/)

←
Blog
Pinecone 2.0: Take Vector Search from the Lab to Production
Edo Liberty
Sep 14, 2021
Product
Share:
Jump to section:
Single-Stage Filtering
Hybrid Storage
Other Updates
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Pinecone 2.0 helps companies move
vector similarity search
from R&D labs to production applications. The fully managed vector database now comes with metadata filtering for
greater control over search results
and
hybrid storage for up to 10x lower costs
.
This update also includes a new REST API for ease of use, a completely new architecture for maximum reliability and availability, and a completed SOC2 Type II audit for enterprise-grade security.
Single-Stage Filtering
Store metadata with your vector embeddings, and limit the vector similarity search to embeddings that meet your metadata filters.
In many cases, you want to combine a vector similarity search with some arbitrary filter to provide more relevant results. For example, doing a semantic search on a corpus of documents but only from certain categories, or excluding certain authors.
In the past, you had two options: The first was pre-filtering, which first filters records by metadata and then must use an inefficient brute-force search through the remaining vectors. The second was post-filtering, where you would first retrieve a large set of nearest neighbors and then apply metadata filters on the results. In that case there is a high latency penalty for retrieving more items than needed, and there is no guarantee the result set would include all the items you actually want.
For the many companies that require filtering in their search, there was no good option. It’s no wonder vector search has been stuck in R&D labs.
The metadata filtering introduced in Pinecone v2.0 provides the fine-grained control over vector search results that many search and recommendation applications require, at the ultra-low latencies their users expect. Get the power of vector search with the control of traditional search. It accepts arbitrary filters on metadata and retrieves exactly the number of nearest-neighbor results that match the filters. For most cases the search latency will be even lower than unfiltered searches.
For example, suppose you want to search through vector embeddings of documents (i.e., semantic search), but only want to include documents labeled as “finance” from this year. You can add the metadata to those document embeddings within Pinecone, and then filter for those criteria when sending the query. Pinecone will search for similar vector embeddings only among those items that match the filter.
See documentation for metadata filtering.
Hybrid Storage
Vector searches typically run completely in-memory (RAM). For many companies with over a billion items in their catalog, the memory costs alone could make vector search too expensive to consider. Some vector search libraries have the option to store everything on disk, but this could come at the expense of search latencies becoming unacceptably high.
Pinecone 2.0 introduces a hybrid configuration, in which a compressed
vector index
is stored in memory and the original, full-resolution vector index is stored on disk. The in-memory index is used to locate a small set of candidates to search within the full index on disk. This method provides the same fast and accurate search results yet
cuts infrastructure costs by up to 10x
.
Other Updates
New Architecture
Pinecone now provides fault tolerance, data persistence, and high availability for customers with billions of items and many thousands of operations per second.
Before, enterprises with strict reliability requirements either had to build and maintain complex infrastructure around vector search libraries to meet those requirements or relax their standards and risk downgraded performance for their users.
Now, the Pinecone platform has been re-architected to use Kafka ingestion and Kubernetes orchestration, in a cloud-native paradigm which separates the read and write paths and disassociates storage and compute. This makes Pinecone’s vector database as reliable, flexible, and performant as top-tier enterprise-grade cloud databases.
REST API and Python Client
Pinecone now uses a new
REST API
based on the OpenAPI spec. This makes Pinecone more flexible and even easier to use for developers from any system and in any language.
Upsert and query vectors using HTTPS and JSON without the need to install anything. The REST API gives you maximum flexibility to use the Pinecone service from any environment that can make HTTPS calls. No need to be familiar with Python.
For users who prefer Python, the Python client has been rebuilt to use the new API and to use fewer dependencies. Clients for Go and Java are coming soon.
This update also comes with a completely revamped
documentation portal
to make developing with Pinecone even easier.
SOC2
Pinecone is now SOC2 Type II audited, with certification expected soon. Enterprises with even the strictest security requirements can deploy Pinecone to production with confidence and assurance that their data is safe.
Learn how we keep your data secure
, such as regularly performing third-party penetration tests, keeping data in isolated containers, encryption, and more.
Whether you’re already experimenting with vector search or just learning about it, Pinecone 2.0 makes it quicker, easier, and more cost-effective to bring vector search into production applications than ever before.
Pinecone 2.0 is available now by request.
Contact us
with questions or
request a free trial
today. It will be generally available to all users within a few weeks. Learn all about the new features and ask us questions in a live webinar,
Introduction to Pinecone 2.0
.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
