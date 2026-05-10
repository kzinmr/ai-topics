---
title: "The Fine-Tuning Bottleneck Isn't the Algorithm"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/fine-tuning-bottlenecks"
scraped: "2026-05-10T01:27:25.688599+00:00"
lastmod: "2026-04-08T03:57:21.000Z"
type: "sitemap"
---

# The Fine-Tuning Bottleneck Isn't the Algorithm

**Source**: [https://fireworks.ai/blog/fine-tuning-bottlenecks](https://fireworks.ai/blog/fine-tuning-bottlenecks)

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
Fine Tuning Bottlenecks
The Fine-Tuning Bottleneck Isn't the Algorithm
PUBLISHED
3/28/2026
Table of Contents
The Destination Is Always an Agent
The Bottlenecks That Show Up Every Time
Integration and Data Sovereignty
Iteration Velocity
Use the Right Tool for the Job
The Ladder from Managed to Full Control
Where We Are Heading
Start Fine-Tuning Today
Table of Contents
Table of Contents
The Destination Is Always an Agent
The Bottlenecks That Show Up Every Time
Integration and Data Sovereignty
Iteration Velocity
Use the Right Tool for the Job
The Ladder from Managed to Full Control
Where We Are Heading
Start Fine-Tuning Today
Table of Contents
Teams default to chasing the latest training algorithm, but the real bottlenecks are integration, iteration speed, and knowing when to reach for SFT vs. RFT vs. DPO.
TL;DR:
Integration friction and slow iteration cycles are the bottlenecks that actually stall fine-tuning — not the algorithm. We share the patterns we see across engagements, how teams like Cursor and Genspark broke through them, and where the workflow is heading: toward fully agentic fine-tuning loops that close themselves.
Most teams that come to us for fine-tuning are not struggling with the training algorithm. They are struggling with everything around it: getting reward functions to talk to internal APIs without leaking data, waiting days between experiments because each step lives in a different tool, and figuring out whether the problem even calls for SFT, RFT, or DPO. Over the past year, working with a select group of the most innovative startups, digital natives, and Fortune 500 companies, we have seen these patterns repeat across every engagement.
The Destination Is Always an Agent
Every team that comes to us for
fine-tuning
is building a domain-specific agent. Code fixing, customer support, deep research, financial operations — the use case differs but the shape is the same. A generic frontier model hits a quality ceiling and the path forward is model-level customization.
The ceiling is concrete.
Genspark
's Deep Research agent was stuck at a 0.76 reward score on closed frontier models. They moved to RFT on open models via Fireworks and pushed past 0.82 — a jump that prompt engineering alone could not deliver. One large digital native company we worked with saw a 30% increase in task quality and a 2.5x reduction in latency after fine-tuning with RFT. Prompt engineering can only get you so far, to reach a new capability tier you need fine tuning.
Within a single account, we saw use cases ranging from escalation detection to reward modeling to AI-powered search — all running concurrently. That breadth inside one organization tells you fine-tuning is ongoing infrastructure for building
agentic systems
, not something you do once and move on from.
The Agent Journey
Every team follows the same arc: a generic model hits a quality ceiling, fine-tuning closes the gap, and the result is a domain-specific agent in production.
The Bottlenecks That Show Up Every Time
Across these engagements — different industries, model sizes, use cases — the same problems keep coming back. The interesting thing is that none of them are about the training algorithm itself. They are all about what surrounds it.
Integration and Data Sovereignty
The most consistent blocker is integration. Reward functions, internal graders, and evaluation APIs have to stay inside the customer's environment. Sensitive business logic and proprietary data cannot leave for third-party scoring.
Fireworks addresses this at two levels. For teams that need full data isolation,
Training API
lets you run training loops where the data never leaves your environment — you control the Python process, the data stays on your side, and only weight updates flow through the platform. For managed fine-tuning,
secure bring-your-own-bucket storage
and
remote environments
keep
evaluators
executing inside the customer's VPC.
One team was constrained to specific non-Chinese open-source models for compliance. Model availability and geopolitical requirements shape the fine-tuning workflow just as much as the training algorithm does. The platform has to support a broad set of base models.
Data Sovereignty Architecture
Reward functions, graders, and training data stay inside the customer environment. The training platform connects securely without data leaving the VPC.
Iteration Velocity
The training job is rarely the bottleneck. Cycle time is.
Teams spend weeks setting up training infrastructure, curating noisy datasets, running a job, then discovering through offline evals that the model still falls short on quality. By the time they have iterated on the data, adjusted hyperparameters, and retrained, another week has passed. The actual GPU time is a fraction of the total cycle.
The teams that move fastest have collapsed that gap from weeks to hours. High-frequency job submission, fast feedback on what improved, minimal manual setup between experiments. One team ran over 100 jobs in the span of weeks. Another submitted dozens of RFT jobs with near-continuous iteration. These cadences look more like CI pipelines than ML experiments. Our work with Cursor on
Composer 2
is the clearest example — Fireworks powered the distributed RL training infrastructure that helped Composer 2 beat top frontier closed-source models on coding benchmarks, with a
new checkpoint shipping every ~5 hours thanks to the tight inference-training loop
.
Collocating fine-tuning and deployment on a single platform is what makes this possible. A trained
LoRA adapter deploys in minutes
— no model export, no separate serving stack. The
eval-protocol CLI
runs evaluations against the live deployment. The
cost estimator
lets teams plan iteration budgets before committing GPU hours.
There is a hidden multiplier here too:
hyperparameter optimization
. Train/test split discipline, grid search, and learning rate tuning still have outsized impact on final model quality. Most product teams building agents do not have a dedicated ML engineer to get this right, and sloppy experiment setup is one of the biggest reasons fine-tuning "doesn't work." This is one of the areas where we think the tooling has the most room to improve — imagine a system that watches your eval metrics across runs and adjusts the training configuration automatically, instead of requiring an ML expert to babysit each experiment. We're building exactly this, and it's closer than you think.
Iteration Velocity
The difference between teams that ship and teams that stall: collapsing the eval-train-deploy cycle from days of fragmented tooling into a tight loop measured in hours.
Use the Right Tool for the Job
The teams that iterate fastest stopped treating fine-tuning as a single technique. Within a single account, we regularly see
SFT
,
RFT
, and
DPO
all running for the same product — each method pointed at a different part of the problem.
Method choice follows the problem, not the other way around.
SFT
when you have high-quality demonstration data and a well-defined output format — distillation, structured extraction, style transfer.
RFT
when the reward signal is clearer than the correct output — agentic tasks, tool use, anything where correctness is hard to label but easy to evaluate (
how RFT works
).
DPO
when you have strong preference pairs and want to align behavior without writing a reward function.
The real power is in combining them. A common pattern we see: start with SFT to distill a strong baseline from demonstration data, then switch to RFT to push quality on the agentic behaviors that SFT alone cannot capture. The platform makes this straightforward. With
eval-protocol
, you can warm-start an RFT run directly from a previous SFT adapter using
--warm-start-from
, so a fine-tuned PEFT checkpoint becomes the starting point for reinforcement training without any manual export. For deeper control, Training API lets you
load a checkpoint from a previous training job
across job boundaries — an SFT run flows into an RFT run with full optimizer state preserved.
Model selection is part of the search space too. We see teams running experiments at multiple scales simultaneously — sub-1B for fast iteration, 200B+ MoE for production quality, sometimes both in the same week. The platform has to make switching between methods and models frictionless. We also support
vision fine-tuning
for multimodal use cases.
The Ladder from Managed to Full Control
There is a consistent maturity pattern. Teams almost always start with
managed fine-tuning
—
SFT
, DPO, or RFT through the API. This is the right starting point. It removes infrastructure from the critical path and validates that fine-tuning works for the problem.
Then they hit a ceiling. Deep domain adaptation, especially on large MoE architectures, needs more control:
custom loss functions
, custom data pipelines, optimizer-step access, full-parameter updates that LoRA cannot reach. The gap between "managed got us 80% of the way" and "we need the last 20%" is where teams either stall or start rebuilding their stack from scratch.
Training API
bridges that gap. Same infrastructure, same deployment targets, but you bring your own training loop. Custom GRPO, DAPO, or hybrid objectives. Full-parameter updates on models up to 200B+. Inference-in-the-loop evaluation with live serving checkpoints. No GPU cluster to provision. The
quickstart
gets you running in minutes.
Start where the abstraction is highest, drop down when you need to. The whole point is that the transition is seamless — you should not have to re-platform to get more control.
Choose Your Level of Control
From fully managed fine-tuning jobs to cookbook-style SFT/DPO/GRPO workflows to custom Python training loops. Same platform at every level.
Where We Are Heading
The industry is moving from manual ML experiments to CI/CD-style fine-tuning loops — and the logical endpoint is a loop that runs itself.
Every bottleneck we described above is a manual step that does not need to be manual. Integration should not require weeks of custom connector work — the training platform should plug into a customer's eval infrastructure natively. Iteration should not stall on a human deciding when to retrain — the platform should watch eval metrics, detect regressions, and kick off training runs automatically. And hyperparameter tuning should not require an ML specialist for every experiment — the system should observe what worked across thousands of prior runs and recommend configurations that are likely to converge.
Put those together and you get a fine-tuning workflow that is itself agentic.
The eval-to-retrain loop closes on its own. The system observes what the model gets wrong in production, selects the right training method, configures the run, validates the result against held-out data, and deploys if quality improves.
Humans define what good looks like and set the guardrails. The system does the rest.
The teams we work with are already stitching together pieces of this loop by hand — writing scripts that monitor eval dashboards, trigger retraining, and gate deployments. We are building the infrastructure to make that loop a first-class primitive. More on this soon.
Agentic Fine-tuning
The future state: the eval-to-retrain loop closes automatically. Humans set objectives and guardrails; the system handles observation, training, validation, and deployment.
Start Fine-Tuning Today
If any of this sounds familiar, you can start now.
•
Managed fine-tuning
—
SFT, DPO, and RFT
through the API. Models under 16B can be fine-tuned at no cost. Start with the
fine-tuning overview
.
•
Need more control?
— For custom training loops, full-parameter updates, and inference-in-the-loop evaluation,
reach out to learn more about our training products
.
We are working on automated hyperparameter optimization, eval-driven retraining, and agentic fine-tuning workflows that close the loop end to end. If you want early access or want to talk through your fine-tuning architecture, reach out via our
contact page
or on
Discord
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
