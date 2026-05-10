---
title: "BigLaw Bench Deep Dive: Sources"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/biglaw-bench-sources"
scraped: "2026-05-10T01:27:17.204395+00:00"
lastmod: "2024-09-23T21:41:00.000Z"
type: "sitemap"
---

# BigLaw Bench Deep Dive: Sources

**Source**: [https://www.harvey.ai/blog/biglaw-bench-sources](https://www.harvey.ai/blog/biglaw-bench-sources)

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
BigLaw Bench – Sources
How to evaluate LLM source referencing, and why Harvey is solving this challenging but essential problem.
by
Harvey Team
•
Sep 23, 2024
We
recently announced
the launch of BigLaw Bench—a public-facing version of our internal dataset for evaluating large language models (LLMs) and model systems on complex legal tasks. BigLaw Bench is a framework for quantitatively evaluating the performance of LLMs on real-world legal tasks; supplementing prior work that measures LLM legal reasoning in more structured settings. One of the primary indicators of model performance in BigLaw Bench is its “source score,” a measure we introduced to judge how well a given model’s answer connects factual statements back to source documents relevant to the query.
Harvey has always invested heavily in enabling models to consistently provide accurate sources, and that investment shows on BigLaw Bench with Harvey’s systems substantially outperforming other LLMs on source score. In this post, we explain why we put so much time into optimizing LLM source referencing, and how Harvey is solving this challenging but essential problem.
Why we measure source scores
For real-world, legal work product, an answer is not complete unless it accurately refers to source material through in-line citations, a references section, or a combination of both. Here, we refer to any (or all) of these methods for referencing source material as “sources.” Sources are essential for legal work product, and even more so when that work product is model generated. There are two reasons for this.
The first, and obvious, reason for sources is trust. There is now a common understanding that even the most sophisticated models can hallucinate when engaging with long inputs and generating complex outputs. Providing sources makes model outputs seamlessly verifiable to a source of truth, building user trust and enabling them to more confidently use a model’s analysis.
Less obviously, but as importantly, sources can enable users to more efficiently engage with source-of-truth documents. In legal practice, quickly understanding long, unfamiliar documents—new law or a dataroom of contracts—is a common task. When using models to facilitate this work, linked sources provide a user with an efficient way to navigate documents, jumping from relevant passage to relevant passage without the need to read irrelevant portions. Similarly, even professionals using models to engage with familiar documents may still leverage sources to develop novel analytical frameworks, arguments, or perspectives. If a user is required to read through a source document to validate LLM-facilitated analyses, much of the efficiency benefit of LLMs is lost. In short, sources make AI-generated outputs more trustworthy and effective by consistently tying them back to the source-of-truth documents that are the real driver of most legal and professional work.
Challenges with better sourcing
Internally at Harvey, we define an effective source as one that links to a specific piece of text
within
a source document. This level of exactness is demanded by legal practice but presents a nontrivial technical hurdle. Generating sources that meet this bar requires solving problems with source specificity and uniqueness, as well as the reasoning challenges that come with demanding both from models. The core of good sources is the specificity problem: models must be able to point to the exact passage from a particular document that justifies each assertion in its response. This is a challenging reasoning problem, requiring models to disambiguate text from multiple documents to identify the source document (or combination of source documents) that effectively support model outputs. Sourcing is particularly difficult for argumentation, synthetic propositions, and other analysis that does not exist directly in any one document or statement.
To effectively generate sources, a model must not only return this highly specific text, it must also do so in a way that is unique enough that sources can be consistently distinguished from the model’s primary response. This uniqueness requirement is essential for delivering a seamless source experience because a model’s sources need to be parsed from the answer, linked to the relevant underlying document(s), and provided in a stylized, familiar way back to the user. Doing so requires creating a symbolic language that enables a model to distinguish “this is my answer” from <this is my source.> The stylization required to make this difference often puts models in the unusual position of switching between its preferred modality of predicting standard language tokens to a pattern of predicting the unique and unusual series of tokens needed to demarcate a source. This constant back and forth, taken together with the reasoning challenges of source entailment, make generating consistent and high-quality sources a hard reasoning problem.
What’s more, we ask models to solve this problem
while also generating an equally high-quality answer
. The simple reality is that adding sources without impacting answer quality in any way is an unreasonable expectation—even the most sophisticated LLMs have limited reasoning capacity and asking them to generate sources poses a fundamental trade-off between answer quality and source fidelity. When asked to generate stylized sources, particularly in a format that can be consistently parsed, the addition of sources tends to take away from overall answer quality, detail and fidelity. The below examples show the degradation of answer quality when ChatGPT and Claude were each given queries formulated two ways: the first without requesting stylized sources, the second including a request for stylized sources. In each, the query formulations that include a request for stylized sources results in a shorter, less complete answer containing additional hallucinations. More complex source patterns or instructions are similarly incapable of consistently incorporating precise sources without detracting from answer style, detail, fidelity or all three.
ChatGPT produced a much shorter response when asked to provide references to specific document passages. The response with references is also less accurate, hallucinating the outside date and the company termination fee. ChatGPT also incorrectly places footnote numbers before the period in each sentence and fails to include document quotes as requested.
Claude produced a much shorter, less thoughtful response when asked to provide sources to specific document passages. Claude also fails to include the requested source demarcator.
How we measure source score for BigLaw Bench
Despite the central importance of granular sources to legal work product, the challenges in producing these sources required BigLaw Bench to take an approach to grading sources that granted models points for meeting the lower-bound of source expectations. Specifically, a task’s source score is derived by identifying valid substantive points a model makes that require verification, and whether the model provides a valid source for it. A valid source for these substantive points is defined as any statement or link affirmatively connecting those sentences to a specific
document
proving that point. For example, the below response from ChatGPT would receive a sourcing point for each source link beyond the introductory statement, because each one links to the document that can be used to validate the preceding assertion. This response would lose sourcing points for each sentence that should be supported by a source, but where no source is present. Superfluous sources, such as those contained in the introductory statement, would not receive sourcing points, nor would they result in point deductions.
The reason for this scoring approach was that general-purpose foundation models are not inherently designed to generate both complex legal analysis and the sources that support that analysis. Pushing foundation models into this paradigm through prompting resulted in a sufficiently material trade-off between answer score and source score that Harvey’s research team decided that prompting models for sources would unfairly detract from answer score. Because BigLaw Bench needed an indicator that can be measured across models, we opted for a scoring criteria that accounts for these limitations and provides benchmark data on how often different foundation models provide these moderately useful, document-level sources. On internal evaluations, however, Harvey demands more of its models.
A Harvey output includes links that point users to the specific document passages that support assertions in the answer.
Sourcing as Agentic Communication
Looking forward, our deep interest in sourcing is not
just
driven by their direct contribution to our perennial goal of empowering our users. As we look towards building increasingly complex agents, the importance of sourcing emerges as a modality for intra-model communication. This next generation of agents will need to delegate to and incorporate the work product of potentially hundreds of other models and model systems. Without sourcing, these model exchanges become an increasingly elaborate game of telephone, with each model call risking information being hallucinated, oversimplified, or taken out of context. Sources mitigate these risks by allowing models to collate and provide original, source-of-truth materials alongside analysis. Effectively conveying more concise and relevant material between model calls allows agentic systems to scale beyond what is possible using only model-generated prose. Thus, investing in source consistency and accuracy is essential not only to establishing user trust today, but building more effective, trusted, and scalable systems in the future.
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
