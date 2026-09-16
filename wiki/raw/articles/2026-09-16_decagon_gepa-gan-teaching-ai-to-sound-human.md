---
title: "GEPA-GAN: Teaching AI to sound human"
source: "Decagon Blog"
url: "https://decagon.ai/blog/gepa-gan-teaching-ai-to-sound-human"
scraped: "2026-09-16T06:00:38.221077+00:00"
lastmod: "2026-09-15T23:24:28.976Z"
type: "sitemap"
---

# GEPA-GAN: Teaching AI to sound human

**Source**: [https://decagon.ai/blog/gepa-gan-teaching-ai-to-sound-human](https://decagon.ai/blog/gepa-gan-teaching-ai-to-sound-human)

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
Research & Technology
GEPA-GAN: Teaching AI to sound human
Posted on
September 15, 2026
Roy Wang
Member of Technical Staff, Research
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
At Decagon, customer-support agents are often evaluated against simulated users. That makes the simulator part of the benchmark: if the simulated customer is cleaner, more patient, or more cooperative than a real person, the agent is being tested on an easier problem.
This blog explores whether adversarial prompt optimization can make simulated users harder to distinguish from real customers. The method pits two language-model programs against each other. A generator produces the next user turn; a judge receives both the real continuation and the synthetic response, in randomized order, and tries to identify which is which. GEPA—a reflective prompt optimizer that turns natural-language analysis of execution traces into candidate prompt updates—then revises both programs’ instructions based on their failures [1].
A GAN-like game for prompt optimization
The system contained three roles:
A
generator
read the conversation and produced the next user message.
A
judge
saw one real response and one generated response in randomized A/B order, then selected the real one.
A
reflector
analyzed failures and helped GEPA propose new prompts for each side.
Optimization alternated between the two competitors. The judge prompt was optimized to improve detection accuracy. The generator prompt was optimized to increase the chance that the judge selected the synthetic response.
The setup follows the core adversarial idea introduced by GANs: a generator tries to produce outputs that a discriminator cannot distinguish from real data, forming what Goodfellow et al. call a “minimax two-player game” [2]. Our implementation is GAN-like rather than a neural GAN: no model weights changed, and GEPA searched over the generator and judge instructions.
That distinction makes the system unusually inspectable. Instead of learning hidden parameters, it produces a sequence of prompts that can be read, compared, and criticized.
Experimental setup
We ran the generator and judge through 11 optimization checkpoints, shown alongside the seed baseline at checkpoint 0.
The preference judge’s accuracy and the generator’s fool rate were complements on the same A/B comparisons. If the judge chose the wrong response, the generator received credit.
The dynamics were highly non-monotonic:
Judge accuracy and generator fool rate are complementary; prompt length is shown on the right axis.
Checkpoint 9 reached a 44% internal fool rate, but checkpoint 11 fell back to 30%. Over the same span, the generator prompt more than doubled in length.
The non-monotonic series is consistent with a moving-target game: improving one side changes the task faced by the other. But sample composition and stochastic generation also changed between iterations.
What changed in the prompt
The initial checkpoint created by frontier LLM in one shot was already substantial. Its 3,079-character prompt asked for the immediate next turn, encouraged practical follow-up questions, mirrored the user’s tone, and discouraged replies that were too polished.
GEPA further expanded from this. By checkpoint 9, the instructions had become more explicit about:
preserving the user’s language, casing, punctuation, and emotional state;
answering only part of a forced-choice question—or ignoring it;
repeating the central complaint when the requested detail was unavailable;
preferring short UI labels, transaction descriptions, and error strings;
introducing no more than a couple of new details;
avoiding support-like phrasing;
The prompt also accumulated more customer- and domain-specific patterns. That made the instructions concrete, but it introduced another risk: unconstrained prompt search can become a catalog of dataset details rather than a compact, transferable model of behavior. Prompt length is not just a deployment concern; it can be a signal that optimization is trading generality for memorization. We found length penalty to be a useful regularization technique in general when using GEPA.
Human evaluation
We asked human annotators to review randomized A/B pairs containing one real user response and one generated response using the prompt behind the final generator checkpoint, then label which response they believed was AI-generated. The human fool rate measures how often the generated response was mistaken for the real one.
The iterated prompt achieved a 34% human fool rate, compared with 30% for the seed prompt. The randomized comparison gives us a direct human measure of realism and shows that the optimized prompt moved in the intended direction.
Takeaway
Adversarial GEPA was valuable here because it transformed an underspecified goal—“sound like a real user”—into an inspectable set of behavioral hypotheses.
The main lesson is methodological: adversarial optimization can be a powerful way to discover failure modes and improve prompts, but realism must be validated outside the game.
Furthermore, no additional model fine-tuning was required. In our setup, GEPA only rewrote the generator and judge prompts while keeping the underlying models fixed. This made the experiment computationally efficient and operationally simple: each checkpoint was just a new pair of text instructions, with no training jobs, weight updates, or new model artifacts to manage.
References
[1] Agrawal et al. “
GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning
.” ICLR, 2026.
[2] Goodfellow et al. “
Generative Adversarial Networks
.” NeurIPS, 2014.
Roy Wang
—
Member of Technical Staff, Research
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
Research & Technology
DuetBench-2: Measuring agent self-improvement in production
Posted on
September 9, 2026
Research & Technology
How we made one of our largest inference workloads 4.7× more GPU-efficient
Posted on
September 3, 2026
Research & Technology
Audio-native semantic speaker-change detection
Posted on
September 3, 2026
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
