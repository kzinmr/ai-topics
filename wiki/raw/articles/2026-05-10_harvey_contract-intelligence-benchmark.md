---
title: "Contract Intelligence: A Scaled Benchmark for Measuring Contract Understanding"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/contract-intelligence-benchmark"
scraped: "2026-05-10T01:27:10.144003+00:00"
lastmod: "2025-11-21T16:00:00.000Z"
type: "sitemap"
---

# Contract Intelligence: A Scaled Benchmark for Measuring Contract Understanding

**Source**: [https://www.harvey.ai/blog/contract-intelligence-benchmark](https://www.harvey.ai/blog/contract-intelligence-benchmark)

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
Contract Intelligence: A Scaled Benchmark for Measuring Contract Understanding
Harvey is publishing its evaluation of LLM contract understanding and interpretation, including performance by both Review tables in Vault and human lawyers.
by
Karl de la Roche
•
Nov 21, 2025
At Harvey, our research isn’t just about pushing the capabilities of AI. It’s also about finding ways to distill those capabilities in order to identify ways to deliver measurable results to real attorneys.
One area where we have found LLMs uniquely capable is in contract extraction, converting contract terms into actionable insights at scale. Last year, we
showed
that LLMs were now sufficiently capable to build specialized agents for contract extraction and achieve near perfect performance on high value deal points.
Our work there also showed that out-of-the-box LLMs struggled on this task, only identifying around 65-70% of valid deal points
.
As our customer base expanded, we saw an increasing diversity of contract types. This made base LLM limitations more acute and building bespoke agents for each contract type difficult, slowing time to value for specialized use cases. To solve for this, we doubled down our general intelligence layer, finding broad ways to make Review tables in
Vault
more effective at understanding contracts.
In parallel, we asked ourselves: How good do Review tables need to be to ensure they are delivering value to every user? We settled on an ambitious goal: as good as the attorneys who will use it.
Today, we’re publishing initial findings from our Contract Intelligence benchmark, which encompasses more than 4,000 data points aimed at measuring extraction accuracy on varying contract types and terms and comparing that accuracy to human experts. This publication highlights key outcomes and does not purport to include every result.
“
Out-of-the-box LLMs struggled on [contract extraction], only identifying around 65-70% of valid deal points.
”
Throughout the rest of this post, I discuss how we think about defining and measuring contract intelligence, approaches to measuring model performance, and what our benchmark tells us about the current state of Vault.
Contract Extraction Versus Contract Intelligence
Contract extraction is a common AI use case that predates modern LLMs. The term extraction, however, can create the reductive impression that the goal of a system is simply to pull data points verbatim from a contract. When we discuss contract use cases with clients, they also indicate a clear need to have models reason, understand, or synthesize those data points to create higher-value structured data.
Through our work, we’ve surfaced three main types of questions that our customers are interested in:
Extraction:
Provide a single piece of information found verbatim in the document:
What is the partnership name?
Single-Term Review:
Answer a single key question based on the terms of the contract, but the answer may not appear verbatim in the contract:
Is there an investment objective?
Multi-Term Understanding:
Answer a multi-part question that requires connecting up disparate points of information about the document:
Does this liquidation distribution include any preferred returns, catch up, and/or carried interest?
Each of these types of questions examines a different layer of understanding, from straightforward identification to conceptual reasoning across multiple terms. Collectively, they test not only
what
is written in an agreement, but what that
means
and
how it is
applied
.
Building a Contract Intelligence Benchmark
In order to evaluate model capabilities across these three types of questions, we established a simple, scalable benchmark framework.
First, we consulted both internal lawyers and customers to identify high value contract types and the key data points associated with them. The number of data points varied depending on contract complexity, ranging from 22 (Side Letters) to 37 (LPAs) data points for a contract type. Each data point was structured as a closed-ended question expressed in natural language. Our team also gathered a representative set of contracts of each type, ensuring diversity in contract format and how key terms were expressed.
The contract and questions were given to contracted transactional attorneys and to Review tables to provide responses. The responses were then compared to each other for any disagreements between human and model responses. Disagreements in responses were resolved by Applied Legal Researchers (ALRs) at Harvey with relevant transactional backgrounds. Data points where models and humans agree were also sampled to ensure that agreement didn’t cover up misunderstanding. This initial pass created a final ground truth set of correct answers and provided human and model scores against the ground truth.
This ground truth baseline is then used to automatically evaluate future Vault systems for accuracy. In these future runs, both agreements and disagreements with the ground truth are sampled and reviewed by ALRs to confirm continued validity of the ground truth or identify other areas of disagreement for review and resolution. In this way, thousands of data points are added, reviewed, and evaluated monthly, making it one of the largest (and constantly growing) sets of annotated contract data anywhere.
Lawyers Working With Review Tables Outperform by 5% or More
In digging into the results, we’ve found that the best performance on our Contract Intelligence benchmark came from lawyers working with Review tables in Vault. These individuals routinely
outscored either the lawyer or LLM alone by 5% or more
, depending on baseline contract complexity.
The results also help us better understand human and LLM performance on this specific task, leading to this main takeaway:
When domain-specialized, LLMs can perform competitively with humans at reviewing contracts and producing structured, analytical data
. This observed equivalence in overall scores does not, however, mean that humans and models perform the task the same way.
Models typically fail at tasks differently than humans. By understanding each side’s unique failure modes, we can better identify both how to improve models and how to best leverage them today.
We found that LLM limitations tended to fall into two common patterns. First, they could be overeager, making assumptions about information beyond the four corners of the provided contract. For instance, in Side Letters where information was incorporated by reference from a main agreement, models might make reasonable but unconfirmable claims about the details of that agreement. Humans, by contrast, recognized the limits of what was in front of them and noted the absence of that information.
Second, we saw that LLMs can overthink, producing technically correct but overly literal responses to questions. For example, in provisions requiring consent (such as the assignment of a lease), a model might return that the contract required both consent and notice, reasoning that notice is part of obtaining consent. Lawyers, on the other hand, collapsed this information hierarchy and correctly noted that the contract simply required consent.
On the other hand, we found that humans make errors in harder to predict ways. Although there are some consistent errors of judgment, these tend to be rare amongst high skill experts. More common are errors that come from just being human: accidental transpositions of buyer and seller, missing a key phrase that changes the meaning of a provision, and other one-off mistakes that don’t recur through the lawyer’s work.
Notably, models do not exhibit this sort of failure on our dataset — where a model understands the core concepts reflected in a datapoint it routinely scores full credit across varying contract types. This leads to what we believe is our most interesting conclusion so far:
Model and human intelligence are complementary on issues of contract understanding and analysis
.
Models are fast, comprehensive, and tireless, avoiding the oversights or inconsistencies that can undermine human work. Conversely, where models fail they do so in a way that is easily steerable by human judgment, particularly where models surface their reasoning and citations back to the source material. Combined, humans and models complement each other to deliver faster and more accurate contract analysis. At Harvey, we’ve always known that
AI accelerates a lawyer’s impact
, and this latest empirical data continues to prove that out.
What’s Next in Our Benchmarking
Work on our Contract Intelligence benchmark is ongoing, and we’re committed to continuously deepening it across the three key axes on which we measure intelligence: contract type, number of contracts, and deal points.
We will add new contract types with a particular emphasis on complex contracts like Merger and Credit Agreements. We’ll also add additional contracts to each set — even contracts of the same type can be diverse, and we’ve seen varied model performance depending on how key terms are drafted and expressed.
Finally, we will continue to add key deal points to each contract type as we identify additional data points that present novel challenges for models or that our customers find valuable to benchmark against in order to validate model performance.
Each of these steps helps us refine Vault as a practical tool for scaling contract understanding. As we expand the benchmark, we’re focused on improving how Vault supports lawyers in producing faster, more consistent, and more reliable contract analysis.
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
