---
title: "May Monthly Product Update"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/may2024-monthly-product-update/"
scraped: "2026-05-10T01:27:46.846093+00:00"
lastmod: "2024-06-04T14:17:00Z"
type: "sitemap"
---

# May Monthly Product Update

**Source**: [https://www.pinecone.io/blog/may2024-monthly-product-update/](https://www.pinecone.io/blog/may2024-monthly-product-update/)

←
Blog
May Monthly Product Update
Xian Huang
Jun 3, 2024
Product
Share:
Jump to section:
Pinecone   serverless is generally available on AWS
Secure your AI applications with Private Endpoints
SDK updates: Improved RAG management and ingestion speed
Streamline development with Github Copilot and more integrations
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
This month, we welcomed the
general availability
of Pinecone serverless on AWS, the public preview of
Private Endpoints
for AWS PrivateLink, and a fast-growing list of new integrations. Check out some of our product highlights below or read the full
release notes
.
Pinecone
serverless is generally available on AWS
Pinecone serverless
reinvented
vector databases for fast, accurate vector search at any scale with up to 50x lower costs. Serverless is currently available on AWS in us-west-2, us-east-1, and eu-west-1 regions, with more regions and support for Azure and GCP coming later in the year. Pinecone serverless also comes with:
A new
Global Control Plane API
that simplifies operations across cloud environments
New SDKs for
Python
,
Node
, and
Java
New integrations with
Pulumi
,
Terraform
, and
Spark
Join developers from more than 20,000 organizations like
Gong
, Notion, and
Shortwave
and
start building on serverless for free
. If you’re already using pod-based indexes, you can
migrate your data to serverless indexes for free
.
Secure your AI applications with Private Endpoints
Enterprise users can now easily
enable Private Endpoints
for AWS PrivateLink. In addition to
encryption
at rest and in transit, Private Endpoints provides additional security by ensuring that your data traffic traverses the AWS network without public internet exposure.
Enabling Private Endpoints for AWS PrivateLink
Private Endpoints also reduces the risk of exposing your VPC resources to the Internet (or other outside networks) through a misconfiguration, and minimizes the risk of unauthorized access to your Pinecone indexes.
SDK updates: Improved RAG management and ingestion speed
The Java client (
v1.2.0
) now supports list record IDs
in a namespace
and
with a common ID prefix
. ID prefixes enable you to query segments of content, which is especially useful for
managing RAG applications
where you often need to chunk large documents into smaller segments. This feature is also supported in the
Node Js
(v2.1.0 and later)
Python
client (v3.1.0 and later).
Our Python client (
v4.0.0
and later) improves your vector upsert throughput by 3x. This is a breaking change if you use the optional GRPC addon (
installed with
pinecone-client[grpc]
).
Streamline development with Github Copilot and more integrations
We’re rapidly expanding our ecosystem to help you streamline your AI application development. You can now access the
Pinecone Copilot Extension
through our
GitHub Marketplace listing
to get personalized recommendations. Get started now with
this demo
.
Other new integrations you can use include data sources
Apify
,
Estuary
,
Flowise
,
Unstructured
, and
StreamNative
, frameworks like
Contex Data
and
OctoAI
, models like
Jina AI
and
Voyage AI
, and observability tools such as
Traceloop
.
Check out the
release notes
for a running list of all product and feature releases. If you’re new to Pinecone,
try it out
for free today.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
