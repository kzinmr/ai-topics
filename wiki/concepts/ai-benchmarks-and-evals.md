---
title: "AI Benchmarks & Evals — Map of Content"
type: concept
aliases:
  - ai-benchmarks-moc
  - benchmarks-and-evals-moc
  - ai-benchmarks-evals-overview
  - ai-benchmarks-and-community
created: 2026-04-25
updated: 2026-06-10
tags:
  - benchmark
  - evaluation
  - model
  - comparison
  - methodology
  - ai-agents
status: active
featured: true
sources:
  - raw/articles/2025-08-03_hoeijmakers_benchmarks-to-evals-guide.md
  - raw/articles/2025-04-29_xeophon-ai-benchmark-eval-series.md
  - raw/articles/2026-05-10_fireworks-ai_ai-benchmark-lying.md
  - raw/articles/2026-05-10_cohere_ai-benchmarks-for-business.md
  - https://x.com/xeophon/status/1917175899948020203
  - https://x.com/xeophon/status/1925513059281305612
  - https://x.com/xeophon/status/1925870415173300350
  - https://x.com/xeophon/status/1927325298011287757
  - wiki/raw/articles/2025-04-29_xeophon-ai-benchmark-eval-series.md
author: Florian Brand (@xeophon) — xeophon series; Rob Hoeijmakers — benchmarks-to-evals framework
---

# AI Benchmarks & Evals — Map of Content

> **MOC**: Systematic navigation of all AI benchmark and evaluation pages in this wiki.
> Combines Hoeijmakers' Benchmarks→Evals framework with @xeophon's 18-part benchmark analysis series.
> Individual benchmark pages live in [[concepts/ai-benchmarks/index|AI Benchmarks Index]].

---

## Part A: Benchmarks vs Evals — The Core Distinction

> "Benchmarks measure **capability**. Evals measure **suitability."** — Rob Hoeijmakers

| Axis | Benchmarks (Static) | Evals (Dynamic) |
|---|---|---|
| **Purpose** | Relative comparison between models | Task-specific suitability judgment |
| **Data** | Fixed datasets | Application-specific, iteratively updated |
| **Evaluation** | Scoreboard, single metrics | Multi-dimensional (accuracy, coherence, safety) |
| **Users** | Model builders, researchers | AI teams, product developers |
| **Limitations** | Saturation, over-generalization | Design cost, subjectivity |

The question shifts from "What is the best model?" to "What is the right model for this job?" → [[raw/articles/2025-08-03_hoeijmakers_benchmarks-to-evals-guide]]

---

## Part B: @xeophon's 18 Benchmark Analyses

Comprehensive summary of Florian Brand's (@xeophon) 18-part "Popular Benchmarks / Evals" series covering design philosophy, data sourcing, and strengths/weaknesses.

### Series Overview

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

### All 18 Part Links

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

### Key Takeaways from the Series

1. **Benchmarks show relative strengths** — not absolute quality. Brand: "Benchmarks should not be taken at face value but rather show relative model strengths and general progress across fields."
2. **Data quality is everything** — Good: GPQA (expert-created), HLE (strict filtering), SWE-Bench Verified (3 annotators). Bad: ChartQA (noisy test data).
3. **Dealing with saturation** — Many benchmarks approaching ceiling: LiveCodeBench (easy problems too easy), MMLU (→MMLU Pro), SWE-Bench (80-85% plateau).
4. **New eval design trends** — Multi-turn/multi-step (BFCL V3), LLM-as-judge (Tau-Bench), personalization (Vibe-Eval), game environments (Factorio LE), human baseline emphasis (ARC-AGI 2).
5. **Benchmark retirement decisions** — Low-quality benchmarks (ChartQA) should be proactively retired.
6. **Rise of agent benchmarks** — SWE-Bench Verified as "the first (?) agentic benchmark."

---

## Part C: Benchmark Catalog (by Category)

→ Full index: [[concepts/ai-benchmarks/index|AI Benchmarks Index]]

### Knowledge & Reasoning

| Benchmark | What It Tests | Wiki Page |
|---|---|---|
| MMLU | Academic knowledge (57 subjects) | — |
| MMLU Pro | Improved MMLU (10 choices, 43% new) | [[concepts/ai-benchmarks/mmlu-pro]] |
| GPQA | Graduate-level science Q&A | [[concepts/ai-benchmarks/gpqa]] |
| HLE | Humanity's Last Exam | [[concepts/ai-benchmarks/hle]] |
| SimpleQA | Factual knowledge check | [[concepts/ai-benchmarks/simpleqa]] |
| TruthfulQA | Resistance to falsehoods | — |
| ARC | Commonsense science reasoning | — |
| ARC-AGI / 2 | Abstract fluid intelligence | [[concepts/ai-benchmarks/arc-agi-2-benchmark]] |
| BBQ | QA bias detection | — |

