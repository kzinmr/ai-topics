---
title: "Building an efficient harness for advanced enterprise work"
source: "Glean Blog"
url: "https://www.glean.com/blog/enterprise-agent-harness"
scraped: "2026-07-10T06:00:51.067726+00:00"
lastmod: "None"
type: "sitemap"
---

# Building an efficient harness for advanced enterprise work

**Source**: [https://www.glean.com/blog/enterprise-agent-harness](https://www.glean.com/blog/enterprise-agent-harness)

Product
Platform Overview
See how Glean works.
Connectors & Actions
Glean offers more than 250 connectors
APIs
Build generative AI experiences
Model Hub
Get access to the latest models
AI Gateway
Accurate and efficient tools
Security
Safely scale AI at work
Glean Assistant
Your personal AI assistant
Proactive Intelligence
Anticipate what matters next
Data Analysis & Research
Turn context into insights
Content Creation
Create grounded, on-brand content
Work Execution
Turn insight into action
Glean Agents
Build and manage agents
Agent Builder
Build agents your way
Agent Orchestration
Automate work across systems
Agent Governance
Scale agents with control
Agent Library
Discover trusted, reusable agents
Agent Harness
Plan and adapt intelligently
Glean Enterprise Context
Context for it all.
Enterprise Search
The foundation for answers
Personal Graph
Understand how you work
Enterprise Graph
Understand how your company works
System of Context
Context that boosts productivity
Hybrid Search
Search grounded in context
Glean browser extension
Customers
Solutions
DEPARTMENTS
All Teams
Engineering
Customer Service
Sales
IT
Marketing
B2B Marketing
B2C Marketing
People
Finance
Legal
INDUSTRIES
Retail
Industrials
Energy & Utilities
Manufacturing
Supply Chain
Professional Services
Consulting
Construction
IT Services
Financial Services
Banking
PE/VC
Asset management
Insurance
Government
Healthcare
Higher Education
Joel McKelvey
Head of Solutions, Glean
Abdullah Haydar
Director of Engineering, LinkedIn
Webinar
AI Powered Engineering
Expert insights and actionable strategies for accelerating developer productivity.
Watch now
Resources
EXPLORE
Resource Center
Blog
Prompt Library
Guides
Product Videos
ENGAGE
Webinars
Newsroom
Glean:GO 2026
Events
Gleaniverse Community
SUPPORT & SERVICES
Help Center
Developers
Partners
Work AI Institute
The Work AI Index 2026
Workers say AI saves them 11 hours a week. Where is that time going?
Download the report
Company
About us
Careers
Thank you! Your submission has been received!
Oops! Something went wrong while submitting the form.
Sign in
Get a demo
Get a demo
Sign in
Get a demo
Get a demo
Product
Customers
Solutions
Resources
Company
Sign in
Sign in
Get a demo
Get a demo
PRODUCT
Platform Overview
See how Glean works.
Connectors & Actions
Glean offers more than 250 connectors
APIs
Build generative AI experiences
Model Hub
Get access to the latest models
AI Gateway
Accurate and efficient tools
Security
Safely scale AI at work
Glean Assistant
Your personal AI assistant
Proactive Intelligence
Anticipate what matters next
Data Analysis & Research
Turn context into insights
Content Creation
Create grounded, on-brand content
Work Execution
Turn insight into action
Glean Agents
Build and manage agents
Agent Builder
Build agents your way
Agent Orchestration
Automate work across systems
Agent Governance
Scale agents with control
Agent Library
Discover trusted, reusable agents
Agent Harness
Plan and adapt intelligently
Glean Enterprise Context
Context for it all.
Enterprise Search
The foundation for answers
Personal Graph
Understand how you work
Enterprise Graph
Understand how your company works
System of Context
Context that boosts productivity
Hybrid Search
Search grounded in context
Glean browser extension
Sign in
Get a demo
Get a demo
SOLUTIONS
DEPARTMENTS
All Teams
Engineering
Customer Service
Sales
IT
Marketing
B2B Marketing
B2C Marketing
People
Finance
Legal
INDUSTRIES
Retail
Industrials
Energy & Utilities
Manufacturing
Supply Chain
Professional Services
Consulting
Construction
IT Services
Financial Services
Banking
PE/VC
Asset management
Insurance
Government
Healthcare
Higher Education
Joel McKelvey
Head of Solutions, Glean
Abdullah Haydar
Director of Engineering, LinkedIn
Webinar
AI Powered Engineering
Expert insights and actionable strategies for accelerating developer productivity.
Watch now
Sign in
Get a demo
Get a demo
RESOURCES
EXPLORE
Resource Center
Blog
Prompt Library
Guides
Product Videos
ENGAGE
Webinars
Newsroom
Glean:GO 2026
Events
Gleaniverse Community
SUPPORT & SERVICES
Help Center
Developers
Partners
Work AI Institute
The Work AI Index 2026
Workers say AI saves them 11 hours a week. Where is that time going?
Download the report
Sign in
Get a demo
Get a demo
COMPANY
About us
Careers
Last updated Jul 09, 2026.
Building an efficient harness for advanced enterprise work
0
minutes read
Michael Cao
Software Engineer
Cathy Chen
Software Engineer
Nikhil Mandava
Engineering
Selene Kim
Product Manager
Listen to article
0:00
0.5x
1x
1.5x
2x
Table of contents
Heading 2
Heading 3
Heading 4
Heading 5
Heading 6
Have questions or want a demo?
We’re here to help! Click the button below and we’ll be in touch.
Get a Demo
Share this article:
Listen to article
0:00
0.5x
1x
1.5x
2x
Agent harnesses are often discussed as a way to help agents take on longer-running, more complex work. Glean’s agent harness accomplishes this in multiple ways, primarily through context management that lets agents reason effectively across tools, data, and workflows. The harness also supports
trace learning
, helping agent systems self-improve based on past sessions. Routing allows
specialist models
to take on the work they’re best suited to handle, so agents achieve high quality outcomes at lower costs.
But harness design isn’t just about making agents more capable. It’s also critical to token efficiency. In this post, we walk through how we moved our harness to orchestrate tools for every query using code, and how this approach proved more efficient, even for simple queries. Compared to our previous approach, it reduced token usage by 24%. We’ll also examine the key design decisions along the way that made those results possible.
Agent harnesses scale best with 100% programmatic tool-calling
The defining feature of Glean's agent harness is 100% programmatic tool calling. Instead of issuing standard tool calls directly, the model writes code in the agent sandbox, calling Glean capabilities through the Python runtime and tools SDK. Code is a better execution primitive than standard tool calls because orchestration, filtering, looping, and branching can all happen within a single script execution instead of being scattered across multiple LLM round-trips.
In a standard tool-calling loop, every tool input and output gets serialized and deserialized back into the context window. The model calls a tool, the result lands in context, the model reads it and calls the next tool. For a workflow touching dozens of documents across multiple systems, that pattern adds token waste, latency, and reasoning overhead that has nothing to do with the actual task logic.
Our first attempt at programmatic tool-calling was a hybrid approach. Standard tool-calling handled simple, single-step operations, while programmatic tool-calling handled multi-tool work. But requiring the model to decide which mode to use on every turn introduced its own overhead, which ate into the efficiency gains we were trying to achieve. It turns out models are just as good at writing a short script for a single tool call as they are at making a standard tool call.
So we removed standard tool-calling entirely. The shell is now the only tool exposed to the model directly, letting the agent write and run scripts in the sandbox for anything it needs to call. Every other capability, including search, write tools, skills, is exposed through Glean's tools SDK.
Tool truncation links context with the sandbox filesystem
A coding harness like this needs a sandbox filesystem to hold tool outputs, intermediate steps, data, and reasoning. That output stays on disk between turns instead of flooding model context, which is reserved for high-signal reasoning, decisions, and truncated tool results. Keeping only the most informative parts of a workflow in the context window helps the harness avoid context rot and stay reliable through long-running work that requires complex reasoning over large amounts of data.
Every harness has to decide how much of a tool's output the model actually sees. If everything stays in context, performance degrades as context accumulates and the model loses attention. If everything gets summarized, the model can lose key information it needs. Over-summarizing has a hidden cost too: since the model doesn't know the structure of a given tool's output ahead of time, it can burn tokens just figuring out how to read data from the filesystem.
In Glean’s coding harness, each tool call returns a truncated preview, writes the full output to a file, and tells the model exactly how much content is sitting on disk. The model reads the file directly when it needs more detail, and skips that cost when it doesn't. This works because once the model sees the structure of a result and a few representative rows or entries, it can infer the rest without needing the entire payload in context. The model just needs to know where the useful output lives and how to get it.
Search and progressive disclosure keep context lean
The coding harness can execute complex workflows with tools at scale, but preloading hundreds of enterprise skills and tools into the context window dilutes attention, decreases reliability, and inflates cost. So we built the harness on a combination of search and progressive disclosure instead.
The harness starts with a minimal set of core tools in the system instructions. This includes just two search tools: one for enterprise context and one for tools and skills. These core tools let the agent find every other resource it needs. When the agent finds a tool or skill through search, it doesn't see the full content right away. It just sees a lightweight name and description, then reads the full schema or complete set of references only when the task actually calls for it through progressive disclosure.
Search and progressive disclosure are both necessary because they solve different problems. Progressive disclosure lets an agent use a complex resource effectively by reading only the parts of a skill or schema relevant to the task at hand, rather than getting distracted by the rest. But progressive disclosure only helps once the agent knows which resource to use. Search points the agent to the right tool or skill, so when it does dive deeper, it can be confident it's looking in the right place.
Re-architecting the harness around a core set of search tools introduced its own challenges. Each search surfaces new tools and skills that the model needs to consider, which means the instruction set the model is reasoning over can grow across each turn. If that context were inserted into earlier turns, it would invalidate the prefix cache, the initial portion of a conversation whose attention states LLMs can reuse instead of recomputing. To avoid this, Glean appends search results to the end of the conversation. That lets the model act on newly surfaced tools and skills without invalidating the prefix cache, making responses faster and more cost-effective.
Why coding harnesses fit long-running enterprise work
The move to a coding harness reflects a bigger shift in enterprise AI. Work increasingly means orchestration and automation across dozens of SaaS systems, not just text-based conversation. Cross-system workflows require precise logic and state management, and code satisfies those requirements more directly than tool calls based on natural language.
Coding harnesses are also becoming the most effective model-agnostic option for agentic execution. Frontier models from every leading lab already excel at agentic coding, and open models are catching up fast. Because a wide range of models can drive Glean’s harness, improvements in LLM coding ability translate directly into better agent execution without requiring a redesign. Agent builders can swap models in and out freely as their needs and requirements change.
A coding harness doesn't just let agents call more tools. It lets them use tools, context, and skills with far greater efficiency and reliability, even at the scale of the 1000+ tools needed to automate an entire enterprise. Paired with a core set of high-precision search tools, Glean’s coding harness becomes the foundation for powerful work agents that complete advanced enterprise workflows with 24% fewer tokens.
Back to all stories
Have questions or want a demo?
We’re here to help! Click the button below and we’ll be in touch.
Get a Demo
Get The Resource
Get The Resource
Work AI for all.
Get a Demo
Work AI that works.
Get a demo
Ask AI for a summary about Glean
634 2nd Street
San Francisco, CA 94107
United States
Go to Glean's Twitter Account
Go to Glean's Linkedin Account
Go to Glean's Instagram Account
Go to Glean's Instagram Account
Language
English (United States)
Japanese (Japan)
French (France)
PRODUCT
Work AI Platform
Workplace Search
Assistant
Proactive Intelligence
Data Analysis and Research
Content Creation
Work Execution
Prompt Library
Agents
Agent Builder
Agent Orchestration
Agent Library
Agentic Engine
Connectors
Model Hub
Security
System of Context
SOLUTIONS
All Teams
Engineering
Sales
Marketing
Support
People
Retail
Financial Services
USE CASES
Enterprise AI
Enterprise Search Software
AI Agent Orchestration
Enterprise AI Software
AI Agent Builder
COMPARISONS
Glean vs other alternatives
Glean vs ChatGPT Enterprise
Glean vs Microsoft 365 Copilot
Glean vs Claude Enterprise
RESOURCES
Resources Center
Product Videos
Guides
Customer Stories
Blog
Events
Webinars
Developers
Help Center
Download Glean
Product Drops
AI Glossary
Gleaniverse Community
COMPANY
About
Careers
Newsroom
Referrals
Partners
Trust center
260 Sheridan Ave, Suite 300
Palo Alto, CA 94306, United States
Gartner®, Peer Insights™, Voice of the Customer for Insight Engines, Peer Contributors, 28 June 2024.
Gartner Peer Insights content consists of the opinions of individual end users based on their own experiences, and should not be construed as statements of fact, nor do they represent the views of Gartner or its affiliates.
Gartner does not endorse any vendor, product or service depicted in this content nor makes any warranties, expressed or implied, with respect to this content, about its accuracy or completeness, including any warranties of merchantability or fitness for a particular purpose.
GARTNER is a registered trademark and service mark of Gartner, Inc. and/or its affiliates in the U.S. and internationally, and PEER INSIGHTS and GARTNER PEER INSIGHTS CUSTOMERS’ CHOICE BADGE is a registered trademark of Gartner, Inc. and/or its affiliates and are used herein with permission. All rights reserved.
©
2026
, Glean Technologies, Inc.
Website Terms
Privacy
