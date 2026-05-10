---
title: "When "Performance" Means Two Different Things"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/performance-as-a-measurement/"
scraped: "2026-05-10T01:27:46.234090+00:00"
lastmod: "2026-03-16T15:27:40Z"
type: "sitemap"
---

# When "Performance" Means Two Different Things

**Source**: [https://www.pinecone.io/blog/performance-as-a-measurement/](https://www.pinecone.io/blog/performance-as-a-measurement/)

←
Blog
When "Performance" Means Two Different Things
Noah Rizika
,
Lea Wang-Tomic
Mar 3, 2026
Research
Share:
Jump to section:
Two Types of Performance
Why the Distinction Matters
What to Do
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
TLDR
: In AI applications, "performance" refers to two distinct concepts: infrastructure metrics (latency, throughput, cost) and result quality (accuracy, precision, relevance). Conflating them causes confusion. This post breaks down the difference and shows why discussing both independently matters.
We see "performance" thrown around constantly in conversations about AI applications. Teams often say "we need to optimize for performance" or "performance regressed after the latest deploy". Ultimately, the word "performance" doesn't refer to any specific metric.
Performance describes two fundamentally different technical concepts:
how fast and efficient
your infrastructure
is
versus
how accurate and useful your results are
. Conflating them creates misalignment between teams and missed expectations with stakeholders. This post clarifies what each type means, why they're independent, and how to approach them.
Two Types of Performance
To build a reliable AI product, you must monitor two separate "scoreboards." While they often influence one another, they are measured with entirely different tools.
Infrastructure Performance:
This is what database and platform teams get alerted on. It’s deterministic, quantifiable, and frequently benchmarked. If this fails, your system is "broken" in the traditional sense.
Latency:
Did the query return in 50ms, or is the user staring at a loading spinner?
Throughput:
Can the system handle 10,000 queries per second during a traffic spike?
Cost:
What is the cost per million operations? Is the unit economics of the app sustainable?
Result Quality:
This is what users actually experience and what product teams care about. Result quality is determined by the entire retrieval pipeline. If this fails, your system is "hallucinating" or useless, even if it’s lightning-fast.
Chunking strategy
: How documents are split and structured before embedding.
Embedding model
: Which model embeds data into vectors.
Query embedding approach
: How user questions get vectorized.
Retrieval parameters
: How many results to return ($k$-nearest neighbors) and what metadata to filter on.
Query routing and expansion
: Whether to split one query into multiple, rewrite it for tailored results, and/or expand the context around returned results.
Semantic Search
: What proportion of embeddings are searched over, accounting for index size and metadata filtering.
Reranking results
: Post-retrieval scoring to reorder results by relevance before they reach the LLM.
LLM prompt, context, and guardrails
: How the retrieved context is synthesized into a final answer.
The Vector Database Factor:
The result quality pipeline is centered on fostering a high quality semantic search. A good vector database should solve the AI infrastructure layer out-of-the-box by excelling not only in highly accurate recall, but in top performing indexing and retrieval. This allows developers to stop worrying about low-level systems optimization and focus their "performance budget" on their greater retrieval pipeline.
Why the Distinction Matters
Infrastructure performance and result quality can move in opposite directions. In one evaluation, a team tested two dataset versions where the second was optimized to reduce cost by cutting 40% of the dataset’s size. They found:
Infrastructure performance improved:
Throughput increased and costs fell because the index was smaller.
Result quality regressed:
Using an LLM-as-a-judge to score correctness, the new version underperformed. The root cause was aggressive data pruning that removed chunks critical for relevant answers.
The tradeoff between accuracy and cost became clear. Without measuring both types of performance independently, the team would have celebrated an "optimization" that actually degraded the user experience.
What to Do
Be explicit about which performance is being measured.
Infrastructure performance
is table stakes. If latency is high or cost is unpredictable, nothing else matters. Track p95 latency, queries per second, and cost per query.
Result quality
is what users see. Consider accuracy scores, task completion rates, and user feedback. Optimize it by testing changes across the entire pipeline, not just one aspect.
When teams report performance regressions, the first question should be: which type?
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
Learn
Jun 28, 2025
Chunking Strategies for LLM Applications
Roie
,
Arjun
Learn
Jun 30, 2023
What are Vector Embeddings
Rajat Tripathi
Learn
May 15, 2024
A Developer’s Guide to Approximate Nearest Neighbor (ANN) Algorithms
Brian
,
Xian
