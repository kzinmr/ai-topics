---
title: "Personal agents are here. Meet them on your terms."
source: "Decagon Blog"
url: "https://decagon.ai/blog/personal-agents-are-here"
scraped: "2026-10-02T06:00:12.373413+00:00"
lastmod: "2026-10-01T17:25:01.971Z"
type: "sitemap"
---

# Personal agents are here. Meet them on your terms.

**Source**: [https://decagon.ai/blog/personal-agents-are-here](https://decagon.ai/blog/personal-agents-are-here)

Decagon Dialogues 2026 is here.
Register today
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
Personal agents are here. Meet them on your terms.
Posted on
October 1, 2026
Jesse Zhang
Co-founder & CEO
Ashwin Sreenivas
Co-founder & President
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
In the past month, Meta launched Muse, OpenAI introduced dots, and Instinct started placing phone calls for its users. These personal agents book, buy, cancel, and negotiate on their owners’ behalf. They're already contacting customer support, where they often reach a brand's AI agent. Customer experiences today weren't built for an agent on both ends.
Policies written for people assume finite time and patience. A person denied a refund might ask once more and let it go. A personal agent might ask for a refund once, or keep trying different approaches to maximize the concession. Businesses need to uphold their policies in either case. They also need to confirm what the customer authorized: permission to check a balance doesn’t necessarily mean permission to move money.
Blocking these agents risks losing customers to competitors and pushes agents to get better at passing as human. Letting them in without controls means more requests, less certainty, and account access that isn't secure. Businesses should embrace personal agents as a new kind of customer, but own the terms of engagement.
Four things enterprises need to get right
1. Identification
Businesses need to know whether they’re talking to a customer or the customer’s agent. Most agents today call in or open a chat like anyone else, and they can look just like a person. Detection takes signals from both the business, like device fingerprints and account history, and the CX platform, like conversational patterns and request cadence. It works best alongside an easy way for agents to identify themselves upfront, so detection only has to catch the ones that don't.
2. Access
Personal agents should reach businesses through a channel built for agents, which costs both sides less than phone calls or navigating websites. The business’s agent interprets requests and applies its policies, rather than leaving that judgment to the personal agent.
That channel should support different logic and policies for personal agents than for people. Businesses decide how requests are handled, which actions are available, and when to escalate. Those rules should apply to any personal agent through one channel. Otherwise, businesses end up rebuilding integrations and maintaining the same policies separately for every provider.
3. Authorization
Businesses must confirm which customer an agent represents and what it’s allowed to do. OAuth offers a familiar model: when you connect an app to your Google account, you approve what it can access. Here, the business defines scopes, like viewing or changing a reservation, and the customer explicitly grants them to their agent. The grant also creates a record of what the customer authorized, so the business can prove it.
4. Resolution
Two agents can loop forever if neither is built to stop. The business’s agent must hold its position on policy while remaining helpful. Escalation runs both ways. The business’s agent may need a human, and the personal agent may need its owner.
Putting these principles into practice
Today, we’re introducing Decagon’s
Personal Agent Gateway
to help enterprises identify personal agents, route their requests, and control what they can do.
Personal agent detection
handles identification. The gateway flags likely personal agents in live chat and voice using various signals; each business decides what happens next and what those agents can access. Detection will keep improving as personal agents evolve.
The personal agent channel
handles routing, trust, and resolution for agents that identify themselves. It sits alongside other channels like chat, email, and voice, with separate
Agent Operating Procedures
(AOPs). The same request can follow a different workflow depending on who’s asking, while less sensitive requests can reuse existing workflows without extra setup.
Permissions live inside the AOPs. Businesses define the scopes an agent can request and mark which sections require each one. Without the required scope, those sections are never exposed to the agent.
Take an airline. A traveler asks their personal agent to move their trip to an earlier flight. The agent requests permission to view and rebook flights, but the traveler approves only viewing. The airline’s agent shares earlier options but can’t make the change, so the personal agent asks the traveler to authorize rebooking.
A secure authorization protocol
A dedicated channel only helps if agents can find and use it consistently. Businesses also need a reliable way to verify who an agent represents and what it’s allowed to do. That’s why Decagon is introducing
PACT (Personal Agent Consent & Trust)
, a protocol that lets a person’s agent act on their behalf under permissions the service defines and the person grants.
PACT builds on the Agent2Agent protocol, which covers how agents find each other and exchange messages. It adds delegated authorization built on OAuth 2.0: a way for an agent to prove which person it represents and what that person allowed it to do.
We’re working with personal agent providers and enterprise customers to shape the protocol and refine the specification.
Every agent is someone’s customer
When people can hand the asking to an agent, they’ll reach out more often and about more things. A business that knows who’s on the other end and what the customer approved can say yes to more of those requests. Each one it resolves gives that customer another reason to stay.
Personal Agent Gateway and PACT help businesses welcome this new kind of customer with clear permissions and control. The customer chooses who acts for them. The business sets the terms.
Jesse Zhang
—
Co-founder & CEO
Ashwin Sreenivas
—
Co-founder & President
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
Introducing Voice 3 and Chord, our new speech model
Posted on
October 1, 2026
Product
Introducing Chord: a speech model built for customer conversations
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
