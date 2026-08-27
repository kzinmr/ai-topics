---
title: "DeepSeek V4 Pro: Tops SWE-Bench & Cuts Cost per Task by 3x vs. Fable 5"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/DeepSeekV4Pro-Fable5"
scraped: "2026-08-26T06:00:57.407085+00:00"
lastmod: "2026-08-26T01:33:11.000Z"
type: "sitemap"
---

# DeepSeek V4 Pro: Tops SWE-Bench & Cuts Cost per Task by 3x vs. Fable 5

**Source**: [https://fireworks.ai/blog/DeepSeekV4Pro-Fable5](https://fireworks.ai/blog/DeepSeekV4Pro-Fable5)

DeepSeek-V4-Pro-0813 available now on Fireworks
Product
Solutions
Models
Pricing
Resources
Log In
Get Started
Blog
Deepseekv4pro Fable5
DeepSeek V4 Pro: Tops SWE-Bench & Cuts Cost per Task by 3x vs. Fable 5
PUBLISHED
8/26/2026
Table of Contents
Routing changes your bill
Training on Deepseek v4 Pro Available Now
What you should know about Deepseek’s Harness
Get started
Table of Contents
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
Table of Contents
Routing changes your bill
Training on Deepseek v4 Pro Available Now
What you should know about Deepseek’s Harness
Get started
Table of Contents
TLDR;
DeepSeek V4 Pro 0813 tops our SWE-Bench and LiveCodeBench runs, costs a third of Fable 5 per solved task, and turns out to be a better routing partner than Kimi K3. Training is live.
Last week we enabled Deepseek on Fireworks with serverless endpoints, dedicated deployments, and training support. The model provides a 1M-token context window with native tool calling and preserved reasoning history, targeting long-horizon agentic workloads.
We ran DeepSeek V4 Pro 0813 through the same eval suite we used for
Kimi K3 in July
. We evaluated Deepseek against Kimi K3 and Fable 5 across four benchmark families: SWE-Bench Verified, LiveCodeBench v6, Aider Polyglot v1, and Terminal-Bench 2.1. Deepseek V4 Pro is the strongest single model in this combined eval on two of four families.
Benchmark
Kimi K3
Deepseek V4 Pro 0813
Fable 5
SWE-Bench Verified (500)
92.6%
95.2%
85.4%
LiveCodeBench v6 (100)
88.0%
92.0%
91.0%
Aider Polyglot (225)
76.4%
73.8%
88.0%
Terminal-Bench 2.1 (89)
80.9%
76.4%
76.4%
Figure 1: Accuracy across Benchmarks with Oracle Routers
Deepseek V4 Pro delivers a massive cost advantage to Fable 5 on standard code tasks, running $0.309 per solved task on SWE-bench (vs. $0.808 for Fable 5) and $0.040 on LiveCodeBench (vs. $0.225).
On Terminal-Bench there are two key things to note about Fable 5’s performance and costs:
•
Fable 5 scores the same, but requires multiple attempts, bringing task costs to $16.85. We show this setup to stay consistent with our published K3 benchmark.
•
Scored on its first attempt, Fable 5 hits 74.2%, while cost per task leaps to $75.40. Internal evaluations rely on this primary-run baseline.
Where Deepseek V4 Pro is not as strong is the multi-language breadth. As we demonstrated in our
K3 analysis vs. Fable 5
, model specialization varies widely by ecosystem. On Aider Polyglot, V4 Pro stays strong in Rust (90.0%) and C++ (80.8%), but falls to 48.9% on Java (the largest slice at 47 tasks) compared to Fable 5’s 74.5%.
Java performance accounts for nearly the entire gap. If you run a Java-heavy codebase, you may face bottlenecks if you use a single model. As we discovered with our K3 testing, multiple models is a better solution than using a single-model architecture. Routing tasks dynamically to specialist models yields better overall accuracy at a fraction of the cost.
Routing changes your bill
We tested oracle routing between DeepSeek V4 Pro and Fable 5, picking the better model per task and breaking ties toward the lower cost one. As a quick refresher: oracle routing is a method for measuring the best theoretical performance by running the task through each model and then picking the cost-optimized correct option to establish the cost and performance ceiling.
On the 409-task combined cohort, routing hits 92.4% against Fable 5 alone at 86.6%. That is 5.9 points better than the frontier model, at $0.279 per task against Fable's $4.510. Sixteen times lower costs, and better. And 86.3% of tasks route to V4 Pro, which is the real finding: the expensive model is the exception, not the default.
Every V4 Pro pairing beats the equivalent K3 pairing. LiveCodeBench hits 94.0% against 92.0%, Aider reaches 93.3% against 91.6%, and the combined cohort lands at 92.5% against 91.1%. V4 Pro is a better router partner than K3 even though K3 scores higher on CyberGym, because V4 Pro's wins land on tasks Fable 5 misses.
Figure 2: Cost Per Task
It is worth noting what oracle routing is: an upper bound computed after the fact, not a policy you can deploy today. Real routers capture a fraction of it. This is important because the gap size tells you how much headroom exists.
Training on Deepseek v4 Pro Available Now
Want to build a specialized model tailored to your specific domain? DeepSeek V4 Pro training is live on Fireworks with full support for SFT, DPO, and RFT. You get frontier-grade infrastructure to push model performance without running into artificial platform limits. Once your run finishes, you can deploy your fine-tuned checkpoint to production in a single click. Because training and serving run on the same co-optimized backend, your production performance matches your training benchmarks every time.
What you should know about Deepseek’s Harness
Deepseek’s own published benchmark runs use the DeepSeek Harness (dsh) which is a native agent runtime handling everything from the model adapter down to the core execution loop. It speaks Deepseek V4’s native tool semantics instead of routing calls through a generic OpenAI-style interface. For this model, Deepseek also has not ship a standard chat template, so small serialization mismatches can silently drop model performance.
During testing on Fireworks, we found that a "minimal-first" setup yields much more consistent tool calls than jumping straight to the full standard catalog. Starting with a bare bash and editor surface before promoting to dsh standard brings DeepSeek V4 Pro much closer to the setup DeepSeek used in their own benchmark runs.
Get started
Whether you are looking to cut unit costs on autonomous agents, run zero-refusal security audits, or build a specialized domain model, DeepSeek V4 Pro gives you frontier-grade capabilities at half the cost per solved task. Across 840 traced adversarial security runs, it recorded zero refusals and zero output-length truncations, guaranteeing your agents complete their workloads without hitting unexpected guardrails.
Here is how you can start building today:
•
Serverless & Dedicated API:
Spin up deepseek-v4-pro-0813 directly on Fireworks serverless or provision dedicated capacity for production workloads.
•
Training:
Bring your domain data and train specialized checkpoints using our co-optimized SFT, DPO, and RFT infrastructure, deploying straight to production in a single click.
•
Check out our Security Evaluations on Deepseek:
here
Deploy Deepseek v4 Pro 0813 on Fireworks
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
