---
title: "Pinecone serverless is now generally available on Google Cloud, adding knowledge to AI assistants and other applications"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/gcp-serverless-ga/"
scraped: "2026-05-10T01:27:41.860045+00:00"
lastmod: "2024-08-27T10:03:26Z"
type: "sitemap"
---

# Pinecone serverless is now generally available on Google Cloud, adding knowledge to AI assistants and other applications

**Source**: [https://www.pinecone.io/blog/gcp-serverless-ga/](https://www.pinecone.io/blog/gcp-serverless-ga/)

←
Blog
Pinecone serverless is now generally available on Google Cloud, adding knowledge to AI assistants and other applications
Anshum Garg
Aug 27, 2024
Product
Share:
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
As we work to make generative AI easily accessible, I am pleased to announce that the Pinecone serverless vector database is generally available (GA) on Google Cloud and Google Cloud Marketplace. Along with AWS and Azure, you can now build with serverless on the cloud and region that suits you best.
Enterprise-grade AI needs to be accurate, scalable, and secure for mission-critical workloads. That’s why on top of our industry-leading vector database we're introducing new features to give you greater control and protection over your data. This includes backups for serverless indexes and more granular access controls.
Build knowledgable AI with Pinecone serverless
Get started
Grounding your AI with Pinecone serverless for better outcomes
With our vector database at the core, Pinecone grounds AI applications in your company’s proprietary data. When developers build these knowledgeable applications, they are more accurate and reliable, and lead to better outcomes. Pinecone serverless helps organizations by providing:
A fully-managed developer experience:
No need to provision, manage, or even think about infrastructure when building and deploying your AI applications
High-quality results at any scale:
Proprietary algorithms provide AI applications with highly-relevant and fresh results as your data changes and grows
Fast and cost-effective vector search:
Only pay for what you use with a cloud-native decoupled compute and storage architecture
Read the technical deep-dive
from our VP of R&D, Ram Sriharsha, to learn more about the design decisions, architecture, and performance of Pinecone serverless.
Building faster and better GenAI with Pinecone and Google Cloud
Since first launching serverless, over 30,000 organizations have collectively indexed over 25 billion embeddings for use cases ranging from AI search to classification and model training to building powerful AI assistants. With GA, enterprises like Cisco, Inkeep, and Intuist.AI are moving from prototype to production.
“​​At Cisco, we’re not only integrating generative AI capabilities throughout products for our customers, we’re also enabling our employees with the most cutting-edge technologies like Pinecone. By leveraging Pinecone’s industry-leading vector database on Google Cloud, our enterprise platform team built an AI assistant that accurately and securely searches through millions of our documents to support our multiple orgs across Cisco.” - Sujith Joseph, Principal Engineer, Enterprise AI & Search at Cisco
To make it even easier for customers to leverage the Pinecone serverless database and easily create knowledgeable AI assistants, recently we released
Pinecone Assistant
as a managed service on Google Cloud. Pinecone Assistant delivers high-quality and dependable answers for text-heavy technical data such as financial and legal documents. Through a simple API, all the infrastructure, operations, and optimization of a complex Q&A system are handled for you.
“Bringing Pinecone’s serverless vector database to Google Cloud Marketplace will help customers quickly deploy, manage, and grow the platform on Google Cloud's trusted, global infrastructure. Pinecone customers can now easily build knowledgeable AI applications securely and at scale as they progress their digital transformation journeys.” - Dai Vu, Managing Director, Marketplace & ISV GTM Programs at Google Cloud
Protecting your data with Backups for serverless
Today we are introducing
backups for serverless indexes
to enable seamless backup and recovery of your data. Available to all Standard and Enterprise users, these features allow you to:
Protect your data from system failures or accidental deletes.
Revert bad updates or deletes and restore an index to a known, good state.
Meet compliance requirements (e.g., SOC 2 audits).
You can manually backup and restore your serverless indexes via the Pinecone console. Backups for serverless are now in public preview for all three clouds.
Create and view your serverless backups under ‘Backups’ within the Pinecone console.
More granular access controls
We are also announcing API Key Roles in early access to enable Project Owners to set granular access controls – NoAccess, ReadOnly, or Read/Write – for both the Control Plane and Data Plane within Pinecone serverless.
API Key Roles let you set granular access controls within the control and data planes.
We’ll be introducing more User Roles at the Organization and Project levels in the coming weeks. Organization-level User Roles including Org Owner, Billing Admin, Org Manager, and Org Member will let you determine access to managing projects, billing, and other users in the organization. Project-level User Roles including Project Owner, Project Editor, and Project Viewer will let you determine access to API keys, the Control and Data planes, and other users in the project.
Simplifying large-scale data ingestion with import from object storage
Finally, we are introducing the ability to bulk import from object storage for Pinecone’s serverless infrastructure. This new capability makes ingesting large amounts of data more efficient with up to 6x lower costs compared to the equivalent upsert-based process.
It also streamlines development for developers wanting to build accurate, secure, and large scale (e.g. >100M records) AI applications, onboard a known or new tenant, or migrate an entire production workload from another data store to Pinecone. Import from object storage is currently available in early access, with public preview coming soon.
Start building with Pinecone serverless today
Pinecone serverless on Google Cloud is available for all Standard and Enterprise customers and currently supports Google Cloud’s 'us-central1' (Iowa) and ‘europe-west4’ (Netherlands), with more regions coming soon.
Start building on Pinecone serverless
using one of our
sample notebooks
or subscribe through
Google Cloud Marketplace
. If you have questions,
ask the community
or
contact us
for help.
Additional customer quotes
“Pinecone serverless on multiple regions and cloud providers, especially Google Cloud, has been incredible for us. Being able to integrate our AI search and support copilots on Google Cloud and our customer’s Google Cloud environments has been key to our infrastructure as we continue to grow. We’ve been able to scale our high-volume, high-throughput indexing workloads while delivering high quality and low latency performance.” - Nick Gomez, Founder and CEO, Inkeep
“At intuist.ai, we sought the finest vector database provider for our cutting-edge RAG (Retrieval-Augmented Generation) system tailored for enterprises. In the fall of 2023, we chose Pinecone, and it was undoubtedly one of our best decisions. Pinecone stands out as a best-in-class provider, characterized by its responsiveness and relentless pursuit of excellence. Their transition to a serverless architecture exemplifies their commitment to innovation and performance. With Pinecone, we are empowered to deliver unparalleled service to our clients, ensuring that our RAG system remains at the forefront of technological advancement.” - Johri Dhanotra, CEO and Founder at intuist.ai
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
