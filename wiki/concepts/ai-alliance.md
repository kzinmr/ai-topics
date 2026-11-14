---
title: "AI Alliance"
type: concept
aliases:
  - ai-alliance
  - thealliance.ai
created: 2026-04-25
updated: 2026-11-15
tags:
  - concept
  - organization
  - nonprofit
  - open-source
  - ai-organization
  - ibm
sources:
  - https://thealliance.ai/
  - raw/articles (dorialexander Common Corpus / SYNTH entries)
---

# AI Alliance

The **AI Alliance** (thealliance.ai) is a nonprofit collaborative network — originally launched in 2023 with **IBM** and **Meta** as lead sponsors — of companies, startups, universities, research institutions, and governments advancing **open, safe, and responsible AI** through open-source data, models, evaluation, and advocacy. It is the institutional home of the open-weight ecosystem's "public goods" projects, and is distinct from NVIDIA's security-focused [[concepts/open-secure-ai-alliance]].

## Structure (two nonprofits)

| Organization | Form | Mission |
|--------------|------|---------|
| **AI Alliance Community** | 501(c)(3) | Research & education: open datasets, evaluation, safety research, widescale education |
| **AI Alliance Association** | 501(c)(6) | Industry association: open-source AI agents, models, applications, and policy advocacy |

Member-driven working groups organize work into four project categories: **The Open Agent Hub**, **Open Data and Models**, **Safety and Governance**, and **Education and Advocacy**.

## Flagship Projects

### Open Trusted Data Initiative — Common Corpus
The largest fully open multilingual pretraining dataset: **~2.3T tokens, 517M documents, 300+ languages**, built from six collections (Open Government, Open Culture, Open Science, Open Code, Open Web, Semantic Data), all permissively licensed with verifiable provenance. Orchestrated by alliance member [[entities/dorialexander|Doria Alexander]]'s team (Kognitis); ICLR 2026 oral; downstream use by NVIDIA, Anthropic, IBM, Elastic.

### SYNTH (Nov 2025)
First fully **synthetic** generalist pretraining dataset (~79.6M samples, ~100B tokens), released jointly with the AI Alliance around open standards for data attribution and releasability — an attempt to standardize synthetic-data provenance.

### Project Tapestry (2026)
Collaborative foundation for **open and sovereign AI**, announced April 2026 — pairing the alliance's open-stack work with national sovereign-AI programs (e.g., expansion to Indonesia).

### Other active programs
- **GEO-Bench-2** — geospatial AI evaluation ("from performance to capability").
- **MCP-Agent / deep-research agent** reference implementations; governed conversational-BI agent builds.
- **National AI Research Resource (NAIRR) Pilot** deep partnership (US public AI infrastructure).
- Domain-specific AI blueprints (semiconductor, maritime safety-critical industries).

## Position in the Open-AI Debate

The AI Alliance is the institutional counterweight to both closed-lab vertical integration and casual scraping-based open models: its thesis is that open AI becomes durable only with **trusted data provenance, shared evaluations, and governance frameworks** — public-goods infrastructure no single lab will fund. It anchors the governance wing of [[concepts/open-source-ai-must-win]] and complements [[concepts/open-source-llm-governance-debian-gr]].

## Distinguishing: AI Alliance vs Open Secure AI Alliance

| | AI Alliance | Open Secure AI Alliance |
|---|---|---|
| Founded | 2023, IBM + Meta | 2026, NVIDIA (Jensen Huang) |
| Framing | Open innovation + trusted data/governance | Security case for open weights |
| Artifacts | Common Corpus, SYNTH, Tapestry, GEO-Bench | Open-weight security advocacy |

## Related Concepts

- [[entities/dorialexander]] — Common Corpus / SYNTH lead
- [[concepts/open-secure-ai-alliance]] — the separate NVIDIA security alliance
- [[concepts/open-source-ai]] / [[concepts/open-source-ai-must-win]] — the ecosystem debate it participates in
- [[concepts/open-source-licensing]] — provenance/permissive-licensing discipline

## Sources

- [thealliance.ai](https://thealliance.ai/) — mission, structure, project catalog (scraped 2026-11-15)
- [[entities/dorialexander]] — timeline entries for Common Corpus (Nov 2024) and SYNTH (Nov 2025)
