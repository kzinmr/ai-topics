---
title: "Own Your AI: Fireworks Training Preview"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/training-preview"
scraped: "2026-05-10T01:27:46.442135+00:00"
lastmod: "2026-04-08T04:48:14.000Z"
type: "sitemap"
---

# Own Your AI: Fireworks Training Preview

**Source**: [https://fireworks.ai/blog/training-preview](https://fireworks.ai/blog/training-preview)

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
Training Preview
Own Your AI: Fireworks Training Preview
PUBLISHED
4/6/2026
Table of Contents
What Teams Have Built
RL: Agentic Behavior That Prompt Engineering Can't Reach
SFT: The Foundation That Beats Closed Models
Classification: Fine-Tuning Wins Across Every Use Case
DPO: Alignment Without Writing a Reward Function
Full-Parameter Training at Frontier Scale
Numerical Parity Between Training and Inference
Three Surfaces, One Platform
Training Agent
Managed Training
Training API
Get Started
Table of Contents
Table of Contents
What Teams Have Built
RL: Agentic Behavior That Prompt Engineering Can't Reach
SFT: The Foundation That Beats Closed Models
Classification: Fine-Tuning Wins Across Every Use Case
DPO: Alignment Without Writing a Reward Function
Full-Parameter Training at Frontier Scale
Numerical Parity Between Training and Inference
Three Surfaces, One Platform
Training Agent
Managed Training
Training API
Get Started
Table of Contents
Fireworks Training
is now in preview: an end-to-end platform for training and deploying frontier models at scale. Three surfaces for three kinds of teams, from a conversational agent that handles everything, to managed infrastructure for ML engineers, to bring-your-own training loop on Fireworks-hosted clusters. All on the same infrastructure that already handles production inference for Cursor, Vercel, Genspark, and others.
What's new today:
•
Full-parameter training at frontier scale, from Qwen3 8B to Kimi K2.5 at 1T parameters
•
Custom loss functions via the Training API
•
Multi-LoRA serving for teams iterating across multiple adapters
•
Training Agent: describe your task, deploy your model
All three surfaces are in preview now.
What Teams Have Built
RL: Agentic Behavior That Prompt Engineering Can't Reach
Reinforcement learning is how teams push past the ceiling SFT hits on multi-step reasoning, reliable tool use, and mid-flight self-correction.
Vercel
used our RL infrastructure
to build a custom "Auto Fix" model for v0. The model checks the output stream for errors and self-corrects without a second pass, reaching a
93% error-free generation rate
, significantly outperforming closed frontier models, with a
40X improvement in end-to-end latency vs. the proprietary model it replaced
and over 8,000 characters per second throughput.
"Using a fine-tuned reinforcement learning model with Fireworks, we perform substantially better than SOTA. In our evaluation, Sonnet 3.5 compiled at 62%, and we got our error-free generation rate well into the 90s."
— Malte Ubl, CTO at Vercel
Genspark
applied frontier RL to Kimi K2
, a 1 trillion parameter open-source model, for deep research agents requiring multi-source investigation and chained tool calls. The RL-trained model unlocked a
33% increase in tool calls
, surpassing a state-of-the-art closed model at
50% lower cost
.
"Fireworks enabled us to own our AI journey, and unlock better quality in just four weeks."
— Kay Zhu, CTO at Genspark
Cursor
ran RL rollouts for Composer 2 (now top-scoring on CursorBench) across 3 to 4 clusters worldwide, with training and production traffic sharing the same GPU pool via delta-compressed weight updates.
Frontier RL doesn't require one mega-cluster.
The assumption that you need co-located RDMA hardware rests on moving a full 1 TB checkpoint on every update. You don't.
"Our RL inference scales elastically and globally because of it. When we have low prod traffic we scale up RL, when we have high prod traffic, we scale down RL."
— Federico Cassano, Research at Cursor
SFT: The Foundation That Beats Closed Models
RL gets the headlines, but the truth is most teams start their fine-tuning journey with SFT and the gains are immediate. The most common pushback we hear is that closed models are "good enough."
On a customer support dataset, a fine-tuned Qwen3 8B Instruct model hits an F1 score of 76.38% vs 69.40% on leading closed source model. In fact Qwen3 0.6B, 4B, and 30B all outperform the closed model on this benchmark, at significantly lower cost. On a production customer operations dataset, fine-tuned Qwen3 30B reaches 91.71% versus the closed model's 82.48%.
Classification: Fine-Tuning Wins Across Every Use Case
On a ticket routing task, fine-tuned Qwen3 30B reaches 80.91%, a 19-point gap over Claude Haiku (61.47%) and 9 points over Gemini Flash (71.93%). Fine-tuned Qwen3 models at every size beat or match Gemini Flash, produce zero invalid outputs (versus 15% for Claude Haiku), and run 2.5–20X faster at p50–p95 latency.
DPO: Alignment Without Writing a Reward Function
For tasks where correctness is hard to label but preference is easy to express: structured outputs, compliance judgments, domain-specific alignment. DPO closes the gap between a capable model and a trustworthy one.
Evaluated across 100 samples per task by an independent LLM judge.
Full-Parameter Training at Frontier Scale
Most training services cap out at LoRA. LoRA is the right starting point: fast, cost-effective, and well-suited for rapid iteration. But
LoRA and full-parameter training learn in meaningfully different ways
. LoRA learns less and forgets less. Full-parameter produces behavioral changes that adapter-based methods can't reach.
Fireworks Training now supports full-parameter training from Qwen3 8B on a single node to Kimi K2.5 (1T parameters) on 64x B200s. Getting there required solving distinct distributed systems problems at each scale: composable parallelism across FSDP, pipeline, context, and expert dimensions; Blackwell-native MXFP8 for expert computation; and streaming pipeline parallelism so RL rollout data trains as it arrives rather than waiting on batch accumulation.
More detail in the training infrastructure writeup.
LoRA and full-parameter run on the same platform. You don't have to choose your ceiling when you start.
Numerical Parity Between Training and Inference
Fireworks runs production inference across DeepSeek, Kimi, Qwen, and others at scale. That's not background — it's the reason the training infrastructure is trustworthy. The numerical edge cases that surface in frontier MoE models aren't hypothetical for us. We've already debugged them, in production, on the same hardware.
The hardest part wasn't performance. It was correctness.
MoE models are numerically fragile in ways dense models aren't.
A small hidden-state change can flip expert selection and cascade through subsequent layers. Kernel fusions that are mathematically equivalent produce numerically different results because floating-point addition is not associative. For RL workloads, KL divergence between training and inference logprobs anchors the reward signal. If those two stacks disagree numerically, your evals are measuring the gap between them, not model quality.
We publish k3 KL divergence across training and inference checkpoints for every model in our catalog. All values below 0.01 are production-grade. These values cover the full inference catalog; the subset available as training shapes today is noted in the Three Surfaces section below.
Three Surfaces, One Platform
The bottleneck is rarely the algorithm.
It's integration friction and iteration speed. Start at whatever level of abstraction fits your team. Drop down when you need more control. Same platform, same deployment targets throughout.
Training Agent
For product teams going from data to deployed model without ML infrastructure
Describe your task, upload your data. The Agent formats it, picks a base model, runs a hyperparameter sweep, writes evals, and deploys. No training infrastructure to manage. Currently LoRA-only.
"For the first time, any team with data and a use case can own a model that's genuinely theirs, trained on their product, their customers, their domain. We're not just making model training easier. We're making model ownership the default."
— Lin Qiao, CEO, Fireworks AI
Managed Training
For ML engineers who want reliable infrastructure without managing it
Bring formatted data, choose SFT, DPO, or RFT, and we handle the rest. Native RFT lets you define a reward function instead of authoring thousands of demonstrations. Full-parameter training available for the deepest behavioral changes. Multi-LoRA lets you serve multiple fine-tuned adapters on a shared base model, so teams that can't yet saturate a full node aren't paying for dedicated serving infrastructure per experiment.
Training API
For research teams and advanced ML platform teams who need full algorithmic control
Bring your own training loop. The platform has no opinion on your objective. Write custom loss functions — GRPO, DRO, DAPO, or anything else — chain SFT into RFT runs with full optimizer state preserved, or run frontier RL across regions with Fireworks handling rollout inference and weight sync. LoRA and full-parameter supported.
"The Fireworks Training SDK lets us focus on our research instead of wrestling with infrastructure. The platform is fast, well-optimized, and just works."
— Kyle Montgomery and Sijun Tan, Core Contributors, rLLM
Get Started
Your model is your product. Your data is your moat. Fireworks Training is how you build both.
Fireworks Training is in preview.
Start Here
Further reading:
Scaling and Optimizing Frontier Model Training
·
Frontier RL Is Cheaper Than You Think
·
When Faster ≠ Identical: Numerical Pitfalls in MoE Models
·
The Fine-Tuning Bottleneck Isn't the Algorithm
*
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
