---
title: "How we made one of our largest inference workloads 4.7× more GPU-efficient"
source: "Decagon Blog"
url: "https://decagon.ai/blog/gpu-efficient-inference-serving-stack"
scraped: "2026-09-09T06:00:05.269728+00:00"
lastmod: "2026-09-04T10:13:34.525Z"
type: "sitemap"
---

# How we made one of our largest inference workloads 4.7× more GPU-efficient

**Source**: [https://decagon.ai/blog/gpu-efficient-inference-serving-stack](https://decagon.ai/blog/gpu-efficient-inference-serving-stack)

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
How we made one of our largest inference workloads 4.7× more GPU-efficient
Posted on
September 3, 2026
Nick Liu
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
The biggest gains didn’t come from a single inference optimization. They came from removing bottlenecks across the serving stack.
At @DecagonAI, that process led to a
4.7× improvement
in fleet-level GPU efficiency on one of our largest scheduled inference workloads
Our baseline was a conventional autoscaling deployment. The optimized stack paired higher-memory GPUs with three serving changes:
disaggregating prompt processing from token generation, adding an admission controller to manage traffic bursts, and reducing the time it takes new GPU capacity to become useful
.
Requests arrive in bursts, and individual request latency is not critical. The goal is to finish the work within a bounded window while maximizing GPU efficiency, defined as tokens processed per GPU-hour.
We count GPU-hours across the full autoscaling lifecycle, including startup, idle capacity, steady-state processing, and queue drain.
Specialize prefill and decode
Prefill/decode disaggregation has become a prominent direction in high-throughput inference because the idea is intuitive. One group processes input prompts and passes the KV cache to another group that generates the response. Each group can then be tuned for its specific job.
But our first disaggregated deployments were not dramatically faster, and some larger configurations were actually slower. The split introduces a large data transfer between GPUs, so it only helps when the gains from better batching and specialization outweigh that cost.
Form larger batches.
P/D works best when each group has enough concurrent work to keep the GPUs busy. Moving to GPUs with more VRAM let us batch more aggressively and process larger prompt chunks. Reducing the memory reserved upfront on prefill workers created additional room for those batches.
Keep state transfer fast
. Prefill produces a large block of intermediate data that decode needs. One early build silently fell back from the intended intra-node NVLink transport to TCP because the necessary runtime support was missing. The system still worked, but communication became the bottleneck. We now verify the fast path when building the container and again when workers start.
Match topology to traffic.
Prompt-heavy workloads may benefit from
2P:1D
(2 prefill workers, 1 decode worker), while generation-heavy workloads may favor
1P:2D
. We select the ratio by measuring which phase limits throughput, then autoscale that P/D topology as a unit.
Keep burst traffic redistributable
A naive autoscaling setup sends each burst directly to the small set of containers already running. Those containers accept requests faster than they can process them, causing their inference engines to build large internal queues.
By the time new containers become ready, much of the burst is already pinned to the original containers and cannot be redistributed. The fleet has more capacity, but it cannot help the requests waiting inside another container.
We moved that queue in front of the GPU containers.
A lightweight admission controller tracks the queued and active work on each container, limits how much new work each one receives, and keeps the remaining requests in a shared queue. As new capacity becomes available, those requests can be routed to it instead of remaining stuck on an overloaded container.
This keeps per-container concurrency high enough for efficient batching but low enough that excess requests remain redistributable. The shared queue also gives the autoscaler an early signal that more capacity will be needed.
Make scaled capacity useful sooner
A new GPU worker needs the model files before it can serve requests. We began prefetching them into local memory during container setup instead of waiting for each worker to fetch them from shared storage. Along with a few smaller startup optimizations, this cut median startup time nearly in half.
During a burst, every additional minute of startup is another minute requests remain queued. Faster startup lets newly scaled capacity begin draining that backlog sooner.
The result
Measured across the full burst lifecycle, from scale-out through queue drain, the optimized stack used roughly
80% fewer GPU-hours
for equivalent production traffic.
Efficient inference requires continuously finding and addressing bottlenecks across the serving stack. In our case, the constraint moved from batch formation and memory pressure to state transfer, burst admission, and worker startup. Fixing one bottleneck often revealed the next.
That end-to-end iteration turned a series of serving optimizations into a
4.7× gain in fleet-level GPU efficiency
.
Nick Liu
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
Audio-native semantic speaker-change detection
Posted on
September 3, 2026
Research & Technology
Scaling real-time text-to-speech inference
Posted on
August 20, 2026
Research & Technology
Teaching flow-matching text-to-speech models with RL
Posted on
August 18, 2026
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
