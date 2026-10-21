---
title: DeepSeek Search & Fetch APIs
created: 2026-10-21
updated: 2026-10-21
type: concept
tags: [deepseek, agentic-search, tool-use, inference-api, pricing, agents]
sources:
  - raw/articles/2026-10-18_deepseek-search-fetch-api.md
  - https://api-docs.deepseek.com/guides/search/
confidence: high
---

# DeepSeek Search & Fetch APIs

Launched October 18, 2026, **DeepSeek's Search and Fetch APIs** give agents and RAG applications access to live web content via raw JSON endpoints, powered by DeepSeek's **in-house search engine** (not a third-party aggregator). The release is notable both as a product (agentic web access at an aggressive price) and as a strategic move by a model lab into agent/tool infrastructure.

## The two APIs

| API | Endpoint | Function |
|-----|----------|----------|
| **Search** | `POST https://api.deepseek.com/v1/tools/search` | Finds web pages for a query; returns structured results (`title`, `url`, `summary`) |
| **Fetch** | `POST https://api.deepseek.com/v1/tools/fetch` | Retrieves a single web page and returns its content as **Markdown** |

Both use the same bearer authentication as the DeepSeek API (`Authorization: Bearer <key>` + `Content-Type: application/json`).

Search request fields: `query` (1–128 Unicode chars, supports query operators), `count` (result count), `need_content` (return page content/summary).

## Pricing — the headline

| API | Unit | Price |
|-----|------|-------|
| Search | Per 1,000 successful requests | **$0.75** |
| Fetch | Per 1,000 successful requests | **$0.75** |

- A request is billable only when it returns HTTP 200 *and* produces a result (non-empty `results` for Search; page content for Fetch). Failed requests, empty results, and timeouts are **not** billed. `count` does not affect per-request price.
- When the DeepSeek API is used through **DeepSeek Harness, Claude Code, or Codex**, server-side tool calls already hit Search/Fetch. These are **currently free**; per-request billing starts 00:00 Beijing time **November 1, 2026**.

## Rate limits

- Account-level QPS (regardless of which API key), separate from model concurrency limits; exceeding → HTTP 429.
- Fetch additionally has a **per-domain QPS** limit; exceeding → HTTP 429.

## Why it matters

1. **First-party search.** DeepSeek is running its own search engine to power agent/RAG tools rather than reselling SerpAPI/Brave/Tavily — control over the retrieval stack and its economics.
2. **$0.75/1k is aggressive** for agentic web access, where per-step search/fetch costs compound across long agent loops (see token-economics thinking).
3. **Tied into coding harnesses.** Making Search/Fetch free *inside* DeepSeek Harness, Claude Code, and Codex wires the tool APIs directly into agentic coding workflows — echoing the industry trend of model vendors internalizing tool providers (search, fetch, browser) as first-party capabilities.

## Related

- [[concepts/agentic-search]] — search as an agentic capability
- [[concepts/agentic-retrieval]] — retrieval inside agent loops
- [[concepts/retrieval-augmented-generation]] — RAG, a primary consumer of Search/Fetch
- [[concepts/tool-use-necessity]] — why agents need external tools like search/fetch
- [[concepts/token-economics]] — compounding cost of per-step tool calls
- [[entities/deepseek]] — the lab behind the APIs
- [[concepts/mcp]] — the protocol alternative for exposing such tools to agents
