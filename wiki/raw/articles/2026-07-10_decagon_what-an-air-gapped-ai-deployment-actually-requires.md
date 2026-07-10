---
title: "What an air-gapped AI deployment actually requires"
source: "Decagon Blog"
url: "https://decagon.ai/blog/what-an-air-gapped-ai-deployment-actually-requires"
scraped: "2026-07-10T06:00:51.012901+00:00"
lastmod: "None"
type: "sitemap"
---

# What an air-gapped AI deployment actually requires

**Source**: [https://decagon.ai/blog/what-an-air-gapped-ai-deployment-actually-requires](https://decagon.ai/blog/what-an-air-gapped-ai-deployment-actually-requires)

Introducing Duet Autopilot.
Learn more
Product
Product overview
Channels
Voice
Human-like conversation
Chat
Safe, on-brand replies
Email
Contextual resolutions
Duet AI partner
Build
AOPs
Workflows for AI agents
Integrations
Support for tool connectors
Optimize
Experiments
Live A/B testing
Testing & QA
Simulations at scale
Scale
Insights & reporting
Voice of the customer
Watchtower
Always on QA
Suggestions
AI powered knowledge
Industries
Retail
Travel & hospitality
Technology
Financial services
Health & wellness
Media
Telecommunications
Customers
Resources
Learn
Resources Hub
Decagon University
Glossary
Introducing Duet Autopilot: The self-improving agent for conversational AI
Learn more
Company
About
Careers
Security
Sign in
Get a demo
Sign in
Get a demo
Research & Technology
What an air-gapped AI deployment actually requires
Posted on
July 9, 2026
Sahib Pandori
Member of Technical Staff, Infra
Article
Table of contents
Introduction
What is an Agent Engineer?
Subscribe to our Newsletter
Get monthly updates with our latest articles, podcasts, videos, and more.
Must be a valid company email (i.e. example@companydomain.com)
Get a demo
Done!
Oops! Something went wrong while submitting the form.
In the early days of enterprise AI, the fastest path to production was to find a high-value, well-scoped use case and keep the AI agent's access narrow to manage security. That approach worked well enough to generate early wins, but those wins created an appetite for more sensitive workflows that required deeper integrations with core business systems.
With that expanded scope comes a more demanding conversation about deployment. Scoping down is no longer a viable security strategy, particularly for regulated industries like financial services, healthcare, and travel, which have very strict requirements around infrastructure.
At Decagon, we have worked through this evolution with some of the largest enterprises across these verticals. Earlier this year, we deployed our conversational AI platform entirely inside an F50 financial services company's own VPC to support their voice use cases, one of the most demanding infrastructure configurations we've encountered.
Here is what it took, and what we learned.
Not every enterprise needs the same deployment
Before getting into the specifics, it helps to understand the range of options. Enterprise deployment requirements exist on a spectrum, and the right model depends on your organization's risk tolerance, regulatory environment, and operational capacity.
Decagon offers several deployment options, but generally they fall into three broad categories:
Standard SaaS
is where the majority of Decagon's customers run, including heavily regulated F50 enterprises. Decagon hosts and manages everything, and customers get the fastest path to production. For most enterprises, this model already meets stringent security requirements.
Single-tenant SaaS
gives customers a dedicated VPC inside Decagon's cloud. The infrastructure is isolated at the customer level, with stronger separation than multi-tenant SaaS, while Decagon retains full operational responsibility.
Cloud-prem / VPC
means Decagon's full stack runs inside the customer's own cloud environment. The customer owns the infrastructure, while Decagon manages the software. It is the most demanding option in every respect, and it exists for organizations whose requirements genuinely cannot be met any other way.
These three models cover the vast majority of deployments we operate today, though we also support options such as on-premises datacenter deployments for more specialized requirements.
Standard SaaS
Single-Tenant
Customer VPC
Best for
Most enterprises, including heavily regulated industries
Organizations requiring dedicated infrastructure without operational overhead
Enterprises with strict data residency or air-gap requirements
Key benefits
Fastest time to value, lowest overhead, full feature parity
Dedicated isolation, Decagon-managed operations
Maximum control, data never leaves customer environment
Tradeoffs
Shared infrastructure
Higher cost than SaaS
Highest cost, longest deployment, customer owns uptime
For a small number of enterprises, that third option is the only one that works. Getting there required us to solve certain deployment problems we had not faced before.
The engineering challenge
A customer VPC deployment means no public internet connectivity beyond the bare-minimum deemed necessary by the customer to reach the environment. Every service Decagon's stack depends on had to be either replaced with a customer-approved alternative or routed entirely through the customer's internal network. No outbound requests leave the environment, and every third-party dependency was evaluated against the customer's approved services list.
That constraint is table stakes for this class of deployment. In practice, it surfaces three specific challenges that are worth understanding in detail.
Building a telephony layer from scratch
Voice is a core part of what Decagon delivers. In this deployment, the standard telephony vendor was not on the customer's approved services list. Rather than scoping voice out of the deployment, our engineering team built a self-hosted telephony layer from the ground up using telecom industry primitives, running entirely within the customer's environment.
This was the most technically complex part of the project. The team had to solve for SIP signaling, media handling, and connection management without any of the managed infrastructure that telephony vendors abstract away. The result is a production-grade, self-hosted system that delivers full voice capability inside an air-gapped environment.
To our knowledge, no other AI-native conversational platform has built and deployed something comparable.
Self-hosted models inside the customer perimeter
Decagon’s agents are built upon a coordinated network of specialized models. We use both models from the frontier labs, along with our models developed by Decagon Labs that are purpose-built for CX performance and latency.
In an air-gapped environment, standard external API calls to those providers are not possible. The solution required two things in parallel: private connectivity with frontier model providers into the customer environment, and self-hosted model inference layer for the models Decagon has developed. The full model infrastructure had to be reconstructed within the customer's perimeter without degrading agent quality or response latency.
Deep integration with customer systems
Enterprise customers do not have generic infrastructure. This customer had its own internal tooling, authentication systems, and data systems that Decagon's agent runtime needed to connect with natively rather than through APIs. The integration work required building custom connectors specific to this customer's environment, coordinating closely with their engineering teams, and going through their internal approval processes for each system touch.
This kind of work is operationally intensive. Getting an AI agent to work for specific workflows is one problem, but getting it to work inside a highly specific, tightly controlled environment is a different one.
Why SaaS is still the right call for most
The deployment described above is impressive engineering. It is also expensive, slow to stand up, and operationally demanding for the customer. That is worth being direct about.
Customer VPC deployments require over-provisioned infrastructure by design, high setup costs, and a deployment timeline that is longer than standard SaaS. Because the customer owns the environment, they are also responsible for first-line uptime defense, which adds to the operation burden.
Several enterprises have gone through serious evaluations of the VPC model and concluded that Decagon's standard SaaS meets their actual security requirements. That outcome is not a failure of ambition but reflects a genuine understanding of what the VPC model costs versus what it delivers. For organizations without hard regulatory or contractual requirements that mandate private infrastructure, the SaaS model provides a hardened, enterprise-grade security posture without the overhead.
A new baseline for enterprise AI
The enterprises setting the highest infrastructure bar are not waiting. Decagon now has validated, working deployment packages across a large spectrum and has operational experience to support all of them.
If infrastructure requirements have been the reason your organization has not moved forward with AI, we would love to talk.
Sahib Pandori
—
Member of Technical Staff, Infra
“With Decagon Voice, we’re able to combine high performance and seamless brand customization with cross-channel memory, ensuring every interaction is connected and true to Chime’s member-first values.”
Janelle Sallenave
Chief Operating Officer
Start improving your workflow with Decagon
With Decagon, CX teams don’t have to guess whether a change will improve CSAT or deflection. They can move quickly, measure what matters, and act on what works.
Get a demo
Your browser does not support the video tag.
Join us
There are very few places where you can prototype with frontier LLMs, ship to production in days, and watch users engage with the systems you built—all while owning the entire stack, from intent parsing and tool usage to API integration and observability. This role at Decagon is one of those places.
From my own experience working across both agent development and broader engineering initiatives at Decagon, I’ve seen firsthand how uniquely impactful this work can be. Whether I’m building intelligent workflows for customers or designing infrastructure that supports our agent platform, it’s rare to find an environment where the work transitions from concept to production within days, actively powering user experiences and transforming how businesses operate.
If you’re looking for a role where you can:
Build at the frontier of LLMs, automation, and user interaction
Deploy AI agents that solve high-value business use cases across industries including retail, travel and hospitality, fintech, edtech, and more
Work directly with customers on high-impact use cases
Ship fast, iterate constantly, and own your work from idea to production
Join a fast-moving, collaborative team solving real-world challenges with AI
We’d love to hear from you!
Explore careers
Related posts
Research & Technology
DuetBench: An evaluation of self-improving customer service agents
Posted on
June 9, 2026
Research & Technology
Why MCP alone isn’t enough for reliable agent tool use
Posted on
April 14, 2026
Research & Technology
Optimizing GEPA for production: A test-driven approach to prompt engineering
Posted on
March 25, 2026
Explore more topics
AI agent building
Test & experimentation
Analytics & Voice of Customer
Voice & omnichannel support
Guardrails, security, & governance
Use cases & experiences
Workplace
The AI concierge for every customer.
Get a demo
Footer
Product
Overview
AOPs
Chat
Email
Voice
Integrations
Experiments
Insights & Reporting
Testing & QA
Watchtower
Suggestions
Trust Center
Industries
Retail
Travel & Hospitality
Technology
Financial Services
Health & Wellness
Media
Telecommunication
Resources
Customers
Resources Hub
Glossary
Company
About
Careers
Privacy Policy
Security
Contact Sales
Contact Support
©
0000
Decagon. All rights reserved.
