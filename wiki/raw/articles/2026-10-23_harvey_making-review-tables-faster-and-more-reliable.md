---
title: "How We Made Review Tables Faster and More Reliable"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/making-review-tables-faster-and-more-reliable"
scraped: "2026-10-23T06:00:37.794209+00:00"
lastmod: "2026-10-22T16:00:00.000Z"
type: "sitemap"
---

# How We Made Review Tables Faster and More Reliable

**Source**: [https://www.harvey.ai/blog/making-review-tables-faster-and-more-reliable](https://www.harvey.ai/blog/making-review-tables-faster-and-more-reliable)

We Raised $550M at a $15.5B Valuation to Help Legal Teams Own Their Intelligence
Learn more
We Raised $550M at a $15.5B Valuation to Help Legal Teams Own Their Intelligence
Learn more
We Raised $550M at a $15.5B Valuation to Help Legal Teams Own Their Intelligence
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
Spaces
→
Work with legal teams across organizations in secure, shared spaces.
Command Center
→
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
Contract Intelligence
→
Surface insights, strengthen negotiations, and accelerate reviews.
Horizon Scanning
→
Track, assess, and take action on regulatory changes.
Intake
New
→
Capture, route, and resolve legal Intake from across the business.
Connector Library
New
→
Bring your team’s tools into Harvey with security-reviewed connectors or custom MCP.
Legal Work Orchestration
New
→
Assign, execute, and review legal work with agents and your team.
Overview
For In-House
→
For Law Firm
→
For Mid-size Firm
→
Industries
Healthcare & Life Sciences
→
Energy & Utilities
→
Technology
→
Media, Entertainment & Telecom
→
Practice Area & Teams
Litigation
→
Transactional
→
Innovation
→
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
Research
→
Models, benchmarks, and field notes from Harvey's research on the frontier of legal AI.
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
Spaces
Work with legal teams across organizations in secure, shared spaces.
Command Center
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
Contract Intelligence
Surface insights, strengthen negotiations, and accelerate reviews.
Horizon Scanning
Track, assess, and take action on regulatory changes.
Intake
New
Capture, route, and resolve legal Intake from across the business.
Connector Library
New
Bring your team’s tools into Harvey with security-reviewed connectors or custom MCP.
Legal Work Orchestration
New
Assign, execute, and review legal work with agents and your team.
Solutions
Overview
For In-House
For Law Firm
For Mid-size Firm
Industries
Healthcare & Life Sciences
Energy & Utilities
Technology
Media, Entertainment & Telecom
Practice Area & Teams
Litigation
Transactional
Innovation
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
Research
Models, benchmarks, and field notes from Harvey's research on the frontier of legal AI.
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
How We Made Review Tables Faster and More Reliable
Harvey engineers redesigned Review Table loading for reviews spanning thousands of documents, fetching rows page by page so large tables open faster and stay responsive.
by
Shrihari Murlidharan
and
Stella Ge
•
Oct 22, 2026
The Review Table is Harvey’s largest, most exhaustive inference engine, allowing users to analyze thousands of legal documents and standardize insights using natural language. Lawyers can ask questions against uploaded documents and obtain the results in a structured tabular format, with rows corresponding to individual documents and columns mapping to the questions. Each cell answer includes the model’s reasoning and is backed by citations from the source document.
Review Tables are also designed to be a living, collaborative surface: rows can be assigned out to collaborators for review, answers can be verified or locked, and users can leave comments for further discussion. Once verified, teams can lean on their review table as a reusable, validated source of truth for their next memo or presentation without needing to recreate their insights from scratch.
That collaborative workflow depends on the table remaining responsive as it grows. As teams began querying hundreds of columns across thousands of files, loading the full table in the browser caused delays and, in the largest cases, could prevent it from loading at all. This post explains how we changed the table’s data and loading paths to support larger reviews while preserving sorting and filtering.
When Browser Loading Hit its Limits
Historically, all table operations were performed on the client side. The browser loaded the entire Review Table from the blob store and performed sorting, filtering, and any sort of aggregation in-memory. While this solution worked for small Review Tables, we saw performance issues once the table exceeded thousands of rows.
When Review Tables adoption and usage skyrocketed, we saw that tables sometimes experienced lag times or became unresponsive. For extremely large tables, browsers could potentially run out of memory or fail to load entirely.
It may seem like solving this scaling problem is straightforward. Since it’s a table data structure at its core, we
should
be able to address this problem by implementing server-side pagination. In reality, there’s two main things that prevent this fix:
The requirement to segregate sensitive data
. Client data at Harvey is extremely sensitive and as such, only the metadata lives in Postgres while raw customer data lives in Azure blobs. The data had to be fetched from Azure at request time, merged with Postgres data, and passed from the backend to the client. In order to support server-side pagination with filtering and sorting, we would need an interface to query on top of Azure blob store.
There is no existing grid library that supports the kind of pagination scheme this would require
. As a result, we had to come up with our own abstractions for page loading strategy, factoring in grouping by folder path, sorting, and filtering. In order to ensure this implementation achieved parity with our existing features, we built our own versions of table functionality for row selection and expanding/collapsing sections that we no longer got for free from our current grid library.
How We Implemented Pagination
Choosing a data store
In order to scale the user interface, we moved all client side operations to the server side. This necessitated a reliable data store that both satisfied our segregation requirements and exposed a rich querying interface with aggregation. Postgres would still be our source of truth while the new data store would provide the read interface (CQRS pattern).
Turbopuffer is a vector data store that runs on top of existing Azure blobs while supporting vector search (ANN, KNN), full text search (BM25), and straightforward filtering through an inverted index. Turbopuffer organizes data into documents which belong to a namespace. A namespace has a strict defined schema. This fit in neatly with our requirements, but there were still some open questions that needed to be addressed before we could implement successful server side pagination:
Pagination support
: Turbopuffer doesn’t support pagination out of the box, so a cursor-based or limit/offset solution was out of question.
After considering multiple alternatives we landed on an ID based pagination. The backend returns a list of row ids that are ordered based on how they would appear on the UI. Any sort/filter operations would refetch this list. The client can request data for an arbitrary list of row ids, which gives us the flexibility to support adhoc page loads of variable widths while keeping the implementation and loading overhead to a minimum.
Data type aware sorting/filtering
: Review Tables support different column types, like currencies and dates, which need to be sorted by their values and not lexically. Since LLM responses are not guaranteed to conform to data types and Turbopuffer requires strict data type conformance, we needed a design that worked around these limitations.
We ended up dual projecting strict data types, the first field mapping to the respective data type and the second field mapping to a String data type. This gives us the ability to support data type aware sorting and filtering
Schema drift
: Turbopuffer has a strict typing requirement enforced through a schema. Any failure in writing to the schema could cause a permanent drift between the Postgres+Azure and the Turbopuffer data sources.
In a dual write system drifts are inevitable, even after retries, and the concern here is to minimize the impact for end users. So when a schema drift is detected we immediately fall back to the Postgres logic, and drifted schemas can be healed by a backfill job
Schema evolution:
Even though every table data differs, there are some core attributes, like timestamps and row status, that are common across all tables and evolve over time. We needed to design a system for schema evolution as we add more core attributes.
The setup layer
The Review Table data lives in two separate places: Postgres and Turbopuffer. Both of them are backed with blob storage. The lifecycle of Review Table data is as follows:
When the user creates a table we first generate the table skeleton — the row, column, and cell objects — and persist them in Postgres, while sensitive data lands in a segregated Azure blob. We also derive the schema for the table and persist it in Turbopuffer.
When the cells are actually generated, we write them to both Postgres + blob storage and Turbopuffer while batching the writes to Turbopuffer.
If any writes to Turbopuffer fail, we immediately direct any reads to fall back to Postgres while a backfill job fixes the broken Turbopuffer namespace.
Cells that have a non-string data type (date, currency, classification) have dual representation in Turbopuffer as strictly typed fields and as string fields in order to support both range queries on numerical/date fields and membership queries on classification fields.
Loading strategy
Our guiding principle is to reduce perceived latency of Review Table load for our end users. We accomplish this by employing a multi-phased loading strategy.
Skeleton first
The frontend first requests a slim representation of the table so it can populate essential fields like table status, columns, and metadata on the files in the table.
Sort column values
The Review Table is always sorted by one of its columns (file names by default). We wanted to support the best possible user experience with pagination by allowing users to click arbitrarily along the length of the scrollbar to go to different sections of the table. In order to support this, we needed to load all the values in the sort column, in sorted order, to determine which rows to request from the backend.
Once the skeleton and sort column values are loaded, we can render a table outline with the row and column headers populated, in the proper order. We show a loading animation in the cells to indicate that the data is coming soon.
Loading the rows
The frontend then calculates the range of rows represented by the user’s current page, taking into account any sorts and filters that have been applied. The backend takes those bounds, queries Turbopuffer, then returns all rows within the page to be rendered. We make requests for additional pages as the user continues to scroll through the table, with a cap on how many rows we hold in memory at once.
The same steps apply when a user changes the sorted column or adds filters to the table. We re-request sort column values with updated parameters, then subsequently fetch new pages of rows.
Results
On the technical side, we saw immediate latency wins across all table sizes, with load improvements compounding on larger tables. Most critically, tables that used to break now load, and do so quickly.
Number of Cells in the Table
Speedup Improvement
<1K
1.2x
1K-10K
2.2x
10K-100K
5.8x
100K-500K
4.2x
Customers have called this change a massive improvement, reporting that Review Tables feel noticeably faster, making it easier to get more work done in Harvey. That matters because lawyers routinely work across hundreds to thousands of documents, and much of a Review Table’s value comes from seamlessly filtering and sorting to zero in on the right comparison.
As we continue building more powerful capabilities into the Review Table, we can rely on this new foundation, where any comparison a lawyer wants to make is possible at any scale.
Acknowledgements
Thank you to the following members of Harvey’s EPD team for their contributions to this project: Brian Ford, Prithvi Kannan, Jessica Peng, Charlie Samuels, Grace Hong, Anojen Jeyapalan, Yena Oh, Jeffrey Li Kwong Ken, Stephen Rice, John Graham, Guru Sivanesan.
Next Up
How Harvey is Building a Frontier Marketing Org
Building Harvey’s MCP Policy Engine
How We Built Harvey’s Connector Library to Work Across External Tools
Unlock Professional Class AI for Your Organization
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
Spaces
→
Command Center
→
Contract Intelligence
→
Horizon Scanning
→
Ecosystem
→
Intake
→
Partnerships
→
Solutions
Innovation
→
Transactional
→
Litigation
→
In-House
→
Law Firms
→
Mid-Sized Firms
→
Healthcare & Life Sciences
→
Energy & Utilities
→
Technology
→
Media, Entertainment & Telecom
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
