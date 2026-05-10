---
title: "Harvey partners with Voyage to build custom legal embeddings"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/harvey-partners-with-voyage-to-build-custom-legal-embeddings"
scraped: "2026-05-10T01:27:02.376344+00:00"
lastmod: "2024-07-22T21:25:00.000Z"
type: "sitemap"
---

# Harvey partners with Voyage to build custom legal embeddings

**Source**: [https://www.harvey.ai/blog/harvey-partners-with-voyage-to-build-custom-legal-embeddings](https://www.harvey.ai/blog/harvey-partners-with-voyage-to-build-custom-legal-embeddings)

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
Company
:Harvey: partners with Voyage to build custom legal embeddings
Announcing a custom embeddings model with Voyage AI, fine-tuned on case law.
by
Harvey Team
and
Tengyu Ma
•
Jul 22, 2024
Intro
Retrieval-augmented-generation (RAG) is a fundamental component of real-world LLM systems, and a tool we often use to augment our custom models with specialized context. Embeddings are the backbone of RAG, enabling retrieval of items by their semantic meaning and complementing classical search strategies like keyword search. The challenge with standard embeddings, like standard language models, is that they are trained on general corpora of data and therefore struggle to perform in specialized fields. For example, when considered against the entire universe of text, legal jargon is all relatively similar—this prevents embedding-based retrieval methods from disambiguating relevant text from the rest of the data.
Voyage AI
Voyage AI, led by Stanford professor Tengyu Ma, is a leading developer of customized embedding models and LLM retrieval infrastructure. Voyage has assembled a world-class AI research team that has developed novel techniques that enable embeddings to better capture the nuances of specialized text in the same way as domain experts. For example:
voyage-finance-2
Embeddings optimized for financial applications.
voyage-law-2
Embeddings optimized for legal applications and long-context retrieval.
voyage-multilingual-2
Embeddings optimized for multi-lingual retrieval.
Given their track record of building domain-specific embedding models, we were excited to partner with the Voyage AI team to fine-tune embeddings specifically for Harvey use cases.
Custom Embeddings
Together, we collaborated to fine-tune an embedding model on US case law — more than 20 billion tokens of legal text where even the best standard embedding models struggle to distinguish cases relevant to common questions. Starting from voyage-law-2 as a base, our model was trained on both the raw case law text itself, using Voyage AI’s proprietary self-supervised techniques, and subsequently on a dataset of exemplar questions and expert annotations on relevant cases collected by our legal research team.
Voyage’s custom training work has been immediately impactful. We evaluated our model and other leading embedding models on our Harvey legal retrieval task — a large dataset of query-content pairs generated from a variety of legal documents — and used Normalized Discounted Cumulative Gain (NDCG@10) and Recall at 100 items (Recall@100) as performance metrics (both are standard metrics for retrieval quality). Our custom embedding model, named voyage-law-2-harvey, reduces the amount of irrelevant material returned in top results by nearly 25% compared to the next best off-the-shelf embedding models (e.g. Google’s text-embedding-004 or OpenAI’s text-embedding-3-large). It is able to accomplish this with 1/3 of the embedding dimensionality, leading to significant benefits in storage and latency. We have also combined voyage-law-2-harvey’s more robust understanding of legal text with other proprietary search methods, further improving the ability of our retrieval systems to identify relevant cases and passages from cases in response to complex legal questions.
Next Steps
We are excited to continue working with Tengyu and Voyage to develop a suite of custom embeddings models for legal (and beyond), as well as work with our clients to create firm/company-specific embeddings for enterprise search, RAG systems, and other GenAI applications.
Credits: Aravind Srinivasan[1], Calvin Qi[1], Wen Phan[2], Daniel Hunter[1], Julio Pereyra[1], Niko Grupen[1], Tengyu Ma[2], Gabriel Pereyra[1]
[1]
Harvey
[2]
Voyage AI
Next Up
The Supreme Case for Harvey
How we Built Image Understanding for Legal Documents
Introducing Harvey’s Transformation Office
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
