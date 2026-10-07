---
title: "OpenAI DevDay 2026"
created: 2026-10-07
updated: 2026-10-07
type: event
tags: [openai, event, announcement, api, ai-agents]
sources:
  - raw/articles/simonwillison.net--2026-sep-29-openai-devday-2026-live-blog--e0ba6a4a.md
  - raw/inbox/newsletter-ingest/20261001T101035Z-triage.json
  - https://developers.openai.com/api/docs/changelog
  - https://developers.openai.com/api/docs/guides/agents-api/overview
  - https://developers.openai.com/api/docs/guides/decisions
date: 2026-09-29
---

# OpenAI DevDay 2026

## Scope and evidence

DevDay took place on September 29, 2026, as recorded in Simon Willison's saved live blog. This page covers the agent/API announcements; it is not an exhaustive launch catalog. The October 1 newsletter triage marked coverage critical and requested this event plus two distinct canonical concepts. Newsletter priority is an editorial signal, not specification evidence.

## API announcements and later changes

| Surface | DevDay context | Status verified on October 7 |
|---|---|---|
| [[concepts/openai/agents-api]] | Live blog at 10:31 reports Computer Use | Official changelog dates public beta to September 10 and Computer Use to September 29; DevDay was not the API's initial launch |
| [[concepts/openai/decisions-api]] | Live blog at 10:25 describes a Luna preview selecting predefined options with low latency | October 6 changelog records beta release; current guide calls it public beta |
| [[concepts/openai/agents-sdk]] | Existing open-source framework, a separate product | Application-owned harness; not an alias for Agents API |
| [[concepts/openai/responses-api]] | Existing model/tool API, useful comparison baseline | Direct model requests rather than the managed Codex session surface |

The live blog also records GPT-6.1 Sol, Ultrafast, Dots, Codex Cloud/Security, and collaboration/plugin announcements. These are historical reporting here; their availability and detailed specifications require separate primary-source checks.

## Reading boundaries

Preserve the Decisions preview description as historical evidence, superseded for current availability by the October 6 beta release. Do not backdate today's request schema to DevDay. Likewise, the live blog's question about whether Agents API was new is resolved by the earlier official release date, not copied as a launch claim.

The newsletter raw digests are link inventories rather than complete API documentation. The saved live blog is eyewitness secondary evidence; current OpenAI docs establish current API behavior. Neither establishes measured end-to-end latency for a particular workload, guaranteed recovery semantics, or customer-specific permissions.

## Sources

- [Saved live blog](../raw/articles/simonwillison.net--2026-sep-29-openai-devday-2026-live-blog--e0ba6a4a.md) — event chronology and preview wording.
- [October 1 triage](../raw/inbox/newsletter-ingest/20261001T101035Z-triage.json) — ingest priority and missing-coverage request.
- [Official changelog](https://developers.openai.com/api/docs/changelog) — dated release history, checked 2026-10-07.
- [Agents API overview](https://developers.openai.com/api/docs/guides/agents-api/overview) and [Decisions guide](https://developers.openai.com/api/docs/guides/decisions) — current coverage, checked 2026-10-07.
