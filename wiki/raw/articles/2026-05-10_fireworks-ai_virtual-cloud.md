---
title: "Build for Scale with Fireworks Virtual Cloud (GA)"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/virtual-cloud"
scraped: "2026-05-10T01:20:44.938955+00:00"
lastmod: "2026-02-12T18:52:00.000Z"
type: "sitemap"
---

# Build for Scale with Fireworks Virtual Cloud (GA)

**Source**: [https://fireworks.ai/blog/virtual-cloud](https://fireworks.ai/blog/virtual-cloud)

DeepSeek V4 Pro is Live → Try it now.
Platform
Models
Developers
Pricing
Training
Partners
Resources
Company
Log In
Get Started
Blog
Virtual Cloud
Build for Scale with Fireworks Virtual Cloud (GA)
PUBLISHED
6/16/2025
Table of Contents
Built for scale
Leverages the latest hardware
Flexible global scheduling
Workload-aware infrastructure
High reliability
Bring-your-own-cloud (BYOC)
Conclusion
Table of Contents
Table of Contents
Built for scale
Leverages the latest hardware
Flexible global scheduling
Workload-aware infrastructure
High reliability
Bring-your-own-cloud (BYOC)
Conclusion
Table of Contents
Anyone who has run a production application at scale knows the impact that performance and reliability has on product success. For AI applications, the challenge is often to successfully operate a fleet of GPUs that handles scaled, globally distributed traffic, potentially in the midst of unprecedented growth.
A few factors make managing bare-metal GPU deployments on your own difficult:
•
Differences and peculiarities of individual GPU clouds
•
Failover and disaster recovery
•
Global replication
•
Hardware failures and degradations
Ultimately, these distract your team from what matters: building winning product experiences for users. That’s why today we’re excited to announce the GA of the
Fireworks Virtual Cloud
, a platform that abstracts away the complexity of managing GPU deployments, handling hardware failures, and scaling workloads across a global fleet.
Launching with over 18 global regions across 8 cloud providers, including support for BYOC, Fireworks Virtual Cloud lets you build for scale from Day 1. To get started with Fireworks Virtual Cloud,
contact us
.
Built for scale
As of June 2025,
Fireworks processes 5 trillion+ tokens every day at 100,000+ requests/s
. For reference, this is roughly the same as the number of search queries Google processes per second
We enable this through our hardware fleet that spans 8 different cloud providers over 18 different regions. Working with multiple providers allows Fireworks to provide high-availability access to hardware when our customers need it. For security-sensitive enterprise workloads, we also support BYOC.
Leverages the latest hardware
Fireworks offers a wide variety of compute architectures from NVIDIA and AMD. We consistently strive to deliver the latest GPU generation to customers quickly and enable optimal performance across the entire stack. For example, we were among the first providers to bring up
AMD MI300X last year
. We also offer older generations of accelerators that can strike a better performance/$ tradeoff for some workloads.
We’re excited to offer the latest generation of NVIDIA B200s GPUs on Fireworks as of May 2025. Blackwell GPUs offer native support for float4 precision which allows unmatched speed and cost efficiency. Using float4 without quality regression requires additional tuning, now automatically provided by FireOptimizer. See the
B200 announcement blog post
for more details.
Thanks to the latest hardware and end-to-end stack optimization Fireworks is able to offer groundbreaking speeds, for example over 250 token/s for
DeepSeek V3
and R1 models.
Top-of-the-line performance running DeepSeek R1 on B200 independently benchmarked by Artificial Analysis
Flexible global scheduling
We previously shared how
Fireworks 3D Optimizer
considers your specific workload characteristics and tunes our proprietary inference engine across the dimensions of speed, quality, and cost.
Additionally, each workload might have unique constraints determining its scheduling:
•
Geographic locality
- to place the GPUs close to the users across the globe
•
Autoscaling or fixed scheduling
– to account for varying traffic patterns
•
Compliance and security requirements
– that may limit permitted regions
•
Disaster resilience
- spreading workload across multiple regions and availability jobs to provide uninterrupted service in case of underlying outages.
Fireworks Virtual Cloud Scheduler lets you specify these requirements and automatically arranges resources to satisfy these constraints.
Workload-aware infrastructure
GenAI workloads have complicated performance characteristics. At Fireworks we co-design our inference stack for optimal speed and efficiency at every level, from GPU kernels all the way to routing traffic across the globe.
For example, an interesting property of many workloads we run is
heterogeneity
. Reinforcement fine-tuning, for instance, consists of alternating phases of policy rollouts (inference-like workload) and policy updates (training-like workload). Similarly, LLM inference consists of prompt processing (GPU compute bound) and token generation (memory bandwidth bound). We can exploit this heterogeneity through
disaggregation
. Each part of the workload can be configured and scaled independently, allowing our scheduler to achieve higher efficiency.
Another example is
prompt caching
. Caching KVs for prompts is one of the most fundamental and critical optimizations to high-performance LLM inference. While conceptually simple, it can be deceptively difficult to optimize when running in large-scale, distributed inference. The system has to balance load on two dimensions: individual component load and locality of the existing precomputed KV cache entries (at region, cluster and node level). At Fireworks we implemented a multi-tiered caching and traffic routing system to maximize the cache hit rate in such real-world scenarios. Even under diverse workload conditions, we often see cache hit rates between 60-90% (or equivalently, 3-10x savings on prompt processing).
High reliability
Running any hardware at scale involves dealing with failures on a regular basis. GPUs in particular are prone to failure due to any number of reasons: disappearing from the system (“falling off the bus”), overheating (leading to lower performance), memory corruption (leading to strange crashes), etc.
The
Llama 3 paper
reports 99.95% reliability for a single GPU on a given day, or only 83% reliability over the course of a year. While in practice we observe worse baseline up-times, even taking the generous estimates means a deployment running on 100 GPUs will experience some failure every 20 days, and a deployment running on 1000 GPUs will experience some failure every other day!
Fireworks Virtual Cloud hides this complexity by proactively monitoring GPU and node health. If an unexpected failure does occur, Fireworks automatically re-provisions capacity and moves your workloads to healthy hardware to minimize downtime. And, our multi-region capability allows customers to create high-availability deployments that protect against geographically-correlated outages.
Bring-your-own-cloud (BYOC)
For maximum data security, Fireworks enables you to bring GPU hardware running on your own cloud infrastructure through our hybrid bring-your-own-cloud offering. We enable you to run the Fireworks inference engine inside your own VPC, so you get all the benefits of Fireworks while ensuring data never leaves your secure environment.
Our BYOC offering is perfect for customers who:
•
Need to host sensitive workloads
•
Have existing commitments for GPUs
•
Want maximum transparency and control over the hosting environment
The Fireworks Virtual Cloud seamlessly integrates with your cloud environment, so deploying your workloads is just as easy as using our fully hosted solution. We also enable running in a hybrid mode as well, where some more sensitive workloads may run in your self-hosted environment while others may run on Fireworks cloud.
Conclusion
At Fireworks, we believe that AI teams should be able to build for scale without worrying about scale. With Fireworks Virtual Cloud, you now have access to a highly-available global fleet of GPUs, optimized for your workload, fully managed and running on state-of-the-art hardware.
Contact us
to explore how Fireworks Virtual Cloud can support your needs.
Platform
AI Native
Enterprise
Customers
Use Cases
Code Assistance
Conversational AI
Agentic Systems
Search
Multimodal
Enterprise RAG
Developers
Model Library
Docs
CLI
API
Changelog
Pricing
Serverless
On-Demand
Fine Tuning
Enterprise
Partners
Cloud and Infrastructure
Consulting and Services
Technology
Fireworks for Startups
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
© 2026 Fireworks AI, Inc. All rights reserved.
