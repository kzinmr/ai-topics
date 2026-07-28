---
title: "Scaling Document Processing Across Harvey"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/scaling-document-processing-across-harvey"
scraped: "2026-07-28T06:00:03.233923+00:00"
lastmod: "2026-07-27T17:00:00.000Z"
type: "sitemap"
---

# Scaling Document Processing Across Harvey

**Source**: [https://www.harvey.ai/blog/scaling-document-processing-across-harvey](https://www.harvey.ai/blog/scaling-document-processing-across-harvey)

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
Company
Overview
→
A unified view of how Harvey's products work together to support your entire practice.
Agents
→
Purpose built agents execute complex legal work end to end.
Vault
→
Securely store, organize, and bulk-analyze legal documents.
Knowledge
→
Research complex legal, regulatory, and tax questions across domains.
Shared Spaces
→
Work with legal teams across organizations in secure, shared spaces.
Command Center
→
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
Contract Intelligence
→
Surface insights, strengthen negotiations, and accelerate reviews.
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
About
→
Who we are and what we're building.
Careers
→
Join our team and help Harvey shape the future of professional services.
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
Agents
Purpose built agents execute complex legal work end to end.
Vault
Securely store, organize, and bulk-analyze legal documents.
Knowledge
Research complex legal, regulatory, and tax questions across domains.
Shared Spaces
Work with legal teams across organizations in secure, shared spaces.
Command Center
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
Contract Intelligence
Surface insights, strengthen negotiations, and accelerate reviews.
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
Company
About
Who we are and what we're building.
Careers
Join our team and help Harvey shape the future of professional services.
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
Scaling Document Processing Across the :Harvey: Platform
A look at the infrastructure changes that enabled Harvey to scale document processing without compromising performance or reliability.
by
Tom McCormick
,
Jin Zhang
,
Shunrang Cao
,
Jinfeng Zhuang
,
Anna Zhang
,
Adam Shen
, and
Gary Lam
•
Jul 27, 2026
At Harvey, document processing sits underneath
Vault
,
Assistant
, and every workflow that interacts with a customer's own data. Unlike many other AI products, almost every query from a lawyer involves documents. These queries often range from a single file to hundreds or thousands of documents at once.
Contracts, closing binders, deposition transcripts, email archives, scanned PDFs, and entire data-room exports all pass through the same path: fetch the file, extract the content, split it into useful pieces, and make it searchable.
A year ago, that platform handled just under one million documents in a busy week. Users rarely think about document processing when it is working. Over the last 12 months, our work has been focused on keeping it that way while weekly volume moved from
hundreds of thousands of documents to tens of millions
.
The main lesson was simple: At this scale, document processing stops being one pipeline and starts behaving like several different systems. Extraction, chunking, embedding, indexing, storage, and retrieval all break in different ways. We had to split the work along those lines.
Below, we share a look into some of the work we did to stay reliable and low latency while scaling incredibly fast, plus a glimpse into the future and some of what we have planned for growth.
A Look at the Growth
Measured by completed-processing time across customer workspaces, the scale curve looked roughly like this:
Timeframe
Documents Processed
Original File Data
A Year Ago
0.94 million
1.44 TB
Latest Complete Week
24.8 million
56 TB
At current scale, full weeks are regularly in the tens of millions of documents. The latest complete week in the measurement window averaged about 3.5 million documents per day. Compared with a year ago, that is
26x more documents
and
39x more data
.
Rounded quarterly snapshots. Raw weekly data has normal operational and holiday volatility; this view emphasizes the underlying scale curve.
What Drove the Growth
The growth in volume came from a shift in how customers use Harvey. Instead of relying on one-off uploads, users are increasingly treating us as a central system of record for massive document collections. Vault has historically been our main source of this large document traffic. However, we are seeing a lot of momentum from our connectors as more customers sync their existing document management systems directly with Harvey, including iManage, SharePoint,
Box
, Google Drive,
NetDocuments
, and on-premise setups.
The file mix also got more complex. Scanned PDFs, email archives, data-room exports, eDiscovery material, international document formats, and difficult encodings keep pushing processing complexity up. Growth was not just more documents; it was more kinds of documents, with more OCR, conversion, and indexing edge cases showing up at production frequency.
Every one of those documents has to be processed durably, quickly, and without one customer's bulk upload degrading the rest of the platform.
Background: The Document Processing Pipeline
Our Document Processing pipeline contains three main steps, each with their own performance and scaling constraints. Every document goes through these three broad stages.
First, we
extract data and metadata
. The platform downloads the file, identifies the file type, extracts text and structure, runs OCR for scanned content, and captures metadata such as file type, size, page count, source, and processing status. This is where most format-specific complexity lives: PDFs, Microsoft Office files, scanned documents, email archives, connector exports, and edge-case encodings all need different handling.
Second, we
generate embeddings for the file contents
. Once the document is converted into structured text, the platform splits it into retrievable chunks and generates embeddings for those chunks. This stage is constrained by document size, chunk volume, CPU, and embedding-model throughput.
Third, we
index
. The chunks, metadata, and embeddings are written into the retrieval layer so Vault, Assistant, and workflows can search, cite, and reason over the customer's documents. This stage is constrained by vector-store write throughput, blob-read memory, and downstream backpressure.
Data residency
adds another constraint to the pipeline. Documents need to be processed in the right region, with workers and storage aligned to customer requirements. That matters later in the pipeline, especially when large intermediate artifacts move between storage and workers.
At lower volume, those stages could share more infrastructure. At Harvey's current volume, they behave like different systems. Each stage has a different bottleneck, a different failure mode, and a different capacity model.
Making the Pipeline Work Durable
The original pipeline ran on an older job queue. That worked while the volume was lower. As batches grew longer and ingestion became burstier, the old model exposed the wrong failure modes: workers could restart mid-batch, deploys could interrupt long-running work, downstream limits could force broad retries, and coordination logic had to answer questions like, "Is this the last job?" under load.
So, we rebuilt our document processing system on our new Job Framework, the internal backbone we use to orchestrate long-lived, observable background work
Workflow state is durable. A worker crash or deploy mid-batch resumes instead of restarting the whole batch. Each activity has explicit timeout and retry behavior. File-level failures are isolated: if one document is corrupt, password-protected, unsupported, or empty, the workflow marks that file and continues processing the rest.
That changed the failure model. The workflow is no longer a chain of jobs coordinated by hand. The Job Framework is the coordinator and gives us queue isolation, task routing, observability, and regional worker management.
Splitting the Pipeline by Bottleneck
A year ago, much of the system pressure was hidden inside one broad "process this document" path. As Vault and connector ingestion grew, the bottlenecks separated.
Extraction was dominated by file format, OCR, and conversion behavior. Chunking and embedding were dominated by chunk volume and embedding-model throughput. Indexing was dominated by vector-store writes, large intermediate blobs, and downstream backpressure.
So we split the pipeline along those boundaries.
Extraction now has dedicated capacity because OCR-heavy and conversion-heavy files can be slow without starving the rest of the system. Chunk/embed and indexing are split because they fail and scale differently. Chunk/embed produces the intermediate representation; indexing consumes it and writes to the vector store.
That split lets each stage retry independently, scale independently, and fail partially without turning one bad file into a failed batch. An OCR-heavy upload can slow the extraction lane without starving indexing. A vector-store rate limit can back off the indexing lane without forcing extraction to retry. A few bad documents can be marked failed while the rest of the batch continues.
Making Document Format a Scaling Boundary
At this volume, intermediate formats are infrastructure. The pipeline writes and re-reads large artifacts between stages. A format that looks harmless at small scale can become a memory multiplier when parsed tens of millions of times a week.
One example here is UDF, the Unified Document Format. Before UDF, a lot of extraction output moved around as one big Pydantic-shaped document object. That was fine for a while, but it started to get expensive as more downstream systems only needed one slice of the document: page text, tables, images, or a lighter-weight view for navigation.
UDF changed that into a versioned internal format with typed pieces of the document. In our benchmarks, that translated into lower extraction latency across the distribution: p50 fell by about 19%, p90 by about 17%, and p99 by about 11%, with no observed output-quality regression.
The more important part was the boundary. We can keep improving extraction, table handling, image handling, multimodal retrieval, and future extraction backends without forcing every downstream consumer to know about one monolithic document object.
Reworking the Indexing Hot Path
The Challenge: Live Vector DB Migration
Our original vector-store architecture couldn't handle today's volume, hitting limits across memory pressure, bulk indexing, and cache management. To scale, we initiated a live migration of our primary Vector Database.
To maintain retrieval quality without downtime, we adopted an incremental rollout:
Dual-writing
to both systems simultaneously
Validating
at scale via shadow reads and backfills
Promoting
the new database once stabilized
While this migration solved many of our immediate scaling and reliability problems, it created some new challenges.
Dual-writing temporarily forces indexing workers to hold both working sets, increasing memory pressure and making vector-store backpressure highly visible.
As part of the migration, we needed to handle backoffs from our new Vector DB, while balancing and resource utilization and embedding usage. We decided to persist our embeddings to avoid embedding the same data multiple times. This new embedding persistence had the unintended consequence of increasing latency and memory utilization of our pipeline.
Optimization: Moving to Arrow IPC
One of the improvements we made to mitigate the increased memory usage and reduce latency was to replace the heavy JSON serialization/deserialization with
Arrow IPC
in the embed-to-index handoff. This change reduced Serialization/Deserialization time, the payload size and the memory footprint!
Backpressure Instead of Collapse
At scale, downstream systems hit limits, and continuing to run performantly under these conditions is essential for our customers. Vector stores return rate limits. OCR providers slow down. Blob reads time out. Conversion services hang on pathological files.
The scaling work is turning those events into fallbacks and slower drains rather than system-wide failures.
Extraction runs through ordered fallback chains
. Eligible OCR traffic starts with a primary path, then falls back through Harvey-operated services and deterministic local paths. Controlled failures fall through to the next option rather than immediately failing the file.
Vector DB rate limits use
explicit backoff and retry accounting
. Oversized writes can be split. Long-running activities persist enough state to avoid losing all progress on retry. The system distinguishes a bad document from a saturated dependency, and it handles those two cases differently.
Observability is part of the control loop
. Stage-level metrics, blob read/write duration buckets, task-slot saturation monitors, storage-account tags, and precise failure taxonomies tell us whether we are looking at a difficult file, a saturated dependency, a regional storage path, or a queue-level capacity issue.
Document
ingestion is bursty
. A Vault upload or connector sync can drop millions of documents into the system, then go quiet. CPU alone is a late signal for that kind of load because the real pressure is work waiting in the queue, downstream rate limits, and stage-specific saturation.
Today, the production story is stage-specific capacity control: separate task queues, separate worker counts, per-stage memory sizing, rate limits, task-slot monitors, and activity-level retry budgets. That is what lets the system absorb different bottlenecks independently.
The next phase is broader metrics-driven autoscaling across document-processing and Job Framework worker pools. Queue backlog, in-flight work, downstream rate-limit headroom, and worker saturation are the signals that map to document-processing load. The goal is capacity that follows the queue in near real time rather than chasing CPU after the fact.
Where This Leaves Us
Most of the architecture described above is already live in production: Job Framework workflows, dedicated extraction/chunk/embed/index queues, Vector DB dual-write and shadow-read migration paths, Arrow IPC for the embedding handoff, parallel range downloads for the chunk-embedding blob, and heartbeat-persisted retry budgets.
The remaining work is mostly about finishing the migration and removing temporary costs. The legacy vector-store path retires once shadow reads, backfills, and scoped migrations are complete. The split chunk/embed and index path becomes the default everywhere it applies. Temporary dual-write memory overhead comes down once one write path retires.
The next set of problems is less about whether the system can process a giant batch at all, and more about how quickly capacity follows the work. Slow OCR and conversion-heavy files continue moving into more isolated lanes. Parallel blob reads expand beyond the hottest embedding handoff. Autoscaling moves from explicit queue sizing toward metrics that track the work itself: backlog, in-flight activities, rate-limit headroom, and worker saturation.
The throughput curve is not flattening. The work now is to keep cost, latency, and failure behavior predictable while the curve keeps climbing.
Acknowledgements
As always, this isn’t the work of a single person or team, it takes a village and time. So many people contributed to these efforts in so many ways, but a special thanks to: Zhiyi Chen, Qige Chen, Samer Masterson, Malay Keshav, Nijanthan Hariharan, Niranjhan Kantharaj, Steven Zhou, Surya Keswani, and Ganesh Jothikumar.
Next Up
Building a Faster, More Reliable Upload Experience in Vault
Why we Built our own Cloud Agent Infrastructure
Building an Agentic Security Operations Center
Unlock Professional Class AI for Your Firm
Request a Demo
Copyright © 2026 Harvey AI Corporation. All rights reserved.
Platform
Overview
→
Agents
→
Vault
→
Knowledge
→
Shared Spaces
→
Command Center
→
Contract Intelligence
→
Ecosystem
→
Harvey Mobile
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
Company
Customers
→
Security
→
About
→
Careers
→
Newsroom
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
Instagram
→
Copyright © 2026 Harvey AI Corporation. All rights reserved.
