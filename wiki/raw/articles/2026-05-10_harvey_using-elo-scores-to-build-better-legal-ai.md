---
title: "How We Use ELO Scores to Build Better Legal AI"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/using-elo-scores-to-build-better-legal-ai"
scraped: "2026-05-10T01:27:01.296109+00:00"
lastmod: "2026-02-26T16:00:00.000Z"
type: "sitemap"
---

# How We Use ELO Scores to Build Better Legal AI

**Source**: [https://www.harvey.ai/blog/using-elo-scores-to-build-better-legal-ai](https://www.harvey.ai/blog/using-elo-scores-to-build-better-legal-ai)

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
How We Use ELO Scores to Build Better Legal AI
Turning human preference into measurable, meaningful improvements across the Harvey platform.
by
Harvey Team
•
Feb 26, 2026
In BigLaw Bench: Arena, we described our system for scaling human preference over results. The core artifacts produced by that system are ELO scores for Harvey systems and non-Harvey baselines. These scores help us understand how likely the output of one system is to be preferred to another when both outputs are presented to lawyers.
To make this concrete, the
Assistant
ELO scores from
BLB: Arena
suggest that the responses of Harvey Assistant are
preferred more than 70% of the time to those of generic foundation models
.
Importantly, we use ELO not just to celebrate the results of applied AI work, but also to help shape that work. In the rest of this post, we explain how we use ELO generally to understand and improve AI systems through specific, recent examples from across Harvey’s products.
ELO Explained
ELO is a rating system for competitors originally used in chess and later adopted to measure skill in many competitive games. It converts a large number of head-to-head wins and losses into a single, comparative measure of how good a competitor (e.g., an AI system) is.
Specifically, a pair of ELO scores expresses the
likelihood
that one AI system will win (be preferred in the quality of its output) over another system on any given task. We use ELO at Harvey because it provides an intuitive way to express quality differences between AI systems and measure when those differences become meaningful to our customers.
“
ELO expresses the likelihood that one AI system will [be preferred] to another system on any given task.
”
In practice, an ELO gap of around 150–200 points tends to reflect a clear preference. Roughly speaking, this means the higher-rated system is preferred about 70% of the time. In this case, users routinely report that the better system
feels
clearly better for their work. Smaller gaps than this tend to be qualitatively neutral to customers: some lawyers prefer one system, while others see no difference in practice.
At around a 400-point ELO gap, systems are usually experienced as fundamentally different, not just improved. With this gap, preference for the stronger system exceeds 90%, and users find it more useful almost all the time. Historically at Harvey, shifts of this size have marked genuine step-changes — such as the introduction of sentence-level citations or focused investments in research models like
case law
and
tax
.
Because these patterns recur reliably in human evaluations, we use ELO as a shorthand for understanding when improvements are likely to be felt by customers and how. For that reason, human preference — and the ELO scores derived from it — remains central to how Harvey measures progress and builds meaningfully differentiated AI.
Understanding Systems: Knowledge Sources (November 2025)
The main way we use ELO is to understand what people like and dislike about using AI systems. Oftentimes, we run studies to generate initial ELO scores and then work through the data to convert those scores into a meaningful why. This is especially helpful when we may not have intuitions about a system, such as when we build new international
knowledge sources
.
When building our Australia knowledge source, we contracted with local lawyers to evaluate at scale across various AI systems and figure out what they genuinely preferred. The results were somewhat unsurprising. Lawyers preferred systems that were accurate, drew on primary sources, and provided clear and actionable content from those sources. We used these pillars to build a strongly differentiated Australia knowledge source.
Australia System*
ELO
Harvey Preference Rate (% of time Harvey is preferred over alternative)
Harvey
1500
N/A
GPT-5 (reasoning high)
1333
72.34%
Gemini
1165
87.31%
GPT-5 (no reasoning)
1154
87.99%
OpenAI Deep Research
1133
89.21%
*All systems have web search access
As we extended these research cycles to other countries, we found another nuance that did not exist in Australia. In many countries, localization was a challenge for models even when provided web search access. For instance, questions written in German by Austrian lawyers would often return answers about German law. Adding strong localization to our systems allows us to deliver systems in Austria that are even more differentiated than those in Australia in enabling high quality responses for local legal work.
Austria System*
ELO
Harvey Preference Rate (% of time Harvey Knowledge Source is preferred over alternative)
Harvey (Knowledge Source)
1500
N/A
Harvey (General Web)
1281
77.91%
GPT-5 (Auto)
1181
86.25%
Claude 4.5 Sonnet
907
96.81%
*All systems have web search access
Setting New Standards: EDGAR (December 2025)
Another way we use ELO is to benchmark and improve against a particular standard. When we rebuilt our EDGAR system, we wanted to ensure it remained differentiated not just against generalist models, but against specialized financial data search APIs.
EDGAR System
ELO Before EDGAR Rebuild
Harvey Preference Rate (% of time Harvey EDGAR is preferred over alternative)
Human
1651
29.54%
Harvey (EDGAR)
1500
N/A
Harvey (Web)
1499
50.14%
GPT-5 (Financial Search API)
1489
51.58%
GPT-5 (Web)
1488
51.73%
Our results were surprising: None of these systems were differentiated from each other — each had unique strengths and weaknesses that overall came out neutrally. So, we set a new standard. Building on our general knowledge source understanding, we asked human lawyers to write short, accurate, primary-sourced answers to dozens of EDGAR search questions. These answers handily beat AI systems and set a north star for improvement.
From there, we iterated on our EDGAR system to improve in places where AI-generated answers fall short of human answers (accuracy) and lean in where they tend to excel (tireless detail). The result:
an EDGAR system that can go head-to-head in preference with human experts and is differentiated from other AI systems
. While there are still improvements to be had, ELO allowed us to track and iterate on not just performance, but meaningful performance.
EDGAR System
ELO After EDGAR Rebuild
Harvey Preference Rate (% of time Harvey EDGAR is preferred over alternative)
Harvey (EDGAR)
1695
N/A
Human
1689
50.86%
Harvey (Web)
1491
76.39%
GPT-5 (Financial Search API)
1489
76.6%
GPT-5 (Web)
1488
76.7%
Pushing Our Own Boundaries: Vault (September 2025)
ELO also helps us iterate in places where no external baseline exists. In evaluating Harvey’s
Vault
product, we knew it was as
accurate
as humans on meaningful tasks. But, we wanted to ensure we were presenting that information as usefully and as quickly as possible. So, we set out with three competing objectives:
Could we gain ELO over our existing Vault system while also reducing the time to generate a cell and improving citation quality?
To explore the possibilities, Harvey Applied Legal Researchers competed to build different interpretations of Vault using an array of models, prompts, and other techniques to optimize the relevant parameters. The result was an array of choices for a better Vault system, including several systems that both meaningfully improved human preference and citation quality while drastically reducing latency.
Additionally, we found surprising strengths in unexpected models, such as GPT-4.1-mini’s ability to provide clear, compelling answers (though it struggled on citations). Continuing research on possibilities unlocked by new models is expected to compound these improvements, allowing us to continuously improve the Vault experience as new tools become available.
Vault System (listed by base model)
ELO
Harvey Preference Rate (% of time Harvey A is preferred over alternative)
Citation Quality (% of valid citations)
Latency (average time to complete batch of 50 cells)
Harvey A (GPT-4.1-mini)
1603
N/A
62%
17.37s
Harvey B (GPT-5)
1549
57.71%
97%
11.27s
Harvey C (Sonnet 4)
1538
59.25%
89%
16.29s
Harvey Baseline
1500
64.4%
92%
23.91s
Harvey D (GPT-5-mini)
1454
70.22%
92%
14.04s
Continuous Improvement
The baseline expectations of AI are always shifting. New models, paradigms, and tools are constantly becoming available to push the capabilities of AI in professional services. Human preference and ELO are one of the main tools we use to separate hype from value by turning complex human data into clear insights. Doing so allows us to differentiate from baseline AI capabilities, and continue constantly refining those capabilities to deliver the best AI systems for legal work.
Credits:
The research cited in this post was performed by Cam MacGregor and Olga Baranoff (Vault); Chris Bello (Knowledge Sources), Emilie McConnachie (EDGAR), and Elizabeth Lebens (Assistant)
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
