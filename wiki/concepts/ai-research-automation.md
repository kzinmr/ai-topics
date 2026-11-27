---
title: AI Research Automation
created: 2026-11-27
updated: 2026-11-27
type: concept
tags: [ai-research-automation, research, ai, benchmark, evaluation, reproducibility, ai-society]
sources:
  - raw/articles/databasearchitects.blogspot.com--2026-11-can-we-save-vldb-and-sigmod-html--d5467ddd.md
  - raw/articles/databasearchitects.blogspot.com--2026-11-next-level-benchmarking-overfitting-html--2306a535.md
confidence: medium
---

# AI Research Automation

**AI research automation** is the use of LLM agents to perform the pipeline of scientific
research itself — implementing ideas, running experiments, analyzing results, and writing
papers — rather than merely generating text about research. As of late 2026 the term names
both a capability claim (agents can produce publishable results) and an institutional
crisis (peer review and publication filters were priced against human research cost, which
agents collapse).

This page tracks the *institutional* dimension. The benchmark-gaming dimension (agents
optimizing metrics rather than workloads) lives in [[concepts/benchmarking-crisis]]; the
two share an author and a mechanism.

## The canonical first-hand account: Thomas Neumann (Nov 2026)

The clearest evidence-to-date comes from **Thomas Neumann** (TU Munich, designer of Umbra;
Database Architects blog), who is simultaneously an agent power user and the field's
sharpest institutional critic — see [[concepts/benchmarking-crisis]] for his GenDB-V
teardown of "AI-generated, formally verified" database engines.

In "Can we save VLDB and SIGMOD?" (Nov 2026) he reports:

- **Submission flood**: 500+ submissions for a single *non-peak-month* VLDB deadline;
  ~2,000 SIGMOD submissions in 2026; over 5,000 combined, ~1,000 accepted. Program
  committees grow fast but reviewers are overloaded, authors get random reviews, and
  outcomes are "more and more random."
- **Two multiplicative drivers**: China's huge investment in science × AI-in-research.
- **The writing failure mode**: AI "writes well at the sentence level but not at the level
  of an entire paper" — producing superficially good-looking, low-novelty submissions that
  are hard to read and review.
- **A Goodhart loop on submissions themselves**: the more random review becomes, the more
  rational it is to submit *more* papers; proposed institutional reforms are "way too
  incremental."
- **First-hand productivity numbers**: over several months he ran a number of research
  ideas through agents; **half a dozen produced "amazing results that I would have
  published in the past," each in at most a couple of days of prompting for what was
  previously many months of work**. AI also "greatly accelerates the production of
  mediocre (but not very good) writing."
- **Prescription**: raise the publishing bar *way* up — the value of genuinely good
  research is rising (good ideas integrate into systems faster), while incremental
  busywork previously accepted for its implementation cost now has "little or even
  negative value."

## Why it's a wiki-worthy category

Research publication is a **cost-signal system**: novelty claims were credible partly
because producing the artifact was expensive. Agent automation removes the cost without
removing the signal, so every filter built on the old price structure (review capacity,
acceptance rates, "hard to fake" effort markers) degrades. This is Goodhart's law applied
to peer review, structurally identical to benchmark overfitting on the evaluation side
([[concepts/benchmarking-crisis]], [[concepts/evaluation/reward-hacking]]).

## Open questions

- Whether "raise the bar" reforms can scale when reviewers are themselves overloaded, or
  whether fully automated review (with its own gaming surface) becomes the only option.
- Whether agent-produced results that pass raised bars are distinguishable from
  agent-gamed results — the GenDB-V pattern (verification that never fires) suggests not.
- Disclosure norms: Neumann reports half a dozen publishable agent results privately; no
  venue currently requires disclosing agent-generated research labor.

## Related

- [[concepts/benchmarking-crisis]] — same author, same cost-signal-collapse mechanism on the eval side
- [[concepts/evaluation/reward-hacking]] — agent-side Goodhart's law
- [[concepts/agent-generated-software]] — the engineering analogue of agent-produced artifacts
- [[concepts/recursive-self-improvement]] — automation of research as the frontier-lab endgame thesis
