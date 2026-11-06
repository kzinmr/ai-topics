---
title: "Ripple-65B Preview: U.S. Open-Weight SOTA on Agentic Coding (Ricursive Intelligence)"
url: "https://www.ricursive.com/ripple"
fetched_at: 2026-11-06T12:05:00+00:00
source: "Ricursive Intelligence"
type: article
sha256: 4901d340247e9a5ace505ca43da647f7116faecb89442cb97e51bfebb4307590
---

# Ripple-65B Preview — Ricursive Intelligence

Source: https://www.ricursive.com/ripple — HN: https://news.ycombinator.com/item?id=50369925 (336 pts, 125 comments, Nov 4 2026)

Ricursive Intelligence is a full-stack AI lab building self-improving systems by co-optimizing hardware, software, and model. To power its chip-design platform, it trained a language model from scratch that it says sets a new **U.S. open-weight SOTA on agentic coding**.

## Headline claims

- Ripple-65B Preview: dense 65B-parameter general-purpose variant of the proprietary model powering Ricursive's AI chip-design platform.
- Pretrained on 12 trillion tokens; supports up to 1M context length.
- **TerminalBench 2.1: 80.52** — claimed U.S. open-weight SOTA, surpassing significantly larger US open-weight models: Reflection Beam 501B (80.1), Meta Muse Spark Open 816B (76.4), Thinking Machines Inkling 975B (63.8), NVIDIA Nemotron 3 Ultra 550B (56.4).
- Dense architecture chosen for strong reasoning with low-latency token generation; the small parameter envelope runs efficiently on local devices such as NVIDIA DGX Spark (high FLOPs, low memory bandwidth relative to datacenter accelerators).
- "Achieving U.S. Open-Weight Frontier at One-Tenth Cost" — positioned against GPT-4's >$100M and Amodei's $1B/$10–100B training-cost projections.
- Available on Hugging Face, Together AI, GMI Cloud, OpenRouter, Fireworks.

## HN discussion highlights (item 50369925, 336 pts)

- [wmf] "Congratulations I guess but it's a pretty bad look to not even mention those other open weight models." (i.e., the Chinese ones)
- [ghc] (counterpoint) "my company is restricted from doing on-prem non-US model deployment. I appreciated not having to look up where each model was from."
- [stewartpark] "the primary users of this model won't even look at 'those other open weight models' as options... (e.g. US Gov't agencies, chip design industry, etc)."
- [karmakaze] "after cherry picking models for comparison, they further cherry picked Inkling for size comparison instead of better and smaller Beam 1.0. The bar chart also shows Nemotron 3 Ultra instead of smaller and better Nemotron 3.5 Super."
- [schleck8] "Because Chinese models heavily rely on distillation and regularly behave strangely in public benchmarks... It's difficult to quantify to what extent labs like Moonshot would be competitive if they could not distill from OpenAI, now that Anthropic mostly blocks it."
- [kevmo314] "It would also be pretty difficult to quantify to what extent labs like Anthropic would be competitive if they could not distill from human knowledge."
- [xyzrt] "One making self-improving AI via AI-chip co-design, the other relying only on software for self-improving AI." (Ripple vs Kimi K3.1 Pro, per the page's positioning)
- [syntaxing] "When a post doesn't mention Qwen for comparison, you know the performance isn't going to be great."
