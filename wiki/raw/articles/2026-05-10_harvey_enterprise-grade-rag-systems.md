---
title: "Enterprise-Grade RAG Systems"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/enterprise-grade-rag-systems"
scraped: "2026-05-10T01:21:10.717467+00:00"
lastmod: "2025-02-20T23:16:24.389Z"
type: "sitemap"
---

# Enterprise-Grade RAG Systems

**Source**: [https://www.harvey.ai/blog/enterprise-grade-rag-systems](https://www.harvey.ai/blog/enterprise-grade-rag-systems)

Harvey Agents execute legal work end-to-end
Learn more
Harvey Agents execute legal work end-to-end
Learn more
Harvey Agents execute legal work end-to-end
Learn more
→
:Harvey:
Platform
Solutions
Customers
Security
Resources
About
Overview
→
A unified view of how Harvey's products work together to support your entire practice.
Assistant
→
Ask questions, analyze documents, and draft faster with domain-specific AI.
Vault
→
Securely store, organize, and bulk-analyze legal documents.
Knowledge
→
Research complex legal, regulatory, and tax questions across domains.
Workflow Agents
→
Run pre-built Workflow agents or build your own, tailored to your firm's needs.
Harvey Mobile
→
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
→
Access Harvey where you already work and ground every answer in sources you trust.
Harvey Agents
→
Harvey Agents execute legal work end-to-end, so you can focus on what only lawyers can do.
Innovation
→
Scale expertise and impact to drive firmwide transformation.
In-House
→
Streamline work and shift focus to strategy and speed.
Transactional
→
Accelerate due diligence, contract analysis, and review with precision and control.
Litigation
→
Reduce manual effort, prioritize strategy, and drive stronger outcomes in litigation.
Mid-Sized Firms
→
Drive outsize impact with tools built for lean teams.
Collaboration
→
Work with legal teams across organizations in secure, shared spaces.
A New Era of Collaboration for Legal and Professional Services
→
Law firms and professional service networks have been using Harvey to build new service models and add value collaboratively.
Blog
→
Product updates, insights, and behind-the-scenes from the Harvey team.
Resources Hub
→
The latest videos, webinars, guides, and reports from Harvey.
Press Kit
→
Resources for maintaining a uniform and professional presentation of the Harvey brand.
ROI Calculator Law Firm
→
See Harvey's Impact on Your Firm.
ROI Calculator In House
→
See Harvey's Impact on Your Business.
Harvey Academy
→
Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.
Company
→
About Harvey, our leadership, and career opportunities.
Newsroom
→
Press releases and partnership announcements.
2025 Year in Review
→
In 2025, we celebrated major customer wins, introduced product breakthroughs, and expanded our global presence. Most importantly, we continued to deepen our commitment to building the best AI solutions for our customers.
Login
Request a Demo
Platform
Overview
A unified view of how Harvey's products work together to support your entire practice.
Assistant
Ask questions, analyze documents, and draft faster with domain-specific AI.
Vault
Securely store, organize, and bulk-analyze legal documents.
Knowledge
Research complex legal, regulatory, and tax questions across domains.
Workflow Agents
Run pre-built Workflow agents or build your own, tailored to your firm's needs.
Harvey Mobile
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
Access Harvey where you already work and ground every answer in sources you trust.
Harvey Agents
Harvey Agents execute legal work end-to-end, so you can focus on what only lawyers can do.
Solutions
Innovation
Scale expertise and impact to drive firmwide transformation.
In-House
Streamline work and shift focus to strategy and speed.
Transactional
Accelerate due diligence, contract analysis, and review with precision and control.
Litigation
Reduce manual effort, prioritize strategy, and drive stronger outcomes in litigation.
Mid-Sized Firms
Drive outsize impact with tools built for lean teams.
Collaboration
Work with legal teams across organizations in secure, shared spaces.
A New Era of Collaboration for Legal and Professional Services
Law firms and professional service networks have been using Harvey to build new service models and add value collaboratively.
Customers
Security
Resources
Blog
Product updates, insights, and behind-the-scenes from the Harvey team.
Resources Hub
The latest videos, webinars, guides, and reports from Harvey.
Press Kit
Resources for maintaining a uniform and professional presentation of the Harvey brand.
ROI Calculator Law Firm
See Harvey's Impact on Your Firm.
ROI Calculator In House
See Harvey's Impact on Your Business.
Harvey Academy
Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.
About
Company
About Harvey, our leadership, and career opportunities.
Newsroom
Press releases and partnership announcements.
2025 Year in Review
In 2025, we celebrated major customer wins, introduced product breakthroughs, and expanded our global presence. Most importantly, we continued to deepen our commitment to building the best AI solutions for our customers.
Request a Demo
Login
US
EU
AU
Technical
Enterprise-Grade RAG Systems
How Harvey builds high-performance Retrieval-Augmented Generation (RAG) systems by leveraging enterprise-grade Vector Databases for speed, accuracy, and security.
by
Harvey Team
•
Feb 20, 2025
Introduction
Harvey works with legal and professional services firms to
effectively
and
securely
leverage AI and Large Language Models (LLMs). One technique critical to this mission is Retrieval Augmented Generation (RAG), which enriches LLMs with relevant, up-to-date or user-inputed knowledge, ensuring that the product we provide is grounded and accurate.
Though simple in concept, there are a number of important technical considerations for deploying enterprise-grade RAG systems, especially for the high-scale, privacy-conscious enterprise use-cases our customers have.
At the heart of RAG systems are vector databases (VectorDBs), which enable efficient searching across massive datasets. Choosing the right database requires careful consideration of performance and compliance.
Enterprise Data
At Harvey we build retrieval systems for three key types of data sources that reside in our platform:
User-uploaded files in Assistant that persist for the duration of a thread (1-50 documents)
User-stored documents in Vault projects persisted for the duration of a long-term project (1,000-10,000 documents)
Private & public third party data sources that provide key regulations, laws, and statutes for richer legal research & memos
Since we now serve users in 45 countries, these documents can be in all different languages and regional formats. The combination of these sources basically encompasses all complexities of legal information in the world across both the public internet and private professional knowledge.
In the case of user-uploaded documents and Vault projects, our system needs to be optimized for data privacy and ingestion speed, since sensitive user documents need to be strictly isolated. Users will also start querying documents immediately, so ingestion speed is critical. In addition, to support large corpora of knowledge, the system needs to have high indexing throughput and high accuracy at massive volumes of documents.
Why Retrieval is Hard
Enterprise RAG is far from straightforward. Building an effective system requires solving for many complexities, such as:
Sparse vs. Dense Representations
: Traditional keyword-based search lacks context and can miss subtleties in meaning, while purely dense embeddings might struggle with rare terms such as case identifiers and named entities.
Performance at Scale
: Large corpora require optimized indexes and infrastructure that can search over millions of documents quickly, while also continuously ingesting large volumes of new data.
Accuracy at Scale
: Models must be extremely accurate at discerning relevance, understanding nuances, filtering on metadata, and more.
Complex Query Structures
: Real-world queries can be ambiguous and multilayered. Questions often have complex intents that require deeper reasoning or understanding.
Complex, Domain-specific Data:
Legal and tax datasets are full of context-dependent content and intricacies. For example, laws reference each other, evolve over time, and can be overruled through various mechanisms. To fully grasp the details, our models must incorporate regional and situational knowledge.
Evaluation
: Straightforward ground-truth evaluation sets do not exist publicly for these specialized tasks. We need to work with domain experts to evaluate these models and develop evaluation objectives for very open-ended and complex use cases.
What Makes a Vector Database Useful for RAG
RAG is powered by semantic search, which uses embedding vectors to capture semantic meaning of text or images and find relevant items for the user. While traditional databases and search indexes are optimized for exact matches (e.g., SQL queries, keyword search), these semantic searches rely on large-scale vector similarity computations, hence the need for a specialized vector database.
When evaluating vector databases for RAG, we typically focus on:
Scalability
and performance for both ingestion throughput and query latency
Accuracy
of retrieval when using approximate-nearest-neighbor indexing
Flexibility
of indexing and filtering, as well as developer tooling
Privacy and enterprise-readiness
to maintain security to keep complete privacy for our customers
Unique Enterprise-Ready VectorDB Requirements
Our main priority is keeping customer data private and secure. This same standard extends to the vectors that we embed on our customers' documents. So for enterprise-ready deployments, we require a vector database that can be hosted within a private cloud environment and store both embeddings and source data in our customers’ own secure storage (e.g., their private cloud buckets).
This setup is crucial for meeting stringent security and privacy requirements, ensuring that sensitive data never leaves the client’s domain. In addition, we require high-performance querying at scale, with robust indexing and real-time updates. By combining on-prem deployments, customer-controlled storage, and best-in-class performance, we can guarantee that our platform remains compliant, secure, and reliable for enterprise use cases.
Choosing a VectorDB
With these considerations in mind, we evaluated multiple vector database options across the axes that are important to us. Below are two of the leading options that we evaluated and now actively use at Harvey.
Requirement
Postgres with PGVector
LanceDB
Latency
500K embeddings <2s P50
15M rows w/ metadata filtering: <2s P50
Accuracy
High accuracy at small-medium scale via brute force KNN, HNSW index at large scale with minimal recall degradation
Supports massive-scale IVF-PQ index with search parameters to tune recall against latency
Ingestion Throughput
Strong, can handle highly parallel and batched writes
Limited on open source, strong on enterprise offering
Scalability
Vertical scaling, compute tied to storage
Unlimited horizontal scaling of storage
Data Privacy
Each postgres instance can be encrypted, but data within an instance is centralized
Decentralized by design. Data can live in various cloud buckets.
Hosting
Abundant hosting options on cloud providers
Serverless, self hosted OSS. Enterprise can be hosted in VPC.
Monitoring
Strong built-in instrumentation and ecosystem of tools
Requires building some in-house monitoring and tooling
We primarily use LanceDB Enterprise in production because of its strength across latency, accuracy, ingestion throughput, scalability, data privacy, and hosting. Meanwhile, we still appreciate the simplicity and feature-completeness of Postgres for rapid development, and use it for smaller-scale projects that operate on public data.
Using Domain Expertise to Refine Retrieval
A key part of building robust retrieval pipelines at Harvey is working hand-in-hand with domain experts to develop, evaluate, and refine our models. This begins with guidance on the most authoritative data sources and the nuances involved in understanding them, and continues with their usage and detailed feedback, which is then used to tune the models for further accuracy.
A prime example is our
collaboration with PwC’s tax professionals to build a Tax AI Assistant
. Here, specialists in tax law helped us create a system that is 91% preferred over off-the-shelf ChatGPT, tackling much more complex problems with higher quality outputs.
Conclusion
Developing a robust RAG system requires a methodological approach across accuracy, scalability, privacy, and more. Choosing the right vector database is an essential step in establishing strong foundations, enabling us to build a product that brings highly accurate answers to hundreds of professional service firms worldwide.
Thanks to everyone who’s worked on retrieval systems at Harvey!
Contributors: Aman Kishore, Calvin Qi, Samarth Goel, Aravind Srinivasan, Jenny Pan, Pablo Felgueres, Mayank Kishore, Vasudha Rengarajan, Spencer Poff, Philip Lan, Aaron Stern, Phil Cerles, Samer Masterson, Mark McCaskey, Niko Grupen, Julio Pereyra
Next Up
How we Built Image Understanding for Legal Documents
How Harvey Secures Embeddings at Scale
Rebuilding the Review Algorithm to Increase Accuracy and Speed
Unlock Professional Class AI for Your Firm
Request a Demo
Copyright © 2026 Harvey AI Corporation. All rights reserved.
Platform
Assistant
→
Vault
→
Knowledge
→
Workflow Agents
→
Ecosystem
→
Partnerships
→
Solutions
Innovation
→
In-House
→
Transactional
→
Litigation
→
Mid-Sized Firms
→
Collaboration
→
About
Customers
→
Security
→
Company
→
Newsroom
→
Careers
→
Law Schools
→
Resources
Blog
→
Resources Hub
→
Harvey Academy
→
Help Center
→
Legal
→
Privacy Policy
→
Press Kit
→
Your Privacy Choices
→
Follow
X
→
LinkedIn
→
YouTube
→
Copyright © 2026 Harvey AI Corporation. All rights reserved.
