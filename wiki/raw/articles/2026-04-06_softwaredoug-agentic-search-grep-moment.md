---
title: "Agentic Search Is Having a Grep Moment / Is grep all you need for RAG?"
source: "https://softwaredoug.com/blog/2026/04/06/agentic-search-is-having-a-grep-moment"
authors:
  - Doug Turnbull
  - softwaredoug.com
date: 2026-04-06
---

# Is grep all you need for RAG?

**Source:** https://softwaredoug.com/blog/2026/04/06/agentic-search-is-having-a-grep-moment
**Author:** Doug Turnbull
**Date:** April 6, 2026

## The "Grep Moment"

Agents are moving toward filesystems as their primary interface. Instead of complex vector databases, agents use standard CLI tools: `grep`, `cat`, `ls`, and `find`. Frontier LLMs are heavily trained on code navigation — `grep` is a "happy path" they already understand.

> "RAG is great, until it isn't. Agents are converging on filesystems as their primary interface because `grep`, `cat`, `ls`, and `find` are all an agent needs." — Mintlify

## The Two-Loop Architecture

1. **Inner Loop (The Agent)**: LLM iterates through tool calls until satisfied
2. **Outer Loop (The Harness/Hooks)**: Programmatic validation (rerankers, LLM-as-a-judge, metadata checks). If results don't meet quality bar, harness tells agent to "try harder."

## Limits of Grep

1. **Actionable Feedback**: If search tool can't prioritize relevance, "try harder" won't help
2. **Complexity**: Modern retrieval balances recency, popularity, embeddings, lexical — hard to model in flat markdown
3. **Token Cost**: Many tool calls to compensate for dumb search is expensive

**Verdict**: While grep is having a moment, high-quality retrieval still matters. The most appropriate tool is a well-tuned `search` function.
