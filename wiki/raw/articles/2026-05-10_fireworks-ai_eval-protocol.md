---
title: "Fireworks AI"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/eval-protocol"
scraped: "2026-05-10T01:27:13.578766+00:00"
lastmod: "2026-02-12T18:51:38.000Z"
type: "sitemap"
---

# Fireworks AI

**Source**: [https://fireworks.ai/blog/eval-protocol](https://fireworks.ai/blog/eval-protocol)

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
Eval Protocol
Announcing Eval Protocol
PUBLISHED
8/4/2025
Table of Contents
Introducing Eval Protocol (EP)
Quickstart
The Problem: LLM agents are software, but not developed with the same rigor
Three Core Workflows, One Protocol
Resources:
Table of Contents
Table of Contents
Introducing Eval Protocol (EP)
Quickstart
The Problem: LLM agents are software, but not developed with the same rigor
Three Core Workflows, One Protocol
Resources:
Table of Contents
Can I swap one model for another?
It is a simple question with no consistent method for answering confidently. Divergences of one for or another are hard to trap. So we set out to provide that method, and today launched
Eval Protocol
, an OSS library and SDK for making model evaluations work like unit tests, and through CI/CD automation.
Introducing Eval Protocol (EP)
EP is an open protocol that standardizes how developers author evaluations for large language model (LLM) applications
. EP provides a specification for writing evals and storing eval results that travel with developers from local model picking and prompt engineering, through production CI/CD, to automated fine-tuning and reinforcement learning for real-world use-cases- from simple markdown and JSON generation to complex customer service agents with tool calling.
EP bridges the gap between quick wins and long-term customization. Developers can start with immediate benefits like automated CI/CD checks to prevent regressions today, then scale to sophisticated multi-turn evaluations using Model Context Protocol (MCP) for agent optimization tomorrow.
Quickstart
EP can be installed with
pip install eval-protocol
In this simple single-turn eval example, we run a mark for checking instruction-following test:
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
22
23
24
25
26
27
28
29
30
31
import
re
from
typing
import
Any
,
Dict
,
List
,
Optional
from
eval_protocol
.
models
import
EvaluateResult
,
EvaluationRow
,
Message
from
eval_protocol
.
pytest
import
default_single_turn_rollout_processor
,
evaluation_test
from
.
utils
import
markdown_evaluate
@evaluation_test
(
input_dataset
=
[
"tests/pytest/data/markdown_dataset.jsonl"
]
,
dataset_adapter
=
markdown_dataset_to_evaluation_row
,
model
=
[
"accounts/fireworks/models/llama-v3p1-8b-instruct"
]
,
rollout_input_params
=
[
{
"temperature"
:
0.0
,
"max_tokens"
:
4096
}
]
,
threshold_of_success
=
1.0
,
rollout_processor
=
default_single_turn_rollout_processor
,
num_runs
=
1
,
mode
=
"pointwise"
,
)
def
test_markdown_highlighting_evaluation
(
row
:
EvaluationRow
)
-
>
EvaluationRow
:
"""
Evaluation function that checks if the model's response contains the required number of formatted sections.
"""
meets_requirement
=
markdown_evaluate
(
row
)
if
meets_requirement
:
row
.
evaluation_result
=
EvaluateResult
(
score
=
1.0
,
reason
=
f"✅ Found
{
actual_count
}
highlighted sections (required:
{
required_highlights
}
)"
)
else
:
row
.
evaluation_result
=
EvaluateResult
(
score
=
0.0
,
reason
=
f"❌ Only found
{
actual_count
}
highlighted sections (required:
{
required_highlights
}
)"
)
return
row
For a multi-turn example with MCP, check out our
τ²-bench implementation
.
The Problem: LLM agents are software, but not developed with the same rigor
Building LLM apps involves juggling prompts, models, data, environments, and evals themselves. Today, developers face a fractured workflow: one-off scripts for model selection, disjointed tracing for production, and custom code for fine-tuning. Our opinion is that, if a developer wants to be confident with the quality of the LLM agent, we need to bring the same SDLC lifecycle back into LLM agents, with the familiar concepts of unit testing & CI/CD front and center. For example, you may have the following question around your application:
•
Can I swap models without losing quality? (Manual swaps in API clients)
•
Did my deployment cause a regression? Is my new prompt better or worse? (Ad-hoc scripts and console checks)
•
Is my fine tuned model solving real problems?
Three Core Workflows, One Protocol
EP is designed around your AI journey, with emphasis on getting quick value from CI/CD while paving the way for advanced customization.
Local Evals & Model Picking:
Kick off in your notebook. Use the
eval-protocol
library to benchmark models on your use case. Answer "Can I switch from Claude to Kimi?" with reproducible results. Supports row-wise rewards for single-turn rollouts and test MCP for multi-turn simulations with user agents.
Scale Up & CI/CD:
This is where EP shines for developers right now—no waiting for complex setups. Use the same eval suite on production logs for monitoring. Integrate into CI/CD via GitHub Actions: Run evals on PRs against golden datasets, get pass/fail comments with regression examples. Prevent issues before merge, ensuring "Did I break anything?" is answered automatically. Start simple with single-turn evals, then layer in MCP for multi-turn as your app grows.
Customized model:
As things grow, EP helps you evaluate your own model and own your AI stack. Curate bad traces into datasets, and re-evaluate with your original suite for proven improvements. This carries you from basic quality gates on top of proprietary models to evaluating your customized models.
EP evolves with you.
Resources:
•
Get started with Installing Eval Protocol:
pip install eval-protocol
•
More Docs:
Introduction,
Single-turn Guide
,
Multi-turn with τ²-bench
•
GitHub Repository:
GitHub
•
Join:
#eval-protocol
in our Discord for community support
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
