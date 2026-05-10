---
title: "Four New GA Features for Dedicated Read Nodes That Give Teams More Control and Observability"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/dedicated-read-nodes-ga-features/"
scraped: "2026-05-10T01:27:36.716519+00:00"
lastmod: "2026-04-15T04:01:03Z"
type: "sitemap"
---

# Four New GA Features for Dedicated Read Nodes That Give Teams More Control and Observability

**Source**: [https://www.pinecone.io/blog/dedicated-read-nodes-ga-features/](https://www.pinecone.io/blog/dedicated-read-nodes-ga-features/)

←
Blog
Four New GA Features for Dedicated Read Nodes That Give Teams More Control and Observability
Gavin Johnson
Apr 15, 2026
Product
Share:
Jump to section:
TL;DR
1) Configurable performance versus recall, per query
2) Metrics exporting for production observability
3) Web console experience for day-2 operations
4) Multi-namespace support —  early access
Get started
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Pinecone Dedicated Read Nodes (DRN) are now generally available. For the full story on what DRN is and why it matters, read
Pinecone Dedicated Read Nodes: Now Generally Available
.
DRN gives teams running revenue-critical systems a clear path to consistent low-latency retrieval under sustained load with predictable cost scaling. But once you ship to production, new questions surface: How do I know if I'm over-provisioned? How do I keep multi-tenant workloads isolated? Can I hit a latency target by trading off recall? Without answers, teams either over-spend on capacity they don't need or under-provision and risk latency spikes that hurt conversion.
DRN answers those questions with four new capabilities that give teams deeper control and better observability.
TL;DR
With GA, DRN adds four new production capabilities:
Configurable performance vs. recall
per query
Metrics exporting
for CPU visibility and external observability
A
web console experience
for day-2 operations
Multi-namespace support
— early access
1) Configurable performance versus recall, per query
Not every query needs maximum recall. Some queries require high throughput at cost.
Interactive experiences often require a hard latency budget. Batch jobs may prefer higher recall even if they run slower. Until now, Pinecone has always executed queries at maximum recall.
With GA, DRN adds two query-time parameters:
max_candidates
: an integer cap on how many candidate vectors the search considers
scan_factor
: a float from 0.5 to 4.0 that controls how much of the index Pinecone scans
You can now trade recall for speed per query without changing your index.
A simple mental model:
Lower
scan_factor
scans less of the index, improving throughput and latency, but can lower recall.
Higher
scan_factor
scans more, improving recall, but costs more to compute.
Backwards compatibility stays intact. If you omit these parameters, Pinecone preserves current behavior and runs at maximum recall.
2) Metrics exporting for production observability
You can't run a dedicated serving tier as a black box. You need to answer:
Am I CPU-bound, or over-provisioned?
Do I have a hotspot on one shard?
Should I add replicas, add shards, or switch node type?
With GA, we’ve added CPU utilization visibility for DRN, exposed at the shard level and index level, available:
In the Pinecone console for quick diagnosis
Via the metrics export endpoint for integration with your observability stack
3) Web console experience for day-2 operations
With GA, we’ve added a first-class DRN experience in the Pinecone web console. You can:
See dedicated capacity configuration (shards, replicas, node type)
Track readiness and scaling operations
View key performance and capacity signals, including CPU utilization
4) Multi-namespace support —
early access
Many production architectures use namespaces for multi-tenant isolation. DRN previously supported one namespace per index, which created friction for platforms and ISVs.
DRN’s multi-namespace support (in early access), enables:
Multi-tenant DRN indexes without forcing one index per tenant
Better fit for workloads where tenant sizes vary
A smoother path from On-Demand multi-namespace patterns into DRN without redesign
Multi-namespace indexes will be fully supported in DRN soon. Currently, they are available in early access. So, if you’d like multi-namespace indexes for DRN to be enabled, contact your account rep or file a support ticket in the Pinecone console.
Get started
Running vector retrieval in production means answering hard questions about cost, latency, and isolation. These four capabilities give you the configurability and visibility to answer them confidently.
DRN is now generally available and includes these new capabilities.
Create a DRN index
to get started, or read the
DRN documentation
for configuration details, scaling guidance, and API reference.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
