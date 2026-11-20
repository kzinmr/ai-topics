---
title: "How We Built Agentic Retrieval for Patent Research"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/how-we-built-agentic-retrieval-for-patent-research"
scraped: "2026-11-20T06:00:37.403906+00:00"
lastmod: "2026-11-19T16:00:00.000Z"
type: "sitemap"
---

# How We Built Agentic Retrieval for Patent Research

**Source**: [https://www.harvey.ai/blog/how-we-built-agentic-retrieval-for-patent-research](https://www.harvey.ai/blog/how-we-built-agentic-retrieval-for-patent-research)

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
Review Tables
→
Connected, cited tables your team builds on
Legal Work Orchestration
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
Services
→
Harvey’s experts, working alongside your team
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
Review Tables
Connected, cited tables your team builds on
Legal Work Orchestration
Orchestrate legal work with agents
Apps
Contract Intelligence
AI contract review and negotiation
Horizon Scanning
Track and act on regulatory changes
Intake
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
Services
Harvey’s experts, working alongside your team
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
How We Built Agentic Retrieval for Patent Research
In Harvey, an agent navigates fragmented patent sources, decides what information to seek next, and conducts focused research within a bounded budget.
by
Zhonglei Wang
and
Blake Chizen
•
Nov 19, 2026
Patent research often requires more than finding a document. A question about a claim may depend on its history: how it changed during examination, how the applicant addressed prior art, and whether later proceedings affected its status.
This is the central challenge of patent research:
the answer often depends on following a record over time and deciding what to inspect next
. Patent attorneys do this naturally. They start with one document, notice a later event or missing fact, open another record, and continue until the question is supported, or until they can clearly identify the remaining gap.
Consider a question that sounds simple:
What does claim 8 cover?
A conventional retrieval system can find the patent and return claim 8 as issued. But depending on what the attorney needs to know, the question may involve:
What did the application originally claim?
What language appeared in the issued patent?
How did the applicant distinguish the claim from prior art?
Is the claim still in force today?
Traditional retrieval-augmented generation (RAG) searches a fixed index, selects relevant passages, and generates an answer. That works when the information is already in one collection and the research path is predictable. In patent research, a result may reveal another record to inspect or another fact to verify.
Harvey’s patent research agent starts with a research question, identifies the information needed to answer it, and selects sources based on what they contain. As it reviews the record, each result guides the next search. The rest of this post explains why a single patent index may fall short, how Harvey’s agent selects sources, and how it uses each result to decide what to search next.
Why a Single Patent Index Falls Short
Patent information is scattered across sources built for different purposes.
Published patents
contain claims, specifications, abstracts, and drawings.
Patent-office systems
contain application metadata, prosecution events, Office Actions, assignments, reexaminations, and PTAB proceedings.
Patent indexes
support broad full-text and semantic discovery.
Web sources
help cover international patents, procedural materials and jurisdictional gaps. Each source also has its own boundaries and limitations.
Combining these sources into one corpus would be costly to build and maintain. Each new jurisdiction or provider would require more ingestion and normalization, while a larger index alone would not tell the system what information a question needs. The system also needs to recognize when a source is incomplete, choose an alternative, and decide whether the information answers the question or calls for another search.
Our Solution: Agentic Retrieval Across Patent Sources
Each research task starts with the question to be answered. Harvey passes it to the patent research agent as a
research objective
. The agent identifies the
information
needed and selects from the
sources
available for that run.
Figure 1. The objective determines what information is needed, which then determines the sources that are eligible.
1. Research Objective
The objective describes what the answer must establish without prescribing every retrieval step. Preserving the user’s full question — including patent numbers, claim numbers, timing, and legal context — lets the research agent plan from the desired outcome rather than from a reduced bag of keywords.
2. Required Information
For recurring research patterns, we give the agent concise paths:
Research Task
Typical Path
Current claim status
Issued claim → reexamination or PTAB history → controlling certificate or decision
Art applied by an examiner
Office Action record → substantive rejection reasoning → cited reference
PTAB outcome
Proceeding → decision listing → controlling paper
Prior-art research
Target claim scope → candidate references → timing and feature comparison
We do not attempt to enumerate every patent research task. Patent questions are too varied for a fixed decision tree. The built-in paths cover important recurring patterns, while the agent can construct additional paths from the objective and the information it discovers.
These are information requirements, not hard-coded source assignments. The same claim text, decision, or family relationship may be available from more than one source. The agent can choose among the sources available to it at runtime.
3. Eligible Sources
The agent receives a routing table assembled from the sources enabled for the run. Within the table, each data source tells the agent:
What data it has
Which information needs it serves best
Where its material boundaries lie
Which alternative data source can be a fallback
The routing guidance also sets source priorities and fallbacks. For example, it prioritizes the USPTO for U.S. patent text and identifies Google Patents as an alternative when the USPTO isn’t available in the run.
With this design, the query from earlier (
What does claim 8 cover?
) runs as follows:
Objective:
Determine the claim’s scope and whether that scope remains operative.
Required information:
Retrieve the issued claim and any later record capable of changing its status.
Eligible sources:
Start with authoritative U.S. patent and post-grant records, using another enabled source when the preferred record is incomplete.
Research:
Inspect the issued text, follow any relevant reexamination or PTAB record, and reconcile the two.
Stop:
Return a cited answer when the objective is supported, or clearly identify the unresolved gap within the run’s bounded research budget.
The research path can change as the agent reviews information. A result may reveal another need, point to an eligible fallback source, or show that the objective is supported. The agent stops when it can return a cited answer, identify what remains unresolved, or if it reaches the run’s research budget.
Looking Ahead: A Shared Information Layer for Patent Workflows
Today, users can attach Patent Research as a knowledge source in Harvey.
The
objective → required information → eligible sources
model gives each workflow a stable way to request information without coupling it to a provider. Over time, this approach could extend to non-patent literature, international patent-office records, licensed sources, and authorized private records. Each workflow could request the information it needs through the same model, while the agent selects among the sources available to it.
This creates a path for new patent workflows to draw on a shared retrieval layer as Harvey’s patent capabilities develop.
Request a Demo
Thank you!
We'll be in touch shortly.
Next Up
Building Ethical Wall Enforcement Into Harvey
How We Made Review Tables Faster and More Reliable
How Harvey is Building a Frontier Marketing Org
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
Review Tables
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
Facts & Chronologies
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
