---
title: "Kilo Code — We Audited the Same Codebase with Claude Opus 4.8 and MiniMax M3"
date: 2026-06-07
date_ingested: 2026-06-08
source: https://x.com/kilocode/status/2063719228499542327
author: Kilo (@kilocode)
type: x_article
tags:
  - model-comparison
  - code-audit
  - claude-opus
  - minimax
  - cost-efficiency
  - benchmarking
  - coding-agent
related:
  - entities/kilo
  - entities/minimax
  - concepts/minimax-m3
  - concepts/claude-opus-4-8
---

# We Audited the Same Codebase with Claude Opus 4.8 and MiniMax M3

**Source:** [X Article by @kilocode](https://x.com/kilocode/status/2063719228499542327)
**Engagement:** 293 likes · 138 bookmarks · 24 retweets · 35.8K impressions (as of 2026-06-08)

## Summary

Kilo Code ran a controlled code-audit benchmark comparing **Claude Opus 4.8** (at 4 reasoning levels: medium, high, xhigh, max) against **MiniMax M3** on a fixed TypeScript webhook delivery service codebase with 17 pre-catalogued known issues.

**Key findings:**
- **MiniMax M3**: 13/17 issues found at ~$0.07 — best cost-per-issue ratio
- **Claude Opus 4.8 medium/high**: 13/17 issues — same count as M3, but $1.30–$1.93
- **Claude Opus 4.8 xhigh**: 15/17 issues — best coverage at $2.03
- **Claude Opus 4.8 max**: 15/17 issues — most expensive ($3.39), missed finding xhigh caught

## Pricing Comparison

Claude Opus 4.8 is ~8× higher on input and ~10× higher on output per-token pricing vs MiniMax M3.

## Test Setup

- **Codebase**: Webhook delivery service (TypeScript, Bun, SQLite) with known bugs left in place
- **Prompt**: "Treat this webhook delivery service as production-bound code and audit it for security, reliability, correctness, and test coverage, without editing any files. Write your report to audit.md."
- **Tool**: Kilo Code CLI, each run in its own session with no shared state
- **Metrics**: Token count, cost, wall-clock time, issues found (out of 17 known)

## Results

| Model | Setting | Issues Found | Tokens | Cost | Time |
|-------|---------|-------------|--------|------|------|
| MiniMax M3 | default | 13/17 | ~59% of Opus medium | $0.07 | 5m 03s |
| Claude Opus 4.8 | medium | 13/17 | baseline | $1.30 | 3m 53s |
| Claude Opus 4.8 | high | 13/17 | +6% vs medium | $1.93 | 4m 33s |
| Claude Opus 4.8 | xhigh | 15/17 | +17% vs high | $2.03 | 7m 26s |
| Claude Opus 4.8 | max | 15/17 | slightly fewer than xhigh | $3.39 | 9m 24s |

## What Each Model Caught

**All runs caught (major blockers):**
- Missing authentication on every route
- Unsafe outbound-request handling
- Signature computed over wrong byte string
- Non-constant-time signature check
- Worker sending same webhook twice (no idempotency)

**MiniMax M3 uniquely caught (among cheaper runs):**
- Endpoint returning stored secret
- Delivery-list filter dropping condition on combined filters
- Subscriber deletion failing with delivery history
- Replay path accepting wrong-state deliveries

**MiniMax M3 missed (caught by Opus xhigh/max):**
- Invalid JSON returning 500
- Database setup running at import time
- Async callback inside synchronous transaction

## Key Insight: Reasoning Level ≠ Linear Improvement

Raising Claude Opus 4.8's reasoning level changed where the model spent its attention more than how much it checked:
- medium/high caught async-in-sync-transaction (xhigh/max missed it)
- xhigh caught secret-returning endpoint (max missed it)
- max was the most expensive and slowest with no improvement over xhigh

## Conclusion

- **Low-cost/high-volume audits**: MiniMax M3 ($0.07, 13/17 issues)
- **Fast Claude pass**: medium ($1.30, 13/17, <4 min)
- **Best single-pass Claude**: xhigh ($2.03, 15/17)
- **Hardest to justify**: max ($3.39, same count as xhigh, missed one xhigh finding)
- **Trend**: Cheaper models (including open-weight) are closing the gap on proprietary models at much lower cost

## Article Body

> Anthropic released Claude Opus 4.8 on May 28, 2026, and MiniMax shipped MiniMax M3 on June 1, 2026. The two models sit at very different price points, and we wanted to see how they perform compared to each other. We gave the same code audit task to Claude Opus 4.8 at four reasoning levels and to MiniMax M3, then tracked tokens, cost, time, and how many known issues each run found.
>
> TL;DR: MiniMax M3 surfaced 13 of 17 known issues for about $0.07, the same count as Claude Opus 4.8 at medium and high and two behind Claude Opus 4.8 at xhigh and max. Claude Opus 4.8 caught the most issues at its higher settings, but every run cost at least ten times more than MiniMax M3.
>
> The two models sit far apart on per-token price. Claude Opus 4.8 is about 8x higher on input and 10x higher on output. Price and performance do not always move together, so the two are worth looking at side by side rather than on their own.
>
> The codebase we audited is a webhook delivery service written in TypeScript, Bun, and SQLite. It accepts events over an HTTP API, stores them, and delivers them to subscriber URLs with signed payloads. We left known bugs in place rather than fixing them.
>
> We asked each model to review the code. Each run got the same prompt: "Treat this webhook delivery service as production-bound code and audit it for security, reliability, correctness, and test coverage, without editing any files. Write your report to audit.md."
>
> We ran Claude Opus 4.8 at four reasoning levels: medium, high, xhigh, and max. MiniMax M3 does not expose the same reasoning control, so we ran it once at its default setting.
>
> Every run used the Kilo Code CLI, each in its own session with no shared state, and we recorded the token count, cost, and wall-clock time from the CLI's run summary.
>
> MiniMax M3 used fewer tokens than any Claude Opus 4.8 run. It spent 41% fewer tokens than Claude Opus 4.8 at medium and 53% fewer than Claude Opus 4.8 at xhigh. At $0.07 it came in well under a tenth of the cheapest Claude Opus 4.8 run.
>
> Before running this test, we reviewed the codebase ourselves and cataloged 17 issues across security, reliability, correctness, and test coverage. We used that list as the answer key and counted how many of the 17 each run surfaced.
>
> Every run caught the major blockers. MiniMax M3 held its own on the more specific issues. It caught the endpoint that returned a stored secret, the delivery-list filter that dropped a condition when two filters were combined, subscriber deletion failing once delivery history exists, and the replay path accepting deliveries in the wrong state.
>
> MiniMax M3 missed three issues that the Claude Opus 4.8 runs caught. It did not flag invalid JSON returning a 500, the database setup running at import time, or an async callback running inside a synchronous transaction in the event route.
>
> Claude Opus 4.8 at xhigh and max led on coverage with 15 of 17 each. Claude Opus 4.8 at xhigh was the only run to flag the secret-returning endpoint and still cover everything else its tier caught.
>
> More reasoning did not move in one direction. Claude Opus 4.8 medium and high both flagged the async callback inside a synchronous transaction, which neither xhigh nor max mentioned. Claude Opus 4.8 at max missed the secret-returning endpoint that xhigh caught.
>
> Claude Opus 4.8 at max cost $3.39, which is 67% more than Claude Opus 4.8 at xhigh, while using slightly fewer total tokens than the xhigh run. The token total alone does not set the price. A different mix of output and cached tokens can push the bill up even when the total holds steady, and on this task that extra spend did not buy a better report.
>
> MiniMax M3 had the lowest cost per issue by a wide margin. Claude Opus 4.8 at max had the highest.
>
> MiniMax M3 sat in the middle at 5m 03s, slower than Claude Opus 4.8 at medium and high and faster than Claude Opus 4.8 at xhigh and max.
>
> One caveat on the timing: MiniMax says it plans to release the M3 weights publicly. The weights are not public today, but once they are, other inference providers can host the model, and some may run it at higher throughput than we saw here.
>
> Inside the Claude Opus 4.8 runs, higher reasoning cost more time and scaled with the tokens spent. Claude Opus 4.8 went from 3m 53s at medium to 7m 26s at xhigh, then to 9m 24s at max.
>
> The four Claude Opus 4.8 runs did not improve in a straight line as we turned the reasoning up. Medium and high both surfaced 13 of 17. Going from medium to high added only about 6% more tokens but 48% more cost. Going from high to xhigh added 17% more tokens and only 5% more cost, but it added almost three minutes and moved the count to 15. The xhigh setting was where Claude Opus 4.8 produced its best report.
>
> Max added the most cost and the most time of any run and returned the least for it here. It matched xhigh's count of 15, dropped one finding that xhigh caught, and cost 67% more.
>
> The choice here is less about which model is better and more about matching the run to the job. For low-cost or high-volume audits, MiniMax M3 is the value pick. For a more precise Claude Opus 4.8 review without the longest waits, high works. For the most thorough single pass, Claude Opus 4.8 at xhigh produced the best report. Claude Opus 4.8 at max was the hardest setting to justify on this task.
>
> The broader trend worth watching is that cheaper models, including open-weight ones, are improving quickly and getting close to proprietary models like Claude Opus at a much lower price. They are not all the way there yet. On this task MiniMax M3 matched Claude Opus 4.8 at medium and high but still came in two issues behind its higher settings. The practical approach is to test a few models on the kind of work you actually do, look at how they perform, and pick based on your requirements, budget, and how much coverage the task needs.
