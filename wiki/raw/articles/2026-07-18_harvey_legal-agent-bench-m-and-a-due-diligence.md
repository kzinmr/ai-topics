---
title: "Extending Legal Agent Bench to M&A Due Diligence"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/legal-agent-bench-m-and-a-due-diligence"
scraped: "2026-07-18T06:00:53.176576+00:00"
lastmod: "2026-07-17T16:00:00.000Z"
type: "sitemap"
---

# Extending Legal Agent Bench to M&A Due Diligence

**Source**: [https://www.harvey.ai/blog/legal-agent-bench-m-and-a-due-diligence](https://www.harvey.ai/blog/legal-agent-bench-m-and-a-due-diligence)

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
Insights
Extending Legal Agent Bench to M&A Due Diligence
Introducing a new extension to Legal Agent Bench that evaluates AI agents on one of legal's most complex workflows: M&A due diligence.
by
Julio Pereyra
•
Jul 17, 2026
Our goal with
Legal Agent Bench
(LAB) is to create and distribute realistic, high-scale agent environments to evaluate agents’ ability to perform end-to-end legal work and support open model training and agent research. Today, we’re extending LAB to cover one of the most critical legal tasks: M&A due diligence.
Diligence underlies every merger and acquisition which collectively amounted to around
$4.8 trillion dollars
of economic activity in 2025. Diligence costs typically range from
1-4% of deal value
, landing them between $50 and $200 billion per year. Much of that cost is spent reviewing a virtual data room (VDR), systematically working through a company's legal and financial history to identify risks, mitigate them, and confirm the deal lives up to expectations.
LAB Diligence compared to leading benchmarks across disciplines on environment size and independent validation criteria per task.
To develop LAB environments for diligence, we wanted to focus on emulating the depth and complexity of a real VDR. This requires building novel evaluative environments that scale both size and depth of evaluation. Historic benchmarks have either focused deeply on reasoning over relatively contained context or narrow task execution over larger datasets. Diligence requires a model to do both, reading hundreds of documents to identify many independent transaction risks.
To evaluate models on this problem, we created multiple synthetic VDRs spanning thousands of documents and embedded with issues spanning diligence specialties from tax to tech transactions. In an exemplary environment, agents are given a VDR with tens of millions of tokens of context requiring them to find and remediate dozens of issues with their work validated by hundreds of rubric criteria.
Throughout the rest of this post, we explain what diligence looks like, how LAB diligence emulates a key piece of it, and how we are building specialized agents to help conduct diligence.
What Diligence Looks Like
Let’s say you want to buy a company. You meet with their principals and reach a rough agreement on a few key terms like price, form of payment, and confidentiality of the negotiations. This agreement is memorialized in a
term sheet
spanning a few pages. By the time the deal actually happens, that term sheet is replaced by an
acquisition agreement
sprawling hundreds of pages and detailing the mechanics of the acquisition, the obligations of the parties, and what happens if things go wrong. The work that shaped these additional pages is diligence.
Diligence and its relationship to an acquisition agreement.
At its core, legal diligence has two parts. The first is understanding and ascribing an accurate value to the underlying business. The second is allocating the risk of acquiring, combining, and integrating the business successfully. Both of these tasks require developing an understanding of the business from its primitives: the commercial contracts, employment agreements, IP portfolio, tax and regulatory documents, and other legal agreements that establish its rights and liabilities.
This is where the VDR comes in. After agreeing to the deal in principle, key documents (often numbering in the hundreds or thousands) are organized by the parties and added to a VDR. Once opened, teams of lawyers representing various specialties will work systematically through the VDR identifying risks, gaps, and follow-up questions. This initial pass will generate follow-up requests, interviews with key people at the target, and additional negotiations about the deal and subsequent disclosures. These reviews happen at all possible speed, with lawyers routinely working hundred-hour weeks to wrap their heads around every aspect of the business under tight timelines.
The resulting analysis is compiled into a diligence memorandum. This memo influences the final negotiations and planning on:
Deal Price:
How the company is actually valued, as many legal issues identified in diligence can impact that valuation
Deal Structure:
The nature of what is purchased (equity or assets) and the form of the purchase
Representations, Warranties, and Indemnities:
What a seller is made to guarantee is true and correct about the business and what risks they are required to pay for if they materialize
Disclosure Schedules:
What known issues a seller is explicitly off the hook for
Conditions and Consents:
The third party consents or regulatory approvals that are required to close the deal
Post-Closing:
How the two companies actually integrate into a productive new entity and other actions that are required post-closing
Effective diligence is not just knowing the company factually. It’s layering judgment on top of that factual record to understand what actually creates value for the business, what risks exist to that value, and how to negotiate those risks into a final agreement satisfactory to all parties.
Building a VDR
LAB’s diligence environments test agents’ ability to identify and action issues at the scale of realistic VDRs. As an example, take the VDR of Sentinel Cloud Security, which is being diligenced for a potential acquisition by Helios Cloud Holdings in a deal loosely modeled on Google’s $32 billion acquisition of Wiz in terms of industry, deal size, and acquisition type.
The file system of the VDR for the synthetic Helios–Sentinel Cloud Security acquisition.
Sentinel’s VDR is a filesystem categorized by the key types of documents required to validate its business. Across these categories are more than 3,500 documents ranging from commercial contracts to litigation materials. Collectively, these documents total around 45 million tokens of context. Diligence requires both aggregating these millions of tokens into a coherent story about Sentinel and then identifying issues within that context.
These issues may be direct, a key customer may have the right to terminate a contract upon a change of control and no consent to the proposed acquisition has been obtained. It may be a missing file, there is no proof that the company owns or leases certain key offices. Or it may require reasoning across a number of clues: the company has a risky view of copyleft licenses that risks exposing some of its key IP. That view can only be sussed out by reviewing a mix of product counsel memos, technical specifications, and taking an opinionated view of how they fit together under current copyright laws.
The amount of context and the shape required to understand it makes diligence a uniquely hard problem for current-state agents. They cannot keep tens of millions of tokens in context, and task-oriented compaction strategies prevent them from forming a clear global picture of the VDR. Lossiness in compaction also means that subtle, multi-document issues are not picked up on as their threads are not maintained clearly enough for models to connect the dots. In practice, these fundamental issues are exacerbated by frontier model biases towards efficiency using keyword search and selective reading strategy rather than exhaustively reviewing documents at scale.
Other VDRs, the real deals they’re modeled on (industry, size, and acquisition type), and environment size in LAB diligence.
Diligence Agents
In practice, diligence is solved by exactly this kind of brute force: dozens of lawyers across various practice areas who collectively review the VDR for thousands of hours. Different specialists consider the target’s IP portfolio, their employment agreements, equity and compensation plans, commercial contracts, and financial and tax records. Findings across each are then consolidated into a diligence memo which is used to shape the deal terms and closing strategy.
To successfully diligence a LAB VDR, one or more agents takes on all of these roles, identifying issues holistically and drafting a first pass diligence memo. This memo is then checked against a rubric containing ground truth findings and recommendations for each issue planted in the VDR.
The evaluation environment, agent behavior, output, and grading criteria for a LAB Diligence task.
These rubrics allow us to explore strategies at both the harness and post-training level for effectively shaping agents that can engage in diligence. Doing so requires solving novel technical problems including:
Context Management:
Agents must read and make connections across information stretching many times their context window. Novel approaches to
memory and compaction
are required to allow them to effectively parse and retain key information while identifying and tracing risks.
Exhaustive Review:
Most agents are trained to identify the relevant portion of a large data space such as the relevant function in a code base. Their bias is to search efficiently, not completely. Diligence requires reversing this intuition and teaching them to check, and double check, every possible issue.
Contextualized Judgment:
A change-of-control in a million dollar contract may tank one deal, it may be an inconvenience to another. Agents must learn what issues matter, how much they matter, why they matter, and how best to remediate them.
Agents that can do all of these are helpful for diligence. But, diligence is a team sport. To actually do diligence an agent must also be able to (1) source its findings to specific documents and be capable of explaining or defending them; (2) communicate recommendations clearly, including alternative approaches where multiple valid strategies exist; and (3) present it all at the right level of detail for different stakeholders.
We believe that agents will learn to be maximally effective participants in a diligence team the same way junior associates do: via incisive feedback from experienced practitioners. This is why our diligence environments are built not just for research, but as a data-safe way to collaborate with customers to train models using their feedback. Our customers are the ones trusted with billion dollar deals today; their agents will be the ones trusted with those same deals tomorrow.
What’s Next
In the coming weeks we will publish our research identifying strategies for effective diligence agents and initial results across a diverse set of VDRs. We will also release additional LAB extensions covering tasks ranging from enterprise search, to fund formation, to investigations and discovery.
In parallel, we will work on moving these worlds from research to production, showing how agents can be improved through natural language feedback and collaborating with our customers to refine custom models that solve hard problems the way that they do.
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
