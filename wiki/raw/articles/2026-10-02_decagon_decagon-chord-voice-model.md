---
title: "Introducing Chord: a speech model built for customer conversations"
source: "Decagon Blog"
url: "https://decagon.ai/blog/decagon-chord-voice-model"
scraped: "2026-10-02T06:00:11.972039+00:00"
lastmod: "2026-10-01T17:25:01.721Z"
type: "sitemap"
---

# Introducing Chord: a speech model built for customer conversations

**Source**: [https://decagon.ai/blog/decagon-chord-voice-model](https://decagon.ai/blog/decagon-chord-voice-model)

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
Introducing Chord: a speech model built for customer conversations
Posted on
October 1, 2026
Samuel Zhang
Member of Technical Staff, Agent Orchestration
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
A voice agent only works if customers engage with it. The moment someone realizes they’re talking to a machine, they become more rigid, give less context, and start asking to speak to a human, so a problem the agent could have solved gets escalated. Our goal is the opposite: get customers to lean in and trust the agent to help. The clearest lever we found was naturalness. The more natural the voice and the back-and-forth, the more people engaged, and the more the agent could resolve.
In customer calls, people speed up and slow down, lean on certain words, shift their tone, pause to think, and drop in the occasional "um." While cloning can improve off-the-shelf voices, getting them to reproduce that natural presence is a different challenge.
We wanted a level of naturalness that nothing on the market reached. The best speech models are genuinely impressive, and we still use them across our stack. They are, however, built to support a wide range of use cases, capping how natural they can sound in a live conversation. To clear that ceiling, we built our own: Chord, a speech model we post-trained for customer conversations.
What "good" means for a customer voice
The hard part was defining the target. The industry optimizes for a clean, even read, but real conversation is the opposite. It has presence: shifting pace, natural emphasis, a tone that moves with the moment. Ironing that out is exactly what makes a voice sound synthetic, so we defined "good" as preserving that conversational presence rather than smoothing it away.
A few properties carry that presence. Pacing and energy shift with the length and meaning of a sentence. Emphasis and tone change with intent. Speech carries small imperfections, like the mid-thought pause or the occasional filler. We preserve all of it because together, it’s what a listener unconsciously reads as natural and trustworthy. We hypothesized that a human-like voice will be able to move the needle on business outcomes.
The training methodology is most of the problem
Chord starts with a dedicated pipeline we built to produce conversational data that sounds like a customer call. A typical speech-training pipeline scrubs that data clean, flattening the pacing, smoothing the delivery, and cutting the small imperfections to leave tidy, readable text. We designed ours to do the opposite and keep the full texture of how people actually talk. That texture, the shifting pace, the natural emphasis, the pauses and fillers, is what makes speech sound human, so a model trained on it learns conversational presence instead of reading like a script.
Two things made that possible. The first is a verbatim transcription approach that captures how people actually speak, faithfully preserving the pacing, emphasis, and disfluencies instead of tidying them into clean text. The second is how we capture voice talent: hand a voice actor a script and you get a performative read, so we developed a recording method that combines the content of a script with the naturalness of free-flowing conversation, capturing how a person actually sounds when they're talking, and their speech profile, in the process.
Choosing a base model to post-train
We post-trained a tokenizer-free diffusion model. Most speech models discretize audio into tokens, and every tokenization step throws information away. By representing speech without tokenizing it, Chord stays close to lossless and preserves the fine detail that separates a voice that's merely intelligible from one that sounds present. It also makes the model far more steerable: we can shape a specific emotion, pace, or emphasis with precision, which is exactly what a live customer conversation demands.
In production, Chord is served on
Modal
.
The results
We measured Chord against the definition above: a voice that sounds and stays natural across a whole interaction, and the customer outcomes that naturalness produces. Three results stand out.
Chord lifted resolution rate across different industries
The most important test is what happens on live calls. We looked at customers in telecom, financial services, and travel and hospitality who switched from an off-the-shelf voice to a voice on Chord. We compared the same programs before and after the switch, changing only the voice.
Resolution rate increased in every case: up 6.1 points for the telecom, 7.1 for the financial services provider, and 2.6 for the travel brand.
Customers also fought the voice agent less, with barge rates decreasing by 14.5, 6.1, and 5.3 points across the three. Barge rate is the share of calls where the caller's only goal is to reach a human, repeating the ask for a "representative" or similar verbiage until they get one. It drops when the voice is good enough that people are willing to work with the agent.
Approximately 90% of listeners couldn’t tell which voice was AI
We ran a blind listening test across three voices. For each, we played the same audio samples twice, once spoken by Chord and once by the voice talent it was modeled on, and asked people to pick which one was the AI.
The bar for a natural voice is: can listeners tell the AI from the real person? Results that represent a coin flip of 50-50 means they can’t. Across our sample, 45.7% of listeners believed the real human voice was the AI, close enough to 50-50 that the two were effectively indistinguishable.
Preferred over other leading voices
We also put Chord head-to-head against three other leading speech models. Same words spoken, with the only variable being the model. We asked listeners to simply choose the voice they'd most want to talk to if they were a customer chatting about a problem.
Across 185 listeners, Chord came out first overall at 36.2%, ahead of all three, and performed well in individual rounds, reaching as high as 48.4%. Against models built specifically for expressive, human-sounding speech, the voice built for conversation was the one people preferred.
What comes next
Most of the industry is still optimizing for how a voice sounds in isolation. The harder and more valuable problem for us is how a voice behaves inside a real conversation: whether it earns trust over five minutes, holds up when the call gets messy, and leaves the customer better than it found it.
Chord is the latest expression of the core bet at Decagon Labs. For customer interactions, a model fine-tuned for the specific task outperforms a general-purpose frontier model built for everything. Voice is where that difference is most audible, but it's the same approach behind the rest of our models. Owning the model is what lets us keep setting the bar for what a customer voice should sound like.
Samuel Zhang
—
Member of Technical Staff, Agent Orchestration
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
