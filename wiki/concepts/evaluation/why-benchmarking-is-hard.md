---
title: "Why Benchmarking Is Hard (Epoch AI) — Scaffold and Provider Variance"
created: 2026-09-09
updated: 2026-09-09
type: concept
confidence: high
tags:
  - benchmark
  - evaluation
  - methodology
  - infrastructure
  - agent-evaluation
  - agent-harness
sources:
  - https://epoch.ai/gradient-updates/why-benchmarking-is-hard
related: [agent-evaluation-methodology, scaffold-vs-rl-debate, harness-engineering, epoch-ai, florian-brand]
---

# Why Benchmarking Is Hard — Scaffold and Provider Variance

Epoch AI's Gradient Updates post ["Why benchmarking is hard"](https://epoch.ai/gradient-updates/why-benchmarking-is-hard) (Florian Brand and Jean-Stanislas Denain, Dec 23, 2025) decomposes the benchmarking pipeline and argues that **any two scores on the same benchmark are hard to compare**, because variance enters at every stage. The two dominant factors: **scaffolds** (benchmark-setup side) and **API providers** (model-access side).

## The pipeline decomposition

Epoch splits the process into two halves:

- **Benchmark Setup** — prompt template, sampling parameters, scaffold, execution environment, scoring method
- **Model Access** — SDK/API, aggregator layer, model provider

## Benchmark Setup findings

- **Even "simple" benchmarks are re-implemented differently.** GPQA-Diamond implementations differ in prompt template and default temperature across lm-evaluation-harness (temp 0.0), OpenAI simple-evals (temp 0.5), gpt-oss scripts (temp 1.0), and groq/openbench (temp 0.5). For modern reasoning models on simple benchmarks the prompt effect is small (gpt-oss: 74–80% across settings, not statistically significant given only 198 questions), but this was not always the case.
- **Scaffolds have an outsized impact on agentic evals.** Switching scaffold on SWE-bench Verified moves scores **up to 11% for GPT-5 and up to 15% for Kimi K2 Thinking**. The scaffold choice is "the single biggest impact on overall performance." Customizing a harness per model risks hill-climbing on the eval and breaks cross-model comparability. Epoch's resulting fork:
  - *Comparing models* → a standardized scaffold (e.g. mini-SWE-agent) is usually enough.
  - *Assessing frontier capabilities* → requires leading products like Claude Code.
- **Execution environments** are a moderate factor, except when broken or hackable (web-searching agents can find the dataset or re-hosting sites; banlists need continuous maintenance). OpenAI could only run 477/500 SWE-bench Verified problems in its o3/o4-mini evals due to infrastructure issues.
- **Scoring** via a second LLM (SimpleQA, tau-bench user simulator) makes the grader model itself a score-affecting choice.

## Model Access findings

- **SDK/API matters**: OpenAI reports up to 3% on SWE-bench Verified from Responses API vs ChatCompletions; **Minimax reports a 23-percentage-point tau-bench difference** between its native API and the standard ChatCompletions-compatible endpoint. Using the wrong SDK underelicits capability.
- **Aggregators** (LiteLLM, Inspect AI, OpenRouter, HF Inference Providers) add a layer that can introduce new bugs.
- **Provider is the biggest source of variance**, especially for open models: Epoch re-ran several open models on GPQA-Diamond (4-run averages, retries capped at 3, API errors scored as failures) and found provider-driven score differences for **every** model tested; provider bugs/instabilities are the largest source of evaluation errors, hitting newest models hardest.

## Position in the evaluation literature

This post is the clearest third-party statement of the **scaffold-as-confound** problem that also drives [[concepts/scaffold-vs-rl-debate]] and the harness-side analysis in [[concepts/harness-engineering]] — a benchmark score is jointly a function of model, scaffold, SDK, and provider, not of the model alone. It is cited from [[concepts/evaluation/epoch-capabilities-index]] under "underelicitation." Florian Brand ([[entities/florian-brand]]) co-authored it and has repeatedly argued from it that frontier capability reporting *should* push models as hard as possible inside real harnesses, because "models are trained and used in their harnesses."

## See Also

- [[concepts/evaluation/agent-evaluation-methodology]] — floor-raising vs benchmark-maxxing
- [[concepts/scaffold-vs-rl-debate]] — where scaffold gains come from
- [[concepts/evaluation/epoch-capabilities-index]] — Epoch's composite metric (cites this post)
- [[entities/florian-brand]] — co-author
- [[entities/epoch-ai]] — organization
