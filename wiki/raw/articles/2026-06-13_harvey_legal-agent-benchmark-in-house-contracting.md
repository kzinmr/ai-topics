---
title: "Legal Agent Benchmark: In-House Contracting"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/legal-agent-benchmark-in-house-contracting"
scraped: "2026-06-13T06:01:04.978359+00:00"
lastmod: "2026-06-12T17:00:00.000Z"
type: "sitemap"
---

# Legal Agent Benchmark: In-House Contracting

**Source**: [https://www.harvey.ai/blog/legal-agent-benchmark-in-house-contracting](https://www.harvey.ai/blog/legal-agent-benchmark-in-house-contracting)

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
Agents
→
Purpose built agents execute complex legal work end to end.
Harvey Mobile
→
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
→
Access Harvey where you already work and ground every answer in sources you trust.
Contract Intelligence
→
Surface insights, strengthen negotiations, and accelerate reviews.
Command Center
→
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
Shared Spaces
→
Work with legal teams across organizations in secure, shared spaces.
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
Agents
Purpose built agents execute complex legal work end to end.
Harvey Mobile
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
Access Harvey where you already work and ground every answer in sources you trust.
Contract Intelligence
Surface insights, strengthen negotiations, and accelerate reviews.
Command Center
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
Shared Spaces
Work with legal teams across organizations in secure, shared spaces.
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
Insights
Extending :Harvey:’s Legal Agent Bench to In-House Contracting
Creating a benchmark to evaluate agents’ ability to negotiate contracts end-to-end.
by
Niko Grupen
,
Gabe Pereyra
, and
Julio Pereyra
•
Jun 12, 2026
Last month we released
LAB
, our benchmark for measuring long-horizon agent capabilities on legal work, and showed that it is an effective tool for measuring and improving agent capabilities. In our first extension of LAB, we’re shifting our focus to contracting, with an emphasis on the types of contract drafting, review, and negotiation performed by
in-house legal teams
. We’re introducing 500 new tasks to LAB focused on contracting — organized by the various types of contracts lawyers have to engage with and the different stages required to negotiate them end-to-end.
Adding contract negotiation as a first-class concept in LAB is critical for building agents that can effectively support large enterprises. Contracting is the most common in-house function, underpinning nearly every business function from research to sales. It is also a uniquely challenging long-horizon agent problem because the agent is required to maintain and learn from context that evolves across a multi-turn negotiation with various stakeholders.
In this post, we outline the agent contracting process, how we’ve encoded it into our existing LAB framework, and the research directions we see as most important for building and evaluating contract negotiation agents.
Benchmarking Contract Negotiation in LAB
Contracts are a primary operating layer for enterprises, governing long-term relationships with customers, vendors, employees, partners, lenders, and other organizations. Despite this, law imposes very few constraints on their form. A valid contract consists simply of (1) an offer; (2) acceptance of that offer; and (3) the consideration, or exchange of value.
This flexibility means that contract complexity scales with what is being contracted for and agreements vary widely in length, negotiation intensity, risk allocation, regulatory constraints, and business importance. Enterprises regularly draft, review, and negotiate dozens of contract archetypes each with their own nuances in what matters and how it can be validly negotiated. This diversity of contracts represents a natural complexity gradient for agents from simple, five-page NDAs to sprawling hundred page credit agreements.
LAB maps these different types of contracts by function. Contracts may be used to advance commercial relationships, raise money, employ people, or conform to regulatory requirements. For each contract, we model their negotiation using similar primitives to how we evaluated an agent's abilities to complete law firm tasks. Adapting these for the contracting workflow, a LAB contract task consists of:
Environment
: The agent is provided with all of the materials of a contract negotiation at a point in time – the contract, playbooks and other guidance materials, and deal context scattered across emails, prior turns of the contract, and internal memos.
Instruction
: The agent receives a short next-state instruction, such as drafting an initial agreement, responding to a counterparty redline, preparing an issues list, or escalating a non-standard term.
Output
: The agent must produce the contract artifact that advances to the next state of negotiation, such as a draft, redline, comment response, open-issues list, or escalation memo.
Verification
: The agent's work is graded against expert rubrics that reflect what the appropriate next stage in negotiation would be, including what edits to make or not make and how to frame up acceptances, concessions, or escalations.
1 of 10
As in LAB, responses are graded under all-pass scoring. Unless an agent successfully makes all of the appropriate edits and identifies all of the red flags, they fail the task. Initial LAB results confirmed our intuition that while criteria scoring provides useful information, all-pass remains the best way to distinguish between effective agents and those not ready for autonomous legal work.
A Single Contract Negotiation Task
Each contract task is built to evaluate an agent’s ability to move contract negotiations forward from a point in time such as forming an initial draft, reviewing the counter-party’s paper, or responding to a redline. To successfully complete the task, the agent must move the contract to the next stage by effectively responding to all of the changes and open issues under the constraints set by the business and deal context.
As an example, one task may ask the agent to respond to a counterparty redline of a Master Services Agreement that has already been heavily negotiated across redlines turns by each party. The counterparty has returned the agreement with additional edits that extend the negotiation by:
Increasing worst-tier SLA credits.
Enabling a single-month termination right for breach of SLA.
Pushing the data-breach indemnification above the general cap.
Adding uncapped indemnities for IP and willful misconduct.
Adding a 50% early-termination fee.
Shifting governing law to Delaware with arbitration in Wilmington.
And more.
In addition to the redlined contract, the agent has access to the prior redlined versions (v1, v2), emails memorializing specific negotiated concessions, a playbook establishing typically allowed negotiating positions and escalation requirements, and various other documents.
To complete the task, the agent must determine which issues genuinely remain in dispute and how those issues should be resolved based on the business and deal context. Doing so requires the agent to realize that it should:
Accept issues where the parties have converged such as general indemnity caps;
Continue to negotiate issues that are within the scope of its authority such as SLA credits;
Reject novel positions that are clearly unacceptable, such as single-month termination; and
Escalate issues the items which remain high-friction across many terms such as governing law.
The agent must not only realize this, but also convert these various decision points into both a v4 redline for the other party and an internal issues list noting what issues have been closed, which remain unresolved, and which require escalation. Doing so allows us to measure both an agent’s ability to negotiate and also its ability to recognize the bounds of its delegated authority. This ensures we know whether an agent can negotiate well and also whether it can bring humans into the loop when demanded by the situation.
What’s Next
While our current benchmark measures the ability of agents to negotiate contracts end-to-end, it does so with each stage as a discrete step. This tells us whether an enterprise team could leverage agents at each step but not the more interesting question of whether agents are prepared to autonomously negotiate contracts while escalating key decisions to humans. To answer this more ambitious question, we are pursuing further research including:
Additional Tasks and Contract Types:
Increase diversity of modeled negotiation states across axes such as leverage, criticality, and more to ensure agents can respond effectively to different business and deal contexts.
Discovered Negotiation States:
Currently, agents are prompted towards the next step of the negotiation. In the future, they will need to discover the state of the negotiation and understand whether the right next step is negotiating, escalating, or even walking away.
Interactive Benchmarks:
Learning to autonomously negotiate requires an effective and dynamic negotiation partner. Building benchmarks that allow agents to learn how to extract and shape deal context and convert it into the correct business outcome are essential to moving agents from supporting negotiations to running them.
These research directions will be informed by initial results on the current contracts task and what those tell us about the state of agents for contract negotiation. In addition, a large amount of in-house work does not involve contracting and we plan to holistically understand in-house teams by expanding LAB to cover non-contract in-house tasks.
LAB has already shown incredible promise in helping better understand and improve agents for legal work. We are excited to extend those insights to contracting tasks which form a core pillar of the work done in-house at companies and where they commonly seek support from outside counsel. As always, we continue to invite feedback on LAB, its constituent tasks, and research directions it could support to help build better legal agents.
Acknowledgements
Spencer Poff has been vital to our research initiatives, including LAB and its contracts extension, advancing our understanding of how agents read, reason about, and act on contracts. We're also grateful to the team who brought Contract Intelligence into the product itself. Sakshi Pratap, Pablo Felgueres, Maharshi Patel, Zach Huang, and Scott Werwath have shaped how reviews are accelerated, how playbooks stay current with every executed agreement, and how insights surface across the portfolio — turning Contract Intelligence into a product that legal teams can rely on every day.
This is one part of a much larger effort spanning Research, Product, Engineering, Design, and our Applied Legal Research team, alongside the design partners who have shaped Contract Intelligence from the start. We're grateful to everyone who continues to make this work possible.
Next Up
Why Legal Professionals are Turning to AI Legal Assistants
How Lawyers Are Using AI to Draft Contracts Faster
AI Maturity in Legal and Why Some Teams Move Faster
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
Shared Spaces
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
Legal Agent Benchmark: In-House Contracting | Harvey
