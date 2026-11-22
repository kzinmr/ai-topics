---
title: "brendanh0gan — nanogpt-speedrun record holder"
type: concept
aliases:
  - brendanh0gan
  - Brendan Rappazzo
created: 2026-04-25
updated: 2026-11-22
tags:
  - person
  - pseudonymous
  - open-source
  - nanogpt-speedrun
sources:
  - https://x.com/brendanh0gan
  - https://github.com/KellerJordan/modded-nanogpt
  - wiki/entities/grad.md
status: stub
---

# brendanh0gan

**brendanh0gan** is a contributor to the **nanoGPT speedrun** (KellerJordan/modded-nanogpt)
credited with one of the largest single architectural jumps in the record history: the
**U-net pattern skip connections + double learning rate** record.

## Credited Records

From the official modded-nanogpt record table (track 1, 8×H100, target val loss 3.28):

| Record | Time | Change | Date | Credits |
|--------|------|--------|------|---------|
| **#11** | **7.2 min** (from 7.8) | [U-net pattern skip connections & double lr](https://x.com/kellerjordan0/status/1856053121103093922) | 2024-11-10 | **@brendanh0gan** |
| #20 | 2.992 min (first sub-3-minute run) | Merged QKV weights, long-short attention, attention scale, lower Adam epsilon, batched Muon | 2025-01-16 | @leloykun, @fernbear, @YouJiacheng, **@brendanh0gan**, @scottjmaddox, @Grad62304977 |

The U-net trick — adding skip connections from early layers to later layers in a U-net
pattern — was later extended by others (record #15: "U-net pattern value embeddings",
@leloykun/@YouJiacheng), making it one of the most reproduced ideas in the run's history.

He is also listed among the ten authors of the formal citation for the project:
"Keller Jordan, Jeremy Bernstein, **Brendan Rappazzo**, @fernbear.bsky.social, Boza
Vlado, Jiacheng You, Franz Cesista, Braden Koszarsky, and @Grad62304977.
modded-nanogpt: Speedrunning the NanoGPT baseline. 2024."

## Identity Status

- X/Twitter: [@brendanh0gan](https://x.com/brendanh0gan) (linked from the modded-nanogpt
  README contributor list) — primary public identity.
- GitHub: `brendanh0gan` returns **404** (API + page, checked 2026-11-22); `brendanrappazzo`
  is private or absent.
- The **most likely real name is "Brendan Rappazzo"**, from the project's formal citation —
  but no independent public profile confirms the handle↔name mapping, so treat as
  high-confidence inference, not verified.

## Open Questions

- Professional affiliation (never publicly stated under this handle to our knowledge).
- Individual technical notes behind the double-LR discovery — see the record #11 log
  in `records/track_1_short/2024-11-10_UNetDoubleLr/`.

## Related Pages

- [[concepts/jxbz]] — Jeremy Bernstein, Muon co-creator, fellow contributor
- [[concepts/bozavlado]] — fellow contributor
- [[entities/grad]] — Fares Obeid, fellow contributor with a full profile
- [[concepts/aurora-optimizer]] — downstream Muon follow-up
