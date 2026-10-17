---
title: "Where the Missing Software Went"
created: 2026-10-17
updated: 2026-10-17
type: query
tags: [ai-economics, ai-industry, productivity, developer-tooling]
sources:
  - raw/articles/2026-10-17_seangoedecke_ai-is-driving-a-boom-in-modestly-successful-software.md
confidence: medium
related:
  - "[[concepts/modest-success-software-boom]]"
  - "[[concepts/code-review-bottleneck]]"
  - "[[concepts/ai-slop-productivity-paradox]]"
  - "[[concepts/harness-tax]]"
---

# Where the Missing Software Went

> Question: "If AI lets anyone build software, where is all the new software?"
> Answer: it exists, but it is small, used by hundreds-to-thousands, and invisible to
> hit-product metrics. Filed because the answer reconciles three otherwise-contradictory
> wiki claims.

## Three measurements that looked contradictory

| Page | Claim | Apparent tension |
|---|---|---|
| [[concepts/modest-success-software-boom]] | 2x modestly-successful projects, 10x total projects | Software *is* booming |
| [[concepts/code-review-bottleneck]] | +30% LOC, +20% commits, +23% PRs, net shipped software ≈ flat | Software is *not* booming |
| [[concepts/ai-slop-productivity-paradox]] | Output metrics inflated, no GDP/quality gain | The boom is *fake* |

## Resolution: they measure different gates and different populations

1. **Different populations.** Jellyfish telemetry covers ~700 *firms* (2021→Mar 2026).
   Goedecke measures *hobbyist registries* (NVDA addons, HACS, Steam, Obsidian, Nexus,
   Blender). The two samples barely overlap.
2. **Different gates.** Enterprise has a **human code-review gate** that caps throughput
   regardless of how fast agents write code — so enterprise output stays flat even as
   LOC climbs. Hobbyist registries have **no review gate**; the only filter is whether a
   few hundred people install it. Cheap code converts to shipped software there, not here.
3. **Different tiers.** Growth is confined to the *modest* tier (>100 installs, >100
   reviews). The *wild* tier is flat everywhere — consistent across both datasets and with
   Goedecke's feature-saturation + "good ideas are hard" hypotheses.
4. **Different cost structures.** Enterprise AI carries the full
   [[concepts/harness-tax|harness tax]] — tooling, review, audit, maintenance of an
   owned system (the Hex "prototype is cheap, owning is expensive" trap). A hobbyist
   shipping an Obsidian plugin carries none of it.

## Net position

The "missing software boom" is not missing and not slop: it landed in ungated, low-stakes,
long-tail software, where a model's marginal capability converts directly into shipped
artifacts. In gated, high-stakes enterprise work, the same capability is reabsorbed by
review and ownership cost. A model improvement shows up as *more small tools* before it
shows up as *more enterprise throughput*.

## Unresolved

- No dataset yet measures hobbyist software's *economic* value, so Marcus's "no real
  impact" and Goedecke's "it's used by thousands" are not yet in direct contact.
- Whether wild-tier projects lag (and will appear) or are structurally unreachable by
  cheap code is the single load-bearing open question.

## Sources

- Goedecke registry study (2026-10-15): `raw/articles/2026-10-17_seangoedecke_ai-is-driving-a-boom-in-modestly-successful-software.md`
- Chen & Stratton (Harvard) Jellyfish telemetry, covered by Ars Technica (2026-10-09) — see [[concepts/code-review-bottleneck]]
