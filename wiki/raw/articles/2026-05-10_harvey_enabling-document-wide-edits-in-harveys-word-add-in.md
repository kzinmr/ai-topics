---
title: "Enabling Document-Wide Edits in Harvey’s Word Add-In"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/enabling-document-wide-edits-in-harveys-word-add-in"
scraped: "2026-05-10T01:21:09.409277+00:00"
lastmod: "2025-09-11T13:00:00.000Z"
type: "sitemap"
---

# Enabling Document-Wide Edits in Harvey’s Word Add-In

**Source**: [https://www.harvey.ai/blog/enabling-document-wide-edits-in-harveys-word-add-in](https://www.harvey.ai/blog/enabling-document-wide-edits-in-harveys-word-add-in)

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
Enabling Document-Wide Edits in :Harvey:’s Word Add-In
Our engineering team shares the architecture, implementation, and evaluation process that made this functionality possible.
by
Rina Kim
,
Aaron Weldy
,
Scott Werwath
,
Aadil Manazir
, and
Spencer Poff
•
Sep 11, 2025
When Harvey first introduced AI-powered editing within Microsoft Word, we focused on optimizing the experience for targeted local edits. This choice enabled users to make fast and predictable edits, but created constraints for longer documents that required complex, multi-page coordinated changes.
Recognizing this need, we have significantly expanded Harvey’s capabilities.
Users can edit 100+ page documents with a single query
, which unlocks a range of powerful legal drafting and revision use cases. With one instruction to Harvey, you can now:
Conform a draft agreement to a checklist or term sheet stored in a Vault project.
Define a new term and ensure it is applied consistently throughout a contract.
Convert a draft into a template document for easy reuse across matters or clients.
Revise a letter or memorandum using content from emails, meeting notes, or client instructions.
Shorten a long memorandum, letter, or similar document while preserving the substance of its content.
Repurpose a document for a different jurisdiction or client by updating references and adapting provisions accordingly.
Switch drafting posture (for example, buyer-friendly and seller-friendly) across the entire document.
Proofread for grammar, typos, and defined term usage at scale.
The result is a dramatic increase in efficiency, transforming hours of manual effort into a single seamless interaction with Harvey.
In this post, we’ll walk through the architecture, implementation, and evaluation process that makes these document-wide edits possible. Along the way, we’ll discuss the decisions we made and tradeoffs we considered.
Addressing OOXML Challenges in the Word Add-In
Microsoft Word documents are complex files that deal with formatting, styling, lists, links, tables, and other objects. Word documents are stored as Office Open XML (OOXML) packages, and a “.docx” file is a ZIP container organized into “parts” (XML and media) connected by explicit relationships.
Within the main document part, text lives in paragraphs (“w:p”), runs (“w:r”), and text nodes (“w:t”), while structures like tables (“w:tbl”), numbering, and styles live in their own parts. In Harvey's Word Add-In, we interact with this structure through the Office JavaScript API, using ranges, paragraphs, tables, and content controls rather than raw XML.
Having a model read and write OOXML leads to an increased chance of poor-quality outcomes and is less efficient with regards to input token usage. OOXML is verbose and interdependent, so a small text change can disturb styles, numbering, or content controls. Unconstrained generation often produces invalid or schema-nonconformant XML. More importantly, LLMs are trained primarily on natural language. When asked to simultaneously “do legal reasoning about this complex edit request” and “parse and emit XML,” performance on both tasks tends to regress. Studies from
Cornell University
and the
Association for Computational Linguistics
on structured generation have found that format restrictions can trade off with reasoning quality.
Our approach separates concerns by creating a reversible mapping between OOXML objects and their natural-language content. We translate the OOXML to a natural language representation of the document, ask the model to propose edits over text, then deterministically translate those edits back into precise OOXML mutations that preserve styles and structure. For insertions (new paragraphs, list items, or tables), the model anchors placement relative to existing elements. The add-in infers appropriate styling from the new element's surrounding context and Word’s style parts, and we apply changes through the Word JavaScript object model to avoid corrupting the markup.
Comprehensive Edits via Agentic Parallelization
Legal documents are often hundreds of pages, and a single edit request can require thousands of individual changes. While the content of these files can fit inside modern long-context models, our evaluations found that one-shot edits on these long documents tend to miss large portions of the document when thorough document-wide edits are needed.
In practice, we see position bias: Models over-attend to the beginning or end of the context and under-edit the middle, which yields partial coverage instead of a comprehensive pass. This recency and placement bias is known as the
“lost in the middle” effect
and it occurs even with explicitly long-context models. Treating a 200-page M&A agreement as one monolith also increases latency and cost without guaranteeing better recall of edit obligations.
To mitigate these thoroughness and latency issues, we introduced an
orchestrator-subagent architecture
. An orchestrator model reads the whole document, plans the work, and decomposes the request into targeted tasks that each operate on a bounded chunk. Subagents receive precise, localized instructions and achieve thoroughness by only having to consider a small portion of the document. The orchestrator also issues global constraints to keep edits consistent across chunks, such as propagating newly defined terms, aligning tone and style, and updating cross-references. This pattern borrows from established agent and decomposition methods that improve reliability by separating global planning from local execution.
Scaling Offline Evaluation for Reliable Editing
Building to deliver value while navigating the constraints of AI capabilities and product realities requires many rounds of experimentation and iteration. With Harvey being a
multi-model company
, we had a wide variety of model choices to evaluate for each role in the orchestrator-subagent architecture–each with their own tradeoffs on latency, cost, and quality. The number of experiments we wanted to run quickly exceeded our human evaluation capacity. To maintain development velocity while holding a high quality bar, we had to get clever about how we combined
automated and expert-led evaluation
.
In order to develop our evaluations, domain experts, product owners, and engineers worked together closely to define the metrics that mattered most. This included quantitative metrics, such as the percentage of body elements modified by the algorithm, and qualitative metrics, such as how well the algorithm’s output aligned with the user’s request. Developing an automated approach to generate directional signals along both axes was an involved process with active collaboration with human lawyer experts. This process eventually enabled us to generate a full set of outputs over a large input set on our target experiment in less than five minutes.
Once this framework was established, we were able to quickly generate A/B experiments and validate different approaches to the implementation. One concrete example of this was when we began representing tracked changes to the model, adding <ins> and <del> tags to the representation of the document body to indicate where tracked changes existed in the document. Automated offline evaluation confirmed that there was no regression on the previous dataset, and demonstrated a clear improvement over baseline performance on queries that referred to redlines in the input document.
Over the course of this project, we tested 30+ model combinations across major model providers and generated tens of thousands of sample outputs. We condensed years of manual work into weeks, and our testing gave us confidence that we exhausted every viable path to deliver the highest-quality version of the feature.
Bringing full-document editing to Harvey’s Word Add-In demonstrates the coordination of document engineering and scalable evaluation methods grounded in legal expertise. This launch turns complex, hours-long legal editing tasks into cohesive one-query interactions. More importantly, it reflects our broader approach at Harvey: deeply understanding legal work, then building product infrastructure and ML systems that meet it with rigor and care.
Next Up
Harvey in Practice: How In-House Teams Monitor, Interpret, and Act on Regulatory Change
How we Built Image Understanding for Legal Documents
Legal Agents for Every Matter, Tailored to You
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
