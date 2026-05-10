---
title: "BigLaw Bench Workflows: SPA Deal Points"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/biglaw-bench-workflows-spa-deal-points"
scraped: "2026-05-10T01:27:10.643303+00:00"
lastmod: "2024-09-26T23:37:00.000Z"
type: "sitemap"
---

# BigLaw Bench Workflows: SPA Deal Points

**Source**: [https://www.harvey.ai/blog/biglaw-bench-workflows-spa-deal-points](https://www.harvey.ai/blog/biglaw-bench-workflows-spa-deal-points)

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
BigLaw Bench Workflows: SPA Deal Points
Expanding BigLaw Bench to evaluate legal workflow agents, starting with extracting deal points from Share Purchase Agreements (SPAs).
by
Harvey Team
•
Sep 26, 2024
We are expanding our publicly-released BigLaw Bench data to include data we use to benchmark, evaluate, and improve legal workflow agents. These workflow datasets represent a large number of samples of a complex, recurring task and are used to evaluate and improve agent systems on these hard reasoning problems. The first dataset we are releasing is extracting deal points from Share Purchase Agreements (SPAs). Although these documents fit within the context window of foundation models, they struggle to reason effectively over these complicated agreements, correctly identifying only between 66.04% (GPT-4o) and 72.27% (Gemini) when given a basic set of deal points. In contrast, Harvey’s SPA agents are able to extract 98.47% of deal points correctly across diverse SPA documents. Here, we discuss our results and provide a subset of both the SPA data and the deal points schema.
Dataset
We collected a large number of SPAs from the SEC’s website and other sources. Our legal research team reviewed these SPAs and identified a subset of documents that were representative of the diversity and complexity of documents they worked with during their time at BigLaw firms. A sample of this dataset is available
here
. Each SPA was annotated according to a schema of deal points (
example JSON
) defined in collaboration between our legal research team and clients. We continue to actively solicit and collect feedback to improve our primary schema and define custom schemas for specialized private use cases across document types.
Workflow
Building an agentic workflow using this dataset required understanding the reasoning challenges that standard models faced with correctly understanding and extracting deal points. By categorizing these issues and asking our research team to trace the correct way to reason about these deal points, we were able to identify common patterns that an agentic system would need to improve against in order to perform to our requirements. For example, all foundation models struggle to identify the indemnification cap with respect to Purchaser Fundamental Representations in the
HealthEquity SPA
. Correctly identifying this cap requires building systems that are able to reason effectively across multiple layers of cross-references, as this cap requires a model to consider, at least:
Section 5.2(d): defining the cap as "limited to an amount equal to the Purchase Price actually due to the Sellers”;
The definition of “Purchase Price”: as an amount equal to the Final Consideration, plus the Escrow Amount (if any released to the Sellers);
The definition of “Final Consideration”: as “(i) the Base Consideration, plus [a number of other factors]”;
The definition of “Base Consideration”: which “has the meaning set forth in Section 2.4”;
And finally to Section 2.4: which sets the Base Consideration at $50,000,000.
Then reason back through these various layers to correctly contextualize the value of this deal point. These traces, along with other qualitative analyses, were used to build a system composed of multiple LLMs and traditional ML techniques that effectively reason about and extract the relevant deal points from the target documents. Because the entire system is specialized for a single task, we are able to achieve better performance than is possible in the base Harvey platform and significantly better than the capabilities of general purpose foundation models.
In addition to accuracy, our system is designed to deliver on two other key components of an effective LLM answer—transparent reasoning and sources. Foundation models may return partially correct answers, but they do so without elaboration. Asking for details often confounds models or locks them into poor reasoning patterns, making scores worse. In contrast, Harvey’s agents are able to deliver exceptional accuracy, and build confidence in these results by providing both a reason for each data point returned and source(s) that backs up its conclusion.
Evaluation
We evaluated our agentic system, as well as existing foundation models, on the BigLaw Bench SPA set. This set consists of a set of SPAs not used in the building of our agentic system to ensure generalization of processes and avoid overfitting. For evaluation, we compute accuracy compared to the ground truth deal points as extracted and verified by BigLaw attorneys. For fields that are not string-typed (e.g. dates, numbers, booleans), we perform exact matches once the fields are normalized. For text based fields we used a model to compare matches and verified model grader efficacy with BigLaw attorneys. Overall accuracy is computed as a straight average over the test set and all the individual fields.
Next steps
We plan to continue expanding BigLaw Bench to include more workflows and more complex tasks. By continuing to make BigLaw Bench methodologies and data public we will provide the industry with ideas for more rigorous and realistic benchmarks and encourage other providers to do the same. We think this is the first step towards more standardized benchmarking for the industry as a whole.
We also hope these workflows serve as inspiration for our present and future clients. We’ve had a lot of requests for workflows and will be incorporating them into the Assistant and Vault products over the next few months.
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
