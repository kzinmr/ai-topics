---
title: "Fireworks AI"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/K3-LoRA-Training"
scraped: "2026-07-28T06:00:04.252685+00:00"
lastmod: "2026-07-27T17:05:00.000Z"
type: "sitemap"
---

# Fireworks AI

**Source**: [https://fireworks.ai/blog/K3-LoRA-Training](https://fireworks.ai/blog/K3-LoRA-Training)

Kimi K3 on Fireworks: Frontier Intelligence You Can Own
Product
Solutions
Models
Pricing
Resources
Log In
Get Started
Blog
K3 Lora Training
Make Kimi K3 Yours: LoRA Training on Fireworks
PUBLISHED
7/26/2026
Table of Contents
First, a quick primer
Cost Efficiency at Scale: Pay-Per-Token Training and Flexible Serving
Why Fireworks Serverless Training
How LoRAs learn reliability for your tasks
Task 1: teach K3 a new objective (Countdown)
Task 2: teach K3 to work through a problem step by step (Frozen Lake)
Your Model Is Only as Good as Your Reward
Try it
Beyond LoRA
Table of Contents
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
Table of Contents
First, a quick primer
Cost Efficiency at Scale: Pay-Per-Token Training and Flexible Serving
Why Fireworks Serverless Training
How LoRAs learn reliability for your tasks
Task 1: teach K3 a new objective (Countdown)
Task 2: teach K3 to work through a problem step by step (Frozen Lake)
Your Model Is Only as Good as Your Reward
Try it
Beyond LoRA
Table of Contents
Kimi K3 is now available for Multi-LoRA serving and training in private preview with
Fireworks Serverless Training.
Kimi K3 is a massive mixture-of-experts model with roughly 2.8 trillion total parameters, the first open-weights model to reach the 3T parameter scale. Training a model this massive used to be a big project. As of today it is a one-line change on Fireworks.
The secret? LoRA adapters: cheap to train, cheap to serve, and powerful enough for meaningful K3 post-training. With Fireworks Training, you can take the best open model in the world and cheaply teach it to nail your exact task, without paying frontier prices or touching a GPU cluster.
First, a quick primer
LoRA (Low-Rank Adaptation)
•
Instead of training every single parameter of a model, you train a small side-car of weights (called an
adapter
) on top of the model.
•
It's the cheapest way to train and easy to store: the adapter is only megabytes.
•
Best for behavior and style: personas, tone, format, structured outputs, a new objective, a tool-using loop.
•
Complexity is set by the adapter's
rank (r)
. Even a rank-1 adapter, a single direction of change, can meaningfully steer behavior, which is why LoRA punches so far above its size.
Serving a LoRA on Fireworks
Once trained, an adapter loads into an inference deployment for evaluation or production. We offer two ways:
Live merge
folds a single adapter into the model at deploy time, so it runs at full base-model speed with no overhead.
Multi-LoRA
hosts many adapters on one deployment and routes each request to the right one.
Either way, the base weights sit in memory once, so with many adapters on top the marginal cost of each new fine-tune is close to zero. See the
deploying LoRAs guide
.
Cost Efficiency at Scale: Pay-Per-Token Training and Flexible Serving
Fine-tuning a frontier model is genuinely hard. It takes work across three layers: the research itself, trainer implementation and optimization, and infrastructure and GPU management. Serverless training on Fireworks is your new infrastructure team, collapsing all three so a researcher can operate without a dedicated infra team behind them.
There's no trainer to spin up and no reserved GPU cluster to book. There's no trainer to spin up and no reserved GPU cluster to book. The loop is yours: your code calls forward_backward, steps the optimizer, and samples your latest weights in the same session. Fireworks runs those operations on a shared pool of GPUs. You keep the training logic, we handle the hardware. Nothing to start, nothing to tear down. Nothing to start, nothing to tear down.
"At HUD, we run agents across thousands of concurrent environments to produce the best post-training data for some of the most demanding labs in the world. That means the training layer underneath has to be best-in-class. Our training also comes in bursts as we're constantly iterating on environments and rewards, and the last thing we want is to babysit a cluster or pay for idle GPUs between runs. Fireworks serverless training meets both requirements: we point our loop at one endpoint, attach to a warm pool in seconds, and pay per token instead of by the reserved hour. We scale to whatever the workload requires without thinking about GPU clusters, keeping the team focused on environments and reward quality, where the real work is."
Lorenss Martinsons, Founder & Co-CEO at HUD
Change the rank (r) to match the adapter's capacity to your task, and iterate. Preview accounts run up to 8 concurrent training jobs with generous rate limits, so you can test several ideas in parallel.
Why Fireworks Serverless Training
You pay per token. A small reinforcement learning run, roughly 20 steps and 860K training tokens, costs about $65 all in, training plus sampling, and finishes in 30 to 60 minutes depending on pool load. Reinforcement learning is the primary use case: sample from the adapter, score it with your reward, take a step, repeat. And with full KV-cache awareness, multi-turn agent runs cost far less, since repeated context bills at just 20 percent of the standard prefill rate. See the
serverless training guide
for more.
When you outgrow the shared pool, the same SDK runs on
dedicated training
, the same path for full-parameter training, DPO, sustained RL, and explicit control over checkpoints, deployments, and lifecycle.
We also
guarantee consistent numerics alignment
between training and inference across both serverless and dedicated, so what you see in a training rollout is what you get in production. When your model is ready, deploy it straight to inference with one click, with no re-platforming and no handoff.
How LoRAs learn reliability for your tasks
To see LoRA in action, we picked two tasks that look like the work people actually ship. Then we trained a single small adapter on top of K3 for each one and watched it learn. No full-parameter run. No touching the base weights. Just a small adapter and a few dozen steps of practice.
Task 1: teach K3 a new objective (Countdown)
A common reason people fine-tune models is to teach it how to achieve a goal efficiently using knowledge it already has.
The
Countdown
task hands the model a few numbers (45, 14, and 39) and a target number (20). The model has to hit the target using arithmetic (45 - 39 + 14 = 20). The model is graded on its final distance from the target: partial credit for getting close, full credit for hitting it. The model already knows how to add and multiply. What it has to learn is the goal itself: keep combining numbers until you land on the target, then stop.
K3 starts off decently, getting ~80% of the way to its goal in most cases, but it can do better. It just has to learn this new objective and within about ten steps it locks in and holds near a perfect solve rate. This task shows us that when a task is mostly about learning behavior over facts, a small adapter can pick it up quickly.
You can reproduce this in a few minutes. The code is at the end of this post.
Figure 1: Countdown Chart
Task 2: teach K3 to work through a problem step by step (Frozen Lake)
Another common reason people turn to fine-tuning is to teach their tool-calling agent how to achieve a goal by using its toolset efficiently.
The
Frozen Lake
task puts the agent on a grid and asks it to move from start tile to a goal tile, without stepping into a hole. Each turn, K3 looks at the grid, calls a single move tool (up, down, left, or right), observes what happened, and decides its next move. It keeps going, turn after turn, until it reaches the goal or fails.
This is the loop behind real agents: look, act, observe, repeat. And the reward is equally realistic. Unlike Countdown, the model cannot earn partial credit for simply wandering in the right direction. It can only get full credit if it reaches the goal and will earn nothing if it fails.
This time, K3 starts off close to a coin flip because the model has to learn the whole loop of moving, checking, and deciding. after only a few attempts it settles near the top and by the end of training it reaches the goal on almost every run.
Figure 2: Frozen Lake Reward Per Training Step
Let’s break that graph down a different way. Same x-axis but this time at each training step, look at how many times K3 reached the goal, and how many times it went nowhere. On the first step, K3 reached the goal as often as it failed (map that to the 50% in the first step in the above graph).
Figure 3: Frozen Lake Attempts Per Step
The success and failure lines separate quickly and by the end almost every attempt gets to the end and the failures have all but disappeared. K3 didn’t just get a little better. It went from rarely finishing to reliably finishing.
Your Model Is Only as Good as Your Reward
LoRA makes training so comparatively cheap that the challenge is no longer whether you can afford to train, it’s deciding what exactly to reward. Getting a LoRA to train well still takes the usual care: you tune the learning rate and the rank until the run is healthy. But the reward is the lever that decides what the model is aiming at, and in both examples above it shaped the curve more than anything else.
Countdown gave partial credit, so the model earns something for getting closer. That signal is dense, and the curve rises quickly and smoothly. Frozen Lake paid only for reaching the goal. That signal is sparse and noisier, so the reward took longer to start climbing. The model earns something for getting closer, so the signal is
dense
and the curve rises quickly and smoothly.Frozen Lake paid only for reaching the goal. The signal is
sparse
and noisier so it took longer for the reward to start climbing smoothly.
We had the same base model, same kind of adapter, two very different learning curves, mostly because of how we chose to score the task. That is the real skill in post-training today. There are many ways to design rewards, both sparse and dense, and while the training curves can look different, the goal is always the same: define “done and correct” clearly enough that a small adapter can reliably chase it. Get that wrong, and even full-parameter training won’t be able to save you.
Try it
The Countdown run above is the serverless RL quickstart. Install the SDK, clone the cookbook, and run it against a base model enabled on your account:
1
2
3
4
5
git clone
<
https
:
/
/
github
.
com
/
fw
-
ai
/
cookbook
>
pip install
-
e
.
/
cookbook
/
training
export
FIREWORKS_API_KEY
=
"fw_..."
python
-
m examples
.
serverless_rl
.
countdown_rl
K3 post-training is available if you r
equest access
and mention serverless training. For the serving details, see
deploying LoRAs
and
understanding LoRA performance
.
Beyond LoRA
For a single, bounded behavioral task there is almost always a rank value that gets you there. For many tasks, tuning is teaching a model how to combine capabilities it already knows, and a frontier model like K3 knows a lot of capabilities. Most of the time you are teaching it a surface form, and LoRA is good enough for that.
Full-parameter training still earns its place when the target gets broad or genuinely novel: training many unrelated tasks at once, broad distillation, continued pre-training, or a new language or domain. And if a full fine-tune does win, it may not be obvious why, so it can be worth trying a LoRA run first.
The real advantage shows up when training and serving live on one platform
. Train an adapter, deploy it with a single API call to an auto-scaling endpoint, monitor latency, accuracy, and cost in production, collect the feedback, failures, and edge cases, then trigger a fresh run on that new data. Each turn produces a smarter model.
That is the flywheel. LoRA makes the first turn cheap enough that anyone can start today, and because every cycle feeds the next, specialized intelligence compounds into a moat that widens the longer you run it.
Figure 4: The Data Flywheel
The flywheel doesn't stop here, and neither do we. More soon.
Explore us in AI tools
ChatGPT
Claude
Grok
Perplexity
CoPilot
Gemini
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
