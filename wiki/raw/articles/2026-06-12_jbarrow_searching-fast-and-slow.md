---
title: "Searching, Fast and Slow"
author: "@jbarrowai"
date: 2026-06-12
url: https://jbarrow.ai/2026-06-12-searching-fast-and-slow/
source: X Article (@jbarrowai)
source_fallback: false
tags: [slow-search, agentic-retrieval, information-retrieval, latency]
---

# Searching, Fast and Slow — Revisiting "Slow Search" in the Age of Agentic Retrieval

**Author**: Josh Barrow (@jbarrowai)
**Date**: June 12, 2026
**Source**: X Article (https://x.com/i/article/2065421433048625152)
**Also available**: https://jbarrow.ai/field_notes/slow-search/

## TL;DR

Are you willing to wait even longer for better search results? Maybe not. But an agent is, and that can actually speed up agentic search. Some recent results show that doing so can actually reduce the time taken to finish the whole task.

## Two Competing Philosophies for Agentic Retrieval

1. **Latency doesn't matter** in agentic search because the user is already willing to wait, and the models themselves don't care about latency
2. **Agents are more sensitive to latency and scalability issues** because they will issue far more queries than humans ever could

The resolution: (1) is correct for **per-query latency**, and (2) is right for **throughput and "whole task time"**.

## The Slow Search Paper (2013)

The 2013 "Slow Search" paper (Teevan et al.) posed: what would search look like if we didn't care about latency, and under what circumstances would users accept that?

Notably, they proposed **search agents** as an example of slow search — answering queries "in the background as [searchers] engage in other tasks, search-related or otherwise."

## Agentic Retrieval Evidence

- **Reason-ModernColBERT** (Antoine Chaffin, LightOn AI): Better retrieval is a rising tide that lifts all boats (model sizes). On BrowseComp-Plus, improved retrieval directly helps all model sizes.
- **Direct Corpus Interaction (DCI)** paper: Gave an agent access to grep and bash. Similar performance increase, but with more than double the tool calls and double the cost.

For agentic retrieval, both time and cost are primarily driven by the LLM itself. Every tool call means paying cached input cost and waiting for generation time. So you can end up waiting longer with lower-latency search.

## Test-Time Compute in Retrieval

There is a Pareto frontier of retrieval quality depending on how much time/compute you're willing to spend per query. Moving to better (larger) models and further up the frontier (multivector, two-stage retrievers with LLM rerankers) trades latency for quality.

## Trading Query Latency for Throughput

Hornet.dev (@HornetDev, run by @jobergum) is betting that retrieval engines designed for agents should be focused on **throughput** rather than latency. Core bet: "agents issue more queries than humans and aren't as latency sensitive."

## We Should Do More Slow Search Research

Original Slow Search paper finding: only 25.5% of participants could imagine waiting for better results. This drove relentless focus on search latency in the IR community.

But **agents are the perfect slow searchers** — infinitely patient, and cheaper/better to run if you can give them better results.

Reference to Ben Clavie's X thread arguing the IR community focuses too strongly on engineering/scalability and not enough on novel ideas.

## References

1. Antoine Chaffin (2025). Reason-ModernColBERT. https://huggingface.co/lightonai/Reason-ModernColBERT
2. Teevan, Collins-Thompson, White, Dumais, Kim (2013). Slow search: Information retrieval without time constraints. Proc. Symposium on HCI and IR.
3. Li et al. (2026). Beyond semantic similarity: Rethinking retrieval for agentic search via direct corpus interaction. arXiv:2605.05242.
4. Ben Clavie X thread: https://x.com/bclavie/status/2062151045346984032
5. Obliq-Bench: https://jbarrow.ai/field_notes/obliq-bench/
