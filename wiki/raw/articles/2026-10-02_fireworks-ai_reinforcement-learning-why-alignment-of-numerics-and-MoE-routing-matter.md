---
title: "Reinforcement learning: Why alignment of numerics and MoE routing matter "
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/reinforcement-learning-why-alignment-of-numerics-and-MoE-routing-matter"
scraped: "2026-10-02T06:00:12.508148+00:00"
lastmod: "2026-10-01T21:43:22.000Z"
type: "sitemap"
---

# Reinforcement learning: Why alignment of numerics and MoE routing matter 

**Source**: [https://fireworks.ai/blog/reinforcement-learning-why-alignment-of-numerics-and-MoE-routing-matter](https://fireworks.ai/blog/reinforcement-learning-why-alignment-of-numerics-and-MoE-routing-matter)

Join us for our inaugural conference, Forge 2026
Product
Solutions
Models
Pricing
Resources
Log In
Get Started
Blog
Reinforcement Learning Why Alignment Of Numerics And Moe Routing Matter
Reinforcement learning: Why alignment of numerics and MoE routing matter
PUBLISHED
9/30/2026
Table of Contents
TL;DR
RL at scale is a systems problem
What our experiments revealed
Numerical mismatch can derail learning
Mixture-of-Experts models are even harder to align
How numerical differences disrupt learning
Probability mismatch can distort updates
MoE routing can amplify the mismatch
Fireworks keeps the training loop consistent
Table of Contents
Table of Contents
TL;DR
RL at scale is a systems problem
What our experiments revealed
Numerical mismatch can derail learning
Mixture-of-Experts models are even harder to align
How numerical differences disrupt learning
Probability mismatch can distort updates
MoE routing can amplify the mismatch
Fireworks keeps the training loop consistent
Table of Contents
TL;DR
•
Numerical mismatch can derail training: in a Fireworks GLM 5.2 experiment, the same algorithm and data produced collapsing reward without alignment and stable reward with alignment over 25 steps.
•
Training MoE models adds complication to alignment: our Qwen3.5-MoE investigation found that differences in how expert outputs were combined caused disagreement even when one implementation used higher precision.
•
These discrepancies can distort training updates and resemble problems with data, rewards, or learning rate, sending teams through expensive experiments that leave the underlying cause unresolved.
•
Frontier training requires co-optimized training and inference: Fireworks develops and validates the trainer and rollout engine together so teams can scale reinforcement learning with alignment across numerics, kernels, and MoEs.
RL at scale is a systems problem
Rollout generation can account for most of the time spent on reinforcement learning (RL). ML teams often use a separate inference engine to generate rollouts efficiently. But that engine can use kernels, precision, batching, and parallelism that differ from the trainer. Now there are two implementations of the policy: the one generating the tokens and the one computing the gradients. Even with identical weights, they can assign different probabilities to the same tokens.
If the training algorithm does not account for that mismatch, it can distort updates and destabilize learning. In a mixture-of-experts (MoE) model, that mismatch can also flip a routing decision. When router scores are nearly tied, a rounding difference can change which experts fire. The same token then takes different computational paths through the model.
Our experiments show where numerical differences arise, why router replay alone is insufficient, and what it takes to close the gap.
What our experiments revealed
Numerical mismatch can derail learning
In a
Fireworks experiment
, we ran the same RL task twice on GLM 5.2: a countdown reasoning problem, with the same algorithm and the same training data. The only change was whether the trainer and the rollout engine calculated token probabilities the same way.
When they didn't, the run fell apart. The two systems disagreed by a KL of about 0.013, and the standard safeguards were throwing out roughly 45% of every batch just to keep training stable. Even that wasn't enough. Reward climbed to about 0.9, then collapsed to under 0.2 around step 20 as the model chased a target that no longer matched what it had generated. With the numbers aligned, KL was zero, nothing was thrown out, and reward held steady for the full run.
Fireworks GLM 5.2 countdown experiment: reward collapsed without numerical alignment and remained stable with alignment over 25 training steps. The zero-KL result applies to the tested LoRA configuration.
The numerical implementation changed the outcome without a change to the algorithm or data. That makes agreement between the trainer and rollout engine an important check before committing to more runs with changes to the training recipe
Mixture-of-Experts models are even harder to align
With routed experts, there are many places where "mathematically equivalent" optimizations produce numerically different results. A
Fireworks training experiment with Qwen3.5-MoE
traced a significant numerical mismatch to how expert outputs were combined.
On image tokens, the training path diverged from the Hugging Face reference by a k3 of 0.296, roughly 300 times the 0.001 threshold we use to call two paths equivalent. At that level, the two copies of the model disagreed about as much as two different models would.
The team traced the gap to MoE aggregation by swapping only the MoE blocks for Hugging Face's reference modules and leaving the rest of the stack alone. The k3 values for both text and image tokens dropped to zero. Further investigation identified differences in the precision used to weight and sum expert outputs.
The finding shows why matching expert selections alone is insufficient: the numerical precision and execution order used to combine their outputs must also align.
Fireworks’ Qwen3.5-MoE experiment comparing three expert-output aggregation paths and the precision used at each step.
The GLM experiment showed what numerical mismatch can mean for learning: a run that consumes compute while reward collapses. The Qwen investigation showed how easily that mismatch can escape checks on individual layers. For researchers, the symptoms can resemble problems with data, rewards, or learning rate, leading to additional runs that change the recipe without addressing the underlying cause.
How numerical differences disrupt learning
Probability mismatch can distort updates
Training and inference software often use different levels of numerical precision or perform operations in a different order. Because intermediate results are rounded,
(a + b) + c
can differ from
a + (b + c)
. Across a model’s computations, those differences can change the probabilities assigned to the same tokens. Floating-point addition isn’t associative, and RL is a very expensive way to find out.
Many RL algorithms use probability ratios to guide updates. An unaccounted-for difference between the rollout engine and trainer can change those ratios before any learning has happened. That can alter how strongly tokens influence the update or trigger clipping because of execution differences. The
verl rollout correction documentation
explains how corrections account for this gap.
A rollout can look reasonable even when the trainer assigns different probabilities to its tokens. Checking generated text alone will not reveal that discrepancy. Comparing probabilities at identical weights exposes it; training–inference KL measures the disagreement.
MoE routing can amplify the mismatch
In a Mixture-of-Experts model, a small numerical difference can also change which experts process a token. When routing scores are nearly tied, rounding can tip the selection toward a different expert. The token then passes through different weights, potentially magnifying the discrepancy through subsequent layers.
The
R3 researchers
showed that inconsistent routing can destabilize RL. Their router replay method records routing decisions during rollout generation and reuses them during training. It stabilized training in the settings they tested.
Router replay keeps expert selections consistent, but differences in how their outputs are calculated and combined can remain. Keeping rollout and trainer probabilities aligned requires engineering across both implementations, including their kernels, precision, and execution order. That work is part of the infrastructure needed to run a training recipe reliably.
Fireworks keeps the training loop consistent
Fireworks develops the trainer and rollout engine together, taking on the complex engineering required to keep fast rollout generation consistent with training. This reduces the risk of expensive runs lost to implementation discrepancies, leaving more of the training budget for testing and scaling promising recipes.
Our approach includes three key elements:
Numerical alignment: make the calculations agree.
Alignment covers how the model executes across both systems, including attention, expert computation, aggregation, and operations across GPUs.
Router replay: use the same experts.
Router replay support
provides teams using their own trainer with the expert selections recorded during rollout generation. Integrating those records into training enables the trainer to reuse the same selections.
Validation: measure agreement across the full model.
Comparing token probabilities at identical weights reveals discrepancies that checks on individual operations can miss. Ongoing validation uses training–inference KL to measure agreement under varying batch conditions for models launched on Fireworks Training. The GLM comparison above is one published example.
Frontier training requires frontier inference.
Run your RL training loop with the Fireworks Training API
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
Resources
Blog
Demos
Cookbooks
Company
Leadership
Investors
Careers
Trust Center
Privacy Choices
© 2026 Fireworks AI, Inc. All rights reserved.
