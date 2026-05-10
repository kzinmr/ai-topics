---
title: "Fireworks AI"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/gpt-oss-on-fireworks-ai"
scraped: "2026-05-10T01:20:51.381828+00:00"
lastmod: "2026-02-12T18:51:35.000Z"
type: "sitemap"
---

# Fireworks AI

**Source**: [https://fireworks.ai/blog/gpt-oss-on-fireworks-ai](https://fireworks.ai/blog/gpt-oss-on-fireworks-ai)

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
Gpt Oss On Fireworks Ai
Quality first: how Fireworks.ai is the go-to place for gpt-oss
PUBLISHED
8/12/2025
Table of Contents
The Critical Weak Point: Tool Calling
Engineering in the Open
The Result: OpenAI Under-Reported Some Benchmarks
Reproducing Our Results
Why This Matters for You
Get Started with the Best GPT-OSS Today
Table of Contents
Table of Contents
The Critical Weak Point: Tool Calling
Engineering in the Open
The Result: OpenAI Under-Reported Some Benchmarks
Reproducing Our Results
Why This Matters for You
Get Started with the Best GPT-OSS Today
Table of Contents
It’s been an incredible week for the open-source AI community. The release of GPT-OSS marked a significant milestone, opening up new possibilities for developers and researchers worldwide. This is especially exciting as it is released from a US frontier lab 🇺🇸. At
Fireworks.ai
, we believe that making a model available is only the first step. The real work lies in making it reliable, performant, and truly production-ready.
From the moment GPT-OSS was released, our team worked tirelessly not just to host it, but to provide the single best implementation available anywhere. Our "Quality First" approach meant diving deep into the code, identifying critical issues, and deploying robust fixes to ensure our partners and the entire community could build on a solid foundation.
We were proud to help power the official demo site at
gpt-oss.com
and support the Hugging Face team to ensure everyone could experience the power of GPT-OSS from day one.
https://x.com/ClementDelangue/status/1953119901649891367
The Critical Weak Point: Tool Calling
For modern AI applications, tool calling (or function calling) is not just a feature; it's the bridge between language models and the real world. It allows models to interact with APIs, access external data, and perform actions, transforming them from simple chatbots into powerful agents.
However, the initial release of GPT-OSS, while powerful, had inconsistencies and bugs in its tool-calling implementation. This meant developers would face malformed outputs, failed function calls, and unreliable behavior—barriers to building robust, production-grade applications.
We immediately focused our engineering efforts on solving this. Our deep dive paid off, and the results were quickly recognized by the community. OpenRouter, a leading LLM gateway that rigorously tests model providers, highlighted the quality of our implementation, naming it the best for tool calling.
https://x.com/xanderatallah/status/1953122779022209230 where OpenRouter quoted us to be the best at tool calling
Engineering in the Open
Our commitment to quality extends to the entire open-source ecosystem. After identifying and fixing a critical bug in the model's tokenizer logic, we didn't keep it to ourselves. We immediately upstreamed our fix, sharing it with the community to ensure that every implementation of GPT-OSS could benefit from this improvement. This is what true open-source collaboration looks like.
The Result: OpenAI Under-Reported Some Benchmarks
Here’s where it gets exciting. After implementing our fixes, particularly the harmony tokenizer fix, we re-ran the tool-calling benchmarks. Our findings suggest that the initial scores reported by OpenAI were based on the model before these critical bugs were addressed.
With the fixes in place, the model’s true capabilities are even more impressive than we thought.
We believe OpenAI under-reported their tool-calling benchmarks by 5~10% due to possible
issues with tool calling or differences in test setup**.**
Here are the scores on our production-ready, fully-patched GPT-OSS implementation across several challenging tool-use benchmarks, all done with average 8 runs.
Reproducing Our Results
The numbers reported above are an average over 8 runs, where we used:
•
A reference implementation of gpt-oss
https://github.com/openai/gpt-oss?tab=readme-ov-file
chat completion sampler
1
python
-
m gpt_oss
.
evals
-
-
sampler chat_completions
-
-
base
-
url https
:
//
api
.
fireworks
.
ai
/
inference
/
v1
-
-
eval
aime25
-
-
model
"$MODEL_ID"
-
-
n
-
threads
4
-
-
debug
•
For reporting evaluations with confidence interval, we use eval-protocol which calculates the evals. For example, for AIME low effort, here is the following command to reproduce from eval-protocol’s python SDK
1
2
3
4
5
# AIME:
python
-
m eval_protocol
.
benchmarks
.
run aime25_low
-
-
model fireworks_ai
/
accounts
/
fireworks
/
models
/
gpt
-
oss
-
120b
-
-
print
-
summary
-
-
out
/
tmp
/
aime_local
-
-
max
-
rows
all
-
-
reasoning
-
effort low
-
-
num
-
runs
8
-
-
max
-
tokens
131000
-
-
max
-
concurrency
16
# Tau2 Bench Retail:
python
-
m eval_protocol
.
benchmarks
.
run tau_bench_retail
-
-
model fireworks_ai
/
accounts
/
fireworks
/
models
/
gpt
-
oss
-
120b
-
-
print
-
summary
-
-
out
/
tmp
/
tau_retail_local
-
-
max
-
rows
all
-
-
reasoning
-
effort medium
-
-
num
-
runs
8
-
-
max
-
tokens
131000
-
-
max
-
concurrency
16
•
We also cross check with the base implementation of Tau2-Bench:
tau2-bench
. This is the script we ran.
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
#!/usr/bin/env python3
from
tau2
.
data_model
.
simulation
import
RunConfig
from
tau2
.
run
import
run_domain
config
=
RunConfig
(
domain
=
"retail"
,
agent
=
"llm_agent"
,
llm_agent
=
"fireworks_ai/accounts/fireworks/models/gpt-oss-120b"
,
llm_args_agent
=
{
"extra_body"
:
{
"reasoning_effort"
:
"medium"
}
,
"temperature"
:
0.8
}
,
user
=
"user_simulator"
,
llm_user
=
"gpt-4.1"
,
num_trials
=
8
,
max_concurrency
=
50
,
)
if
__name__
==
"__main__"
:
results
=
run_domain
(
config
)
print
(
"✅ Run completed!"
)
Note that for results that is supposed to be run with temperature > 0, we strongly recommend model builders to release benchmark with CI results going forward, so that the users can have clearer expectation on model performance, and it can also help uncover cases where model builders accidentally under report their results.
Why This Matters for You
For developers building the next generation of AI applications, quality is everything. When you build on
Fireworks.ai
, you get:
•
Unmatched Reliability:
Our fixes mean fewer errors, more predictable behavior, and a stable foundation for your products.
•
Superior Performance:
Access the true, unlocked potential of GPT-OSS with benchmark-proven improvements in critical areas like tool calling.
•
Faster Development Cycles:
Don't waste time debugging model-level inconsistencies. Build with confidence, knowing the underlying engine is solid.
Get Started with the Best GPT-OSS Today
The hype around a new model release is exciting, but enduring value comes from meticulous engineering and a relentless focus on quality. At
Fireworks.ai
, we didn’t just host GPT-OSS; we perfected its implementation to deliver the performance and reliability the community deserves.
Try out gpt-oss on fireworks at
https://fireworks.ai/models/fireworks/gpt-oss-120b
. Let us know if you have any feedback!
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
