---
title: "Training API now generally available"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/train-past-the-frontier-training-api-now-generally-available"
scraped: "2026-09-01T06:00:48.904073+00:00"
lastmod: "2026-09-01T02:20:06.000Z"
type: "sitemap"
---

# Training API now generally available

**Source**: [https://fireworks.ai/blog/train-past-the-frontier-training-api-now-generally-available](https://fireworks.ai/blog/train-past-the-frontier-training-api-now-generally-available)

Training API now generally available
Product
Solutions
Models
Pricing
Resources
Log In
Get Started
Blog
Train Past The Frontier Training API Now Generally Available
Train past the frontier: Training API now generally available
PUBLISHED
8/31/2026
Table of Contents
Own your intelligence
Training API, now generally available
Why teams train on Fireworks
Correctness: Training and inference alignment
Performance efficiency: Maximized throughput across the RL loop
Development speed: Compressed iteration cycle
Getting started: Fireworks Lab can help
Table of Contents
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
Own your intelligence
Explore training
Table of Contents
Own your intelligence
Training API, now generally available
Why teams train on Fireworks
Correctness: Training and inference alignment
Performance efficiency: Maximized throughput across the RL loop
Development speed: Compressed iteration cycle
Getting started: Fireworks Lab can help
Table of Contents
Own your intelligence
Explore training
Own your intelligence
The next frontier of competitive advantage is specialized intelligence. The most ambitious companies are training models with the capabilities that underpin differentiated products and operations, across coding, chip design, cybersecurity, and beyond:
•
Harvey
post-trained Kimi K3 for long-horizon legal work using asynchronous RL. Harvey Tenet scored 19.7% all-pass on LAB against 10.8% for base Kimi K3 at effectively flat cost per task.
•
Vercel
used RFT and speculative decoding to fine-tune an open model for v0's auto-fixer, reaching a 93% error-free generation rate for v0 and 40x end-to-end latency improvement.
•
Heidi
moved its clinical scribe onto open models it fine-tuned, going from POC to production in four weeks and achieving 3.5x lower latency.
•
Factory
fine-tuned two small LoRA adapters (one to flag risky secrets, one to clear false alarms) on an open Qwen base. At a 5% false-alarm budget, the trained model caught about 70% of real secrets versus ~59% for GPT-5.5, while being faster and more cost-effective.
Across these workloads, training a base model for specific tasks improved quality, latency, cost, and/or behavioral consistency. Fireworks makes this level of specialization accessible to teams through three training surfaces, each designed for a different level of expertise, operational ownership, and control.
Training API
Managed Training
Fireworks Lab
Built for
ML Researchers
ML Engineers
All Levels
Workflow
Bring your own data and loop for deepest control. From LoRA and per-token pricing to full-parameter and reserved capacity.
Bring your data or evals, we run the loop. Pick your method (SFT, RFT, DPO) and run via UI/API.
We provide embedded ML researchers and forward-deployed engineers. Engagements range from co-design to custom build.
No infrastructure to manage: Choose your method on Managed Training or write your own loop with the Training API.
Today, we are announcing the general availability of our Training API and Fireworks Lab.
Training API, now generally available
We’ve worked with ML teams around the world to understand where existing training workflows fall short: constrained model and method choice, limited control over parameters and training loops, rigid and underutilized compute, and fragmented training and rollout infrastructure that bloats costs, creates synchronization overhead, and introduces numerical drift. Those partnerships shaped our Training API.
The Fireworks Training API connects your custom training loop to Fireworks-managed distributed training and rollout infrastructure. You orchestrate the loop in Python from wherever you choose, with full control over your loss or reward, data, and environment. Fireworks manages high-performance compute: the trainer computing gradients and updating the model, and the rollout deployment generating samples from the trained model. Fireworks also manages the interaction between these two, from weight synchronization to failed-swap recovery, and train-rollout alignment. All of this allows you to focus on refining your learning signal, not infrastructure challenges.
python
Copy
1
2
3
4
5
6
7
def
reward_fn
(
completion
:
str
,
row
:
dict
)
-
>
float
:
"""Return 1.0 if the model's numeric answer matches the ground truth."""
predicted
=
extract_answer
(
completion
)
truth
=
extract_answer
(
str
(
row
.
get
(
"ground_truth"
,
""
)
)
)
if
predicted
is
None
or
truth
is
None
:
return
0.0
return
1.0
if
predicted
==
truth
else
0.0
Example of a custom reward function defined in Python. This code can be dropped directly into a training loop using the Fireworks Training API.
One API, two compute options.
Choose Serverless when speed to experiment matters most, or talk to us about Dedicated when scale, control, and GPU economics take priority.
Serverless training
allows you to train LoRA adapters on top of shared infrastructure. You pay per token, and sampling runs in the same session. Use it to iterate on experiments, de-risk a larger run, or run RL loops that alternate between rollout and training.
Deploy a promising checkpoint to production inference instantly through the UI (Managed Training) or API (Training API & Managed Training). With multi-LoRA deployment, each customer or use case gets its own tuned model without standing up separate infrastructure.
Dedicated training
is best when you need full-parameter training, models beyond the serverless pool, larger context lengths or LoRA ranks, or sustained throughput where per-GPU-hour pricing is more economical than per-token. Fireworks gives you dedicated, elastic capacity sized to each run, with the ability to scale GPU type and cluster size as needed.
Serverless
Dedicated
Parameter mode
LoRA
LoRA and full-parameter
Models
A curated list of popular models
Unlimited depth and breadth, up to the largest MoE models
Provisioning
Attach to an always-on shared pool, nothing to spin up
Trainer and deployment provisioned for your run; support for disaggregation to speed up training across trainer or rollout
Throughput
Shared capacity and per-account rate limits
No contention, scale up as you need
Billing
Per-token
Per-GPU-hour
"The Fireworks self-serve API has boosted our experimentation velocity and overall productivity, freeing up Figma's AI team to spend more time on science and research, and less time debugging infrastructure. We're able to iterate faster and build features that make a real difference in design and product development workflows."
— Sumithra Bhakthavatsalam, AI Research Manager, Figma
Start on Serverless in minutes, nothing to spin up:
Start training →
Why teams train on Fireworks
Fireworks is among the few organizations outside the frontier labs to have operated reinforcement learning (RL) across more than 10,000 GPUs. RL turns training and inference into one continuously coupled system; every step starts with rollouts from the current policy, updates the weights, and feeds those weights back into inference for the next round of sampling. At frontier scale, the algorithm is only part of the challenge. Effective RL hinges on three requirements: correctness, performance efficiency, and development speed.
Correctness: Training and inference alignment
For correctness in RL training, the rollout engine and trainer need to share the same numerical definition. Small numerical drift can corrupt a learning signal, from token clipping to reward collapse, when everything appears to be working. With Fireworks,
•
Numerical formats match end to end.
Differences in precision or quantization between training and inference can change the values the model computes, even with the same weights. Fireworks aligns trainer and rollout numeric formats (e.g. BF16, block-wise FP8, and NVFP4) so the model the trainer saves is the one that the rollout deployment runs.
•
Kernels match, too.
The same numeric format does not guarantee the same computation. Floating-point reductions, kernel selection, and parallelism can produce different numbers even at identical precision, so Fireworks aligns the underlying implementations across both paths.
•
MoE execution stays consistent.
Small numerical differences can change which experts fire and send a token down a different computational path. Fireworks uses Router Replay to preserve expert selections between rollout and backward pass, alongside batch-invariant kernels and deterministic reductions for supported frontier MoEs.
Fireworks validates this alignment directly by running the same sequences through the rollout engine and trainer and measuring train-inference KL divergence (KLD). All models launched on Fireworks training are continually validated to ensure KLD is minimized.
Performance efficiency: Maximized throughput across the RL loop
At scale, RL is largely a generation problem. Much of the wall-clock time is spent producing rollouts rather than updating weights, so rollout throughput and GPU utilization become primary determinants of training time and cost. Completion lengths also vary widely, which means rigid batching can leave GPUs idle while a small number of long-running trajectories finish.
Fireworks can run asynchronous RL, overlapping rollout collection with training rather than forcing the two sides of the loop to execute sequentially. Rollout GPUs can begin generating the next batch while the trainer updates on the previous one, with bounded weight staleness available when the algorithm permits more overlap. The objective is simple: keep GPUs doing useful work instead of waiting at synchronization barriers.
Once the loop completes a training step, the updated model must be transmitted and loaded into the rollout deployment. Rather than tearing down the rollout deployment and reloading a full model after every step, Fireworks hot-loads new weights into the running deployment. For full parameter checkpoints, novel compression techniques are used to reduce the bandwidth and storage requirements for weight transmission. An XOR Diff is computed between current and previous weights, and zstd compression is used to reduce the size of this payload. This results in up to a 10x reduction in transmission bandwidth, significantly speeding up the training loop.
Development speed: Compressed iteration cycle
The bottleneck to production is often not the training job, but the time between iterations. In a fragmented stack, every cycle means moving checkpoints between training and inference systems, redeploying, reconciling differences, running evals, and starting again.
Fireworks turns that process into a continuous development loop: train → deploy → evaluate → retrain on one platform. Checkpoints move directly into serving, while production traces, evals, and feedback feed the next training run. And because we handle GPU provisioning, capacity, and configuration, customers skip the procurement, model enablement, and infrastructure-sizing work that slows iteration and time to market. Teams report 2–4x more iterations on the same training budget, compressing model development from weeks to hours and accelerating time to production.
Getting started: Fireworks Lab can help
With correctness, performance efficiency, and iteration speed built into the platform, teams can focus on their training strategy. The strategy includes the decisions that shape model quality: the training loop, data, rewards, evaluators, and harness design. It also includes the systems choices that determine how the workload should run at scale, such as synchronous versus asynchronous RL, acceptable weight staleness, rollout-to-trainer allocation, parallelism, and checkpoint and hot-load strategy.
Fireworks Lab helps teams make those decisions more confidently and execute faster. Forward-deployed researchers and engineers embed directly with your team. A full engagement starts with a diagnosis that defines the capability, baseline, success criteria, and scope, then moves into a time-boxed implementation built backward from your target date. You keep the production-ready model, evaluation harness, data pipelines, training loop, and recipes.
"Fireworks helped us move our clinical scribe off closed frontier models and onto open models we fine-tuned ourselves, from proof of concept to production in four weeks. Optimizing both the fine-tuning and serving on one platform allowed us to hit a clinical quality bar this quickly."
— Yu Liu, CTO at Heidi Health
Talk to Fireworks Lab →
Related Posts
Company News
7/15/2026
Announcing our Series D and $1B ARR
Company News
4/6/2026
Own Your AI: Fireworks Training Preview
Company News
3/8/2026
Introducing Fireworks on Microsoft Foundry: Bringing Best-in-Class Open Model inference to Azure
Next
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
