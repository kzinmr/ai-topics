---
title: "Building Image Understanding for Legal Documents"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/building-image-understanding-for-legal-documents"
scraped: "2026-05-10T01:27:24.824002+00:00"
lastmod: "2026-05-06T18:00:00.000Z"
type: "sitemap"
---

# Building Image Understanding for Legal Documents

**Source**: [https://www.harvey.ai/blog/building-image-understanding-for-legal-documents](https://www.harvey.ai/blog/building-image-understanding-for-legal-documents)

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
How we Built Image Understanding for Legal Documents
An on-demand vision system that enables Harvey to reason over charts, diagrams, and complex layouts without sacrificing speed or accuracy.
by
Tom McCormick
,
Anna Zhang
, and
Gary Lam
•
May 6, 2026
Legal documents aren't just made up of text. They're full of charts, diagrams, signature blocks, floor plans, org charts, and tables that lose critical meaning when reduced to Optical Character Recognition (OCR) output in AI systems. When a lawyer asks an AI tool, "what does the revenue chart on page 47 show?", they need an answer that actually reads the chart and understands the colors of each bar and how they map to the chart key, rather than simply extracting the numbers and text as chunks.
We built a system in Harvey that enables our agent to see and reason about visual content in documents, on demand, at query time (i.e. only when a user asks a question that requires visual understanding). Throughout the rest of this post, we’ll walk through how we aligned on this approach, designed the feature, and deployed it in practice.
The Problem: Complex Legal Documents
Traditional document processing pipelines only extract text and have no way to extract or pass on visual information. That works for text-based contracts and memos, but falls apart when documents contain:
Financial charts where the actual values matter
Engineering diagrams and floor plans
Tables with complex layouts that don't survive text extraction
Scanned documents with handwritten annotations
Signature pages where visual context matters
Images that contain no text or caption
Since models are reliant on the extracted text to use as context, any missing information causes lower quality responses in the final output. In addition, the model has no way of knowing what was dropped or left out during document processing, and must fill in the gaps through reasoning and assumptions.
Our Approach: On-Demand Analysis
Rather than having Harvey describe every image at indexing time (a process that is expensive, lossy, and often wrong without context), we built an
on-demand visual analysis tool
that the agent invokes only when it needs to. This approach avoids wasting compute on irrelevant images when a query doesn't need it, while improving accuracy when visual understanding is actually required.
How it Works
The agent decides when to look.
When a user asks a question in Harvey that involves visual content, the agent recognizes this and invokes the image analysis tool — similar to how a person flips to the relevant page in a document to look at the relevant chart.
Smart page finding.
For large documents, the user doesn't need to say "look at page 47." The agent first searches through the document's text to identify candidate pages likely to contain the relevant visual content, then examines them for visual content.
High-fidelity rendering.
We render document pages at high resolution, handling edge cases like oversized images, unusual formats, and documents that need PDF conversion. A dedicated rendering service handles this at scale, separate from the main application.
Structured visual reasoning.
The vision model doesn't just describe what it sees — it's prompted to read chart axes, interpolate values between tick marks, distinguish exact from approximate readings, and always provide its best answer with confidence levels. For example, when reading a revenue chart, it will identify axes, extract labeled values, and estimate unlabeled points when necessary.
Text-first, vision-second.
We gate image analysis behind a text search step. If the agent can find the answer in the text, we don't spend more token on vision. This keeps responses fast for common queries while being thorough when it matters.
Engineering Challenges and How we Solved Them
Building a high-performance vision system isn't just about choosing the right vision model; it’s also about architecting a system that is high speed and low cost. To handle billions of images without breaking the bank or the clock, we had to rethink our pipeline from the ground up.
Scale.
Legal documents routinely span hundreds of pages. We can't render and analyze every image on every page, we need to be surgical. Our candidate page selection narrows a 500-page document down to 2-3 pages in milliseconds using existing search infrastructure.
Consistency.
Lawyers upload a myriad of different document types in Harvey, and any number of these could contain visual content that needs to be analyzed. To solve this, documents are first converted to a consistent format before we render the image at high DPI — enough to read small chart labels, but with intelligent downscaling for oversized images.
Cost.
Processing a single image is roughly 50x more expensive than generating a text response. Last month, our pipeline handled billions of images within the documents we processed. However, we discovered a massive optimization opportunity: 90% of those images are not actually necessary for answering the query. By shifting to an on-demand processing model, we’re cutting significant waste without sacrificing performance.
Graceful degradation.
If a page doesn't contain the visual element the user asked about, the system detects this and moves on rather than hallucinating an answer. The tool reports what it can and can't determine, with confidence levels.
Key Learnings
Building this system surfaced two key insights that shaped the final design:
Foundation models are surprisingly good with just text.
In many cases, the underlying models handle visual questions well using only the extracted text, no image rendering needed. Charts with labeled data points, tables with clean structure, and diagrams with descriptive captions often yield correct answers from text alone. This reinforced our text-first architecture: vision is the fallback, not the default.
Tool description tuning and evaluation matters more than you'd expect.
The agent decides when to invoke image analysis based on its tool description. This means that the tool needs to be carefully evaluated and its description adjusted. It shouldn’t over trigger and affect other tool recall metrics, but it also shouldn’t undertrigger when actually presented with an image use case.
Getting this balance right was one of the highest-leverage investments we made. Too broad, and the agent wastes cycles rendering pages for questions that text can answer. Too narrow, and it misses cases where vision would help. Small changes to the tool description, how we frame what the tool does, when to use it, and what kinds of questions benefit from it, had an outsized impact on overall tool recall and response quality.
Making Image Understanding a Tool, not a Step
We evaluated this tool against a curated dataset of real legal document queries involving visual content: chart reading, diagram interpretation, and image-based questions. In our evaluations, the system reliably extracts specific numeric values from charts, identifies visual elements in complex layouts, and provides structured answers that lawyers can cite.
The key insight:
image understanding shouldn't be a preprocessing step — it should be a tool the AI uses only when needed.
This matches how people actually work with documents. You don't memorize every chart before someone asks you a question. You find the right page, and then look at the chart.
What’s Next
We're continuing to improve tool recall, increase rendering quality for edge cases, reduce latency, and expand vision capabilities into other areas at Harvey. We are committed to meeting lawyers where they are, in all formats of work that they do.
We're hiring engineers who want to solve hard problems at the intersection of AI, document understanding, and legal technology. If building systems like this sounds interesting,
check out our open roles
.
Next Up
How Harvey Secures Embeddings at Scale
Rebuilding the Review Algorithm to Increase Accuracy and Speed
Building Spectre
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