### Coding & Software Engineering

| Benchmark | What It Tests | Wiki Page |
|---|---|---|
| HumanEval | Python code generation | — |
| LiveCodeBench | Rolling problems (contamination-free) | [[concepts/ai-benchmarks/livecodebench]] |
| Aider Polyglot | 6-language code editing | [[concepts/ai-benchmarks/aider-polyglot]] |
| SWE-bench / Verified | Real GitHub issue resolution | [[concepts/ai-benchmarks/swe-bench]] |
| DeepSWE Benchmark | Deep SWE evaluation | [[concepts/ai-benchmarks/deepswe-benchmark]] |
| Frontier SWE Benchmark | Frontier SWE capability | [[concepts/ai-benchmarks/frontier-swe-benchmark]] |
| FrontierCode | Code quality | [[concepts/ai-benchmarks/frontiercode]] |
| Stack Benchmarking | Tech stack evaluation | [[concepts/ai-benchmarks/stack-benchmarking]] |

### Multimodal

| Benchmark | What It Tests | Wiki Page |
|---|---|---|
| MMMU | College-level multimodal understanding | [[concepts/ai-benchmarks/mmmu]] |
| ChartQA | Chart understanding | [[concepts/ai-benchmarks/chartqa]] |

### Function Calling & Instruction Following

| Benchmark | What It Tests | Wiki Page |
|---|---|---|
| BFCL V3 | Berkeley Function Calling | [[concepts/ai-benchmarks/bfcl-v3]] |
| IFEval | Instruction following | [[concepts/ai-benchmarks/ifeval]] |
| Tau-Bench | Function calling (LLM simulates users) | [[concepts/ai-benchmarks/tau-bench]] |
| Tau-Voice | Voice agent evaluation | [[concepts/ai-benchmarks/tau-voice]] |
| Tau-Knowledge | Knowledge-based evaluation | [[concepts/ai-benchmarks/tau-knowledge]] |

### Long Context & Numerical Reasoning

| Benchmark | What It Tests | Wiki Page |
|---|---|---|
| MRCR | Multi-round coreference resolution | [[concepts/ai-benchmarks/mrcr]] |
| GSM8K | Grade-school math reasoning | — |
| MATH | Competition mathematics | — |
| DROP | Discrete reasoning over paragraphs | — |
| CountBenchQA | Counting | [[concepts/ai-benchmarks/countbenchqa]] |

### Agent & Game Environments

| Benchmark | What It Tests | Wiki Page |
|---|---|---|
| Factorio LE | Factory automation via code+REPL | [[concepts/ai-benchmarks/factorio-learning-environment]] |
| Agent Survival | Agent survival under PvP pressure | [[concepts/ai-benchmarks/agent-survival-benchmark]] |
| Vending Bench | Vending machine operation | [[concepts/ai-benchmarks/vending-bench]] |
| Agent Arena | Causal tracing agent comparison | [[concepts/ai-benchmarks/agent-arena]] |

### Domain-Specific

| Benchmark | What It Tests | Wiki Page |
|---|---|---|
| Legal Agent Benchmark | Legal agent evaluation | [[concepts/ai-benchmarks/legal-agent-benchmark]] |
| GAIA | General AI assistant | [[concepts/ai-benchmarks/gaia-benchmark]] |
| FreshStack | RAG evaluation | [[concepts/ai-benchmarks/freshstack-benchmark]] |
| EQ-Bench | Emotional intelligence | — |

---

## Part D: Evaluation Methodology

### Core Frameworks

| Concept | Summary | Wiki Page |
|---|---|---|
| AI Evaluation | Manual → code-based → LLM-as-Judge | [[concepts/ai-evaluation]] |
| LM Evaluation Harness | EleutherAI's 60+ benchmark framework | [[concepts/llm-evaluation-harness]] |
| Evaluation Flywheel | Data → eval → analysis → improvement | [[concepts/evaluation-flywheel]] |
| Eval Loops | Automated quality control scoring | [[concepts/eval-loops]] |
| Offline Evaluation | Offline evaluation techniques | [[concepts/offline-evaluation]] |

### Philosophy & Debate

| Concept | Summary | Wiki Page |
|---|---|---|
| Evals vs Monitoring | Offline eval vs production monitoring | [[concepts/evals-vs-monitoring-debate]] |
| Evaluation Harness Validity | Harness design determines capability | [[concepts/evaluation-harness-validity]] |
| Benchmaxxing | Benchmark over-optimization trap | [[concepts/ai-benchmarks/benchmaxxing]] |
| AI Resistant Evaluations | AI-resistant evaluation design | [[concepts/ai-benchmarks/ai-resistant-evaluations]] |

### Agent Evaluation

