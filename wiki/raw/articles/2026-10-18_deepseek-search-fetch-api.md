---
title: "DeepSeek Search & Fetch APIs — web tools for agents/RAG"
url: https://api-docs.deepseek.com/guides/search/
source: api-docs.deepseek.com
date: 2026-10-18
fetched_at: 2026-10-21
type: raw-article
tags: [deepseek, agentic-search, tool-use, inference-api, pricing, agents]
confidence: high
---

# DeepSeek Search & Fetch APIs (Oct 18 2026)

Source: https://api-docs.deepseek.com/guides/search/
HN: 602 pts, 280 comments (Oct 18 2026)

## Summary
The Search API and the Fetch API give agents and RAG applications access to live web content:
- **Search API** finds web pages for a query and returns structured results. It is powered by DeepSeek's **in-house search engine**.
- **Fetch API** retrieves a single web page and returns its content as **Markdown**.

Both are raw JSON APIs using the same bearer authentication as the DeepSeek API.

## Endpoints
Base URL: `https://api.deepseek.com`
- Search: `POST https://api.deepseek.com/v1/tools/search`
- Fetch: `POST https://api.deepseek.com/v1/tools/fetch`

Auth: `Authorization: Bearer <DeepSeek API Key>` + `Content-Type: application/json`.

## Search API request fields
- `query` (string, required): 1–128 Unicode chars, not all whitespace; supports query operators.
- `count` (integer): how many results to return.
- `need_content` (bool): return content/summary.
Example returns per result: `title`, `url`, `summary`.

## Billing
| API | Unit | Price |
|-----|------|-------|
| Search | Per 1,000 successful requests | $0.75 |
| Fetch  | Per 1,000 successful requests | $0.75 |

- A request is billable only when it returns HTTP 200 and produces a result (Search must return a non-empty `results` array; Fetch must return page content). Failed requests, empty search results, and timeouts are **not** billed. `count` does not affect the per-request price.
- When using the DeepSeek API through **DeepSeek Harness, Claude Code, or Codex**, server-side tool calls already hit the Search and Fetch APIs. These calls are currently **free of charge**; per-request billing starts at 00:00 Beijing time on **November 1, 2026**.

## Rate limits
- QPS limits calculated at the **account level**, regardless of which API key is used; separate from model concurrency limits. Above account-level QPS → HTTP 429.
- Fetch is additionally subject to a **per-domain QPS limit**; above that → HTTP 429.

## Significance
DeepSeek launching its own in-house web search + page-fetch tool APIs (not a third-party aggregator) is a strategic move into agent/RAG infrastructure economics. $0.75/1k requests is an aggressive price point for agentic web access, and the "currently free inside DeepSeek Harness / Claude Code / Codex" framing ties the tool APIs directly into agentic coding harnesses, echoing the broader industry trend of model vendors internalizing tool providers (search/fetch/browser) as first-party capabilities.
