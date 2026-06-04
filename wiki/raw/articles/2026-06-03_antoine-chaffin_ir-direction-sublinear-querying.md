---
title: "Antoine Chaffin on IR Direction: Sublinear Querying, Not Reconstruction"
author: Antoine Chaffin (@antoine_chaffin)
date: 2026-06-03
source_url: https://x.com/antoine_chaffin/status/2062081232842682448
type: x-thread
tags: [information-retrieval, embeddings, sparse-retrieval, dense-retrieval, late-interaction, colbert, sublinear-search, representation-learning]
---

# Antoine Chaffin on IR Direction: Sublinear Querying, Not Reconstruction

**Source**: https://x.com/antoine_chaffin/status/2062081232842682448
**Date**: June 3, 2026

## Context Chain

This tweet is part of a discussion thread sparked by Mixedbread's "Latent Terms" blog post:

1. **@mixedbreadai** (original announcement): "By now, everyone knows that single-vector embedding models are hugely limiting for modern workflows. But they contain more than you think: you can extract sparse Latent Terms from them. And it turns out that BM25 is all you need to turn this vocabulary into a strong retriever." (188 likes, 23 RTs)

2. **@bclavie (Ben Clavié)** (quote tweet): "my main takeaway from this isn't 'oh, this is cool! BM25 works on hidden activations!' but 'we understand so little about retrieval that models have an entire sparse indexable world we knew almost nothing about'. future's bright, tons of work to do." (122 likes, 76 bookmarks)

3. **@antoine_chaffin** (this tweet, quoting @bclavie): See full text below.

## Antoine Chaffin's Analysis (Full Text)

Despite being insanely cool results by itself, I think this study highlights something much more important for the future direction of IR

The goal has never been to create representations that contains all the information about the original input. We know for a very long time (e.g, 2023 from @jxmnop [arxiv.org/abs/2310.06816](https://arxiv.org/abs/2310.06816)), that dense - single vector - embeddings contains enough information to reconstruct the input given enough decoding capability.

The BP frames it very nicely: "the role of the embedding model is to convert the information in the documents into a format that can be readily consumed by the efficient scoring mechanism we discussed above"

What we are trying to do, is encoding this information that is _queryable_ in **sublinear time**. You can pre-compute a very large part of the document representations and only do small cross-encoding operations to recover most of the cross-encoder (reranker performance) (@_VictorMorand_ [arxiv.org/abs/2602.16299](https://arxiv.org/abs/2602.16299)). You would still be unable to search among millions of documents unless you have a first stage retriever that look for this information in sublinear time.

To enable this, information retrieval needs to create a structure that allows to traverse our documents pool quickly while finding everything that is relevant for a query. The dense space does that by leveraging spatial proximity and finding elements that are in the same neighborhood. The sparse space does so by leveraging the overlaps of components activated between two elements. Both shares a lot (and I would love to come up with an unified theory about them), but they are intrinsically representing the information in two different ways that enable fast search.

More than ever it is important to question everything we have been doing and what we know and start asking fundamental questions. We should stop asking ourselves "how do I encode all of my information", but "how do I present the information such that I am able to query it quickly and accurately"

ColBERT models lifted some limitations of dense - single vector - models. But so does sparse retrieval, in a different way. Maybe the question is not which one is going to win, but whether we'll find something even better in the way

## Key Arguments

1. **Information reconstruction ≠ retrieval goal**: Dense embeddings already contain enough info to reconstruct inputs (known since 2023). The real goal is making information **queryable in sublinear time**.

2. **Scoring mechanism as the real constraint**: The embedding model's role is to convert document info into a format consumable by an efficient scoring mechanism.

3. **Dense vs Sparse are complementary**: Dense leverages spatial proximity, sparse leverages component overlap. Both enable fast search in different ways. A unified theory is needed.

4. **Reframe the question**: Stop asking "how do I encode all information" → ask "how do I present information for quick, accurate querying"

5. **Neither dense nor sparse will "win"**: The real question is whether something even better exists beyond both paradigms.

## Replies

### @_miven (mi) — 2026-06-03T08:37:25Z
"Reminds me a lot of Epiplexity which formalizes information 'extractability' under bounded compute. Here a simple dot product just can't do enough work to leverage all the information contained in a dense vector. I think I've mentioned it to you at ECIR?"
→ 4 likes, 1 reply

### @antoine_chaffin (reply to @_miven) — 2026-06-03T08:42:13Z
"Yeah, this is definitely related! Good time to dig back into this paper, thanks for the reminder!"
→ 2 likes

### @Prithvi_Jadwani — 2026-06-03T20:53:25Z
"So you're saying IR's real goal is pre-computing queryable representations in sublinear time, not reconstructing inputs from dense vectors."
→ 0 likes (bot-like summary)

## Referenced Papers
- arxiv.org/abs/2310.06816 — Dense embeddings contain enough info to reconstruct input (jxmnop, 2023)
- arxiv.org/abs/2602.16299 — Victor Morand's work on cross-encoder recovery from pre-computed representations
- Epiplexity — formalizes information "extractability" under bounded compute (mentioned by @_miven)
