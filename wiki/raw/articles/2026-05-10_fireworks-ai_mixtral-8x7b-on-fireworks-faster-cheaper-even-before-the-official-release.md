---
title: "Mixtral 8x7B on Fireworks: faster, cheaper, even before the official release"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/mixtral-8x7b-on-fireworks-faster-cheaper-even-before-the-official-release"
scraped: "2026-05-10T01:21:07.658803+00:00"
lastmod: "2026-02-12T18:53:20.000Z"
type: "sitemap"
---

# Mixtral 8x7B on Fireworks: faster, cheaper, even before the official release

**Source**: [https://fireworks.ai/blog/mixtral-8x7b-on-fireworks-faster-cheaper-even-before-the-official-release](https://fireworks.ai/blog/mixtral-8x7b-on-fireworks-faster-cheaper-even-before-the-official-release)

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
Mixtral 8x7b On Fireworks Faster Cheaper Even Before The Official Release
Mixtral 8x7B on Fireworks: faster, cheaper, even before the official release
PUBLISHED
12/14/2023
Table of Contents
Fastest inference on Fireworks
Passing cost savings to you
Accessing Mixtral through Fireworks
How good are the experts?
Race to MoE awesomeness
Table of Contents
Table of Contents
Fastest inference on Fireworks
Passing cost savings to you
Accessing Mixtral through Fireworks
How good are the experts?
Race to MoE awesomeness
Table of Contents
The newest Mistral AI MoE model, Mixtral 8x7B, is available on the Fireworks platform in both base and instruction-tuned variants. We offer it with unprecedented speed reaching 175 tokens/s and a low cost of $0.45 to $0.6 per million tokens for summarization or multi-turn chat respectively.
Fastest inference on Fireworks
To enable Mistral on Fireworks we added support for the mixture of experts layers into our custom-built inference engine powering Fireworks.ai platform. In combination with other optimizations (custom kernels for layers like
MQA
to purpose-built communication primitives and flexible parallelization schemes) our engine is able to achieve
175 tokens/s
on a latency-optimized setup for Mixtral 8x7B served in original (16 bit) precision.
Our engine also supports 8-bit floating point (fp8) regime, which delivers much higher throughput for custom deployments. Unlike integer-based quantization, which can be finicky, fp8 comes with virtually no impact on model quality.
As we explained in
our benchmarking blogpost
, when it comes to inference performance, there is
no one size fits all
. Fireworks specialized in multi-faceted deployment to optimize towards your LLM workload pattern, varying from latency-optimized, fixed-latency-throughput-optimized, to throughput-optimized. The diagram below illustrates the variation of deployment configurations.
We have the best setup for everyone!
For example, the configuration deployed on the
playground and public API
runs a moderate load, so you should see speeds of 80–100 tokens/s.
We're continuing performance optimization work on Mixtral, so expect to see more improvements in the future.
Passing cost savings to you
We're introducing the new pricing tier for Mixture of Experts models that ends up costing $0.45 to $0.6 per million tokens on average for Mixtral 8x7B.
Our official pricing separates prompt and generation tokens. For Mixtral 8x7B, the prompt is charged at $0.4/million and generation at $1.6/million. For multi-turn chat we typically see a 4:1 to 6:1 prompt to generation ratio resulting in an average of $0.6/million tokens. For summarization, the average cost is around $0.45/million tokens.
We're able to provide this competitive pricing thanks to our custom inference engine that can utilize GPUs effectively and deliver high throughput under low latency constraints. This is particularly true for Mixture of Experts models: to reap the benefits of selective expert activations, one has to run at sufficiently high load (as
explained here
).
Accessing Mixtral through Fireworks
You can head to
our playground
now to play with Mixtral using free credits (no credit card required).
We offer
OpenAI-compatible API
(for both base and chat completions) that you can call using REST, our Python client or any OpenAI-compatible client library. For example you can migrate your existing application using OpenAI python client by providing a different base url:
How good are the experts?
Over the previous weekend, Mistral AI released a new, very exciting model: Mi
x
tral. The “x” highlights the twist. Most of today's LLMs are dense, meaning that every model parameter participates in generating every token. Mixtral brings the “sparse mixture of expert” technique back to the mainstream: it divides feed-forward layers of the model into 8 independent “experts” with only 2 of them executed for every token. Thus it enables higher model capacity at lower inference cost and higher speed.
Mixtral 8x7B is released under Apache 2.0 license and it beats Llama 2 70B and GPT-3.5 on most benchmarks as
highlighted in the release blog
. Our early experiments confirm that model capabilities are very strong.
Race to MoE awesomeness
The last few days were quite intense. The Mistral AI team did a very unconventional release, dropping the
model checkpoint on torrent
last Friday morning. There was no model code or way to run it!
By reverse-engineering parameter names, we were the first to implement working inference code just 4 hours later. We
shared it
with the community and enabled people to experiment with the model on various datasets on the same day. The base model was up on the Fireworks platform the same evening. Over the next few days, we added necessary performance enhancements to get the speeds described here.
The original model drop on Friday included only the base model and was not suitable for chat use cases. So, we quickly fine-tuned an
instruction-following variant
of the model and deployed it on Saturday. We later substituted it with the official Mixtral-8x7B-Instruct, which was released the following Monday.
We're adding features to Mixtral deployment, in particular, the ability to deploy your own custom LoRA fine-tunes on Fireworks with no additional cost (like you can for
other models
already).
We want to thank the Mistral AI team for sharing an extremely capable model openly with the community and for creating a fun puzzle on how to enable it initially.
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
