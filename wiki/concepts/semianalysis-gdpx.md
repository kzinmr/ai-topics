---
title: "SemiAnalysis GDPx — professional-task benchmark"
created: 2026-11-10
updated: 2026-11-26
type: concept
tags:
  - benchmark
  - evaluation
  - evals
  - labor
  - domain-expertise
  - semianalysis
sources:
  - raw/newsletters/2026-11-10-spotify-s-claude-code-token-trick-tested-the-real-savings.md
  - raw/newsletters/2026-11-26-semianalysis-gdpx-full-body.md
  - https://newsletter.semianalysis.com/p/evaluating-recent-model-releases
  - https://www.aibyaakash.com/p/spotifys-90-trick
---

# SemiAnalysis GDPx — professional-task benchmark

**GDPx** is a **SemiAnalysis** evaluation that gives frontier models **real tasks from 11 professional fields** — including chip design, law, and finance — rather than academic or code-competition style problems.

## Headline result

As reported in November 2026, **the best model, Claude Opus 5.5, scored just 12%**. Jack Clark-style framing ("AI still struggles at real professional work") is the natural reading: even the top frontier model completes professional-grade work at a level far below what an expert in the field would produce. See [[concepts/evaluation/ai-evals]], [[concepts/claude/opus-5]].

## Methodology

GDPx launched **November 1, 2026** with an explicit design thesis: AI's economic impact is unevenly distributed, so a frontier-progress benchmark should weight **the domains where models will actually be most impactful** rather than chasing GDP-share or O*NET taxonomies (the approach SemiAnalysis criticizes in GDPVal and Agent's Last Exam). Consequences of that thesis:

- **Government and real estate are intentionally excluded** as domains where frontier capability is not yet economically load-bearing.
- **14 specialized data partners** produced **206 tasks**, each meant to be genuinely representative of its field.
- Runs are executed at the **highest reasoning level** and across all domains.

The headline property is **difficulty headroom**: while most benchmarks debut with the top model above 50%, GDPx's founding top score was 12% (Opus 5.5). SemiAnalysis argues this gap is precisely what lets GDPx keep discriminating between future releases, unlike saturated suites such as Terminal Bench 4.0 (which it treats as no longer informative).

## Official results (Nov 26, 2026 update)

First SemiAnalysis-published leaderboard update since launch, covering the wave of releases since Nov 1: OpenAI's [[entities/openai-astra|GPT-6.2 Astra/Sol]], Anthropic's [[concepts/claude/fable-5|Fable 5.2]], the [[concepts/gemini/gemini-4-carbon|Gemini 4]] series, plus Alibaba and Moonshot.

### Main leaderboard (all domains, binary grading)

| Rank | Model | GDPx score |
|------|-------|-----------|
| 1 | **GPT-6.2 Astra** | **19.3%** |
| 2 | Claude Fable 5.2 | 16.4% |
| 3 | GPT-6.2 Sol | 11.5% |
| 5 | Gemini 4 Carbon | 10.9% |
| 6 | Gemini 4 Neon | 10.1% |
| — | Qwen4-Max (best Chinese model) | 7.44% |

**OpenAI is the current king of GDPx**, and per SemiAnalysis it also **completely dominates the cost-performance Pareto frontier** — only DeepSeek v4.1 Flash barely registers at the low-cost corner. The main leaderboard covers all domains including cyber/bio/alignment, where safety classifiers can suppress a model's apparent capability.

### Classifier-adjusted view

SemiAnalysis presents a second, defensible leaderboard: **excluding cyber, biology, and alignment** (the three domains where safety classifiers fire) and switching the notoriously hard legal and finance domains from binary to **partial grading**. On that view the OpenAI–Anthropic gap nearly closes: **GPT-6.2 Astra 32.2% vs Fable 5.2 29.9%**. The page deliberately leaves both readings open — classifiers genuinely limit real-world usefulness in cyber/bio, but refusing a task is a poor proxy for measuring raw intelligence. (6.2 Astra's classifier is also judged weaker than GPT-6 Astra's.)

### Per-domain highlights

- **GPT-6.2 Astra** is strongest in complex-reasoning domains — chip design, hardware design, materials science, RSI. It is the **first model ever to exceed 0% on legal** and is **SOTA on finance**. Its weakness is **software engineering**, where it scores **half of Fable 5.2's** — notably, SWE is precisely the domain the X/Twitter crowd ranks models on, which explains the sentiment/measurement split. Astra also **outperforms Fable 5.2 on RSI, 33.22% vs 24.13%**, which SemiAnalysis attributes to Anthropic **explicitly nerfing AI-research capability** in public models.
- **Fable 5.2** dominates **chip design, software engineering, and quant trading**. SWE is its standout: **24.4%**, nearly tripling Opus 5.5 (8.9%) and well ahead of GPT-6.2 Sol (15.6%). With partial grading its finance score (53.6%) is effectively tied with Opus 5.5 (54.6%) and Astra (53.5%).
- **Gemini 4 Neon** is the top biology model — probably because OpenAI/Anthropic refuse bio tasks more often — but remains decisively behind Anthropic and OpenAI across virtually all frontier domains.

### Cost & token economics

Fable 5.2 is by far the most expensive model to run: **$88 and 1.23M output tokens per task**, i.e. **1.9× the cost and 3.9× the output tokens of GPT-6.2 Astra for a lower score**. SemiAnalysis attributes the spend to Fable 5.2's persistence and its habit of spawning subagents for testing/review.

