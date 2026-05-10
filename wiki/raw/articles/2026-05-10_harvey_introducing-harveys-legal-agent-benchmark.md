---
title: "Introducing Harvey’s Legal Agent Benchmark"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark"
scraped: "2026-05-10T01:27:17.038682+00:00"
lastmod: "2026-05-06T15:30:00.000Z"
type: "sitemap"
---

# Introducing Harvey’s Legal Agent Benchmark

**Source**: [https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)

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
Insights
Open-Sourcing :Harvey:’s Long Horizon Legal Agent Benchmark
An open-source benchmark built to evaluate and improve agent capabilities for supporting legal work.
by
Niko Grupen
,
Gabe Pereyra
, and
Julio Pereyra
•
May 6, 2026
We’re introducing Harvey’s Legal Agent Benchmark (LAB), an open-source benchmark for legal agents. LAB was built to evaluate and improve agent capabilities for supporting real world work done by lawyers. Each task consists of an instruction, a client matter containing relevant materials, and a requirement that the agent produce a work product for review. This structure is designed to mirror how work is assigned, performed, and reviewed at large law firms.
The goal of LAB is to provide a clear picture of how agents can be deployed to support legal work in the real world. By articulating where agents can do all, some, or none of a task, LAB helps law firms measure the ROI of AI investments and where such investments can augment their teams’ work.
The first version of LAB includes more than 1,200 agent tasks across 24 legal practice areas, and is evaluated by over 75,000 expert-written rubric criteria. We are open-sourcing LAB to give model providers, agent builders, researchers, and law firms a shared way to measure progress on long-horizon legal agents.
We're intentionally launching LAB without a leaderboard because we expect the dataset to evolve over time and we want to work with the community to ensure results are clear and intuitive in how they convey agent performance. In the coming weeks we will work with research partners to get baseline results on LAB and publish a leaderboard to provide perspective on the current state of legal agents. In addition, we will publish standards for normalizing submissions to allow people to identify improvements and track benchmark progress as the benchmark itself evolves with new tasks, practice areas, and knowledge work disciplines.
You can find the open-source version of LAB
here
.
Why we built an agent benchmark
At Harvey, we have spent the past year building agents for the legal domain. This has forced us to think deeply about how to measure their performance on real-world legal tasks.
To date, there has not been a benchmark that illustrates agent progress for long-horizon legal work. Existing evaluations, including
LegalBench
,
CUAD
,
LEXam
, and our own earlier work on
BigLaw Bench
, have graded short-horizon reasoning: read a contract, answer a question, compare cases, or analyze an argument.
In coding, agent benchmarks have served as an important leading indicator of agent capability. For example, agent scores on
SWE-Bench Pro
,
SWE-Bench Verified
, and
Terminal-Bench 2.0
reflected a step-function improvement around the same time our engineering team started to feel the shift in practice; a moment crystallized by Karpathy’s observation that coding agents
“basically didn’t work before December and basically work since”
.
Agent Inflection Point
That pattern is now extending beyond coding. Benchmarks such as
GDPval
,
OSWorld-Verified
,
BrowseComp
,
MCP Atlas
,
FinanceAgent
,
Humanity’s Last Exam
, and
APEX-Agents
have helped make progress legible across real-world knowledge work, computer use, web research, tool use, financial analysis, frontier reasoning, and professional-services tasks.
LAB is intended to provide this same legible index to law firms seeking to deploy and maximize ROI from AI systems. Understanding where agents are capable across practice areas allows firms to identify opportunities to deploy them in order to accelerate client value while moving lawyers to a high-leverage delegate and review pattern. Identifying areas where agents struggle also allows firms to understand where task execution should remain heavily human-in-the-loop. Combined, this context allows law firms to make deployment decisions that are both responsible, secure, and maximally effective for their clients.
Initial results on LAB for leading open and closed-source models will be published in the coming weeks following additional input from research partners and feedback from the community. These conversations will ensure that benchmark scores represent agent performance in a clear, unbiased, and transparent manner. This release will also provide guidance for submitting benchmark runs under normalized conditions to allow third-parties to communicate improvements made on any part of the agent stack and to track how scores change as the benchmark evolves with new tasks and other extensions.
A strong public benchmark doesn’t only measure progress, it helps accelerate it. We are already seeing LAB being used by both our internal teams for product evaluation and the larger research community to explore open-weight post-training, auto-research, memory, domain-specific legal skills, and harness optimizations for long-horizon agent work. We’re excited for the potential of LAB to create a shared foundation for progress on legal agents, and to help bridge the AI research and legal communities.
Legal Agent Benchmark
LAB is a client matter-centric benchmark. It is built to mirror how legal work is actually delivered at a law firm, and we’ve mapped each step of the agent execution and evaluation process to its legal counterpart:
Instructions:
The agent’s instructions are written as a request for work
from a partner to an associate
. Instructions are given as affirmative statements of what is required rather than detailed explanations on expected outputs or style.
Environment:
The agent’s environment is a
client matter.
The client matter defines a closed-universe set of documents and other materials that are needed for the law firm to complete work on behalf of the client. These documents can include matter files, firm templates, email communications, and other information that an agent must discover and sort through in order to accomplish the instructions.
Output:
To complete tasks successfully, the agent must produce
reviewable legal work product
.
Verification:
The agent’s work is graded by
expert rubrics
, which outline what a correct answer must produce in terms of format, facts, and analysis. These criteria emulate the scrutiny work product undergoes when handed off to partners and clients.
Mirroring Legal Work
This client matter-centric structure is the foundation for how we define each task in LAB. Each task is designed not just to test whether an agent can answer a legal question, but whether it can navigate open-ended assignments.
Defining a task
Each task in LAB is built to test agent capabilities to navigate real world work. Instructions are short, averaging just fifty words. Environments mix key and peripheral files and embed issues across multiple documents. An agent must start from a loose instruction, build context across the matter files, and use that context to produce the relevant deliverables.
As an example, one corporate M&A task asks the agent to analyze change-of-control provisions in connection with the proposed (fictional) acquisition of Crestview Software Solutions in a $458 million, 100% equity transaction.
Example M&A task
As input, the agent receives access to a file system containing the background on the deal, a virtual data room and a short instruction from the partner asking the agent to review the data room, identify change-of-control provisions, assess the risk to the deal, recommend next steps, and prepare a review-ready draft memorandum for the deal team and Board. The data room contains a mix of relevant documents – including eight material contracts and other adjacent materials (e.g. 10-K, deferred compensation plan, etc) that may or may not be relevant to the analysis. To complete the task, the agent must determine which files matter, read them in context, and synthesize the relevant provisions across the full matter.
The required output is a reviewable deal-team memo. It must include, amongst other things, an executive summary with a risk mapping, a contract-by-contract analysis of the relevant provisions, severity ratings, and recommendations on how to mitigate each risk identified.
Evaluating a task
When the agent completes the task, the final output(s) are graded against expert rubrics intended to reflect detailed review by a partner or client. Each rubric breaks down what these stakeholders would scrutinize in a submitted deliverable into atomic, binary pass/fail criteria: facts, conclusions, citations, severity ratings, recommendations, deadlines, dollar amounts, and formatting choices. Each criterion is tied to a specific deliverable file. This also makes the rubric consistent across runs. The same criteria can be applied by an LLM judge, used to compare models and harness changes, and fed back into agent training loops as per-criterion reward signals.
Evaluating a task
For the change-of-control task, the rubric contains 57 criteria covering nine legal issues planted across the matter. Each issue is broken into four to nine criteria, covering the underlying facts, severity rating, financial exposure, and recommended action.
The rubric criteria span a range of complexity, from straightforward checks, such as whether the report identifies that the Pinnacle license converts exclusivity to non-exclusivity after a change of control, to checks on more detailed work product, such as whether the report calculates aggregate financial exposure, builds a consolidated consent and waiver timeline, and reconciles inconsistent change-of-control definitions across the agreements.
Importantly, a task is marked complete only if every criterion passes, a concept we refer to as
all-pass grading
. A deal-team report that identifies eight of ten risks is not 80% useful; it is materially incomplete. The missing issue could change deal economics, require the analysis to be redone before closing, or surface as a problem after the deal closes.
“
All-pass grading reflects how high-stakes legal work is reviewed in practice — there is no partial credit for catching most of the issues.
”
Practice area distribution
The change-of-control task is one of 1,250 tasks in LAB, spanning 24 legal practice areas. Large firms have hundreds of distinct practices, so this initial release focuses on a representative set of transactional, advisory, regulatory, and litigation work that associates regularly encounter.
Practice area distribution
To scale the benchmark, we started with real client matters handled by practicing lawyers in each practice area. We then broke those matters into the discrete tasks an associate would typically be delegated to complete. The 24 practice areas in this release are not exhaustive, and many task types within those areas remain uncovered. Future releases will add more tasks within existing areas, expand into additional law firm practices, and move beyond law firms to cover in-house legal work and adjacent knowledge-work domains such as asset management and banking.
Building with the community
LAB is our first fully open-source benchmark. As we continue to expand and develop LAB we are interested in collaborating with:
Lawyers
: To validate and improve the benchmark by reviewing existing tasks, auditing rubrics, and contributing new task families that reflect the work they actually do.
Law Firms:
To help us better capture the workflows, deliverables, and review standards that define the work they do and to ensure that the benchmark helps them understand the state of agents in a meaningful and actionable way.
Legal Technologists:
To build domain-specific skills, tools, and agents for legal workflows.
Agent Researchers:
To improve the planning, retrieval, tool use, memory, and harness design for long-horizon work.
AI Labs:
to work on post-training models that are better at producing reliable legal work product.
“
Our goal is to not only provide a transparent way to measure performance and progress in legal agents, but also to accelerate research progress within the legal and AI communities.
”
We’d also like to acknowledge the following research groups who have already made contributions to the benchmark and the research directions that it enables:
1
of
18
The open-source release is meant to expand this work. We want model providers, startups, researchers, legal AI companies, and law firms to run the benchmark, audit the rubrics, improve the harness, contribute new task families, and help define what legal agent evaluation should measure next.
What’s next
This first version of LAB addresses several important challenges in evaluating legal agents, but it is only the beginning. Over time, we plan to expand LAB in three main areas:
Expanding coverage to all Biglaw practice areas and coverage of tasks within those practice areas.
Expanding coverage beyond law firms to cover other professional service workflows from in-house counsel, to non-lawyers like asset managers, bankers, and tax professionals.
Improving task coverage and sample diversity with an emphasis on building datasets that can be used not only for evaluation but for improving models through fine-tuning and training.
Our overall goal is to help the legal and AI communities understand where agents are useful today, and how to make them better over time. That will require input from more than Harvey. We need researchers, lawyers, and firms using agents in real client work to help test the benchmark, pressure-test the tasks, and tell us where the signal is clearest or missing. For law firms in particular, LAB is meant to help understand which parts of a workflow can be delegated to agents, where lawyer review matters most, and what capabilities still need to improve.
In the coming weeks, we’ll be sharing initial results benchmarking a variety of models and agents on this benchmark. If you have feedback on LAB, want to conduct research using the dataset, or are interested in evaluating specific tasks or outcomes, please reach out to any member of the Harvey research team listed in the blog byline.
Acknowledgements
This work would not have been possible without the tremendous support of our internal teams at Harvey and our external partners. Spencer Poff was the technical lead for the open source portion of the Github repo, spear-headeding much of the early harness design, agent sandboxing, and work to make the benchmark open-source. Julio Pereyra led task design, developing a novel document and scenario generation pipeline that helped us scale task creation. Special thanks also go to Nick Gonella from our Security team; Chris Paradis, Gary Lam, Bronwyn Austin, and Jinfeng Zhuang from our AI Platform team; Phil Cerles and Philip Lan from our Assistant team; Laura Toulme, Blake Chizen, and Nick Gillies from Applied Legal Research; Shawn Farsai from Brand; and Nico Belmonte, Tara Waters, Ryan Samii, Joe Marando, Farrah Pepper, and Joe Cohen for ongoing feedback on the benchmark. We’d also like to thank Dan Biderman, Neel Guha, Velen Wu, Reinhard Heckel for providing feedback on this post.
Next Up
Harvey Power Users: The Skill You're Sharpening
Inside PwC’s Shift Toward AI-Enabled Deal Execution
Where Legal AI is Becoming Real Work
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
