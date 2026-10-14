---
source_url: https://www.anthropic.com/engineering/redesigning-source-control
ingested: 2026-10-14
sha256: 70ecaa458c059026f4e2e236ec11d7b6640d7193e52123cc3df6bec2b3fb57b0
title: Redesigning source control at Anthropic (Scion + Antique)
author: Anthropic Engineering
published: 2026-10-13
---

# Redesigning source control at Anthropic

Published 2026-10-13 by Anthropic Engineering. Summarized here (extracted body of the
Anthropic engineering post + Simon Willison's commentary at
https://simonwillison.net/2026/Oct/13/redesigning-source-control-at-anthropic/).

## Problem: source control became the bottleneck, not coding

- Coding is no longer Anthropic's bottleneck; **developer infrastructure built for human
  scale is** (source control, builds, CI).
- Merge rate: **~2,500 code changes merged/day in May 2026 → 30,000+/day by September 2026**
  (more than tenfold in a few months). "The latent demand for merging code is practically
  infinite, and every bottleneck we remove immediately leads to a further increase in the
  amount of code we produce."
- Anthropic believes most AI-heavy orgs will hit the same pressure points soon.

## Scale numbers

- Main branch history alone is almost **100 GB**; a compressed working copy is **over 25 GB**.
- **~25 million code checkouts per day** for CI alone (before dev envs, agent sandboxes,
  research jobs). Naively fetched that would be **over 600 PB of git traffic per day**.
- At peak they operated **several hundred internal git mirrors** to serve load; these became
  hard to operate as merge rate rose (seeds drifted from tip of main; diff/blame got hard on
  partial clones).

## What they built

- **Scion** — in-house version control system. Monorepo fully migrated off git in **five
  months**, built by a **team of seven**.
- **Antique** — new code review surface. Also shipped code search, a source-control IAM
  system, and new ways to land large amounts of reviewed code, same period.
- Prior art acknowledged: **Google's Piper** and **Meta's Sapling** (large-monorepo VCS).

## Principles for agent-scale source control (Scion's design bets)

1. **Clients are always online.** Git assumes offline clients needing a complete repo copy.
   Nearly all Scion clients are agents and jobs that are online by definition, so the
   client/protocol is designed around an always-reachable server; clients fetch on demand.
2. **Client–server asymmetry.** In git every client can be a full server. In Scion the server
   answers history/blame questions, creates commits, does merges/rebases. The client keeps a
   bounded local object cache, lays out working files, watches filesystem changes — and
   computes very little locally in exchange for needing far less data.
3. **Source control as a service / API.** All source-control queries are exposed via API, so
   jobs often don't need a local repo at all. Enables automated bisect and revert pipelines at
   scale via cheap programmatic access.
4. **Everything horizontally scalable.** Repository data is distributed; every component
   independently scalable. No fully materialized copy of the repo anywhere, even on the server.
   No equivalent of git packfiles.

## Notable quotes / observations

- On removing offline support: a Scion engineer ("Nick G") on Hacker News said since **Claude
  is by far the heaviest user of Scion and is necessarily online, offline support "just wasn't
  important to do."** (Simon Willison)
- On adversarial review: "Anthropic also makes extensive use of adversarial review, and, while
  this is incredibly effective in many ways, it can also be myopic, so skilled engineers needed
  to steer Claude away from over-engineering parts of the system in response to hypothetical
  concerns." (Simon Willison relayed this reflected his own experience playing Claude and GPT
  off each other for adversarial review.)
- Simon Willison's read: Scion "sounds like a reinvention of centralized source control along
  the lines of Subversion"; the introduction of Fable/Mythos-class models is his guess for the
  key factor in the coding-velocity jump.

## Cross-links (wiki)

- Related to the "the repo is the factory" thesis: dark-factory-software-factory,
  agentic-software-factory-hierarchy-of-needs, lint-rules-as-agent-feedback-loop.
