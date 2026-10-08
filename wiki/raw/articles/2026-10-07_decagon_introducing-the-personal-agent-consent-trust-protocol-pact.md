---
title: "Introducing the Personal Agent Consent & Trust Protocol (PACT)"
source: "Decagon Blog"
url: "https://decagon.ai/blog/introducing-the-personal-agent-consent-trust-protocol-pact"
scraped: "2026-10-07T06:00:28.901502+00:00"
lastmod: "2026-10-06T19:15:12.643Z"
type: "sitemap"
---

# Introducing the Personal Agent Consent & Trust Protocol (PACT)

**Source**: [https://decagon.ai/blog/introducing-the-personal-agent-consent-trust-protocol-pact](https://decagon.ai/blog/introducing-the-personal-agent-consent-trust-protocol-pact)

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
Financial services
Travel & hospitality
Health & wellness
Technology
Retail
Telecommunications
Media
Customers
Resources
Resources Hub
Blog
Decagon University
Videos
Glossary
Guides
Introducing Duet Autopilot: The self-improving agent for conversational AI
Learn more
Company
About
Careers
Trust Center
LinkedIn
X
Sign in
Get a demo
Sign in
Get a demo
Product
Introducing the Personal Agent Consent & Trust Protocol (PACT)
Posted on
October 6, 2026
Harry Gao
Member of Technical Staff, ASWE
Gram Liu
Member of Technical Staff
Article
Table of contents
Introduction
What is an Agent Engineer?
Subscribe to our Newsletter
Get monthly updates with our latest articles, podcasts, videos, and more.
Must be a valid company email (i.e. example@companydomain.com)
Sign up
Done!
Oops! Something went wrong while submitting the form.
Today, we’re open-sourcing the
Personal Agent Consent & Trust Protocol (PACT)
, co-developed and supported by Instinct. We’re also excited to join the Personal Agent Protocol working group announced by the team behind Meta’s Muse to help shape an industry standard.
Personal agents like Muse, Instinct, and dots are starting to book travel, manage purchases, and resolve issues on their users’ behalf. As they contact businesses, they increasingly encounter AI agents acting for those businesses. PACT gives these interactions explicit, verifiable customer permissions. Built on the Agent2Agent protocol and OAuth 2.0, it lets businesses verify whom a personal agent represents and what that customer has authorized it to do.
Last week, we introduced
Personal Agent Gateway
and the principles behind it. In this post, we walk through how PACT works and the design decisions that shaped it.
How PACT works
PACT involves three parties: the customer’s personal agent, the business, and the provider (such as Decagon) that hosts the business’s agent. It separates the identity of the personal agent from its authority to act on a customer’s account. The interaction follows three steps.
1. Discover and connect
The personal agent discovers the business’s
A2A Agent Card
, which advertises its endpoint, authentication requirements, and available permissions. Each business defines its own scopes, such as orders:read or orders:cancel, with descriptions the personal agent can use to select the permissions it needs.
The personal agent authenticates its requests with a short-lived, signed JWT. The provider verifies the signature against the personal agent’s published public keys. This establishes which platform is calling, but does not yet prove ownership of a customer account.
2. Authenticate the customer and obtain consent
For delegated account access, the personal agent requests scopes through OAuth’s device authorization flow and presents the customer with a login link. The customer signs in directly with the business, then chooses which permissions to approve. The personal agent never handles the customer’s login credentials.
The provider issues a short-lived, signed delegation token binding the verified customer account, personal-agent platform, target business, and approved scopes.
3. Act within the granted permissions
Each subsequent request carries both the personal agent’s identity and the customer’s delegation. The provider verifies the agent’s identity and delegated authorization before running the business’s agent within the approved scopes. The business’s policies continue to govern which actions are allowed.
If the conversation requires additional permission, PACT uses A2A’s authorization-required state to request it and continue the same conversation. Replies under delegated authorization include signed receipts recording the scopes used and actions taken.
Design decisions
Route requests through the business’s agent.
Personal agents express what the customer wants; the business’s agent handles the underlying tools and workflows under the business’s policies.
Build on existing standards.
Reuse A2A for communication and OAuth for authorization, specifying how they work together.
Separate identity from authority.
Verify which agent is calling independently of what the customer has permitted it to do.
Let businesses define permissions.
Standardize how scopes are discovered and granted while leaving capabilities and policies to each business.
Keep login with the business.
Bind consent to a verified customer account without exposing login credentials to the personal agent.
An open standard
Personal agents need to work across businesses, and businesses need to serve customers using different personal agents. Without a shared specification for this interaction, developers must reconcile differences in how providers identify agents, obtain customer consent, and carry authorization with each request.
PACT makes those mechanics consistent across implementations. Personal-agent developers can use the same integration pattern across participating providers, while businesses can support different personal agents through a common interface. The customer’s choice of personal agent shouldn’t depend on which platform a business uses.
We built PACT in collaboration with Instinct to bring both sides of the interaction into its design. By publishing the specification openly, we’re inviting other personal-agent developers, businesses, and agent platforms to implement it and help shape its evolution.
To get started, read the
PACT specification
, or explore the code and share feedback on
GitHub
.
Harry Gao
—
Member of Technical Staff, ASWE
Gram Liu
—
Member of Technical Staff
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
Product
The AI concierge for every customer [and their agent]
Posted on
October 1, 2026
Product
Personal agents are here. Meet them on your terms.
Posted on
October 1, 2026
Product
Introducing Voice 3 and Chord, our new speech model
Posted on
October 1, 2026
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
