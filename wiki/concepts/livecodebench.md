---
title: "LiveCodeBench"
type: concept
created: 2026-05-08
updated: 2026-05-08
status: active
tags:
  - benchmark
  - evaluation
  - coding
  - code-generation
  - contamination-free
  - programming
aliases:
  - livecodebench
  - lcb
  - "LiveCodeBench"
sources:
  - https://arxiv.org/abs/2403.07974
  - https://livecodebench.github.io/
  - https://github.com/LiveCodeBench/LiveCodeBench
  - wiki/raw/articles/2025-04-29_xeophon-ai-benchmark-eval-series.md
related_entities:
  - entities/florian-brand.md
related_concepts:
  - concepts/ai-benchmarks-evals-overview.md
  - concepts/llm-evaluation.md
  - concepts/aider-polyglot.md
  - concepts/swe-bench.md
---

# LiveCodeBench

> **Part 2 of @xeophon's 18-part AI Benchmarks & Evals series.** A contamination-free, continuously-updated coding benchmark that pulls fresh problems from competitive programming platforms (LeetCode, AtCoder, CodeForces) every few months — ensuring models are tested on genuinely unseen code.

**Paper**: [arXiv 2403.07974](https://arxiv.org/abs/2403.07974) (Mar 2024, ICLR 2025 Poster) | **Authors**: Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, Ion Stoica (UC Berkeley, MIT, Cornell)

---

## What It Measures

LiveCodeBench evaluates LLMs on **code-related capabilities** beyond mere code generation. It defines four evaluation scenarios:

| Scenario | Description |
|----------|-------------|
| **Code Generation** | Given a problem statement, produce a correct program that passes all test cases |
| **Self-Repair** | Given a problem + a buggy solution + execution feedback, fix the code to pass tests |
| **Test Output Prediction** | Given code + input, predict the output without execution |
| **Code Execution** | Given code + input, predict execution behavior (correct output, error type, etc.) |

Problems are sourced from **three competitive programming platforms**:
- **LeetCode** — Algorithm and data structure problems (easy, medium, hard)
- **AtCoder** — Japanese competitive programming contests
- **CodeForces** — International competitive programming platform

---

## Data Sourcing Method

LiveCodeBench's defining feature is its **contamination-free, rolling-update design**:

1. **Continuous collection**: New problems are harvested from platform contests every few months
2. **Release-date annotation**: Every problem is tagged with its original publication date
3. **Time-segmented evaluation**: Models are evaluated only on problems released AFTER their training cutoff date — ensuring no data contamination
4. **Automatic verification**: Solutions are validated against platform test cases (not human judgment)
5. **Growing dataset**: Started with ~400 problems (May 2023–May 2024); expanded to 600+ by Aug 2024 and continues growing

This approach also enables **contamination detection**: If a model performs significantly worse on post-cutoff problems than pre-cutoff problems, it's evidence of training data contamination. The paper notably found that DeepSeek models exhibited sharp performance drops on LeetCode problems released after their training date.

---

## Key Numbers

| Metric | Value |
|--------|-------|
| **Initial dataset** | 400+ problems (May 2023–May 2024) |
| **Expanded dataset** | 600+ problems (May 2023–Aug 2024) |
| **Problem sources** | LeetCode, AtCoder, CodeForces |
| **Scenarios** | 4 (code gen, self-repair, test output prediction, code execution) |
| **Models evaluated** | 50+ (as of ICLR 2025) |
| **Languages** | Primarily Python (competition standard) |
| **Contamination-free** | Yes — time-segmented by release date |

### Key Findings from Paper

- **HumanEval overfitting detected**: Many open-source fine-tuned models score well on HumanEval but underperform on LCB-Easy problems of similar difficulty — evidence of benchmark overfitting
- **Open vs closed gap**: Closed API-access models generally outperform open models; only fine-tuned 30B+ parameter open models compete
- **Claude-3-Opus vs GPT-4-turbo**: Opus overtakes GPT-4-turbo on test output prediction but not code generation — different models have different coding strengths
- **DeepSeek contamination detected**: Performance drops on post-release-date LeetCode problems reveal training data contamination

---

## @xeophon's Key Insights

From the Part 2 analysis (Apr 30, 2025):

1. **Rolling problems keep it fresh**: The continuous-update model is one of the best approaches to combating benchmark saturation and contamination
2. **Modern LLMs are bored with easy/medium LeetCode**: Today's frontier models find standard algorithmic tasks trivial — the benchmark's difficulty needs to keep pace with model capabilities
3. **Contamination-free by design**: Time-segmented evaluation is a robust, principled approach that also serves as a contamination detection tool
4. **Goes beyond code generation**: The multi-scenario design (self-repair, execution prediction) tests a broader range of coding capabilities than traditional benchmarks
5. **Still limited to competition-style problems**: Doesn't cover real-world software engineering tasks like those in SWE-Bench

---

## Strengths

- **Truly contamination-free**: Time-segmented evaluation with release-date tracking is the gold standard for preventing data leakage
- **Continuously updated**: New problems prevent saturation — the benchmark stays relevant as models improve
- **Contamination detection**: Can identify models that were trained on benchmark data
- **Holistic evaluation**: Four distinct scenarios test different aspects of code capability
- **Objective scoring**: Automatic verification via test cases — no human or LLM judging needed
- **Multi-platform sourcing**: Three diverse problem sources reduce platform-specific biases
- **Open leaderboard**: Community submissions accepted via GitHub PR

---

## Weaknesses

- **Competition-style only**: All problems are algorithmic contest problems — no real-world software engineering (repos, PRs, debugging real codebases)
- **Python-centric**: Competition platforms standardize on Python; limited multi-language evaluation
- **Difficulty ceiling**: Easy/medium problems are already saturated for frontier models
- **Test case dependency**: Quality depends on the test suites provided by platforms
- **No agentic capability**: Tests code generation, not the full agentic loop of understanding issues, navigating codebases, and deploying fixes (cf. SWE-Bench)
- **Single-file solutions**: Problems expect self-contained solutions, not multi-file projects

---

## Relationship to Other Benchmarks

| Benchmark | Focus | Contamination Handling |
|-----------|-------|----------------------|
| **LiveCodeBench** | Competition coding (multi-scenario) | Time-segmented, continuous updates |
| **HumanEval** | Basic function completion | Static — known overfitting issues |
| **MBPP** | Basic Python programming | Static |
| **Aider Polyglot** | Multi-language code editing | Static (225 Exercism exercises) |
| **SWE-Bench Verified** | Real-world GitHub issue resolution | Human-verified subset |
| **CodeForces** | Competitive programming Elo | Native platform rating |

---

## Related Pages

- [[concepts/ai-benchmarks-evals-overview]] — Full 18-part benchmark series overview
- [[entities/florian-brand]] — Florian Brand (@xeophon), series author
- [[concepts/aider-polyglot]] — Aider Polyglot (multi-language coding)
- [[concepts/swe-bench]] — SWE-Bench (real-world software engineering)
- [[concepts/llm-evaluation]] — LLM evaluation landscape

---

## Sources

1. Jain et al., "LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code," arXiv:2403.07974, Mar 2024 (ICLR 2025 Poster). https://arxiv.org/abs/2403.07974
2. LiveCodeBench Official Website. https://livecodebench.github.io/
3. LiveCodeBench GitHub Repository. https://github.com/LiveCodeBench/LiveCodeBench
4. LiveCodeBench HuggingFace Data. https://huggingface.co/livecodebench/
5. @xeophon (Florian Brand), "AI Benchmarks & Evals Series, Part 2: LiveCodeBench," Apr 30, 2025.
