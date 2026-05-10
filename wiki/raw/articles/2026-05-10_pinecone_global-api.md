---
title: "Going Global: Building the Global Control Plane API"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/global-api/"
scraped: "2026-05-10T01:27:24.079334+00:00"
lastmod: "2024-04-22T16:15:03Z"
type: "sitemap"
---

# Going Global: Building the Global Control Plane API

**Source**: [https://www.pinecone.io/blog/global-api/](https://www.pinecone.io/blog/global-api/)

←
Blog
Going Global: Building the Global Control Plane API
Gareth Jones
,
Jack Pertschuk
Apr 22, 2024
Engineering
Share:
Jump to section:
Evolving the control plane
Going Global
Start Building Today
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
We built the
Global Control Plane API
to make it even easier to build and scale with Pinecone. It uses a global URL for all control plane operations (e.g.,
list indexes
,
create indexes
,
list collections
), regardless of cloud environment.
Launched in preview alongside
Pinecone serverless
, we’ve continued to iterate and make improvements, and are excited to announce that the Global Control Plane API is now generally available (GA) to all users.
In this blog, we share the motivations and engineering efforts behind our transition from the regional (or legacy) control plane API to the new global API, and show you how to get started.
Note: The legacy version of the API, which requires regional URLs for control plane operations, is deprecated as of April 15, 2024 and will be removed in a future, to be announced, release. We recommend
migrating to the new API
as soon as possible.
Evolving the control plane
Users have a set of control plane endpoints to interact with and create instances of Pinecone. In the legacy API, each environment has its own endpoint for managing projects, indexes, collections, and API keys, independent of other environments. Because of this architecture, each project is restricted to a single environment and region. Any resources and data that the user creates or uploads are forever scoped to that environment, and users who need to manage resources in multiple environments have to create and keep track of separate projects and API keys for each region in which they use Pinecone.
In the legacy API, each project is restricted to a single environment and region.
We initially chose to build region-scoped APIs for fault tolerance. Since all the API calls go directly to the regional endpoint where the customer’s data lives, an outage in a single cloud or region wouldn't impact customers in other regions.
Over time, however, it became clear that region-scoped endpoints resulted in a poor user experience. Many of our users manage resources for different use cases such as development, staging, and production across many geographies. This makes it difficult for them to maintain visibility and control over all resources in Pinecone. Additionally, the regional scope of Pinecone’s legacy control plane made it difficult to implement commonly requested features such as multi-region indexes that involved sharing data and resources between geographies or environments.
We determined there was a critical demand for a more integrated and transparent approach to project and resource management across various environments and regions.
Going Global
To address the challenge of managing resources across multiple Pinecone environments and projects, we developed a new global control plane API —
api.pinecone.io
. The global API eliminates the need for per environment endpoints and allows users to access resources from multiple environments with the same API key.
The new, global API uses a global URL for all control plane operations regardless of cloud environment.
Note: The legacy environment endpoints are now deprecated and will be removed in a future release, but will continue to be available until then. New features will only be supported by the new global control plane API.
Despite moving control plane operations to a single global URL, we wanted to maintain some advantages of the legacy regional API, such as:
Fault tolerance and reliable service
Secure credential storage
Low latency to clients globally
We needed to back our new API with a database that provided high availability and geographical replication out of the box. For this purpose, we chose
Google Cloud Spanner
, which also gives us the ACID-compliant transactions and durability required to enforce quotas, uniqueness constraints, and safely persist user metadata.
Improving the developer experience was another key objective. By deploying a globally replicated, highly available Rust API server backed by Cloud Spanner, we are able to serve traffic with minimal latency, no matter where users are located. The best part of this is that users don’t have to take any special steps — requests to
api.pinecone.io
are automatically routed to the nearest API server via Google Cloud’s
global load balancer
. We also made a handful of usability improvements to the new API, including:
Eliminating inconsistent naming conventions
Updating API response types to simplify new features
Implementing more accurate and standardized errors
Start Building Today
The Global API is currently supported within our Python, Node, and Java
clients
. View the
quickstart
to start building today, or check out the
migration guide
to upgrade to the new API.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
