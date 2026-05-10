---
title: "NVIDIA Nemotron 3 Nano on Fireworks: The Engine for Next-Generation AI Agents"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/nvidia-nemotron3-nano"
scraped: "2026-05-10T01:28:02.566437+00:00"
lastmod: "2026-01-16T21:08:28.000Z"
type: "sitemap"
---

# NVIDIA Nemotron 3 Nano on Fireworks: The Engine for Next-Generation AI Agents

**Source**: [https://fireworks.ai/blog/nvidia-nemotron3-nano](https://fireworks.ai/blog/nvidia-nemotron3-nano)

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
Nvidia Nemotron3 Nano
NVIDIA Nemotron 3 Nano on Fireworks: The Engine for Next-Generation AI Agents
PUBLISHED
12/15/2025
Table of Contents
From Nemotron 2 Nano to Nemotron 3 Nano: Architecture, Efficiency, and Real-World Impact
Unlocking Peak Performance: NVIDIA Nemotron 3 on Fireworks
Getting Started on Fireworks
Additional Resources
Table of Contents
Table of Contents
From Nemotron 2 Nano to Nemotron 3 Nano: Architecture, Efficiency, and Real-World Impact
Unlocking Peak Performance: NVIDIA Nemotron 3 on Fireworks
Getting Started on Fireworks
Additional Resources
Table of Contents
We're excited to launch Day-0 support on Fireworks for the latest model in the NVIDIA Nemotron family, NVIDIA Nemotron 3 Nano, an advanced reasoning model set to fuel the next generation of AI Agents. This model is a small, powerful, hybrid Mixture-of-Experts (MoE) model built for developers who need maximum compute efficiency and cutting-edge accuracy for specialized agentic systems.
From Nemotron 2 Nano to Nemotron 3 Nano: Architecture, Efficiency, and Real-World Impact
The model builds on the
Nemotron 2 Nano release
combining a new Mixture-of-Experts architecture with the Nemotron hybrid transformer-mamba architecture. The MoE design reduces compute overhead to meet the tight latency demands of real-world applications. For leading accuracy, Nemotron 3 Nano is a 30B parameter model with 3B active parameters for inference, and a large 1M context length that has been trained using NVIDIA-curated, high-quality synthetic data from expert reasoning models. Along with the MoE architecture it features a new token thinking budget to ensure optimal accuracy while minimizing the generation of reasoning tokens, streamlining inference cost and predictability. This combination of speed and precision makes it a game-changer for use cases like accelerating loan processing and detecting fraud in finance, automatically triaging security threats in cybersecurity, assisting with tasks like code summarization, and optimizing software development of inventory and service management in retail.
Under the hood, the MoE architecture consists of 23 Mamba-2 and MoE layers, complemented by 6 Attention layers. Within each MoE layer, you'll find 128 experts plus 1 shared expert, with 5 experts activated per token. While the model leverages a full 30B parameters, its optimized design means it only activates an incredibly efficient 3B active parameters for inference. This streamlined design makes it optimal for tasks involving coding, scientific reasoning, math.
Unlocking Peak Performance: NVIDIA Nemotron 3 on Fireworks
Customers rely on Fireworks to deploy their models because we are committed to building the future of inference. We provide the fastest AI Inference Cloud, powered by the latest NVIDIA GPU architectures—like the NVIDIA B200 and H200—to ensure unmatched performance. Developers get more than just hardware infrastructure: our platform includes proprietary optimizations like FireAttention v4 and custom kernel techniques that deliver up to 4x higher throughput and unlock unprecedented inference speeds while fully preserving model quality. This is the optimal environment for production workloads: a highly scalable, reliable, and high-performance foundation that seamlessly integrates with the open-source models like the NVIDIA Nemotron family, ultimately empowering developers with optimized costs and superior speed.
Getting Started on Fireworks
Developers can deploy Nemotron 3 Nano on on demand, and to make experimentation easier, we put together a hands-on cookbook that shows exactly how to get started.
The cookbook walks through how to use Nemotron 3 Nano on Fireworks AI for real code summarization tasks. It covers the full inference setup, how to construct reliable summarization prompts, and how the model behaves when run on both small Python scripts and large multi function files. It also includes a practical chunking strategy for long source files where the model generates section summaries first, then synthesizes them into a final high level overview.
Why does this matter? Code summarization is one of the simplest ways to accelerate onboarding, debugging, and cross team collaboration. Engineers reach for summaries when they inherit legacy code, audit unfamiliar repositories, hand work off across time zones, or need quick context before modifying a component. A fast, lightweight model that runs locally or on low cost infrastructure can turn minutes of scanning into seconds of comprehension.
This is where Nemotron 3 Nano fits well. It is designed to punch above its size on coding tasks, and the benchmarks reflect that. The model is compact enough for edge style deployments, responsive enough for interactive workflows, and strong enough to generate summaries that capture intent, data flow, and function relationships without getting lost in boilerplate. For internal tools, documentation helpers, or agent style systems that need to extract structure from code, Nano 3 is a solid building block.
If you want to try it out, explore the full cookbook here:
Cookbook For Nemotron 3 Nano
The NVIDIA Nemotron 3 Nano introduces significant efficiency and accuracy improvements:
•
MoE hybrid architecture reduces cost while improving throughput
•
Fireworks unlocks maximum performance through kernel and attention-level optimizations
•
Ideal for agentic workloads requiring real-time reasoning and long-context window
Deploy Nemotron models on Fireworks today with a single command and experience the future of efficient AI. We're excited to work with NVIDIA to make these breakthrough models available to developers worldwide.
Questions? Join our
Discord
or contact
[email protected]
Additional Resources
•
NVIDIA Nemotron Technical Paper
•
NVIDIA Nemotron 3 Nano
•
Fireworks x NVIDIA Partner Page
•
Cookbook For Nemotron Nano 3
•
NVIDIA Nemotron 3 Family
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
