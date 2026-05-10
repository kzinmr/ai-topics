---
title: "Codestral Embed"
source: "Mistral AI Blog"
url: "https://mistral.ai/news/codestral-embed"
scraped: "2026-05-10T01:20:38.629953+00:00"
lastmod: "2025-05-28T22:12:17.187Z"
type: "sitemap"
---

# Codestral Embed

**Source**: [https://mistral.ai/news/codestral-embed](https://mistral.ai/news/codestral-embed)

Codestral Embed
Research
The new state-of-the-art embedding model for code.
May 28, 2025
Mistral AI
We are excited to release Codestral Embed, our first embedding model specialized for code. It performs especially well for retrieval use cases on real-world code data.
Codestral Embed significantly outperforms leading code embedders in the market today: Voyage Code 3, Cohere Embed v4.0 and OpenAI’s large embedding model.
Codestral Embed can output embeddings with different dimensions and precisions, and the figure below illustrates the trade-offs between retrieval quality and storage costs. Codestral Embed with dimension 256 and int8 precision still performs better than any model from our competitors. The dimensions of our embeddings are ordered by relevance. For any integer target dimension n, you can choose to keep the first n dimensions for a smooth trade-off between quality and cost.
Results
Below  we show the performance of Codestral Embed for several categories. The details of the benchmarks corresponding to each category can be found in the table in the “Benchmarks details” section.
SWE-Bench is based on a dataset of real-world GitHub issues and corresponding fixes, and is especially relevant for retrieval-augmented generation for coding agents. Text2Code (GitHub) contains benchmarks relevant for giving context for code completion or edition. We believe that these two categories are especially relevant to code assistants.
Use cases
Codestral Embed is optimized for high-performance code retrieval and semantic understanding. It enables a range of practical applications across development workflows, especially when working with large-scale code corpora.
1. Retrieval-augmented generation
Codestral Embed facilitates rapid and efficient context retrieval for code completion, editing, or explanation tasks. It is ideal for AI-powered software engineering in copilots or coding agent frameworks.
2. Semantic code search
Embed enables accurate search of relevant code snippets from natural language or code queries. It is suitable for use within developer tools, documentation systems, and copilots.
3. Similarity search and duplicate detection
The model’s embeddings can be used to identify near-duplicate or functionally similar code segments, even with significant lexical variation. This supports use cases such as identifying reusable code to avoid duplicates, or detecting copy-paste reuse to enforce licensing policies.
4. Semantic clustering and code analytics
Codestral Embed supports unsupervised grouping of code based on functionality or structure. This is useful for analyzing repository composition, identifying emergent architecture patterns, or feeding into automated documentation and categorization systems.
Availability
Codestral Embed is available on our API under the name `codestral-embed-2505` at a price of $0.15 per million tokens. It is also available on our
batch API
at a 50% discount. For on-prem deployments, please
contact us
to connect with our applied AI team.
Please check our
docs
to get started and our
cookbook
for examples of how to use Codestral Embed for code agent retrieval.
Chunking parameters
For retrieval use cases, while you can use the full context size of 8192 tokens, it is often more efficient to chunk your dataset. We recommend using chunks of 3000 characters with 1000 characters overlap. Larger chunks tend to adversely affect the performance of the retrieval system. Refer to
our
cookbook
for more information about chunking.
Benchmark details
You can find the details of the benchmarks that we used to evaluate our model in the table below. We report the average score per category, and the macro average (average of the scores of each category).
Benchmark
Description
Category
SWE-Bench lite
Examples from SWE-Bench lite: given real github issues, retrieve the files that should be modified to fix the issue from the given state of the repository. Most relevant for code agent RAG.
swebench_lite
CodeSearchNet Code -> Code
Given real-world code from GitHub, retrieve the code that appears in the same context
code2code
CodeSearchNet doc2code
Given a docstring from real-world GitHub code, retrieve the corresponding code
Text2code (github)
CommitPack
Given a commit message from real-world GitHub code, retrieve the corresponding modified files
Text2code (github)
Spider
Retrieve SQL code given a query
Text2SQL
WikiSQL
Retrieve SQL code given a query
Text2SQL
Synthetic Text2SQL
Retrieve SQL code given a query
Text2SQL
DM code contests
Match problem descriptions to correct solutions for programming competition websites (corpus is correct + incorrect solutions for each problem).
Text2Code (Algorithms)
APPS
Match problem descriptions to solutions for programming competition websites.
Text2Code (Algorithms)
CodeChef
Match problem descriptions to solutions for programming competition websites.
Text2Code (Algorithms)
MBPP+
Match algorithmic questions to solutions for mostly basic python programs
Text2Code (Algorithms)
DS 1000
Match data science questions to implementations
Text2Code (Data Science)
Share this article
More from Mistral AI
News
Models
AI Services
