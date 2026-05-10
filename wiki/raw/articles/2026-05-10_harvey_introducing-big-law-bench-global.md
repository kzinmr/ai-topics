---
title: "Introducing BigLaw Bench: Global"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/introducing-big-law-bench-global"
scraped: "2026-05-10T01:27:30.831759+00:00"
lastmod: "2026-02-18T20:00:00.000Z"
type: "sitemap"
---

# Introducing BigLaw Bench: Global

**Source**: [https://www.harvey.ai/blog/introducing-big-law-bench-global](https://www.harvey.ai/blog/introducing-big-law-bench-global)

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
Introducing BigLaw Bench: Global
BLB: Global is built to understand models’ ability to deliver on core AI tasks for our customers around the world, starting with the UK, Australia, and Spain.
by
Harvey Team
•
Feb 18, 2026
As we
announced
earlier this month, the first of our three major extensions to BigLaw Bench (BLB) is our Global dataset. BLB: Global extends the principles of BLB by working with local experts to build benchmarks reflecting the nuance of legal work in global jurisdictions.
Designed in collaboration with our data partners at Mercor, one of the world’s leading companies in the expert data space, BLB: Global is built to understand models’ ability to deliver on the core promises of AI for our customers around the world. This understanding will enable us to ensure that customers across jurisdictions can execute core AI workflows accurately, consistently, and in alignment with local norms.
Our initial BLB: Global dataset more than doubles the size of our public-facing BLB benchmark, adding unique benchmarks for the UK, Australia, and Spain. Throughout the rest of this post, we discuss how we built BLB: Global, what it’s focused on benchmarking, and how we intend to extend it.
Core Tasks, Local Nuance
Over time, models have steadily performed better on BigLaw Bench, with various leading foundation models now meeting around 90% of the criteria required to successfully complete the enumerated tasks. These improvements have tracked the realities of model intelligence — LLMs now routinely deliver effective results on core legal tasks. However, we still see models struggle on particular tasks due to difficulties in either recalling or applying particular legal principles.
In separate research, we have seen that these struggles can increase as models are applied in more and more localized settings. The goal of BLB: Global is to help understand and remediate where foundation models struggle to localize effectively on core AI tasks.
“
The goal of BLB: Global is to help understand and remediate where foundation models struggle to localize effectively on core AI tasks.
”
Specifically, we identified six major categories of tasks that our customers say they routinely find (or hope to find) value in models:
Drafting:
The production of legal documents ranging from legal analysis memos to contracts.
Long Document Analysis:
The analysis of lengthy documents for key points, risks, or other legal features.
Document Comparison:
Critical or strategic comparison between two documents such as redlines or a regulatory requirement and its implementing policy.
Public Research:
Research of publicly available information to either provide strategic context or answer precise legal questions.
Multi-Document Analysis:
Answering questions relying on multiple documents from a large corpus of provided information.
Extraction:
Converting documents into structured data or semi-structured data such as contract clauses or litigation claims.
Not only do these tasks provide immediate value for lawyers, they also represent the building blocks of capabilities that allow models to deliver value in more complex work. These task categories were converted into rich, real-world scenarios by experts from different practice areas such as:
Country
Task Type
Task Description
UK
Public Research
A Chief Strategy Officer sells shares before a failed drug trial announcement. Advise on potential criminal prosecution and FCA civil enforcement, including whether a cooperative strategy may be legally advantageous.
Spain
Drafting
HR directors of six competing Spanish tech companies reach a "gentlemen's agreement" on salary caps and no-poach rules, which one director proudly describes in a media interview. Draft a research memo analyzing legal classification and potential CNMC fines. (Translated from original Spanish.)
Australia
Multi-Document Analysis
An infrastructure fund backed by sovereign wealth funds and a state pension seeks to acquire a 20.5% interest in an Australian waste-to-energy project during a turbine replacement. Determine whether FIRB approval is required.
Each scenario represents two things. First, an intrinsically useful task. Second, proof of capabilities to execute a general category of useful tasks. Measuring both helps us deeply understand model capabilities across the globe.
Built With Local Experts
To build out specific tasks for these categories, we worked with local experts to build the same complex data that supports BLB. These experts were drawn from experienced legal practitioners and selected for both their legal expertise and their ability to work well with AI data. Each practitioner’s task choice and data was also cross-reviewed by Harvey Applied Legal Researchers to ensure data quality standards and alignment with our customers’ practice focuses. Overall, our initial global set represents close collaboration between more than two dozen experts.
In building BLB: Global, we also focused on balancing benchmark quality with providing local experts flexibility to express their own judgments about the tasks that were valuable in their jurisdiction. This freedom created more diverse datasets and richer perspectives on what types of legal tasks a model should be expected to perform. As models support a growing number of customers in additional countries, this breadth helps us ensure they are doing so at a consistent quality level.
Next Steps for BLB: Global
While three new countries is a start, it’s hardly the end of building a truly global dataset. We will continue to build local expert cohorts and benchmarks for new countries. Additionally, we will deepen existing datasets with new tasks as we identify areas of focus in collaboration with our customers.
Separately, we will internationalize other key Harvey benchmarks like
BLB: Arena
to capture lawyer-driven preferences and provide a full picture of model performance in the localities where our customers are delivering legal services.
Ultimately, BLB: Global is about enabling our customers to work globally without sacrificing quality or confidence. Measuring how models perform on the same core legal tasks across jurisdictions helps ensure that Harvey delivers consistent, reliable performance wherever work takes place.
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
