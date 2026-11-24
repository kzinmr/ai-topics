---
title: "Big graphs, small vectors: HNSW at a billion"
source_url: "https://hornet.dev/blog/big-graphs-small-vectors-hnsw-at-a-billion"
fetched: 2026-11-24
type: raw-article
---

---
title: "Big graphs, small vectors: HNSW at a billion"
description: "HNSW's query cost grows much more slowly than the graph, so we keep graphs as large as memory allows and quantize vectors to fit."
excerpt: "Every extra HNSW graph adds a full search to every query. Here is why we keep graphs as large as memory allows, quantize vectors to 2 bits, and rescore against full vectors on disk."
date: "2026-11-19"
authors: ["baldersheim"]
tags: ["Infrastructure"]
category: "Proof"
heroImage: "hero.webp"
---

Embedding-based retrieval makes unstructured data searchable by meaning. Scaling it to billions of vectors is a hard systems problem. That requires balancing [memory, CPU and disk I/O](/blog/why-we-started-hornet) with a firm hand.

A solution had to meet four criteria:

1. True real time. When a write returns, the new document must be visible to every query that follows.
2. A high query rate, with low and predictable latency.
3. Scaling well with hardware, with balanced use of memory, CPU and disk.
4. Good recall: the true neighbors must be found.

Brute force, computing the distance from the query to every vector, is exact but does not scale: for example, at 1B vectors of 1,024 dimensions in bfloat16, each query would read about 2 TB and compute 1B distances. So we chose to approximate.

