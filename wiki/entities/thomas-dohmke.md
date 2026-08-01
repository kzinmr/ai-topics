---
title: Thomas Dohmke
type: entity
created: 2026-08-01
updated: 2026-08-01
status: L3
tags:
  - person
  - ceo
  - github
  - open-source
  - coding-agents
  - git
  - entrepreneur
aliases:
  - "Dohmke"
  - "Thomas Dohmke"
  - "@ashtom"
  - "thomas-dohmke"
sources:
  - https://entire.io/blog/an-entirely-new-git-hosting-network
  - https://entire.io/blog/how-version-control-will-evolve-for-the-agent-boom
  - https://entire.io/about/company
  - https://en.wikipedia.org/wiki/Thomas_Dohmke
  - https://github.com/ashtom
---

# Thomas Dohmke

**Thomas Dohmke** (born 1978, East Berlin) is a German software developer and business executive. He is best known as the former CEO of **GitHub** (November 2021 – 2025, succeeding Nat Friedman) and co-founder of **HockeyApp** (acquired by Microsoft, 2014). In early 2026 he founded **Entire**, a developer platform for the agent era, valued at $300M by February 2026.

## Quick Facts

| Field | Value |
|-------|-------|
| **Born** | 1978, East Berlin, East Germany |
| **Education** | Diplom-Ingenieur, Technische Universität Berlin (computer engineering); PhD, University of Glasgow (mechanical engineering) |
| **Known for** | ex-CEO of GitHub; co-founder of HockeyApp; founder/CEO of Entire |
| **X/Twitter** | [@ashtom](https://x.com/ashtom) |
| **GitHub** | [ashtom](https://github.com/ashtom) |

## Career Timeline

| Year | Event |
|------|-------|
| 2000s | Co-founded **HockeyApp**, a mobile app distribution and crash reporting platform (with Daniel Bock, et al.) |
| 2014 | HockeyApp acquired by **Microsoft** |
| 2014–2021 | Microsoft: various roles including Chief Product Officer of GitHub after the 2018 acquisition |
| Nov 2021 | Became **CEO of GitHub**, replacing Nat Friedman |
| 2021–2025 | Led GitHub through the AI coding era; oversaw the explosive growth of **GitHub Copilot** |
| Aug 2025 | Announced departure from GitHub at end of year to start a new company (Axios exclusive) |
| Early 2026 | Launched **Entire**, a startup merging human and AI-based programming |
| Feb 2026 | Entire valued at **$300M** (Bloomberg) |
| Jul 2026 | Published "An Entirely New Git Hosting Network" — Entire's distributed Git mirror network launch |

## GitHub Era (2021–2025)

As GitHub CEO, Dohmke led the platform during the AI coding boom. GitHub Copilot became the defining product of the era, and under his leadership GitHub shipped Copilot Workspace, Copilot Autofix, and expanded into the AI-native developer experience. He was a prominent evangelist for AI-assisted coding, frequently publishing essays and appearing at conferences on the future of software development.

Notable wiki references to his GitHub tenure:
- **Shopify's Copilot deployment**: Farhan Thawar emailed Dohmke on his first day as GitHub CEO — "I would like GitHub Copilot deployed for all Shopify engineers as soon as humanly possible" — making Shopify the first company outside GitHub to deploy Copilot (2 years free in exchange for feedback). See [[entities/farhan-thawar]] and [[entities/shopify]].

## Entire (2026–present)

Dohmke founded **Entire** after leaving GitHub, with the thesis that **session logs are the most important artifact in software development** and should be stored alongside code in the repository. Entire productizes:

- **Checkpoints** — agent sessions (prompts, tool calls, decisions) stored in git history, paired with every commit
- **Entire CLI** — open-source (MIT), works with any coding agent
- **Distributed Git Network** — regional mirrors of GitHub repos so agent fleets clone fast without rate limits; Git hosting "returning to its original promise" of decentralization

His July 2026 essay "An Entirely New Git Hosting Network" argues that centralized Git hosting was built for a human-paced loop that breaks under agent-scale concurrency, and that Git hosting must evolve into a distributed network of many hosts. He also frames Git's future as a **semantic memory layer** where session logs give agents the full history of how a codebase was built — not just the code, but the decisions behind it.

## Key Quotes

> "By design, Git was always meant to be decentralized... This was sustainable until agents came along, sending thousands of concurrent requests in seconds, triggering traffic caps, and exposing failure points. We believe that Git hosting must return to its original promise: a truly distributed network, not a system where the world's software lives in a single location." — *An Entirely New Git Hosting Network* (Jul 2026)

> "As code becomes increasingly abundant through agents, the context behind 'why' the code was written is becoming vital: the agent sessions with their prompts, tool calls, checkpoints, and decisions. They all reveal the intent of the developer and tell the story of how a piece of software was built." — *How Version Control Will Evolve for the Agent Boom* (Jul 2026)

## Related Entities

- [[entities/entire]] — His startup; he serves as CEO
- [[entities/evis-drenova]] — Principal engineer at Entire
- [[entities/farhan-thawar]] — Shopify CTO who deployed Copilot org-wide during Dohmke's GitHub tenure
- [[entities/shopify]] — Early Copilot adopter during his GitHub era

## Related Concepts

- [[concepts/evaluation/agent-observability]] — Capturing agent sessions and decisions (Entire's core value prop)
- [[concepts/pgr]] — Agentic search tool built by Entire's team
- GitHub Copilot — AI pair programmer that defined Dohmke's GitHub era (no dedicated entity page yet)

## Sources

- [Wikipedia: Thomas Dohmke](https://en.wikipedia.org/wiki/Thomas_Dohmke)
- [An Entirely New Git Hosting Network (entire.io)](https://entire.io/blog/an-entirely-new-git-hosting-network)
- [How Version Control Will Evolve for the Agent Boom (entire.io)](https://entire.io/blog/how-version-control-will-evolve-for-the-agent-boom)
- [Entire Company page](https://entire.io/about/company)
- [GitHub: ashtom](https://github.com/ashtom)
