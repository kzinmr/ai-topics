# AI Topics Hot Post — 2026-10-26 morning (09:30 JST)

> Discord delivery translated to Japanese per report-quality skill; wiki archive stays English per wiki language policy.

## 🏆 Kimi K3.1 Pro — AA 55 vs Opus 5.5's 58, at exactly half the price

**▶ One-liner**: The open-weight vs closed frontier gap is no longer "6 months" but "9 days" — K3.1 Pro at AA 55, $2/$10, sitting between GPT-6.1 Sol ($2/$10) and Claude Opus 5.5 ($4/$20), with weights promised Nov 4.

**Details**:
- Artificial Analysis score **55**. Only Claude Opus 5.5 (**58**) above it. Below: Claude Fable 5.1 / GPT-6 Astra / Gemini 4 Argon (**all 53**). First time a soon-to-be open-weight model scored this high against the frontier ([[entities/simon-willison]] link post, Oct 23; HN 939pts).
- Price **$2.00/M input · $10/M output** = same as GPT-6.1 Sol, half of Claude Opus 5.5. Highspeed variant is 2–3× faster at 2× the price (cache-hit inputs priced the same). Sources: [Simon Willison — Introducing Kimi K3.1 Pro](https://simonwillison.net/2026/Oct/23/kimi-k31-pro/) (raw: `wiki/raw/articles/simonwillison.net--2026-oct-23-kimi-k31-pro--a41c8d02.md`), [[comparisons/llm-api-pricing]], [[entities/gpt-6-1-sol]], [[events/claude-opus-5-5-gpt-6-release-sep-2026]].
- Weights are still private — Moonshot's promise: **"Full model weights will be released by Nov 4, 2026."** API-first to prove quality, then drop to OSS on Nov 4. A two-stage play.

| Model | AA | $/M in | $/M out | Release state |
|---|---|---|---|---|
| Claude Opus 5.5 | 58 | $4 | $20 | closed |
| **Kimi K3.1 Pro** | **55** | **$2** | **$10** | API; weights promised Nov 4 |
| GPT-6 Astra | 53 | $10 | $50 | closed |
| Claude Fable 5.1 / Gemini 4 Argon | 53 | — | — | closed |

**Deep dive — testing the "gap closed" thesis**:
- [[concepts/open-weight-vs-closed-llm-gap]]: Doubleword (Jamie Dborin, 2026-06-22) linear extrapolation projected the open/closed gap reaching **0 around 2026-12-03** (HN 299pts). K3.1 Pro beats that forecast by 9 days.
- The same period was a headwind for open weights: Meta fully dropped weights for the new Muse Spark models; Alibaba (Qwen) shifted to API-first releases ([[concepts/open-weights-licensing-tightening]]). The lab that closed the gap is China's Moonshot, while incumbent open-weight suppliers retreat — a new configuration for the "Intelligence" front of [[concepts/us-china-ai-competition]].
- Watch the price discontinuity vs the previous generation. K3 launched July 2026 at **$3/$15** — "the most expensive model from a Chinese provider to date" ([[concepts/kimi-k3]]). Three months later K3.1 Pro undercuts it to **$2/$10**. China's price floor is now cutting below its own previous ceiling ([comparisons/llm-api-pricing "China's Price Floor Is Sub-Floor" section](https://github.com/kzinmr/ai-topics/blob/master/wiki/comparisons/llm-api-pricing.md)).
- Counter-signal on record: a 3pt AA scalar gap is within harness-noise range. GPT-6 Astra measured **62.7% vs 99.9%** on ARC-AGI-3 depending on harness — a 37pt swing on the same model ([[concepts/ai-benchmarks/arc-agi-3]] / [[concepts/ai-benchmarks/benchmaxxing]]). Moonshot's own benchmarks put K3.1 Pro roughly level with Opus 5.5 and GPT-6 Astra, but third-party reproduction is still ahead.
- Confidence the Nov 4 date holds: ~50%. If it slips, the story flips to "API-only frontier goes permanent." Worth re-checking on Nov 4.

**Next move**: if weights land, open `concepts/kimi-k3-1-pro` and verify whether KDA (6.3× decoding), AttnRes (~25% training efficiency) and LatentMoE (16-of-896 experts active) carry over ([[entities/moonshot-ai]]).
