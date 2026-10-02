---
title: "How We Built Harvey’s Connector Library"
source: "Harvey Blog"
url: "https://www.harvey.ai/blog/how-we-built-harvey-connector-library"
scraped: "2026-10-02T06:00:12.898675+00:00"
lastmod: "2026-10-01T16:00:00.000Z"
type: "sitemap"
---

# How We Built Harvey’s Connector Library

**Source**: [https://www.harvey.ai/blog/how-we-built-harvey-connector-library](https://www.harvey.ai/blog/how-we-built-harvey-connector-library)

We Raised $550M at a $15.5B Valuation to Help Legal Teams Own Their Intelligence
Learn more
We Raised $550M at a $15.5B Valuation to Help Legal Teams Own Their Intelligence
Learn more
We Raised $550M at a $15.5B Valuation to Help Legal Teams Own Their Intelligence
Learn more
→
:Harvey:
Platform
Solutions
Customers
Security
Resources
Company
Overview
→
A unified view of how Harvey's products work together to support your entire practice.
Agents
→
Purpose built agents execute complex legal work end to end.
Vault
→
Securely store, organize, and bulk-analyze legal documents.
Knowledge
→
Research complex legal, regulatory, and tax questions across domains.
Spaces
→
Work with legal teams across organizations in secure, shared spaces.
Command Center
→
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
Contract Intelligence
→
Surface insights, strengthen negotiations, and accelerate reviews.
Horizon Scanning
→
Track, assess, and take action on regulatory changes.
Harvey Mobile
→
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
→
Access Harvey where you already work and ground every answer in sources you trust.
Introducing Memory
New
→
Your preferences carried across Harvey so every response comes back consistent with how you work.
Innovation
→
Scale expertise and impact to drive firmwide transformation.
Litigation
→
Reduce manual effort, prioritize strategy, and drive stronger outcomes in litigation.
Transactional
→
Accelerate due diligence, contract analysis, and review with precision and control.
In-House
→
Streamline work and shift focus to strategy and speed.
Law Firms
→
Deliver your firm's best work on every matter, with more time for clients.
Mid-Sized Firms
→
Drive outsize impact with tools built for lean teams.
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
Research
→
Models, benchmarks, and field notes from Harvey's research on the frontier of legal AI.
ROI Calculator Law Firm
→
See Harvey's Impact on Your Firm.
ROI Calculator In House
→
See Harvey's Impact on Your Business.
Harvey Academy
→
Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.
About
→
Who we are and what we're building.
Careers
→
Join our team and help Harvey shape the future of professional services.
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
Agents
Purpose built agents execute complex legal work end to end.
Vault
Securely store, organize, and bulk-analyze legal documents.
Knowledge
Research complex legal, regulatory, and tax questions across domains.
Spaces
Work with legal teams across organizations in secure, shared spaces.
Command Center
Analytics, benchmarking, and agentic insights to lead their organization’s AI transformation
Contract Intelligence
Surface insights, strengthen negotiations, and accelerate reviews.
Horizon Scanning
Track, assess, and take action on regulatory changes.
Harvey Mobile
Get up to speed, capture new information, and keep work moving from anywhere.
Ecosystem
Access Harvey where you already work and ground every answer in sources you trust.
Introducing Memory
New
Your preferences carried across Harvey so every response comes back consistent with how you work.
Solutions
Innovation
Scale expertise and impact to drive firmwide transformation.
Litigation
Reduce manual effort, prioritize strategy, and drive stronger outcomes in litigation.
Transactional
Accelerate due diligence, contract analysis, and review with precision and control.
In-House
Streamline work and shift focus to strategy and speed.
Law Firms
Deliver your firm's best work on every matter, with more time for clients.
Mid-Sized Firms
Drive outsize impact with tools built for lean teams.
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
Research
Models, benchmarks, and field notes from Harvey's research on the frontier of legal AI.
ROI Calculator Law Firm
See Harvey's Impact on Your Firm.
ROI Calculator In House
See Harvey's Impact on Your Business.
Harvey Academy
Introducing Harvey Academy: on-demand training, expert workflows, and step-by-step guidance to help legal teams get the most out of Harvey.
Company
About
Who we are and what we're building.
Careers
Join our team and help Harvey shape the future of professional services.
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
How We Built Harvey’s Connector Library to Work Across External Tools
Building the Connector Library meant making external tools available to agents while enforcing permissions and accounting for differences between providers.
by
Chenghao Wang
•
Oct 1, 2026
A law firm runs on a stack of services such as Outlook or Gmail for client communication, iManage for documents, and data rooms for transactions. Harvey's
Connector Library
is built for exactly that scenario: an admin enables a connector, a user connects once, and the services the firm already relies on become usable inside Harvey. Today, users hold more than 110,000 individual connections across these sources, and agents make tens of thousands of connector tool calls a week.
Making those services available to an agent creates a recurring engineering challenge. For every tool call, we need to know whether the user can use the tool, whether the result stays within their permissions, and whether the call is trustworthy. A single request may involve several calls, so those checks must hold at every step.
This post explains how we enforce those boundaries and how we handle the differences between vendors without passing that complexity on to the agent.
The Connector Architecture: From a Tile to Tools in the Agent's Hands
A connector in the library is a vendor-level object: a tile in the catalog, one permission, one admin toggle, backed by one or more members that each provide part of the integration. A member is either a native integration or an MCP connector (a server the vendor operates, which Harvey calls over the
Model Context Protocol
).
Everything that defines a connector is collected in one registry that lives in code: what the connector is, which capabilities its native and MCP members provide, its permission, and the routing note written for the agent; the rest of the backend is an extension of this registration. That is what makes onboarding cheap — since Early Access opened, new connectors have entered the catalog one after another.
When a user works with the agent, the client sends their selected connector and tools with the request. The backend resolves that selection into the connector’s native or MCP members and their tool configurations. Unknown connector types and tool keys are rejected.
Resolution happens once per turn. The resulting configuration travels with the run and is reused as the agent works.
The selected tools are registered into the model through Harvey's own adapters, and the agent decides, within that selection, what to call at each step. These tool requests still clear one more set of machinery and are allowed or refused. An allowed call goes out with the connection's own credential: for sources holding personal data that is always the asking user's own grant, and the source system returns only what that user may see under its own ACLs. In the results, documents retrieved by native members are presented to the user with inline citations, while MCP members' output enters the model context as plain text.
The Trust Architecture: Approval and Call Safety
Connector security starts before a tool reaches users and continues when the agent calls it. Before launch, our security team reviews threats such as prompt injection, misuse of write capabilities, credential compromise, cross-tenant leakage, and supply-chain risk. At runtime, each call must still pass the applicable permission and policy checks.
When a connector is introduced, our security team validates it against Harvey's bar for security, assessed against a set of core threat scenarios: prompt injection, abuse of write capabilities, credential compromise, cross-tenant leakage, and supply-chain risk.
A native member is a wrapper we wrote around the vendor's API, and it goes through the same security review: which of the vendor's APIs we call and which scopes we request are what the security team signs off on. An MCP member's server is operated by the vendor, so the review has to judge a system someone else runs, and it gets an extra layer of admission. The vendor submits its full tool list and capability scope, hosting and auth details, data-processing regions, and test credentials, and the security team reviews the tools one by one, deciding for each whether it is approved and assigning its risk level. This way, approval is a hard gate before engineering integration begins. Those decisions land in a registry that ships with the code: a structured URL matcher, the vendor's full advertised tool list, the subset that may be invoked, and a hand-written risk and capability annotation for each.
With this information in hand, we add a further layer of runtime controls for MCP. It shapes what the agent can even see, and tools outside the approved set never appear in the model's list. We designed our own module for this, the
MCP policy engine
. Each time the agent wants to call a tool, it checks that the tool is still on the approved list, that the risk and capability annotation written at review time is still there (a missing one is an outright refusal), and that the workspace and user settings allow it. The engine's rule layer is written in Rego (Open Policy Agent's policy language), with the interpreter embedded in-process. The input that reaches the rules is deliberately data-blind: only the tool’s identity, risk level, capability flags, and the names of the run’s prior MCP calls cross over, a user's arguments and free text never do, and a rule-evaluation error fails closed.
We also keep our own fingerprint of each approved tool, pinning its description and input schema at review time and comparing them on every tool discovery, and a change or a disappearance alerts the team. Tool results still pass through sanitization, including detection of mixed-script confusable characters, to catch as much encoding- and rendering-level disguise as possible. The aggregate telemetry along this path holds the same line: tool arguments, result contents, server URLs, and user identifiers never appear in our health events and metrics.
Beyond what Harvey enforces, we hand controls to the customer. A workspace admin can disable or enable, for their own users, a specific connector, a specific member (native or MCP), or a single MCP tool; users can tighten further on top of the admin's settings.
Together these controls compose into one intersection: the MCP tools the model can see = advertised by the vendor ∩ reviewed by Harvey ∩ allowed by the effective workspace and user settings ∩ explicitly selected for this request, when a selection is present.
But as we support more and more connectors, additional problems appear.
Platform Differences: Keeping Each Vendor's Quirks Inside the Adapter
We kept finding that vendors behave differently, and the differences turn into concrete problems. For example, a valid token gets thrown away as invalid, a user is asked to re-authorize for no visible reason, or a tool schema the vendor declares legal is rejected by the model.
The MCP authorization spec is still evolving, and the servers we integrate support different versions of it. The expected flow involves protected resource metadata discovery (RFC 9728), authorization server metadata (RFC 8414), dynamic client registration (RFC 7591), OAuth 2.1 with PKCE, and resource binding (RFC 8707).
In production, servers follow that flow differently. Some never send the 401 challenge that should start discovery. One token endpoint returns a valid token with 201 Created, and servers interpret the same scope declaration differently. Our authorization layer has to accommodate those differences for each server we integrate.
Token handling differs too. Several providers issue single-use refresh tokens, while frontend prechecks, scheduled syncs, export jobs, and background renewal can all want the same user's token at the same time. This layer serves roughly 13 million credential reads a day.
The same goes for tools. Client registration alone has three paths: the 2026-07-28 spec revision makes CIMD (Client ID Metadata Documents) the recommended path and deprecates Dynamic Client Registration, keeping it for backwards compatibility, while in production some servers we integrate only support dynamic registration and others only work with a client Harvey pre-registers. A tool's schema also passes through three hands, the MCP server, the agent SDK, and the model API.
We handle these differences in an adapter layer. For authorization, we follow the behavior a server actually exposes: we can discover metadata directly when it does not send a challenge, accept valid tokens returned with either 200 or 201, and request the scopes it advertises.
We also use conditional write-backs to handle competing token updates without locks. At discovery, we normalize tool schemas before registering them with the agent. If the adapter encounters behavior it does not recognize, it alerts the team so we can investigate and update the integration.
Building on a Consistent Foundation
Each new connector brings another set of vendor behaviors to account for. Keeping those differences in the adapter lets us expand the library while applying the same approval, permission, and runtime checks to every tool call.
The Connector Library is now live.
Explore the connectors
Harvey has reviewed and approved, connect the tools your team uses, and start working with them in Harvey.
If you'd like your service connected to Harvey, use the
Connector Library intake form
. And if these sound like the engineering challenges you'd like to work on,
we're hiring
.
Next Up
How We Rebuilt Playbook Review as a Multi-Agent System
Harvey Tenet Research Preview
Scaling Document Processing Across the Harvey Platform
Unlock Professional Class AI for Your Organization
Request a Demo
Copyright © 2026 Harvey AI Corporation. All rights reserved.
Platform
Overview
→
Agents
→
Vault
→
Knowledge
→
Spaces
→
Command Center
→
Contract Intelligence
→
Horizon Scanning
→
Ecosystem
→
Harvey Mobile
→
Partnerships
→
Solutions
Innovation
→
Transactional
→
Litigation
→
In-House
→
Law Firms
→
Mid-Sized Firms
→
Company
Customers
→
Security
→
About
→
Careers
→
Newsroom
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
Instagram
→
Copyright © 2026 Harvey AI Corporation. All rights reserved.
