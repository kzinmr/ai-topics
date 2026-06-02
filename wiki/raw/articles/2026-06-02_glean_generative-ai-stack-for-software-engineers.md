---
title: "Generative AI for software engineers: Build the right AI stack"
source: "Glean Blog"
url: "https://www.glean.com/blog/generative-ai-stack-for-software-engineers"
scraped: "2026-06-02T06:00:10.085991+00:00"
lastmod: "None"
type: "sitemap"
---

# Generative AI for software engineers: Build the right AI stack

**Source**: [https://www.glean.com/blog/generative-ai-stack-for-software-engineers](https://www.glean.com/blog/generative-ai-stack-for-software-engineers)

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
Professional
Services
Consulting
Construction
IT Services
Legal
Scroll for more
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
Professional
Services
Consulting
Construction
IT Services
Legal
Scroll for more
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
Last updated Jun 01, 2026.
Generative AI for software engineers: How to build the right AI stack
0
minutes read
Nikhhar Gupta
SEO Manager
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
Generative AI coding assistants have made typing faster but haven’t fixed the real bottleneck in software engineering: reconstructing context across fragmented systems like GitHub, Jira, Slack, docs, incidents, and observability tools, which leads to rework, trust issues, and safety risks rather than durable productivity gains
The engineering AI stack is best designed as two layers: a shared, permission-aware context layer that unifies code, tickets, incidents, docs, logs, and ownership, and a set of coding and interaction surfaces (IDEs, code hosts, Jira, chat, observability, agents) that call into this context instead of each rebuilding partial views.
Glean’s role in this landscape is to provide that secure, model-agnostic context foundation—indexing engineering systems once, enforcing source permissions, and exposing an enterprise graph that improves workflows like onboarding, safe routine changes, and incident response while working alongside existing coding assistants via protocols like MCP.
To build the right generative AI stack for software engineering, treat AI as a layered system: use coding assistants for local code work, add a shared context layer that connects code to tickets, incidents, docs, and ownership, and plug in incident and agent tooling around that foundation.
Software engineering teams are no longer deciding whether to use AI. They’re deciding how to make it useful in production. Generative AI technologies like GitHub Copilot have pushed AI into daily workflows, but helping engineers write code faster doesn’t solve the harder problem — getting the right context, guardrails, and workflow support around the code so teams can ship safely and reliably.
The real bottleneck for most teams is context reconstruction. Engineers still lose hours chasing design docs, Jira tickets, incident history, ownership records, Slack threads, and runbooks across systems that don’t naturally talk to one another. A stack that closes that gap is worth building. One that adds another disconnected tab isn’t.
The best generative AI stack for software engineers combines coding assistants, context systems, observability tools, and governance in a way that fits how engineering work actually happens.
Three gaps that stall early AI rollouts
Engineering managers typically see three recurring gaps when adopting generative AI technologies through coding assistants:
Outcome
– AI feels faster, but creates downstream rework. In a
METR randomized controlled trial
of experienced open-source software developers, tasks completed with AI took 19% longer — even though participants expected to be 24% faster and still believed afterward that AI had helped.
Trust
– Suggestions land close enough to look right, but still need heavy verification. In the
2025 Stack Overflow Developer Survey
, more developers actively distrusted AI accuracy than trusted it, and 66% cited code that was “almost right, but not quite” as their biggest frustration.
Safety
– Weak guardrails increase the attack surface. In the
2025 Veracode GenAI code security report
, close to 45% of AI-generated code samples contained at least one high-severity security vulnerability.
Better code generation from the model helps. But these gaps don't close with a better model. They close with a better system of context around it.
Four categories of AI tools in the engineering AI stack
The clearest way to plan your stack is to think in terms of four discrete jobs your tools need to do across the software development process:
1. Assistants for local code generation
IDE-native tools like Cursor, GitHub Copilot, Claude Code, Windsurf, Codeium, and Sourcegraph Cody handle inline code generation, code refactoring, test generation, bug detection, and localized debugging. They help individual developers write code faster inside a repo or workspace, and most teams already have one in place.
Where they fall short is visibility into the surrounding system. A coding assistant working from repo context alone has no awareness of the Jira ticket that motivated the change, the incident that flagged the regression, the design doc that set the constraints, or the Slack thread where the team decided on their approach.
41% of software developers
say their biggest productivity drain is outdated, inconsistent, or siloed information.
2. A context platform that understands engineering work
A context platform connects the artifacts and people behind the code. It links code hosts, work tracking, docs, chat, incidents, and observability trails into a shared, permission-aware view of the engineering environment — so an engineer can ask “What broke the last time this alert fired?” or “Who owns this endpoint now?” and get a grounded answer built from real artifacts instead of a plausible guess.
This is the layer many companies discover they need once generative AI in software development moves from experiment to daily use. In Atlassian’s
State of Developer Experience Report
, 62% of developers said reconstructing context across multiple tools slows them down.
Glean
is designed for this role. It builds a shared system of context across tools like GitHub, Jira, Confluence, Slack, and Teams, using its Enterprise Graph to link services, incidents, tickets, owners, and design artifacts. Because Glean inherits and enforces source-system permissions, answers stay within the access boundaries engineers already have.
3. Observability AI for incident signals
Observability AI knows what the metrics say. It can summarize alerts, traces, and logs, group related signals, and highlight likely regressions — all of which helps improve developer productivity and reduce mean time to resolution. What it can‘t tell you is which Jira ticket changed the service, what the design doc specified, who approved the rollout, or how a similar incident was resolved six months ago. Pairing incident tools with a context platform fills those gaps and turns triage from a log-reading exercise into a cross-system investigation.
4. Agent platforms and model hubs
General-purpose AI platforms and agent frameworks — including large language model providers and orchestration runtimes — give teams model choice, agent runtime support, and workflow orchestration. They make it easier to prototype assistants and connect them to other technologies in the stack.
What they don’t provide on their own is shared engineering context: integrations across code, tickets, incidents, and docs, plus a consistent, permission-aware view across systems. Agent platforms are only as useful as the data, structure, and governance you plug into them — which is why they work best when they can call into a shared context layer rather than each rebuilding its own partial view.
From four tool categories to two architectural layers
Those four tool categories map to a simpler architectural model: one layer that
understands the work
(context), and one layer where engineers
do the work
(coding and interaction surfaces).
The context layer connects to code hosts, Jira, incident systems, observability tools, docs, wikis, and chat. It indexes those systems, links related artifacts, respects permissions, and gives engineers one trusted way to assemble context across the software development lifecycle.
A useful context layer should be able to answer questions like:
Which repos, tickets, incidents, and owners are tied to this service?
What changed before this issue appeared?
Which design docs and prior decisions still matter here?
Who should review or approve the next step?
The coding and interaction layer is where engineers spend their time. This includes the IDE, the code host, work tracking, incident consoles, and collaboration tools. These surfaces are where code is edited, reviews happen, incidents are resolved, and work moves forward.
The key point is that coding and interaction surfaces shouldn’t have to rebuild context for every query. When each assistant builds its own partial view of the world, engineers get inconsistent answers, duplicated security work, and more AI sprawl.
Evaluate every tool with these questions in mind
The entire AI stack involves fast-evolving technologies. Before adding another GenAI tool to the stack, keep the conversation grounded with these four questions:
What context does it actually have?
“Context-aware” can mean almost anything. A tool that only sees the current file or repo will miss the tickets, incidents, docs, owners, and constraints that shape real engineering decisions. A stronger tool can follow the chain from alert to ticket to code change to owner to prior incident without a human stitching it together. The depth of access to your engineering systems determines the quality of every AI-generated answer, and that context matters more than the model‘s training data alone.
How is trust earned, not assumed?
Engineers trust systems that show their work — answers that are grounded in real artifacts, linked back to sources, and easy to verify. If people still have to redo the investigation to confirm the answer, adoption stalls and code quality gains disappear. Glean grounds every response in your own code, tickets, docs, and discussions, with source links so engineers can inspect the evidence directly.
Where does your data go, and who can act on it?
Once AI can read source code, incidents, and tickets — and especially once it can take action — you’re making a security and governance decision. That means understanding where indexes live, whether permissions are inherited from source systems, how auditing works, and whether the tool operates inside the controls your security team requires. Glean supports single-tenant deployment options across AWS, Azure, or GCP, with strict permission enforcement and auditability built in.
Does it fit the way your teams already work?
The strongest tools fit inside existing workflows, not alongside them. A practical stack should integrate cleanly with GitHub or GitLab, Jira, Slack or Teams, observability tools, the IDE — and let you start with one development team‘s specific needs before expanding.
Design the stack around real workflows
A good engineering architecture is much easier to evaluate when you look at common workflows instead of abstract features.
Onboarding and service understanding should start with context
New engineers rarely struggle because there’s no code. They struggle because the code is surrounded by scattered history: the design doc is in one wiki, the service owner changed twice, the last incident is buried in Slack, and the Jira trail is incomplete. According to
GitLab research
, nearly half (44%) of organizations say onboarding new software developers takes more than two months.
This is the problem a context layer solves. When the stack connects service ownership, docs, incidents, and code history, onboarding becomes faster and less dependent on tribal knowledge. GitLab also found that 43% of developers using AI for software development reduced onboarding time to less than a month. With Glean, for example, a new engineer can ask for an overview of a service and get back the relevant design docs, recent incidents, current owners, and related tickets — assembled from real artifacts and documentation, not a summary someone remembered to update.
Routine changes should use AI with guardrails
Generative AI already handles repetitive, low-scope software engineering tasks well: config tweaks, test case generation, documentation updates, simple bug fixes, incremental refactors. But even routine changes need the surrounding requirements and constraints.
Mature teams focus on defining clear change classes where AI is allowed to propose edits — log-level changes, certain config updates, non-behavioral refactors, documentation and tests — and treat linked tickets, design docs, and comments from shared context as guardrails. The coding assistant writes the patch; the context layer acts as a quality assurance check, confirming the patch lines up with the ticket, the service constraints, and the code quality expectations for that code path.
Incident response should combine signals with cross-system context
During an incident, the three urgent questions are: what changed, what is failing, and who needs to be involved? Observability AI can summarize the signals. A context platform connects those signals to recent code changes, related tickets, owners, prior incidents, and relevant docs — so the team isn’t rebuilding the story from scratch during an outage.
LinkedIn built a Glean-powered threat-bot agent for exactly this kind of cross-system triage and saved $2.4M in annual engineering time. Uber engineering saw a 20% reduction in time to ship code after adopting Glean as their context platform.
Glean: the context foundation for the rest of the stack
Glean fits into this picture as the
shared context layer
that helps the rest of the AI-powered stack work from the same set of facts.
Glean connects engineering data sources — code hosts, Jira, docs and wikis, chat, incidents, observability-adjacent systems — and builds a shared system of context, using its Enterprise Graph to connect people, content, and work. Engineers can search and reason across the real stack instead of bouncing between disconnected tools. Coding assistants can pull that context into the editor through MCP, so suggestions are grounded in the broader system, not just the open file.
That approach is already proving out. Two of the three largest coding-assistant organizations already rely on Glean to power the context layer behind their engineering platforms.
The generative AI stack will keep changing. Teams will swap coding assistants, test new models, and cycle through workflow technologies. A stable, governed context layer underneath those shifts is what keeps your stack from fragmenting every time something new ships — and gives future tools the same trusted foundation from day one. Glean is designed for that role: model-agnostic, open to the coding assistants and agent frameworks your architecture already includes, and built so you index once and reuse that context across every surface.
Build the stack deliberately, not tool by tool
The conversation about applying generative AI in software engineering has moved past “Which copilot is best?” The question now is what stack helps your software developers move faster without creating more rework, trust issues, or security exposure.
For most organizations, the answer is a layered approach: coding assistants for local work, shared context connecting engineering systems, incident and observability AI for telemetry-heavy workflows, and agent platforms orchestrating tasks on top of that foundation. The organizations building this way are already measuring team performance gains in cycle time, onboarding speed, code quality, and incident resolution.
Get the full framework
For the complete tooling landscape, a detailed look at the two-layer model, real-world examples, and the evaluation priorities engineering leaders should use before scaling generative AI technologies across the software development lifecycle, read
The software engineer’s field guide to the AI stack
.
Frequently asked questions
What is MCP and how does it connect coding assistants to a context layer?
MCP (Model Context Protocol) is an open standard that lets AI-powered tools, including large language model-based coding assistants, call into external data sources during a session. A coding assistant like Cursor or Claude Code can query a context platform mid-task — pulling in tickets, incidents, ownership, or design docs — without leaving the editor. Glean supports MCP so compatible assistants can call into the same shared context layer that powers Glean search, Assistant, and agents.
How do I keep source code and internal data secure when using AI coding tools?
Ask three questions: where does the data live, who can see it, and what gets logged? Any generative AI tool that indexes source code or internal docs should enforce the same access controls as the source systems. Look for single-tenant architecture, customer-controlled cloud deployment, and audit logging your security team can use. Glean runs in a single-tenant cloud environment, inherits and enforces source-system permissions, and supports the auditability enterprise teams expect.
Where should an engineering team start when building an AI stack?
Start with what you have. Most teams already run a coding assistant. The highest-leverage next step is a context layer connecting tickets, incidents, docs, and ownership to the code. Pick one development team or workflow, measure progress in cycle time and rework, and expand from there.
Do I need a context platform or can I build one with RAG and internal tooling?
A basic RAG pipeline gets you semantic search over a subset of your data. What it doesn’t give you is a linked enterprise graph, source-system permission enforcement, or a governed surface that multiple assistants and agents can call into. Most teams that start with internal RAG end up rebuilding permission logic and maintaining connector pipelines across dozens of systems. A purpose-built platform like Glean handles that infrastructure.
How do I measure whether an engineering AI stack is actually working?
Measure cycle time, rework rate, onboarding time, mean time to resolution, and context-switching frequency — not just adoption counts. Senior engineers and team leads should track these against a baseline. If cycle time drops but rework rises, the stack is producing code faster without the right guardrails. If onboarding time drops and teams are still shipping high quality code, the context layer is working. The goal is faster, safer delivery across the full workflow, not just faster output on repetitive tasks.
How long does it take to connect Glean to an existing engineering stack?
Glean’s
connectors
cover the most common engineering platforms — including GitHub, GitLab, Jira, Confluence, Slack, Teams, PagerDuty, and Datadog — with inherited permissions and real-time sync across systems. Most organizations start with one workflow or team and expand from there.
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
French (France)
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
