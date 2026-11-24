---
title: "What way, old man? Why we started Hornet"
source_url: "https://hornet.dev/blog/why-we-started-hornet"
fetched: 2026-11-24
type: raw-article
---

---
title: "What way, old man? Why we started Hornet"
description: "Two decades in search taught us to adapt as hardware and workloads changed. Agents are now changing who we build retrieval for."
excerpt: "Lessons from two decades in search, and why we're building a retrieval engine for agents."
date: "2026-11-12"
authors: ["bergum", "baldersheim"]
tags: ["Hornet.dev"]
category: "Thinking traces"
heroImage: "hero.webp"
---

When we started Hornet, we spent a lot of time walking the forest trails around Trondheim, discussing nearly twenty years of building retrieval systems together. Those discussions centered on two observations:

1. **Building relevant retrieval is hard.**
2. **Building and scaling retrieval workloads is hard.**

(*“Why this hard?”*, as we used to say at Yahoo.)

Throughout our careers, we have seen teams with data scientists, ML specialists, and search engineers struggle with both. Improving relevance while scaling retrieval multiplies the complexity: a ranking change can require more compute, while a limit on query cost can restrict which documents get scored. A simple change like adding phrase matching or more query terms affects both result quality and [serving cost](/blog/agentic-query-workloads-change-retrieval-cost).

We wanted a simpler way to build relevant retrieval and scale it efficiently. We had spent years reworking systems as hardware, models, and workloads changed, so adaptability was a requirement from the start. We chose to bring retrieval methods, ranking, and scalable execution into one runtime that developers and agents could configure, evaluate, and improve.

We think [agents becoming the user of retrieval](/blog/the-case-for-a-new-retrieval-engine-for-agents) will be the biggest change of our working lives. The earlier shifts changed the systems around a largely human user. This changes the user too, and we are only seeing the start of it.

## Hardware evolves

We started working together in January 2007 at Yahoo. The search platform we developed and ran served queries for Yahoo's products from the company's own data centers. This was before cloud, and what we now call bare metal was simply what we had: servers with typically two to four CPU cores and 4 to 8 GB of DRAM. Memory was expensive, so we spent time finding ways to use less of it. To handle larger datasets within those limits, we had to shard early, so a single query could involve many nodes.

### Memory

That constraint changed over the next two years. 

{% decades-dram /%}

*McCallum's retail memory price series, 2006 to July 2024 [[1]](https://tinyos.stanford.edu/memory-prices.html)*


More memory let us keep more documents per node and use fewer shards for the same dataset. It also made different indexing designs practical.

Henning led a rewrite of the core indexing code to better use the additional memory (beyond page cache), retaining much of the throughput of batch indexing while making updates searchable in real time. Flickr needed both high update throughput across a large corpus and tag changes that users could search for immediately. We could acknowledge the tag update once it was searchable, so the next query would see the change.

