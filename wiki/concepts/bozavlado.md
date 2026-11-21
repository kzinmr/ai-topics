---
title: "bozavlado — nanogpt-speedrun contributor"
type: concept
aliases:
  - bozavlado
  - Bozavlado
created: 2026-04-25
updated: 2026-11-21
tags:
  - person
  - pseudonymous
  - open-source
sources:
  - https://github.com/alexjc/nanogpt-speedrun
  - wiki/entities/grad.md
status: stub
---

# bozavlado

**bozavlado** is a pseudonymous contributor to the
**nanoGPT speedrun** effort — the community project to train
Karpathy's nanoGPT on WikiText-103 to val loss ≤ 3.28 in record wall-clock
time on 8×H100 hardware. The handle is credited explicitly in the
`alexjc/nanogpt-speedrun` README's contribution list.

## Credited Contribution

The canonical attribution line from the speedrun README:

> "The training has attained this speed due to the contributions of meself,
> @Grad62304977, @jxbz, @bozavlado, @brendanh0gan, @KoszarskyB, &
> @fernbear.bsky.social."

bozavlado is one of the eight credited contributors whose techniques (together)
cut training time by ~45% from prior records, with the record reaching
**2.9 minutes** (as of 2025). The other contributors documented in the wiki:

| Handle | Known contribution | Wiki page |
|--------|-------------------|-----------|
| @Grad62304977 | Fares Obeid — value embeddings, Muon optimizer lineage | [[entities/grad]] |
| @jxbz | Jeremy Bernstein — Newton-Schulz iteration | [[concepts/jxbz]] |
| @brendanh0gan | U-net, 2× learning-rate record | [[concepts/brendanh0gan]] |
| @bozavlado | (technique not individually itemized in README) | this page |
| @KoszarskyB / @fernbear | (EleutherAI speedrun team) | — |

## Identity Status

- GitHub search and Wayback Machine return **no public profile** for the
  handle as of 2026-11-21 — the account appears deleted or never existed on
  GitHub; the handle was primarily an X/Twitter identity.
- Pseudonymous, like [[entities/grad|Grad]] (who was later doxxed as Fares
  Obeid). No verified real-name attribution exists for bozavlado.

## Open Questions

- Which specific speedrun technique (kernels, init scheme, optimizer tweaks)
  bozavlado authored — needs a git-blame pass over speedrun forks.
- Whether the handle maps to a known ML-engineering identity.

## Related Pages

- [[entities/grad]] — fellow speedrun contributor with a full profile
- [[concepts/jxbz]] — fellow speedrun contributor
- [[concepts/brendanh0gan]] — fellow speedrun contributor
