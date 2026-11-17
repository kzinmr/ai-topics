---
title: "Prefer synthetic traffic over LLM-as-a-judge"
source_url: https://softwaredoug.com/blog/2026-11-12/agent-search-traffic
author: Doug Turnbull (@softwaredoug)
published: 2026-11-12
captured: 2026-11-17
captured_by: x-accounts-scan
type: raw-article
status: partial — full text unavailable, metadata + tweet only
---

# Prefer synthetic traffic over LLM-as-a-judge

**Doug Turnbull**, softwaredoug.com, published 2026-11-12.
Canonical URL (as listed in the site's own RSS `feed.xml`):
`http://softwaredoug.com/blog/2026-11-12/agent-search-traffic.html`
Tweet URL form: `https://softwaredoug.com/blog/2026-11-12/agent-search-traffic`

## ⚠️ Capture status — read before citing

The article body could **not** be retrieved on 2026-11-17. Attempts made: direct curl
(Chrome UA, Googlebot UA, Referer variants), `https` and `http`, `.html` and extensionless
and trailing-slash forms, the site's blog index, `sitemap.xml` (serves the 404 page), and
r.jina.ai — all returned softwaredoug.com's 14 KB Pelican 404 page (ASCII-art "404",
`og:url` = `/404.html`). Wayback has no snapshot. The post is confirmed to exist only via
the site's own RSS feed (`https://softwaredoug.com/feed.xml`), which lists it as the
newest item with title, pubDate, and link but a one-line description. **Do not treat any
claim below as a quotation from the article body.** A future run should retry the fetch.

## What is verified (from RSS + the author's own tweet)

RSS description (verbatim, the only article text obtained):

> "We don't need to stay married to an old model of evaluation that silos the UI from
> ranking"

Author's announcement tweet (2026-11-16 16:31 UTC,
https://x.com/softwaredoug/status/2122367009761497352):

> "My search consulting moved away from LLM judges. Now I: * Vibecode a facsimile of my
> clients application * Let agents act as users to use the app to solve search use-cases
> When using agent evals, I stay in the lane of sessions, clicks, etc - not NDCG"

## Reading of the thesis (from the two verified fragments)

Turnbull reports that his search consulting practice has **abandoned LLM-as-a-judge
relevance scoring** in favour of **synthetic agent traffic**:

1. **Vibecode a facsimile** of the client's actual application (a working stand-in UI,
   not a ranking harness).
2. **Let agents act as users**, driving that app to complete real search use-cases.
3. **Measure session-level behavioural signals** — sessions, clicks, and similar
   interaction telemetry — rather than offline ranking metrics such as NDCG.

The argument against the status quo, in his own one-line framing, is that the classic
evaluation model **silos the UI from ranking**, and that teams don't need to stay married
to it. This is a continuation of positions already on file for Turnbull: relevance
judgments reconstructed from A/B test behaviour
(`blog/2022-06-08/deriving-relevance-judgments-from-an-a-b-test`), "Search golden sets
are anything but" (Oct 26 2026), and his standing "Grug-brained evals" line favouring
cheap human/behavioural labels over elaborate quality metrics.

## Related wiki pages

- [[entities/doug-turnbull]] / [[entities/softwaredoug]]
- [[concepts/llm-evaluation]], [[concepts/evaluation/ndcg]]
- [[concepts/agentic-retrieval]]
