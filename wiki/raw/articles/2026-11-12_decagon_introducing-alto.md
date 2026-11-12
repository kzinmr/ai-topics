---
title: "Introducing Alto: the voice model driving a 5+ point lift in resolution"
source: "Decagon Blog"
url: "https://decagon.ai/blog/introducing-alto"
scraped: "2026-11-12T06:00:22.999798+00:00"
lastmod: "2026-11-11T19:10:34.778Z"
type: "sitemap"
---

# Introducing Alto: the voice model driving a 5+ point lift in resolution

**Source**: [https://decagon.ai/blog/introducing-alto](https://decagon.ai/blog/introducing-alto)

Introducing Voice 3, our most advanced voice agent yet.
Hear it for yourself.
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
Introducing Alto: the voice model driving a 5+ point lift in resolution
Posted on
November 11, 2026
Quique Lores
Product Manager
Dante Everart
Speech AI Researcher
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
Last month at Decagon Dialogues, we introduced
Voice 3
, the first duplex voice agent handling customer calls in production. It combines an architecture that lets the agent listen, talk, and work at the same time with
Chord
, our speech model trained for customer conversations.
Today, we’re taking our voice agent further with Alto, a new model from Decagon Labs that powers the conversational layer of the duplex architecture. Alto determines when to speak and what to say. It knows when to answer a question, wait for confirmation, or keep the conversation moving while the agent takes action.
With Alto, our voice agent responds in about 700 milliseconds on average without relying on the generic filler statements that other systems use.
On live customer calls, Alto has increased resolution rates by 5+ percentage points
, with no other significant changes to the agent’s logic. This builds on the gains from Chord, which independently lifted resolution by up to 7 percentage points.
{{demo-cta text="Hear it for yourself" sub="Try our voice agent on the kinds of calls our customers handle every day." button="Experience Decagon Voice" link="/product/voice#demo"}}
‍
"Customers have been trained for years to speak in short fragments at these IVRs just to get through to a human. The problem is, an LLM can’t do its job without real dialogue and context. But with Decagon the voice sounds like it’s actually listening, and it keeps the conversation moving instead of going quiet while it works. People start talking to it naturally without even thinking about it. That’s what Decagon delivers."
- Christian Niedworok, Lead of Digital Service Communication at Deutsche Telekom
‍
The promise and tradeoff of duplex
Most voice agents process each turn in sequence through a cascade pipeline: transcribe, reason, then speak. A duplex agent splits that work across two models running in parallel: a fast conversational model that listens and speaks, and a more powerful reasoning model that handles complex decisions and actions behind the conversation.
Duplex brings interacting with voice agents much closer to talking with a person. Responses come faster. The agent keeps the conversation going while it works, instead of making callers wait in silence. And because part of the agent is dedicated to managing the conversation, it can be tuned to sound natural rather than like a system reading out results.
But getting a duplex agent to work well on real customer calls is hard. People interrupt, change their minds, and expect the right answer every time. For a conversation to feel natural, the agent has to be quick to respond, but smaller, faster models tend to make more mistakes.
That creates a decision on every turn: should the conversational model answer immediately or hand off to the slower reasoning model? Waiting can disrupt the flow, but answering too soon risks saying something that isn’t true, like telling a caller their reservation has been changed before the change is confirmed. The challenge is keeping the conversation natural without compromising reliability.
Alto makes conversations natural and reliable
Running our voice agent in production showed us where that tradeoff matters most, and we built Alto to address it. Its core skill is judgment: on every turn, it decides whether it can answer right away or needs to wait.
Alto continuously tracks what the caller has said and what the rest of the agent is working on. It uses that context to decide when to speak, give an update, or change course. If the agent needs a few seconds to look up information or make a tool call, Alto keeps the conversation moving, the way a person would on the phone. It grounds its responses in a shared record of the call, waiting for confirmation before telling a caller an action is complete.
Most voice agents fill the wait with, “Got it, one moment.” Alto puts that time to use. While a lookup runs, it can ask for the next piece of information it needs or check in with the caller. If the result comes back just as the caller asks something new, Alto answers the question and shares the result in the same reply, just as a human agent would.
How we trained Alto
Instructions alone can only take a model so far. To make Alto both natural and reliable, we trained it specifically for customer conversations.
We started with a small open-weight model to keep responses fast, then fine-tuned it on simulated calls informed by what we’d learned in production. Next came reinforcement learning. At each point in a conversation, the model generated several possible responses. We scored each one first on whether it correctly chose to answer or wait, then on whether its wording followed the business’s policies and reflected confirmed information.
The hardest part was finding examples that would help the model improve, because it already handled most situations correctly. We focused on cases where the right decision was less obvious and varied the policies and tools across simulated businesses. That helped Alto learn judgment it could apply across different situations, rather than memorize one company’s script.
Before any caller heard it, Alto was tested across more than 90 million simulated calls. It then ran in shadow mode alongside live production traffic, allowing us to evaluate its responses without having it speak to callers.
Specialized models for customer conversations
Alto is the latest model from
Decagon Labs
, and it follows the same principle as Chord: a model trained for one specific job will outperform a general-purpose model in customer conversations. Chord shapes how our agents sound; Alto shapes how they hold a conversation.
See how our agent handles your conversations
here
, or
set up some time
with us to learn more.
Quique Lores
—
Product Manager
Dante Everart
—
Speech AI Researcher
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
How we taught our agents to recognize other agents
Posted on
November 10, 2026
Product
Hypothesis: Autopilot is better than ever. Results: Tested and validated.
Posted on
November 5, 2026
Product
Introducing Experiment Hub: the latest experimentation platform on Decagon
Posted on
October 22, 2026
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
