---
title: "How Cursor built Fast Apply using the Speculative Decoding API"
source: "Fireworks AI Blog"
url: "https://fireworks.ai/blog/cursor"
scraped: "2026-05-10T01:27:12.576810+00:00"
lastmod: "2026-02-12T18:52:57.000Z"
type: "sitemap"
---

# How Cursor built Fast Apply using the Speculative Decoding API

**Source**: [https://fireworks.ai/blog/cursor](https://fireworks.ai/blog/cursor)

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
Cursor
How Cursor built Fast Apply using the Speculative Decoding API
PUBLISHED
6/23/2024
Table of Contents
What Cursor is building?
Instant Apply
Smart Rewrites
Cursor Prediction
Features Used
Rewrite Problem
Speculative Decoding
Getting started with Speculative Decoding
Fireworks AI Promise
Table of Contents
Table of Contents
What Cursor is building?
Instant Apply
Smart Rewrites
Cursor Prediction
Features Used
Rewrite Problem
Speculative Decoding
Getting started with Speculative Decoding
Fireworks AI Promise
Table of Contents
TL;DR
•
Cursor leveraged Fireworks inference stack to achieve 1000 tok/sec.
•
Announcing new Speculative Decoding API, that enables users to speculate a larger number of tokens in parallel.
Millions of developers write code everyday to improve software systems at large bringing productivity to many business workflows, however, very few tools help them improve their own productivity.
With the advent of Generative AI, we see an emerging category of developer tooling built around Large Language Models (LLMs) especially for
code generation
. Some popular tools in this regard are Github Copilot, Sourcegraph, Phind, Continue, Blackbox, Codeium, Cognition, Factory, Aider., the list goes on…
Among them is a standout product,
Cursor
. Cursor is an AI-native IDE that helps developers write better code faster. Their core features include:
Cursor’s Copilot++
is a more powerful AI-assistant which predicts your next edit taking in account of your recent change.
Cmd/Ctrl-k, an instructed edit model that you can use to make changes to any region of code with natural language
A chat that sees your whole codebase and can “instantly apply” the changes to your code.
Our mission at Fireworks is to assist developers building innovative and mission critical Generative AI experiences at enterprise scale. In this blog, we will go through how
Fireworks inference stack
enabled Cursor to achieve 1000 tokens per sec using our Speculative Decoding API with low latency.
What Cursor is building?
There are many feature highlights in Cursor, but here are some that are making developers love them more.
Instant Apply
Instantly applying the generated code to a file using a “Play” button.
Smart Rewrites
Rewriting and making minute multi-line syntactic corrections to a snippet of code as developers write code like prose.
Cursor Prediction
Cursor’s Copilot++ predicts your next cursor position so you can seamlessly navigate your code.
Features Used
•
Fireworks Custom Model deployment for inference with performance optimizations for specific workload.
•
Fireworks Chat Completion and Completion API enabled with Speculative Decoding flag.
Rewrite Problem
Frontier models like GPT-4 and GPT-4o struggle with large code edits, exhibiting issues such as laziness, inaccuracy, and high latency. These weaknesses are particularly evident in coding agents, where accurately editing hundreds of lines of code can require multiple model calls and lead to infinite loops or buggy outputs. The slow performance of existing models on large edits also disrupts programmers' workflow.
To address these challenges, Cursor has trained a specialized model on the "
fast apply
" task, which involves planning and applying code changes. The fast-apply model surpasses the performance of GPT-4 and GPT-4o, achieving speeds of ~1000 tokens/s (approximately 3500 char/s) on a 70b model.
The model is trained on a combination of synthetic data generated from CMD+K prompts and instant apply inputs. Fireworks deployed a custom trained “llama-70b-ft-spec” model on the inference engine using speculative decoding, enabling the model to generate speeds >1000 tokens/s.
Speculative Decoding
In a regular LLM inference, every token depends on the context of the entire corpus of tokens generated previously. It is not possible to generate the n+1 token without the nth token.
Speculative Decoding enables parallelization of the token generation, enables users to speculate a larger number of tokens in parallel and consume them without deviating from the provided context.
Most LLM use cases have a wide variety of possible inputs which makes it hard to produce good speculations. Usually one trains a
separate “draft” model (or adapter) capable
of
guessing a few tokens
at time.
Cursor built a variant of speculative decoding called “
speculative edits
”, an algorithm that uses much longer speculations to make code edits substantially faster.
These longer speculations are possible in case of partial text rewriting when the caller has a strong guess of what the generation might look like, especially with Code Generation. This speculative guess is used by Fireworks to speed up the response considerably.
The speculation is always validated using deterministic (greedy) generation. I.e., the server will find the longest prefix of the "speculation" field that matches the model's generation with temperature=0. After that, it will proceed with normal generation respecting request parameters, including the temperature.
Fireworks deployed Cursor’s special fine-tune of Llama-3-70b for the coding task “
Fast Apply
” using the speculative API flag, enabling them to ~13x speedup over vanilla inference using Llama-3-70b and a ~9x speedup over their previous GPT-4 speculative edits deployment leading them to achieve ~1000 tokens/sec.
Powered by Llama
Getting started with Speculative Decoding
Using Speculative Decoding as a feature is easy because it is a flag in
Fireworks API
.
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
import
fireworks
.
client
prompt
=
"""def print_fibonacci(n):
a, b = 0, 1
for i in range(n):
print(a, end=" ")"""
prediction
=
"""
a, b = c, a + b
"""
fireworks
.
client
.
api_key
=
"YOUR_API_KEY"
completion
=
fireworks
.
client
.
Completion
.
create
(
model
=
"accounts/fireworks/models/starcoder-16b"
,
prompt
=
prompt
,
prediction
=
prediction
,
temperature
=
0
,
stop
=
"\n\n"
,
)
choice
=
completion
.
choices
[
0
]
print
(
choice
.
text
)
Fireworks AI Promise
Traditional Large Language Models struggled with providing relevant context and often produced suboptimal results or slow responses.
Using Fireworks AI Inference stack, Cursor achieved a remarkable speed bump compared to vanilla inference and their previous GPT-4 deployment.
At Fireworks, our mission is democratizing AI for developers and businesses, serving the best of
language
, audio and
image
models at the fastest speeds and highest reliability. Today, we work with companies like Quora, Uber, Doordash with industry-leading inference speed and quality for production use cases across image and text generation.
If you are a developer or an enterprise starting on the Generative AI, consider
joining our community
of practitioners, sign up to
Fireworks AI platform
to freely build Generative AI experiences up to two million tokens.
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
