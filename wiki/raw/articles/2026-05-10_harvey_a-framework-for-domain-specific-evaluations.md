---
title: "A Framework for Domain-Specific Evaluations"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/a-framework-for-domain-specific-evaluations"
scraped: "2026-05-10T01:27:11.496853+00:00"
lastmod: "2025-10-27T13:00:00.000Z"
type: "sitemap"
---

# A Framework for Domain-Specific Evaluations

**Source**: [https://www.harvey.ai/blog/a-framework-for-domain-specific-evaluations](https://www.harvey.ai/blog/a-framework-for-domain-specific-evaluations)

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
A Framework for Domain-Specific Evaluations
Harvey is expanding our public-facing evaluation work in four key areas: Insights, Research, Approaches, and Context.
by
Julio Pereyra
•
Oct 27, 2025
At Harvey, we spend a lot of time thinking about evaluation of large language models (LLMs) on domain-specific applications. Where important for the public conversation about evaluation, we have
published our research
to further the discussion about how this evaluation could be done, or done better.
Today, we think the most important piece missing from the evaluation discourse is not a research finding or benchmark, but rather
a clear, shared understanding of what evaluation of LLMs does and does not tell us
. Failing to build a communal understanding of evaluation risks evaluation succumbing to Goodhart’s law: "When a measure becomes a target, it ceases to be a good measure." While models will continue to saturate benchmarks, those gains will fail to translate into real value.
At worst, misaligned benchmarks may actively push models towards unhelpful behaviors as showcased by OpenAI’s recent
work
arguing that current evaluative methods increase hallucinations by penalizing abstention under uncertainty. These risks are particularly acute in domain-specific evaluation, where limited access to expensive domain experts makes sparse or misaligned evaluations all the more likely.
Solving for this requires not just better evaluation, but better understanding of evaluation by both model producers and consumers. To start closing this gap, we are expanding our public-facing evaluation work in four key areas: Insights, Research, Approaches, and Context. In the same way the
IRAC
framework helps break down legal reasoning, we use this acronym to capture the four pillars of building evaluations that are both rich and accessible. Throughout the rest of this post, we’ll dig deeper into these four pillars and our forthcoming work across each of them.
Insights
How well is AI performing at a particular task at a particular point in time?
Insights are the core of evaluation. An insight is a single number describing how a model performs on a particular task or set of tasks. For example, our main
Biglaw Bench
(BLB) evaluation describes how well models complete real world legal tasks. It also produces derivative insights on how well those tasks are performed across practice areas and task types.
While these numbers can be reductive, they are essential to building scalable and comprehensible evaluations. Most people do not have the time to routinely engage with the underlying data — that’s our job. Well-aligned insights allow us to aggregate and communicate that data efficiently, creating a useful shorthand for understanding and engaging with evaluations.
Insights will continue to headline most of our work in evaluation. As important as the larger conversation about evaluation is, the most important thing remains that we can identify and describe exactly how our systems are delivering value today and how that value is improving over time. Insights are the broadest way to communicate those critical features and start deeper conversations about what exactly those insights mean and how they can be refined.
Research
How are we evolving our benchmarks to better understand models and agents?
Research represents longer-term work on evaluative methodologies aimed at creating new insights or improving existing insights. Currently, our research focuses extensively on evaluative utility — defining benchmarks that provide direct and meaningful insights about model performance in the real world.
As benchmarks continue to evolve, we think that the essential question becomes building evaluations representing the extremes of model performance. On the one hand, evaluations should establish where models are exceptionally good — these are today’s high value use cases. On the other, evaluations should identify meaningful use cases where models continue to struggle — these establish the continuing frontier for model development.
To support both ends of this spectrum, we will be publishing at least two novel benchmarks. First, our work on
Contract Intelligence
, which focuses on understanding which contracts models can analyze as well as human experts and how models can express this analysis in different forms. Second, we are supplementing our BLB core benchmark with a
BLB Challenge
benchmark focused on queries where we see leading models and agents struggle to solve tasks critical to supporting legal work.
Approaches
How do we operationalize evaluations and use them to drive improvements?
In addition to large benchmarks, we run many other evaluation loops to both tell how good our products are doing, and how to make them better. Approaches describe the end-to-end ways we operationalize and digest these various evaluative signals to determine what’s good, what’s better, and where we can invest to make systems their best.
Approaches also describe the nuts and bolts of evaluation, answering questions like:
How do we incorporate lawyers into both producing and understanding our evaluations?
How do we listen to and incorporate client feedback into evaluations while adhering to strict data privacy?
How do we ensure that systems work well across jurisdictions, languages, and practice areas?
How do we convert expert review into automated evaluation systems using LLMs and other signals?
In short, approaches cover the people and practices that turn our research into insights and insights into improvements.
Context
How do we ground our understanding of what evaluation does and does not tell us?
Context ties evaluation together and makes it accessible through plain-language explanations of the concepts, terms, and methodologies behind evaluative methods. Building and sharing context on AI and evaluation is built into Harvey’s DNA. Since day one, we have hired smart lawyers with no AI experience (and smart AI engineers with no legal experience) and taught them these concepts from scratch. Bringing these conversations to the public can help make evaluations both meaningful and actionable.
Take, for example, recent benchmarks of real-world tasks.
Mercor
claims GPT-5 is the most economically valuable model.
OpenAI
(the makers of GPT-5) disclaim this, ceding that title to Anthropic’s Claude Opus 4.1. Our own
Biglaw Bench gives GPT-5 a modest edge
, though the recently released
Claude Sonnet 4.5
closes the gap. The leaders also come in at 70%, 47%, and 89% on these respective benchmarks. At face value, these insights are somewhere between meaningless and paradoxical. They certainly do not tell a time-pressured associate which model will help them deliver a great outcome and maybe get a few more hours of sleep.
Context on the means, methods, and measures of these benchmarks can help cut through this confusion. It will also, unfortunately, tell you that none of those benchmarks can give direct guidance to that associate — we’d suggest they use Harvey. Knowing what evaluation currently does and does not tell us is the key to productive conversations on the current and future state of AI. Context is what makes those conversations possible.
What's to Come
As models and agents continue to improve, building a broad coalition on evaluation is necessary to ensure these improvements translate into real-world value. Building that coalition requires not only pushing the frontiers of evaluation, but also ensuring that those frontiers are understood and explorable by everyone. We are excited to start building that community, so that together we can keep building the best AI for legal work.
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
