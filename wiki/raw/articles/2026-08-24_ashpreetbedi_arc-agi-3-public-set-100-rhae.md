---
title: "Ashpreet Bedi — Agno ARC-AGI-3 Arcade: Verified 100.00 RHAE on public set"
date: 2026-08-24
date_ingested: 2026-08-25
source: https://x.com/ashpreetbedi/status/2092002398805856339
author: Ashpreet Bedi (@ashpreetbedi)
type: x_post
tags: [agent-evaluation, benchmark, harness-engineering, agent-framework, reasoning, evaluation]
related:
  - concepts/ai-benchmarks/arc-agi-3
  - entities/ashpreet-bedi
  - entities/agno
---

# Ashpreet Bedi — Agno ARC-AGI-3 Arcade: Verified 100.00 RHAE on public set

## Tweet

**Posted:** 2026-08-24T21:33:34Z  
**Author:** Ashpreet Bedi (@ashpreetbedi), founder/CEO of Agno  
**URL:** https://x.com/ashpreetbedi/status/2092002398805856339

> Tomorrow. 100% on ARC-AGI-3 public set.
>
> [GitHub - agno-agi/arc-agi-arcade](https://github.com/agno-agi/arc-agi-arcade)

**Engagement (2026-08-25 UTC):** 44 likes, 2 replies, 5 retweets, 0 quotes, 37 bookmarks, 5,532 impressions.

## Linked repository: `agno-agi/arc-agi-arcade`

- **URL:** https://github.com/agno-agi/arc-agi-arcade
- **Description:** "Agents playing the ARC-AGI-3. Top score: a verified 100.00 RHAE."
- **Language:** Python
- **License:** MIT
- **Created:** 2026-08-23
- **Stars/forks/watchers:** 6 / 0 / 6 at ingest (very new)
- **Default branch:** main

### What the repo says (README summary)

The repo is a live arcade of **Agno agents** playing the 25-game public set of ARC-AGI-3 (183 levels total). Every VERIFIED run links to an official ARC scorecard minted in Competition Mode and replayed action-by-action.

**Top leaderboard at ingest:**

| Player | Run | Score (RHAE) | Levels | Actions |
|---|---|---:|---:|---:|
| GPT-5.6 Sol | warm-3 | **100.00** | 183/183 | 7,189 |
| GPT-5.6 Sol | warm-1 | **100.00** | 183/183 | 7,891 |
| Gemini-3.7-Flash (seeded GPT-5.6) | seeded-2 | 96.42 | 179/183 | 8,308 |
| GPT-5.6 Sol | cold-1 | 96.15 | 180/183 | 9,422 |
| Human baseline (ARC published expert aggregate) | — | 95.4 | 183/183 | — |
| GPT-5.6 Sol | warm-2 | 94.81 | 179/183 | 7,601 |
| Grok-4.6 (seeded GPT-5.6) | seeded-1 | 89.31 | 168/183 | 8,032 |
| Gemini-3.7-Flash (seeded GPT-5.6) | seeded-1 | 88.78 | 168/183 | 7,648 |

### Key details

- **Three modes:** cold (blank start), warm (reuses own prior learnings/manuals), seeded (reuses other agents' manuals, merged with own).
- **Python kernel (CodeMode):** agents get a stateful Python environment with filesystem access; observed behavior includes reading game source code, reading other models' manuals, and building offline copies of games — runs where this occurs are flagged CONTAMINATED.
- **Learning store:** agents save verified facts while playing; session resets at each level so only the "manual" survives and is injected into the next session.
- **Action budget:** a game's budget is 5x its human baseline, capped per run as a cost guard. Later runs use per-run `--cap` declarations (default 2500). Raising the cap cannot inflate score because RHAE scores a level as `min((baseline/actions)^2, 1.15)`.
- **Verification:** every committed action is recorded to a trace; `replay.py` re-plays traces through ARC's engine and mints scorecards server-side.

### Important caveats

- The 100.00 RHAE is on the **public demonstration set only** (25 games, 183 levels). ARC-AGI-3's primary evaluation is on harder, out-of-distribution private sets that are not publicly playable; the public score "says nothing about them."
- The repo's own disclaimers state that nobody has beaten ARC-AGI-3 on the private basis (as far as they know).

## Wiki context

This result extends the existing [[concepts/ai-benchmarks/arc-agi-3]] page, which previously documented OpenAI's July 2026 finding that GPT-5.6 Sol's score tripled from 13.3% to 38.3% when reasoning retention and compaction were enabled. The Agno arcade adds:

1. **Public-set saturation** — a frontier model (GPT-5.6 Sol) has now achieved a verified 100.00 RHAE on the full public set, exceeding the published human expert baseline of 95.4.
2. **Harness/agent-loop evidence** — the Agno composition (single action toolkit + Python CodeMode kernel + persistent learning manuals + campaign engine) is an independent harness that achieves the public-set top mark, supporting the broader "harness engineering matters" thesis.
3. **Cross-model seeding effect** — models seeded with GPT-5.6's manuals consistently outperform their own cold runs (e.g., Gemini-3.7-Flash 96.42 vs GPT-5.6 cold 96.15), showing transferable game-mechanics knowledge.

## Related pages

- [[concepts/ai-benchmarks/arc-agi-3]] — ARC-AGI-3 benchmark page
- [[entities/ashpreet-bedi]] — Ashpreet Bedi, Agno founder
- [[entities/agno]] — Agno agent platform
