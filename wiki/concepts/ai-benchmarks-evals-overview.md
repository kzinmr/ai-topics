---
title: AI Benchmarks & Evals Overview (xeophon Series)
type: concept
created: 2026-05-08
updated: 2026-05-08
status: active
featured: true
tags:
  - benchmark
  - evaluation
  - model
  - comparison
sources:
  - https://x.com/xeophon/status/1917175899948020203
  - https://x.com/xeophon/status/1925513059281305612
  - https://x.com/xeophon/status/1925870415173300350
  - https://x.com/xeophon/status/1927325298011287757
  - wiki/raw/articles/2025-04-29_xeophon-ai-benchmark-eval-series.md
author: Florian Brand (@xeophon)
related_entities:
  - entities/florian-brand.md
related_concepts:
  - concepts/llm-evaluation.md
  - concepts/swe-bench.md
---

# AI Benchmarks & Evals Overview

> Comprehensive summary of Florian Brand's (@xeophon) 18-part "Popular Benchmarks / Evals" series.
> Covers each benchmark's design philosophy, data sourcing methods, and strengths/weaknesses.

---

## Series Overview

| Part | Date | Benchmark | Category | Key Insight |
|------|------|-----------|----------|-------------|
| 1 | 2025-04-29 | **GPQA** | Knowledge (Science) | Bio/Physics/Chemistry only. Diamond set > main set. |
| 2 | 2025-04-30 | **LiveCodeBench** | Coding | Rolling problems stay fresh. Easy tasks bore modern LLMs. |
| 3 | 2025-05-01 | **Aider Polyglot** | Coding (Multi-lang) | 6 languages, not just Python. Rarer than expected. |
| 4 | 2025-05-02 | **MMLU Pro** | Knowledge (Multi-domain) | 43% new questions vs MMLU. LLM-assisted filtering. |
| 5 | 2025-05-05 | **MMMU** | Multimodal | Broad topics, college-level. Hand-crafted by students. |
| 6 | 2025-05-06 | **MRCR** | Long-context | Multiple needles. Improvements over NIAH. |
| 7 | 2025-05-07 | **SimpleQA** | Knowledge (Factual) | Sanity check. Important for RL-trained models. |
| 8 | 2025-05-08 | **Vibe-Eval** | Personalized | Custom prompts. Everyone should have their own. |
| 9 | 2025-05-09 | **BFCL V3** | Function Calling | Multi-turn, multi-step. Human-validated. |
| 10 | 2025-05-13 | **IFEval** | Instruction Following | Simple, tests one aspect. Easy to evaluate. |
| 11 | 2025-05-14 | **ChartQA** | Multimodal (Charts) | Noisy test data. Brand recommends retirement. |
| 12 | 2025-05-15 | **Tau-Bench** | Function Calling (Agent) | LLM simulates users. Small but powerful. |
| 13 | 2025-05-19 | **HLE** | Knowledge + Reasoning | Hardest MMLU-style. Strict filtering. |
| 14 | 2025-05-20 | **CountBenchQA** | Counting | Ultra-simple. Tests one thing well. |
| 15 | 2025-05-21 | **ARC-AGI (1)** | Abstract Reasoning | Fluid intelligence. Chollet's classic. |
| 16 | 2025-05-22 | **ARC-AGI 2** | Abstract Reasoning | Human-validated improvement. Non-human perf tanks. |
| 17 | 2025-05-23 | **SWE-Bench Verified** | Software Engineering | 3 annotators/issue. Models stuck at 80-85%. |
| 18 | 2025-05-27 | **Factorio LE** | Game-based Agent | Code+REPL interface. No vision needed. |

---

## Benchmark Categories

