---
title: "3 Principles That Helped us Scale Agent Development"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/principles-that-helped-us-scale-agent-development"
scraped: "2026-05-10T01:27:16.230734+00:00"
lastmod: "2025-11-03T17:00:00.000Z"
type: "sitemap"
---

# 3 Principles That Helped us Scale Agent Development

**Source**: [https://www.harvey.ai/blog/principles-that-helped-us-scale-agent-development](https://www.harvey.ai/blog/principles-that-helped-us-scale-agent-development)

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
3 Principles That Helped us Scale Agent Development
Harvey engineers share why we adopted agents and how the shift to an agent framework helped scale feature development and accelerate delivery.
by
Philip Cerles
,
Philip Lan
,
Aaron Stern
,
Boling Yang
,
Varun Nair
,
Kevin Ko
, and
Billy Wan
•
Nov 3, 2025
Agents have solidified from marketing speak to practical engineering systems. At Harvey, our
Assistant
’s shift from prompts and bespoke orchestration to a fully agentic system meant big changes for both our codebase and how teams collaborate.
In this post, we’ll cover why we adopted agents and how Tool Bundles and eval gates let us scale in‑thread features alongside the number of engineering teams at Harvey. We’ll also share what broke along the way and how this shift to an agent framework ultimately enabled us to
scale feature development and accelerate delivery
.
Why We Adopted an Agent Framework
The Assistant team’s goal is to
proactively plan, create, and execute
end‑to‑end tasks on our customers’ behalf, using tools from inside and outside of Harvey. Our system integrates core building blocks — retrieval, drafting, and review — into one powerful thread. Depending on the question a customer asks, the correct answer might be:
Make multiple retrieval requests to a specialized tax law database, then check them against recent news.
Decide to pull in new information from a customer’s Vault to tackle a tricky section in a long draft.
Add new columns to a document review table and then aggregate over them.
This year, our Assistant also became the home for critical integrations (like
Ask LexisNexis
and
iManage
) and new product modes (for example, Deep Research). Our goal was to enable other teams to contribute these integrations into Assistant, rather than relying on our team to integrate it into a monolithic system.
These two problems — open‑ended problem solving and many integrations — are well‑suited to an agent framework because it can cleanly separate capabilities ("adding columns," "editing drafts," "searching Lexis") from the model’s reasoning. Adopting a single agent framework scaled our in‑thread feature development from one team to four, led to emergent feature combinations, and enabled centralized eval. But switching to agents also introduced new collaboration and org‑scaling challenges. We had to design new interfaces and new testing methodologies for those teams to move quickly.
“
The hardest part of adopting agents isn’t writing the code — it’s learning, as an engineering org, to share ownership of a single brain.
”
Throughout this process, one thing became clear: The hardest part of adopting agents isn’t writing the code — it’s learning, as an engineering org, to share ownership of a single brain.
Pre-Agent Development
Before agents, the Assistant team’s AI feature development was straightforward: write Python, mix it with LLMs, run an eval, then ship it. This led to highly tuned systems that enabled us to release benchmark-leading numbers on our internal datasets.
As we pulled new features into the Assistant framework, we routed them with design. Need to draft? Use Draft mode. Need to pull in a knowledge source? Surface knowledge source recommendations. New features that other teams added were limited to retrieval knowledge sources.
Then we hit a UX, engineering, and collaboration wall. People weren't discovering Draft mode. Integrating multiple retrieval calls behind a single interface was complex to maintain. New features, like
Ask LexisNexis
, didn't have a clear path to launch.
Early Challenges With Adopting Agents
In mid-2025, we decided to shift to a pure agent framework. Forced retrieval calls became tool calls, new integrations became tool calls, and bespoke editing logic became (you guessed it) tool calls, along with a growing system prompt.
Our first intuition was that collaboration with agents was going to be easy. One team owns the system prompt, one owns the tools. But as we started developing with agents, we realized that each new capability required its own set of directions within the main system prompt. And as soon as multiple engineers modify the system's core instructions, there's the potential to step on each other's toes.
“
As one of our developers put it, ‘You're no longer merging unit-testable code, you're merging English.’
”
If developer A is focused on improving tool recall for retrieval tools, they might be tempted to tell the system prompt: "Call all the tools at your disposal." However, developer B might be working on reducing the average latency of queries and instruct the system prompt, "Don't overthink things and take the fastest path to the goal." In an orchestrated system, these two engineers work on different parts. But in an agentic system, their goals directly collide. As one of our developers put it, "You're no longer merging unit-testable code, you're merging English."
How We Scaled Agent Development
We had three goals with agent development at Harvey:
High quality output that gets better over time:
We wanted to
leverage the capabilities of models to their fullest.
Interoperability between new features:
Capabilities, like retrieval or drafting, should naturally work together.
Minimal involvement from a centralized team:
One team shouldn’t own adding all new capabilities, or we can’t scale feature development.
In order to achieve this goals, we adopted three core principles, which we walk through in more detail below:
No Custom Orchestration:
All new product features that live in Assistant are Tool Bundles, and every top‑level thread interface is an agent.
Capabilities are Tool Bundles
: Give partial control of the system prompt to feature developers and bundle multiple tools into one capability.
Eval Gates on Capabilities
: Tool Bundles and system prompt upgrades must pass leave-one-out gates to be deployed.
1. No Custom Orchestration
Individual product developers at Harvey were used to writing bespoke orchestration to accomplish goals. For example, a case law research product would deterministically query a user's document, then use the result to investigate recent case law.
While this is always the shorter path to a product goal, it quickly introduces the same web of routing and human decision-making — and goes against goals one and two.
In this case, a strong interface can help. We decided to adopt an external library, the OpenAI Agent SDK, instead of writing our own agent library. Compared to other frameworks, it explicitly left out an option to orchestrate code in a more "workflow" type format. Rather than being negative, this lack of flexibility forced our team to work with the strengths of the newest generation of models — calling tools in a loop — rather than building hybrid systems.
While we couldn't guarantee determinism in execution for the case law product, it turned out that we hit high rates of recall with a tuned prompt. And by adhering to the framework, we immediately unlocked integration with other knowledge sources and our deep research system.
2. Capabilities are Tool Bundles
An agent at Harvey is composed of a system prompt and a set of Tool Bundles. A
Tool Bundle
is an interface we designed that allows developers to package together new capabilities, which may be composed of multiple tools or sub-agents, into a single entity. For example, a file system Tool Bundle comprises a grep-like file search tool, a file open tool, and a semantic search tool, along with instructions that guide the model on how to leverage these together. A drafting Tool Bundle comprises an editing tool and a drafting sub-agent.
Tool Bundles give feature and integration developers the freedom to inject instructions into the main agent system prompt to achieve their capabilities without needing to make a request of the Assistant team. They also enable capabilities to be portable between different agents. Most importantly, Tool Bundles allow us to apply leave-one-out validation gating on key benchmarks.
3. Eval Gates on Capabilities
A contribution-based framework leads to three major risks for system performance:
System Prompt → Tool Bundle conflicts:
If the reasoning component of the system prompt is updated to push for fast decision-making, the model may drop its recall on specific tools.
Tool Bundle → System Prompt conflicts:
If a Tool Bundle mandates that the model must “always call every tool,” the agent will call tools in other bundles.
Context rot:
If the new tool outputs significant context, the agent can suffer from context rot.
Harvey guards against this by requiring the Assistant team and feature and integration developers to maintain datasets and evaluators for each of their Tool Bundles, along with thresholds that fire if metrics drop below a certain score. For example, our retrieval dataset defines a large number of queries with expected recall across a set of knowledge sources. When any change is made to the system, developers can verify that their capability has not regressed.
Developing Agents With the Right Safeguards
Agents allow you to scale feature development in thread products to the size of your engineering team, but they are a deceptively complex surface to develop. At Harvey, a “no custom orchestration” rule kept behavior centralized, Tool Bundles gave teams a safe contribution model, and eval gates protect quality as our capabilities multiply.
Harvey's Engineering team is hard at work building new capabilities, behaviors, and context management into our agents. Here are some other technical challenges we’re working on:
Deepening our understanding of agents and introducing new best practices around system prompt and tool design.
Scaling our eval gating framework to more capabilities — how do we smartly test for a combinatorial number of Tool Bundles?
Leveraging reinforcement-fine-tuning to improve tool recall, answer quality, and reduce reliance on prompt engineering.
If these problems sound interesting to you,
we're hiring for roles across the Engineering team
.
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
