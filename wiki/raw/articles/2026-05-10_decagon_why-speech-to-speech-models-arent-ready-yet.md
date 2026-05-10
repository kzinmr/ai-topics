---
title: "Why speech-to-speech models aren’t ready for the enterprise (yet)"
source: "Decagon Blog"
url: "https://decagon.ai/blog/why-speech-to-speech-models-arent-ready-yet"
scraped: "2026-05-10T01:19:51.825352+00:00"
lastmod: "None"
type: "sitemap"
---

# Why speech-to-speech models aren’t ready for the enterprise (yet)

**Source**: [https://decagon.ai/blog/why-speech-to-speech-models-arent-ready-yet](https://decagon.ai/blog/why-speech-to-speech-models-arent-ready-yet)

Introducing Proactive Agents.
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
Build
AOPs
Workflows for AI agents
Integrations
Support tool connectors
Optimize
Experiments
Live A/B testing
Testing & QA
Simulations at scale
Scale
Insights & Reporting
Voice of the Customer
Watchtower
Always-on QA
Suggestions
AI-powered knowledge
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
AI and the next generation of customer experience
Why exceptional service is the new brand differentiator as AI reshapes consumer expectations.
Spring ’26 Release: Proactive Agents
See how user memory, outbound voice, and Agent Workbench can help you build stronger customer relationships
Company
About
Careers
Security
Sign in
Sign in
Get a demo
Sign in
Get a demo
Product Update
Company news
Technology & research
Industry
Technology & Research
Blog
/
Why speech-to-speech models aren’t ready for the enterprise (yet)
Why speech-to-speech models aren’t ready for the enterprise (yet)
October 16, 2025
Written by
Dennis Cui
Share to
Copy link
Table of contents
Example h2
Subscribe to our newsletter
Get monthly updates with our latest articles, podcasts, videos, and more.
Voice
is quickly becoming the next major interface for customer experience. It’s the most natural and intuitive way for people to communicate, fitting seamlessly into how customers already engage with their favorite brands.
In that context, speech-to-speech (S2S) models have captured a lot of excitement. These models promise real-time, expressive conversations that sound genuinely human, capable of inflecting tone, emotion, and cadence in a way that text-based systems cannot. Unlike traditional
speech-to-text → language model → text-to-speech
pipelines, S2S models operate directly on audio, skipping the transcription and synthesis steps entirely.
This generally makes them faster and more fluid, which is ideal for demos where “good” is defined by voice quality, tone, and naturalness. Moving from a demo to an enterprise deployment, however, is a very different challenge. For production use cases, success isn’t just about how natural the system sounds but also how reliably and accurately it executes workflows.
The challenges taking speech-to-speech models to production
Speech-to-speech models represent a remarkable technical achievement, but their current limitations become clear in enterprise settings. These systems struggle with three critical requirements for production deployment: reliability, factual accuracy, and cost efficiency.
Reliability
Enterprises depend on systems that behave predictably, so they need AI agents that follow defined workflows explicitly. Speech-to-speech models, while expressive, often struggle with this kind of precision. It’s difficult to enforce consistent behavior; their smaller, streamlined architectures make them faster, but also more prone to mistakes when precision matters most.
This variability becomes especially risky in sensitive workflows. Models optimized for conversational fluidity can skip steps entirely, creating inconsistent or unsafe outcomes that erode customer trust.
Hallucinations and factual accuracy
Speech-to-speech models also tend to
hallucinate
more than traditional text-based systems. Without an intermediate text layer, it’s difficult to insert guardrails or validation steps without adding latency, which makes it harder to balance real-time responsiveness with reliability.
Because these models blend tone and meaning into a single representation, they sometimes “fill in” implied details or paraphrase incorrectly, prioritizing smooth delivery over factual precision. In high-stakes enterprise workflows, that behavior is risky.
Cost efficiency
Finally, cost remains a major constraint. Speech-to-speech models process tokens for every slice of audio (not just words), so they consume more compute than text-only systems. What might be a few tokens of text can become dozens in speech, since pauses, inflections, and background noise all add up.
At enterprise scale, that token expansion compounds quickly. For deployments handling thousands of concurrent calls, the cost difference becomes substantial, making S2S models difficult to justify for production use today.
Why guardrails are critical for AI agents
For most enterprises, the challenge is achieving both low latency and high reliability, not one or the other. The traditional
speech-to-text → language model → text-to-speech
pipeline introduces more latency than speech-to-speech models, but that structure is what makes enterprise voice agents predictable, auditable, and safe.
In practice, that “middle layer” is often more than a single language model. It’s a system of models orchestrated together to execute workflows while enforcing
critical guardrails
. These include things like:
Ensuring instructions are followed explicitly and no steps are skipped
Catching hallucinations before they’re spoken to a customer
Detecting bad actors before sensitive actions are taken
Escalating high-risk or sensitive conversations to human agents when appropriate
Those guardrails inevitably add a few hundred milliseconds, but they’re non-negotiable for use cases across
financial services
,
retail
,
travel and hospitality
, or any other industry.
Some of the voice demos circulating online sound instantaneous because they minimize or remove those safeguards entirely. They optimize for perceived speed and naturalness rather than operational reliability. But once the same systems are deployed in production, performance often suffers: accuracy drops, workflows break, and customers lose trust.
The reality is that guardrails are what make voice agents viable for mission-critical workflows, not what hold them back. And from the end user’s perspective, what matters most is whether the agent understands their intent, follows the right steps, and resolves their problem reliably.
Achieving low latency without compromising reliability
Speech-to-speech models are advancing quickly and will no doubt play an important role in the future of voice AI. Their ability to capture tone, emotion, and nuance makes them an exciting direction for the field. But for now, enterprises still need systems that balance speed with reliability and deliver exceptional customer experiences at scale.
With
Decagon Voice 2.0
, we’ve made deep optimizations across every layer of the voice stack to achieve that right balance. Generation latency is now 65% faster, enabling responses that flow as naturally as talking to another person. Fine-tuned models boost both responsiveness and accuracy, while improved prosody in streaming generation produces speech with human-like rhythm and emphasis. On the infrastructure side, deploying key pipeline components within the same cloud regions has cut round-trip times dramatically.
The results are agents that smoothly navigate background noise, interruptions, and customers who change direction mid-sentence. Conversations stay crisp, fluid, and on track, without sacrificing the precision, auditability, and control that Decagon is known for and enterprises depend on.
Book a demo
with us today to see the next generation of our voice agents in action.
Recent posts
Bringing the AI concierge to Australia
Decagon is opening a new office in Sydney, Australia
Introducing automatic optimization and Root Cause Analysis
Today, we’re excited to announce two new capabilities to help you rapidly improve your agent’s performance.
Bringing Decagon’s AI concierge solution to Google Cloud Marketplace
We're excited to announce that Decagon is now available on Google Cloud Marketplace.
Deliver the concierge experiences your customers deserve
Get a demo
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
