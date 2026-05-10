---
title: "Glean's open agent platform: because while not all agents will be built on Glean, all agents should be connected to enterprise data"
source: "Glean Blog"
url: "https://www.glean.com/blog/open-agent-platform"
scraped: "2026-05-10T01:27:51.355562+00:00"
lastmod: "None"
type: "sitemap"
---

# Glean's open agent platform: because while not all agents will be built on Glean, all agents should be connected to enterprise data

**Source**: [https://www.glean.com/blog/open-agent-platform](https://www.glean.com/blog/open-agent-platform)

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
Last updated Jan 27, 2026.
Glean's open agent platform: because while not all agents will be built on Glean, all agents should be connected to enterprise data
0
minutes read
Arvind Jain
CEO
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
Glean is an open and extensible Work AI platform that allows enterprises to bring their own cloud, LLM, security provider, and third-party agents, supporting both first and third-party integrations.
Open standards of communication, such as MCP and LangChain’s Agent Protocol, enable agents to connect to various tools seamlessly, fostering collaboration and improving efficiency.
By indexing enterprise data once and ensuring permissions-aware access across tools, Glean enhances productivity, security, and knowledge sharing within organizations.
Glean is an open and extensible Work AI platform where enterprises bring their own cloud, LLM, security provider, and — available now — third-party agents. While Glean is a powerful platform for creating and orchestrating agents, it’s understandable that customers working in even the largest of Glean environments won’t be building all their agents in Glean. We firmly believe enterprises should be given a choice when building their agent tech stacks. We also believe that other agent frameworks benefit from Glean by gaining access to indexed enterprise data - data that’s indexed and secured only once -  and enabling agents built anywhere to be grounded in relevant, personalized context.
Glean flourishes when operating in a larger ecosystem, and fails when isolated in a walled garden. That’s why today I’m sharing Glean’s support for the latest universal standards of communication and open agent frameworks, including
Anthropic’s Model Context Protocol
(MCP),
LangChain
, LangGraph,
Nvidia NIM
, OpenAI Agents SDK (via MCP), and many more to come in the future.
Glean began as an enterprise search solution breaking down knowledge silos across the organization and now we’re seeing that mission extending to breaking down application silos. We see a future where agents overcome the barriers that have traditionally made automating knowledge work across SaaS applications a manual, time-consuming, and brittle process.
Open standards of agent communication
Agents act autonomously to get work done, reasoning through complex tasks and pulling in the right tools and workflows. While LLMs excel at reasoning, they lack enterprise knowledge, processes, and the ability to take action. This is where agent platforms step in, orchestrating and securing agentic work to align with user goals.
Enterprise work is scattered across disconnected SaaS tools, often requiring workers to switch between multiple applications for a single task. Traditional automation has been rigid and expensive, reserved for critical processes. Agents change this by enabling dynamic, context-aware automation for individuals and teams. Yet, the agent and SaaS landscape remains fragmented, making it hard for agents to access data in other applications, call other tools and accomplish their work.
Rather than further fragment the industry by creating our own bespoke APIs and conventions, the value of agents could be realized faster with a common communication framework. It would also avoid customers being locked into a single system, unable to take advantage of a future filled with ever more innovative models and easy-to-use tooling. I firmly believe we’re still in the early innings of AI and that everyone should have the freedom and flexibility to adapt their approach, without coming face-to-face with a heavy rearchitecture.
This is why I’m personally enthused by the introduction of universal communication protocols like Anthropic’s Model Context Protocol (MCP), LangChain’s Agent Protocol, and Cisco, LangChain, and Galileo’s
AGNTCY
. These aim to provide an open standard for AI agents to connect to various tools and agents without bespoke integrations. When every agent speaks the same language, it’s easy for them to collaborate and uplevel work in the enterprise.
While Glean seeks to make it easy for everyone to build agents in the enterprise, there is a diversity of preferences filled by open-source agent framework alternatives. As an open platform committed to meeting those preferences, we offer support for LangChain and LangGraph. If you do choose to build on Glean, we’ll deliver an enterprise-wide agent experience that empowers everyone to build and deploy agents. Our platform supports scalable orchestration across both first and third-party agents, all anchored in your enterprise data and safeguarded by strict permissions enforcement.
The Glean developer platform with support for MCP, LangChain, and LangGraph. Some capabilities, including Agent and Connector SDKs, are coming soon.
MCP use cases for Glean
Prototyping Glean support for new open agent frameworks like MCP provided us with valuable learnings on how they’re best utilized in the ecosystem:
Glean Agents calling external tools
MCP provides a standardized way to connect agents to different data sources and tools based on the client-server architecture. The framework establishes communication between:
Host: Agents that initiate connectors
Clients: Connectors
Servers: Services that provide resources (context), prompts (templated messages), and tools (functions to execute)
With Glean operating as the host, it can connect out to any number of enterprise tools, as long as they have MCP servers in place. This enables Glean to expand its support to a number of new actions, with little to no engineering effort. Let’s look at an example of a customer who wants Glean to resolve tickets through its homegrown Support Hub:
While this is a straightforward example involving the retrieval and updating of a support ticket, in the future, steps within the agentic reasoning engine could be delegated to various other systems, orchestrated by Glean. You could also imagine that Glean, through conversations with other agents, could actually spawn another agent’s work. That’s because protocols are being designed for bidirectional communication, leveraging the dynamic nature of agents to get work done without needing to wait for explicit triggers. It’s pretty neat stuff.
External tools calling Glean Agents
We can also use Glean in another agent environment, say within the popular AI IDE Cursor. In this example, engineers never have to leave their IDE to gather full enterprise context including documentation, communication, and their code base from Glean.
While
Glean in GitHub
offers a similar experience, with added support for automated PR descriptions and code reviews, we had not yet built Cursor or Codeium integrations. With MCP, we don’t have to.
We see a future where Glean Agents work in concert with both tools and other agents. In some scenarios, like a developer environment where engineers spend their day, it makes sense for Glean’s strengths to be tapped in that environment. In other scenarios, you may turn to Glean Agents for its secure data access, permissions enforcement, and orchestration capabilities with third party agents. The cooperation across boundaries is now becoming a reality.
What comes next
New protocols and developer frameworks for building agents have reinforced the need for orchestration across both first-party and third-party agents. They’ve also underscored the value of a horizontal AI platform like Glean in the enterprise.
Our customers want to index their data just once — intelligently bringing context into agents rather than duplicating efforts across multiple solutions. Customers also want to secure, govern, and observe their agents in one go. Glean is designed to help users do just that — guaranteeing permissions awareness, access authentication, and enterprise data protection.
There’s value in the AI ecosystem - with its developer-friendly frameworks and standardized communication protocols - as well as in a unified platform that secures and indexes your data. Glean delivers both.
MCP documentation and repo
available now.
LangChain documentation and repo
available now.
Nvidia NIM documentation and repo
available now.
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
