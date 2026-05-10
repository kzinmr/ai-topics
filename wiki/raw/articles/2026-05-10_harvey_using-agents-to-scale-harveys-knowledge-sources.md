---
title: "Using Agents to Scale Harvey’s Knowledge Sources"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/using-agents-to-scale-harveys-knowledge-sources"
scraped: "2026-05-10T01:27:19.658994+00:00"
lastmod: "2026-02-02T20:00:00.000Z"
type: "sitemap"
---

# Using Agents to Scale Harvey’s Knowledge Sources

**Source**: [https://www.harvey.ai/blog/using-agents-to-scale-harveys-knowledge-sources](https://www.harvey.ai/blog/using-agents-to-scale-harveys-knowledge-sources)

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
Using Agents to Scale :Harvey:’s Knowledge Sources
How we built an autonomous pipeline of AI agents to scale our knowledge sources from six to 60+ jurisdictions.
by
Samarth Goel
and
Chris Bello
•
Feb 2, 2026
Last month, a customer in São Paulo needed Harvey to analyze a specific ruling from Brazil's Superior Tribunal de Justiça. We had 72 hours. The problem: Brazilian federal case law wasn't indexed in Harvey, so the agent couldn't access the ruling.
A year ago, this would have triggered weeks of manual work — finding the repository, writing a custom connector, ingesting the data, hand-labeling test cases, iterating to improve retrieval and agent quality, and recruiting a Brazilian attorney for review.
But this time, our system had already flagged Brazilian federal courts as a coverage gap, validated the relevant online databases for commercial use, built a connector, and generated evaluation scenarios. When the customer ran their query, the agent successfully retrieved the ruling and answered correctly on the first try.
This post walks through how we built
The Data Factory
, an automated pipeline that discovers legal sources and turns them into tools for our
agents
. Since August 2025, this pipeline has helped Harvey scale its
knowledge source
coverage from just six jurisdictions to over 60, and from 20 unique legal data sources to more than 400.
Before we dig deeper, here’s a brief overview of the architecture we built at a high level:
Intake engine:
Discovers and validates new legal sources through automated jurisdiction mapping and compliance review, turning customer requests and coverage gaps into vetted, pipeline-ready data sources.
Evaluation pipeline:
Tests whether agents can actually use new sources to solve legal problems, using synthetic scenario generation, production simulation, and multi-agent quality assessment to validate performance before launch.
Configuration layer:
Defines each jurisdiction through a declarative config — domain lists, filter hierarchies, permissions, and agent instructions — that turns vetted sources into parameterized tools for a single unified reasoning agent.
Automated Discovery
The first challenge in building a global legal agent is understanding the topology of a jurisdiction. We need our agents to know where to look — whether that's primary legislation, case law, parliamentary records, or regulatory guidance.
To move beyond manual source requests, we built a
Sourcing Agent
. It maps a jurisdiction's legal infrastructure, identifies trusted repositories, and cross-references them against our existing tools to find gaps. By the time a user needs a specific tax ruling from a new jurisdiction, the Sourcing Agent has often already flagged the source, validated its domain authority, and queued it for tool creation.
We also built a
Legal Review Agent
that accelerates compliance review. It pre-analyzes terms of use, automated access policies, local copyright laws, and other relevant considerations, then extracts key clauses and flags restrictions. The output is a structured summary for our Legal team. Attorneys still review every source before it goes live — but they're reviewing distilled analysis, not raw documents. As a result, review throughput has doubled: attorneys now process
two to four sources per hour
, up from one to two.
From Six to 60+ Jurisdictions
After a source passes legal review, we need to turn it into a functional tool.
To accomplish this, our first step was to replace our hand-tuned system with a declarative configuration (config) layer. Each jurisdiction is defined by a single config object: the domains to search, the filter hierarchy for narrowing queries, the permissions required for access, and optional agent instructions. This means we can expand coverage in days rather than weeks, and every jurisdiction benefits from improvements to the shared infrastructure.
This configuration layer also shaped our agent architecture. A natural design would assign each jurisdiction its own specialized agent, but subagent handoffs can lose crucial conversation history, which can create friction during multi-turn legal research. Instead, we treat domain-specific sources as parameterized tools. The agent selects the relevant jurisdiction, and the configuration determines which curated sources to search. The result is a
single reasoning system that can fluidly move between Austrian court decisions and Brazilian statutes in the same conversation
.
“
Our curated domain lists ensure every result comes from a vetted government portal or authoritative legal database.
”
Why not just use open web search? Our customers care deeply about source authority. A law firm advising on German tax law needs results from official Bundesministerium der Finanzen guidance — not a blog post that happens to rank well. Open web search might surface the right answer, but it can't guarantee the source meets the evidentiary standards attorneys require. Our curated domain lists ensure
every result comes from a vetted government portal or authoritative legal database.
Evaluating Agent Performance
Once we give an agent access to authoritative sources in a new jurisdiction, how do we know it will reason correctly? General benchmarks fail on complex, siloed legal questions. A model might ace law school exams while botching the procedural nuances of filing a claim in the Commercial Court of Paris.
To solve this, we built a four-step evaluation pipeline that allocates compute asymmetrically: low budgets for agent execution (to mirror production latency), heavy compute for evaluation. This mirrors how a senior partner operates — efficient when asking questions, thorough when reviewing work. Each source evaluation consumes roughly 150,000 tokens.
Step 1: Answer-first scenario generation.
We don't just check if a URL is active; we check if an agent can use it to solve a problem. Early tests showed that general queries allowed agents to answer from base knowledge without citing documents, leading to false negatives due to lack of citations. To fix this, we use an "Answer-First" approach: A model identifies specific legal materials (like statutes and judicial decisions) within the source, then reverse-engineers a precise, fact-pattern-based scenario that forces the agent to find and interpret that material. Each query is paired with "underlying materials" (the specific statutes or decisions the evaluator expects to find), creating ground truth without human labeling.
Step 2: Production simulation.
We run these synthetic scenarios through a replica of our production environment. Our agents must demonstrate they can autonomously select the correct jurisdiction, navigate the relevant legal database, handle messy data formats (like scanned PDFs), and extract the relevant logic.
Step 3: Trace validation.
We feed the agent's reasoning trace, retrieved documents, and final answer into a multi-step evaluator. It verifies the process — did the agent reach the right content or did it get stuck on search results? — and enforces strict fact-checking. Hallucinated citations cause an automatic rejection. We use a two-stage decision flow: deterministic rules catch obvious failures (low number of citations per query or a high percentage of answers with poor citations), while a separate model handles nuanced cases in an uncertainty band.
Step 4: Multi-agent quality assessment.
An answer can be factually accurate but still miss the mark. To catch subtle failures, we deploy an ensemble of specialized agents:
URL Classification Agent:
Distinguishes real content (statutes, decisions) from navigation noise (homepages, search results). It analyzes URL structure and spot-checks page content via web search.
Citation Quality Agent:
Checks if the retrieved URLs actually support the legal arguments made.
Answer Quality Agent:
Evaluates whether the model’s legal reasoning would satisfy a licensed attorney.
Presentation Agent:
Scores clarity, structure, and tone.
Each agent assigns quantitative scores on a 1-5 scale, creating a multi-dimensional assessment.
Agent
Task
Sourcing Agent
Maps a jurisdiction's legal infrastructure, identifies trusted repositories, and cross-references them against our existing tools to find gaps
Legal Review Agent
Pre-analyzes terms of service, robots.txt, copyright assertions, and local database rights, then extracts key clauses and flags restrictions
URL Classification Agent
Distinguishes real content from navigation noise, analyzes URL structure, and spot-checks page content via web search
Citation Quality Agent
Checks if the retrieved URLs actually support the legal arguments made
Answer Quality Agent
Evaluates whether the reasoning would satisfy a licensed attorney
Presentation Agent
Scores clarity, structure, and tone
Decision Agent
Aggregates all signals, weighs citation distributions and consistency, then makes a pass/fail determination
Finally, a
Decision Agent
aggregates these signals, then makes a final pass/fail determination on the integration of that particular legal database into Harvey’s platform. Ambiguous cases route to human review. Everything else is automatically categorized, removing the need for expensive human-written datasets in dozens of jurisdictions across a wide range of practice areas.
Scaling Local Knowledge
With this work, we're moving beyond static retrieval toward agents that can navigate the legal web across 60+ countries. The goal is that when a customer in Jakarta, Lagos, or Munich runs a query, their agent already has access to the local sources that matter. We're continuing to invest in this pipeline so that regardless of where our customers are located, they will always have an agent equipped with the local knowledge they need.
And we're just getting started. Here's what we're building next:
Increasing coverage and quality.
We're continuing to expand into new jurisdictions while tightening our evaluation standards, improving citation accuracy, reducing latency, and catching edge cases our current pipeline misses.
Smarter source organization.
Today, sources are organized by jurisdiction. We're building a layer that also groups them by practice area — case law, tax codes, regulatory filings, parliamentary records — so agents can reason across source types, not just geographies. Imagine asking a transfer pricing question and having your agent pull from tax authority guidance in three jurisdictions simultaneously.
Novel experiences grounded in authoritative data.
With a foundation of vetted global sources, we can unlock capabilities beyond search: automated monitoring for regulatory changes, comparative law analysis across jurisdictions, and proactive alerts when new rulings affect a client's matters.
To learn more about how we can support your jurisdiction, reach out to your Harvey representative or contact our team below. If you're interested in building these types of agentic systems, check out our
open roles
.
Request a Demo
Unable to load form. Please try again.
Try Again
Thank you!
We'll be in touch shortly.
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
