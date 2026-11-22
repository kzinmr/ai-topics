---
title: "Active Crawl Research Note — 2026-11-22"
type: research-note
created: 2026-11-22
updated: 2026-11-22
sources:
  - https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens
  - https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026
  - https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers
  - https://www.noemamag.com/the-mythology-of-conscious-ai/
  - https://betterdatacenterproject.com/2026-11-16/how-ai-is-powered-a-breakdown-of-fuels-used-by-data-centers/
tags: [raw]
---

# Active Crawl Research Note — 2026-11-22

Discovery sources: blogwatcher SQLite (last 3 days, 60 articles), HN Algolia `search_by_date` (6 queries, 5-day window, points>=30), log.md same-day pipeline dedup.

## Topics processed

### 1. Dragos inference canary study (FULL gap → new page) ★★★★★
- ~2M canary-laced prompts July–Nov 2026, HD Moore / Dragos. Three provider compromises, marketplace resellers reading prompts via plain logging, ZDR violations incl. US→China flows and the Feishu-chat incident.
- Raw: `raw/articles/2026-11-19_dragos_ai-supply-chain-canary-tokens.md` (published Nov 19; HN 84pts Nov 22).
- Created: `concepts/dragos-inference-canary-study.md` (confidence: medium — single first-party source).

### 2. Zero Data Retention as a concept (FULL gap → new page) ★★★★☆
- ZDR appears in 10+ existing pages (managed-agents, fireworks breach, sglang exposure, kimi-k3, codex agent loop…) but had no concept page. Nov 2026 incidents (Dragos, Fireworks/Notion, Together) collectively define its real-world semantics: "binds at most the first hop."
- Created: `concepts/zero-data-retention.md` (synthesis page; cross-refs the three incident pages).

### 3. Together AI prompt-leak security event (already COVERED same-day by blog-ingest)
- Commit 5cbae342 (10:09 UTC) added the full Security Event section to `entities/together-ai.md`. Skipped per same-day dedup rule. Raw saved anyway for the two new pages' source lists.

### 4. Anil Seth "Mythology of Conscious AI" (PARTIAL → enriched) ★★★☆☆
- Noema essay (2025 Berggruen Prize winner, resurfacing in HN Nov 22, 72pts). `concepts/ai-consciousness-debate.md` had Hinton/Marcus/Pope but not Seth — added a full section (bias taxonomy + four anti-computational-functionalism arguments + conscious-seeming harms).

## Candidates considered & deferred
- **OpenRouter "Data Processing Incidents on Inference Providers"** (Nov 22, HN 159) — router-side response to the same ecosystem; no raw access attempted this run (JS/Cloudflare likely). Follow-up candidate: enrich `entities/openrouter.md` when scrapeable.
- **Better Data Center Project fuel breakdown** (Nov 16, HN 143: "87% of Anthropic power from gas, 11% coal by 2028") — 404 on the URL as indexed in HN; content would fit `concepts/ai-energy` / data-center pages. Deferred: find correct URL next crawl.
- **Pandex — "Official European Law for AI Agents, over MCP"** (Nov 21, HN 97) — corporate site, unclear substance vs. marketing; needs verification before page creation.
- **Token fraud (Simon Willison video, Nov 20)** — raw saved by blog-ingest; no standalone page yet, content volume thin for thresholds. Watch.
- **Nasdaq AI sell-off / Anthropic IPO bust** (HN 512/198/66) — covered by existing `events/anthropic-ipo-roadshow-2026.md` + prior hot-post logs; day-2 selloff details are paywalled (WSJ/Guardian).
- **llms.txt and MCP didn't move the needle** (Nov 20, HN 31) — opinion piece from a vendor blog; low durable value.
