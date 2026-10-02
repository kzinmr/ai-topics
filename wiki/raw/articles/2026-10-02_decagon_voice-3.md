---
title: "Introducing Voice 3 and Chord, our new speech model"
source: "Decagon Blog"
url: "https://decagon.ai/blog/voice-3"
scraped: "2026-10-02T06:00:12.649146+00:00"
lastmod: "2026-10-01T17:25:01.914Z"
type: "sitemap"
---

# Introducing Voice 3 and Chord, our new speech model

**Source**: [https://decagon.ai/blog/voice-3](https://decagon.ai/blog/voice-3)

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
Introducing Voice 3 and Chord, our new speech model
Posted on
October 1, 2026
Quique Lores
Product Manager
Ariana Xiang
Senior Product Marketing Manager
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
Today we're introducing
Voice 3
, our most advanced voice AI agent yet. Voice 3 launches alongside
Personal Agent Gateway
,
Agent Modules
, and
Duet Apprentice
at
Decagon Dialogues
.
Voice is the hardest channel to get right and the least forgiving when you don't. Customers notice every interruption and unexplained silence, and the way most voice agents are built makes both likely.
Voice 3 speaks through
Chord,
the first voice model trained by
Decagon Labs
specifically for customer conversations. It also now runs on a
new duplex architecture
that lets the agent listen, speak, and act at the same time. Together, they make conversations more natural and let agents take on more sophisticated, long-running interactions, in any of 70+ languages.
"Customers have been trained for years to speak in short fragments at these IVRs just to get through to a human. The problem is, an LLM can't do its job without real dialogue and context. But with Decagon the voice sounds like it's actually listening, and it keeps the conversation moving instead of going quiet while it works. People start talking to it naturally without even thinking about it. That's what Decagon delivers."
- Christian Niedworok, Lead of Digital Service Communication at Deutsche Telekom
‍
Built for a call instead of a script
Most voice agents sound stiff on a live call because the models behind them were built to handle a range of use cases, from narrating a book to voicing over video games, rather than handle the breath, hesitation, and natural pauses of conversation. We built our own model to fine tune the voice specifically for customer conversations.
Chord
is our first voice model, developed by Decagon Labs and post-trained on real-world CX conversations. The model shapes speech phrase by phrase, slowing down for a confirmation code or phone number, then returning to a conversational pace, rather than relying on one global speed setting.
Below are three pairs of recordings. In each pair, one voice is a real person and the other is that same voice run through Chord.
Voice 1
0:00 / 0:20
Human
0:00 / 0:20
Chord
Voice 2
0:00 / 0:20
Human
0:00 / 0:20
Chord
Voice 3
0:00 / 0:20
Human
0:00 / 0:20
Chord
In a blind test across these three voices, we asked listeners to pick the human in each pair. The results showed that on average, approximately 90% of users couldn’t tell.
The familiar controls to customize the voice to your brand also carry over too: voice selection, pronunciation of business-specific terms, and delivery tuned to the business.
Chord is trained on licensed data and consented voice talent, never on customer-owned data. To learn more about Chord, check out
this blog
.
A conversation shouldn’t stop while the agent works
Most voice agents run on a cascaded pipeline: speech-to-text transcribes the caller, an LLM decides how to respond, and text-to-speech speaks the response. Each stage adds delay, and coordinating them makes natural turn-taking difficult. A simple “mhm” can trigger an interruption, and a long lookup can leave the caller listening to silence. For the end user, that means talking
to
an agent: telling it what to do, one command at a time.
Voice 3 removes that friction using a new duplex architecture with two layers running in parallel. A low-latency conversational model handles the listening and speaking, from answers to progress updates. A more powerful model handles the reasoning, tool calling, and guardrail enforcement happening behind the conversation.
What this unlocks is an entirely new experience in conversation. Now, you can actually talk
with
the agent. The agent handles several things at once without losing the thread, so you can ask a follow-up question while it’s still working. It gives quick progress updates when something takes a few seconds, while helping you with other smaller requests. It responds faster, phrases things more naturally, and works with you to figure out what you need.
Decagon Voice sounds local everywhere
Our customers serve people around the world, and every caller should feel like the agent speaks their language. That takes more than translation. Dialect, cultural norms, and local expectations all inform what sounds natural.
Decagon supports 70+ languages without requiring teams to build a separate agent for each. It detects the caller’s language and switches automatically, even when callers move between languages mid-sentence. Locale-specific voices reflect how people speak in each market, and every language is validated by native speakers before it ships.
Specialized intelligence, better conversations
General-purpose models are invaluable when you’re still discovering what a use case requires, but production experience brings the problem into focus. What’s needed then is a model trained to do a particular job exceptionally well.
That’s the philosophy behind Decagon Labs. We continue to build on leading models while developing specialized models for the demands of customer experience. Chord brings the approach to voice, turning what we’ve learned from customer conversations into speech built for them. As agents take on more of the customer journey, that depth of expertise becomes even more valuable.
Want to hear Voice 3 for yourself?
Book a demo
.
Quique Lores
—
Product Manager
Ariana Xiang
—
Senior Product Marketing Manager
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
