---
title: "Everyone is wrong about open source AI in the enterprise"
source: "Decagon Blog"
url: "https://decagon.ai/blog/everyone-is-wrong-about-open-source-ai-in-the-enterprise"
scraped: "2026-07-10T06:00:50.885241+00:00"
lastmod: "None"
type: "sitemap"
---

# Everyone is wrong about open source AI in the enterprise

**Source**: [https://decagon.ai/blog/everyone-is-wrong-about-open-source-ai-in-the-enterprise](https://decagon.ai/blog/everyone-is-wrong-about-open-source-ai-in-the-enterprise)

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
Industry
Everyone is wrong about open source AI in the enterprise
Posted on
July 9, 2026
Jesse Zhang
Co-founder & CEO
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
The prevailing story right now is that open source is eating the enterprise. The capability gap between the best closed and open models has shrunk to low single digits. A third of the Fortune 500 has verified accounts on Hugging Face, Chinese labs are shipping frontier-adjacent models with open weights every few weeks, and the inference providers are ripping.
Meanwhile, at Decagon, we now run ~90% of our workloads on open source models instead of OpenAI or Anthropic. This is consistent with most of the hypergrowth app companies and we’re seeing the big enterprises we work with move this direction as well.
And yet enterprise spend as a whole is moving the opposite direction. Open source models just fell to 11% of enterprise LLM spend, down from 19% a year ago.
The trend is actually moving the other way compared to the popular narrative. Why is this and what does it mean for the future?
First, some context on why we're 90% open source. It wasn't cost, and it wasn't because our customers demanded it (though they don't mind it). It was because we had no other option.
When you're running AI agents in production for customer service, latency makes or breaks the product. A conversation where every turn takes 8 seconds is not a product anyone will use. So you need small, fast models. Each model call does not need to know the capital of Lithuania or high school physics.
But small models out of the box aren't good enough for the quality bar our customers hold us to. They only get there through heavy fine-tuning on the exact task. The frontier labs don't really sell this combination. You can't fine-tune their best models the way we need to, and their small models aren't ours to shape. Small + fine-tuned means open weights. The cost savings are real but secondary, and enterprise comfort with self-hosted models is a nice side effect, not the reason.
So why is a company like ours 90% open source while the broader enterprise number is going down?
The answer is use case maturity. When a use case is new, you want the smartest general-purpose model you can get. You don't know the shape of the problem yet, so you pay a premium for intelligence you may not end up needing. That's the right trade at that stage. But once the use case is fully built out, when you know the distribution of inputs, the behaviors you need, and the failure modes to guard against, the trade flips. Now general intelligence is overhead, and you want the smallest, fastest model fine-tuned to do your specific thing extremely well.
Customer service happens to be one of the most obvious AI use cases in the industry. Well-understood workflows, enormous conversation volume, tight quality bars. Which means companies like us are simply further along the curve than the average enterprise deployment.
And that's the resolution to the paradox. The reason open source share fell isn't that open source is losing. It's that enterprise AI as a whole is at the very beginning of the maturity curve. Last year enterprises stopped building and started buying, and thousands of brand new use cases spun up at once. New use cases run on frontier models, so closed share exploded. The 11% is a denominator problem: the pool of immature use cases is growing faster than the pool of mature ones.
If that's right, then every use case being prototyped on a frontier model today is a future open source migration. As deployments mature, companies will do what we did: distill, fine-tune, specialize. The frontier labs will keep owning discovery. Open source will increasingly own production.
However, this will take longer than people think. Most use cases are just not at the point where the “shape” of the agent is finalized such that it makes sense to start fine-tuning open source models.
Fine-tuning takes effort, and most organizations don’t have the resources or expertise to do it. The use case would have to be very high ROI and already fully deployed at scale for it to be worth it. You also need enough data to make sure the smaller models can perform at the same level as the frontier ones at a given task.
Otherwise, it’s just way easier to plug in one of the frontier closed-source models. You don’t have to worry about owning any of the infrastructure and you get the freedom to iterate and experiment freely.
Therefore, the share of LLM spend on open source will eventually inflect up but it won’t happen for many years.
Jesse Zhang
—
Co-founder & CEO
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
Beyond latency: The art of building a truly great voice agent
Posted on
April 9, 2026
Industry
What we’ve learned about designing AI-ready CX teams
Posted on
March 23, 2026
Industry
AI agents are never done: The new build-vs-buy calculus
Posted on
February 12, 2026
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
