---
title: "Kimi K3 on AMD MI355X — 952 tok/s Serving Benchmark"
source: "X/Twitter — @wafer_ai"
url: "https://x.com/wafer_ai/status/2083628389903315406"
date: 2026-08-01
created: 2026-08-04
type: raw
tags: [kimi-k3, amd-mi355x, serving-benchmark, inference]
---

# Kimi K3 on AMD MI355X — 952 tok/s Serving Benchmark

**Source**: [@wafer_ai](https://x.com/wafer_ai/status/2083628389903315406), August 1, 2026

**Engagement**: 457 bookmarks, 885 likes, 430K impressions, 82 retweets, 28 quotes

## Original Tweet

> 🚨 BREAKING:
>
> these engineers figured out how to serve Kimi K3 on @AMD MI355X at 952 tok/s/node and 118 tok/s single stream!
>
> this crushes B200 by 3.8x in aggregate throughput/node and 1.3x in single stream decode + beats B300 on performance per dollar (48 vs 33 tok/s/$)
>
> See how [image]

## Bookmark Commentary

The bookmarker (@unknown) added context that Kimi K3 is so massive that it needs 16x B200s across two NVIDIA servers, but fits inside one 8x MI355X AMD server because AMD gives you much more HBM memory per GPU (288 GB HBM3e on MI355X vs 192 GB HBM3 on B200).

## Key Metrics

| Metric | AMD MI355X (8-GPU) | NVIDIA B200 (16-GPU) | Advantage |
|--------|-------------------|---------------------|-----------|
| **Node count** | 1 node | 2 nodes | MI355X: single-node serving |
| **Aggregate throughput** | 952 tok/s | ~250 tok/s (est.) | MI355X: **3.8x** |
| **Single-stream decode** | 118 tok/s | ~91 tok/s (est.) | MI355X: **1.3x** |
| **Perf/$ vs B300** | 48 tok/s/$ | 33 tok/s/$ | MI355X: **1.45x** |

## Context

This result is enabled by MI355X's 288 GB HBM3e per GPU, which allows the full Kimi K3 model (2.8T MoE, ~1.5 TB weights) to fit in a single 8-GPU node (8 × 288 = 2,304 GB total) vs requiring 16 × 192 = 3,072 GB across two B200 nodes. The single-node deployment eliminates inter-node communication overhead, contributing to the throughput advantage.

**Wafer** (@wafer_ai) is a model serving platform that routes and optimizes open models across NVIDIA, AMD, TPUs, and beyond.
