---
title: "Scaling Harvey’s Document Systems: Vault File Upload and Management"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/scaling-harveys-document-systems-vault-file-upload-and-management"
scraped: "2026-05-10T01:27:13.835294+00:00"
lastmod: "2025-10-09T14:30:00.000Z"
type: "sitemap"
---

# Scaling Harvey’s Document Systems: Vault File Upload and Management

**Source**: [https://www.harvey.ai/blog/scaling-harveys-document-systems-vault-file-upload-and-management](https://www.harvey.ai/blog/scaling-harveys-document-systems-vault-file-upload-and-management)

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
Scaling :Harvey:’s Document Systems: Vault File Upload and Management
How we made Vault systems faster, more responsive, and more reliable — including an 89% improvement in upload time for 10,000 files.
by
Tau Jin
•
Oct 9, 2025
This post is part one of our two-part series on scaling document systems across Harvey’s engineering systems. In this installment, we focus on Vault-specific improvements: How we rearchitected file upload, reduced browser memory, and made Vault dramatically faster for large projects.
When Harvey first launched
Vault
, we optimized for a typical legal use case: project folders with hundreds to thousands of documents. But as Harvey grew to serve more leading law firms, we encountered a new reality: Enterprise firms weren't just uploading thousands of files — they were uploading tens of thousands. Entire M&A data rooms. Complete litigation discovery sets. Years of regulatory filings.
What had been built as a nimble document management system was now being stress-tested at unprecedented scale. As a result, our engineering team embraced the challenge of building infrastructure that could handle the most demanding legal workflows.
Throughout the rest of this post, I’ll share how we rebuilt Vault's architecture to deliver 10 times better performance while maintaining the seamless experience our users know and expect.
The Challenge of Scale in Vault
Building Vault for legal documents becomes exponentially harder as you scale up. Here are some challenges we’ve faced:
Volume and velocity
: In just one M&A deal, upwards of 50,000 documents can be uploaded in waves throughout due diligence. Teams often work against tight deadlines, uploading thousands of files minutes before a filing deadline or negotiation session.
Maintaining interface performance
: Harvey’s Vault interface needs to handle more than 100,000 documents in a single project while maintaining instant search, filtering, and navigation. Users expect responsive pages when browsing massive data rooms for every interaction from document preview to bulk operations.
Rich interaction models
: Vault isn't just storage; it's an interactive workspace. Users need to be able to seamlessly transition between uploading documents, organizing them into folders, applying tags and metadata, generating Review tables, and querying content with
Assistant
. Each interaction demands different optimizations, from file explorer lists that handle thousands of files to Review tables that support complex filtering across millions of cells.
Complexity and variety
: Legal documents range from single-page NDAs to 500-page credit agreements, and from simple PDFs to complex Excel models with hundreds of thousands of cells. Each document type requires different processing strategies, and ensuring reliability across all formats is critical for a smooth user experience.
With this context in mind, our telemetry revealed key challenges that could impact the user experience should Vault usage continue to grow:
Browser memory consumption will cause performance degradation on low-spec laptops.
Large document sets could take a long time to upload and process.
Complex and OCR-heavy documents will experience elevated error rates.
We set out to systematically address each of these challenges, combining architectural changes with targeted optimizations to transform Vault's performance at scale.
Rearchitecting File Upload for Bulk
Our original upload architecture prioritized data integrity and validation, which are essential qualities for document management. The system carefully orchestrated uploads to ensure each document was properly validated before proceeding. This conservative approach provided the reliability required by Vault as a document management system in the early days.
New possibilities for optimization opened up as we scaled our tech foundations. By isolating upload operations into dedicated web workers, implementing separate state management for temporary failures vs. processing errors, and building a robust file reconciliation system, we eliminated the architectural constraints that previously required sequential processing. We can now batch our file upload more effectively.
This transformation required sophisticated coordination across the stack:
Intelligent parallel batching
: The frontend now dynamically adjusts parallelism based on file metadata and system load.
Transactional integrity
: Despite parallel processing, we are able to maintain integrity through careful transaction management.
Query optimization:
The backend consolidates individual queries into efficient bulk operations.
Smart conflict resolution:
The platform enhances duplicate detection and optimistic creation to handle concurrent uploads gracefully.
Real-time progress tracking:
We provide granular per-file status updates across all sub-systems.
Detailed upload visibility:
The UI shows comprehensive user-facing improvements with granular status transitions from initial upload through processing steps.
As a result, upload time for 10,000 files dropped
from 20 minutes to just over two minutes
— an
89% improvement
.
Solving the Memory Problem With Server-Side Migration
As Vault projects grew larger, we faced a fundamental architectural decision about where compute-intensive operations should happen. Our original approach prioritized immediate responsiveness in browsers with client-side operations. This worked well for typical projects, but hit scaling limits as customers began uploading entire data rooms with tens of thousands of documents. Interactions became sluggish, and overall user experience degraded.
To solve this challenge, we evolved to a server-side architecture where the backend handles sorting, filtering, and aggregation, while the browser maintains only a lightweight viewport into the data.
This transformation required reimagining every interaction and came with a lot of heavy lifting. Here’s a summary of what we built:
Server-driven search and file list
that operates across the entire Vault without loading all results.
Cross-page file selection with lazy parent-mapping
that tracks folder hierarchies incrementally as users navigate. We resolve selections by walking up the ancestry chain at query time, allowing users to select entire directory trees without ever loading them. In particular, it solves for complex scenarios like deselecting specific files within a selected folder hierarchy, while maintaining states across the nested folder tree.
Event-driven context architecture
that separates data ownership (in hooks) from event coordination (in context), enabling file operations triggered in modals to instantly update the file explorer without global state pollution.
New bulk operation APIs
that handle actions spanning thousands of uploaded files.
Smart caching with predictive prefetching
that makes scrolling feel instantaneous despite on-demand loading.
Adaptive progress indicators
that show detailed file-by-file status for small uploads while gracefully scaling to summary views for bulk operations.
As a result, memory usage
dropped by 90%
for large Vaults, while initial load time
improved by 80%
.
Lessons From Scaling Vault
Now that we’ve walked through how we rebuilt Vault's architecture and what we built, let’s take a look at the improvements by the numbers:
Metric
Improvement
10k file upload
89% faster
Browser memory
93% reduction
Initial page load
80% faster
These optimizations have fundamentally changed how legal teams work with documents at scale. What once required careful planning around system limitations (uploading documents overnight, breaking large projects into smaller chunks, working with degraded browser performance) now happens more seamlessly within the natural flow of legal work.
Building for scale also taught us three critical lessons:
Progressive enhancement over premature optimization
: Our initial architecture served the needs of our very early users and allowed us to iterate on new product capabilities quickly. By building a solid foundation first, we could identify actual bottlenecks through real usage patterns rather than guessing at theoretical problems.
Coordinated optimization yields exponential gains
: Each improvement delivered meaningful gains independently. But when combined, they created a multiplicative effect that transformed the user experience.
Observability is non-negotiable
: Distributed tracing and comprehensive telemetry weren't nice-to-haves. They were essential for understanding system behavior at scale. In other words, you can't optimize what you can't measure.
The work to continue optimizing Vault’s performance doesn’t end here. Each order of magnitude brings new challenges, bottlenecks, and lessons, and our team is excited to tackle them with the same level of precision. That's the thing about scaling: the job's never really finished.
Stay tuned for part two of this series, where we’ll dive into backend pipelines, document ingestion, and retrieval optimizations that enable even faster document processing and retrieval experiences across millions of documents.
Acknowledgements
Thank you to the following members of Harvey’s Engineering team for their work on Vault: Cindy Nguyen, Stella Ge, Joey Wang, Ganesh Jothikumar, Samer Masterson, Mark McCaskey, Shrihari Murlidharan, Nijanthan Hariharan, Zhiyi Chen, Jin Zhang, Bhavesh Kakadiya, Philip Lan, John Graham, and Steve Mardenfeld.
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
