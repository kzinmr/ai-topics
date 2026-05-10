---
title: "Introducing BigLaw Bench: Research"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/introducing-big-law-bench-research"
scraped: "2026-05-10T01:27:09.222957+00:00"
lastmod: "2026-03-11T15:00:00.000Z"
type: "sitemap"
---

# Introducing BigLaw Bench: Research

**Source**: [https://www.harvey.ai/blog/introducing-big-law-bench-research](https://www.harvey.ai/blog/introducing-big-law-bench-research)

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
Introducing BigLaw Bench: Research
BLB: Research helps us identify how foundation models are improving on research tasks, enabling investigation of ways to improve AI-based legal research.
by
Laura Toulme
•
Mar 11, 2026
The second of our major BigLaw Bench (BLB)
expansions
this quarter is BLB: Research. This dataset focused on hard agentic legal research problems. Working with our data partner Snorkel AI, a leader in creating complex expert data for frontier AI, we identified a series of US Case Law research problems that leading models are currently unable to solve — even when provided with search tools like web search.
The purpose of BLB: Research is twofold. First, to
identify how foundation models are improving on research tasks
and the failure modes that continue to cause them to return unsatisfactory answers. Second, to
investigate ways to improve AI-based legal research
through agentic systems and access to non-public data in addition to foundation model capabilities.
By enabling us to both identify the best model and to build better infrastructure for those models, BLB: Research helps us build deeper and more accurate research capabilities for our customers.
Benchmarking Beyond Models
BLB: Research is our first benchmark that requires models to operate end-to-end over more than documents. Models must use tools to perform searches in order to identify relevant research context and provide a grounded, cited response. While historically we had measured search capabilities
independently
, evolutions in agent building and model deployment led us to combine search and response into a unified benchmark.
The main driver of this change is the growing consensus on search as the primary means for providing grounded model responses across the industry. On the research side, as models are increasingly trained to use search rather than training data for up-to-date knowledge, benchmarking their capabilities without search unrealistically undersells what they can do.
“
Building a holistic search benchmark allows us to measure performance in the way that tracks how research capabilities are being developed and how our customers expect them to be delivered.
”
Search is also becoming table stakes in practice, with customers relying on knowledge sources and expecting pin-cited sources as the default for research-driven use cases. Building a holistic search benchmark allows us to measure performance in the way that tracks how research capabilities are being developed and how our customers expect them to be delivered.
Building Realistic Complexity
Given its ubiquity as a paradigm, models are, perhaps unsurprisingly, very good at search. They can write booleans and web searches and have learned to use search to explore, understand, and refine their research. A primary objective for BLB: Research was to validate these baseline capabilities, as well as identify areas in which the models were still not capable of turning their search capabilities into meaningful research outcomes for lawyers. In short, we wanted to create a hard benchmark.
A good way to make benchmarks hard is to make them esoteric. This is unfortunately also a great way to make a benchmark useless. While we could show the models fail at a number of tasks, if succeeding at those tasks wouldn't actually help a legal professional, that failure is beside the point. Accordingly, we needed to ensure that tasks were difficult and realistic. Realistic tasks are both intrinsically useful and represent a research pattern that is generally useful, such as identifying the best case to cite for a proposition, drafting a research memo, or planning a claim or defense.
From these realistic task types we then had to find those that were hard. We did this not by predicting what
should
be hard but by actually finding the frontier of model capabilities.
First, we identified what failure looked like on a structured rubric: How poorly must a model perform before its answer is unhelpful to a legal professional? We found that many partly correct answers are still helpful. For example, slightly-off analysis with good citations to principal cases still gives users a research head start.
In general, we found that model answers become unhelpful once the model completes less than 60% of the required task criteria. On these tasks, models are often missing critical reasoning junctures, making wrong turns in their research, or providing answers that are too surface level to be useful.
Here are some research tasks that Harvey will use to benchmark models’ research capabilities:
Practice Area
Task Objective
Task Description
Corporate
Assessing Earn-Out Manipulation Claims After Asset Sale
A strategic buyer acquires a Delaware company's assets with a multi-year earn-out, then consolidates the business, reallocates overhead, shifts pricing strategy, and reassigns key salespeople. Assess whether the buyer's integration decisions breach the Asset Purchase Agreement.
Securities Litigation
Evaluating Securities Fraud Claims Against EV Company for Prototype Misrepresentations
A publicly traded hydrogen fuel-cell truck company's CEO made statements about fully functional prototypes and secured partnerships that internal documents contradict. Evaluate material misrepresentation, scienter pleading, and PSLRA safe harbor defenses after a 45% stock price decline.
Privacy and Cybersecurity
Analyzing Defenses to Nationwide Class Action Arising from FinTech Data Breach
A financial-technology company with 650,000 affected users faces a putative nationwide class action after a breach caused by a compromised contractor API credential. Evaluate Article III standing for speculative-harm plaintiffs, choice-of-law barriers to nationwide class certification, and Rule 12(b)(6) strategies.
Other practice areas included in the benchmark are: Intellectual Property, Commercial Litigation, Constitutional Law, Regulatory, Employment & Labor, Health Law & Life Sciences, Tax, Tort, Real Property, Media and Technology, Immigration, and Family Law.
What’s Next for BLB: Research
Sifting through troves of documents to find answers, narratives, and trends is one of the most common tasks in legal practice. The same search capabilities that make models good at case law research also underpin the ability to search EDGAR, an investigation corpus, a deal room, or even a law firm’s own internal knowledge. BLB: Research will build towards measuring all these capabilities and finding the right tools for enabling models to move lawyers from sifting to solving.
The next step-change in search capabilities can come from various sources: model capabilities, unique data sources, or the tools to enable the former to interact with the latter. BLB: Research will allow us to track and design innovations in all of these spaces, and convert them into the best possible research results for our customers.
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
