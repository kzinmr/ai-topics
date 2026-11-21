---
title: "Hack Club — nonprofit youth coding community and fiscal sponsor"
type: concept
aliases:
  - hack-club
  - Hack Club Bank
  - Hackathons
created: 2026-04-25
updated: 2026-11-21
tags:
  - organization
  - open-source
  - community
  - ai-education
sources:
  - wiki/raw/articles/mitchellh.com--writing-ghostty-non-profit--0165e454.md
  - wiki/raw/articles/mahadk.com--posts-slack--1f8284e2.md
  - wiki/raw/articles/mahadk.com--posts-spaces-vuln--abeb80da.md
---

# Hack Club

**Hack Club** is a US 501(c)(3) nonprofit that provides coding education,
hardware, and community to teenagers worldwide (founded ~2012, run largely by
teenagers and former teenagers). It is doubly relevant to this wiki: as an
**AI-education/community institution**, and — unusually — as a **fiscal
sponsor of flagship open-source AI-adjacent developer tools**.

## Fiscal Sponsorship of Open Source

- **Ghostty** (Mitchell Hashimoto's terminal emulator, heavily used by AI
  coding-agent users) became fiscally sponsored by Hack Club in 2025. Under
  the arrangement Hack Club manages compliance, donations, accounting, and
  governance; 7% of donations go to Hack Club as overhead; all transactions
  are publicly viewable via the **Hack Club Bank** ledger. Mitchell pledged
  zero funds to himself personally. See
  [[entities/mitchell-hashimoto]] and
  [[raw/articles/mitchellh.com--writing-ghostty-non-profit--0165e454]].
- The model — a nonprofit fiscal sponsor as the "boring infrastructure"
  that keeps an OSS project free from rug-pull risk — has become a reference
  pattern for individually-maintained tools entering the AI toolchain.

## Engineering Culture

Hack Club members ship production-scale infrastructure themselves, which makes
the org a recurring source of security and platform writing:

- **Spaces** — Hack Club's self-hosted alternative to GitHub Codespaces for
  teen hackathon participants; a sandbox-escape vulnerability in it was
  documented in [[raw/articles/mahadk.com--posts-spaces-vuln--abeb80da]].
- **Slack departure** — after 11 years on Slack (paying $5k/yr as a nonprofit),
  Hack Club migrated off; the community post-mortem is at
  [[raw/articles/mahadk.com--posts-slack--1f8284e2]].

## Notable People (alumni orbit)

Many Hack Club alumni and staff move into AI/developer-tool startups; the org
functions as a talent pipeline discussed in AI-education contexts.

## Related Pages

- [[entities/mitchell-hashimoto]] — Ghostty fiscal-sponsorship decision
- [[concepts/ai-education]] — youth coding education as AI-literacy groundwork
- [[concepts/open-source]] — Hack Club Bank as OSS sustainability infrastructure
