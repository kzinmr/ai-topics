---
title: "Deployment Shapes: One Click Deployment Configured for You"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/deployment-shapes"
scraped: "2026-05-10T01:20:46.074377+00:00"
lastmod: "2026-02-12T18:51:18.000Z"
type: "sitemap"
---

# Deployment Shapes: One Click Deployment Configured for You

**Source**: [https://fireworks.ai/blog/deployment-shapes](https://fireworks.ai/blog/deployment-shapes)

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
Deployment Shapes
Deployment Shapes: One-Click Deployment Configured For You
PUBLISHED
10/23/2025
Configuring the right LLM serving set-up can be a headache for developers. There are a variety of optimizations that can be tweaked to balance speed and cost, ranging from quantization level, hardware choice, speculation technique and model sharding specifics. Historically, Fireworks worked closely with our customers to manually implement all these optimizations, pushing the limits of what is possible and optimizing between latency, throughput, and cost for the customer’s use case. We make this infrastructure accessible to you in a few easy ways.
Serverless
The easiest way to start using Fireworks is with our serverless deployments, which let you make requests to the most popular models without any setup. Serverless deployments are preconfigured with one set-up for everyone. That makes serverless very easy to use, but it also means that serverless might not be optimal for your goals, especially if you have the volume to utilize a single-tenant deployment.
On-demand
On-demand deployments provide single-tenant, customizable deployments that can be customized specifically for your needs. They present a great upgrade route from serverless in situations like:
You’re optimizing for latency and need faster speeds than serverless
You have high request volume and want lower prices than serverless
You’re using a less popular or custom model that’s not available on serverless
Until today, users had to fully configure settings for their on-demand deployment, like quantization level and GPU choice. Today, we’re making it even easier to use on-demand deployments, while also helping developers achieve faster and more cost-efficient results
Unlock Faster Testing Cycles with Deployment Shapes
The best LLM inference is tailored to your use case. Fireworks is introducing pre-configured
deployment shapes
for our most popular models. Deployment shapes are pre-set templates that make it really easy to create a deployment optimized for your goals. We’re introducing three types of deployment shapes that are optimized for the three most common needs: latency, throughput, and cost.
Figure 1: Sample Deployment Shapes Web View
Most likely, you still care about all three, so each shape optimizes for one goal, while balancing for the two others. This means these shapes don’t give you the absolute fastest or highest throughput possible on Fireworks (if that’s what you need, talk to us via
[email protected]
).
Minimal:
This shape is the cheapest deployment for the model. This is best for users testing models at a small scale. Users who are trying out a fine tuned model or an open source model not available on Fireworks serverless should choose this option.
Fast:
This shape is best for low latency use cases, usually when the LLM interaction is customer facing. For example, users building chatbots or code completion features should choose this option.
Throughput:
This shape is best for getting the lowest per token pricing at scale. Latency does not matter as much. This is ideal for users who want to do benchmarking or bulk testing
Improved Inference with Fireworks Magic
Behind the scenes, for each deployment shape, Fireworks has configured settings to optimize for cost and/or speed. Some of these settings are publicly viewable (GPU choice, quantization) while hidden settings like speculation and caching specifics are configured behind-the-scenes. Deployment shapes are configured around typical prompt sizes (5k tokens input, 1k tokens output), so results may vary if your workload differs. To get the optimal serving for your specific workload and constraints,
contact us
.
Since the beginning of Fireworks, our research teams have iteratively improved our GPU kernels in all directions. From being the first to support open source
mixture of experts models
to most recently
reaching industry leading speeds
by leveraging FP4 precision on NVIDIA Blackwells, we have also been adding different configurations to Fireworks, so that deployments can be tailored to your use case.
We’ve taken full advantage of these toggles for customers, leading to impressively fast inference at scale. For example, we
worked with Cursor
, to build latency-sensitive features like Smart Rewrite. One of the major configurations we have is speculative decoding, which contributes to a massive speed up for Smart Rewrite users’ coding experiences. Behind the scenes, we’re also configuring things like batch size and KV cache sharding.
Our research team is continuously improving FireAttention and adding in configurations that can help further optimize deployments for your specific use cases. We’re iterating on newer speculation methods, caching techniques, and new kernels. These methods are also applied to deployment shapes, so that you automatically take advantage of any cutting edge technology tailored to your use case.
Get Started Today with Deployment Shapes
You can start using deployment shapes today from both the website and the CLI.
•
If you prefer the CLI, visit our
quick start guide
.
•
If you prefer to use the website, visit the
create deployment page
.
If you need further optimizations beyond the shapes available to you publicly, our team has extensive experience extracting every bit of power from GPUs for our enterprise customers. For further questions, reach out on Discord or via
[email protected]
.
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
