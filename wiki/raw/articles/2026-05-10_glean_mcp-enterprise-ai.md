---
title: "Is MCP dead? When to use MCP for enterprise AI"
source: "Glean Blog"
url: "https://www.glean.com/blog/mcp-enterprise-ai"
scraped: "2026-05-10T01:20:53.951669+00:00"
lastmod: "None"
type: "sitemap"
---

# Is MCP dead? When to use MCP for enterprise AI

**Source**: [https://www.glean.com/blog/mcp-enterprise-ai](https://www.glean.com/blog/mcp-enterprise-ai)

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
Last updated Mar 27, 2026.
Is MCP dead? When to use MCP for enterprise AI
0
minutes read
Daniel Martinho
Technical Marketing Engineer
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
MCP is not universally the right abstraction: for local, single-user workflows, direct CLIs, small wrappers, and ad hoc integrations are often simpler, cheaper, and more practical than wrapping everything in MCP.
The real dividing line is not “MCP vs. no MCP,” but local laptop use versus enterprise-scale AI operations, where remote HTTP MCP becomes shared infrastructure for identity, permissions, policy, observability, and reuse across many tools and hosts.
At company scale, MCP adds value by centralizing auth and secrets, standardizing prompts/resources as reusable skills and docs, enabling org-wide telemetry, and supporting “integrate once, use everywhere” deployment across IDEs, chat apps, internal assistants, and other agent surfaces.
Last week, Charles Chen published “
MCP is Dead; Long Live MCP!
,” arguing that much of the backlash against the Model Context Protocol (MCP) is aimed at the wrong target, and often blurs the line between where MCP is overkill and where it solves real problems.
For a lot of local, single-user workflows, the argument is fair. If you’re building on your own machine, working with a small set of tools, and controlling the full environment yourself, MCP can add structure you don’t need.
But, the problem is different at the company scale. You are not just trying to help one model call one tool on one laptop. You are trying to  roll out AI safely and consistently across an entire organization. When you zoom out to what it takes to run AI as a governed, observable service for thousands of people — that’s where MCP starts to matter.
The useful question isn’t whether or not MCP is dead. It’s
when does MCP add unnecessary complexity, and when is it doing real work for you?
Where the article is right
Charles’ post gets several things right, especially for individual builders:
‍
For solo developers, CLIs are often the better tool.
If the model already “knows” tools like curl, jq, git, psql, or aws from pre‑training, you don’t need extra schemas or documentation to get value. In many cases, the model can use those tools directly, which is cheaper in tokens and simpler to set up.
‍
Wrapping every REST endpoint in MCP is overkill.
If all you’re doing is calling a couple of bespoke APIs from your own agent, hand‑rolled wrappers or small CLIs can be perfectly fine. MCP doesn’t automatically make those calls better.
‍
MCP over stdio is usually the wrong abstraction for local tools.
For a local agent and a local tool, stdio‑based MCP can just add structure without adding much value. A thin CLI may be the more direct option.
‍
The hype cycle around “MCP for everything” was real.
For a while, MCP was treated like the answer to every integration problem, without being clear about when it’s actually the right fit versus when it just adds unnecessary complexity.
If all you ever do is run a single agent on your own machine, talking to a few APIs you control, it’s hard to argue with those critiques.
But that’s not what most enterprises are trying to do.
The distinction that actually matters
The original piece draws out two distinctions that matter a lot, especially from an enterprise point of view:
Local stdio
vs.
remote HTTP MCP
A single user’s laptop
vs.
an entire company’s AI estate
On your laptop, you control everything:
You own the API keys.
You’re the only user.
You’re comfortable debugging issues directly to see what went wrong.
You don’t need a permissions model or an audit log for who ran what.
At a company level, the questions change:
Who is allowed to call which tool, on whose behalf, and under what identity?
How do we make the same capabilities available across multiple AI surfaces, like IDEs, chatbots, agents, without rebuilding integrations each time?
How do we see which tools are actually being used, which are failing, and where agents are getting stuck?
How do we keep prompts, skills, and docs up to date across all those surfaces?
Those aren’t CLI design questions. They’re platform questions.
That’s where
remote MCP servers
stop looking like simple “API wrappers” and start looking like shared infrastructure: a common layer for tools, identity, policy, and distribution across the enterprise.
If you want a deeper look at how we’ve implemented that infrastructure in practice, we go into more detail in our post “
Glean’s MCP servers bring full company context to where your AI runs
”.
What enterprises actually need from this layer
If you strip away protocol details and focus on outcomes, most enterprises want the same four things from their “AI-to-tools” layer:
1. Centralized, per‑user auth and secrets management
In a 10,000‑person company with five AI tools in play, “just give the agent an API key” doesn’t scale. You don’t want every developer (or every agent host) holding long‑lived API keys to Jira, Salesforce, Slack, and internal services. You want:
One login (OAuth or SSO) to the company’s “tool gateway.”
Short‑lived tokens issued per user.
The ability to revoke access centrally when someone leaves or changes roles.
A remote MCP server naturally fits into this role: the server holds the secrets; users and hosts authenticate to the server; the server fans out to underlying APIs.
From Glean’s perspective, this is exactly why we paired remote MCP servers with centralized OAuth and Glean Protect — so customers can turn tools on and off in one place and have permissions enforced end‑to‑end.
2. Org‑wide telemetry and observability
When you have many teams, hosts, and tools, you need to answer questions like:
Which tools are actually moving the needle?
Which tools are failing or timing out?
Which teams are over‑ or under‑using certain actions?
With a centralized server, you can emit standard traces and metrics, such as OpenTelemetry, and get a single, consistent view of how tools are being used across the org. That view becomes even more important as agents start to take autonomous actions on top of your index and knowledge graph, not just answer questions.
3. Standardized prompts/skills and docs across surfaces
The original article makes an important observation:
MCP prompts are essentially server‑delivered skills, and MCP resources are server‑delivered docs.
That gives you a way to:
Publish a single “code review” or “incident triage” skill once and have it show up consistently in many tools.
Keep docs in sync across teams and repos, without copying Markdown into every project.
Inject dynamic context, like the latest status, pricing, or policy updates, into prompts and docs at request time.
This is the same idea behind
Glean skills
. It’s a way to package expertise into reusable skills that agents can invoke anywhere they run. MCP gives you a neutral transport layer for those skills and docs, so they aren’t trapped inside a single app.
4. One integration surface for many hosts
Modern enterprises don’t live in a single UI. They have:
IDEs like Cursor, VS Code, Windsurf
AI chat apps like Claude, ChatGPT
Internal assistants and agent builders
Vertical tools with embedded agents
Without a protocol, every pairing becomes a bespoke integration. With MCP, you get closer to “
integrate once, use everywhere
”: define tools in one place, connect them to many hosts, and keep your Enterprise Graph and policy logic behind a single surface.
None of this is about saving a few tokens in your context window. It’s about running AI as a governed, observable platform.
When you probably
don’t
need MCP
It’s worth being explicit about cases where we wouldn’t reach for MCP first:
You’re building a single personal workflow between an LLM and one or two APIs you own.
All the logic lives on your laptop or in a single service you control end‑to‑end.
You don’t need shared auth, telemetry, or multi‑tenant separation.
You’re happy to document usage in a README or AGENTS.md and call it a day.
In those situations, a CLI or minimal SDK wrapper is often exactly the right fit. You get faster iteration with less overhead, and you can always move “up” to MCP later if your workflows outgrow it.
When MCP adds real value
By contrast, MCP starts to earn its keep in patterns like these:
Any host, same tools.
You want Cursor, Claude, ChatGPT, and your internal assistant to all be able to:
Search the same enterprise graph.
Use the same tools to file a ticket or update a record.
Respect the same permissions and audit rules.
A shared MCP server gives you one place to define those tools and one place to enforce policy, while each host just speaks the same protocol.
Admin‑approved, user‑friendly tools.
Security and IT want to:
Approve which MCP servers and tools are visible.
Configure OAuth, redirect URIs, and host allow‑lists.
See usage and errors without having to trace issues across disconnected systems and custom scripts.
That’s much easier when you have a first‑class concept of MCP servers and tools in an admin console, backed by a central server layer, instead of a sprawl of one‑off CLIs and scripts.
Company‑wide skills and docs.
You want:
SREs, PMs, and engineers to see the
same
incident runbooks and triage prompts, no matter which agent surface they use.
Those prompts and docs to stay current, including dynamic context like current status or version info).
Visibility into which skills and docs are actually being used.
MCP prompts and resources, delivered from a central server, are designed to do exactly that.
Agents that outlive one environment.
As soon as you want agents that:
Run in CI/CD or GitHub Actions
Trigger from ticketing systems or alerts
Show up inside SaaS apps you don’t control
…you’re by definition in
remote, multi‑tenant, audited, permissioned
territory. That’s where MCP over HTTP, with the right auth and logging, starts to look a lot less like overhead and more like the right approach.
We’ve seen a similar pattern play out with indexing vs. federated search: protocols like MCP and federated connectors are great for interoperability, but the real leverage comes when they’re sitting on top of a strong index and knowledge graph that can actually deliver relevant, permission‑aware context to those agents.
Moving beyond the hype cycle
Charles is right to call out the influencer‑driven hype cycle around MCP. Six months ago, it felt like everyone wanted to position themselves as “MCP‑compatible”. Now, the pendulum has swung the other way, and the conversation often centers on why a CLI is simpler.
Underneath that shift, the architectural story is fairly simple. On a single machine, direct CLIs and ad‑hoc wrappers are often the most pragmatic tool.
At company scale, teams eventually need:
A standard contract between AI hosts and tools
A central place to manage auth, telemetry, and policy
A shared way to deliver skills and docs across many surfaces
MCP isn’t the only way to get there. A company could build its own protocol, stand up a custom gateway, and wire every host into it. But if the ecosystem is already converging on an open standard that provides much of that foundation out-of-the-box, it’s fair to ask whether that’s infrastructure you want to build and maintain yourself.
At Glean, we think
open protocols and strong indexing are complementary
, not competing:
Our Enterprise Graph and indexing stack do the heavy lifting of unifying, structuring, and ranking enterprise data.
Open standards like MCP, skills, and agent frameworks help that context reach the agents and hosts our customers actually use.
So no, we don’t think MCP is “dead.”
MCP on a single laptop was probably over‑sold. But
MCP as a central layer for enterprise AI is only just getting started.
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