### Knowledge & Science
- **GPQA** — Graduate-level Google-proof Q&A. Created by experts (PhD holders/candidates). Diamond set is the most reliable subset.
- **MMLU Pro** — Improved MMLU. Expanded to 10 choices, trivial questions removed. 43% new questions.
- **SimpleQA** — Niche factual knowledge check. Useful for detecting knowledge loss in RL-trained models.
- **HLE (Humanity's Last Exam)** — The hardest MMLU-style benchmark. Strict filtering and high participation incentives.

### Coding
- **LiveCodeBench** — Regularly collects new problems from LeetCode/AtCoder/CodeForces. Contamination-free code generation eval.
- **Aider Polyglot** — Supports 6 languages, not just Python. Tests multilingual coding ability.

### Software Engineering
- **SWE-Bench Verified** — Agentic benchmark solving real GitHub issues. Human-verified subset by Ofir Press / OpenAI (500 tasks). 3 annotators per issue. Models plateau at 80-85%.

### Multimodal
- **MMMU** — College-level multimodal understanding. 6 fields, 30 subjects, 183 sub-fields. Hand-crafted by university students.
- **ChartQA** — Chart understanding. Good data but noisy test set. Retirement recommended.

### Function Calling / Instruction Following
- **BFCL V3** — Berkeley Function Calling Leaderboard V3. Multi-turn, multi-step function calling. Human-verified.
- **IFEval** — Simple instruction-following eval. Tests one aspect, easy to evaluate.
- **Tau-Bench** — Function calling test using another LLM to simulate users.

### Long Context
- **MRCR** — Multi-Round Coreference Resolution. Uses multiple needles, improving on NIAH.

### Abstract Reasoning
- **ARC-AGI (1)** — General fluid intelligence test by Francois Chollet. Abstract visual pattern reasoning. Still one of the most important benchmarks.
- **ARC-AGI 2** — Improved first version with extensive human task validation. Similar tasks but non-human performance drops sharply (showing the gap in abstract reasoning where humans excel and AI struggles).

### Counting
- **CountBenchQA** — Ultra-simple counting. Tests one thing at one level.

### Personalized
- **Vibe-Eval** — Prompt sets based on personal interests. Everyone should have their own.

### Game-based Agent
- **Factorio Learning Environment (FLE)** — An environment modeled after the Factorio game where models write code and operate via REPL. No vision needed. Fun but addictive.

---

## Key Takeaways

### 1. Benchmarks Show Relative Strengths
Brand's consistent message: "Benchmarks should not be taken at face value but rather show relative model strengths and general progress across fields." They do not measure absolute model quality.

### 2. Data Quality is Everything
- **Good examples**: GPQA (expert-created and verified), HLE (strict filtering), SWE-Bench Verified (3 annotators)
- **Bad example**: ChartQA (noisy test data, inconsistencies)

### 3. Dealing with Saturation
Many benchmarks are approaching saturation:
- LiveCodeBench: easy/medium LeetCode problems are too easy for LLMs
- MMLU: MMLU Pro was developed due to insufficient room for improvement
- SWE-Bench Verified: Models plateau at 80-85% - the remaining 15-20% is genuinely hard
- Regular problem updates (LiveCodeBench approach) is one solution

### 4. New Eval Design Trends
- **Multi-turn, multi-step**: Moving from single-turn function calls to complex dialogues, as BFCL V3 demonstrates
- **LLM-as-judge**: Using another LLM to simulate users, as in Tau-Bench
- **Personalization**: Customized evaluations like Vibe-Eval
- **Game environments**: Testing agent capabilities in immersive environments like Factorio LE
- **Human baseline emphasis**: Validating difficulty with many human participants, as in ARC-AGI 2

### 5. Benchmark "Retirement" Decisions
Benchmarks with low data quality, like ChartQA, should be proactively retired. This is important for maintaining a healthy benchmark ecosystem.

### 6. Rise of Agent Benchmarks
Positions SWE-Bench Verified as "the first (?) agentic benchmark," suggesting a shift toward testing the ability to solve real-world issues, not just write code.

---

## All 18 Part Links

| Part | Tweet URL | Benchmark |
|------|-----------|-----------|
| 1 | [link](https://x.com/xeophon/status/1917175899948020203) | GPQA |
| 2 | (in thread) | LiveCodeBench |
| 3 | (in thread) | Aider Polyglot |
| 4 | (in thread) | MMLU Pro |
| 5 | (in thread) | MMMU |
| 6 | (in thread) | MRCR |
| 7 | (in thread) | SimpleQA |
| 8 | (in thread) | Vibe-Eval |
| 9 | (in thread) | BFCL V3 |
| 10 | (in thread) | IFEval |
| 11 | (in thread) | ChartQA |
| 12 | (in thread) | Tau-Bench |
| 13 | (in thread) | HLE |
| 14 | (in thread) | CountBenchQA |
| 15 | (in thread) | ARC-AGI (1) |
| 16 | [link](https://x.com/xeophon/status/1925513059281305612) | ARC-AGI 2 |
| 17 | [link](https://x.com/xeophon/status/1925870415173300350) | SWE-Bench Verified |
| 18 | [link](https://x.com/xeophon/status/1927325298011287757) | Factorio LE |

---

## Related Pages

- [[concepts/ai-benchmarks-and-community]] - AI Benchmarks & Evals MOC (systematic navigation of all benchmark/eval pages)
- [[entities/florian-brand]] - Florian Brand (@xeophon) entity page
- [[concepts/llm-evaluation]] - LLM evaluation overview
- [[concepts/swe-bench]] - SWE-bench details
- Individual concept pages for each benchmark (created as needed)
