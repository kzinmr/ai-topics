---
title: "LLM Idea Convergence"
created: 2026-09-05
updated: 2026-09-08
type: concept
tags:
  - concept
  - ai-commentary
  - philosophy
  - ai-agents
  - vibe-coding
  - ai-society
  - memetics
sources:
  - raw/articles/lucumr.pocoo.org--2026-9-5-latent-powers--6e8dcc87.md
related:
  - entities/armin-ronacher
  - concepts/vibe-coding
  - concepts/latent-terms
  - concepts/jagged-frontier
---

# LLM Idea Convergence

**LLM Idea Convergence** is the hypothesis that because independent builders all
consult the *same* frontier models — with the same capability distribution, the
same training corpus, and the same "plausible next step" priors — those models
silently steer people toward the *same* projects, so that ideas which feel
individually original are in fact a shared artifact of the model ecosystem.

The term describes a phenomenon articulated most crisply by
[[entities/armin-ronacher]] in his post **"Latent Powers"** (2026-09-05), though
the observation circulates as a running joke across the AI-builder community
("we're all building the same thing").

## The core mechanism

Ronacher's CarPlay-dongle anecdote is the canonical worked example:

1. He wanted to hack a cheap CarPlay bridge so his own code could run alongside
   CarPlay passthrough.
2. Asking his coding agents (Fable / Sol via Pi) surfaced **CatPlay**, a Rust
   reimplementation of the CarPlay protocol for Carlinkit devices. Ronacher
   *did not find CatPlay* — the model did.
3. Separately, an acquaintance independently decided to wire his own agent into
   his car and — also from an LLM, around the same time — discovered the same
   CarPlay hacking community as an option.
4. Both believed they were pursuing a personal idea; both were pushed there by a
   conversation with the same class of model.

Ronacher's sharper framing:

> "What if we took paths, because those were the paths that were more likely with
> current generation models?"

> "Completely independent people end up building things they believe are their own
> ideas. Yet they were inspired or pushed towards doing something by a conversation
> with an LLM — a conversation that someone else also had."

## Second worked example: HTML over Markdown reports

Lucas Meijer's proposal (via Pi) to have a model produce **HTML reports instead
of Markdown** initially looked like a personal aesthetic preference. It has since
become the default choice for many builders — partly because the models
themselves are increasingly *trained* to prefer it (cf. Claude Artifacts). A
"taste" that seemed individual turned out to be a property of the shared model
distribution.

## Why it matters

| Dimension | Pre-LLM invention | LLM-mediated invention |
|-----------|-------------------|------------------------|
| Idea source | Human search, community, intuition | Chat with a widely-used model |
| Search breadth | Idiosyncratic background, geography, mentors | Same training corpus for everyone |
| Tenacity threshold | Many projects abandoned as "too laborious" | Agents supply persistence; more projects survive ("my clanker is tenacious") |
| Independence signal | Coincidence is rare | Coincidence is the expected outcome |

Three consequences:

1. **Originality is harder to attribute.** A project's "who thought of it first"
   history is now mediated by shared priors that don't show up in citations.
2. **The builder landscape is correlated.** Popular projects cluster along the
   highest-probability branches of current model outputs, not along the true
   possibility space.
3. **Model capability distribution = cultural attractor.** Any capability or
   preference baked into frontier models — e.g. "produce HTML artifacts",
   "use a Rust rewrite when you find a protocol", "prefer Raspberry Pi for
   hardware" — becomes a global default, independent of any human advocate.

## Where this fits in the wider conversation

- Extends [[concepts/vibe-coding]]: vibe-coding describes *how* code gets
  written when humans and models coauthor; LLM Idea Convergence describes what
  happens to *which projects get started at all* once the ideation loop is also
  model-mediated.
- Analogous to mode collapse / low-diversity sampling, but applied to the
  *human* idea stream after the model is introduced as a collaborator, rather
  than to text outputs inside a single model.
- Related to [[concepts/latent-terms]] in spirit: the "latent space" of models
  contains attractor basins whose shape leaks out into what builders build.
- Related to [[concepts/jagged-frontier]]: which project paths feel "possible"
  depends on which frontier the model can support; different model generations
  will make *different* hobbyist projects discoverable.

## Open questions

- Can the convergence effect be measured (e.g. clustering newly-announced
  projects over time against model releases)?
- Do diverse model ecosystems (open-weight vs frontier-only) measurably increase
  project diversity in a community?
- Is there a *positive* reading — a coordination mechanism that helps
  complementary projects find each other — or only the homogenizing one?
- Does model-mediated *tenacity* ("my clanker is tenacious") widen the project
  distribution (more projects started) even as it narrows it (same projects)?

## Measurement

The open question ("can convergence be measured?") has a cheap first probe:
**repeated attribution**. If many independent builders "discover" the same
pre-existing repo (CatPlay, in Ronacher's example) inside a short window, the
models — not the community — are the discovery channel. A concrete protocol:

1. Pick an open-source project whose README/repo age predates a model release.
2. Count first-time contributors/blog posts/tweets mentioning it in windows
   before vs after that release.
3. A spike unaccompanied by any human advocate (no HN thread, no newsletter)
   is model-mediated discovery — a cultural attractor event.

OpenAI's model cards corroborate the mechanism at the output side: the GPT-5
family system cards report output diversity via distinct-n with and without
repetition penalty ([[concepts/gpt/gpt-5-system-card]] and its 5.1/5.2
updates). If the *outputs* of a single model measurably collapse toward shared
modes, the human idea streams fed by that model inherit the same distribution —
the wiki's [[concepts/representation-collapse]] page describes the same dynamic
for models trained on model output; idea convergence is its human-facing mirror.

## Related

- [[entities/armin-ronacher]] — articulator of the thesis
- [[concepts/vibe-coding]] — adjacent phenomenon: model-mediated authorship of code
- [[concepts/latent-terms]] — internal model features that also "leak" outward
- [[concepts/jagged-frontier]] — uneven capability determines which ideas feel reachable

## Sources

- [Latent Powers — Armin Ronacher (2026-09-05)](https://lucumr.pocoo.org/2026/9/5/latent-powers/)
- [Announcement tweet](https://x.com/mitsuhiko/status/2096221291455947172)
