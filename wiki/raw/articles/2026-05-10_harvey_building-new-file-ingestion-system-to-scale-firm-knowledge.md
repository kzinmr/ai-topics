---
title: "Building a New File Ingestion System to Scale Firm Knowledge"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/building-new-file-ingestion-system-to-scale-firm-knowledge"
scraped: "2026-05-10T01:27:05.513681+00:00"
lastmod: "2026-02-11T16:00:00.000Z"
type: "sitemap"
---

# Building a New File Ingestion System to Scale Firm Knowledge

**Source**: [https://www.harvey.ai/blog/building-new-file-ingestion-system-to-scale-firm-knowledge](https://www.harvey.ai/blog/building-new-file-ingestion-system-to-scale-firm-knowledge)

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
Building a New File Ingestion System to Scale Firm Knowledge
How we built a durable, high-throughput system for ingesting hundreds of thousands of files from document management systems into Harvey.
by
Reggie Cai
•
Feb 11, 2026
The best legal work doesn’t happen in a vacuum. It builds on years of accumulated institutional knowledge: prior deal structures, successful motion templates, negotiation playbooks, and matter-specific expertise. Most often, this context lives in files stored in document management systems (DMS).
When lawyers bring this context into Harvey, AI output quality improves. Answers are grounded in the firm’s actual precedents, and drafts reference real examples of proven work products.
But getting it there isn't easy. Large firms often have millions of documents in their DMS, whether it be iManage, SharePoint, Google Drive, or another platform. Getting this knowledge into Harvey — and keeping it up to date — required a rethinking of our file ingestion infrastructure. Below, I briefly describe how we made this possible.
Moving Beyond Manual Uploads
We introduced DMS integrations more than a year ago, allowing manual import (and export) of files. The impact was immediate: customers who connected their DMS saw significantly more file uploads, leading to improved answer quality with more grounded and precedent-aware outputs.
However, our customers experienced some issues as adoption grew. At scale, our synchronous file ingestion couldn't process extremely large uploads quickly. Users also had to manually select large sets of individual files (not folders), a process that was progressively untenable.
Even after files were uploaded to Harvey, they eventually became stale. When users updated a document in iManage, they had to also update the same files in Harvey. In an ideal world, they shouldn’t need to dedicate time to manually maintain their firm knowledge in Harvey.
To solve these pain points, we decided to build two new features.
Folder uploads:
Select any folder from a DMS and import the entire hierarchy into Harvey — including nested folders, their associated files, and all relevant metadata. Our goal was to support one click import of hundreds of thousands of files.
One-way sync:
Connect a folder or client matter for continuous synchronization. When files or folders change in the DMS, Harvey automatically detects and syncs the updates.
Building such a system at scale required solving several core challenges around orchestration, resilience, correctness, and performance.
Orchestrating Asynchronous Workflows
Reaching our goals meant migrating from synchronous file downloads to an asynchronous workflow architecture. We chose Temporal as our orchestrator because file ingestion at scale is inherently complex and unpredictable — traffic is bursty, external services rate limit, and requests fail transiently.
Complex, multi-step orchestration.
Our file ingestion and processing pipelines are complex and continuously evolving, and Temporal makes it straightforward to define and edit these workflows with branching logic, fan-in/fan-out steps, and many individual decomposed tasks.
Work can be parallelized and scaled horizontally.
We can run thousands of file downloads concurrently across a distributed set of workers while maintaining correctness guarantees. Increasing throughput is as simple as adding more workers to specific task queues.
Every step is checkpointed.
If a workflow fails midway through processing 100,000 files, it resumes from exactly where it left off, not from the beginning.
Retries are automatic and configurable.
Transient failures get retried with appropriate backoff. Non-retryable errors (like authentication failures) surface immediately.
The high-level view of our file ingestion workflow is as follows:
Step 1: Folder selection
A user picks a folder from their connected DMS to upload or sync to Harvey.
Step 2: Crawl and build manifest
We traverse the folder hierarchy, building a complete manifest of all files and folders with their metadata. This happens asynchronously and handles pagination, rate limits, and transient failures gracefully.
Step 3: Diffing
For sync operations, we compare the manifest against Harvey’s internal representation and compute the minimal set of changes needed: which files and folders to create, update, rename, move, or delete.
Step 4: Apply changes
Files are downloaded in parallel and database updates are batched and committed.
Step 5: Trigger downstream processing
Once files land in Harvey, we trigger downstream processing like chunking, embedding, and OCR to integrate them into the context leveraged by our AI systems.
Resilience: Handling Failures Gracefully
While Temporal provides many useful durability guarantees and retry mechanisms, we still need to be mindful of our workflow architecture to take full advantage of them.
Crawling Resiliently
The crawling workflow uses a breadth-first traversal pattern to iterate through folders in parallel and is structured so that each API request is an individual Temporal activity.
This granularity is intentional. When crawling a folder hierarchy with thousands of nested folders, we might need to make thousands of API calls — each potentially subject to rate limits or transient failures. By making each API request its own activity, we get automatic retry behavior at the most granular level. If we hit a rate limit on page 47 of a 200-page folder listing, Temporal retries just that request after the appropriate backoff, and we don't lose the progress from pages 1-46.
Isolated File Downloads
File downloads follow a similar pattern. An orchestration workflow creates batches of files to process, with each individual file in a batch downloaded in a separate activity to ensure failure isolation. Files that fail with retryable errors are queued to retry with an appropriate delay.
Rate Limiting: The Hidden Complexity
Managing rate limits across this distributed system turned out to be a challenge. We must ensure that we never exceed external rate limits because other Harvey products that connect to the same integrations would experience degraded performance. It is paramount that asynchronous file ingestion jobs in Vault don’t exhaust external API quota and take down real-time user journeys like Assistant file uploads.
Each integration partner enforces rate limits differently—by request count, payload size, or both; scoped per-user, per-organization, or both; and sometimes changing dynamically based on tier or infrastructure load.
To solve for this, we implemented multiple variations of an in-house rate limiter built on top of Redis that accommodate this complexity. Each integration has a configuration that specifies the rate limit dimensions, scopes, and overall quota. Every external request is tracked, and when we approach limits, the system automatically throttles — rescheduling jobs proactively rather than exceeding external rate limits.
Ensuring Correctness With the Sync Algorithm
For one-way sync, we need to compute exactly what’s changed between the external source and Harvey’s internal state. Our diffing algorithm compares the crawled manifest against Harvey’s internal representation:
Mapping external IDs to internal IDs.
Each file and folder in Harvey stores the external ID from the source system, enabling us to track identity across renames and moves.
Detecting changes.
For each resource in the manifest, Harvey determines if it needs to be created, renamed, re-downloaded, or moved. Resources no longer present are deleted.
Ordering operations carefully.
The order of operations for applying the changes matters when it comes to folders. Folders must be created before any of their children files or folders, and deletions should occur after any children have been moved.
For content change detection, we use hash-based comparison when available, falling back to timestamp comparison if necessary.
This ensures we only re-sync files that have actually changed
. Advanced integrations also provide functionality for capturing deltas after a given time, thus making it even easier to track necessary changes to apply.
Performance: Moving Data at Scale
Ingesting hundreds of thousands of files means moving large amounts of data quickly and writing many updates to our database. After several iterations, we designed a system with the following key principles to optimize performance:
Batch aggressively.
Database operations are batched at every step, reducing network round trips and pipeline latency.
Connection pooling.
We use PgBouncer to reduce connection overhead and prevent exhausting database connection limits.
Parallelize when possible.
Individual files are downloaded separately, so we maximize work completed simultaneously.
Use blob storage for intermediate states.
Manifest data and sync state get written to blob storage rather than passed through Temporal’s event history. This keeps workflows lightweight while handling arbitrarily large folders.
Design task queues carefully.
By assigning Temporal tasks to different task queues, we can isolate tasks and scale workers appropriately for CPU vs I/O intensive workloads. Workers can then be tuned to optimize performance for a task queue.
Clean up immediately.
For privacy and security, temporary data in blob storage is deleted as soon as processing completes.
Results: Scale and Speed
The new system significantly expands what’s possible for our customers. It is designed to support ingestion of hundreds of thousands of files, with an architecture that can
scale further
as customer needs grow. Requests are queued for asynchronous processing without degrading in-app user experience, and users can conveniently upload entire practice libraries or client matters.
We’ve also made meaningful improvements to
speed
and
workflow
. File upload tasks that previously required substantial manual effort can now be completed with a few quick clicks. Files are designed to stay in sync with their source systems, so when a lawyer updates a document, those changes are reflected in Harvey on the next scheduled sync. Together, these updates are intended to support higher-quality outputs that are more grounded and better tailored to the materials provided.
The Future of Firm Knowledge at Harvey
We built this system with extensibility in mind. Now, adding a new DMS integration is a matter of implementing a well-defined interface and updating configurations.
What previously took weeks of engineering work now takes days. The core workflow orchestration, rate limiting, diffing algorithm, and file processing pipeline are all shared.
We’re building toward a world where customers can reliably use Harvey as the intelligence layer across all their firm knowledge. Data should flow seamlessly between storage systems and Harvey, with no friction around finding relevant context, enforcing access controls, and exporting work products back.
This means:
Beyond files:
The same ingestion infrastructure extends to other resources that provide valuable context — client matter metadata, ethical walls, emails, billing entries, and more. Anything that can be crawled and indexed can flow into Harvey.
Agentic search across DMS:
This infrastructure — durable workflows, rate-limited API access, and integration adapters — can power real-time AI agents that search and retrieve documents directly from a customer’s DMS without requiring pre-ingestion.
Broader integration coverage:
More DMS providers, more practice management systems, and more ways to connect firm knowledge. All behind the same, simple user interface.
These features are currently in early access and will be generally available soon. Contact your Harvey representative to get early access in the meantime. If you're interested in building these types of systems, check out our
open roles
.
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
