---
title: "Announcing Sonic: a low‑latency voice model for lifelike speech - Cartesia"
source: "Cartesia Blog"
url: "https://cartesia.ai/blog/sonic"
scraped: "2026-05-10T01:19:31.059685+00:00"
lastmod: "None"
type: "sitemap"
---

# Announcing Sonic: a low‑latency voice model for lifelike speech - Cartesia

**Source**: [https://cartesia.ai/blog/sonic](https://cartesia.ai/blog/sonic)

Meet Sonic-3: the best text-to-speech for voice agents
|
Learn more
Meet Sonic-3: the best text-to-speech for voice agents
|
Learn more
Sonic-3: the best text-to-speech for voice agents
Models
new
Agents
Solutions
Resources
Pricing
Contact sales
Sign in
Start for Free
Start for Free
May 31, 2024
·
Research
Announcing Sonic: a low‑latency voice model for lifelike speech
Announcing Sonic: a low‑latency voice model for lifelike speech
Karan Goel
We founded Cartesia to build long-lived real-time intelligence for every device, starting with a kernel of architectural innovation: state space models. We're releasing Sonic, our low-latency voice model that generates lifelike speech today.
Building Real-Time Intelligence
Imagine a world where AI is unbelievably efficient: Processing any-sized contexts, running on any device in the world, and natively processing any modality in real-time. This is a world where intelligence is ubiquitous and long-lived, converses with us to help us understand and navigate our surroundings, and operates independently to solve complex problems for us. In this world, everyone can access, control and execute instant intelligence, personalized and private to their needs.
Our belief is that this future requires fundamentally new architectures for intelligence. Today's models fall far short of the standard set by human intelligence. Not only do they not understand the world with the detail that we do, they're slow and expensive in a way that has hegemonized their development and dissemination to large companies. Not even the best models can continuously process and reason over a year-long stream of audio, video and text—1B text tokens, 10B audio tokens and 1T video tokens—let alone do this on-device. Shouldn't everyone have access to cheap intelligence that doesn't require marshaling a data center?
Making this vision a reality is our life's work. Over the last 4 years, our co-founders Albert and Karan worked together to create a new paradigm, the "state space model" or "SSM", which offers a fundamentally more efficient approach to building AI models. State space models provide an elegant foundation for training efficient real-time models that can natively stream in information—just like humans. State space models like S4 and Mamba, originally developed by our team (with the inimitable Tri Dao) in academia, are now being rapidly adopted across the world and inspiring a new generation of work from other labs in academia and industry—from variants for vision, robotics and biology, to language models in industry (Jamba, Zamba and others). These models provide a glimpse into a future where AI can be far more efficient and accessible than ever.
At Cartesia, we're obsessed with optimizing the efficiency of intelligence—making it faster, cheaper and easier to access for everyone. We're building the platform to power long-lived real-time intelligence that runs on every device.
Real-time intelligence will have many forms, and the first goal we're building towards is real-time conversational AI with long-lived memory. This is a new computing platform where models natively converse and understand audio, have a long-term memory of interactions and can take action to solve problems. We're excited about how this platform will enable new experiences, from real-time gaming to customer support, and we're reporting initial progress in our development below.
Low-Latency Models for High-Resolution Modalities
Latency is a major challenge in building real-time intelligence. Models should respond instantly when presented with an input. We've made progress in developing new state space model architectures that enable efficient, low-latency generation of modalities like audio and video at high-resolution. In line with building real-time conversational AI, we've been experimenting with and scaling our approach on speech and audio to start.
In experiments so far, we've found that we can simultaneously improve model quality, inference speed, throughput, and latency compared to widely used Transformer implementations for audio generation. A parameter-matched Cartesia model trained on Multilingual Librispeech for one epoch achieves 20% lower validation perplexity. On downstream evaluations, this results in a 2x lower word error rate and a 1 point higher quality score (out of 5, as measured on the NISQA evaluation). At inference, it achieves lower latency (1.5x lower time-to-first-audio), faster inference speed (2x lower real-time factor), and higher throughput (4x).
We'll be releasing more detail on our new architecture in a separate report.
Sonic: Low-Latency Voice Generation
We've used this architecture to train a new voice model called Sonic that we're releasing today. Sonic creates high quality lifelike speech for any voice with a model latency of 135ms—the fastest for a model of this class.
We've built and optimized our own state space model inference stack to enable us to serve Sonic with low latency and high throughput—enabling us to serve high quality models at lower costs. Sonic is released with a web playground and low latency API. The playground features a diverse voice library for applications across customer support, entertainment, and content creation with support for instant cloning and voice design (speed, emotion), all of which can be used through the API.
You can sign up and try it here. If you're interested in partnering with us to build real-time conversational AI, reach out to us on this form, and we'd be glad to chat.
What's Coming Next
Zooming out, our larger agenda is to enable developers and businesses to build and run real-time multimodal experiences on any device. Audio is just the beginning—we want our models to instantly understand and generate any modality. We'll be bringing natively multimodal, real-time intelligence to every modality over the next year.
(And stay tuned for an exciting open-source release soon that we think developers will love.)
Hiring
If you're excited about our mission to bring real-time multimodal intelligence to every device, we'd love to hear from you at join@cartesia.ai.
Related articles
Related articles
Sep 24, 2025
·
News
Cartesia achieves GDPR compliance
Aug 19, 2025
·
News
Introducing Line: The Modern Voice Agent Development Platform
Jul 11, 2025
·
Research
Hierarchical modeling
Sep 24, 2025
·
News
Cartesia achieves GDPR compliance
Aug 19, 2025
·
News
Introducing Line: The Modern Voice Agent Development Platform
Real-time, multimodal intelligence for every device.
Models
Sonic
Ink
Agents
Solutions
Customer service
Localization
Recruiting
Sales
Finance
Healthcare
Gaming
Hospitality
Regions
Asia pacific
Brazil
China
India
Japan
Korea
Latin America
Middle East
North America
Western Europe
Eastern Europe
Resources
Blog
Customers
Docs
Events
Pricing
Research
Support
Company
About
Careers
Legal
Terms of Service
Privacy
Acceptable Use
Cookie Settings
Real-time, multimodal intelligence for every device.
Models
Sonic
Ink
Agents
Solutions
Customer service
Localization
Recruiting
Sales
Finance
Healthcare
Gaming
Hospitality
Regions
Asia pacific
Brazil
China
India
Japan
Korea
Latin America
Middle East
North America
Western Europe
Eastern Europe
Resources
Blog
Customers
Docs
Events
Pricing
Research
Support
Company
About
Careers
Legal
Terms of Service
Privacy
Acceptable Use
Cookie Settings
Real-time, multimodal intelligence for every device.
Models
Sonic
Ink
Agents
Solutions
Customer service
Localization
Recruiting
Sales
Finance
Healthcare
Gaming
Hospitality
Regions
Asia pacific
Brazil
China
India
Japan
Korea
Latin America
Middle East
North America
Western Europe
Eastern Europe
Resources
Blog
Customers
Docs
Events
Pricing
Research
Support
Company
About
Careers
Cookie Settings
Legal
Terms of Use
Privacy
Acceptable Use
