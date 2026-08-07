---
title: ""Agent, agent, agent": designing conversations to reduce barge"
source: "Decagon Blog"
url: "https://decagon.ai/blog/designing-conversations-to-reduce-barge"
scraped: "2026-08-07T06:00:40.467709+00:00"
lastmod: "None"
type: "sitemap"
---

# "Agent, agent, agent": designing conversations to reduce barge

**Source**: [https://decagon.ai/blog/designing-conversations-to-reduce-barge](https://decagon.ai/blog/designing-conversations-to-reduce-barge)

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
Industry
"Agent, agent, agent": designing conversations to reduce barge
Posted on
August 6, 2026
Briana Li
AI Conversation Designer
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
There's a caller every support leader knows. They found a charge they didn't recognize, dialed in, and spent a few minutes working through an IVR. By the time an AI agent picks up the conversation, they have exactly one intent: "agent, agent, agent," until a human answers.
In voice AI, this is called barge, where callers refuse to engage with the AI agent at all and simply demand a person. Most teams treat their barge rate as a fact of nature. Some share of callers will never talk to a machine, and the only question is how gracefully you escalate them. The design effort goes everywhere else, and the barge number just sits there.
We no longer believe that number is fixed. Working with a global telecom provider on billing disputes (their hardest intent), we reduced barge by over 15% in a single conversational design pass. This was done not with a new model or a better voice, but by changing what the agent said in its first few turns and whether each turn visibly served the caller.
The hardest conversation in support
Billing disputes sit near the top of any list of hard workflows, and the reasons have little to do with any one company. They're structural, and they hold for nearly every large contact center.
Enterprise voice systems often hand calls from the IVR to the AI agent seamlessly, so callers experience one continuous conversation. That continuity is a decent starting design, but it means the agent inherits whatever frustration built up before it said a word. Intent routing through an IVR is never perfect, so the agent sometimes opens pointed at a slightly different problem than the one the caller actually has. And the subject is money, so callers believe something on their bill is wrong, with their patience already spent.
Billing is also genuinely hard to do out loud. A monthly bill can carry dozens of line items: prorated charges, device installments, one-time fees, and credits. A human rep handles this by reading a screen. A voice agent has to decide which of those details matter right now, and every unnecessary one it reads is a few more seconds of an angry person's patience spent.
None of that is a failing of any team, but the shape of the problem. The agent gets no benefit of the doubt; it has to earn the caller's trust turn by turn, and the barge rate is the scoreboard.
The three changes that moved the number
Our conversational design team started the way we always do: by analyzing real conversations. We pulled a batch of production calls, flagged where each one went wrong, and defined what the ideal response would have been. That review became a golden set of target behaviors. And because Decagon enables agent behavior to be built and iterated upon as natural language instructions rather than code, the changes went live the next day as a controlled experiment.
Three changes did most of the work that we’ve since codified as guidelines for any billing workflow.
1. Say less and lead with what matters
The AI agent's answers were thorough, and that was the problem. When someone is upset about a charge, a long answer doesn't read as diligence. It reads as a filibuster.
We cut response length across the flow so the agent led with what matters most. On a billing call, those are the charges that changed since last month, because whatever made the bill go up is usually why the caller dialed. The caller will ask for more detail if they actually need it, and a crisp answer earns the follow-up question instead of the barge.
2. Stop asking questions that serve the system
The agent ended most messages with a question. On paper that looks like good engagement. In the transcripts, many of those questions weren't helping the caller toward their goal at all. They existed to keep the caller in the conversation.
Callers can tell the difference. A question that advances their problem feels like service; a question that merely prolongs the session feels like being handled. We removed every closing question that didn't move the caller forward, and replaced them with more pointed questions that helped us drive towards resolving the user's end goal.
3. Never read the bill twice
The most striking failure mode was repetition. Some conversations ran past thirty turns, with the agent replaying the same bill details again and again. Imagine hearing your own charges read back to you a third time while you're trying to dispute one of them.
The fix was giving the agent a real sense of conversational state: what it has already explained, and what remains open. Once the agent stopped repeating itself, conversations got shorter, and callers stopped treating it like a machine stuck in a loop.
That was the whole experiment: one focused review of real conversations, shipped as workflow and guideline changes in about a day, and a significant drop in barge.
What a great voice can and can’t do
If conversational design moved the number that far, it's fair to ask what the voice itself contributes. Teams deploying voice AI often start there, holding listening sessions to choose between voice profiles the way they'd cast a spokesperson.
The voice does real work. It's the first thing a caller experiences, and a voice that sounds robotic or broken will drive barge up all on its own; nobody wants to negotiate a bill with a machine they can barely understand. What the voice can't do is carry the conversation alone. It determines whether callers will listen, but not whether the agent says something worth listening to.
We've seen this in production experiments. Swapping between good voice profiles (warmer vs. flatter, male vs. female), on this deployment and others, moved the metrics very little when conversational design was stagnant. Once the voice is genuinely good, callers stop grading it and start grading the conversation. For a routine, low-stakes intent, a pleasant voice adds polish. For a caller disputing money, even the most humanlike voice explaining the wrong things at length will lose them.
None of this is an argument for neglecting the voice. The voice is your brand made audible, and it deserves real investment: callers form an impression of your company within seconds of hearing it. The argument is about proportion. Voice and conversational design are
two halves of the same experience
, and most teams budget generously for the first while leaving the second to chance. A great voice earns the caller's patience; what the agent does with that patience decides the call.
This work needs designers
Two things made a one-day turnaround possible for the telecom deployment.
The first is people. Decagon has a dedicated team of conversational design experts whose full-time job is analyzing transcripts and deciding what a great response sounds like. This isn't work a forward-deployed engineer does on the side.
The second is a platform built for iteration. In much of this market, an insight like "stop repeating the bill" becomes a ticket. It enters the vendor's backlog, waits its turn behind every other request, and ships weeks later, after the transcripts that inspired it have gone stale. Your designers' judgment is worth exactly as much as your ability to act on it while it still matters.
Decagon is built so the insight never has to leave the team that had it. Agent behavior lives in natural-language
Agent Operating Procedures
that the people reading transcripts can change themselves, and
Duet
helps them mine those conversations for the patterns worth acting on. On this deployment, the changes went live the next day, and we now run several experiments a week.
An angry caller isn't rejecting AI, but rejecting a conversation that isn't serving them. A voice agent needs to earn every turn by making the current one count.
‍
Briana Li
—
AI Conversation Designer
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
Industry
Everyone is wrong about open source AI in the enterprise
Posted on
July 9, 2026
Industry
Beyond latency: The art of building a truly great voice agent
Posted on
April 9, 2026
Industry
What we’ve learned about designing AI-ready CX teams
Posted on
March 23, 2026
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
