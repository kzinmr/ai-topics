---
title: "Introducing Supervised Fine-tuning V2"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/supervised-finetuning-v2"
scraped: "2026-05-10T01:20:57.273612+00:00"
lastmod: "2026-02-12T18:52:03.000Z"
type: "sitemap"
---

# Introducing Supervised Fine-tuning V2

**Source**: [https://fireworks.ai/blog/supervised-finetuning-v2](https://fireworks.ai/blog/supervised-finetuning-v2)

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
Supervised Finetuning V2
Introducing Supervised Fine Tuning V2
PUBLISHED
6/13/2025
Table of Contents
New Capabilities
More Models
Longer Context Length
Quantization Aware Training
Training with Multi-token Prediction
Multi-turn Function Calling
Faster speeds
Multi-LoRA
Getting Started
Table of Contents
Table of Contents
New Capabilities
More Models
Longer Context Length
Quantization Aware Training
Training with Multi-token Prediction
Multi-turn Function Calling
Faster speeds
Multi-LoRA
Getting Started
Table of Contents
At Fireworks, we believe models and data are core assets for any company. If you're building a vertical product, owning both your data and your models is key to delivering a premium user experience and creating strong product differentiation.
Data and models should form a self-improving loop: a better model powers a better product, a better product attracts more users, and more users generate more data to improve the model further. This is what we call the data flywheel.
You likely already have strong GTM and engineering teams to accelerate growth. Fireworks can help you close the loop by turning your data into a high-quality, customized model, and potentially, an even better product. We're excited to unveil
Supervised Fine Tuning V2,
the next generation of our supervised fine-tuning service, designed to do just that.
V2 is not just an upgrade of our original fine-tuning service, it is a complete rewrite to deliver both better quality and faster training speed. Along with the beta release of our
Reinforcement Fine Tuning platform
we announced earlier this week, this provides you with another tool in your toolbox to adapt models to your specific use case and data.
Let’s dive into the new features and enhancements that we’re introducing with SFT V2.
New Capabilities
More Models
Our fine-tuning capabilities have expanded to include a broad range of models. This now encompasses the Qwen 2/2.5/3 series, Phi 4, Gemma 3, the Llama family, as well as leading open-source MoE models like
Deepseek R1
and V3, including, of course, any fine-tuned variants of those models! For a comprehensive view of all supported tunable models, please refer to our Model Library:
Model Library
.
Longer Context Length
We've really cranked things up with optimized kernels and smart memory handling, now we can handle training with context lengths all the way up to 131K. Basically, this means continued training for our models at their full context length.
Quantization Aware Training
To ensure optimal inference quality, both FP4 and FP8 quantization-aware training options are supported. You no longer have to sacrifice quality for speed. As shown below, both FP8 QAT and FP4 QAT reduce evaluation loss compared to not using QAT, and both are able to converge to minimal evaluation loss after further training.
Training with Multi-token Prediction
On DeepSeek V3/R1 models, we additionally support MTP (multi-token prediction) similar to what was described in the
DeepSeek V3
paper to achieve potentially lower loss, and simultaneously adapt the MTP layer to achieve 3X generation speed when used as speculator at inference time.
Multi-turn Function Calling
Supervised Fine Tuning V2 also supports multi-turn function calling fine tuning with vLLM compatible format, where you supply the list of tools and have intermediate tool calls in the chat messages.
1
2
3
4
5
6
7
8
9
{
"messages"
:
[
{
"role"
:
"user"
,
"content"
:
"..."
}
,
{
"role"
:
"assistant"
,
"tool_calls"
:
"..."
}
,
{
"role"
:
"tool"
,
"content"
:
"..."
}
,
...
]
,
"tools"
:
[
]
,
// optional
}
As shown in our
RFT blogpost
, the powerful combination of SFT and RFT helps deliver a model that surpasses SOTA closed model.
Faster speeds
Supervised Fine Tuning V2 boasts training speeds twice as fast as V1, thanks to numerous optimizations in training infrastructure. To illustrate, fine-tuning a
Qwen 72B
model on 1 million tokens can be achieved in under 10 minutes. Ongoing optimizations are continuously being added to further accelerate training.
While by default, a fine-tuning job will use a single GPU, you can now optionally enable turbo mode with the
--turbo
flag on non-Deepseek models to accelerate training using multiple GPUs to make your training jobs complete even faster.
Multi-LoRA
For early prototyping and experimentation workflows, we encourage you to take advantage of
Multi-LoRA
, which allows you to load up to 100 LoRA addons onto a single base model deployment. This increases utilization of your deployment and saves you from cold-start times when testing several fine-tuned variants of the same model.
Getting Started
Supervised Fine Tuning is key to unlocking the power of your data to achieve unrivaled quality over your data and use case. With SFT v2, you now have access to a wider array of models, more powerful tuning techniques, and faster speeds to help you iterate quickly.
To get started, please check out our
docs
and
API reference
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
