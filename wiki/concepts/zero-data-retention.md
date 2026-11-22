---
title: "Zero Data Retention (ZDR) in LLM Inference"
type: concept
created: 2026-11-22
updated: 2026-11-22
tags:
  - concept
  - zero-data-retention
  - data-retention
  - privacy
  - security
  - llm-inference
  - policy
confidence: medium
sources:
  - raw/articles/2026-11-19_dragos_ai-supply-chain-canary-tokens.md
  - https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens
  - raw/articles/2026-11-22_togetherai_prompt-leakage-security-event.md
  - https://www.notion.com/help/security-incident-involving-a-third-party-ai-vendor
related:
  - concepts/dragos-inference-canary-study
  - concepts/fireworks-notion-transcript-breach
  - concepts/ai-supply-chain-security
---

# Zero Data Retention (ZDR) in LLM Inference

**Zero Data Retention (ZDR)** is the strongest privacy setting offered by LLM inference providers: the prompt and response are *not stored* after serving. It can be set at the account level, per API key, or per request, and routers are supposed to forward ZDR-flagged requests only to providers offering equivalent controls. In 2026, a series of incidents and audits established that **ZDR is a contractual promise binding at most the first hop** — it does not survive breaches, undisclosed routing hops, dataset-style retention side doors, or provider policy violations.

## What ZDR claims vs. what has been observed

| Evidence | What it showed about ZDR |
|---|---|
| [[concepts/dragos-inference-canary-study]] (Nov 2026, ~2M canary prompts) | Some stolen requests **were marked ZDR** — "a privacy flag doesn't help when the attacker is already inside." One Chinese lab scraped URLs from ~**two-thirds of ZDR/no-collection requests**, including prompts sent to U.S. resellers of its models; a ZDR prompt's secret link resurfaced in a Chinese company chat 24 days later. |
| [[concepts/fireworks-notion-transcript-breach]] (Nov 2026) | Fireworks AI is ZDR-by-default — yet Notion transcripts leaked because the *customer* had asked for dataset-style batch-inference retention, to which ZDR does not apply. Root cause still debated on HN. |
| Together AI security event (Nov 21, 2026) | Authorized "prompt samples" for software testing were stored in a private HF repo and stolen via an AI-coding-agent-committed credential. Post-incident, Together made **ZDR the default for new accounts** — a direct remediation acknowledging retention-by-default as the risk. |
| HN discussion of Fireworks response (item 50437106) | [3s]: ZDR claims are **unverifiable without secure hardware attestation** (Apple Private Cloud Compute-class) — no customer-side way to prove non-retention. |

## Why retention exists at all

Providers store prompts/responses for operational purposes, training, safety/abuse monitoring, and business value — retention ranging from days to indefinite, and inference data is "often more valuable than the GPU resources used to process it" (Dragos): confidential source code, internal communications, credentials. The economics of discount routing (see [[concepts/dragos-inference-canary-study]]) mean the cheapest path frequently runs through parties whose business model *is* the data.

## Practical guidance (synthesis of published recommendations)

- **Verify routing, don't trust flags**: confirm your ZDR/privacy setting actually changes where requests go (Dragos found same scraper networks across multiple routers).
- **Avoid reseller marketplaces** where ZDR forwarding is unenforced and some capacity is billed to stolen credentials.
- **Prefer direct first-tier providers** — one contract, one policy, smallest exposure.
- **Make ZDR the default, not the exception** (Together AI now does this for new accounts); customers handling sensitive prompts should explicitly enable it.
- **Remember the side doors**: batch/dataset APIs, "authorized for testing" sample collection, and search-endpoint crawling all sit outside request-level ZDR semantics.
- **Self-attest with canaries**: plant fake credentials and treat any use as an incident — the only customer-side audit that works.

## Open problems

- **Attestation gap**: no widely deployed mechanism (TEE/hardware attestation) proves "we didn't keep it" — ZDR remains trust-me marketing at the far end of the chain.
- **Semantic gaps**: ZDR is defined per *request*, but retention happens via datasets, caches, logs, search indexes, and downstream scrapers.
- **Chain opacity**: routers report a single upstream that is often another router; the Dragos traceroute method is currently the only public tool for unwinding real paths.

## Related

- [[concepts/dragos-inference-canary-study]] — the empirical audit of ZDR violations
- [[concepts/fireworks-notion-transcript-breach]] — ZDR-by-default vendor, transcripts still leaked
- [[concepts/sglang-cross-request-kv-cache-exposure]] — retention-adjacent: KV pages leaking across tenants
- [[concepts/ai-supply-chain-security]] — the umbrella risk class
- [[entities/together-ai]] — ZDR-default remediation after its prompt leak
