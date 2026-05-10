---
title: "Using Model-as-a-Judge for Reward in Reinforcement Finetuning"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/model-as-judge"
scraped: "2026-05-10T01:20:34.857623+00:00"
lastmod: "2026-02-12T18:51:56.000Z"
type: "sitemap"
---

# Using Model-as-a-Judge for Reward in Reinforcement Finetuning

**Source**: [https://fireworks.ai/blog/model-as-judge](https://fireworks.ai/blog/model-as-judge)

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
Model As Judge
Using Model-as-a-Judge for Reward in Reinforcement Fine Tuning
PUBLISHED
7/10/2025
Table of Contents
TL;DR
Creative Writing in Arena Hard
Training Workflow
Step 1: Dataset Preparation
Step 2: Reward Function Drafting with Reward Kit
Step 3: Training and Evaluation
Additional Experiments
Table of Contents
Table of Contents
TL;DR
Creative Writing in Arena Hard
Training Workflow
Step 1: Dataset Preparation
Step 2: Reward Function Drafting with Reward Kit
Step 3: Training and Evaluation
Additional Experiments
Table of Contents
TL;DR
In domains that are inherently challenging to quantify, such as creative writing, we demonstrate that leveraging a superior large language model (LLM) as a judge can meaningfully improve the performance of the policy model.
•
Using the Fireworks Reinforcement Fine Tuning (RFT) API, we successfully fine-tuned a Qwen2.5 32B base model, achieving a 93.8% win rate on creative writing tasks in the
Arena Hard Auto dataset
against the original base model.
•
To manage the open-source Qwen3 235B judge model, we employed the
Fireworks Build SDK
, enabling the system to automatically allocate the optimal compute resources to host the model.
•
To assign rewards in a nonverifiable domain, the evaluator also supports pairwise comparison, i.e. we compare different rollouts of the same prompt, and assign rewards accordingly.
Creative Writing in Arena Hard
The Arena Hard Auto dataset encompasses tasks spanning creative writing, mathematics, and software engineering. The creative writing subset, for example, features prompts like the one below:
Write a personal dialog about tension in a relationship, using these words: rocket, pollution, fitness, pierce, rational, fee, threaten, falsify, resource, treaty.
Developing an effective rule-based reward function for dimensions such as style, diversity, and coherence is particularly challenging in creative domains. However, by utilizing a capable LLM as a judge, it becomes feasible to evaluate and compare responses with nuanced reasoning. In this blog, we discuss our training methodology and showcase some results.
Training Workflow
Step 1: Dataset Preparation
Download
the Arena Hard dataset
locally and split it into train and test sets. Then upload the train set to the Fireworks Platform. This can be also accomplished via the web UI or by running this firectl command:
firectl create dataset arena-hard-v2 questions.jsonl
Step 2: Reward Function Drafting with Reward Kit
Navigate to the
evaluator UI
, and place your evaluation logic there. Interested readers can see the actual reward function we used
here
.
Note that we use the
Fireworks Build SDK
to call the judge model,
Qwen3 235B
, deployed on Fireworks’ platform. For the reward function, we use the
batch
mode of the reward kit by setting
@reward_function(mode="batch")
so that we can perform pairwise comparison of different rollouts of the same prompt. The reason for doing so is that sometimes it is not easy to give an absolute score to a creative writing piece, and it makes more sense to assign the score in a pairwise way. This reward function/evaluator will subsequently be used in the RFT job in the next step.
Note that when using the Build SDK,
deployment_type=’auto’
defaults to serverless deployment if the model supports serverless. If the user intends to spin up an on-demand deployment, use
deployment_type =’on-demand’
. You can read more about the Build SDK
here
.
Step 3: Training and Evaluation
The base policy model is
Qwen2.5 32B
. We will use the judge model,
Qwen3 235B
deployed serverlessly on Fireworks, to provide evaluation scores to the policy model, and perform reinforcement fine tuning on it. Note that we are using an open source model as the judge. We then run the RFT job for 8 epochs using the Fireworks RFT UI.
Note that since we are using comparative score, i.e. the judge model looks at two rollouts, and give the relative better rollout a score of 1 and the other one a score of 0, or both zero, the average score from epoch to epoch won’t necessarily increase in the case of a rule based reward function. The following is a complete RFT run with the judge model giving reward.
After the RFT job, we run the Arena Hard V2.0 test code against our RFT model. One thing worth pointing out is that Arena Hard V2.0 uses an automated judge by LLM as well. In order to avoid potential bias, we used GPT 4.1 as this automated judge.
Running the arena hard evaluation pipeline shows that the RFT model has a 93.8% winning rate against the base mode Qwen2.5 32B. Note that without training, the win rate of the base model against itself is naturally 50%. One can refer to
this file
for the response before and after RFT.
Model
Scores (%)
CI (%)
qwen2p5-32b-rft-model-as-judge
93.8
(-2.8 / +2.6)
qwen2p5-32b-base
50.0
(-0.0 / +0.0)
Additional Experiments
Beyond creative writing, we also evaluated the impact of LLM-judged reinforcement fine-tuning on tasks with more objective ground truths, such as mathematics and programming. In these domains as well, RFT-finetuned models demonstrated significant improvements over the base models.
To get started with RFT and model-as-judge for your use case, check out our
docs
and join our
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
