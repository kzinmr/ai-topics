---
title: "On-demand mode for Pinecone BYOC"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/byoc-on-demand/"
scraped: "2026-10-16T06:00:51.629243+00:00"
lastmod: "2026-10-15T12:00:01Z"
type: "sitemap"
---

# On-demand mode for Pinecone BYOC

**Source**: [https://www.pinecone.io/blog/byoc-on-demand/](https://www.pinecone.io/blog/byoc-on-demand/)

←
Blog
On-demand mode for Pinecone BYOC
Scale without sizing every index
Manish Talreja
Oct 15, 2026
Product
Share:
Jump to section:
How on-demand mode works
Security and support
Get started
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Starting today, Pinecone Bring Your Own Cloud (
BYOC
) supports on-demand capacity mode. You can now create indexes without sizing each one in advance. Instead, your on-demand indexes share a capacity pool that can hold millions of namespaces, whether you use one per tenant in your app or one per user of your AI agent. Start with a small pool and add capacity as your data grows.
Pinecone BYOC runs Pinecone inside your own AWS, Google Cloud, or Azure account. Your data stays under your control while Pinecone operates the database. It's a common choice for teams in legal, healthcare, and financial services that need to keep their data in their own cloud environment.
Add a shard to the pool, and new writes fill it while existing data stays in place.
How on-demand mode works
If you run semantic or lexical search for your company, most systems make you choose the number of shards for each index up front. Choose too few and you rebuild the index when it outgrows them. Choose too many and you pay for hardware that sits idle. Adding shards later forces a reshuffle of existing data, and some shards still end up much fuller than others.
In on-demand mode, Pinecone uses dynamic sharding to spread your data evenly across a shared pool. It tracks where each piece of data lives and sends new writes to the shards with the most room. When you need more capacity, you add a shard without moving any existing data. New writes fill it over time, so the pool stays balanced.
If one namespace gets far more queries than the others, you can move it to its own index on
dedicated read nodes
in the same BYOC environment. Your other namespaces keep sharing the on-demand pool.
Security and support
Scaling your on-demand pool keeps the
zero-access BYOC model
. Your vectors, metadata, and queries stay in your cloud account. Pinecone adds capacity without SSH, VPN, inbound network access, or a standing cross-account role.
Pinecone monitors environment health through operational metrics such as CPU and latency, without seeing your data. You can also
monitor your indexes
in the Pinecone console or in your own Prometheus. When you need help troubleshooting, you share logs with Pinecone support.
Get started
On-demand mode is available now for every BYOC customer. If you're new to BYOC, Pinecone's setup wizard generates a deployment project that you run in your cloud account to create your environment. If you already run BYOC, you can create an on-demand index in your existing environment. Pick your BYOC environment as the location in the Pinecone console, API, or SDKs, and choose on-demand as the capacity mode. To plan your deployment, talk with your Pinecone account team or
contact us
.
For setup instructions and more on the architecture and data security model, see the
BYOC guide
.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
