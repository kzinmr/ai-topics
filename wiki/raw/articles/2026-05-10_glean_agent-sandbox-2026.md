---
title: "Why agents need sandboxes, not larger context windows"
source: "Glean Blog"
url: "https://www.glean.com/blog/agent-sandbox-2026"
scraped: "2026-05-10T01:27:02.720420+00:00"
lastmod: "None"
type: "sitemap"
---

# Why agents need sandboxes, not larger context windows

**Source**: [https://www.glean.com/blog/agent-sandbox-2026](https://www.glean.com/blog/agent-sandbox-2026)

Product
WORK AI PLATFORM
Platform Overview
Glean Assistant
Your personal AI assistant
Data Analysis
Canvas
Deep Research
Glean Agents
Build and manage AI agents
Agent Builder
Agent Governance
Agent Orchestration
Agent Library
Glean Search
The foundation of enterprise AI
Enterprise Graph
Personal Graph
System of context
Hybrid Search
Connectors & Actions
Connect to all your apps
Model Hub
Get access to the latest models
APIs
Build generative AI experiences
Security
Safely scale AI at work
Agentic Engine
Plan & adapt over company context
GLEAN WHERE YOU WORK
Glean in Slack
Glean in Microsoft Teams
Glean in Zoom
Glean in Service Cloud
Glean in ServiceNow
Glean in Zendesk
Glean in GitHub
Glean in Miro
Browser Extension
Sign in
Customers
Solutions
DEPARTMENTS
All Teams
Engineering
Customer Service
Sales
Marketing
B2B Marketing
B2C Marketing
People
IT
INDUSTRIES
Retail
Financial Services
Banking
PE/VC
Asset management
Insurance
Higher Education
Healthcare
Government
Industrials
Energy & Utilities
Manufacturing
Supply Chain
Sign in
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
Sign in
The AI Transformation 100
Explore 100 real-world moves organizations are making to transform themselves with AI.
Download the report
About
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
About
Sign in
Back
WORK AI PLATFORM
Platform Overview
Glean Assistant
Your personal AI assistant
Data Analysis
Canvas
Deep Research
Glean Agents
Build and manage AI agents
Agent Builder
Agent Governance
Agent Orchestration
Agent Library
Glean Search
The foundation of enterprise AI
Enterprise Graph
Personal Graph
System of context
Hybrid Search
Connectors & Actions
Connect to all your apps
Model Hub
Get access to the latest models
APIs
Build generative AI experiences
Security
Safely scale AI at work
Agentic Engine
Plan & adapt over company context
GLEAN WHERE YOU WORK
Glean in Slack
Glean in Microsoft Teams
Glean in Zoom
Glean in Service Cloud
Glean in ServiceNow
Glean in Zendesk
Glean in GitHub
Glean in Miro
Browser Extension
Sign in
DEPARTMENTS
All Teams
Engineering
Customer Service
Sales
Marketing
B2B Marketing
B2C Marketing
People
IT
INDUSTRIES
Retail
Financial Services
Banking
PE/VC
Asset management
Insurance
Higher Education
Healthcare
Government
Industrials
Energy & Utilities
Manufacturing
Supply Chain
Sign in
Joel McKelvey
Head of Solutions, Glean
Abdullah Haydar
Director of Engineering, LinkedIn
Webinar
AI Powered Engineering
Expert insights and actionable strategies for accelerating developer productivity.
Watch now
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
Sign in
The AI Transformation 100
Explore 100 real-world moves organizations are making to transform themselves with AI.
Download the report
Last updated Apr 22, 2026.
Why agents need sandboxes, not larger context windows
0
minutes read
Ayushi Mrigen
Engineering
Abhilash Samantapudi
Product Manager
Matt Ding
Technical Product Marketing Manager
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
AI Summary by Glean
Agents hit a wall with context windows
— As tasks grow more complex, cramming all enterprise data into an LLM's context window forces costly tradeoffs like aggressive summarization and dropped details. Even larger context windows don't solve this, since model attention is brittle and varies across updates.
Sandboxes act as persistent short-term memory
— By giving agents a virtual environment with a file system, command line, and Python runtime, data becomes iterable and on-demand rather than all-at-once. This lets agents analyze massive datasets — combining structured CRM data with unstructured Gong calls, emails, and docs — far beyond what context windows allow.
Security and existing investments carry forward
— Each sandbox runs in an isolated, VPC-scoped environment inheriting Glean's permissions and governance controls. Earlier engineering work on retrieval, ranking, and classification still powers the sandbox, while the fragile token-budget management of context windows is no longer needed.
Agents are now on the precipice of taking on long‑running, end‑to‑end tasks. They can resolve support tickets, write code, push PRs, and even complete entire sales account plans. But as agents tackle more complex tasks, they’re increasingly constrained by the model’s context window. As your data crowds the context window, agents are forced to make tradeoffs, capping results, summarizing aggressively, or dropping details, which artificially limits how much real work they can take on. Even with models that support large context windows, we still see agents lose attention, and the cost of long-context tasks remains high.
What we’ve found is that if you give an agent a sandbox, a virtual computer equipped with a file system, command line, code runtime, and tool index, it can use that environment to expand its effective short‑term memory and process far more data than LLM context windows allow. Agents can read from the file systems directly, making the data fully iterable so the agent can pull what they need at each phase of execution, rather than trying to fit everything into the context window.
In the enterprise, we’re seeing this unlock new analytical use cases, including aggregating large‑scale datasets that were previously out of reach for agents. In this blog, we’ll walk you through a real use case this opens up.
The agent sandbox is a component of the agentic engine, which plans, executes, and adapts over your enterprise context. When the information an agent needs exceeds the model’s context window, it spins up a sandbox to act as short‑term memory.
Complete analysis of all your structured and unstructured data
Many routine tasks for sales leaders sound simple:
"Review all my Q4 opportunities to analyze pipeline health."
In reality, this requires pulling together thousands of data points from systems of record and productivity apps to get the full picture.
As the agent runs and retrieves the content needed for the pipeline report, it nears the limit of the model’s context window and spins up an agent sandbox.
The agent sandbox works alongside Glean’s enterprise context, bringing in structured opportunity data from Salesforce alongside unstructured Gong call transcripts, Teams messages, Outlook emails, Word documents, Powerpoint presentations, and more.
Glean makes it possible for the agent to make sense of this data by mapping it in the
Enterprise Graph
, which links customers, account managers, and activity across all your business apps. That way, only relevant, high‑quality data lands in the sandbox, and is used at each stage of agent execution, preventing the agent from context overload and interference. The sandbox lets agents extract maximum value from large amounts of context, but only when it’s filled with the right context to begin with.
The agent sandbox includes a Python runtime for analytics and data processing. As the agent runs, it can use code execution to assess pipeline risk, run sensitivity analyses, detect outliers, and generate a ranked list of opportunities with predicted win probabilities.
The real breakthrough is that this analysis isn’t limited to the cleaned, structured data that shows up in CRM reports: the agent can pull in and analyze unstructured data from all your customer conversations, conversations that used to be out of reach to complete the analysis. Now your forecast reflects the actual story happening with customers, not just the narrow slice captured in structured data fields.
Lessons from engineering short-term memory management
Before we built sandboxes, LLM context windows were the only short-term memory Glean Agents had available. Even as context windows expanded with each model release, agents still needed efficient and structured short-term context management to achieve performance.
AT Glean, we designed a classification hierarchy for data flowing into the context window. This allowed agents to distinguish between user inputs, system instructions, and tool outputs across different parts of a conversation. These heuristics helped agents decide what content to trim while preserving critical facts and instructions. Sandbox uses this same hierarchy for a more powerful approach. Instead of discarding information, an agent keeps data it immediately needs in the LLM context window and stores extra data in the filesystem for on-demand access later. With the sandbox, memory management shifted from deletion to persistence.
We also built selector tools that let agents load specific snippets of large documents into memory based on company-specific semantic similarity. This allowed agents to understand long documents quickly without the cost of reading everything upfront. The sandbox filesystem powers a similar strategy with greater capacity. With sandboxes, we can use the selector tools to quickly hone in on the right snippets but now pair it with greedy materialization, analyzing the full document, revisit specific sections, or write code to analyze them.
We exposed advanced filters in Glean search tools, so agents could make better, faster use of the data, allowing them to specify date ranges, document types, and ranking signals like semantic similarity and popularity. These same advanced filters now serve to make the sandbox more efficient.
While our early systems were effective, they were brittle. A framework that worked for GPT-5 might fall short for Claude Sonnet 4.5. Even minor updates (e.g., GPT-5.1 to 5.2) caused large variations in performance. This is because memory in the context window relies on model attention, which changes every update. As a result, the LLM’s interpretation of summaries, instructions, and task states varies across versions, leading to quality drift even if the agent system remains unchanged. Maintaining quality across models meant continuously tuning memory.
This is why agents don’t need larger context windows, the problem of brittle short-term memory would still remain. What they need instead are sandboxes.
This brittleness was the hidden cost of treating the context window as the only form of memory. Sandboxes let us move that state out of the fragile context window and into a stable environment the agent can reliably work in. Many of our earlier investments in classification, retrieval, and ranking continue to be relevant today. At the same time, much of the work spent on aggressive truncation, compression, and token-budget micromanagement went away with sandboxes.
How we made the agent sandbox secure
Security is built into the agent sandbox from the ground up. Every sandbox runs in an isolated environment inside your own VPC, with strict resource limits, scoped file systems, and session-level isolation. Data, code, and intermediate artifacts from one session never leak into another. Sandbox network access is disabled by default and will be fully configurable in the future, minimizing exposure while giving tight control when external connectivity is needed. Because tools and LLM calls are still routed through the same orchestration paths as before, sandbox inherits all of Glean’s existing guardrails, permissions, and governance controls.
Models and context work better together with the agent sandbox
Agent sandboxes don’t replace better models or richer context. They make both more useful together. When you give agents a sandbox, they stop fighting the context window and start taking on more work than before.
For a work AI platform where capable agents meet complete company context, sign up for a demo of Glean today!
Availability: Glean agent sandboxes are coming soon.
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
Language
English (United States)
Japanese (Japan)
PRODUCT
Work AI Platform
Workplace Search
Assistant
Data Analysis
Deep Research
Canvas
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
