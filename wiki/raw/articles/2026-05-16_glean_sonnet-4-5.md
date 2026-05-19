---
title: "Claude Sonnet 4.5 optimizes tool execution to unlock 10% of queries that were previously out of reach"
source: "Glean Blog"
url: "https://www.glean.com/blog/sonnet-4-5"
scraped: "2026-05-16T06:00:21.273497+00:00"
lastmod: "None"
type: "sitemap"
---

# Claude Sonnet 4.5 optimizes tool execution to unlock 10% of queries that were previously out of reach

**Source**: [https://www.glean.com/blog/sonnet-4-5](https://www.glean.com/blog/sonnet-4-5)

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
Finance
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
Finance
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
Last updated May 15, 2026.
Claude Sonnet 4.5 optimizes tool execution to unlock 10% of queries that were previously out of reach
0
minutes read
Kunal Patil
Software Engineer
Nikhil Mandava
Engineering
Seema Jethani
Product Lead
Nilesh Dalvi
Software Engineer
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
Claude Sonnet 4.5, now supported in Glean, delivers significant improvements over its predecessor by efficiently solving 10% of previously unanswerable enterprise queries, thanks to optimized tool execution and fewer planning iterations.
The model demonstrates higher correctness, completeness, and better alignment with human feedback, while using parallel tool calls and adaptive planning more effectively—achieving stronger performance without increasing resource consumption.
Glean’s open platform enables enterprises to quickly access and evaluate Sonnet 4.5 alongside 15+ leading LLMs, empowering users to select the best model for their real-world workloads and make informed decisions based on transparent performance benchmarks.
Glean is an open platform that supports the latest open-source and commercial models, giving enterprises access to the most advanced LLMs. Glean provides the context these models need by tapping into 100+ data sources across the enterprise and building an Enterprise Graph that understands how your company works—the people, the relationships, the projects, the tasks, and the processes. As a result, we help enterprises get more done with AI—from debugging and writing to data analysis and more, all grounded in context.
Glean is committed to quickly supporting cutting-edge models, including Claude Sonnet 4.5, and giving users the ability to try them on real enterprise workloads. We are happy to support Sonnet 4.5 this week in our no-code agent builder, letting users pick the best model for the job from Sonnet 4.5 and 15+ models on a per-agent or per-agent-step basis.
At Glean, we evaluate models and our agentic engine on completeness, correctness, and alignment with human feedback. We then share those results so users can make informed decisions on which models to use. Our evaluations found that compared with Sonnet 4.0, Sonnet 4.5 delivers higher correctness and completeness and, more importantly, successfully tackles an additional 10% of queries with human feedback (downvoted queries), a class of queries that was out of reach for Sonnet 4.0. Sonnet 4.5 gets to the final answer with fewer iterations in planning—driving stronger performance more efficiently.
Sonnet 4.5 tackles queries that Sonnet 4.0 just couldn’t answer
Glean saw its biggest improvement with Sonnet 4.5 on alignment with human feedback, which measures how often newer models successfully resolve previously downvoted queries.
Alignment with human feedback is a moving target. We recently made a significant upgrade to
Glean’s Agentic Engine 2
, the engine that adaptively plans and iterates over enterprise context. This enabled us to solve a class of queries representing 20% of all downvote queries that were previously out of reach. With this new Engine, the bar for addressing human feedback rose substantially, making it harder for Sonnet 4.5 to show performance gains. With this context, we’re impressed with the 10% improvement jump in the newer Sonnet model.
Sonnet 4.5 is more efficient with improved tool calling and better use of adaptive planning
While Sonnet 4.5 made gains on correctness and completeness over Sonnet 4.0, the more notable win is that the model achieved these results efficiently. We track efficiency with two metrics:
Tool calling
: The number of times the agent uses external data or actions during problem solving.
‍
Adaptive planning cycles
: The number of iterations in which the agent revises and executes its plan based on intermediate results until the task is accomplished.
Tool calls (mean)
Parallel tool calls (mean)
Adaptive planning cycles (mean)
Claude Sonnet 4.5
1.61
1.34
2.19
Claude Sonnet 4.0
2.08
1.00
3.08
Not only is the model better at honing in on the right tools faster, it’s also more efficient using parallel tool calling without forceful prompting. The model can infer the right execution order for dependent steps and recognize when calls can be parallelized.
While we see adaptive planning being valuable for open‑ended or research questions, its overuse can increase latency and resource consumption. Sonnet 4.5 is better at parsing large result sets and committing to an answer when its confidence is high, enabling it to answer without running an extra confirmation step.
What’s impressive is that Sonnet 4.5 uses tool calling and adaptive planning more efficiently without degrading performance on completeness or correctness.
How Sonnet 4.5 optimizes tool calling
In the evaluation data, we see that Sonnet 4.5 parses the user’s query and figures out the operators to use, effectively applying the right filters and parameters for tools—resulting in more accurate results with fewer tool calls. It’s also better at pinpointing the tools that measurably advance the task—either by reducing uncertainty, ruling out possible execution paths, or producing the final result.
We see the improvements in tool calling and adaptive planning in this query:
With Sonnet 4.5, this query was answered with 3 parallelized searches rather than 3 sequential searches, saving 2 LLM calls and delivering lower latency.
Access Sonnet 4.5 and leading open-source and commercial models in the Glean model hub
Sonnet 4.5 delivers more accurate, more complete answers for enterprise AI than Sonnet 4.0—and uses enterprise tools more effectively to solve tougher questions with better efficiency. Sonnet 4.5 is coming this week to the Glean model hub alongside 15+ leading open-source and commercial models, so you can see how it works on your own enterprise agents.
If you’re not a Glean user and want to see Sonnet 4.5 at work, sign up for a free
demo
today.
‍
Authors:
Kunal Patil
,
Nikhil Mandava
,
Seema Jethani
,
Nilesh Dalvi
,
Julie Mills
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
Enterprise AI Software
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
