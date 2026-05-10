---
title: "Fireworks AI"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/batch-api"
scraped: "2026-05-10T01:27:03.252668+00:00"
lastmod: "2026-02-12T18:51:42.000Z"
type: "sitemap"
---

# Fireworks AI

**Source**: [https://fireworks.ai/blog/batch-api](https://fireworks.ai/blog/batch-api)

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
Batch Api
Run bulk async workloads with Fireworks Batch API
PUBLISHED
7/31/2025
With Fireworks’ Batch API, you can asynchronously run large volumes of requests on 1000+ open or finetuned models with no rate limits, 50% lower cost, and a 24-hour turnaround time.
This is helpful for use cases like:
•
Evaluations:
Benchmark across models to identify the best model for your use case
•
Data generation:
Generate bulk outputs using large models to fine-tune smaller models
•
Data augmentation:
Create paraphrases, sentiment labels, or question-answer pairs at scale
•
ETL Pipelines and Daily bulk processing:
Process large numbers of documents daily without worrying about rate limits
To use the Batch API, you simply upload your dataset in JSONL batch format and kick off a Batch API job. You can then check in on the status of your request, and retrieve the results once they are ready.
The Batch API has the following benefits:
•
High rate limits:
There is no upper limit on the number of requests in a batch job. The dataset must be <500 MB in size.
•
Lower cost:
50% lower cost compared to typical Serverless (synchronous) API pricing
•
Fast processing:
Results can be retrieved in a few hours, with a max turnaround time of 24 hours
•
Access 1000+ models
: Run batch jobs on all major open models supported by Fireworks or your own fine-tuned models
Getting Started in 3 Steps
Prepare Your Dataset
Create a JSONL Batch format dataset, for example:
1
2
{
"custom_id"
:
"request-1"
,
"body"
:
{
"messages"
:
[
{
"role"
:
"user"
,
"content"
:
"Tell me an interesting fact"
}
]
}
}
{
"custom_id"
:
"request-2"
,
"body"
:
{
"messages"
:
[
{
"role"
:
"user"
,
"content"
:
"Tell me a joke"
}
]
}
}
1
firectl create dataset test
-
set
.
/
my
-
local
-
folder
/
dataset
.
jsonl
Launch a Batch Job
Choose from
1,000+ models
—including base models in our Model Library [link], public community models, and your own fine-tuned variants.
1
2
3
4
firectl create bij \
-
-
input
-
dataset
-
id
test
-
set
\
-
-
model accounts
/
fireworks
/
models
/
qwen3
-
14b \
-
-
output
-
dataset
-
id
output
-
set
Download Results
Once the job completes, fetch your outputs in one command:
1
2
firectl download dataset output
-
set
-
-
output
-
dir
.
/
output
Ready to unlock true AI scale?
Dive in with our Batch Inference Guide
or
API reference
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
