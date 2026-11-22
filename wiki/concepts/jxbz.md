---
title: "Jeremy Bernstein (@jxbz) — Muon co-creator"
type: concept
aliases:
  - jxbz
  - Jeremy Bernstein
  - jeremybernste.in
created: 2026-04-25
updated: 2026-11-22
tags:
  - person
  - ml-research
  - optimization
  - nanogpt-speedrun
  - open-source
sources:
  - https://jeremybernste.in/
  - https://jeremybernste.in/writing/deriving-muon
  - https://github.com/jxbz
  - https://github.com/KellerJordan/modded-nanogpt
  - wiki/entities/grad.md
---

# Jeremy Bernstein (@jxbz)

**Jeremy Bernstein** (GitHub/X handle **jxbz**) is a machine learning researcher
and one of the co-creators of the **Muon optimizer** — the spectral-normalized,
Newton-Schulz–based optimizer that broke the nanoGPT training-speed records and
was subsequently adopted by major labs. He is currently at **Thinking Machines Lab**
(San Francisco).

> Identity resolution: GitHub [jxbz](https://github.com/jxbz) (name "Jeremy Bernstein",
> blog jeremybernste.in, 165 followers) = X @jxbz = jeremybernste.in ("I am a machine
> learning researcher based in San Francisco... I work at Thinking Machines Lab",
> contact jbernstein@mit.edu). Verified 2026-11-22.

## Muon and the nanoGPT speedrun

Bernstein's central role in the speedrun is documented in the
[KellerJordan/modded-nanogpt](https://github.com/KellerJordan/modded-nanogpt) README:

> "Bernstein & Newhouse (2024) suggested [a Newton-Schulz iteration] as a way to compute
> Shampoo preconditioners, and theoretically explored Shampoo without preconditioner
> accumulation. In particular, **Jeremy Bernstein @jxbz sent us the draft**, which caused
> us to experiment with various Newton-Schulz iterations as the orthogonalization method
> for this optimizer. If we had used SVD instead of a Newton-Schulz iteration, this
> optimizer would have been too slow to be useful."

Concretely:

| Record | Date | Contribution | Credits |
|--------|------|--------------|---------|
| #3 — 24.9 min | 2024-10-04 | **Introduced the Muon optimizer** | @kellerjordan0, **@jxbz** |

Muon is joint work with Keller Jordan, Yuchen Jin, **Vlado Boza** (likely
[[concepts/bozavlado|bozavlado]]), Jiacheng You, Franz Cesista
([[@leloykun]](https://github.com/leloykun) — Franz Louis Cesista), and Laker Newhouse.
See [[entities/grad|Fares Obeid (@Grad62304977)]] for the value-embeddings/optimizer
lineage of other speedrun contributors.

## Key ideas

### Deriving Muon (Mar 2025)

His essay [Deriving Muon](https://jeremybernste.in/writing/deriving-muon) frames the
optimizer as derived from an **exact theoretical principle** rather than heuristics:
the update dualizes the gradient under the RMS-to-RMS operator norm ("orthogonalizing"
the gradient — keep singular vectors, discard singular-value magnitudes). Two payoffs:

- **Fast training**: better final loss than Adam at matched compute on nanoGPT speedruns
  (1.35× record improvement when Muon was introduced).
- **Automatic learning-rate transfer across width** — the dualized update induces a
  controlled RMS output change independent of layer width (contrast: μP's explicit
  rescaling). Experiments credited to Laker Newhouse.

Newton-Schulz is applied to the momentum buffer; his own X posts
([@jxbz](https://x.com/jxbz/status/1846188906733044029)) argued for a dimensional
pre-factor expected to scale better.

### Other essays

| Date | Title | Thesis |
|------|-------|--------|
| 2025-09-26 | [Modular manifolds](https://thinkingmachines.ai/blog/modular-manifolds/) (Thinking Machines blog) | — |
| 2021-10-21 | Machine learning is just statistics + quantifier reversal | Conceptual reframing of ML |
| 2020-04-06 | Getting to the bottom | Reductionist research philosophy |
| 2017-01-22 | The world, how was it generated? | Generative view of reality |

## Background

- **MIT** — contact email jbernstein@mit.edu; arXiv records under
  "Jeremy Bernstein" (MIT affiliation; Shampoo/spectral-norm line of work with
  Laker Newhouse, arXiv:2409.20325).
- **Trinity College** (Cambridge) — earlier student projects on his site
  (Project Swarm, 2011; TCSU Annual Record, 2014).
- **Thinking Machines Lab** — current employer (site + Modular manifolds post).

## Open Questions

- Whether Bernstein contributed further record commits beyond #3 (Muon introduction)
  in later speedrun history — the current README credits list does not show @jxbz
  on records after #4.
- Exact degree timeline (Cambridge → MIT PhD dates) — no public CV found as of 2026-11-22.

## Related Pages

- [[entities/grad]] — Fares Obeid, fellow speedrun contributor
- [[concepts/bozavlado]] — Vlado Boza(?), Muon co-author
- [[concepts/brendanh0gan]] — fellow speedrun contributor (U-net + double LR)
- [[concepts/adam-optimizer]] — baseline optimizer Muon competes with
- [[concepts/aurora-optimizer]] — 2026 follow-up fixing Muon's neuron-death flaw
- [[entities/thinking-machines-lab]] — current employer
