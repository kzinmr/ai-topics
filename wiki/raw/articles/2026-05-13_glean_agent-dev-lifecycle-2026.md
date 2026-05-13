---
title: "Introducing the Agent Development Lifecycle (ADLC)"
source: "Glean Blog"
url: "https://www.glean.com/blog/agent-dev-lifecycle-2026"
scraped: "2026-05-13T06:00:21.561212+00:00"
lastmod: "None"
type: "sitemap"
---

# Introducing the Agent Development Lifecycle (ADLC)

**Source**: [https://www.glean.com/blog/agent-dev-lifecycle-2026](https://www.glean.com/blog/agent-dev-lifecycle-2026)

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
Last updated May 12, 2026.
Enable every agent to drive ROI with a robust agent development lifecycle
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
To maximize
ROI
and prevent AI sprawl, CIOs must transition from siloed AI pilots to a structured
Agent Development Lifecycle (ADLC)
that mirrors software engineering standards.
The lifecycle provides a repeatable blueprint across seven distinct stages—Opportunity, Design, Performance, Context, Develop, Launch, and Monitor & Improve—ensuring every agent is tied to clear
business value
and
KPIs
.
Glean is integrating the ADLC directly into its
Work AI platform
with major new features, including Auto-mode agents, deep debug and trace views, modular sub-agents, and a secure agent sandbox to handle massive data processing safely.
‍
Most CIOs have already integrated agents into productivity suites, are running in individual business units, and are enabling teams to stitch together customized agents. Yet, when asked about the total ROI of these initiatives, most CIOs are still figuring out the numbers. Many teams are also building siloed, brittle agents with no coherent strategy stringing them together, making them difficult to govern and resulting in AI sprawl.
Instead, CIOs should treat agents like software. Like other software systems, agents depend on context, tools, permissions, workflows, runtime safeguards, and ongoing oversight. To drive enterprise value, agents should be well-designed, tested, rolled out carefully, monitored in production, and improved over time in the same way that engineering teams deliver other types of enterprise-grade software.
Enterprises that implement agents using a model that mirrors the software development lifecycle gain three things they do not get from ad‑hoc AI pilots alone:
A shared way to talk about agents across functions.
A repeatable pattern that defines ROI for each agent and for the portfolio as a whole.
A clear view of risk and ownership at every step.
ADLC has been a critical factor in helping our customers like
Zillow
,
Ericsson
, and
Motive
scale agent adoption, with millions of agent runs per week. ADLC has also enabled us at Glean to create meaningful results for our own teams: a single agent deployed within Glean’s engineering team reclaimed 17,000+ engineering hours per year and more than $1.7M in ROI.
Based on these results, it’s clear that the Agent Development Lifecycle is not another framework for experimenting with agents, but rather a disciplined way to build agents that generate clear business value.
And now, we are building the ADLC directly into Glean’s Work AI platform.
Introducing the Agent Development Lifecycle
When you talk to teams whose agent projects have stalled, you rarely hear “the model wasn’t smart enough.” You hear statements like the agent didn’t have the right context, the integrations are brittle and continually have to be rebuilt across agents, or no one knows what success looks like post-launch.
Each of these pain points speaks to the lack of an operating model. Every function and vendor ends up reinventing a mini software development lifecycle for agents, with its own language, metrics, and standards. That makes it very hard to compare agents, govern them, or decide which ones deserve more investment.
The Enterprise ADLC provides a single lifecycle that every agent builder can follow. For a simple, low-risk workflow, teams may move through these steps in minutes or hours; for a business-critical agent, they may take days or even a few weeks to execute. But, the discipline to follow the ADLC matters either way. Let’s dig in.
Opportunity
– Start by spelling out the business problem the agent is intended to solve. Use plain language: who is affected today, how work happens without the agent, and what tangible change you expect if the agent succeeds. This anchors everything that follows to outcomes the business already cares about, not just an interesting demo.
Design
– Describe what the agent is actually responsible for. Define the unit of work (a ticket, an incident, a call, a workflow), when it should run, what information it needs, and what it should produce every time. Be explicit about what’s in scope, what’s out of scope, and which assumptions need to be tested early.
Performance
– Turn that intent into a small, concrete set of success metrics: the business KPIs you expect to move, plus agent‑centric quality and safety signals. Agree on baselines and target ranges, and decide up front what would cause you to expand, pause, or roll back the agent.
Context
– Identify the minimum set of permission‑aware data sources, tools, examples, and feedback signals the agent needs to do its job and to be evaluated fairly. This includes which systems it can read from, which actions it is allowed to take, and what telemetry you will use to understand how it’s performing.
Develop
– Turn the design into a reliable agent. Choose the right execution model (for example, a structured workflow versus more flexible auto‑mode), then test against golden examples, run it in parallel with the existing process, and pilot with design partners until the agent behaves predictably—not just on a hand‑picked demo set.
Launch
– Treat rollout as a change‑management exercise, not a switch flip. Decide who will see the agent first, how it will show up in their workflow, what training and communication they need, and which guardrails, SLOs, and kill switches must be in place before you broaden access.
Monitor & Improve
– Operate the agent like any other critical system. Use dashboards, alerts, and runbooks to track impact and quality over time, handle incidents, and feed real‑world signals—user feedback, overrides, drift in key metrics—back into earlier stages of the lifecycle so the agent keeps improving.
This step is not a one-time stage but is actually an ongoing process as agents are maintained, monitored, upgraded, and eventually sunset as business needs change.
New capabilities for Glean agents unlock the ADLC
We’ve focused our product investments around the major stages of the ADLC: designing the right agents, activating your enterprise context with full control, rolling out agents with confidence, and operating them as a portfolio.
Here’s what’s new:
Auto‑mode agents are now generally available:
Describe what you want an agent to accomplish, and auto-mode agents handle the rest by planning, reasoning, and acting across your enterprise graph, within the guardrails and managed actions your organization controls. No predefined workflow. No manual configuration. It's a fundamentally faster path from intent to something you can test and iterate on immediately. This is the most significant release we've shipped for agent builders to date.
Debug and trace views:
Agents fail in ways that aren't always obvious. When something goes wrong mid-run, you need to see exactly what happened, not just the final output. The debug view surfaces every step: the inputs, the tool calls, and the decisions that produced each outcome. That kind of visibility closes the loop between "something went wrong" and "here's what to change."
Sub-agents:
Rather than build one monolithic agent to handle every aspect of a process, teams can now build reusable sub-agents that can be invoked when needed. This allows agents to operate like how the best engineering teams build systems: modular, testable, and governed at every layer.
Agent sandbox:
Agent sandbox is now available for agents. This powerful feature gives each autonomous agent a secure, private runtime environment: a file system for organizing and retrieving intermediate outputs across a long-running task, like analyzing large batches of Gong calls, and a code interpreter for computation that goes beyond what language model reasoning alone can handle reliably.
To learn more about agent sandbox,
check out this blog post
.
Agent library:
As the number of agents in your organization grows, discoverability becomes a real problem. The agent library gives administrators control over which agents are visible to whom, how they're described, and how they're categorized. This ensures the right agents reach the right people, and the catalog doesn't become noise. Verification and curation controls mean that what's surfaced to employees reflects a deliberate decision, not just whatever got published most recently.
Agent access policies:
Now, admins can declare organization-wide guardrails that all agents have to follow, like preventing interns from writing to any system of record using agents. This provides enterprises with peace of mind and ensures that all of your agents are under control.
Agent insights:
New insights surfaces give you a view into which agents are trending, which are rarely used, where users are giving negative feedback, and how behavior is changing over time. Feedback mechanisms inside agents let builders collect structured signals to drive iteration.
The next wave of enterprise AI won’t be won by the teams with the most agent demos. It will be won by the teams that can turn promising ideas into repeatable, measurable outcomes which is what the Agent Development Lifecycle is designed to provide. It gives teams a practical model for deciding what to build, grounding agents in the right context, and improving them based on real-world performance.
Our new Agent features reflect a broader shift in how enterprises need to approach agents: as systems that must be designed, governed, and improved over time.
Because in the enterprise, success won’t come from shipping the most agents. It will come from building agents that are trustworthy, governable, and genuinely useful—the kind organizations can improve over time and scale with confidence.
‍
Ready to go inside the ADLC?
We have captured these ideas—and many detailed examples—in our new eBook,
The CIO’s Guide to Enterprise AI Agents
, which introduces the ADLC, walks through concrete agent examples across Support, Sales, and Engineering, and shows how to measure ROI in a way your CFO will trust.
{{richtext-banner-component}}
Back to all stories
Have questions or want a demo?
We’re here to help! Click the button below and we’ll be in touch.
Get a Demo
The CIO’s guide to enterprise AI agents
Discover how CIOs can turn AI agents into real ROI. Learn the Enterprise Agent Development Lifecycle to build, measure, and scale high-value AI across your business.
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
