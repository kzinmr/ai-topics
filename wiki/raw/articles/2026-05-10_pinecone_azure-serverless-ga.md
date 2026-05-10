---
title: "Build knowledgeable AI with Pinecone serverless, now generally available on Microsoft Azure"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/azure-serverless-ga/"
scraped: "2026-05-10T01:27:24.833399+00:00"
lastmod: "2024-08-27T10:03:39Z"
type: "sitemap"
---

# Build knowledgeable AI with Pinecone serverless, now generally available on Microsoft Azure

**Source**: [https://www.pinecone.io/blog/azure-serverless-ga/](https://www.pinecone.io/blog/azure-serverless-ga/)

←
Blog
Build knowledgeable AI with Pinecone serverless, now generally available on Microsoft Azure
Jeff Zhu
Aug 27, 2024
Product
Share:
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
As we work to make generative AI easily accessible, I am pleased to announce that the Pinecone serverless vector database is generally available (GA) on Microsoft Azure. Along with AWS and GCP, you can now build with serverless on the cloud and region that suits you best.
Enterprise-grade AI needs to be accurate, scalable, and secure for mission-critical workloads. That’s why on top of our industry-leading vector database we're introducing new features to give you greater control and protection over your data. This includes backups for serverless indexes and more granular access controls.
Build knowledgeable AI with Pinecone serverless
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
Since first launching serverless, over 30,000 organizations have collectively indexed over 25 billion embeddings for use cases ranging from AI search to classification and model training to building powerful AI assistants. Customers large and small have started to see the benefits from and potential for Pinecone serverless.
"Pinecone is an integral part of Wipro's Lab45 AI platform, enabling over 100,000 enterprise users to create knowledgeable custom AI assistants and solutions across HR, sales, marketing, operations, and more. Pinecone’s enterprise-grade features provide the performance, stability, and security we need, and we’re excited to see how Pinecone serverless on Microsoft Azure will further enhance our platform's capabilities.” - Kapil Sharma, VP Product, Wipro
"At Fileread, we are transforming how litigation teams conduct fact-finding. Pinecone on Microsoft Azure enables our AI tools to quickly deliver accurate insights from millions of documents to litigation teams, providing significant value while scaling our clients' caseloads with confidence. Pinecone serverless will go further and allow us to save precious engineering time that we can use to deliver even more results to our clients." - Chan-Hee Koh, Co-Founder and CEO at Fileread
Ship fast, accurate GenAI apps with Pinecone and Azure
With Pinecone’s integration with Azure OpenAI Service, you can build AI applications faster by accessing OpenAI’s models and Pinecone serverless within the same Azure environment. With the addition of our
.NET SDK (V1.0)
to our
growing list of SDKs
, Azure developers have more ways to build with Pinecone.
"With Pinecone serverless, Microsoft Azure customers of any size can reimagine their AI workflows, easily create grounded applications, and improve productivity. Together with Azure OpenAI Service, our customers can streamline their path to production, and deliver fast, secure, and performant AI applications.” - Tom Davis, Partner, Microsoft for Startups
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
Simplifying large scale data ingestion with import from object storage
Finally, we are introducing the ability to bulk import from object storage for Pinecone’s serverless infrastructure. This new capability makes ingesting large amounts of data more efficient with up to 6x lower costs compared to the equivalent upsert-based process.
It also streamlines development for developers wanting to build accurate, secure, and large scale (e.g. >100M records) AI applications, onboard a known or new tenant, or migrate an entire production workload from another data store to Pinecone. Import from object storage is currently available in early access, with public preview coming soon.
Start building with Pinecone serverless today
Pinecone serverless on Microsoft Azure is available for all Standard and Enterprise customers and currently supports Azure 'eastus2' (Virginia) with more regions coming soon.
Start building on Pinecone serverless
using one of our
sample notebooks
or subscribe through the
Azure marketplace
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