- **Materials science** is the starkest case: Fable 5.2 costs 2× Astra per task and uses 3.7× the output tokens yet scores **19 points lower (21.8% vs 41.3%)**; even GPT-6.2 Sol beats it (25.8%) at roughly a tenth of the cost ($8 vs $79/task).
- **Finance**: Fable 5.2 is tied with Astra on score but uses **12× the output tokens**, making it **6.6× more expensive per task**.
- **Neon's run cost was $15,286**, inflated by Google's lagging prompt caching. Matching Opus 5.5's cache hit rate would have made it $12,536 (−18%), and Astra's $10,403 (−32%). Google shipped a caching update the same day (+4.5% cache hit), and SemiAnalysis expects the gap to keep closing since improving inference serving stacks is something models are becoming superhuman at. See [[concepts/prompt-caching]], [[concepts/token-economics]].

### Perception vs measurement

The section's most quotable argument is that **X/Twitter sentiment inverted the actual leaderboard**: public reception of 6.2 Astra was "embarrassingly bad" — one influencer called it "the worst model OpenAI has ever released" — while Gemini 4 Neon was hailed as the model of the moment, with some declaring it the single best model in the world.

SemiAnalysis's rebuttal has two parts. First, the Astra contradiction resolves once you look at domains: its log-perplexity dropped significantly (OpenAI's recently-disclosed proxy for pretraining intelligence and sample efficiency), and it wins on hard-reasoning tasks — it is simply bad at the software-engineering tasks that dominate public evaluation. Second, **Gemini 4 Neon's popularity is judged to be driven by model behavior rather than intelligence**: SemiAnalysis characterizes it as "a pleasant model to talk to", whose liberal exclamation marks and cheerfulness recall **GPT-4o**, another beloved model. Qualitatively, Astra is described as too literal, failing to infer intent or make reasonable assumptions, and "annoying to talk to" — i.e. OpenAI's 6.2 line is extremely capable but needs work on pleasantness. (The same steerability/over-clarification failure mode is logged with a concrete Theo Browne example in [[entities/openai-astra]].)

### Ecosystem tiering

SemiAnalysis's race read: **Anthropic and OpenAI are clearly in a tier of their own; Google is a distant third but deserves its own tier; Meta, SpaceX, Moonshot and Alibaba are fighting for 4th.** Notably, SemiAnalysis explicitly retracts its earlier newsletter predicting the demise of Gemini/DeepMind — model progress there "inflected up" over the prior months.

### Chinese frontier models

- **Qwen4-Max leads the Chinese cohort at 7.44%** — slightly below Claude Sonnet 5.5 but significantly cheaper; its biggest gains over Qwen3.8 are in software engineering, RSI, cyber, and bio. See [[concepts/qwen-4-max]].
- **Kimi K3.1 Pro underperforms on GDPx** relative to its Artificial Analysis Intelligence Index standing, because it is **benchmaxxed on Terminal Bench 4.1** (10% of the AA index). It is #1 on Terminal Bench "unironically", while GDPx shows it still trailing Fable 5.2, Gemini 4 Neon and 6.2 Astra. A clean case study for [[concepts/ai-benchmarks/benchmaxxing]]. See [[concepts/kimi-k3]].

### Domain-specific cyber models

Because the major labs keep tightening safety classifiers (getting unmitigated cyber/bio access from any provider is described as "extremely non-trivial"), **domain-specific post-trained models are becoming materially more relevant**. Evaluated: Hinoki's cyber post-train of DeepSeek v4.1 Flash ("HO1") and abliterated Kimi K3.1 Pro / DeepSeek v4.1 Flash from Boundless. Counter-intuitively, **both abliterated models scored slightly worse than their vanilla open-weight counterparts**, while HO1 was marginally better — because the vanilla OSS models never refused the cyber tasks in the first place. Inference for Kimi K3.1 Pro was provided by Modal.

## Why it matters

The number is a useful counterweight to benchmark-driven capability claims. Frontier models post near-ceiling scores on software-engineering and math suites while performing poorly on open-ended professional deliverables, which is the same pattern as the **METR** differential-acceleration result — acceleration is lumpy and domain-specific rather than uniform (see [[entities/metr]], [[concepts/ai-discovery-acceleration]]). For the labor-displacement debate, the load-bearing question is exactly this gap between verifiable benchmark tasks and legible professional work, see [[concepts/labor-economics]] and [[concepts/ai-adoption-barbell]].

The 12% figure should be read as a specific task-set result, not a general "AI is 12% as good as professionals" claim; per-field breakdowns and task definition are the parts that decide what it licenses.

## Related

- [[concepts/evaluation/ai-evals]] — evaluation methodology
- [[entities/anthropic]] — provider of the top-scoring model
- [[entities/metr]] — independent capability assessment org
- [[concepts/recursive-self-improvement]] — verifier-availability argument: professional deliverables lack the fast verifiers that make benchmark progress meaningful
- [[entities/openai-astra]] — GPT-6.2 Astra, #1 on the Nov 26 leaderboard
- [[concepts/claude/fable-5]] — Fable 5.2, #2 and the most expensive model per task
- [[concepts/gemini/gemini-4-neon]] — the model whose reception GDPx disputes
- [[concepts/qwen-4-max]] / [[concepts/kimi-k3]] — the Chinese frontier cohort
- [[concepts/ai-benchmarks/benchmaxxing]] — GDPx as an anti-benchmaxxing instrument

## Sources

- Aakash Gupta, ["Spotify's Claude Code Token Trick, Tested"](https://www.aibyaakash.com/p/spotifys-90-trick), *AI by Aakash*, Nov 9, 2026 — reporting SemiAnalysis's new GDPx test.
- SemiAnalysis, ["Evaluating Recent Model Releases on GDPx"](https://newsletter.semianalysis.com/p/evaluating-recent-model-releases), Nov 26, 2026 — first official leaderboard. Full body: `raw/newsletters/2026-11-26-semianalysis-gdpx-full-body.md`.
