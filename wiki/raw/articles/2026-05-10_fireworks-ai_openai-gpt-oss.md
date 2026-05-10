---
title: "OpenAI gpt-oss 20b & 120b: Overview & Benchmarking Info"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/openai-gpt-oss"
scraped: "2026-05-10T01:21:12.653871+00:00"
lastmod: "2026-02-12T18:51:37.000Z"
type: "sitemap"
---

# OpenAI gpt-oss 20b & 120b: Overview & Benchmarking Info

**Source**: [https://fireworks.ai/blog/openai-gpt-oss](https://fireworks.ai/blog/openai-gpt-oss)

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
Openai Gpt Oss
Introducing OpenAI gpt-oss (20b & 120b)
PUBLISHED
8/5/2025
Table of Contents
1. TL;DR Summary
Here are the key-features you need to know:
2. Benchmarking Information
3. Comparison to other OpenAI Models
Performance Metrics vs other Chinese models (+ any other proprietary model)
4. Technical Details
Post-Training for Reasoning, Tools, and Agentic Behavior (GPT-OSS Models)
5. Implementation Guidance
AMD Partnership
Resources
Table of Contents
Table of Contents
1. TL;DR Summary
Here are the key-features you need to know:
2. Benchmarking Information
3. Comparison to other OpenAI Models
Performance Metrics vs other Chinese models (+ any other proprietary model)
4. Technical Details
Post-Training for Reasoning, Tools, and Agentic Behavior (GPT-OSS Models)
5. Implementation Guidance
AMD Partnership
Resources
Table of Contents
This is a deep dive analysis of gpt-oss (20b & 120b), released by OpenAI on 5th Aug 2025. This blog explores its capabilities, technical architecture, benchmarks, and practical applications for developers.
1. TL;DR Summary
OpenAI is finally back to living up to its name of building “open models”. After GPT-2, this is the first set of open-source LLMs coming from OpenAI.
OpenAI's new open-source models, gpt-oss-20b and gpt-oss-120b, are very strong reasoning models that excel at problem solving and tool calling. Both models support long context windows and adjustable reasoning levels. That makes them a great choice for agentic use cases.
Here are the key-features you need to know:
•
The models performance is at the level of o3 and o4-mini (see section 2.1 for benchmarks)
•
The models support both built-in (code interpreter, browser) and user-provided tools and are able to generate consistent trajectories over doesn’t of turns
•
The models allow for selecting low/mid/high reasoning level (as in o4-mini-high)
•
The model architecture is quite standard mixture-of-experts transformer. The performance upgrades are primarily because of the training data & reinforcement learning tuning
Try out the new OpenAI
gpt-oss-120b
&
gpt-oss-20b
on Fireworks AI!
2. Benchmarking Information
The following table is an evaluation across multiple benchmarks and reasoning levels for both the gpt-oss-20b and gpt-oss-120b
3. Comparison to other OpenAI Models
The following table showcases the Main capabilities evaluations, where gpt-oss models are compared at reasoning level with other OpenAI closed-models including - high to OpenAI’s o3, o3-mini, and o4-mini on canonical benchmarks.
The gpt-oss-120b model surpasses OpenAI o3-mini and approaches OpenAI o4-mini accuracy. The smaller gpt-oss-20b model is also surprisingly competitive, despite being 6 times smaller than gpt-oss-120b.
Performance Metrics vs other Chinese models (+ any other proprietary model)
A fair comparison of gpt-oss against leading commercial models including Kimi, GLM, Qwen and DeepSeek, highlighting areas where it excels and areas for improvement.
4. Technical Details
Post-Training for Reasoning, Tools, and Agentic Behavior (GPT-OSS Models)
After pre-training on massive text data, thegpt-oss models go through a dedicated post-training phase to refine their reasoning abilities and tool usage, drawing from similar Chain-of-Thought (CoT) reinforcement learning techniques used in OpenAI's o3 models.
This phase trains the models on complex, multi-step tasks across coding, math, and science, helping them develop structured problem-solving capabilities and a personality similar to ChatGPT.
4.1 Harmony Chat Format: A New Chat Protocol for Smarter Agents
OpenAI introduced a new format called the Harmony Chat Format- a flexible, role-aware, message-based structure for interactive conversations.
•
It uses labeled roles like System, Developer, User, Assistant, and Tool to enforce a hierarchy when resolving conflicting instructions.
•
Special “channels” like analysis, commentary, and final help guide how reasoning traces, tool calls, and final answers are shown to the user.
•
This structure enables the model to perform more advanced agentic tasks, like embedding tool calls directly within reasoning steps or sharing step-by-step action plans.
💡 If you're deploying gpt-oss models, using Harmony Format correctly is essential for unlocking their full capabilities, especially in multi-turn chats.
4.2 Variable Reasoning Levels
The models are trained to support
three reasoning levels
- low, medium, and high, configured in the system prompt (e.g., Reasoning: high).
As you increase the reasoning level, the model produces longer and more structured CoT traces, allowing it to think through problems with greater depth.
4.3 Agentic Tool Use
gpt-oss models are also trained to work with a range of tools in agentic workflows:
•
Web browsing
, to fetch real-time information and increase factual grounding
•
Python execution
, in a stateful notebook-style environment for live code reasoning
•
Custom developer functions
, defined in-system using schemas (similar to OpenAI’s function calling)
These tools can be turned on or off using system prompts, and OpenAI provides basic harnesses and an open-source implementation to help developers integrate them into real-world apps.
5. Implementation Guidance
You can run both the gpt-oss models (
gpt-oss-120b
&
gpt-oss-20b
) on Fireworks AI Model Library via UI.
1
2
3
4
5
6
7
8
9
10
11
12
13
14
# Example implementation using Fireworks.ai API
import
fireworks
.
ai
as
fw
fw
.
api_key
=
"your_api_key"
response
=
fw
.
Completion
.
create
(
model
=
"fireworks/[model-name]"
,
#Replace [model-name] as
#gpt-oss-120b or gpt-oss-20b
prompt
=
"Your prompt here"
,
max_tokens
=
100
,
temperature
=
0.7
)
print
(
response
.
choices
[
0
]
.
text
)
AMD Partnership
We’re also excited to announce a joint effort between Fireworks AI and AMD to bring OpenAI models to AMD’s latest MI355 GPUs. This collaboration will make powerful AI models more accessible and cost-efficient, coming soon to the Fireworks AI platform.
Try out the new OpenAI gpt-oss models now!
•
gpt-oss-120b:
https://fireworks.ai/models/fireworks/gpt-oss-120b
•
gpt-oss-20b:
https://fireworks.ai/models/fireworks/gpt-oss-20b
Resources
•
Official model documentation:
https://openai.com/index/introducing-gpt-oss/
•
Model card:
https://cdn.openai.com/pdf/419b6906-9da6-406c-a19d-1bb078ac7637/oai_gpt-oss_model_card.pdf
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
