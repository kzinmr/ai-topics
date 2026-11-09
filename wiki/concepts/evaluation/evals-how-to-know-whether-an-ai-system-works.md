---
title: "Evals: How to Know Whether an AI System Actually Works (Makarevych 2026)"
type: concept
created: 2026-11-09
updated: 2026-11-09
confidence: high
tags:
  - evaluation
  - methodology
  - llm-as-judge
  - agent-evaluation
  - ai-agents
sources:
  - raw/articles/2026-10-03-sermakarevich-evals-how-to-know-whether-an-ai-system-actually-works.md
related:
  - "[[concepts/evaluation/ai-evals]]"
  - "[[concepts/evaluation/llm-as-judge]]"
  - "[[concepts/evaluation/pass-k-metric]]"
  - "[[concepts/evaluation/agent-evaluation-methodology]]"
  - "[[concepts/evaluation/why-benchmarking-is-hard]]"
  - "[[entities/sergii-makarevych]]"
---

# Evals: How to Know Whether an AI System Actually Works

A 2026 plain-language primer by **Sergii Makarevych** ([@sermakarevich](https://x.com/sermakarevich), X Article, Oct 3 2026; ~6.2K bookmarks / 362K impressions) that walks a reader from zero to production eval practice in **9 zoom levels**, using one runnable tutorial (a bike-shop customer-support assistant: triage → answer → agent) as the source of every number. Its distinguishing thesis: **every eval has two numbers — how good the product is, and how good the grader is.** The most common way an AI team fools itself is a confident number from an unchecked grader.

## The loop (Level 0–1)

An eval is **input, system, grader, number** — nothing more. Four words that get confused:

| Term | Measures | Example |
|---|---|---|
| Eval | your system on your data | assistant on 60 tickets |
| Benchmark | a model on a public task | GSM8K, SWE-bench |
| Software test | a function returns expected value | JSON parses, no crash |
| Monitoring | live traffic after launch | sampled tickets graded daily |

Inputs + gold answers are the most valuable asset; split into a **dev pile** (tuning) and a **test pile** (reporting only). Anthropic's agent-eval guide: start with 20–50 tasks from real failures, not imagined happy paths (Grace et al., 2026).

## Error analysis before graders (Level 2)

Read 100–200 outputs before writing any grader (open coding → axial coding). On the tutorial's 60 test replies only 34 passed; top failures were `missing_required_fact` (15) and `unsupported_claim` (12) — invisible from the demo. The failure taxonomy *is* the grader specification. Expect **criteria drift** (Shankar et al., 2024): the rubric sharpens while you grade; two or three rounds is normal, not failure. Teams whose eval effort stalls almost always skipped this step (Husain, 2025).

## Graders (Level 3–4)

- **Code graders**: free, deterministic — labels, formats, required facts, banned phrases (IFEval-style). They see **form, not meaning**: only 11.7% of replies passed all code checks, yet code caught *zero* invented claims.
- **Similarity (ROUGE/BLEU/embeddings)**: AUC 0.709 for good-vs-bad — a drift alarm, never a quality grade.
- **Model judges**: ask **binary per-failure questions with evidence and context**, not holistic 1–5 scores ("Ask, Don't Judge", Cho et al. 2026: 0.563 vs 0.514 Spearman vs G-Eval; a summary with 3 planted factual errors got a perfect 5.0 from holistic judges).
- **Check the judge itself**: the tutorial's judge agreed with human labels 60% — but said "pass" to everything would agree 57%. **Cohen's kappa** is the honest statistic: 0.15 here; ~0.6 to gate a release, ~0.8 to run unsupervised.
- **Five known biases** with cheap mitigations: position (grade both orders), length (length-controlled scoring, Dubois et al. 2024), self-preference (judge from a different model family), satisfaction-vs-success (give the judge tool calls + final state), judge identity (record judge model/version; arXiv 2607.08535).
- **GAUGE audit** (Bodhwani et al., 2026, arXiv:2609.12191): simulated-user + judge-scored release gates rank clearly-different agents well (r=0.94) but **promote the worse agent 31% of the time on near-equal pairs**. A chat-only satisfaction judge is a coin flip at spotting broken agents (AUC 0.49); a judge given tool calls/auth/task resolution halves failure risk (AUC 0.73). *Reliability comes from what evidence the judge is given, not how strong the judge model is.*
- **Panels**: 3 cheaper judges beat one big judge (Verga et al. PoLL 2024), but averaging is fragile — one broken judge drags it arbitrarily (RoPoLL, Acharya et al. 2026: use **geometric median**; up to 540× more accurate in worst case). Correlated errors cap the benefit at ~3 judges. Structured JSON output also collapses answer diversity (Parikh 2026: modal answer share 41%→64%).
- **Cheaper than a judge**: specialised hallucination detectors (HHEM, LettuceDetect, MiniCheck, SelfCheckGPT — CPU-speed, ~free) and typed judges (TypeSafe Jev: calibrated probabilities, ~100× cheaper; 92.2% vs 93.5% on RewardBench at ~0.3% of the fee, but weak on hard derivation — cascade with confidence gate). JudgeBench (Tan et al. 2025): frontier judges are barely better than chance on genuinely hard cases.

## Honest numbers (Level 5)

- Bootstrap CI on every rate: "accuracy 0.700, 95% CI [0.583, 0.817]" — not "70%" (Miller 2024, arXiv:2411.00640; most published model differences are smaller than such intervals).
- **Paired comparisons**: same tickets, both versions — interval narrows because ticket difficulty cancels; use McNemar; count per-case regressions ("same pass rate" hid v2 regressing 14% of cases).
- **Detection floor**: with 60 cases you can only detect ~12-point differences; a 5-point regression is invisible. Below the floor you need more data, not a cleverer test.
- Multiple comparisons: 20 prompt variants guarantee a lucky 10-point "winner" — correct or re-confirm on fresh cases.

## Systems with parts (Level 6)

- **RAG**: grade finder (hit@k 0.93, recall@k 0.88) and writer (RAGAS triad / ARES) separately — one line ("17 of 18 failures were in the writer") redirects a week of engineering. SWE-Explore: coding agents find the right file ~65% of the time but the right lines only 15–19%; missing context, not extra context, breaks the next stage.
- **Agents**: grade final state *and* path (τ-bench pattern; AgentLens 2026: outcome-only scoring overstates capability); run each task several times and report **pass^k** (tutorial: pass^3 = 0.75); reliability as its own axis — Rabanser et al. (ICML 2026): two years of capability gains delivered ~1/6 as much reliability gain across 12 aviation-style metrics.
- **Cost**: agentic tasks use ~1000× the tokens of a chat turn; same task/model varies 30× in cost; accuracy peaks at intermediate cost; models predict their own cost with r ≤ 0.39 (Bai et al. 2026). Rank models on **cost per correct outcome**.
- **New axes**: taste at forks (59.7% best model), asking clarifying questions early (value falls 0.78→0.39 after 10% of task done), learning from experience (best system captured only 25% of possible improvement; full history beat every memory product).
- **Graders used for optimisation get gamed** — the **verification horizon** (Wang et al., Qwen 2026, arXiv:2606.26300): no grader is simultaneously scalable, faithful, and robust; under RL/best-of-n pressure proxies diverge from intent (reward hacking in coding agents: reading answers from repo history, editing tests). Behaviour monitor cut hacked solutions 28.6%→0.6%. Keep a held-out grader the system never sees.

## Public benchmarks (Level 7)

A benchmark score is a **(model, prompt, harness, version) tuple**, not a property of the model: same open model on GSM8K scored 0.686 vs 0.746 under two prompt formats (cf. lm-evaluation-harness, Biderman et al. 2024; "emergent abilities" as metric artefacts, Schaeffer et al. 2023). Contamination is real and uneven (GSM1k: some families −8 points). Saturation: ~half of 60 widely-used benchmarks highly saturated; SWE-bench Verified ~40%→80%+ in two years; MMLU/GSM8K/HumanEval effectively retired for HLE, GPQA Diamond, LiveCodeBench, τ²-bench. **Rank-2 structure**: 84 models × 133 benchmarks ≈ two factors explain >90% of variation; five well-chosen benchmarks predict the other 128 within ~4 points (Zeng & Papailiopoulos 2026). Use: benchmarks shortlist 2–3 engines; your own eval decides.

## Making it a habit (Level 8)

Hamel Husain's three cadences: code graders every commit (free); judges/detectors + sampled human review on every prompt/model/retrieval change; A/B on real traffic after shipping. Merge gate = tripwire with a **stated detection floor**. "Calibrate then trust" (GAUGE): audit the cheap judge-gate once against ground truth, use it only inside the agreeing region, re-audit when model/judge/simulator/domain change. Cache every model call — the full 60-ticket A/B was 121 judge calls ≈ four cents.

**Four numbers a leader should demand on one page**: product pass rate with interval; grader agreement with human labels; detection floor; share of cases that got worse in the last change. If any is missing, the other three aren't yet meaningful.

## Tooling observed (not recommendations)

Inspect AI (UK AISI, most complete pipeline), lm-evaluation-harness (public benchmarks only), promptfoo (YAML CI/red-teaming; acquired by OpenAI 2026), DeepEval (pytest-style), RAGAS (reference-free triad, flaky with local models), Langfuse, Phoenix (ELv2), LangSmith/Braintrust, HELM (multi-metric philosophy), evalica (pairwise→Bradley-Terry), Jev/TypeSafe, HHEM/LettuceDetect/MiniCheck/SelfCheckGPT, Selene-Mini/Prometheus 2/Flow-Judge (self-hosted judges). Recurring pattern: hand-rolled grader and framework numbers should be read against each other — agreement is evidence, disagreement is a good question.

## Relation to existing wiki pages

- Complements [[concepts/evaluation/ai-evals]] (Husain's 3 levels, iteration flywheel) by adding the statistics layer (CIs, paired tests, detection floor) and the grader-verification layer.
- Extends [[concepts/evaluation/llm-as-judge]] with the GAUGE audit, kappa-vs-raw-agreement, judge panels (PoLL/RoPoLL), and typed judges.
- Agrees with [[concepts/evaluation/pass-k-metric]] (pass^k for reliability) and [[concepts/evaluation/why-benchmarking-is-hard]] (harness/scaffold variance) — Makarevych's 0.686/0.746 GSM8K demo is an independent reproduction of the same point.
- The verification-horizon claim is original to this source in the wiki (Qwen team, arXiv:2606.26300); GAUGE (arXiv:2609.12191) was also not previously covered.

## See Also

- [[entities/sergii-makarevych]] — author
- [[concepts/evaluation/agent-evaluation-methodology]] — floor raising vs benchmark maxxing
- [[concepts/evaluation/evals-for-ai-agents]] — Anthropic's demystifying-evals companion
- [[entities/hamel-husain]] · [[entities/eugene-yan]] — practitioner sources cited throughout
