---
source: https://x.com/i/article/2062633861515984896
title: "How we made continuous trace intelligence possible at scale"
author: Braintrust (Ankur Goyal)
date: 2026-06-04
fetched_via: x-bookmarks-ingest (xurl article.plain_text)
type: raw-article
tags: [observability, trace-analysis, clustering, bertopic, hdbscan, agent-traces, active-observability]
---

# How we made continuous trace intelligence possible at scale

If you run an agent in production, some part of your day is probably going through countless production logs to see if anything looks interesting. You know there's good intel in there somewhere, but the data doesn't tell you what question you should be asking, or what SQL query would capture it.

We've been thinking about this problem at Braintrust for a long time, and Topics is the solution that lets you analyze traces with intelligence at scale. Like Brainstore, it's one of the small number of big, concentrated technical bets we've made on owning a primitive end-to-end rather than stitching together off-the-shelf pieces. With Brainstore, the bet was on the storage and query layer. With Topics, the bet is on the intelligence layer that sits on top.

In order to find patterns you didn't know to look for, you need to run this intelligence layer over every trace. We call this active observability. The problem is that LLM traces aren't shaped like anything the standard tools expect. The standard NLP toolkit assumes documents that are roughly uniform in shape and size. Topic modeling wants bag-of-words documents in the hundreds of tokens. Sentiment analysis wants a sentence or paragraph. Off-the-shelf clustering on embeddings wants inputs that fit inside an embedding model's context window.

Agent traces don't look like that. A single production trace can be millions of tokens of conversation history, tool calls, intermediate reasoning, retrieved context, and serialized application state. They arrive at high volume, they keep updating after they're "done," and the interesting behavior is usually buried in a few spans out of hundreds. If you embed the raw trace, you get noisy clusters dominated by surface features like message length or tool name frequency. If you summarize first with an LLM, you blow your budget. If you sample aggressively, you miss the long tail, which is where the bugs usually live.

The insight that drove Topics is inspired by Anthropic's Clio paper. Instead of trying to embed or classify the raw trace, you ask an LLM to do one job: summarize the trace along a single dimension in a sentence or two. Then you embed that summary, cluster the embeddings, and name the clusters with a second LLM pass. The trace itself never has to fit in an embedding model's context window, and the downstream pipeline never has to know anything about agents, tools, or token counts.

This sounds like a small move, and architecturally it is. Operationally it changes everything. Once the LLM summary step exists, the same downstream pipeline works for any dimension you care about: task, issues, sentiment, and custom categories you define for your product all flow through the same embed, cluster, name, and classify stages.

Three design goals fall out of that bet. First, the LLM summary step has to be tightly scoped, batch-friendly, and cost-efficient enough to run on every trace. The output of that step is a facet, and it's the unit of work the whole pipeline is built around. Second, cluster generation has to be fast enough to run ad hoc without operator intervention, and the resulting topic map has to be stable enough that trend analysis across runs is meaningful. Third, classification has to be low-cost enough to run continuously, which means no LLM call at classification time.

The pipeline has six stages: preprocess, facet, embed, cluster, name, and classify. The preprocessor turns a raw trace into tokens. The default preprocessor walks every span in scope, parses each span as an LLM conversation, deduplicates messages across spans, and drops scorer spans. Raw traces can be enormous, so the output is hard-capped at 128K tokens before it ever reaches the facet model.

The facet stage is where the LLM does its one job. Each facet has a prompt, like "summarize what the user is trying to accomplish in one sentence," and an output schema. The facet model produces a short text blob, typically a sentence or two, and writes it back to the trace. The built-in facets are Task, Sentiment, and Issues. Custom facets can be anything from use case to SKU segmentation.

There's one optimization in this stage that matters a lot for cost. A naive implementation would compute facets one at a time, so running five facets on a trace would cost roughly five times the trace tokens plus five facet prompts. We batch facets into a single LLM call, so the cost is trace tokens plus the marginal prompt tokens for each facet. Trace tokens are paid once regardless of how many facets you run.

After the facet text is produced, we embed it with our embedding model. The thing to notice here is what we're embedding: the facet output, not the raw trace. That's what makes the rest of the pipeline tractable. A consistent, short, on-topic summary embeds cleanly. A million-token agent trace does not.

Once enough facet embeddings have accumulated, the clustering stage runs on a sample of up to 50,000 facets per generation pass. The default algorithm is HDBSCAN with UMAP for dimensionality reduction. HDBSCAN works well because it doesn't require you to pick the number of clusters up front, and it naturally identifies outliers as noise rather than forcing every point into a cluster. For keyword extraction per cluster, they use c-TF-IDF, the same approach BERTopic popularized.

The naming stage takes representative facet examples for each cluster and asks an LLM to produce a short name and description. This is generative, which means the same cluster can pick up a slightly different name on the next generation pass even if the underlying membership barely changes. That's why they treat the cluster, not the name, as the stable identity. When a new topic map is generated, they automatically match similar clusters to their predecessors and reuse their IDs.

Classification is the lightweight part. For each new trace, they run the preprocess, facet, and embed stages, then look up the nearest cluster centroid in the saved topic map. If the trace is within the configured distance threshold, it gets a label. If it's not, they write no_match instead of forcing a bad label. No LLM call happens at classification time. The whole step is around 100 milliseconds per trace.

The result lands on the trace as structured data. From that point on, it behaves like any other column in your logs. You can filter on it, group by it, join across topic maps, query it from SQL, or alert on it.

The other half of Topics is the automation layer that runs the pipeline continuously in the background. A topic automation starts by accumulating facet data, then recomputes topic maps, backfills recent traces with the new map, and settles into idle until the next scheduled run. You need at least 400 traces in a project for Topics to start, and at least 100 unique facet summaries before it will generate a topic map. Below those numbers, the clusters aren't meaningful, and they'd rather show you nothing than show you noise.

There are two places in the product where you'll see clusters. The Topics view shows the automated topic map: the same persistent set of clusters, the same names, applied consistently to your logs over time. This is what you want for trend dashboards, alerting, and analysis that needs to be comparable across days or weeks. The "Cluster traces by facet" action runs ad hoc clustering on whatever subset you're currently looking at, with parameters tuned for exploration. Both views use the same pipeline. The difference is whether the topic map is persisted and reused or generated on the fly.

All native Topics inference runs on Baseten. The facet model sees preprocessed text capped at 128K tokens and stripped of attachments and metrics. The embedding model only ever sees the facet output, never the raw trace. The clustering step operates on embeddings and facet outputs, never on raw trace contents. Topics inference can be hosted in both the US and EU, and Braintrust is HIPAA compliant.

The architectural choices translate into a few concrete properties you feel as a developer. The pipeline runs continuously rather than as a batch job. Outputs are queryable, not just available in the UI. One pipeline serves every dimension you care about. Topic identity stays stable across regenerations. The built-in facets and default preprocessor work out of the box, and when your trace shape is unusual, you can drop in a custom JavaScript preprocessor that returns exactly the spans you want clustered on.

Topics is the second of the bets they've talked about publicly, and like Brainstore, it has only gotten more useful as the product has grown. They think of it as the most universal baseline layer of intelligence you can run across your traces. The more expensive and more powerful layers they're building sit on top of that baseline, and they think this pipeline shape is going to continue to be useful as production AI workloads keep getting more complex.
