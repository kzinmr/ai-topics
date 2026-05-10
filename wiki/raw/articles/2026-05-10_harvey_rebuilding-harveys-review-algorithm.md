---
title: "Rebuilding Harvey's Review Algorithm"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/rebuilding-harveys-review-algorithm"
scraped: "2026-05-10T01:27:10.691256+00:00"
lastmod: "2026-04-21T16:00:00.000Z"
type: "sitemap"
---

# Rebuilding Harvey's Review Algorithm

**Source**: [https://www.harvey.ai/blog/rebuilding-harveys-review-algorithm](https://www.harvey.ai/blog/rebuilding-harveys-review-algorithm)

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
Rebuilding the Review Algorithm to Increase Accuracy and Speed
Review tables now deliver more accurate answers, more granular citations, and faster results.
by
Grace Hong
,
Cameron MacGregor
, and
Vasudha Rengarajan
•
Apr 21, 2026
Review tables in Harvey enable legal teams to extract information from large sets of documents at once — turning thousands of contracts, filings, or agreements into a structured grid you can scan, filter, and act on. For tasks like
due diligence
, contract analysis, or regulatory review, it compresses work that would otherwise take days into something you can move through in minutes.
Earlier this year, we revamped the algorithm underlying review tables so that they deliver more accurate answers, more granular citations, and faster results. While our previous review algorithm showcased the power of extraction en masse, the new algorithm extends the value of review tables with a focus on
empowering users to efficiently
review at scale
.
In this post, we'll walk through the problems we set out to solve, what we changed, and how we evaluated the impact of those changes.
Key Challenges to Solve
In rebuilding the review tables algorithm, our Engineering, Applied Legal Research, and Product teams focused on three areas:
Reconciling the two existing fields (summary and additional context)
Rethinking our citation methodology
Illuminating model reasoning
Together, these challenges created a friction that undercut one of the core value propositions of review tables: saving lawyers time.
For example, the previous algorithm produced two fields per result: summary and additional context. In some cases, the additional context was the detailed response users wanted, but it wasn't visible at the cell level. In other cases, when customers wanted a straightforward answer, the additional context was duplicative in substance with the summary.
Separately, in the past algorithm, citations were attached to the cell as a whole. For longer outputs, we realized there was an opportunity to more specifically cite how each source backed each statement to expedite review.
Additionally, Harvey didn’t reveal its line of thinking. Filling this gap and shedding light on Harvey’s thought process presented us with a golden opportunity to optimize verifiability — a critical step for lawyers whose reputations and licenses rest on their diligence.
Providing Answer and Reasoning
The new algorithm produces two parts for each result:
answer
and
reasoning
. The answer consolidates the previous summary and additional context into a single field, giving the user both the quick-glance benefits of a short answer and the contextual advantages of a detailed answer. Reasoning is the full analytical picture: what the document says, how Harvey interpreted it, and why it reached its conclusion.
This is most valuable where answers are inherently less clear cut — questions that require interpretation rather than straightforward extraction, where users need to see the thinking behind the answer to decide whether they agree with the conclusion. It's also particularly useful when Harvey doesn’t find responsive information, since it explains why, rather than simply returning an indicator (i.e., “—”) that Harvey didn’t find responsive information. When an answer requires validation, the step-by-step logic behind the conclusion makes it possible to assess whether the model's interpretation is sound. Reasoning also gives users a way to improve their prompts: seeing how the model approached the question makes it easier to identify where to redirect it.
Take a question like, "What were the conclusions of the expert report?" The
answer
gives you the concise, well-formatted takeaway. The
reasoning
then walks through the specific arguments with each point footnoted to the exact line in the report from which it draws. As another example, let’s say Harvey returns “—” as an answer in response to whether a supply agreement contains a change of control provision, since it was unable to find the provision. With reasoning, Harvey will now explain how it reached that conclusion by outlining where in the agreement Harvey searched.
Improved Latency With Sentence-Level Citations
Previously, review tables generated sources through an algorithm that combined model-generated text and fuzzy matching. One of the key innovations for the new citation algorithm, which centers on pointing to indices throughout the document, involved moving from cell-level citations to sentence-based citations, making it patently clear which assertion in the response the citation supported. The additional granularity allows users to more efficiently verify the model's reasoning and answer.
This also resulted in a boost in output speed. By reassessing our execution pipeline, we were able to adopt an implementation that kept per-cell latency low and the overall architecture simple while achieving sentence-level granularity. At scale — a 30-column, 1000-document table produces 30,000 concurrent cells — the latency of this approach is substantial.
Evaluating the New Algorithm
Shipping the new algorithm required answering three questions: Do users prefer it over the previous approach, does citation quality actually improve, and does reliability hold up? We needed a structured way to evaluate all three before rollout.
Harvey's privacy guarantees mean
no one on our team sees real customer queries
. To build evaluation datasets, we work closely with Applied Legal Researchers (ALRs), former practicing lawyers embedded in our product and engineering process. ALRs develop queries that reflect real usage patterns, spanning the range of question types and document complexity that appears in production. For this update to review tables, they generated datasets specifically designed to evaluate differences in answer quality and citation precision between the old and new algorithm outputs, spanning use cases across practice areas.
We measured
quality
through side-by-side preference testing: contract attorneys compared old and new algorithm outputs on the same queries and rated overall answer preference along with citation accuracy.
Latency
was measured separately through benchmarks that accounted for prompt caching and parallel request handling across different models. Quality and speed are both critical, so we knew optimizing for one at the expense of the other wasn’t a worthwhile trade off at table scale.
Reliability
measures the rate at which Harvey fails to provide the user with an answer for parsing reasons or because of unexpected model outputs.
Preference was weighted alongside latency, citation reliability, and cell success rate rather than each being used as a standalone signal. In our evaluation, we saw each metric improve.
Overall,
the new algorithm was preferred four times more than the original algorithm in side-by-side evaluations
, consistent across both transactional and litigation practice areas. Preference was strongest on complex document types; for both credit agreements and trial exhibits, the new algorithm was preferred seven times more than the old algorithm. The top qualitative driver was analytical depth: reviewers consistently preferred responses that showed their reasoning rather than returning a conclusion alone. The results of the evaluation gave us confidence in delivering the new algorithm.
What's Next for Review Tables
The new algorithm helps set the foundation for the next generation of review tables. In its future state, rows and columns will dynamically derive from any knowledge source — splitting entire datasets or web pages into structured rows, while columns draw on context across hundreds of pages and multiple files.
This will unlock a more powerful review experience, with multi-source citations users can easily audit and validate, and confidence-based scoring users use to prioritize their review. With this evolution, agentic review will bring deeper, structured analysis into a single interface, helping our customers move faster while maintaining rigor and confidence.
Next Up
How we Built Image Understanding for Legal Documents
How Harvey Secures Embeddings at Scale
Building Spectre
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
