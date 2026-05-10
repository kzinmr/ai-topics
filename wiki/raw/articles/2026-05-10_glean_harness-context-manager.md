---
title: "The harness as the context manager"
source: "Glean Blog"
url: "https://www.glean.com/blog/harness-context-manager"
scraped: "2026-05-10T01:20:35.772435+00:00"
lastmod: "None"
type: "sitemap"
---

# The harness as the context manager

**Source**: [https://www.glean.com/blog/harness-context-manager](https://www.glean.com/blog/harness-context-manager)

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
Last updated Apr 29, 2026.
The harness as the context manager
0
minutes read
Nikhil Mandava
Engineering
Ayushi Mrigen
Engineering
Chau Tran
Engineering
Abhilash Samantapudi
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
AI Summary by Glean
Agent performance improvements increasingly come from the harness rather than the model alone, because longer-running, multi-step enterprise tasks make context management the core engineering challenge and require moving beyond giant upfront prompts and static tool lists.
Glean’s harness evolves this by treating code as the main execution primitive: programmatic tool calling in sandboxes keeps workflow logic, intermediate state, and bulk tool use outside the prompt, while sub-agents parallelize bounded tasks in isolated context windows for more reliable and scalable reasoning.
To keep agents effective at enterprise scale, Glean combines compaction and search-first skill discovery: compaction preserves only load-bearing task state while offloading raw outputs, and indexed skill retrieval progressively reveals only the capabilities needed at execution time, reducing context noise and improving selection quality.
Harnesses, the execution logic that surrounds models, are producing gains in long-running agent performance across the industry. LangChain improved
Terminal-Bench
by +13.7 points through harness changes alone that held the model constant. Vercel cut
80% of its agent's tools
and saw higher reliability at 3.5x lower latency. In these cases, the performance delta came from the harness, not the model.
We are in a period of rapid harness iteration driven by a shift in what agents are expected to do. Teams are pushing agents into longer-running, multi-step work and finding that first-generation architectures degrade fast. The common pattern of a single system prompt (often 20K+ tokens of conditional instructions) with 20 to 40 tool schemas injected upfront does not hold up. At Glean, we reduced our own system prompt by 45%+ by moving instructions into skills that load progressively instead. The difference shows up fast on tasks like filling in a 200-question RFP, where each question requires independent multi-source research, and compiled answers need to be validated and written back into a spreadsheet.
There is a perception that harnesses are changing as models become more capable. That is not the only driver. Harnesses are being rebuilt because we are giving agents more work, which requires more context. Every additional tool call, skill invocation, search result, and execution output adds to the context window. This is a problem we know well at Glean. Our roots are in enterprise search, where the core challenge has always been narrowing a vast information space down to the precise context needed to get the job done accurately. Similarly, as the volume and variety of work flowing through an agent increases, context management becomes the central engineering problem. The harness is, at its core, a distributed context management system.
At Glean, perfecting our harness is an ongoing pursuit. Now on our third iteration, each rebuild reflects new shifts in model capabilities, technology, and how AI is used across the enterprise. This post covers four changes in harness design:
Programmatic tool calling (PTC) in sandboxes
moves workflow logic into sandboxed code, keeping intermediate state in variables and files rather than in the prompt.
Sub-agents
decompose a single agent loop into isolated execution contexts, each with its own context window.
Compaction
preserves the load-bearing conversation state while moving raw intermediate outputs into file systems.
Search-first discovery of skills
decouples tool and skill discovery from schema hydration, fetching full definitions only at execution time.
In this blog, we’ll walk through each of these changes and how our harness has evolved over time to better scale context.
Code as the main execution primitive
Code is becoming the main execution primitive for agents. As work gets more complex, agents need to iterate through result sets, branch on conditions, filter and join data, rank evidence, batch operations, and parallelize independent steps. Code expresses that logic more naturally than a series of conversational tool calls where the model re-derives its plan from chat history on every turn.
Glean uses PTC to move this workflow logic into a sandboxed execution environment. Tools are exposed as Python-callable functions, so the model writes a small program that retrieves, filters, branches, loops, writes to disk, and takes action in one execution rather than across dozens of conversational turns. 20 tool calls can happen inside one sandbox run, and the orchestrator sees only the summary and structured metadata that come back. Intermediate data stays in Python variables and files.
With PTC embedded into the right harness, we were able to realize the following gains:
Latency.
Independent operations can be batched and parallelized inside a single code run rather than serialized across LLM round-trips.
Reliability.
Loops, filters, joins, and conditional branching are more robust in code than in a fragile chain of chat turns where the model reconstructs its plan from conversation history on every step. This also makes it easier for the agent to recover from errors, as it has stack traces it can inspect.
Consistency.
Scripts can be saved as skills, making it easier to do the same sequence of tool calls for common tasks at both the enterprise and personal level.
Context efficiency at scale.
Only the summary or final outputs return to the orchestrator, not every intermediate artifact. This means that larger analyses, bulk operations, and long-running tasks that need to paginate, store, compute, and revisit state become feasible because the agent has program scope and a filesystem outside the context window.
Subagents as context isolation boundaries
Sub-agents are not new to Glean’s harness, but PTC expanded their scale and reliability. The orchestrator agent can write code to programmatically launch parallel subagents.
Sub-agents become especially powerful when the orchestrator agent needs to apply the same level of analysis across a large collection of independent items, such as researching hundreds of customers or analyzing thousands of support tickets. In these cases, each sub-agent can execute independently on its own task with its own context window and token budget, while the orchestrator agent supplies the shared instructions for how to perform the work through a prompt template or programmatic task definition. With sub-agents the depth of analysis improves as each one can focus its attention on the context and the job to be done without distraction.
This pattern lets the system scale out repeatable reasoning without overloading a single context window, and it echoes ideas from
Recursive Language Models
where higher-level agents decompose work and delegate bounded tasks to lower-level workers.
When it comes to multi-agent work, the orchestrator agent distributes tasks to sub-agents which work independently and in parallel with their own isolated context. As the sub-agents complete their work, they hand off the results back to the orchestrator which aggregates the response. All agents can make use of the Enterprise Graph, skills index, sandbox, and model hub to complete work.
Compaction strategies to preserve the working state
While subagents help distribute work across many independent tasks, keeping parallel lines of reasoning isolated and manageable, they do not address how context builds up over time within a single agent. In Glean, we saw about ~5% of queries hit context window limits.
To solve this, we designed a compaction approach that preserves the parts of conversation state that are load-bearing for continued execution: user intent, decisions made so far, approaches that failed, planned next steps, and recent high-signal tool outputs. Everything else is either summarized or moved out of the context window into the filesystem. The goal is a compressed but semantically complete representation of the task state that lets the agent pick up where it left off after many turns.
There are two technical layers to how this works in practice:
The first is
conversation compaction
. We condense the raw back and forth of earlier turns with what the user asked for, what the agent has tried, what worked, what did not, and what it plans to do next.
The second is
tool-output compaction
. Large tool outputs are written to files in the sandbox filesystem and reduced to summaries with file paths
Compaction and sub-agents reinforce each other. Sub-agents reduce how much irrelevant detail the orchestrator ever sees by keeping intermediate work inside isolated contexts. Compaction handles what remains in the orchestrator's own history, preserving task coherence across time. One manages context spatially, the other temporally.
Search-first discovery for skills
Skills are emerging as an open standard for packaging reusable expertise. There are benefits to this approach, including progressive disclosure where the agent preloads the skill's name and description, then fetches the full payload only when the task actually requires it.
We found that progressive disclosure alone, however, does not go far enough at enterprise scale. It is not feasible for an agent to browse hundreds of tools or skills as even one-line descriptions per item add up and create noise the agent has to reason through on requests where most of those capabilities are irrelevant. That’s why we introduce an index over all skills and only load relevant ones into context.
Discovery in Glean is a three-phased approach:
Search the index.
The model recognizes it needs a capability and queries the index. Our skill search is more powerful than semantic search alone, since we leverage enterprise graph signals to rank based on creator, usage, and more. The aim is to find the right skill even in scenarios where multiple individuals create and share similar skills.
See the short list & lightweight descriptions.
The index returns a short list of candidates with names, descriptions, and execution hints. This is the first time the model sees any detail about these capabilities. It can then select from this targeted list to complete its task.
Hydrate the full schema at execution time.
Only when the model commits to executing a specific skill does the full schema or
skill.md
file enter context.
With Glean, the agent never pays the context tax of browsing the full capability surface. Descriptions appear only for capabilities the model has actively searched for. Full schemas appear only for the one it is about to execute. Each layer of detail is disclosed at the moment the agent needs it. The agent makes better selections because it is reasoning over a targeted short list rather than scanning hundreds of entries, allowing the harness to scale to a large capability surface.
Harnesses distribute context management
Glean’s harness is getting better at scaling and managing context, because it's more distributed: programmatic tool calling allows for complex execution logic, sub-agents isolate context, compaction preserves task state while offloading context, and skill discovery keeps agents focused on the task at hand.
The harness never stops evolving. Each new generation of AI at work exposes the limits of what came before, and our harness evolves with it, expanding to meet the growing demands of agents and the context required for reliable results at enterprise scale. Want to bring a reliable context management system to your agents? Book a Glean
demo
today.
‍
Authors:
Nikhil Mandava
,
Ayushi Mrigen
,
Chau Tran
,
Abhi Samantapudi
,
Julie Mills
,
Matt Ding
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
