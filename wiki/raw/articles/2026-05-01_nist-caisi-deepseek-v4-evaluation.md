---
title: "CAISI Evaluation of DeepSeek V4 Pro"
url: "https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro"
fetched_at: 2026-05-03T12:00:00+00:00
source: "NIST"
tags: [blog, raw]
---

# CAISI Evaluation of DeepSeek V4 Pro

Source: https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro

## Key Findings (May 1, 2026)

- DeepSeek V4 Pro is the most capable PRC model to date
- **Capability gap:** Lags behind the US frontier by approximately **8 months** based on IRT analysis
- Self-reported benchmarks (where DeepSeek claims parity with GPT-5.4) are likely contaminated — CAISI's private benchmarks reveal true gap
- V4 is competitive in **mathematics** (OTIS-AIME-2025: 97%) but drops significantly in:
  - **Abstract reasoning** (ARC-AGI-2 private: 46% vs GPT-5.5 xhigh 79%)
  - **Cybersecurity** (CTF-Archive-Diamond: 32% vs GPT-5.5 xhigh 71%)
  - **Software engineering** (PortBench private: 44% vs GPT-5.5 xhigh 78%)

## Cost Efficiency

- V4 is more cost-efficient than GPT-5.4 mini on 5/7 benchmarks
- Up to **53% less expensive** on certain benchmarks
- V4 Pro: $1.74/1M input, $3.48/1M output (vs GPT-5.4 mini: $0.75/$4.50)
- V4 cached input: $0.0145/1M (95.5% cheaper than GPT-5.4 mini cached)

## Methodology

- IRT (1PL variant) for capability measurement
- Non-public benchmarks: PortBench (port CLI tools between languages), CTF-Archive-Diamond (285 challenges from pwn.college)
- Served on H200 and B200 GPUs with developer-recommended settings
