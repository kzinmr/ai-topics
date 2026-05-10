---
title: "Expanding BigLaw Bench"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/expanding-big-law-bench"
scraped: "2026-05-10T01:27:03.812463+00:00"
lastmod: "2026-02-09T15:00:00.000Z"
type: "sitemap"
---

# Expanding BigLaw Bench

**Source**: [https://www.harvey.ai/blog/expanding-big-law-bench](https://www.harvey.ai/blog/expanding-big-law-bench)

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
Expanding BigLaw Bench
Our model performance benchmarks will extend to global jurisdictions, core legal practice areas, and complex legal research tasks.
by
Harvey Team
•
Feb 9, 2026
In 2024, we published
BigLaw Bench
(BLB) with the goal of understanding how well model intelligence could be used to solve real legal tasks. Over time, model performance has steadily improved on BLB with base model scores going from
60%
(GPT 4o | Claude 3.5 | Gemini 1.5) to
90%
(GPT-5 | Claude 4.5 | Gemini 3). This growth has paralleled improvements in the models’ ability to recall, understand, and apply core legal principles to tasks. In short, our original goal for Biglaw Bench — to build a system for better understanding models’ legal problem-solving capabilities — has been proven out.
BLB has also proven to be an invaluable framework for publicly discussing how we are seeing the models improve in ways that matter to our customers. To continue providing (and deepening) this context, we will be updating and substantially expanding the public version of BLB. In the coming months, we’ll be releasing extended benchmarks that increase the number of BLB data points more than fivefold. This data reflects research in three key areas:
global law, practice areas, and legal research
.
Throughout the rest of this post, we reflect on the learnings from the original BLB, and why continuing to benchmark models provides unique insights and opportunities for improvement. We’ll also preview each of the major BLB investment areas for 2026. Starting in the next few weeks, we will publish methodological deep dives into each benchmark, and afterwards, updated BLB scores for all major models.
Looking Back on a Year of BLB
When we published BLB, our hope was to provide a measure that correlated well with our own understanding of the models’ capabilities for solving legal tasks. We explored various methodologies — measuring models' ability to solve
tasks
, to
provide sources
for those solutions, their rate of
hallucinations
, and their ability to
retrieve information
from large corpora.
While we continue to measure all of these things, we have found that the most accurate measure of model capabilities is core BLB:
their ability to solve tasks as graded by objective, expert-written criteria
. More often than not, as models improve on these tasks, they improve our ability to build and deliver valuable AI solutions to lawyers. This correlation has allowed the Harvey team to understand where models may fall short of delivering value to lawyers; work with foundation model labs to improve model capabilities for law; and probe model capabilities to understand how they behave under different constraints.
Understanding General Model Gaps
One way we use BLB is to understand areas where baseline models struggle to exhibit a generally valuable characteristic. BLB serves as a great vehicle for this understanding because each task can provide insights about performance beyond simply task performance.
For example, US federal evidence law makes a distinction between admissible non-testimonial statements that are not hearsay and those that are hearsay but are nonetheless admissible as evidence. One BLB task asks the model to list the statements that fall into each group. In early measures, many models failed this task by conflating which types of statements fell into each group or, worse, sometimes reversing the two groups entirely. Nowadays, most models can iterate through these groups correctly — especially when provided access to web search to confirm their priors.
Importantly, while this failure mode is itself problematic for litigators, it also suggests a larger trend in model error. If models struggle to distinguish these closely related but clearly distinct concepts, it poses research questions like:
What other evidentiary rules may the model not know or fail to apply correctly?
What other trial rules (such as rules of civil procedure) may also be weakly learned?
Could this extend generally to statutory terms or even other legal concepts like distinguishing contract clause types?
“
Reviewing BLB benchmarks made it easier to see where models struggle in ways that matter for practice. Those gaps aren’t just technical issues, they’re signals that help lawyers know when closer scrutiny is needed and where human judgment adds the most value.
”
Laura Toulme
Applied Legal Researcher at Harvey
This single BLB task serves as a canary for collecting additional data on any model’s internalization of legal rules. It also gives us the ability to mitigate this gap for our customers through the use of better aligned models or access to live data. Other BLB tasks similarly serve as bellwethers for the models’ ability to recall certain information or perform certain tasks effectively.
Testing Model Behavior
Beyond understanding, BLB also allowed us to probe model behaviors by pre-aligning on what defines an accurate response. In 2025, there was a concern about model sycophancy: Models would aim to be pleasant rather than correct. To test whether models were detrimentally eager to please, we looked again to BLB. We picked tasks that seemed subjective, but where experts agreed on a correct view such as predicting the likelihood that certain actions would trigger a Most Favored Nations provision in a side letter.
Instead of looking at how the models performed on this task, we looked at whether performance changed when we rephrased the BLB prompt. In the side letter example, we posed the question three different ways: (1) neutrally, (2) as the general partner hoping to find a loophole, and (3) as the MFN holder hoping to obtain the proposed benefit. In the latter two cases, we looked to whether the model swayed from an accurate prediction based on our stated interest in the result. This helped us identify models prone to sycophancy and to build better guardrails against this behavior.
“
What we found most useful wasn’t simply whether the model arrived at the right answer, but how its reasoning shifted under different assumptions. Having lawyers evaluate those shifts helped distinguish confident legal analysis from answers that were merely responsive to framing.
”
Beth de la Roche
Applied Legal Researcher at Harvey
Insights, not Answers
While BLB is an incredibly powerful framework for understanding models, it is not yet a silver bullet. As we set out to expand the benchmark, we wanted to focus where it had been most impactful — providing insights about model behavior rather than answers about specific outcomes. This mindset helped frame our approach to exploring novel ways to understand models with a refreshed BLB.
The Next Year of BLB
In extending BLB, we wanted to focus both on increasing the diversity of BLB as well as identifying new benchmarking methodologies and taxonomies. Below, we briefly describe the theses behind our three new expansion datasets.
BigLaw Bench Extension
Goal
Global
Model performance in different jurisdictions
Practice Areas
Model performance on practice area-specific workflows
Legal Research
Model and agent search capabilities on complex research problems
Global
Harvey now serves customers in more than 60 countries, with more than 400 international
data sources
available and a commitment to further our
internationalization efforts
. Beyond current BLB baselines, we want to dig deeper into each country to ensure model capabilities translate well to other jurisdictions and their unique legal challenges. Built in collaboration with local experts in each country, our Global dataset tests a model’s ability to solve local problems, starting with benchmarks for the UK, Australia, and Spain.
Practice Areas
Where Global is focused on geographical breadth, Practice Areas focuses on depth and end-to-end task completion. For each practice area, Harvey Applied Legal Researchers worked to map out core tasks and build datasets that tested models’ ability to understand, support, and solve those tasks. Our initial practice areas include a diverse and representative cross section, covering: Capital Markets,
Mergers and Acquisitions
, Fund Formation,
Litigation
, Arbitration, and Intellectual Property.
Legal Research
Legal Research focuses on a model’s cross-practice abilities to solve hard research problems when provided with search tools. Our initial legal research dataset (US case law research) also focuses on identifying legal research problems that models are currently not well-suited to solve. Here, the focus is not just tracking model improvements, but providing benchmarks for finding unique strategies to make models more capable researchers.
What’s Next for BLB
First, we will provide deeper dives into each new benchmark and how we built it. In the coming months, we will publish a refreshed BLB, providing model scores across the above extension area with breakdowns for each benchmark and sub-taxonomy. These scores will come with commentary from the Harvey team about what we learned through this revitalized benchmark and how those learnings will guide our research and AI efforts.
BLB has long served as a cornerstone of our understanding of models, and we’re excited to deepen our investment into this effort in the year ahead.
Credits
:
Laura Toulme, Blake Chizen, Emilie McConnachie, Karl de la Roche, Michael Sitcawich, Chris Bello, Lauren Oh, Bronwyn Austin, Niko Grupen, Julio Pereyra
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
