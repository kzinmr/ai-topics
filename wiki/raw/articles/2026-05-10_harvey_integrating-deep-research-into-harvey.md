---
title: "Integrating Deep Research into Harvey"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/integrating-deep-research-into-harvey"
scraped: "2026-05-10T01:27:03.514000+00:00"
lastmod: "2025-07-03T17:10:32.900Z"
type: "sitemap"
---

# Integrating Deep Research into Harvey

**Source**: [https://www.harvey.ai/blog/integrating-deep-research-into-harvey](https://www.harvey.ai/blog/integrating-deep-research-into-harvey)

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
Integrating Deep Research into :Harvey:
Learn how we integrated Deep Research within Harvey less than 12 hours after the Deep Research API was released by OpenAI.
by
Harvey Team
•
Jul 3, 2025
Overview
The pace of AI continues to accelerate, with significant advancements being announced on a near-weekly basis. At Harvey, a core part of our mission is to translate AI breakthroughs into reliable and secure products capable of solving the world’s most complex legal work – and deliver that value as quickly as possible.
Last week, we put this mission to the test, integrating
Deep Research within Harvey
less than 12 hours after it was released by OpenAI.
Our ability to rapidly deliver AI-enabled features is a result of two foundational investments we've made in our research and engineering organization from day one:
AI-native architecture:
Harvey is purpose-built for complex model systems and agents. We have developed AI sub-systems – such as our citation engine, tools for visualizing model reasoning and search results, and frameworks for model orchestration – that are modular and easily extensible.
Culture of iterative development:
Harvey’s engineering and research culture supports (and encourages) rapid, high-quality iteration and prototyping – an operating model increasingly supercharged by our own internal use of AI-assisted coding tools.
In this post, we'll pull back the curtain on a few of the systems, tools, and cultural principles that enabled our swift incorporation of Deep Research, and share how they fuel a larger capacity to continuously deliver enterprise-grade AI products and services.
Workflow Engine
The Harvey platform has a number of product surfaces that allow users to engage with Harvey agents. Underlying each of them is a modular and extensible framework for composing model systems and orchestrating agent behavior. Particularly relevant to this release is a part of that framework that we call the
Workflow Engine
.
The Workflow Engine underpins both our
Workflows
product and newly released
Workflow Builder
. Here we outline a few of its core features that helped to accelerate our deployment of Deep Research:
AI building blocks
Workflow Engine expresses our internally-developed AI primitives as low-code, composable blocks. These blocks can be sequenced together by a developer or, in an agentic system, called as tools to create and execute end-to-end workflows for a particular legal task. We can quickly create new, multi-step processes as needed, reducing overall development time, increasing flexibility, and minimizing the risk of regression elsewhere in the system.
"Thinking states"
A key principle for the Harvey user experience is transparency. With our native “thinking states”, we provide users with visibility into an agent’s plan and how decisions are made with the user in the loop.
The Workflow Engine allows us to seamlessly integrate the reasoning states and actions of any model directly into our system, enabling users to:
Evaluate intermediate results in an easy-to-ingest format.
Follow along with real-time context about what the models are thinking as they work.
Intervene at any step—adding context, tweaking parameters, or rerunning actions—to course-correct and ensure the final output matches their intent.
Traceable and verifiable steps
At Harvey, we have always prioritized
high-quality citations
as means for understanding and interpreting AI answers. We successfully incorporated the URL citations produced by Deep Research into our citation system, so every step of the workflow can be traced and verified. This is essential for trust and verification in legal applications and also streamlines our development process.
AI-Assisted Development
Upon release of the API, we wanted to understand how to use and integrate it into our codebase as quickly as possible. As part of our culture of rapid prototyping, we embrace the use of AI tools, although this development cycle had some unique challenges to overcome. In particular:
Deep Research was brand new and not part of base LLM knowledge, nor was there much documentation online at the time
Streaming mode for the API was a long-running operation with 20+ dynamic output types, which would need multiple rounds of iteration and exploration to discover
We wanted to make the code compatible with our internal product frameworks, such as the Workflow Engine and thinking states mentioned above
In this scenario, we found it most effective for an engineer to facilitate an iteration loop with an AI coding assistant.
Two other practices were very helpful in accelerating development:
Dumping the full log of streamed API outputs in both
pydantic
and
json
formats. This was used as context for both humans and AI tools to understand the API format and write code for it.
Using streamlit as a tool to quickly build interactive UIs in Python. We have
open-sourced the starter code on GitHub
.
The Future
At Harvey, we’ve spent the last year assembling a suite of core capabilities—including
Vault
,
Knowledge Sources
, and
Word Add-In
—each purpose-built for tasks like document review or authoritative research. The next leap is to weave these capabilities into a single, seamless workspace.
The key to unlocking unification is
tool use
: letting the model intelligently choose and run the right tool at the right moment. Re-framing our building blocks through this lens delivers two decisive advantages:
Unification
: A single collaborative, intuitive interface.
Agency:
Autonomous execution of increasingly sophisticated workflows, always under user oversight
Building Deep Research is one major stride towards that vision, expanding Harvey’s AI capabilities towards increasingly complex and reliable
end-to-end work
. This feature is currently undergoing internal testing and will be available more broadly soon, starting with an early access period. More information will follow in the coming weeks.
Contributors: Pablo Felgueres, Philip Lan, Spencer Poff, Calvin Qi, Karl de la Roche, Julio Pereyra, Niko Grupen
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
