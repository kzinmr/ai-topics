---
title: "Fireworks AI"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/experimentation-build-sdk"
scraped: "2026-05-10T01:20:32.566392+00:00"
lastmod: "2025-06-11T15:28:08.000Z"
type: "sitemap"
---

# Fireworks AI

**Source**: [https://fireworks.ai/blog/experimentation-build-sdk](https://fireworks.ai/blog/experimentation-build-sdk)

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
Experimentation Build Sdk
Building AI agents with the Fireworks Experimentation Platform (GA) and Build SDK (Beta)
PUBLISHED
6/11/2025
Table of Contents
Fireworks Experimentation Platform: Reduce time to iteration from weeks to hours
The Fireworks Build SDK: Rapidly Prototype with Open Models
Code Walkthrough
Powerful features that unlock experimentation with open models
Getting started
What's next
Table of Contents
Table of Contents
Fireworks Experimentation Platform: Reduce time to iteration from weeks to hours
The Fireworks Build SDK: Rapidly Prototype with Open Models
Code Walkthrough
Powerful features that unlock experimentation with open models
Getting started
What's next
Table of Contents
When building AI agents, the best AI companies are jointly developing their product and models in a process of rapid, continuous iteration. Just as we saw the rise of CI/CD pipelines in software, we now see a similar pattern emerging for building AI systems. This development lifecycle has four essential steps:
Launch early, often testing multiple models, to get user feedback and collect interaction data from product usage
Tune multiple candidate models using powerful post-training techniques
Conduct offline evaluations to validate quality improvement and deploy the best performing models
Deploy best performing models, and run online A/B tests to validate that your product metrics improve
Each step, however, has its own challenges that slow you down.
Complex infrastructure setup and failures, time spent waiting for GPUs, reconciling differences between training and serving (both in data and use cases), and maintaining service reliability in production are all pain points that affect the iteration velocity of AI teams.
Fireworks Experimentation Platform: Reduce time to iteration from weeks to hours
To help address these challenges, we’re excited to announce the
GA of the Fireworks Experimentation Platform
– designed to supercharge your experimentation velocity by reducing your iteration time from weeks to hours. The experimentation platform offers powerful capabilities that help you move at the fastest possible speed:
✅ Build SDK with 1000s of models supported
Start building in seconds, without setting up infrastructure or wrangling multiple libraries - explore our
model library
.
🔧 LoRA Add-Ons: Run 100s of fine-tuning experiments in parallel
Make sure you’re not spending your time waiting for GPUs! LoRA Add-Ons allow you to run 100s of experiments in parallel. Instead of conducting experiments sequentially due to limited GPU capacity, you can deploy fine-tuned models as LoRA add-ons onto a single base model deployment.
This lets you scale your experimentation, with just a few lines of code in the Build SDK, without needing to run a huge GPU cluster or wait for capacity or cold starts.
🚀 Flexible Capacity: available on-demand, fully secure
Fireworks On-Demand offers flexible, single tenant capacity across our global fleet. On-demand deployments autoscale with your traffic, making it ideal for A/B testing. And you can transition seamlessly from training to production serving on Fireworks.
The Fireworks Build SDK: Rapidly Prototype with Open Models
To access the full capabilities of the experimentation platform, we’re also excited to announce the beta of our brand-new
Build SDK
, a tool to make rapid prototyping and experimentation on Fireworks easier than ever before. You can use the Build SDK to
programmatically run experiments and evals
, managing your entire AI workflow and Fireworks infrastructure through simple Python code.
Our SDK provides a
declarative, object-oriented interface
that treats Fireworks resources (e.g. deployments, fine-tuning jobs, and datasets) as simple Python objects. We designed it with four principles in mind:
•
Object-Oriented:
Work with Fireworks primitives as intuitive Python objects
•
Declarative:
Describe your desired state and let the SDK handle the reconciliation logic for you.
•
Smart Defaults:
The SDK automatically makes the most logical and resource-efficient choices, such as reusing existing resources instead of creating duplicates
•
Fully Customizable:
You have full access to every configuration parameter for complete customization
Code Walkthrough
It takes just a few lines of code to get started working with open models
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
from
fireworks
import
LLM
# Deploy and use Llama 4 Maverick...or any model from our model library...in seconds
llm
=
LLM
(
model
=
"llama4-maverick-instruct-basic"
,
deployment_type
=
"auto"
)
response
=
llm
.
chat
.
completions
.
create
(
messages
=
[
{
"role"
:
"user"
,
"content"
:
"Hello, world!"
}
]
)
print
(
response
.
choices
[
0
]
.
message
.
content
)
Curious how easily you can experiment at scale with the Build SDK?
Watch Dylan run 125 experiments in 3 minutes using just a single deployment!
Powerful features that unlock experimentation with open models
Declarative Deployments
You specify the model you want and the SDK can automatically choose the best strategy across on-demand and serverless options, spinning up resources for you as needed
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
# Use deployment_type="auto" to let the SDK choose the optimal deployment configuration
llm
=
LLM
(
model
=
"qwen2p5-72b-instruct"
,
deployment_type
=
"auto"
)
# Or, take full control with advanced configurations
llm
=
LLM
(
model
=
"qwen2p5-72b-instruct"
,
deployment_type
=
"on-demand"
,
precision
=
"FP8"
,
accelerator_type
=
"NVIDIA_H100_80GB"
,
draft_model
=
"qwen2p5-0p5b-instruct"
,
min_replica_count
=
1
,
)
Effortless Fine-Tuning
Fine-tuning a model is now as simple as creating a dataset and calling one method:
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
from
fireworks
import
Dataset
,
LLM
# Create dataset from your training data
dataset
=
Dataset
.
from_file
(
"my-dataset.jsonl"
)
# Fine-tune in just a few lines
base_model
=
LLM
(
model
=
"qwen2p5-7b-instruct"
,
deployment_type
=
"on-demand"
)
job
=
base_model
.
create_supervised_fine_tuning_job
(
"my-fine-tuning-job"
,
dataset
)
# Wait for completion and get your fine-tuned model
job
.
wait_for_completion
(
)
fine_tuned_model
=
job
.
output_llm
Programmatic Experimentation
You can easily script experiments across multiple models and configurations. If possible, the SDK will re-use existing deployments or leverage Multi-LoRA to be resource-efficient.
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
models_to_test
=
[
"llama-v3p3-70b-instruct"
,
"qwen2p5-72b-instruct"
,
"mixtral-8x7b-instruct"
]
test_prompts
=
[
#  Your test prompts here
]
results
=
{
}
# Script out the benchmarking
for
model_name
in
models_to_test
:
llm
=
LLM
(
model
=
model_name
,
deployment_type
=
"auto"
)
for
prompt
in
test_prompts
:
response
=
llm
.
chat
.
completions
.
create
(
messages
=
[
{
"role"
:
"user"
,
"content"
:
prompt
}
]
)
results
[
model_name
]
[
prompt
]
=
response
.
choices
[
0
]
.
message
.
content
# Programmatically analyze results and choose the best performing model
best_model
=
analyze_experiment_results
(
results
)
Smart Resource Management
The SDK's smart defaults intelligently reuses and optimizes deployments to let you confidently scale experimentation volume
•
Resource Signatures
: Each resource has a unique signature that prevents duplicate creation
•
Automatic Reuse
: Existing resources are reused across your team when appropriate
•
Resource Optimization
: Built-in scale-to-zero and intelligent deployment choices
Getting started
The Fireworks Build SDK is available now
and getting started takes less than 5 minutes:
1. Install the SDK
1
pip install --upgrade fireworks-ai
2. Set your API key
1
export FIREWORKS_API_KEY=<your-api-key>
3. Start building
1
2
3
4
from
fireworks
import
LLM
llm
=
LLM
(
model
=
"llama4-maverick-instruct-basic"
,
deployment_type
=
"auto"
)
# You're ready to build!
What's next
The Build SDK represents our vision for the future of AI development — where infrastructure complexity disappears and developers can focus entirely on creating amazing AI experiences through code.
We're continuing to expand the SDK with new capabilities:
•
Advanced multi-modal model support
•
Enhanced fine-tuning workflows
•
Better function calling syntax
•
Deeper Fireworks platform integrations
Whether you're building a simple chatbot or running complex AI experiments, we want to hear about your experience and are actively seeking feedback from the developer community. Get started with the SDK by:
•
📖
Reading the complete documentation
•
🚀
Trying the interactive tutorial
•
📧 Sharing feedback on
Discord
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
