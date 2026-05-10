---
title: "Introducing BigLaw Bench to Evaluate LLMs"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/introducing-biglaw-bench"
scraped: "2026-05-10T01:27:16.401126+00:00"
lastmod: "2024-08-29T18:48:00.000Z"
type: "sitemap"
---

# Introducing BigLaw Bench to Evaluate LLMs

**Source**: [https://www.harvey.ai/blog/introducing-biglaw-bench](https://www.harvey.ai/blog/introducing-biglaw-bench)

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
Introducing BigLaw Bench
Presenting BigLaw Bench—a version of our internal dataset for evaluating large language models (LLMs) and model systems on complex legal tasks.
by
Harvey Team
•
Aug 29, 2024
Overview
Today we are announcing the first public results of BigLaw Bench—a public-facing version of our internal dataset for evaluating large language models (LLMs) and model systems on complex legal tasks. BigLaw Bench is a framework for quantitatively evaluating the performance of LLMs on real-world legal tasks; supplementing prior work that measures LLM legal reasoning in more structured settings. Harvey’s proprietary models significantly outperform publicly available LLMs, but all models show substantial room for improvement when benchmarked against full completion of tasks performed by lawyers. The results are promising. They show that legal AI systems have the potential to significantly improve the efficiency of lawyers by completing real world tasks.
BigLaw Bench Tasks
“
Existing multiple-choice or one-size-fits-all benchmarks are insufficient to capture the real billable work that lawyers do.
”
At Harvey, our goal is always to build and evaluate LLMs for actual, billable work performed by lawyers and professionals reflective of our client base. Our benchmarks are conceptualized and designed by our legal research team, composed of attorneys with experience across a wide range of practice areas and BigLaw firms, and constructed using publicly available documents to enable transparent evaluation under realistic conditions.
In defining benchmark tasks, we draw on a familiar feature of the legal profession: the time entry. Time entries cover all of the tasks that lawyers do in service of their clients and provide a concise way to convey the task performed and the value of that work. Because all work is billed, building a comprehensive set of time entries closely reflects the set of legal tasks that make up real-world practice.
The challenge with evaluating models on these tasks is that most of the work that lawyers do—assessing risk, drafting documents, thinking of arguments, and advising clients on novel legal developments—is too complicated to be graded by multiple-choice or other one-size-fits-all criteria which are the hallmarks of existing benchmarks. Effectively capturing how much models can facilitate this kind of work required developing far more sophisticated and task-specific grading criteria than those used in prior benchmarks.
By converting time entries into model-based tasks (prompt / document pairs), we are able to identify and evaluate how models can contribute to real, high-value legal work. These tasks are then sub-divided by other relevant taxonomies, such as the practice area—litigation or transactional—and the portion of a matter the task would facilitate. The following tables outline the major categories and distribution of BigLaw Bench core tasks, i.e. tasks that we use to test fundamental model capabilities to solve problems involving reasoning about, analyzing, and discussing legal concepts and text without the need for multi-part or agentic workflows.
Transactional Task
Fraction of Core Tasks
Corporate Strategy & Advising
28.3%
Drafting
24.5%
Legal Research
13.2%
Due Diligence
11.3%
Risk Assessment & Compliance
9.4%
Negotiation Strategy
5.7%
Deal Management
3.8%
Transaction Structuring
3.8%
Litigation Task
Fraction of Core Tasks
Analysis of Litigation Filings
25.5%
Case Management
23.4%
Drafting
14.9%
Case Law Research
8.5%
Transcript Analysis
8.5%
Document Review & Analysis
6.4%
Regulatory & Advising
6.4%
Trial Preparations & Oral Argument
6.4%
Evaluation Methodology
Harvey’s research team developed bespoke rubrics to evaluate each task. These rubrics establish objective criteria that would be necessary for a model response to effectively accomplish a given task. They also penalize common LLM failure modes such as incorrect tone or length, irrelevant material, toxicity, and hallucinations. Combined, these rubrics effectively capture everything a model
must
do to effectively complete a task, and everything it
must
avoid to ensure it completes that task in a safe, effective, and trustworthy manner.
In order to convert these criteria into a benchmark, each affirmative requirement was assigned a positive score based on its importance to completing the relevant task. Negative criteria, such as hallucinations, were assigned negative scores as the human effort to correct errors can reduce the utility of an otherwise complete piece of AI work product. Answer score is computed by taking the combination of these positive and negative points and dividing by the total number of positive points available for a task.
“
Answer score represents: What % of a lawyer- quality work product does the model complete for the user?
”
In addition to grading the substantive content produced by the model, we also benchmark the verifiability of a model’s answer through a source score. A task’s source score is derived by identifying the substantive points a model was required by a rubric to make and for which a reference to a source document would be needed in order to verify that point. For example: if a substantive point in the rubric was, “The model’s answer must include the termination fee is $10,000,000,” the sourcing point would be “the model must provide a source for its statement that the termination fee is $10,000,000.” A source was defined as any statement or link affirmatively connecting a sentence needing a source to a specific document or part of a document that proves that point.
“
Source score represents: What % of correct statements does the model support with an accurate source?
”
Though related, source score and answer score are independent. A model can make a number of correct assertions (high answer score) while failing to provide traceability of those assertions to relevant source documents to facilitate user trust and validation (low source score).
A sample of instantiated tasks and their associated rubrics are included in the Appendix.
Results
“
Harvey's proprietary models outperform leading foundation models on domain-specific tasks, producing 74% of a final, expert lawyer-quality work product - the outputs are more detailed, capture more nuance, and are much closer to final lawyer quality.
”
The below graphs summarize model performance on BigLaw Bench core tasks. On answer scores, Harvey’s proprietary assistant models outperform each of the leading foundation models, producing outputs that are more detailed and materially closer to a final legal work product. In general, we found that public foundation models provided, on average, reasonably strong answers—solving the blank page problem and getting users more than halfway to a final work product—but often lacked specificity or missed key legal nuances. The advantage of Harvey models remains when tasks are split into litigation and transactional. Overall stronger model performance on transactional tasks is driven by those tasks being, on average, more analytical with litigation tasks tending to require the models to engage more with ideation and argumentation—areas where foundation models tended to underperform.
On source scores, performance differences are far more pronounced. Besides Harvey, only ChatGPT provided sources to documents for a meaningful number of tasks when sources were not explicitly requested in the prompt. To ameliorate this, the Harvey team attempted to derive custom prompts and instructions for all models that would require sources to be included after affirmative statements about the document. These prompts had a substantial negative impact on model performance, as the foundation models would consistently hallucinate sources (either document text, page number, or both) leading to weak source scores and far worse answer scores. In short, the foundation models provide good answers but have trouble showing their work, even when explicitly asked.
Next Steps
BigLaw Bench provides a framework for effectively benchmarking model performance on legal tasks regardless of complexity. However, it currently emphasizes tasks that today’s models can or should be able to do. This list of tasks falls far short of the goal of providing a benchmark of all tasks that lawyers must perform to deliver value for their clients. Many of these tasks remain far beyond the reach of LLMs and even the most sophisticated LLM agents. Mapping and benchmarking this full range of tasks will be necessary for the effective development of domain-specialized AI. As we continue to build this more ambitious benchmark, we intend to deepen and formalize our collaboration with both client and industry partners like
vals.ai
. These collaborations are essential to developing an industry standard benchmark for measuring and improving the ability of AI systems to perform the most complex knowledge work.
Appendix
Here we provide an example task from both the litigation and transactional categories for reference. A more comprehensive description of exemplar tasks sampled from BigLaw Bench, including associated rubrics,
can be found here
.
Category
Task Type
Task
Prompt
Documents
Litigation
Document Review & Analysis
Analyze trial documents and draft an analysis of conflicts, gaps, contradictions, or ambiguities, including a detailed chronology of events and analysis results.
First, generate a detailed chronological summary of events from these trial documents and then second, identify any conflicts, gaps, contradictions or ambiguities.
5 Trial Exhibits
Transactional
Drafting
Draft board consent approving a potential conflict of interest in the engagement of a lawyer who is affiliated with an officer of the company.
Draft board resolutions approving engaging a lawyer who is related to an officer and approval is required to address the conflict of interest.
N/A
Credits: Julio Pereyra, Elizabeth Lebens, Matthew Guillod, Laura Toulme, Cameron MacGregor, David Murdter, Karl de la Roche, Emilie McConnachie, Jeremy Pushkin, Rina Kim, Aaron Chan, Jenny Pan, Boling Yang, Nan Wu, Niko Grupen, Lauren Oh, Aatish Nayak, Gabriel Pereyra
Next Up
Harvey Power Users: The Skill You're Sharpening
How we Built Image Understanding for Legal Documents
Open-Sourcing Harvey’s Long Horizon Legal Agent Benchmark
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
