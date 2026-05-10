---
title: "Kimi K2.5 Is Live on Fireworks: Vibe Coding, Agents, and Full-Parameter RFT"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/kimi-k2p5"
scraped: "2026-05-10T01:27:38.564107+00:00"
lastmod: "2026-02-12T18:51:00.000Z"
type: "sitemap"
---

# Kimi K2.5 Is Live on Fireworks: Vibe Coding, Agents, and Full-Parameter RFT

**Source**: [https://fireworks.ai/blog/kimi-k2p5](https://fireworks.ai/blog/kimi-k2p5)

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
Kimi K2p5
Kimi K2.5 is Live on Fireworks: Vibe Coding, Agents, and Full-Parameter RFT
PUBLISHED
1/26/2026
Table of Contents
What can you build with Kimi K2.5 on Fireworks?
Full Parameter RL Tuning for Kimi K2.5
What is this?
Key Features
What does this enable?
Fastest Kimi K2.5 and K2 Series Speed on Fireworks
Get started with Kimi K2.5 on Fireworks
Table of Contents
Table of Contents
What can you build with Kimi K2.5 on Fireworks?
Full Parameter RL Tuning for Kimi K2.5
What is this?
Key Features
What does this enable?
Fastest Kimi K2.5 and K2 Series Speed on Fireworks
Get started with Kimi K2.5 on Fireworks
Table of Contents
Kimi K2.5
is Moonshot AI’s flagship agentic model and a new SOTA open model. It unifies vision and text, thinking and non-thinking modes, and multi-agent execution into one model.
We are launching Day-0 support for Kimi K2.5. Fireworks offers the fastest endpoint for all Kimi K2 series models as well as fine tuning for Kimi K2 models. Additionally, we now offer a
full parameter RL tuning
private preview
for Kimi K2.5, enabling application builders to fine tune the SOTA OSS VLM model for use cases like vibe coding and agentic workflows. Sign up for the full parameter RL tuning waitlist
here
.
What can you build with Kimi K2.5 on Fireworks?
Kimi K2.5 demonstrates that open source models are now surpassing their closed-source counterparts. The chart provides more details on the multiple benchmarks where Kimi K2.5 achieves SOTA results, including for Agents (HLE Full, BrowseComp, and Deepsearch) and for Vision (OmniDoc Bench 1.5).
Kimi K2.5 Benchmarks
Below is an in-depth look at its core application areas, highlighting the advanced nature across multiple multimodal agent use cases.
When to use Kimi K2.5 vs. Kimi K2 Thinking?
Kimi K2.5 is a multimodal model supporting image and video understanding. For text-only processing, developers can use the Kimi K2 model series including
Kimi K2 Thinking
and
Kimi K2 0905
.
Full Parameter RL Tuning for Kimi K2.5
Fireworks now supports full parameter RL tuning for Kimi K2.5 in private preview, allowing product developers to customize the model to their specific product use cases and exceed the quality of closed models. For companies already tuning models with LoRA, full parameter fine tuning offers an additional lever to get the best model quality. Signup for the waitlist
here
.
What is this?
We are launching full parameter RL fine-tuning for Kimi K2.5 with Tinker API compatibility. Researchers get low-level compute primitives—
forward, forward_backward, optimizer_step, save_weight
—while we handle the distributed training infrastructure.
Key Features
•
Tinker API Compatible
: Same interface researchers already use for LoRA and SFT, now extended to full parameter training. Existing Tinker integrations can switch to full parameter mode with minimal code changes.
•
Cross-Region RL Training
: Support trainer and sampler deployments in different regions. Fireworks RL model format enables seamless weight transfer between regions without customers managing cross-region data pipelines. This is critical for global teams where training data, model providers, and inference endpoints span multiple cloud regions.
•
Customizable Loss
: Customers can implement their own GRPO/reward shaping logic on their side. This keeps our API surface minimal and lets world-class researchers maintain full control over their RL algorithms.
What does this enable?
Global teams can train in one region and hot-load checkpoints into inference deployments elsewhere without managing cross-region weight transfers manually, allowing them to scale up their training to saturate the whole data center. The Fireworks RL trainer + model format handles all the serialization, compression, and ledger bookkeeping.
Fastest Kimi K2.5 and K2 Series Speed on Fireworks
Fireworks offers the fastest endpoint for all Kimi K2.5 and Kimi K2 series models. Fireworks achieves up to 200 Tokens/s on Kimi K2.5. Data from Artificial Analysis’ independent benchmarks shows that Fireworks consistently provides best-in-class performance for Moonshot’s Kimi Models, including Kimi K2 Thinking and Kimi K2 0905. Outperforming the next closest GPU inference provider by up to 75%. Faster speed is essential for real-time user experience, application productivity, and operational efficiency.Stay tuned as our engineering team continues to optimize the performance. Stay tuned as our engineering team continues to optimize the performance.
Kimi K2 Thinking on Artificial Analysis
Kimi K2 0905 on Artificial Analysis
Get started with Kimi K2.5 on Fireworks
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
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
import
requests
import
json
url
=
"https://api.fireworks.ai/inference/v1/chat/completions"
payload
=
{
"model"
:
"accounts/fireworks/models/kimi-k2p5"
,
"max_tokens"
:
32768
,
"top_p"
:
1
,
"top_k"
:
40
,
"presence_penalty"
:
0
,
"frequency_penalty"
:
0
,
"temperature"
:
0.6
,
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
[
{
"type"
:
"text"
,
"text"
:
"Can you describe this image?"
}
,
{
"type"
:
"image_url"
,
"image_url"
:
{
"url"
:
"https://images.unsplash.com/photo-1582538885592-e70a5d7ab3d3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1770&q=80"
}
}
]
}
]
}
headers
=
{
"Accept"
:
"application/json"
,
"Content-Type"
:
"application/json"
,
"Authorization"
:
"Bearer <API_KEY>"
}
requests
.
request
(
"POST"
,
url
,
headers
=
headers
,
data
=
json
.
dumps
(
payload
)
)
Fireworks enables users to control the reasoning behavior of the Kimi K2.5 model and inspect its reasoning history for greater transparency.
Click here
for more details.
Start building with Kimi K2.5 at Fireworks!
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
