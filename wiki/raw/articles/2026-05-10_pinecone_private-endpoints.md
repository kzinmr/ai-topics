---
title: "Introducing Private Endpoints for Pinecone serverless"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/private-endpoints/"
scraped: "2026-05-10T01:27:02.485803+00:00"
lastmod: "2024-05-23T13:57:04Z"
type: "sitemap"
---

# Introducing Private Endpoints for Pinecone serverless

**Source**: [https://www.pinecone.io/blog/private-endpoints/](https://www.pinecone.io/blog/private-endpoints/)

←
Blog
Introducing Private Endpoints for Pinecone serverless
Anshum Garg
May 21, 2024
Product
Share:
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Demo for enabling Private Endpoints for AWS PrivateLink
Private Endpoints for AWS PrivateLink
is now in public preview for
Pinecone serverless
. Private Endpoints allow you to securely connect to Pinecone while keeping traffic from your VPC (virtual private cloud) private from the public internet.
Secure your AI applications with Private Endpoints
More than 20,000 organizations have used Pinecone serverless since Public Preview. To make their AI applications knowledgeable, these organizations store sensitive, proprietary data such as patient healthcare data, legal agreements, and internal operations data in Pinecone.
In addition to encryption
at rest
and
in transit
, Private Endpoints provides additional security by ensuring that your data traffic traverses the AWS network without public internet exposure. Private Endpoints also reduce the risk of exposing your VPC resources to the Internet (or other outside networks) through a misconfiguration, and minimize the risk of unauthorized access to your Pinecone indexes.
Use Private Endpoints to connect to AWS PrivateLink
You can easily
enable Private Endpoints
within the Pinecone console by following a few simple steps:
First, create an Amazon VPC endpoint in the AWS console for a specific region.
Then authorize the VPC endpoint ID in Pinecone through the
console
. These VPC endpoints route all
data plane
traffic from your AWS VPC to Pinecone’s regional VPC over the AWS network, establishing a secure and private connection.
Once you successfully deploy the endpoints, you can run data plane commands (e.g., upsert data) for your index(es) using the index private endpoint hostname.
Connect to Pinecone securely using AWS PrivateLink.
Private Endpoints are set up for a single region and authorize a specific VPC endpoint. Projects with indexes in multiple regions require a Private Endpoint for each region. Multiple VPC endpoints can be authorized per project if needed. Each organization is limited to ten Private Endpoints per project.
Private Endpoints establish connectivity to indexes in a specific region. Turning off internet access to your project will affect Pinecone indexes that communicate via the internet in the same project.
Start building today
Private Endpoints is now available in Public Preview for all Enterprise users. Support for Private Link on GCP and Azure will be added later in the year.
Learn more
about our support for AWS PrivateLink and Private Endpoints, and
start building today
.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
