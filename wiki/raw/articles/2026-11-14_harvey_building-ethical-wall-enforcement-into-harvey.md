---
title: "Building Ethical Wall Enforcement Into Harvey"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/building-ethical-wall-enforcement-into-harvey"
scraped: "2026-11-14T06:00:24.083380+00:00"
lastmod: "2026-11-13T16:00:00.000Z"
type: "sitemap"
---

# Building Ethical Wall Enforcement Into Harvey

**Source**: [https://www.harvey.ai/blog/building-ethical-wall-enforcement-into-harvey](https://www.harvey.ai/blog/building-ethical-wall-enforcement-into-harvey)

:Harvey:
Products
Solutions
Customers
Security
Resources
Company
Platform
Overview
→
One platform for all legal AI work
Agents
→
AI agents designed for legal work
Vault
→
Store and analyze legal documents
Knowledge
→
Legal, regulatory, and tax research
Spaces
→
Secure, shared legal workspaces
Command Center
→
Analytics to lead AI transformation
Memory
→
AI that remembers your preferences
Legal Work Orchestration
New
→
Orchestrate legal work with agents
Apps
Contract Intelligence
→
AI contract review and negotiation
Horizon Scanning
→
Track and act on regulatory changes
Intake
New
→
Capture and resolve legal requests
Facts & Chronologies
New
→
Connect facts, strengthen your case
Connect
Connector Library
New
→
Connect your tools to Harvey via MCP
Ecosystem
→
Use Harvey wherever you work
Overview
For In-House Teams
→
For Law Firms
→
For Mid-Size Firms
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
Public Sector
→
Practice Area & Teams
Litigation
→
Transactional
→
Innovation
→
Featured
A New Era of Collaboration for Legal and Professional Services
→
Law firms and professional service networks have been using Harvey to build new service models and add value collaboratively.
Blog
→
Product updates, insights, and behind-the-scenes from the Harvey team
Resources Hub
→
The latest videos, webinars, guides, and reports from Harvey
Research
→
Research on the frontier of legal AI
Press Kit
→
Official logos and brand guidelines
Support Hub
→
Product documentation and trainings
Featured
Four Legal AI Workflows to Help Mid-Sized Firms Take on More
→
Explore four practical legal AI workflows that help mid-sized law firms expand capacity, improve matter economics, and take on more complex work.
About
→
Who we are and what we're building.
Careers
→
Join our team and help Harvey shape the future of professional services.
Newsroom
→
Press releases and partnership announcements.
Featured
Harvey Raises $550M at a $15.5B Valuation to Help Legal Teams Own Their Intelligence
→
Login
Request a Demo
Products
Platform
Overview
One platform for all legal AI work
Agents
AI agents designed for legal work
Vault
Store and analyze legal documents
Knowledge
Legal, regulatory, and tax research
Spaces
Secure, shared legal workspaces
Command Center
Analytics to lead AI transformation
Memory
AI that remembers your preferences
Legal Work Orchestration
New
Orchestrate legal work with agents
Apps
Contract Intelligence
AI contract review and negotiation
Horizon Scanning
Track and act on regulatory changes
Intake
New
Capture and resolve legal requests
Facts & Chronologies
New
Connect facts, strengthen your case
Connect
Connector Library
New
Connect your tools to Harvey via MCP
Ecosystem
Use Harvey wherever you work
Solutions
Overview
For In-House Teams
For Law Firms
For Mid-Size Firms
Industries
Healthcare & Life Sciences
Energy & Utilities
Technology
Media, Entertainment & Telecom
Public Sector
Practice Area & Teams
Litigation
Transactional
Innovation
Featured
A New Era of Collaboration for Legal and Professional Services
Law firms and professional service networks have been using Harvey to build new service models and add value collaboratively.
Customers
Security
Resources
Blog
Product updates, insights, and behind-the-scenes from the Harvey team
Resources Hub
The latest videos, webinars, guides, and reports from Harvey
Research
Research on the frontier of legal AI
Press Kit
Official logos and brand guidelines
Support Hub
Product documentation and trainings
Featured
Four Legal AI Workflows to Help Mid-Sized Firms Take on More
Explore four practical legal AI workflows that help mid-sized law firms expand capacity, improve matter economics, and take on more complex work.
Company
About
Who we are and what we're building.
Careers
Join our team and help Harvey shape the future of professional services.
Newsroom
Press releases and partnership announcements.
Featured
Harvey Raises $550M at a $15.5B Valuation to Help Legal Teams Own Their Intelligence
Request a Demo
Login
US
EU
AU
Technical
Building Ethical Wall Enforcement Into Harvey
How we bring a firm’s matter restrictions into document access, search, and AI work.
by
Shuaiwei Cui
,
Lilly Xia
, and
Nick Howlett
•
Nov 13, 2026
Imagine a lawyer using Harvey to analyze documents for Acme Corporation’s confidential acquisition. A colleague is barred from accessing information about the deal. That restriction must also apply to conversations and other work created from those documents, even if someone shares the work with the colleague.
Law firms organize work around matters, such as a deal, lawsuit, or advisory engagement. An ethical wall, also called an information barrier, limits who can access information about a matter. An inclusionary wall allows access only to people on its list; an exclusionary wall blocks the people on its list and allows everyone else in.
Bringing ethical walls into an AI platform means protecting information wherever it is used. Firms manage matter records and wall policies in their own systems, and Harvey imports them. A document management system (DMS) enforces walls on the documents it stores. But Harvey also creates conversations, tables, and drafts from those documents. Because that work lives in Harvey, our platform must enforce the walls on it too.
To do that, Harvey links resources — including Vault projects and files, conversations, and Review Tables — to Client Matters and their walls.
This creates three engineering challenges:
Import matters and walls reliably, at the scale of a large firm
Help people find the matters they can access
Enforce walls the same way across different kinds of work
The rest of the blog explains the architecture Harvey uses to carry each firm’s ethical wall rules across the platform, from the matter model to the safeguards around wall data.
Figure 1. Harvey imports matters and walls from firm systems. On every request, it checks both resource permission and matter clearance.
Importing Client Matters and Walls
Before Harvey can enforce a wall, it needs the matter and its policy. Our import architecture separates matter identity from access policy. Provider adapters translate data from each wall provider into one common model. Each firm’s data stays in its own workspace, the firm’s private Harvey environment.
Two separate sync jobs
We split import into two jobs.
Client Matter sync
finds matters in the external system and links each one to an existing Harvey Client Matter or creates a new one. When walls are enabled, it can also set up the matter’s wall.
Wall sync
refreshes the policy for matters already linked to the external system. It fetches each matter’s current policy, matches the people on it to Harvey users, applies membership changes, and updates whether the matter is open or walled.
We keep these jobs separate for three reasons:
Each job can run on its own schedule.
A firm opens new matters at a steady pace, but a wall can change at any moment, for example when a lateral hire arrives with a conflict. Wall sync can run on demand without a scan of the full matter catalog.
A failure in one job does not block the other.
If a wall fetch fails for one matter, matter import continues. If matter import stalls, existing walls still refresh.
Firms do not have to adopt both at once.
Matter data and wall data often live in different systems. A firm can bring its matters into Harvey before it turns on walls, or without walls at all.
For supported integrations, Client-Matter-only sync links an imported document collection to its matter in Vault, even if the firm has not set up walls in Harvey. The project is filed under the right matter from the start.
Figure 2. Import architecture. Matter sync and wall sync are separate jobs. Each runs on a recurring schedule, as a one-time bulk run, or for a single matter.
Recurring and ad hoc execution
Durable workflows run bulk syncs. A direct service refreshes the policy for one matter on request. Recurring schedules keep matter records and wall policies up to date, and a firm can choose its own schedule. Where webhook integration is available, wall changes can also reach Harvey as they happen, with scheduled sync as a backstop.
One-time bulk runs, such as a first import or a reconciliation, start at once. Both kinds of run use the same orchestration on Temporal, a durable workflow engine that provides retries, resumable batches and visibility into partial failures. Each workflow finds its work and splits it into bounded batches. It then processes the batches with controlled concurrency. Retries target only the matters that failed. Each run records its progress and failures in a sync report.
For an urgent change, a Client Matter admin at the firm can refresh one matter’s policy on demand. The refresh fetches and applies the policy at once, without waiting for the next scheduled run. It reuses the provider and policy logic of background sync, and it leaves the recurring schedule in place.
When a sync goes wrong
Harvey matches the people on a wall to Harvey users by email address. Sync is designed so that a failure does not open a wall:
If Harvey cannot fetch a matter’s policy, it keeps the last policy it stored. It retries that matter, and the rest of the batch continues.
If Harvey cannot look up every person on an exclusionary wall, it skips the update and keeps the last policy. A failed lookup does not take anyone off a block list.
If Harvey cannot match a person on an inclusionary wall, it leaves that person off the list, so they stay out.
Efficient, Wall-Aware Client Matter Search
In Harvey, most work starts with the Client Matter picker. This is where people choose the matter for a conversation, a Vault project, a Review Table, or a Space.
Figure 3. The Client Matter picker in a new conversation, searching by client name. The matters shown are fictional.
The picker must be fast. Choosing a matter should be a quick step on the way to the real work, even for a very large firm. Our largest workspace has about 1.7 million matters.
People do not always remember a matter code. They may remember the client’s name, the matter name, a few words from its description, or the name of its Space. The picker should let them search using any of these details.
To support this, we are moving the picker to a dedicated search index built on turbopuffer. Each workspace has its own search index, with one entry per matter. The index combines the matter code, client name, matter name, description, and Space name in one record, so a search can look across those fields without joining several database tables.
The database stays the source of truth. When a matter changes, Harvey copies the change to the index in the background, and a reconcile sweep repairs any update that was missed. If the index is slow or unavailable, the picker falls back to the database.
Figure 4. Client Matter search. Harvey combines Client Matter, client, and Space data in a search index. It checks access before it returns results.
Harvey uses the index to find matching matters, then loads those matters from the database and checks the wall policy stored there before returning results. The index contains searchable text, not wall data, so a delayed index update does not determine whether someone can access a matter.
For users without wall-management access, a walled matter they aren’t cleared to access does not appear in the picker, even as a locked entry. Wall administrators can see every matter in the list so they can manage it, but seeing a matter there does not give them access to its walled work.
Enforcement Across Harvey Product Surfaces
The wall rules are consistent across Harvey, but each type of resource needs a different access check.
A document collection holds items that Harvey can often check one at a time.
A conversation may already contain information drawn from several documents.
Sharing adds another layer, because the people who receive the work may have different clearance from the person who made it.
One policy engine decides every wall question, so each product surface applies the same rules. Access requires the right resource permission and clearance for every linked Client Matter. Each resource type decides which matter links apply, and how the result shapes what the user sees.
Admin roles do not get past walls. Workspace admins and Space admins can open walled work only if the wall lets them in.
Document collections and individual files
Lawyers often reuse documents from other matters. They start from a precedent agreement, adapt a brief from an earlier case, or compare terms with a past deal. So a file can carry its own matter link, separate from the Vault project that holds it. A precedent from Matter B keeps Matter B’s wall, even inside a Matter A project.
Harvey supports two ways to handle a project that contains files from multiple matters:
Filtered view.
A user can open the project and sees only the files they’re cleared to access. For example, Alice has clearance for Matter A, while Bob has clearance for Matters A and B. Alice sees the Matter A files; Bob sees both the Matter A files and the Matter B precedent.
Restricted view.
A user needs clearance for every matter represented in the project before they can open it.
Either way, a user never sees a file that its wall keeps them from.
Conversations
The Client Matter shown in a conversation identifies and organizes the work. But the sources used in the conversation can link it to more matters:
A file attached to the conversation adds that file’s matter.
A Vault project used as a source adds the project’s matter and the matter of every file in it, not only the files cited in an answer. Because a conversation may draw on any file in the project, Harvey applies the wall restrictions for all of those matters.
To open the conversation, a user needs clearance for all of these matters. Suppose a conversation shows Matter A and uses a file from Matter B. Alice has clearance only for Matter A, so she cannot open the conversation, even if someone shares it with her. Bob has clearance for both matters, so he can open it, as long as he also has ordinary access. Sharing work with someone does not clear them to see what it contains.
A matter link stays even if someone later removes the file. Earlier answers may already contain content from that file, so the restriction must outlive the attachment.
Agents and memory follow the same rules. A scheduled agent runs as the person who set it up. Before it reads a file, Harvey checks the file’s matter against that person’s walls. If a saved memory is tied to a matter, Harvey checks that matter’s wall before it uses the memory.
Figure 5. A conversation can link to more than one Client Matter. Access requires clearance for all of them.
Retrieval
Harvey’s file search knows about Client Matters. When a user searches a whole Vault project, the search index holds each file’s matter. So Harvey removes files from matters the user cannot access before it ranks the matches. Because of this filter, restricted files never take up places among the top results.
The search index is eventually consistent. A change to a file, or to its matter link, can take some time to reach the index. So before Harvey sends any returned file content to the model, it checks each returned file against the current policy it has stored.
Figure 6. Retrieval. A matter filter narrows the search. A final access check confirms each returned file before its content reaches the model.
Collaboration
Harvey checks walls when someone shares work, and again each time someone opens it, because clearance can change after a share:
A direct share to a person checks that person’s clearance at once. If a wall blocks them, the share dialog says that an ethical wall prevents sharing with them. It does not say which matter.
A share to a group checks each member when they open the work.
A share into a Space also checks the Space’s content policy.
When someone without clearance opens a link to walled work, Harvey responds as if the work does not exist. The response does not confirm that the work is there.
A Space is a shared area for work on a Client Matter. It may accept only work from its own matter, or work from other matters the user is cleared to access. In either case, Space membership does not override the wall on the Space or its content.
Walls bind the people in the firm’s own workspace. People from another organization, such as a client in a Shared Space, get access only through what the firm shares with them. Harvey checks walls when the firm shares, and an inclusionary wall blocks a share to anyone who is not on its list.
Storage at Scale
Many walls have exactly the same members. For example, a client team often works on many matters for one client, so each of those matters’ walls lists the same people. We store each distinct membership set once per workspace, and many walls can point to it.
A fingerprint, which is a hash of the normalized member list, helps us find a matching set fast. Two different lists could in theory share a fingerprint, so we compare the actual members before we reuse a set.
We never change a shared set in place. When one wall’s membership changes, we point that wall to a set with the new members. Every other wall stays as it was. This cuts duplicate data and keeps each wall’s policy independent. If we edited a shared set in place, the edit would silently change every wall that uses it.
Figure 7. Walls share identical membership sets. When one wall’s membership changes, only that wall moves to a new set.
Security
Wall data is sensitive in its own right. It can reveal client relationships, conflicts, and who works on which matter. The credentials that Harvey uses to fetch this data need the same care.
Harvey encrypts customer data at rest with AES-256 and in transit with TLS 1.2 or later. It keeps each customer’s data logically separate and applies least-privilege access controls. Integration credentials stay on Harvey’s servers, inside the same security boundary. Harvey does not train AI models on customer data, and its AI subprocessors are contractually prohibited from doing so.
Wall sync writes an audit event when it creates a wall, changes a wall’s membership, or removes a wall. Firm admins can see and export these events in Harvey’s audit log, and read them through the API. Together, they show how each policy changed over time.
Carrying Wall Policies Through Harvey
For firms, ethical walls need to keep protecting matter information as it moves from source documents into conversations, analysis, and shared work. Harvey imports the firm’s matter records and wall policies, then checks access against the stored policy on each request. The search index helps people find matters, but it does not determine access. Before file content reaches the model, Harvey checks each file against that policy. If a sync fails, Harvey retains the last known policy, so the failure does not remove the wall.
A shared matter model connects firm policies to documents and the work Harvey creates from them. Bounded sync jobs, a dedicated matter index, and shared membership sets help the system work at a large-firm scale. One policy engine applies the same wall rules as people search, create, and collaborate on legal work.
Next Up
How We Made Review Tables Faster and More Reliable
How Harvey is Building a Frontier Marketing Org
Building Harvey’s MCP Policy Engine
Unlock Professional Class AI for Your Organization
Request a Demo
Copyright © 2026 Harvey AI Corporation. All rights reserved.
Products
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
Memory
→
Legal Work Orchestration
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
