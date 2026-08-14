---
title: danlark-org
description: Daniel Kutenin (danlark) — search infrastructure engineer (ex-Yandex, Google); C++ performance, algorithms, and large-scale systems blog
url: https://danlark.org
type: entity
created: 2026-08-14
updated: 2026-08-14
aliases:
  - Daniel Kutenin
  - danlark
tags:
  - person
  - blogger
  - search
  - cpp
  - performance
  - infrastructure
  - developer-tooling
sources:
  - https://danlark.org/
  - https://danlark.org/feed/
  - raw/articles/danlark.org--2020-07-31-news-aggregator-from-scratch-in-2-weeks--d0a26858.md
---

# Daniel Kutenin (danlark)

**Daniel Kutenin** (blog: danlark.org, handle `danlark`) is a search infrastructure engineer who writes deep technical posts about C++ performance, algorithms, and large-scale systems engineering. His blog is one of the higher-signal sources in the C++/search-engine corner of the web: instead of tutorials, he publishes post-mortems of real production problems (Google-scale `std::sort`, hugepage-aware allocators, a Linux kernel CRC-32 bug) and detailed write-ups of engineering competitions he enters.

## Overview

Kutenin has spent his career working on search engines and core infrastructure: the blog's earliest archived posts describe him as having "been working on the search engine for quite some time", he references "my Yandex ex-colleagues" (in the news-aggregator write-up), and his 2022 post "Changing std::sort at Google's Scale and Beyond" documents work inside Google's C++ libraries team. His writing combines hard-won production experience with competitive-programming instincts — he competes in engineering contests (Google HashCode, Telegram's Data Clustering Contest) and reports exact numbers, trade-offs, and bugs he made along the way.

## Core Topics

### C++ Performance Engineering
- **"Changing std::sort at Google's Scale and Beyond"** (April 2022) — Replacing `std::sort` in Google's codebase: the selection of pdqsort-based approaches, benchmark methodology at fleet scale, and the political/engineering process of changing a function every C++ developer calls.
- **"I need extra C/C++ performance now. How?"** (October 2020) — A practical guide to profiling and squeezing performance out of C/C++ code.
- **"128-bit division"** (June 2020) — Implementing and optimizing 128-bit integer division, a problem that appears in compiler/runtime work.
- **"Why is std::pair broken?"** (April 2020) — A critique of a core C++ standard library type and its layout/ABI issues.
- **"miniselect: practical and generic selection algorithms"** (November 2020) — Open-source library of fast selection algorithms (quickselect variants) with generic C++ interfaces.
- **"CSINC: the ARM instruction you didn't know you wanted"** (June 2023) — A deep dive into an ARM conditional-select instruction and its performance implications.

### Memory & Systems Infrastructure
- **"Beyond malloc efficiency to fleet efficiency: a hugepage-aware memory allocator"** (June 2021) — TCMalloc's hugepage-aware allocator design: why fleet-level efficiency beats single-process malloc metrics, and how hugepages change allocation strategy.
- **"How a bug in the Linux CRC-32 checksum turned out..."** (March 2021) — A production debugging story tracing a subtle checksum bug through the Linux kernel.

### Engineering Competitions
- **"How to crack HashCode competition with some engineering skills"** (March 2020) — Google HashCode write-up emphasizing systems engineering over pure algorithms.
- **"News Aggregator from Scratch in 2 Weeks"** (July 2020) — Telegram's Data Clustering Contest; see the dedicated section below.

## News Aggregator from Scratch in 2 Weeks (July 2020)

Kutenin's write-up of **Telegram's Data Clustering Contest** (May 2020) — a two-week competition to build a Google News-style aggregator: detect article language, separate news from non-news, classify categories, cluster similar articles into threads, and serve ranked queries in real time. He placed **3rd (7,000 EUR)** under the nickname *Mindful Kitten*. The full application was written in **C++17** (training in Python) and is a tour of fast text/ML infrastructure:

