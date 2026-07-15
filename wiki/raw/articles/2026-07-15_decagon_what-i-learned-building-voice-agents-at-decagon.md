---
title: "What I learned building voice agents at Decagon"
source: "Decagon Blog"
url: "https://decagon.ai/blog/what-i-learned-building-voice-agents-at-decagon"
scraped: "2026-07-15T06:00:11.158300+00:00"
lastmod: "None"
type: "sitemap"
---

# What I learned building voice agents at Decagon

**Source**: [https://decagon.ai/blog/what-i-learned-building-voice-agents-at-decagon](https://decagon.ai/blog/what-i-learned-building-voice-agents-at-decagon)

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
Product
What I learned building voice agents at Decagon
Posted on
July 13, 2026
Maeneka Grewal
Associate Director, Agent Development
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
I've always been drawn to agentic voice. The pace of the competition and the industry, the complexity of all the moving components, the massive impact on the business, and, if I'm being honest with myself, because I love to talk. Build an agent that talks back to me? Sign me up.
When I got the chance to focus on it, the
Decagon Agent Development team was already rolling out agents on our other channels almost daily
. Chat, email, SMS, live and resolving real conversations like a machine. So voice should be no different, right? Not quite.
Voice is magic for the end user. No more hold music to cancel a reservation. No more pressing five numbers to check on a prescription. No more repeating yourself to four people before someone finally helps. But to the person on the line, that magic is invisible, and to the team building it, the pain didn't disappear. It transferred to us.
In the early days, we sank hundreds of hours a week into a single voice agent. Everything I knew from text channels was 10x harder here. The architecture was more complex, the information collection more nuanced, and the bar for a good experience was unforgiving. So I did what the work demanded.
To learn,
I followed our voice engineers around the office until they explained how TTS works, then begged them to join customer calls to explain it live.
To build,
we ran dozens of AOP and conversationality experiments, hunting for the one phrasing tweak that changed everything.
To test,
we bribed every Decagon employee we could into one room to replicate a call center (yes, ironic) and stress-tested every scenario we could think of. At one point I was doing my best granny accent to see how transcription held up. Voice acting may be my next calling.
To iterate,
I combed transcripts line by line and ran latency analysis that would make you pull your hair out, hunting for milliseconds to shave.
Then we shipped proactive outbound calling, and the difficulty curve went vertical. Outbound is longer, higher stakes (medication refills, collections), and the branching logic is gnarly. A bad agent interrupting your day? You hang up. An intelligent, empathetic one calling to make your day easier? Five stars. The gap between those two is small in the build and massive in the outcome.
None of it was scalable. We were shipping high-CSAT, high-deflection agents in chat and email like clockwork, but voice was different. And voice was about to be everywhere. We called what we saw coming the voice tsunami.
In December 2025, a few of us sat down to figure out how to ride it. The question was simple to ask and hard to answer: what does it actually take to build voice agents at scale? We tracked every piece of work that went into a voice launch, backfilling tickets for things we'd already shipped so we had a real picture of the lift. My teammate Kevin Liu ran the analysis that showed Agent Development and Voice Product/Eng exactly where to focus.
Then we built the system:
Tribal knowledge into playbooks.
Everything in my head, our voice architects' heads, and our conversational designers' heads, turned into guides a new ADM can ramp on in a week.
Manual config into product.
Voice customization, multilingual setup, a dozen other knobs that used to eat days of engineering time now take an ADM minutes.
Hundreds of test calls into one Duet simulations run.
We worked with voice engineering to ship the latest voice simulations, which surface the issues for us. Pair it with Duet Autopilot and the fixes land without lifting a finger.
Six months later, the whole team ships better voice agents every day. An ADM launches a voice agent on the same timeline and with the same ease as any other channel, with little to no agent engineer involved. Time-to-go-live is down ~37%. Eng hours per launch have more than halved. Better yet, customers are now building the most sophisticated outbound flows on their own.
I came to voice because I love to talk. I stayed because we turned the hardest channel we build into one anyone can. We didn't just figure out how to ride the voice tsunami. We taught everyone else how to surf it too.
Cowabunga.
Maeneka Grewal
—
Associate Director, Agent Development
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
The next generation of Simulations: testing that keeps pace with your agents
Posted on
June 30, 2026
Product
Introducing Duet Autopilot: The self-improving agent for conversational AI
Posted on
June 9, 2026
Product
QA Hub: Agent quality is a team sport
Posted on
May 28, 2026
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
