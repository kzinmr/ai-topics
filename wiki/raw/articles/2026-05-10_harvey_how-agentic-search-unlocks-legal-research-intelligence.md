---
title: "How Agentic Search Unlocks Legal Research Intelligence at Harvey"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/how-agentic-search-unlocks-legal-research-intelligence"
scraped: "2026-05-10T01:27:20.223982+00:00"
lastmod: "2025-12-10T13:00:00.000Z"
type: "sitemap"
---

# How Agentic Search Unlocks Legal Research Intelligence at Harvey

**Source**: [https://www.harvey.ai/blog/how-agentic-search-unlocks-legal-research-intelligence](https://www.harvey.ai/blog/how-agentic-search-unlocks-legal-research-intelligence)

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
How Agentic Search Unlocks Legal Research Intelligence at :Harvey:
A look at how we implemented agentic search to handle the complex, multi-source queries that define legal work.
by
Lysia Li
,
Varun Nair
,
Aaron Stern
,
Pablo Felgueres
,
Calvin Qi
, and
Philip Cerles
•
Dec 10, 2025
Legal research has always been iterative: searching case law, discovering a new angle, refining your query, checking another jurisdiction, cross-referencing with statutes, and repeat. This natural back-and-forth, or reasoning loop, is fundamental to how lawyers work. Traditional retrieval systems, however, reduce this nuanced process to a single query-and-retrieve operation.
At Harvey, we built
Agentic Search
to mirror how legal professionals actually conduct research. The key was moving from static, one-shot retrieval to a system that reasons about what information it needs, where to find it, and when to dig deeper.
This capability helps raise the baseline quality of queries in Harvey Assistant
, while also serving as the technical foundation for Deep Research — our most comprehensive mode for multi-source legal analysis.
In this post, we'll walk through what agentic search is, why it matters for legal research, and how we implemented it to handle the complex, multi-source queries that define legal work.
Complex Legal Research Requires Intelligent Search
To understand why we needed agentic search, it’s helpful to walk through an example of a type of query that traditional retrieval systems struggle with. Let’s focus on
due diligence
.
Imagine conducting due diligence on an acquisition target and using this prompt in Harvey: "Review all employment agreements in the data room and identify any non-compete provisions that may be unenforceable under California law. For each provision, cite the relevant California statute or case law."
This requires:
Analyzing employment agreements stored in the
Vault
data room to extract non-compete clauses
Researching California statutes (e.g. California Business and Professions Code Section 16600)
Finding relevant California case law on non-compete enforceability and exceptions
Cross-referencing each identified provision against those legal standards
Synthesizing findings with specific citations to both the internal documents and legal authorities
The agent must move fluidly between document analysis and legal research, understanding how initial diligence findings trigger the need for additional statutory or case law research, and then applying those legal standards back in order to analyze the specific provisions it found necessitating the research. This requires reasoning about what information is needed, where it lives, and how to synthesize it — capabilities that sit at the core of agentic Retrieval Augmented Generation (RAG).
Traditional one-shot retrieval fails here because it can't adapt its strategy as it discovers information; it can't decide which knowledge sources are relevant; and it can't determine when it has gathered sufficient context. The query demands an intelligent system that reasons about the research process itself.
What is Agentic Search and Why Does it Matter?
Agentic Search represents a paradigm shift in how we approach complex information retrieval.
From Naive RAG to Agentic Search
Naive RAG follows a straightforward pattern: embed the query, retrieve relevant chunks, generate an answer. This works for simple queries but breaks down when research requires multiple rounds of information gathering, synthesis across sources, or reasoning about missing information — exactly like the due diligence example above.
Agentic search transforms this into an iterative reasoning process. The system plans its approach, decides which sources to query, evaluates whether it has sufficient information, and refines its strategy based on discoveries. Here’s a quick comparison between naive RAG and agentic search:
Why Agentic Search Matters for Legal Research
Given the characteristics above, there are a few key reasons why agentic search matters for legal research:
Improved accuracy and reduced hallucinations:
Responses are based on verified, current data from multiple sources that can be traced back to specific documents or database entries. The agent can check answer relevancy and rewrite queries, iterating until achieving the best response — critical for legal work where accuracy is non-negotiable.
Real-time relevance:
Access to the latest case law, regulatory updates, and client documents means the agent operates with up-to-date knowledge across both foundational precedent and recent developments.
Enhanced contextual understanding:
Legal questions involve jurisdiction-specific nuances, practice area context, and implicit requirements that benefit from iterative refinement and intelligent query handling.
Scalable knowledge:
Agents tap into Harvey's 150+ legal
knowledge sources
, internal Vault documents,
iManage integration
, and proprietary databases like case law knowledge through LexisNexis.
How We Use Agentic Search to Solve Legal Research
Building an agentic RAG system requires careful orchestration between reasoning and retrieval. At Harvey, we designed our system around a workflow that allows the agent to make intelligent decisions about when and where to search, evaluate the sufficiency of retrieved information, and determine when it has enough context to answer.
The Agentic Search Workflow
Our implementation follows a reasoning-driven retrieval loop inspired by the ReAct (Reasoning and Acting) paradigm, where the agent interleaves reasoning traces with tool calls:
Query Understanding and Planning:
The agent analyzes what information is needed and develops a search strategy. For complex queries, it identifies which knowledge sources will be relevant.
Dynamic Tool Selection and Retrieval:
The agent decides which sources to query and formulates specific search queries for each. It then executes searches and retrieves relevant information.
Reasoning and Synthesis:
The agent reasons about how the retrieved information connects and applies legal standards to specific facts or provisions.
Completeness Check:
The agent evaluates whether it has sufficient information to fully address the query. If gaps remain, it returns to Step 2 for additional retrieval rounds with refined queries.
Citation-Backed Response:
Once satisfied with the gathered context, the agent synthesizes findings into a comprehensive response with specific citations to source documents.
In the Harvey platform, this workflow enables faster Assistant queries and comprehensive
Deep Research
reports — all powered by agents that can seamlessly query, reconcile, and synthesize across multiple knowledge sources.
Key Challenges With Agentic Search
Building this system revealed three fundamental challenges that went beyond standard RAG implementation. Here’s a quick overview of each before we dig into how we solved these challenges.
Challenge 1: Source Selection in the Wild
Our initial prototype worked well on carefully constructed test queries, but real user queries proved more challenging. Lawyers phrase queries with implicit context — a question like "What's our exposure on the termination provisions?" might require searching internal deal documents, checking market standards, and consulting case law, but doesn't explicitly enumerate these sources. The model would often query only one or two sources when broader coverage was needed.
Challenge 2: Scaling Tool Calls to Query Complexity
Simple questions like "What's the notice period in section 8.2?" should resolve quickly with minimal retrieval, while complex questions should trigger extensive research. Initially, the agent treated nearly every query the same way — making one or two tool calls and moving on. The agent lacked a calibrated sense of when "good enough" was sufficient and when a query demanded exhaustive coverage.
Challenge 3: Multi-Source Citations
Our citation system had historically been built and benchmarked on single-source queries. In order to support multi-source queries, we had to ensure our system built upon the foundational improvements made for each source’s citation quality, while remaining flexible enough to adapt to context from multiple sources. We also invested in citation benchmarking sets that captured the full spectrum of multi-source queries — from those that specified exactly which sources were preferred to those that were far more open-ended.
Our Solution: Building Quality Through Privacy-Preserving Evaluation
These challenges — source selection and scaling effort to complexity — required a systematic approach to improvement. Since Harvey's
privacy guarantees
mean no human has access to or reviews actual customer queries, we faced the question: How do you improve a system when you can't directly observe its real-world performance?
Our solution was to build a systematic evaluation process powered by Harvey's in-house legal experts. Applied Legal Researchers (ALRs) and Strategic Business Development Leads (SBDLs) are former practicing lawyers who collaborate closely with Engineering on product development. In partnership with these teams, we developed a data flywheel that continuously improves the system:
Query Pattern Mining:
After receiving aggregated feedback and support tickets that describe issues, our Legal team analyzes these patterns to understand common failure modes.
Expert Query Generation:
ALRs and SBDLs create evaluation queries that capture real usage patterns, spanning from straightforward searches to multi-jurisdictional analysis.
Rapid Prototyping and Testing:
We build the initial prototype quickly then aggressively test it with our legal team. This tight feedback loop helps us surface issues, fast.
Systematic Evaluation:
Centralized evaluation infrastructure that we built using the OpenAI Agent SDK's OpenTelemetry traces enables us to run offline evaluations in LangSmith. We track metrics like hallucination, tool recall, retrieval recall, formatting, and answer quality.
Targeted Improvements:
We iteratively refine tool design, system prompts, tool bundles and preambles, and tool docstrings.
Continuous Feedback:
As we deploy improvements, our Legal team continues testing with new query patterns and customer feedback informs the next round of eval development.
This approach solved our source selection challenge by giving the agent clearer signals about when to use each knowledge source —
improving tool selection precision from near zero to 0.8-0.9
. For the tool-calling intelligence challenge, we used eval data to calibrate the agent's effort level. Complex queries that initially resolved in a single tool call now appropriately
scale to 3-10 retrieval operations
based on query demands.
What's Next for Agentic Search
Agentic Search brings reasoning to retrieval, enabling Harvey to handle a wide range of tasks, from quick document lookups to comprehensive multi-source legal research. By building a privacy-preserving evaluation system powered by legal experts, we've created a system that continuously improves while still maintaining the data protections fundamental to Harvey.
This represents a significant step forward in legal research intelligence, but there's more work ahead. Our team is focused on these key areas:
Improving AI quality:
Continuing to iterate on tool design, reasoning patterns, and evaluation metrics that capture the nuances of legal research quality.
Expanding knowledge coverage:
Integrating additional legal knowledge sources and databases to ensure agents can access the full breadth of information lawyers need.
Reinforcement fine-tuning on tool use:
Exploring reinforcement fine-tuning to improve tool recall and routing decisions while reducing reliance on complex prompt engineering.
If these challenges sound interesting to you,
we're hiring for roles across the Engineering team
.
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