- **HTML parsing**: Patched **Google's Gumbo parser** (libxml2 was ~3x slower) to handle Telegram Instant View HTML's non-standard self-closing `<iframe>` tags — a one-line change that fixed broken text extraction. Perf work on inlining brought parsing to ~0.4ms/article/thread, ~16-18k articles/sec.
- **Language detection**: Evaluated CLD3 vs **CLD2** (a Naive Bayes quadgram classifier); CLD2 was 7.5x faster with comparable accuracy (0.03% difference on his test set). Solved ISO-639-1 code drift (`iw→he`, `jw→jv`, `in→id`, `mo→ro`) with a static known-language table. Crowdsourced validation via Yandex.Toloka showed **99.35% precision/recall** for English/Russian.
- **News filtering & topic classification**: Combined into one **fastText** classifier trained on ~50k labeled articles (Toloka + Amazon Mechanical Turk labels, extended with Ria.ru/Lenta.ru/BBC/HuffPost Kaggle datasets). Rebuilt without `-march=native` (AVX-512) after realizing Telegram's datacenter CPUs might lack the extensions — settled on SSE4.2, sacrificing at most 2-3% speed.
- **Thread clustering**: Re-trained embeddings with a **Siamese network + triplet loss** (adapting the 1st-place "Mindful Squirrel" team's approach), then clustered with the **SLINK** hierarchical algorithm over a time-sliding window (15k docs, 3k overlap) to bound complexity. Ranking inside threads combined PageRank-style weights with recency (sigmoid of most-recent time + mean similarity).
- **Dynamic server**: protobuf-serialized sharded document store (power-of-two-choices random shard selection for near-lock-free load balancing), **HNSW** (online-hnsw library) for k-NN thread lookup — combining all neighbors found under a similarity threshold to reproduce SLINK transitivity — read-prioritized RW-locks, and precomputed top-thread responses for sub-100ms queries. He notes Google's **scANN** was published right after the contest and believes its SIMD design makes it 20-30% faster than HNSW.

The post is a canonical example of engineering-leveraged ML: minimal model complexity (fastText + CLD2 + HNSW) with maximum systems attention (parsing speed, lock-free data structures, sharding, consistency under deletion). Relevant to HNSW/ANN-style vector-search thinking and text-pipeline infrastructure.

## Writing Style & Philosophy

- **Numbers over narrative**: Every claim is backed by measured figures (tasks/sec, ms/article, precision/recall, speedup factors).
- **Honest failure reporting**: He documents the bugs he shipped (a full similarity-matrix recalculation that degraded the server after 8-9 days uptime, a cluster-size restriction that only worked for single-document merges) rather than polishing the result.
- **Systems-first ML**: His default is to make infrastructure fast and keep models simple — explicitly describing himself as "not a Machine Learning engineer" while winning ML-adjacent competitions through engineering.
- **Competition as forcing function**: He observes he performs best under deadlines and competition, and his contest write-ups are among his richest posts.

## Cross-References

- **[[entities/paulgraham-com]]** — Another independent technical blogger whose essays are cataloged in this wiki; different domain (startup essays vs C++/systems).
- **[[entities/miguel-grinberg]]** — Python-focused educator/blogger counterpart in the wiki's tracked-blog set; both write long-form, empirically grounded technical posts.
- **vector-search / ANN infrastructure** — The HNSW section of the news-aggregator post connects to the wiki's vector-search coverage (ANN benchmarks, similarity search infra).

## References

- `raw/articles/danlark.org--2020-03-13-how-to-crack-hashcode-competition-with-some-engin--c1db4491.md`
- `raw/articles/danlark.org--2020-04-13-why-is-stdpair-broken--15d43901.md`
- `raw/articles/danlark.org--2020-06-14-128-bit-division--4864392f.md`
- `raw/articles/danlark.org--2020-07-31-news-aggregator-from-scratch-in-2-weeks--d0a26858.md`
- `raw/articles/danlark.org--2020-10-08-i-need-extra-c-c-performance-now-how--37083b9d.md`
- `raw/articles/danlark.org--2020-11-11-miniselect-practical-and-generic-selection-algori--b035556f.md`
- `raw/articles/danlark.org--2021-03-08-how-a-bug-in-the-linux-crc-32-checksum-turned-out--ea9eabe9.md`
- `raw/articles/danlark.org--2021-06-11-beyond-malloc-efficiency-to-fleet-efficiency-a-hu--48b71959.md`
- `raw/articles/danlark.org--2022-04-20-changing-stdsort-at-googles-scale-and-beyond--07028621.md`
- `raw/articles/danlark.org--2023-06-06-csinc-the-arm-instruction-you-didnt-know-you-want--d109ea24.md`
