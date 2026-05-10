---
title: "BigLaw Bench Deep Dive: Retrieval"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/biglaw-bench-retrieval"
scraped: "2026-05-10T01:27:04.955864+00:00"
lastmod: "2024-11-13T18:00:00.000Z"
type: "sitemap"
---

# BigLaw Bench Deep Dive: Retrieval

**Source**: [https://www.harvey.ai/blog/biglaw-bench-retrieval](https://www.harvey.ai/blog/biglaw-bench-retrieval)

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
Insights
BigLaw Bench – Retrieval
Harvey’s retrieval system outperforms commonly used embedding-based and reranking methods, identifying up to 30% more relevant content than alternative retrieval methods across a diverse range of legal document types.
by
Niko Grupen
and
Julio Pereyra
•
Nov 13, 2024
Retrieval-augmented generation (RAG) is a critical element of practical Large Language Model (LLM) systems. Despite its importance, RAG is often trivialized and interpreted as a simple semantic search, where relevant content is retrieved by comparing the similarity between embedded passages of text. Building high-quality retrieval systems, however, requires supplementing embedding-based semantic search with domain-specific (often also LLM-based) data preprocessing, metadata extraction, embedding fine-tuning, and re-ranking or filtering techniques.
Thus far, our evaluation work through BigLaw Bench has focused on measures of answer quality and its associated factors (e.g. hallucinations, citations) – emphasizing the "generation" step in RAG. But finding relevant content from a dataset to answer a given query – the retrieval step – is an equally important component of these systems. To that end, we are expanding BigLaw Bench to include retrieval-focused benchmarks over legal documents. On these tasks, Harvey’s retrieval system outperforms commonly used embedding-based and reranking methods, identifying up to 30% more relevant content than alternative retrieval methods from OpenAI and other embedding model providers (Voyage, Cohere) across a diverse range of legal document types. These leading techniques are used throughout Harvey’s products across Assistant, Knowledge Sources, Vault, and Workflows when analyzing everything from complex documents to large databases.
Legal Retrieval Dataset
Retrieval in legal domains presents a number of unique challenges not contemplated by typical RAG solutions. Indeed, different documents within the legal domain have diverse properties that affect optimal ways to retrieve key information, for example:
Contracts
: Complex documents (e.g., hundreds of pages and potentially hundreds of thousands of tokens of text) with cross-references and defined terms which must be tracked to effectively contextualize relevant text.
Discovery Emails:
Relatively short documents that come in high-volume and have complex relationships (e.g., email threads) and rich metadata (sender, recipient, attachments) essential to identifying relevant messages.
Research Databases
: Datasets like case law consisting of millions of documents, where each document can itself be hundreds of pages and where relationships like recency cannot be captured by vanilla semantic search.
Optimizing information retrieval against these documents requires not only a deep understanding of their structure but also  an understanding of how and why lawyers want to search against these documents. For example, in case law, lawyers care that precedents are not only relevant but also that they are recent and controlling in a jurisdiction. Conversely, when finding precedents in Merger Agreements, factors like industry, deal size, and more can make information more or less relevant. Understanding and capturing this nuance in a retrieval dataset is essential to improving RAG performance in a way that matters to our clients.
To do so, we collected comprehensive examples of two types of datasets. The first are research datasets, collections of documents from research databases like case law, legislation, EUR-Lex, and published law firm memoranda. The second are document collections, large scale aggregations of a particular document type that are typically queried together in practice such as contracts (queried to find precedents or specific deal terms) and emails (queried as part of discovery or investigatory work). For each dataset, we used a mix of human experts and AI systems to generate a large number of salient queries that would be asked against the relevant dataset or document type. Then for each question, our AI-assisted experts annotated relevant material that would need to be retrieved in order to correctly respond to each question. Examples of queries used for each dataset can be found
here
.
Evaluation
We evaluated our proprietary Harvey retrieval system, as well as existing embedding and reranking models, on the BigLaw Bench Retrieval dataset. We measured performance as the percentage of relevant content found by the retrieval system for a given user query, graded against a ground truth established in advance by our in-house legal research team. In technical terms, this is equivalent to recall at a fixed token threshold. Below we show retrieval results across both contracts and research datasets. Our tailored systems demonstrate superior performance, consistently identifying a greater proportion of relevant material compared to traditional embedding- or reranker-based methods.
Relevant material retrieved: Overall and By category
The evaluation results also show the benefit of task-specific optimization. Conventional RAG system’s performance on Merger Agreements (“MAs”) and Stock Purchase Agreements (“SPAs”) varies dramatically, although lawyers would typically consider these complex contracts as relatively similar—at least as compared to documents like court opinions. These gaps confirm the value in thinking about domain- and task-specific retrieval in order to maximize the efficacy of AI systems on any particular task.
Relevant material retrieved: MA and SPA datasets
Reviewing the data overall reveals a number of common patterns for why Harvey’s systems achieve best in class performance. These include:
Metadata:
Adding metadata to contextualize passages of text, allowing retrieval systems to contextualize those passages within a complicated document.
Features:
Capturing features like recency that are typically not accounted for in typical semantic search systems.
LLM-based retrieval:
Using language models to reason about hard relevancy judgments and identify semantic patterns not captured by more coarse AI systems like embeddings.
Combined these patterns differentiate Harvey’s retrieval across complex legal datasets. They also provide avenues for deeper research to continue pushing the quality of retrieval for legal tasks.
Next Steps
Even with advances in model training, RAG remains an essential tool for ensuring that models have factual, up-to-date information at their disposal when answering questions grounded in source of truth materials. Our clients operate globally, and rely on information from innumerable sources to provide advice and services. Ensuring high quality retrieval across these varied sources is our primary goal. To this end, we intend to continue extending our retrieval benchmarks to cover all of the datasets and document types that lawyers routinely engage with.
As model systems become more complex, retrieval efficacy becomes even more important for allowing them to contextualize problems, identify relevant information, and execute complex tasks. An AI agent drafting a brief may need to search a docket to understand the procedural posture of a case; parse a discovery corpus to understand its facts; tap into a firm’s DMS to identify one (or more) relevant prior briefs to build from; and then search a case law and legislative database to find all the precedents needed to draft a winning argument. Our RAG benchmarks provide a framework for ensuring that these AI systems, and others, can enable lawyers to surface and leverage critical information more efficiently and effectively in all aspects of their practice.
Contributors: Julio Pereyra, Niko Grupen, Nan Wu, Boling Yang, Joel Niklaus, Matthew Guillod, Laura Toulme, Lauren Oh
Next Up
Harvey Power Users: The Skill You're Sharpening
How we Built Image Understanding for Legal Documents
Open-Sourcing Harvey’s Long Horizon Legal Agent Benchmark
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