[HNSW](https://en.wikipedia.org/wiki/Hierarchical_navigable_small_world) (Hierarchical Navigable Small World, from [Malkov and Yashunin's paper](https://arxiv.org/abs/1603.09320)) is one of many approximate nearest neighbor (ANN) algorithms. It is a graph over all the vectors, held in memory, where each vector links to some of its nearest neighbors, and it supports immediate visibility.

HNSW's query cost grows much more slowly than the graph, but the graph and vectors must fit in memory. When the data is split over several graphs, every query traverses all of them, so we want few, large graphs. Memory is the bottleneck, so we quantize vectors to 2 bits and keep the full resolution vectors on disk for rescoring.

We did not know up front whether recall would hold as one graph grew from 100M to 1B vectors, and HNSW's advantage depended on it.

We wanted to support very large corpora in true real time, so we set out to test whether HNSW was up to it. For that, it had to use less memory and keep its recall as the graph grew. We start with how its search cost grows with the graph.

## How does HNSW search scale?

Two settings decide how many distance computations a search makes. We use Hornet's names:

- Max-links: how many direct neighbors a vector can have (M in the HNSW paper, R in DiskANN).
- Top-K: how many of the best candidates found so far a search keeps (ef in the HNSW paper, efSearch in some libraries, the search list size L in DiskANN).

A search looks only at the neighbors of its top-K best candidates, so on average it costs about **top-K × max-links** distance computations. This is an average observed over many queries, not a bound.

{% themed-image light="search-keeps-top-k-light.svg" dark="search-keeps-top-k-dark.svg" alt="Diagram: a cut-out of a small graph around a query point, with three kinds of points: 8 larger points kept as the top-K best, 16 points that were checked but not kept, and small hollow points that were never reached. Dashed lines are one-way links. A tally reads 24 distance computations, against top-K × max-links = 8 × 4 = 32." /%}

*One synthetic search with top-K 8 and max-links 4: it kept its 8 best candidates and computed the distance to 16 more points that it did not keep.*

We measured the cost on the data in the next post: 1B vectors, 2-bit quantization and 32 max-links. At a top-K of a thousand, a search makes about 25,000 distance computations.

A search's CPU cost is roughly linear to its distance computations, so large graphs are computationally efficient.

## Where HNSW is good

HNSW achieves good recall with few distance computations. It also builds a stable graph: each vector's top layer is drawn at random, so the layer structure does not depend on the insertion order.

HNSW is incremental by design: vectors go in as they arrive, and the stable graph allows modifications with concurrent readers. An insert is a graph search followed by link updates, with no training step to redo as the data changes.

HNSW's large memory footprint has fostered alternatives, such as [DiskANN](https://papers.nips.cc/paper_files/paper/2019/hash/09853c7fb1d3f8ee67a61b6bf4a7f8e6-Abstract.html) and variants of [IVF](https://github.com/facebookresearch/faiss/wiki/Faiss-indexes), which keep a small part in memory and most on disk. But both, as first described, need knowledge of the data up front, so they require a preprocessing step. None of those we briefly tested fit our needs; most failed the real-time requirement.

You can build a better, more efficient graph with preprocessing, but for our workload it is very hard to beat HNSW's stability and ease of use.

## Where HNSW is bad

Memory is the Achilles heel. The graph and the vectors it searches must stay in memory, because random disk access would cost too much. A search computes the distance to all the neighbors of a candidate before it chooses where to go next, so each step waits for the one before. That costs latency, but throughput is the bigger problem: at a top-K of a thousand, each query would read the vectors for about 25,000 distance computations from disk, too costly at thousands of queries per second.

Efficiency prescribes large graphs, so you want machines with as much memory as possible. In AWS you would end up with their x8g at 16 GB per CPU core. 1B 1,024-dimension vectors at 2-bit quantization need around 400 GB of memory. A 1TB machine capable of holding at least 2B vectors would give you 64 cores, far more CPU than the graph search needs. So unless you can use that spare CPU for something else, like rescoring for better accuracy or lexical search, HNSW is not for you.

Two common workloads are better served another way. With few queries, an index such as IVF can keep most vectors on cheaper storage, even object storage, and fetch only the clusters a query needs, trading query latency for lower storage cost. With naturally partitioned data, as in a multi-tenant application where each query stays inside one tenant's documents, you do not need one large graph. Brute force or a small IVF index over those documents is enough.

## Scaling HNSW is hard but worth it

What makes it worth it is how the work per query grows with the amount of data. In an inverted index for lexical search, twice the documents means posting lists about twice as long, and twice the CPU. In a graph, at a given top-K, finding the hundred best neighbors does not cost much more as the graph grows, if recall holds without increasing top-K or max-links too much.

HNSW scales well within one machine, but only until the graph and vectors no longer fit. Then you either build a distributed graph, which is complicated, or you shard.

Sharding divides the data, but the work does not shrink in proportion: every query searches every shard, and the total work goes up, because every graph pays the basic cost of a search, **top-K × max-links**. The same happens when an index is built as many smaller graphs (segments) merged over time: every query searches every segment.

{% themed-image light="one-graph-or-ten-light.svg" dark="one-graph-or-ten-dark.svg" alt="Diagram and bar chart: on the left, 1B vectors in one graph; on the right, ten graphs of 100M each. Bars on one scale show about 25,000 distance computations per query for one graph and about 150,000 for ten, about 6 times the work." /%}

*One graph of 1B 2-bit vectors against ten of about 100M each, 32 max-links, 1,000 queries. At the same recall@100, about 65%, before rescoring, one search at top-K 1,024 made about 25,000 distance computations; ten searches at a top-K of about 600 each made about 150,000 in total.*

This post is about efficiency, not latency. Latency follows efficiency as a graph grows or shrinks, but once you shard, latency stays put and efficiency drops. Sharding a text index is the reverse: latency goes down, and efficiency stays put.

At the same recall@100, about 65%, before rescoring, ten graphs of about 100M needed about six times the distance computations of one graph of 1B, so we avoid sharding for as long as possible. That means memory per vector must go down.

## How quantization cuts memory

Quantization shrinks the vector, not the graph.

{% themed-image light="memory-per-vector-light.svg" dark="memory-per-vector-dark.svg" alt="Bar chart of memory per vector, to scale: a bfloat16 vector of 2,048 bytes plus a graph of about 150 bytes (about 2.2 KB per vector, 2.2 TB per billion); a 4-bit vector of 512 bytes plus the same graph (about 660 bytes, 660 GB per billion); a 2-bit vector of 256 bytes plus the same graph (about 400 bytes, 400 GB per billion)." /%}

*Memory with full, 4-bit and 2-bit vectors (the 1,024-dimension example, 32 max-links), bars to scale. The vectors shrink to one quarter and one eighth; in total, the 4-bit version needs around one third and the 2-bit version around one fifth.*

At 32 max-links, the graph takes about 150 bytes per vector (about 110 bytes at 24 max-links and about 240 bytes at 64 max-links; the exact number depends on the data). The full vectors, about 2 TB per billion, move to disk.

Distances on 2-bit vectors are rough, so their top candidates are not always the nearest. A larger top-K helps a bit, and so does rescoring, the second step of a search: the graph search runs on the quantized vectors, then every top-K candidate is rescored against its full vector, read from local NVMe drives.

Whether rescoring is necessary depends on the recall you need; on the data in the next post, 2-bit vectors needed it to reach 95%.

Why can the full vectors live on disk when the graph and quantized vectors cannot? The graph search follows links step by step, but rescoring reads only top-K full vectors, together, once the candidates are known. SSDs handle such small random reads well, at a lower cost than memory.

At a top-K of a thousand, the graph search makes about 25,000 distance computations on 2-bit vectors in memory, and rescoring makes about a thousand against full vectors on disk, one for every 25 or so.

Both grow with top-K, so top-K is a lever between quality and cost: a larger top-K gives more recall for more CPU and disk reads, not more memory.

Rescoring can only reorder the candidates the graph search found. It cannot add a true neighbor the search missed.

{% themed-image light="rescoring-reorders-candidates-light.svg" dark="rescoring-reorders-candidates-dark.svg" alt="Diagram: two ranked lists of the same six candidates, A, B, D, E, F and G, with a dot on each true nearest neighbor, A and B, in both lists. The quantized order is D, A, F, B, E, G and returns D, A, F: 1 of 3 true. The rescored order is A, B, D, E, F, G and returns A, B, D: 2 of 3 true, because B moves into the results. The true nearest three are A, B and C. C is in neither list, so no rescoring can find it." /%}

*A synthetic example with six candidates and three results. Rescoring moves B into the results. C was never a candidate, so rescoring cannot add it.*

## A global merge wins back some of what sharding costs

Now suppose the data grows from 1B to 10B vectors, more than one machine can hold. We do not build a distributed graph, so the data goes over several machines, for instance ten, each with its own graph, and every query searches all of them. We take that cost in the graph search, and win some of it back by global merge between rescoring phases.

Each machine runs the cheap 2-bit graph search at a top-K of a thousand and sends up its best 1,000. The global merge collects those 10,000 and sends only the best, for instance 2,000, back down for rescoring. Each machine then rescores about 200 on average, not all 1,000 of its own.

{% themed-image light="global-merge-light.svg" dark="global-merge-dark.svg" alt="Diagram of one query over ten machines: a global merge box, labeled 'keeps 2,000 of 10,000', above Machine 1, Machine 2 and Machine 10. Between the merge and each machine are three arrows: a dashed arrow down for the search, an arrow up for the machine's top 1,000, and an arrow down for the candidates sent back to rescore." /%}

*Illustration, not a measurement: ten machines of about 1B 2-bit vectors each. The best 1,000 go up from each machine, the best 2,000 back down for rescoring (about 200 per machine), and the best 100 are returned.*

A true neighbor the merge leaves out is never rescored, so how many it keeps is also a lever between quality and cost.

## As few graphs as possible, if recall holds

Neither the literature nor our earlier experiments said clearly whether recall holds as the graph grows. [The ParlayANN paper](https://arxiv.org/abs/2305.04359) (PPoPP 2024), on graph indexes up to a billion vectors, HNSW among them, wrote that a search with the same settings is less accurate on a larger graph, because it visits a smaller share of it. Some loss is expected; the question was whether recall dropped faster. We assumed that was more a question of the data than the algorithm.

In the data, embedding quality matters most. In high-dimensional spaces all neighbors are far away, so you need villages to have neighbors; random data has none. We trusted that embedding models had become good enough to give many small, separate villages instead of a few big cities, and we expected quantization to act like a low-pass filter, smoothing out detail while keeping that structure. The risk was that the villages would blur into one as the graph grew, and the search would miss the true neighbors.

For our own tests we used Qwen3-Embedding-0.6B, a promising model with 1,024 dimensions. Our first experiments, from 1M to 10M to 100M vectors, showed recall deteriorating faster than we hoped. More bits and rescoring regained quality, which suggested the structure was still there, but more bits cost memory.

Memory had to go down, so we needed better embeddings and better quantization. Qwen3 had already improved the embeddings, but information was still unevenly spread across the dimensions. [RaBitQ](https://arxiv.org/abs/2405.12497) showed how a random rotation can spread a vector's signal across the dimensions before quantization.

We used [TurboQuant](https://arxiv.org/abs/2504.19874), which also rotates the vector and then quantizes each coordinate using levels fixed in advance. We can encode each vector as it arrives, without training on a sample of our data. TurboQuant builds on what RaBitQ found out: RaBitQ made it possible, and TurboQuant made real time simple.

We want as few graphs as possible, as large as a machine allows, and recall has to hold as they grow. We needed to find out:

1. How much recall 2-bit and 4-bit quantization would lose, measured by the recall ceiling: the recall of an exact scan over the quantized vectors, without rescoring.
2. How much of that loss rescoring could regain.
3. How much top-K had to grow to hold recall from 100M to 1B vectors. If it had to grow linearly with the graph, HNSW would lose its advantage.

The next post tests whether recall holds, with numbers for each question, what sharding costs and what we know so far about rescoring cost.

_Editor's note: the next post is coming soon. To hear when it is out, sign up for Stay in the Loop at the bottom of this page._