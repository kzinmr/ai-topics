---
title: "Dynamic Filtering in Claude Web Search: Faster, Cheaper"
source: "https://www.gend.co/blog/claude-web-search-dynamic-filtering"
authors:
  - GEND (Anthropic partner)
date: 2026-03-30
---

# Dynamic Filtering in Claude Web Search: Faster, Cheaper

**Source:** https://www.gend.co/blog/claude-web-search-dynamic-filtering
**Date:** March 30, 2026

## Core Innovation

Anthropic introduced a mechanism where Claude writes and executes code to pre-process web results *before* they enter the context window, significantly reducing noise and cost. This is "filter-before-reasoning" — the model generates extraction scripts (e.g., for pricing tables, specific headings) that run in a sandboxed environment.

## Key Metrics

- **Search accuracy**: ~11% improvement on average
- **Token efficiency**: ~24% fewer input tokens
- **DeepsearchQA F1**: Sonnet 4.6 52.6% → 59.4%, Opus 4.6 69.8% → 77.3%

## How It Works

1. **Search/Fetch**: Claude initiates web search or fetches URL
2. **Script Generation**: Claude generates a small script to extract specific relevant data
3. **Sandboxed Execution**: The script runs in a sandbox to clean the data
4. **Context Loading**: Only filtered, high-relevance output enters context window

## API Requirements

- **Models**: Opus 4.6, Sonnet 4.6
- **Tool versions**: `web_search_20260209` or `web_fetch_20260209`
- **Beta header**: `anthropic-beta: code-execution-web-tools-2026-02-09`
- **Code Execution tool**: Must be enabled
- **Cost**: Code execution is free when used with web tools (standard token costs apply)

## Use Cases

- Technical documentation extraction
- Competitive intelligence (pricing tiers)
- Literature reviews
- Multi-step research (prevents context bloat)
