---
title: "How we taught our agents to recognize other agents"
source: "Decagon Blog"
url: "https://decagon.ai/blog/how-we-taught-our-agents-to-recognize-other-agents"
scraped: "2026-11-11T06:00:34.796638+00:00"
lastmod: "2026-11-10T19:50:47.670Z"
type: "sitemap"
---

# How we taught our agents to recognize other agents

**Source**: [https://decagon.ai/blog/how-we-taught-our-agents-to-recognize-other-agents](https://decagon.ai/blog/how-we-taught-our-agents-to-recognize-other-agents)

The first episode of the The Agent Room debuts 11/18.
Register today
Product
Product overview
Channels
Voice
Human-like conversation
Chat
Safe, on-brand replies
Emails
Contextual resolutions
Duet
AI partner to build self-improving agents
Build
AOPs
Workflows for AI agents
Integrations
Pre-built connectors
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
Personal agents are here. Meet them on your terms.
Detection of personal agents and a dedicated channel to serve them, with permissions you control.
See what it can do
Industries
Financial services
Trust in every interaction
Travel & hospitality
Smoother trips and stays
Healthcare
Simpler access to care
Technology
Better experiences at scale
Retail
Personalized shopping journeys
Telecommunications
Effortless service and connection
Insurance
Claims without the complexity
Customers
Resources
Resource Hub
Blog
Product news and research
Decagon University
Platform courses and training
Videos
Conversations with AI leaders
Glossary
AI and CX terms
Guides
Insights and best practices
Explore launches at Dialogues
Voice 3, Modules, and Duet Apprentice.
Company
About
Our mission and team
Trust Center
Security and compliance
Careers
Open roles
Partnerships
Who we’re working with
LinkedIn
X
Sign in
Get a demo
Sign in
Get a demo
Product
How we taught our agents to recognize other agents
Posted on
November 10, 2026
Thomas Moreno
Senior Agent Product Manager
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
Personal agents are already calling and messaging support teams to book, cancel, price match, and negotiate on a customer’s behalf. Before a business can decide how to handle these conversations, it needs to know who (or what) is on the other end.
Recognizing a personal agent turns out to be a hard technical problem. Deepfake detectors built for clean recordings struggle with phone audio, natural writing makes agents hard to spot in chat, and agent behavior keeps evolving. Existing tools also tend to treat every automated caller as a threat, overlooking agents that are often acting for real customers who need service.
We built our own detection models for voice and chat as part of our
Personal Agent Gateway
, which combines detection with a dedicated personal agent channel. On held-out phone audio, our voice detector catches 95% of AI voices, returning a verdict in a fraction of a second.
Voice: why we built our own detector
The off-the-shelf deepfake detectors we tested performed little better than chance on phone-quality audio, and some flagged most real callers as fakes. We built our own model, trained on how phone calls actually sound, to check every call in two independent ways:
Synthetic voice detection
assesses whether the caller sounds human or machine-generated using signals across the conversation rather than a single moment, helping to limit false positives.
Trusted agent recognition
matches callers against a curated, continuously reviewed library of known personal AI agents.
On held-out phone audio, the detector catches 95% of AI voices, compared with 73% for a general-purpose multimodal LLM. It also returns a verdict roughly 30× faster than that LLM. Precision exceeds 99%, and businesses can tune sensitivity to their tolerance for false positives, from flagging 1 in 100 real callers to 1 in 2,500.
Chat: how agents type gives them away
Agents write naturally enough that text alone is a poor signal. How they use the chat box is more revealing: text appearing without keystrokes, perfectly regular reply delays, inhuman typing speeds, and pointer movements no human hand would produce. We combine these behavioral signals with a few language cues into a single probability score.
When that score crosses a threshold, the business chooses how to respond: record the detection, end the chat, or ask, “Are you an AI assistant acting on someone’s behalf?” Legitimate agents generally identify themselves when asked. This approach allows us to detect personal agents in chat with 99% precision and 85% recall.
Agents evolve. Detection has to keep up.
Personal agents are getting better at acting human. Within weeks of launch, we watched one agent change how it typed, weakening a signal our detector relied on. As agents become harder to distinguish from people, detection remains an active area of investment for Decagon. We keep retraining our models on new signals as they emerge in production.
It’s also why we invest in partnerships with personal agent providers. A well-intentioned agent that identifies itself through the personal agent channel never needs to be caught. Detection helps businesses recognize those that arrive without an introduction.
From recognizing agents to serving them
Once a business sees agent traffic, the next question is how to serve it. Which actions should an agent be allowed to take? When should it reach a human representative? How should the business handle repeated requests for the same concession? Our
guide to serving personal agents
offers practical principles for making those decisions.
The
Personal Agent Gateway
helps businesses put those policies into practice, moving from recognizing agents to serving them through a dedicated channel. Businesses define which workflows agents can use and when to escalate, while verifying what the customer has authorized.
Personal agents will not stay a novelty. Before long, a meaningful share of support conversations will have AI on both sides, making it essential for businesses to recognize agent traffic and choose how to respond now.
Reach out to us
to see what personal agent traffic looks like across your channels.
Thomas Moreno
—
Senior Agent Product Manager
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
Hypothesis: Autopilot is better than ever. Results: Tested and validated.
Posted on
November 5, 2026
Product
Introducing Experiment Hub: the latest experimentation platform on Decagon
Posted on
October 22, 2026
Product
Introducing the Personal Agent Consent & Trust Protocol (PACT)
Posted on
October 6, 2026
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
Healthcare
Telecommunications
Insurance
Resources
Customers
Resources Hub
Glossary
Company
About
Careers
Partnerships
Privacy Policy
Security
Contact Sales
Contact Support
©
0000
Decagon. All rights reserved.
