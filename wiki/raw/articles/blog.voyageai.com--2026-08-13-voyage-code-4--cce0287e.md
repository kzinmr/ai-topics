---
title: "voyage-code-4: code retrieval built for coding agents"
url: "https://blog.voyageai.com/2026/08/13/voyage-code-4/"
fetched_at: 2026-08-14T10:21:53.172103+00:00
source: "Voyage AI Blog"
tags: [blog, raw]
---

# voyage-code-4: code retrieval built for coding agents

Source: https://blog.voyageai.com/2026/08/13/voyage-code-4/

TL;DR
– Introducing
voyage-code-4
, our next-generation code embedding model, purpose-built to improve performance and reduce costs for coding agents. It outperforms Cohere Embed v4 and Gemini Embedding 2 by an average of
28.25%
and
31.03%
on a new benchmark built to measure how coding agents should retrieve code, and by
19.21%
and
16.01%
across the 28 code retrieval datasets from our
voyage-code-3
evaluation. It is available today at $0.12 per 1M tokens, a third below the price of
voyage-code-3
.
Since its launch in December 2024,
voyage-code-3
has been one of our most popular embedding models, with adoption driven by code assistants. What our customers build has changed since then. Coding
agents
now issue many of the code retrieval queries we serve. These agents explore, backtrack, and re-query across multiple steps, often starting from a goal as vague as “find everywhere we mishandle empty arrays.”
We built
voyage-code-4
specifically to tackle the complex retrieval required by coding agents. We are excited to announce the next generation of our code embedding models, which:
Outperforms Cohere Embed v4 and Gemini Embedding 2 by an average of 28.25% and 31.03% on agentic code retrieval, a new benchmark built from issue-fixing pull requests
Outperforms Cohere Embed v4 and Gemini Embedding 2 by 19.21% and 16.01% across the 28 code retrieval datasets used to evaluate
voyage-code-3
Supports 2048, 1024, 512, and 256 dimensional embeddings enabled by Matryoshka learning, and multiple quantization options – including 32-bit floating point, signed and unsigned 8-bit integer, and binary precision – while minimizing quality loss
Is priced at $0.12 per 1M tokens, a third below
voyage-code-3
Why agents need semantic retrieval.
Coding agents require high retrieval accuracy with low latency and cost for high-volume reads: over a single task, an agent may issue dozens of retrieval queries, each consuming prompt tokens, output tokens, and wall-clock time. Most agents today rely on full-text search (i.e., grep), which works well when the agent already knows the identifier it is looking for. However, for queries that describe a symptom rather than syntax (e.g., a bug report), full-text search returns no useful hits, and the agent spends additional requests and tokens searching more of the repository. Semantic retrieval with
voyage-code-4
complements full-text search and significantly reduces wasted token usage.
A new training corpus mined from completed pull requests.
Code embedding models are usually trained on source files paired with docstrings, comments, or synthetic questions. Such corpora teaches a model what code says, and conventional models therefore do well when a query names the function it wants. They do not teach a model what code does wrong, which is the context an agent needs when it starts from a bug report. To address this, we curate an entirely new training corpus from natural language queries to code. Our corpus spans hundreds of thousands of queries across hundreds of programming languages. The corpus spans tens of thousands of repositories and hundreds of programming languages, and is substantially larger than the code corpus used for
voyage-code-3
.
Matryoshka learning and quantization.
Like
voyage-code-3
,
voyage-code-4
supports 2048, 1024, 512, and 256 dimensional embeddings enabled by Matryoshka learning, along with float32, int8, and binary quantization – for more information on MRL and quantization, check out
the
voyage-code-3
blog
.
Evaluation Details
Datasets.
We evaluate on two suites. The first is agentic code retrieval, a suite of 19 benchmarks built from issue-fixing pull requests, where each query is an issue description and the relevant documents are the files the merged fix touched. It measures whether a model can locate the code that needs to change, given only a symptom, to fix the issue – the step an agent performs before it can edit anything. The benchmark is drawn from repositories held out of training, with no overlap against the training corpus. We are in the process of adding these benchmarks to the
RTEB evaluation suite
. The second suite is the 28 code retrieval datasets used to evaluate
voyage-code-3
, spanning five categories, which we report so that results are directly comparable to the previous generation. Each dataset consists of a corpus (e.g., source files from a repository) and queries (e.g., issue descriptions, natural-language questions, etc…).
Models.
We evaluate
voyage-code-4
alongside
voyage-code-3
, Cohere Embed v4, Gemini Embedding 2, and OpenAI v3 large.
Metrics.
Given a query, we retrieve the top 10 documents based on cosine similarities and report the normalized discounted cumulative gain (NDCG@10), a standard metric for retrieval quality and a variant of recall.
Results
All the evaluation results are available in
this spreadsheet
.
Agentic code retrieval.
The bar chart below compares the average retrieval quality of
voyage-code-4
and the alternatives on the agentic code retrieval benchmark. Overall,
voyage-code-4
is the top-performing model, surpassing
voyage-code-3
, Cohere Embed v4, Gemini Embedding 2, and OpenAI v3 large by 27.54%, 28.25%, 31.03%, and 48.58%, respectively.
Traditional code search.
The bar charts below illustrate the average retrieval quality across the 28 datasets used to evaluate
voyage-code-3
.
voyage-code-4
outperforms
voyage-code-3
, Cohere Embed v4, Gemini Embedding 2, and OpenAI v3 large by an average of 13.98%, 19.21%, 16.01%, and 40.06%, respectively.
Try voyage-code-4 today!
voyage-code-4
is available today via the Voyage API, the MongoDB
Atlas Embedding and Reranking API
. The first 200 million tokens are free. Visit
our docs
to learn more.
Follow us on
X (Twitter)
and
LinkedIn
to stay up-to-date with our latest releases.
Contributors
Andrew Gaut, Infra Lead
Tengyu Ma, Project Advisor
Sahil Verma, Project Lead
In collaboration with the Voyage team.
