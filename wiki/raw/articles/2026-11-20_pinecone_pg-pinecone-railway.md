---
title: "pg_pinecone now deploys on Railway in one click"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/pg-pinecone-railway/"
scraped: "2026-11-20T06:00:37.914965+00:00"
lastmod: "2026-11-18T16:00:02Z"
type: "sitemap"
---

# pg_pinecone now deploys on Railway in one click

**Source**: [https://www.pinecone.io/blog/pg-pinecone-railway/](https://www.pinecone.io/blog/pg-pinecone-railway/)

←
Blog
pg_pinecone now deploys on Railway in one click
Gavin Johnson
Nov 18, 2026
Product
Share:
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
With pgvector, the HNSW graph index needs more memory as a table grows, which makes vector search in Postgres increasingly expensive to run. The
pg_pinecone Postgres extension
has lower latency than pgvector at the same recall and uses less memory, so it costs less to run as tables grow. The new
Railway template
for pg_pinecone gives developers Postgres with Pinecone's vector search built in, deployed in one click.
The Railway template runs Postgres 18 with pg_pinecone installed, preloaded, and enabled, so there's no extension to install or image to build. In our benchmarks on 1 million vectors, the pg_pinecone index was about 15 times smaller than a pgvector HNSW index using halfvec and returned results faster at the same recall. Railway bills for the memory and storage a service uses, so a smaller index lets the same Postgres service hold many more vectors for the same cost. When a table needs to scale, a Pinecone API key and one SQL call
move its search
to a serverless index in Pinecone's managed service, and another call moves it back. Wherever the vectors are stored, queries don't change.
The pg_pinecone template is available now in Railway's template marketplace, and the pg_pinecone extension is
open source
under Apache 2.0. The
native
engine, pg_pinecone's default, runs inside Postgres and needs no Pinecone account.
To get started, deploy the
template
on Railway, or read the
pg_pinecone quickstart
.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
