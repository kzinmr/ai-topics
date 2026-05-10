---
title: "Pinecone serverless on AWS is generally available"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/serverless-generally-available/"
scraped: "2026-05-10T01:27:05.461886+00:00"
lastmod: "2024-08-28T21:13:21Z"
type: "sitemap"
---

# Pinecone serverless on AWS is generally available

**Source**: [https://www.pinecone.io/blog/serverless-generally-available/](https://www.pinecone.io/blog/serverless-generally-available/)

←
Blog
Pinecone serverless on AWS is generally available
Elan Dekel
May 21, 2024
Product
Share:
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
Pinecone serverless is a completely reinvented
vector database
that lets you easily build fast and accurate GenAI applications at a substantially lower cost. Since the
public preview announcement
, more than 20,000 companies have already started building with Pinecone serverless, and collectively indexed over 12
billion
embeddings on the new architecture.
Today, we’re announcing the general availability of Pinecone serverless on AWS. We’re also introducing Private Endpoints for
AWS PrivateLink
(public preview) to users on the Enterprise plan for advanced security.
“Pinecone serverless isn't just a cost-cutting move for us; it is a strategic shift towards a more efficient, scalable, and resource-effective solution.”
— Jacob Eckel, VP, R&D Division Manager, Gong
AI applications require on-demand access to relevant and vast knowledge
To build remarkable AI applications quickly, you need the ability to store vast amounts of knowledge from your company or your customers in the form of
vector embeddings
, and search through it with fast, accurate, and efficient
vector search
.
First, this makes your AI applications generate better results. With
Retrieval Augmented Generation (RAG)
, our
research
shows that the more vector data you can store and search for relevant context, the better the answer quality —even reducing unhelpful or hallucinated answers from state-of-the-art models by 50% or more. In classification use cases such as automated labeling or threat detection, comparing data against the entire catalog and not just curated subsets drastically improves accuracy and speed. For discovery use cases, it lets you find relevant items from a larger pool of options in fewer steps, reducing overall latency and improving recommendations.
Second, this helps you find the killer AI application for your business sooner. To experiment with many different use cases, generative models,
embedding models
, and data processing techniques such as
chunking
, you need a database or a “vector store” to effortlessly load large amounts of vectors without ever worrying about capacity limits, resource management, ballooning costs, or degraded performance.
Pinecone serverless gives you this capability with an unmatched combination of performance, cost-efficiency, and relevance at any scale.
New architecture and algorithms for fast and accurate vector search at any scale with up to 50x lower cost
Pinecone serverless write path architecture
Pinecone serverless read path architecture
To help you store and search through an unrestricted volume of knowledge both during experimentation and in mission-critical production applications, we architected a completely new vector database:
Separation of reads, writes, and storage significantly reduces costs for many types and sizes of workloads.
Industry-first architecture with vector clustering on top of object storage provides low-latency, always-fresh vector search over a practically unlimited number of records at a low cost.
Innovative indexing and retrieval algorithms built from scratch to enable fast and memory-efficient vector search from object storage without sacrificing retrieval quality.
Multi-tenant compute layer provides powerful and efficient retrieval for thousands of users on demand. This enables a serverless experience in which developers don’t need to provision, manage, or even think about infrastructure, as well as usage-based billing that lets companies pay only for what they use.
Pinecone serverless latency (P95) for datasets as large as 900M embeddings
Read the technical deep dive
from our CTO, Ram Sriharsha, to learn more about the design decisions, architecture, and performance of Pinecone serverless.
Introducing Private Endpoints for AWS PrivateLink
Private Endpoints for
AWS PrivateLink
is now in Public Preview. It allows secure connectivity from your VPC to your Pinecone index without exposing traffic to the public Internet.
Private Endpoints allows you to:
Reduce risks of VPC resource exposure.
Limit Pinecone access to specific VPCs, enhancing security.
Secure data traffic over Amazon's private network.
Support for Azure Private Link, GCP Private Service Connect, and role-based access control will follow later in the year.
Pinecone Endpoints for AWS PrivateLinks
Learn more about Private Endpoints in the
docs
.
20,000 organizations have used Pinecone serverless to build their AI apps
Pinecone serverless was battle-tested and saw rapid adoption in its four months of Public Preview. More than 20,000 organizations used it to date, with many of them already using it for large-scale, critical workloads with billions of vectors serving millions of customers. AI leaders like
Gong
, Notion, New Relic,
TaskUs
,
You.com
, and
Shortwave
use Pinecone serverless today or are in the process of migrating.
“Notion is leading the AI productivity revolution. Our launch of a first-to-market AI feature was made possible by Pinecone serverless. Their technology enables our Q&A AI to deliver instant answers to millions of users, sourced from billions of documents. Best of all, our move to their latest architecture has cut our costs by 60%, advancing our mission to make software toolmaking ubiquitous.”
— Akshay Kothari, Co-Founder & COO, Notion
"Pinecone has transformed our customer service operations, enabling us to achieve unprecedented levels of efficiency and customer satisfaction. We are prioritizing its serverless architecture to support our diverse portfolio of AI products across multiple regions. With our scale and ambitions, Pinecone is an integral component of our TaskGPT platform.”
— Manish Pandya, SVP of Digital Transformation, TaskUs
“No other vector database matches Pinecone's scalability and production readiness. We are excited to explore how Pinecone serverless will support the growth of our product capabilities.”
— Bryan McCann, CTO & Co-Founder, You.com
The ecosystem around Serverless is also growing fast. Many of the tools you use today are already
available as integrations
, including Anyscale, Amazon Bedrock, Confluent, LangChain, Mistral, Monte Carlo, Nexla, Pulumi, Qwak, Together.ai, Vectorize, and Unstructured. Many more are on the way.
Start building with Pinecone serverless today
Pinecone serverless is now available on AWS in us-west-2, us-east-1, and eu-west-1 regions. More regions, as well as Azure and GCP availability, will come later in the year. It also comes with:
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
Start building on Pinecone serverless for free
using one of our
sample notebooks
. If you’re already using pod-based indexes, you can
migrate your data to serverless indexes for free
.
If you have questions,
ask the community
or
contact us
for help.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
