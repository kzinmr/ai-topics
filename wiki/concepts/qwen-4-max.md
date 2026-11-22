---
title: "Qwen 4 Max"
type: concept
created: 2026-11-16
updated: 2026-11-22
tags:
  - model
  - qwen
  - alibaba
  - open-weight
  - reasoning
  - mixture-of-experts
  - china
sources:
  - raw/articles/2026-11-16_qwen_hn-discussion_qwen4-max.md
  - raw/articles/together.ai--blog-qwen4-max--d62cbc2a.md
  - https://news.ycombinator.com/item?id=50513215
---

# Qwen 4 Max

**Qwen4-Max** is Alibaba's flagship frontier model release of November 16, 2026, the successor line
to [[entities/qwen|Qwen]]3.8-Max (2.4T MoE) and the model the earlier Qwen3.8-Flash-Next release was
explicitly previewing architecturally. The launch hit the HN front page the same day
([594 pts / 250 comments](https://news.ycombinator.com/item?id=50513215)).

> **Confidence note**: the official `qwen.ai/blog?id=qwen4-max` page is client-side rendered and
> returned no server-side HTML to our fetcher, so the release details below are community-reported
> from the HN thread, not vendor-confirmed. Treat specs as provisional until the blog text is
> mirrored.

## What the community reported (Nov 16, 2026)

- **Serving speed is the binding constraint, not raw quality.** One developer running an agent
  "battle system" in opencode said the predecessor's poor win rate traced entirely to latency:
  "the only reason it scores so low is that it's slooooow. (Like 30 tokens per second vs opus near
  80.)" and asked that Qwen 4 "be able to serve 4 faster." A separate OpenRouter listing was cited
  where Qwen 3.8 2.4T is faster than leaderboard-reported but "doesn't handle image input".
- **Architecture preview already validated locally.** "Qwen 3.8 Flash Next [...] is supposed to be a
  preview of Qwen 4's architecture — it runs pretty solidly regardless of context window size and
  completes random deepswe challenges I throw at it locally (at Q2-Q3 quantization!)" (HN).
- **Efficiency-over-size framing.** Commenters read the release as continued focus on "efficiency
  alongside quality", with the community waiting on the smaller **Flash** and **27B** variants to
  populate the local-inference tier.

## Vendor-confirmed specs (Together AI launch post, Nov 21, 2026)

Together AI's day-0 launch post ([raw](raw/articles/together.ai--blog-qwen4-max--d62cbc2a.md)) supplies the first fetchable vendor text for Qwen4 Max and confirms the provisional architecture figures:

- **Architecture**: sparse mixture-of-experts, **2.4T total parameters / 71B active per token** — matching the community-reported 2.4T figure.
- **Capabilities**: 1M-token context window; text + image input; tool calling (multiple calls per turn); thinking on by default (billed as output tokens; disable via `reasoning={"enabled": false}`, maximize via `reasoning_effort: "max"`).
- **Alibaba's claimed benchmarks** (vendor figures, not independently verified): on **Work360** (Alibaba's benchmark of industry tasks across 721 specialized fields) Qwen4 Max outperforms Qwen3.8 Max overall, uses **35% fewer tokens at high reasoning effort**, and costs ~**60% less per task** on average.
- **Open-weight status**: Qwen4 Max itself is **closed** (serverless-only on Together AI, no fine-tuning or dedicated endpoints). Alibaba says **smaller open-weight Qwen4 series models will follow** — relevant to the local-inference "dead zone" complaint above; the community expectation of local Qwen4 variants now depends on those follow-ups.

## Together AI one-shot repo test (Nov 2026)

Together AI's launch demo is the most concrete capability evidence so far: the entire **Tornado** codebase (344 files, **652,519 tokens**) plus a symptom-only bug report in a single request — no tools, no retrieval. First token 54 s, complete patch at 72 s, ~69 cents at sale price ($1.05/$3.15 per 1M in/out; cached input $0.0525). The patch passed the maintainers' own two regression tests and the full 1,673-test suite, and the model independently cited `tornado/iostream.py`'s `BaseIOStream.write` as the in-repo precedent — the same code the maintainers cite in their actual fix. On Together AI the model is **streaming-only** (non-stream requests 400 with `streaming_required`). See [[entities/together-ai]] for full detail and pricing; caching mechanics at [[concepts/prompt-caching]].

## Why it matters

The thread crystallized a recurring 2026 open-weights gap: a "massive dead zone between 24GB and
<100GB of VRAM" where Qwen3.8-27B remains the default, with alternatives like Nemotron 3.5 74B-A9B
and various serving engines (strata, basalt, sushi) filling in. If Qwen 4 Flash inherits the
Flash-Next recipe (125B total / 6B active was the preview), the 96GB Mac Studio tier is the target
market, per several commenters.

## Related

- [[entities/qwen]] — the Qwen family (Qwen3.7-Max, 3.8-Max, 3.8-27B, Flash-Next lineage)
- [[concepts/qwen-3-8-27b]] — the 27B predecessor in the local tier
- [[concepts/qwen-covert-exfiltration-behaviour]] — the October 2026 Cohere security report on Qwen3.8-Flash-Next
- [[concepts/glm-5-3]] — Zhipu's competing open-weight frontier line
- [[concepts/deepseek-v4]] — the other Chinese frontier family

## Sources

- Qwen blog: https://qwen.ai/blog?id=qwen4-max (JS-rendered; body not captured)
- HN discussion: https://news.ycombinator.com/item?id=50513215 (594 pts)
- Together AI launch post: https://www.together.ai/blog/qwen4-max (Nov 21, 2026)
- raw: `raw/articles/2026-11-16_qwen_hn-discussion_qwen4-max.md`, `raw/articles/together.ai--blog-qwen4-max--d62cbc2a.md`
