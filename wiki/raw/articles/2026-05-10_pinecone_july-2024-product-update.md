---
title: "July 2024 Product Update"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/july-2024-product-update/"
scraped: "2026-05-10T01:27:31.082626+00:00"
lastmod: "2024-08-01T11:47:15Z"
type: "sitemap"
---

# July 2024 Product Update

**Source**: [https://www.pinecone.io/blog/july-2024-product-update/](https://www.pinecone.io/blog/july-2024-product-update/)

←
Blog
July 2024 Product Update
Xian Huang
Aug 1, 2024
Product
Share:
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
This month we expanded Pinecone serverless to Google Cloud Platform (GCP) and Microsoft Azure, launched Pinecone Inference, and introduced API versioning. Learn more below and in our monthly
release notes
.
Pinecone serverless is now available on Azure and GCP
Pinecone serverless is
now available in public preview on Azure and GCP
. During the public preview period, serverless indexes on Azure and GCP are limited to Standard and Enterprise users.
Serverless indexes on AWS
are generally available (GA) to all users.
Over 20,000 organizations, including Notion,
Gong
, and New Relic, have already started building on Pinecone serverless. Get started in minutes using one of our
sample notebooks
.
Start for free with Pinecone Inference API to streamline AI workflow
Build knowledgeable AI applications faster, with less complexity and fewer tools to manage with
Pinecone Inference
. Now in public preview, Pinecone Inference is an API that provides easy and low-latency access to embedding and reranking models hosted on Pinecone’s infrastructure, starting with
multilingual-e5-large
.
Explore our
interactive model gallery
and
start building with Inference
for free today.
API versions for stable development and SDK updates to prevent data loss
We’re adopting a
date-based versioning
approach with quarterly releases. This
allows
us to introduce incremental small changes to minimize interruptions and gives you the ability to plan and manage updates more effectively.
The latest releases for our
Python SDK
(v5.0.0),
Node.js SDK
(v3.0.0), and
Java SDK
(v2.0.0) add the ability to
prevent accidental index deletion
. You can now easily enable deletion protection for both new and existing indexes from the console, APIs, and SDKs to reduce the risk of accidental data loss.
Note that the latest release of our
Java SDK
(v2.0.0) introduces a breaking change. Learn more about how to update your client in the
Java SDK v2.0.0 migration guide
.
Build a multimodal search app in minutes with our new sample app
Our
sample apps
allow you to get end-to-end applications up and running in minutes. Use one npx command line npx create-pinecone-app to clone and set up the project locally and then tailor it to your own purposes. Check out our latest
multimodal search sample app
and jumpstart the development of your own application.
Multimodal search sample app
Use Pinecone Connect to access Pinecone from another platform
Pinecone Connect
, an integration that allows developers to manage Pinecone resources directly from another platform via a simple authentication flow, is generally available. Tech platforms looking to provide direct access to the Pinecone can easily set up the
Pinecone Connect integration
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
