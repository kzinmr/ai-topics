---
title: "rerank-3 and rerank-3-lite: the next generation of Voyage rerankers"
url: "https://blog.voyageai.com/2026/09/30/rerank-3/"
fetched_at: 2026-10-01T10:00:42.532755+00:00
source: "Voyage AI Blog"
tags: [blog, raw]
---

# rerank-3 and rerank-3-lite: the next generation of Voyage rerankers

Source: https://blog.voyageai.com/2026/09/30/rerank-3/

TL;DR
– We are excited to introduce the Rerank 3 series, the next generation of Voyage rerankers.
rerank-3
and
rerank-3-lite
improve upon
rerank-2.5
and
rerank-2.5-lite
across nearly all domains at the same price, with the largest gains on long documents and code. On our standard suite of 95 retrieval datasets,
rerank-3
and
rerank-3-lite
outperform Cohere Rerank v4.0 Pro by 2.72% and 2.23%, and Qwen3-Reranker-8B by 3.02% and 2.53%. On long-document retrieval,
rerank-3
outperforms
rerank-2.5
by 3.35% and Cohere Rerank v4.0 Pro by 13.84%. Both models retain the 32K token context length and the instruction-following capability of the Rerank 2.5 series, and
rerank-3-lite
now matches the retrieval quality of
rerank-2.5
at 40% of the price.
Quality: 95 datasets with voyage-4-large top-100 retrieval. Qwen3-Reranker-8B: assumed $0.10 / 1M tokens.
Rerankers are the second stage of a retrieval pipeline. The first stage, usually embeddings and vector search, selects a list of candidates from a large corpus. The reranker then scores each candidate against the query and reorders the list so that the most relevant documents land at the top. Because the reranker only sees a short list, it can afford to be more accurate per document than an embedding model, and it can be added to an existing retrieval system with a single API call and no re-indexing. For an introduction to rerankers, see our
earlier post
. For a comparison against LLMs used as rerankers, see
this post
.
Since its release in August 2025,
rerank-2.5
has been one of our most popular models. Over the same period, the workloads we serve have changed. Coding agents now issue many of the queries that reach our rerankers, and the documents being reranked are getting longer. The Rerank 3 series brings its largest improvements in these two areas.
Today, we are excited to announce
rerank-3
and
rerank-3-lite
. Both models are trained with an updated backbone and an improved mixture of training data.
Improvements on long documents and code
The Rerank 3 series is designed as an upgrade to Rerank 2.5 that requires no changes to your code. The API, the 32K token context length, instruction-following, and pricing are the same. Relevance scores are calibrated to match the score distributions of the corresponding Rerank 2.5 models, so score thresholds tuned on Rerank 2.5 continue to work.
Long documents.
rerank-3
and
rerank-3-lite
score candidate documents of up to 32K tokens, and the largest improvement over the Rerank 2.5 series comes on long documents. On LongEmbed, which consists of NarrativeQA, SummScreenFD, and QMSum,
rerank-3
outperforms
rerank-2.5
by 3.35% and
rerank-3-lite
outperforms
rerank-2.5-lite
by 1.86%. Both models outperform Cohere Rerank v4.0 Pro on long documents by more than 13%.
Code.
As we noted in the voyage-code-4 release, coding agents now issue many of the code retrieval queries we serve. On our code retrieval datasets,
rerank-3
outperforms
rerank-2.5
by 2.17% when evaluated atop
voyage-3-large
and by 2.11% atop
voyage-4-large
.
rerank-3-lite
outperforms
rerank-2.5-lite
by 3.58% and 3.72% on the same two retrievers.
Evaluation Details
Datasets.
We evaluate across 9 domains: technical documentation, code, law, finance, web reviews, multilingual, long documents, medical, and conversations, 95 datasets in total. The multilingual domain is composed of 51 datasets from 31 languages. Detailed information about each of the domains and languages can be found in the
rerank-2 release blog
. To evaluate instruction-following, we use the
MAIR benchmark
, which consists of 123 tasks with task-specific instructions. Examples of instruction-following can be found in the
Rerank 2.5 release blog
.
Method and Metrics.
We evaluate the retrieval quality of various rerankers on top of four first-stage search methods: (1) lexical search with BM25, (2) OpenAI v3 large (text-embedding-3-large), (3)
voyage-3-large
, and (4)
voyage-4-large
. For each query, the first-stage method retrieves up to 100 candidate documents. The reranker then re-orders these documents, and we retrieve the top 10. We report the normalized discounted cumulative gain (NDCG@10), the standard metric for retrieval quality.
Baselines:
We compare our models against
rerank-2.5
,
rerank-2.5-lite
, Cohere Rerank v4.0 Pro, Cohere Rerank v4.0 Fast, Qwen3-Reranker-8B, Jina Reranker v3.5, mxbai-rerank-large-v2, and NVIDIA Llama-Nemotron Rerank 1B v2.
Results
rerank-3
is the top-performing reranker on every first-stage retrieval method we evaluated, and
rerank-3-lite
is roughly on par with
rerank-2.5
at 40% of the price. Both models improve on their predecessors at the same price per token.
Results across domains.
The first bar chart below shows the average accuracy of each reranker across the 9 domains. Specifically:
Averaged across the four first-stage retrieval methods,
rerank-3
outperforms Cohere Rerank v4.0 Pro, Cohere Rerank v4.0 Fast, Qwen3-Reranker-8B, and
rerank-2.5
by 2.72%, 5.74%, 3.02%, and 0.96%, respectively.
rerank-3-lite
, while optimized for latency, outperforms Cohere Rerank v4.0 Pro, Cohere Rerank v4.0 Fast, Qwen3-Reranker-8B, and
rerank-2.5-lite
by 2.23%, 5.25%, 2.53%, and 1.10%, respectively.
rerank-3-lite
outperforms Qwen3-Reranker-8B, the leading open-weights reranker, despite being over an order of magnitude smaller.
Both models provide a significant quality improvement on top of all first-stage retrieval results.
rerank-3
improves NDCG@10 by 7.65% atop
voyage-3-large
, 6.38% atop
voyage-4-large
, 16.67% atop OpenAI v3 large, and 20.33% atop BM25.
Long documents.
On LongEmbed,
rerank-3
outperforms
rerank-2.5
, Qwen3-Reranker-8B, and Cohere Rerank v4.0 Pro by 3.35%, 4.95%, and 13.84%, respectively.
rerank-3-lite
outperforms
rerank-2.5-lite
, Qwen3-Reranker-8B, and Cohere Rerank v4.0 Pro by 1.86%, 4.92%, and 13.80%. The gains over
rerank-2.5
come from NarrativeQA and QMSum, where
rerank-3
improves by 3.77% and 6.20%; all Voyage rerankers score above 99% on SummScreenFD.
Code.
On our code datasets (DS-1000, APPS, CodeChef C++, RepoBench Java, and WikiSQL),
rerank-3
outperforms
rerank-2.5
by 2.17% atop voyage-3-large and 2.11% atop
voyage-4-large
, and
rerank-3-lite
outperforms
rerank-2.5-lite
by 3.72% and 3.58%. On CodeChef,
rerank-3
and
rerank-3-lite
improve by 2.45% and 2.63% averaged across retrieval methods.
Multilingual.
Averaged across the four first-stage retrieval methods,
rerank-3
outperforms
rerank-2.5
and Cohere Rerank v4.0 Pro on the 51 multilingual datasets by 0.52% and 1.19%, and
rerank-3-lite
outperforms
rerank-2.5-lite
by 0.80%.
Instruction-following.
Both models retain the instruction-following capability introduced in Rerank 2.5. On MAIR,
rerank-3
performs on par with
rerank-2.5
, and
rerank-3-lite
outperforms
rerank-2.5-lite
by 0.91%.
rerank-3
and
rerank-3-lite
outperform Cohere Rerank v4.0 Pro on MAIR by 3.58% and 2.34%, respectively.
Comparison with Jev.
We also evaluate the very recent Jev model in domains requiring strong expertise. Across 26 datasets,
rerank-3
leads Jev 1.13 by 1.77, 5.69, and 5.87 NDCG@10 points in code, law, and finance, respectively. We use the score mode for Jev and did not apply any specific prompt tuning. We did not perform a full eval due to rate limits.
Detailed results.
Numeric results for all evaluations are available in
this spreadsheet
.
Try rerank-3 and rerank-3-lite today!
As our results show, combining Voyage embedding models with Voyage rerankers delivers the highest possible retrieval accuracy.
Both
rerank-3
and
rerank-3-lite
are available today with flexible, token-based pricing, at the same price as
rerank-2.5
and
rerank-2.5-lite
: $0.05 and $0.02 per million tokens. For existing
rerank-2.5
and
rerank-2.5-lite
users, we recommend upgrading to
rerank-3
and
rerank-3-lite
, respectively. This upgrade provides better quality at the same cost and requires no code changes. We will continue to offer the
rerank-2.5
series for existing users who do not wish to upgrade.
For new users, head over to our
docs
to get started and learn more; the first 200M tokens are free.
rerank-3
and
rerank-3-lite
are also available to MongoDB Atlas customers through the Atlas Embedding and Reranking API and Native Reranking in Atlas Vector Search. Learn more in our
docs
here.
Follow us on
Twitter
and
LinkedIn
to stay up-to-date with our latest releases.
Contributors
Tengyu Ma, Project Advisor
Minghan Li, Project Lead
In collaboration with the Voyage team at MongoDB.
