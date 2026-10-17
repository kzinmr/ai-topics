---
title: Scion (Anthropic version control system)
created: 2026-10-14
updated: 2026-10-17
type: entity
confidence: medium
tags: [company, ai-agents, agent-infrastructure]
sources:
  - raw/articles/2026-10-14_anthropic-redesigning-source-control-scion.md
  - raw/articles/anthropic-scion-mononoke-derived-data-rain-2026-10-14.md
related:
  - dark-factory-software-factory
  - agentic-software-factory-hierarchy-of-needs
  - software-factory
  - agent-native-infrastructure
  - lint-rules-as-agent-feedback-loop
  - anthropic
aliases:
  - Antique
  - Scion (VCS)
  - Scion and Antique
---

# Scion (Anthropic version control system)

**Scion** is Anthropic's in-house version control system, with **Antique** as its companion
code-review surface. Announced in the Anthropic Engineering post *"Redesigning source control
at Anthropic"* (2026-10-13). The team of seven fully migrated Anthropic's monorepo off **git**
in five months, and shipped Scion, Antique, code search, and a source-control IAM system.

## Why: source control became the bottleneck, not coding

At Anthropic the bottleneck is no longer writing code — it is developer infrastructure built
for human scale (source control, builds, CI). Merge rate went from **~2,500 changes/day (May
2026)** to **30,000+/day (September 2026)**. As the post puts it, "the latent demand for
merging code is practically infinite, and every bottleneck we remove immediately leads to a
further increase in the amount of code we produce." This is the [dark factory / software
factory](dark-factory-software-factory.md) thesis showing up at the *infrastructure* layer:
once agents do the coding, the repo and its tooling become the constraint.

Scale that broke git:
- Main-branch history alone is **~100 GB**; a compressed working copy is **>25 GB**.
- **~25 million code checkouts/day** just for CI — naively fetched, **>600 PB of git traffic/day**.
- They had to run **several hundred internal git mirrors** to serve load; these became hard to
  operate (seeds drifting from tip of main; hard diff/blame on partial clones).

## Design principles: source control for agents

Scion is a deliberately **agent-first** rethinking of version control (prior art: Google's
Piper, Meta's Sapling):

1. **Clients are always online.** Git assumes offline clients that sync a full repo copy. Most
   Scion clients are agents/jobs that are online by definition, so the protocol assumes an
   always-reachable server and clients fetch on demand.
2. **Client–server asymmetry.** In git every client can be a full server. In Scion the server
   answers history/blame, creates commits, and does merges/rebases; the client keeps a bounded
   cache, lays out files, watches changes — and computes very little locally.
3. **Source control as a service / API.** Every query is exposed via API, so jobs often need no
   local repo at all. Enables automated bisect and revert pipelines at scale via cheap
   programmatic access.
4. **Everything horizontally scalable.** Repo data is distributed; no fully materialized copy of
   the repo exists anywhere (even server-side); no git packfile equivalent.

Simon Willison's read: Scion "sounds like a reinvention of centralized source control along the
lines of Subversion." He also relayed a Scion engineer (HN) noting that since **Claude is by far
the heaviest user of Scion and is necessarily online, offline support "just wasn't important to
do."**

## Why it matters

Scion is one of the first concrete, production examples of **agent-native infrastructure**: a
core developer tool rebuilt from assumptions about *who the client is* once the client is a
fleet of online agents rather than humans with laptops. It pairs with the broader pattern of
rebuilding human-scale tooling around agent throughput (see
[agent-native-infrastructure](agent-native-infrastructure.md) and the
[agentic software factory hierarchy of needs](agentic-software-factory-hierarchy-of-needs.md)).

## "Heavily inspired by Mononoke" controversy (2026-10-14/15)

Within a day of the announcement, **Rain (sunshowers.io)** — a former Meta engineer who helped
build **Mononoke** (Meta's Rust source-control server, designed 2017-18) — published a comparison
arguing Scion's "derived data" concept (used to make `blame` and similar ops efficient) closely
mirrors how he described Mononoke's derived-data design in his 2022 Oxide candidate materials.
He notes Scion credited Sapling only for "hard-won lessons" and never mentioned Mononoke, which he
called "border[ing] on plagiarism," and observed the write-up reads as if Claude designed it all.
A follow-up post answered questions. Notably, Rain holds **no grudge about the copying itself** —
Mononoke is deliberately open source "to benefit humanity through the spread of good ideas."

The durable thesis (why this matters beyond the dispute): as LLMs design new systems they
**index heavily on existing designs in their training set**. Mononoke is open source and in every
major model's training data; Rain reports that asking Opus 5.5 or GPT-6 Astra about Scion's prior
art surfaces the Mononoke similarities immediately. His conclusion: *"Giving credit to those that
came before us is now easier — and more important — than ever. There is no longer an excuse."*
This is a concrete instance of the **AI-derived-data / training-set lineage** question: when a
model reproduces an idea it absorbed from an open-source project, who gets credit? It pairs with
the broader agent-native-infrastructure trend above — Scion is both a genuine re-architecture for
agents *and* a case study in LLM-era attribution.

## Caveats

Anthropic's own post plus commentary and an external attribution critique. Specific design
decisions — no local repo, no offline, server-centric — have trade-offs that will show up in
real-world use; the engineering post is not yet battle-tested by outsiders. The Mononoke-similarity
claim is one engineer's (well-sourced) reading, not an admitted finding by Anthropic. Set
`confidence: medium` accordingly.

## Sources

- [Redesigning source control at Anthropic — Anthropic Engineering](https://www.anthropic.com/engineering/redesigning-source-control)
- [Sim on HN: Anthropic's new source control system](https://news.ycombinator.com/item?id=49849712)
- [Anthropic's Scion is heavily inspired by Mononoke — Rain (sunshowers.io)](https://sunshowers.io/posts/anthropic-mononoke/) (HN 425pts, [item 50094694](https://news.ycombinator.com/item?id=50094694))
- [More on Anthropic's Scion ripping off Mononoke — followup](https://sunshowers.io/posts/anthropic-mononoke-2/) (HN 253pts, [item 50106738](https://news.ycombinator.com/item?id=50106738))
- Raw: `raw/articles/2026-10-14_anthropic-redesigning-source-control-scion.md`, `raw/articles/anthropic-scion-mononoke-derived-data-rain-2026-10-14.md`