Jeff Dean describes a similar pattern of search-system rewrites at Google. [[2]](https://research.google.com/people/jeff/Stanford-DL-Nov-2010.pdf)

### CPU cores

Core counts grew faster than clock speeds, so getting more out of a server increasingly depended on finding work that could run in parallel. [[3]](https://www.amd.com/en/products/processors/server/epyc/9006-series/amd-epyc-9996.html)

{% decades-cpu-cores /%}

More cores changed how much data we could serve from each node. When a query used one CPU thread, we often had to shard a growing index across more nodes to keep query latency in check. Intra-query parallelism let us split one query's work across cores on the same server, making larger indexes per node practical (when memory and I/O allowed it). [[4]](https://www.microsoft.com/en-us/research/publication/predictive-parallelization-taming-tail-latencies-in-web-search/)

More docs per node would also reduce how many nodes each query needed to touch (fan-out). A query that waits for every shard is delayed by the slowest response. Spreading the work across more nodes can amplify the effect of latency variation on a single node, increasing tail latency for the complete query. Dean and Barroso describe this effect in *The Tail at Scale*. [[5]](https://research.google/pubs/the-tail-at-scale/)

### Storage

The move from spinning disks to SSDs changed the cost of random access. NVMe then increased throughput, with Micron now specifying up to 28 GB/s of sequential reads for its Gen6 9650. [[6]](https://www.micron.com/content/dam/micron/global/public/products/storage/ssds/data-center/9650/9650-nvme-ssd-product-brief.pdf)

{% decades-storage-bandwidth /%}

This brings us back to the memory decision. Keeping data in RAM avoids storage reads, but faster (and cheaper) storage changes how much memory we need. A workload dominated by random lookups makes a different case for memory than one that scans data sequentially.

## Workloads, workloads, workloads

Workloads matter the most. Flickr needed updates searchable when acknowledged by the system; an index rebuilt overnight may not. 

A service may store a billion or trillion documents, which might sound impressive, yet route every query directly to a preconfigured tenant partition or namespace containing only a few thousand where the search problem is trivial. An exact scan of that small set may be simpler and more efficient than building indexes to accelerate a few queries per second. [[7]](https://arxiv.org/abs/2403.04871)

Standing up a service that searches across billions of documents without a partition key is a different challenge that requires a different architecture. 

Supporting multi-tenancy is another challenge where we have seen teams struggle with legacy infrastructure. Searching a global ANN index and filtering the returned candidates by tenant can discard most of the results. Restricting graph traversal to the tenant's documents up front can reduce recall and impact performance. [[7]](https://arxiv.org/abs/2403.04871)

Traffic adds another dimension. A service handling 10,000 queries per second with tight tail-latency targets may need a different query execution strategy from a background job that can wait seconds. 

## Scaling retrieval

We have seen engineers try to scale retrieval by adding nodes without accounting for how the retrieval algorithm scales with dimensions like data volume and queries. Index freshness too. And as more infrastructure has added more retrieval methods, it has become easier to shoot yourself in the foot when scaling (figuratively).

Scaling retrieval is hard. Well, scaling retrieval algorithms that scale linearly with the number of documents is relatively easy. Divide N over K nodes and total work becomes K × (N/K), which equals N. We have seen cases where engineers have scaled up systems with 10× the nodes and cost for only 2× the query throughput, maybe even less, because the retrieval algorithm was closer to log(N) than N. When every query searches every shard, the work per shard shrinks far less than the data.

At a billion documents, we therefore need more than a document count to decide how to scale. We need to understand the properties of the top-k retrieval algorithm. Sharding spreads data across nodes and can reduce the latency through parallel work. Replication adds capacity for concurrent queries and redundancy. The two can be combined; which to add depends on whether the constraint is storage, query latency, throughput, or availability. 

Even better, before scaling, we need to understand and benchmark the workload using representative data, queries, filters, and update rates. Then we can identify bottlenecks and test whether adding capacity or changing the execution strategy improves throughput, latency, or cost at the required result quality.

## Retrieval methods evolve

We saw ranking move gradually from linear models to gradient-boosted decision trees (GBDTs). At Yahoo, these models served web search and several verticals, but collecting clickstream data, training models, and maintaining evaluations required resources few organizations could sustain. [[8]](https://doi.org/10.1145/2939672.2939677)

The pace accelerated with fancier neural methods such as Transformers in 2017 and BERT in 2018. [[9]](https://arxiv.org/abs/1706.03762) Pretrained models made learned retrieval and ranking more practical for more teams, with many off-the-shelf embedding models on Hugging Face. After ChatGPT's release in November 2022, [[10]](https://openai.com/index/chatgpt/) we noticed a big uptick in teams interested in retrieval due to RAG. Those teams faced a steady stream of retrieval techniques promising better results, often adding more models, retrieval stages, and settings to assemble and maintain.

Older methods still have value. BEIR showed that dense retrievers could perform worse than BM25 outside their training data. [[11]](https://arxiv.org/abs/2104.08663) 

To put these to real work, teams have to evaluate combinations on their own data and queries, then make them work within a serving budget. As these methods evolved, putting the system together became harder. 

But there is hope in sight. LLMs can now supply relevance judgments for evaluation [[12]](https://arxiv.org/abs/2411.08275) and synthetic training examples, [[13]](https://arxiv.org/abs/2209.11755) reducing the need to collect clickstreams. But teams still have to integrate, evaluate, and operate the resulting system.

## Retrieval has a new user

Some of the changes we have described happened gradually; others came quickly. Each forced us to revisit assumptions and adapt our systems.

Agents are the new user of retrieval infrastructure. It's a new type of workload. A person has limited time to type queries and read results; an agent can generate long queries and issue many of them in parallel. It can also inspect results, refine a query, and search again. [[14]](https://arxiv.org/abs/2210.03629) Our [analysis of published agent traces](/blog/this-is-what-agentic-retrieval-looks-like) shows phrases, query operators, and many sequential queries within a task. [Each query adds serving cost](/blog/agentic-query-workloads-change-retrieval-cost); sequential queries also accumulate latency. Query execution needs to be efficient, and the engine needs to handle concurrent queries within the task's latency budget.

The results also enter a different reading process. A person can skip an irrelevant result without much cost. A model may carry it into context and use it as a premise in later reasoning, as we explored in [Mutually assured distraction](/blog/mutually-assured-distraction). Reading those results also costs money: a 24-search task returning five full 512-token snippets per search would cost about $0.61 to read once at GPT-6 Astra's standard uncached input rate of $10 per million tokens. [[15]](https://developers.openai.com/api/docs/models/gpt-6-astra) A search results page (SERP) for agents has to account for both the quality of the evidence and the cost of putting it into context.

We have learned a lot about this new workload by working with organizations using Hornet to build large-scale web search APIs for agents and search over more focused collections: company and product data, research documents, and internal knowledge bases. An agent may need to search across several of these collections during one task. [Relevance is the horizontal challenge](/blog/the-case-for-a-new-retrieval-engine-for-agents), while freshness, isolation, and serving cost depend on the use case.

## Conclusion  

Our thesis is that investing in retrieval is mandatory for any organization that wants agents to work with its data. That brings us back to the two problems we started with: getting relevant results and scaling the workload. An engine for agents has to make both easier for organizations of any size.

That the workload changes with agents is well recognized. But we believe that agents should also be able to configure and improve their own retrieval. For example, an agent can change a scoring configuration, test it against judged queries, and compare quality and query cost before adopting it. We described many of these choices in [How we build a retrieval engine for agents](/blog/how-we-build-a-retrieval-engine-for-agents).

We have been fortunate to work with companies that share our thesis, and their query volumes are growing rapidly. Our initial bets are paying off: better agents help us build and tune the engine, while better retrieval gives agents better context. Progress in relevance compounds as models improve. 

*In the next post, we'll look more closely at vector search: model quality, ANN accuracy, quantization, updates, and serving cost. To be notified when it lands, {% signup-link %}join our user community list{% /signup-link %}.*

## References

1. [McCallum memory-price data, preserved by Stanford DAM](https://tinyos.stanford.edu/memory-prices.html). Retail prices, nominal USD.
2. [Jeff Dean, Building Software Systems at Google and Lessons Learned](https://research.google.com/people/jeff/Stanford-DL-Nov-2010.pdf), 2010.
3. [Intel Xeon 5160 in a 2006 SPEC submission](https://ftp.spec.org/cpu2006/results/res2006q4/cpu2006-20060918-00108.html) and [AMD EPYC 9996 specifications](https://www.amd.com/en/products/processors/server/epyc/9006-series/amd-epyc-9996.html). [Chart data and model sources](/blog/why-we-started-hornet/hardware-data.json).
4. [Jeon et al., Predictive Parallelization: Taming Tail Latencies in Web Search](https://www.microsoft.com/en-us/research/publication/predictive-parallelization-taming-tail-latencies-in-web-search/), SIGIR 2014.
5. [Dean and Barroso, The Tail at Scale](https://research.google/pubs/the-tail-at-scale/), Communications of the ACM, 2013.
6. [Micron 9650 product brief](https://www.micron.com/content/dam/micron/global/public/products/storage/ssds/data-center/9650/9650-nvme-ssd-product-brief.pdf). [Chart data, drive specifications, and test conditions](/blog/why-we-started-hornet/hardware-data.json).
7. [Patel et al., ACORN: Performant and Predicate-Agnostic Search Over Vector Embeddings and Structured Data](https://arxiv.org/abs/2403.04871), 2024 ([PDF](https://petereliaskraft.net/res/acorn.pdf)).
8. [Yin et al., Ranking Relevance in Yahoo Search](https://doi.org/10.1145/2939672.2939677), KDD 2016 ([PDF](https://www.kdd.org/kdd2016/papers/files/adf0361-yinA.pdf)), and [Louis et al., Use of Query Similarity for Improving Presentation of News Verticals](https://ceur-ws.org/Vol-880/VLDS-p62-Louis.pdf), VLDS 2011.
9. [Vaswani et al., Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017, and [Devlin et al., BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805), 2018.
10. [OpenAI, Introducing ChatGPT](https://openai.com/index/chatgpt/), November 30, 2022.
11. [Thakur et al., BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models](https://arxiv.org/abs/2104.08663), 2021.
12. [Upadhyay et al., A Large-Scale Study of Relevance Assessments with Large Language Models: An Initial Look](https://arxiv.org/abs/2411.08275), 2024.
13. [Dai et al., Promptagator: Few-shot Dense Retrieval From 8 Examples](https://arxiv.org/abs/2209.11755), ICLR 2023.
14. [Yao et al., ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629), ICLR 2023.
15. [OpenAI, GPT-6 Astra pricing](https://developers.openai.com/api/docs/models/gpt-6-astra). Standard uncached input: $10.00 per million tokens; checked November 10, 2026.