| Concept | Summary | Wiki Page |
|---|---|---|
| Agent Evaluation Methodology | Agent evaluation lifecycle | [[concepts/agent-evaluation-methodology]] |
| Coding Agent Evaluation | Coding agent eval design | [[concepts/evaluation-coding-agents]] |
| Evals for AI Agents | AI agent eval practices | [[concepts/evals-for-ai-agents]] |
| Macro Evals for Agentic Systems | Large-scale agentic eval | [[concepts/macro-evals-for-agentic-systems]] |
| Infrastructure Noise in Agent Evals | Infra noise quantification | [[concepts/infrastructure-noise-agent-evals]] |
| Process Reward Models | PRM-based agent evaluation | [[concepts/process-reward-models-agent-eval]] |
| Harness Design Patterns | Multi-agent GAN loop etc. | [[concepts/agent-harness-primitives]] |

### Metrics

| Metric | Summary | Wiki Page |
|---|---|---|
| LLM-as-Judge | Automated LLM evaluation | [[concepts/llm-as-judge]] |
| Pass@k | Code generation success rate | [[concepts/ai-benchmarks/pass-k-metric]] |
| NDCG | Search ranking metric | [[concepts/ai-benchmarks/ndcg]] |

---

## Part E: Evaluation Tools & Platforms

| Tool/Platform | Summary | Wiki Page |
|---|---|---|
| Langfuse Academy | Trace → Monitor → Dataset → Experiment → Evaluate | [[concepts/ai-evaluation]] |
| LangSmith / Braintrust / Arize Phoenix | Evaluation tool comparison | [[comparisons/eval-tools-comparison]] |
| Lighteval | Hugging Face evaluation library | [[concepts/ai-benchmarks/lighteval]] |
| Galileo Eval Engineer | Evaluation engineering | [[entities/galileo-eval-engineer]] |
| Raindrop | Agent monitoring | [[concepts/evals-vs-monitoring-debate]] |
| Braintrust | Eval platform | [[concepts/evals-vs-monitoring-debate]] |

---

## Part F: Industry & Societal Context

### Benchmark Trustworthiness Issues

- **Benchmark Lying**: Fireworks AI on score manipulation → `raw/articles/2026-05-10_fireworks-ai_ai-benchmark-lying.md`
- **Business Benchmarks**: Cohere's "AI benchmarks for business" → `raw/articles/2026-05-10_cohere_ai-benchmarks-for-business.md`
- **Multilingual Fairness**: Cohere on multilingual fairness → `raw/articles/2026-05-10_cohere_towards-fair-and-comprehensive-multilingual-and-multicultural-llm-benchmarking.md`
- **Benchmark Framing**: Framing effects → tag: `benchmark-framing`
- **Mismeasure of Open Source**: Mis-measurement → [[concepts/mismeasure-of-open-source]]

### Governance & Regulation

- Regulators referencing benchmarks for compliance frameworks
- Safety, fairness, and bias contexts driving eval adoption

---

## Part G: Evolution Timeline

```
2020-2022: Static benchmark golden age (MMLU, GSM8K, HumanEval, HellaSwag)
    ↓
2023: SWE-bench arrives → first agentic benchmark
    ↓
2024: Benchmark saturation visible (MMLU→MMLU Pro, ARC→ARC-AGI 2)
     SWE-bench Verified (human-validated subset)
    ↓
2025: Evals culture rises (Langfuse Academy, Braintrust vs Raindrop debate)
     @xeophon 18-part series systematizes benchmarks
     Hoeijmakers articulates the Benchmarks→Evals shift
    ↓
2026: Agent evaluation matures
     Agent Arena (causal tracing), LAB (domain-specific)
     Benchmaxxing problem, infrastructure noise quantification
     Macro evals, process reward models
```

---

## Cross-Reference Links

- [[concepts/ai-benchmarks/index]] — Individual benchmark page index
- [[concepts/ai-evaluation]] — Evaluation methodology (Langfuse Academy)
- [[concepts/evals-vs-monitoring-debate]] — Evals vs monitoring debate
- [[concepts/evaluation-harness-validity]] — OpenAI harness design framework
- [[concepts/llm-evaluation-harness]] — EleutherAI lm-eval
- [[concepts/ai-benchmarks/benchmaxxing]] — Benchmark over-optimization
- [[concepts/agent-evaluation-methodology]] — Agent evaluation lifecycle
- [[concepts/ai-benchmarks/swe-bench]] — SWE-bench (origin of agentic benchmarks)
- [[concepts/ai-benchmarks/agent-arena]] — Agent Arena (causal inference-based)
- [[concepts/evals-for-ai-agents]] — Agent eval practices
- [[concepts/evaluation-flywheel]] — Continuous evaluation cycle
- [[entities/florian-brand]] — Florian Brand (@xeophon), series author
