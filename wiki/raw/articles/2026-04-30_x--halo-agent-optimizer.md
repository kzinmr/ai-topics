---
title: "We’re introducing HALO 😇

Hierarchal Agent Loop Optimizer

HALO is an RLM-based ..."
source: "https://x.com/i/status/2049619541727302040"
date: 2026-04-30
type: x_tweet
tweet_id: "2049619541727302040"
author: "Sam Hogan"
---

We’re introducing HALO 😇

Hierarchal Agent Loop Optimizer

HALO is an RLM-based agent optimization technique capable of recursively self-improving agents by analyzing their execution traces and suggesting changes. 

This work is inspired by the Mismanaged Genius Hypothesis proposed by @a1zhang  and @lateinteraction earlier this month.

tldr; we improved performance on AppWorld (Sonnet 4.6) from 73.7 --> 89.5 (+15.8) by giving HALO-RLM access to harness trace data and asking it to identify issues. 

The feedback from HALO surfaced failures in the harness such as hallucinated tool calls, redundant arguments in tools, refusal loops, and semantic correctness issues. Each issue mapped cleanly to a direct prompt update.
 
We then fed these finding into Cursor (Opus 4.6), and asked the coding agent to update the underlying harness.
 
We repeated this trace -> HALO-RLM analysis -> code update loop until the score plateaued.

Today we’re open-sourcing the core HALO-RLM framework, evals, and data for further review.
