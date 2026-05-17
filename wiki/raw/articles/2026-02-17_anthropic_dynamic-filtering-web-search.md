---
title: "Improved Web Search with Dynamic Filtering"
source: "https://claude.com/blog/improved-web-search-with-dynamic-filtering"
authors:
  - Anthropic
date: 2026-02-17
updated: 2026-05-17
publication: "Anthropic Blog"
category: "Product announcements"
product: "Claude Platform"
tags:
  - web-search
  - code-execution
  - dynamic-filtering
  - tool-use
---

# Improved Web Search with Dynamic Filtering

**Source:** https://claude.com/blog/improved-web-search-with-dynamic-filtering
**Date:** February 17, 2026
**Reading time:** 5 min

Alongside Claude Opus 4.6 and Sonnet 4.6, Anthropic released new versions of the web search and web fetch tools. Claude can now natively write and execute code during web searches to filter results before they reach the context window, improving accuracy and token efficiency.

## Web Search with Dynamic Filtering

Web search is a highly token-intensive task. Agents using basic web search tools need to make a query, pull search results into context, fetch full HTML files from multiple websites, and reason over it all before responding. But the context being pulled in from search is often irrelevant, which degrades the quality of the response.

To improve Claude's performance on web searches, the web search and web fetch tools now automatically write and execute code to post-process query results. Instead of reasoning over full HTML files, Claude can dynamically filter the search results before loading them into context, keeping only what's relevant and discarding the rest.

Anthropic had previously found this technique to be effective across other agentic workflows, and had added tools such as code execution and programmatic tool calling for native support on the API. These same techniques are now brought to web search and web fetch.

## Evaluating Claude's Ability to Search the Web

Web search was evaluated on Sonnet 4.6 and Opus 4.6 with and without dynamic filtering and no other tools enabled. Across two benchmarks, BrowseComp and DeepsearchQA, dynamic filtering improved performance by an average of **11%** while using **24% fewer input tokens**.

### BrowseComp: Searching the Web to Find One Answer

BrowseComp tests whether an agent can navigate many websites to find a specific piece of information that is deliberately hard to find online. Dynamic filtering improved Claude's accuracy significantly:

| Model | Without Dynamic Filtering | With Dynamic Filtering |
|-------|--------------------------|------------------------|
| Sonnet 4.6 | 33.3% | **46.6%** |
| Opus 4.6 | 45.3% | **61.6%** |

### DeepsearchQA: Searching the Web to Find Many Answers

DeepsearchQA presents agents with research queries that have many correct answers, all of which must be found via web search. It tests whether an agent can systematically plan and execute multi-step searches without missing any answers. Measured by F1 score (balancing precision and recall):

| Model | Without Dynamic Filtering | With Dynamic Filtering |
|-------|--------------------------|------------------------|
| Sonnet 4.6 | 52.6% | **59.4%** |
| Opus 4.6 | 69.8% | **77.3%** |

Token costs will vary depending on how much code the model needs to write to filter context. Price-weighted tokens decreased for Sonnet 4.6 on both benchmarks but increased for Opus 4.6.

## Customer Spotlight: Quora (Poe)

Poe by Quora is one of the largest multi-model AI platforms, giving millions of users access to over 200 models through a single interface. Internal teams at Quora found that Opus 4.6 with dynamic filtering "achieved the highest accuracy on our internal evals when tested against other frontier models," said Gareth Jones, Product and Research Lead.

> "The model behaves like an actual researcher, writing Python to parse, filter, and cross-reference results rather than reasoning over raw HTML in context."

## API Usage

Dynamic filtering is turned on by default when using the new web search and web fetch tools with Sonnet 4.6 and Opus 4.6 on the Claude API.

```json
{
  "model": "claude-opus-4-6",
  "max_tokens": 4096,
  "tools": [
    {
      "type": "web_search_20260209",
      "name": "web_search"
    },
    {
      "type": "web_fetch_20260209",
      "name": "web_fetch"
    }
  ],
  "messages": [
    {
      "role": "user",
      "content": "Search for the current prices of AAPL and GOOGL, then calculate which has a better P/E ratio."
    }
  ]
}
```

**Requirements:**
- Models: Opus 4.6, Sonnet 4.6
- Tool versions: `web_search_20260209` or `web_fetch_20260209`
- Beta header: `anthropic-beta: code-execution-web-tools-2026-02-09`
- Code Execution tool must be enabled (free when used with web tools; standard token costs apply)

## Tools Graduating to General Availability

Alongside dynamic filtering, several tools graduated to GA:

- **Code Execution**: Provides a sandbox for agents to run code during a conversation to filter context, analyze data, or perform calculations
- **Memory**: Store and retrieve information across conversations through a persistent file directory, so agents can retain context without keeping everything in the context window
- **Programmatic Tool Calling**: Execute complex multi-tool workflows in code, keeping intermediate results out of the context window
- **Tool Search**: Dynamically discover tools from large libraries without loading all definitions into the context window
- **Tool Use Examples**: Provide sample tool calls directly in your tool definitions to demonstrate usage patterns and reduce parameter errors
