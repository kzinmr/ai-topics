---
title: "Post-training Kimi K3 with Harvey for long-horizon legal work"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/post-training-kimi-k3-with-harvey-for-long-horizon-legal-work"
scraped: "2026-08-27T06:00:33.057077+00:00"
lastmod: "2026-08-26T17:27:11.000Z"
type: "sitemap"
---

# Post-training Kimi K3 with Harvey for long-horizon legal work

**Source**: [https://fireworks.ai/blog/post-training-kimi-k3-with-harvey-for-long-horizon-legal-work](https://fireworks.ai/blog/post-training-kimi-k3-with-harvey-for-long-horizon-legal-work)

DeepSeek-V4-Pro-0813 available now on Fireworks
Product
Solutions
Models
Pricing
Resources
Log In
Get Started
Blog
Post Training Kimi K3 With Harvey For Long Horizon Legal Work
Post-training Kimi K3 with Harvey for long-horizon legal work
PUBLISHED
8/26/2026
Table of Contents
TL;DR
What LAB measures, and why all-pass is the bar
Results
Performance
Generalization
Minimal regression
Cost
What’s next
The infrastructure behind the run
Numeric alignment
Batch invariance
Build your own frontier
Table of Contents
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
Talk to the Fireworks training team
Get in touch
Table of Contents
TL;DR
What LAB measures, and why all-pass is the bar
Results
Performance
Generalization
Minimal regression
Cost
What’s next
The infrastructure behind the run
Numeric alignment
Batch invariance
Build your own frontier
Table of Contents
Talk to the Fireworks training team
Get in touch
TL;DR
•
Harvey
recently announced its first model
, Tenet, post-trained in collaboration with Fireworks for long-horizon legal work from a Kimi K3 base using asynchronous reinforcement learning on the
Fireworks Training API
.
•
Initial work shows promising results for both performance and cost-efficiency, with Tenet completing almost twice as many held-out Legal Agent Benchmark (LAB) tasks as base Kimi K3.
•
Tenet performance gains transfer to agentic benchmarks the model never saw during training, with no significant regression on legal knowledge benchmarks.
What LAB measures, and why all-pass is the bar
Legal work is complex and exacting. It requires lawyers to synthesize information, apply judgment, and produce work to the highest of standards.
The
Legal Agent Benchmark (LAB)
is built to meet those high standards. LAB drops agents into sandboxed workspaces with real legal documents and tools and asks them to produce finished deliverables: memos, marked-up contracts, diligence summaries. An LLM judge then opens each deliverable and grades it against dozens of concrete criteria.
A deliverable only passes if it meets every criterion. The metric that matters is all-pass: the share of tasks that clear all of the criteria end to end. A model can score well on average and still miss a single criterion that undermines the output.
Results
Performance
Harvey Tenet scores 19.7% all-pass on LAB against 10.8% for base Kimi K3, and 11.3% on Lab Contracts against 9.3% for base Kimi K3 — increases of 9 and 2 percentage points respectively, with almost twice as many held-out LAB tasks completed. Harvey reports these improvements are grounded in broad criteria gains around answer detail and citations. Tenet achieves state-of-the-art performance on LAB Contracts and places second on LAB.
Generalization
The gains transfer to agentic benchmarks the model never saw during training. Against base Kimi K3, Tenet improves from 58.8% to 74.0% on
Mercor’s Apex Agents
(Corporate Law) and from 49.3% to 55.5% on
Crosby’s Redline Bench
. Neither benchmark appeared in training, and Redline Bench ran in an entirely different harness than the one the model was trained in. Behavior learned in training transferred across both benchmarks and harnesses.
Minimal regression
Tenet holds its performance on benchmarks that test legal knowledge and parametric reasoning rather than agentic capability, including LegalBench, CUAD, MAUD and Mercor’s Apex-v1. Measured against base Kimi K3, improving agentic capability did not come at the expense of the base model’s broader understanding of law.
Cost
Additionally, the performance came without a cost penalty. Harvey Tenet runs at $5.92 per LAB task against $5.62 for base Kimi K3 — effectively flat, while completing nearly twice as many tasks. Two things make that possible: (1) open-weight per-token pricing, and (2) the reward shaping described below. Baseline scores are from the Vals LAB leaderboard.
What’s next
This post is an introduction to the post-training efforts that Harvey and Fireworks have partnered on. A detailed technical write-up of the training methodology (the reward design, the async RL setup, and what we learned running long-horizon rollouts at this scale) will follow.
The infrastructure behind the run
Post-training at this scale is an infrastructure problem. Tens of thousands of long-horizon rollouts per checkpoint, each running past 50 turns and 100,000 generated tokens in a live sandbox, put pressure on the training stack in ways that shorter-horizon workloads do not.
Two properties of the Fireworks platform matter most for reinforcement learning of this kind.
Numeric alignment
We build the training and inference stacks together, and as a result, training and serving share the same numerics. The checkpoint you post-trained is the one that runs. This is not only an operational convenience. When training and inference diverge numerically, that divergence surfaces as token clipping and, past a threshold, reward collapse mid-run. Keeping train-inference KL down is what keeps a long RL run stable.
Batch invariance
Requests return identical results regardless of what else is in the batch, through deterministic choices in attention reduction ordering, sparse attention token selection, expert matmul kernel selection, router tie-breaking and cross-GPU all-reduce. Reproducibility at temperature 0 means an eval result is a property of the checkpoint rather than of the batch it happened to land in.
Because training and serving live on the same platform, a promising checkpoint can be promoted and validated while training continues, then moved into production without leaving the platform.
Build your own frontier
•
Build a frontier legal organization -
Harvey
•
Train your own model on Fireworks -
Training docs
•
Learn more about
Frontier-lab training infrastructure as a service
Related Posts
Partner Announcements
12/15/2025
NVIDIA Nemotron 3 Nano on Fireworks: The Engine for Next-Generation AI Agents
Partner Announcements
11/24/2025
Fireworks Expands AWS Alliance: Strategic Collaboration Agreement + GenAI Competency
Partner Announcements
10/20/2025
Fireworks and AMD partner to power the next gen of AI infrastructure on AMD Instinct™ GPUs
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
