---
title: "AI Benchmarks & Evals — Map of Content"
type: concept
aliases:
  - ai-benchmarks-moc
  - benchmarks-and-evals-moc
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
---

# AI Benchmarks & Evals — Map of Content

> **MOC**: Systematic navigation of all AI benchmark and evaluation pages in this wiki.
> Uses Hoeijmakers' framework as the backbone, charting the evolution from static benchmarks to dynamic evals to agent evaluation.

---

## 1. Benchmarks vs Evals: The Core Distinction

> "Benchmarks measure **capability**. Evals measure **suitability."** — Rob Hoeijmakers

| Axis | Benchmarks (Static) | Evals (Dynamic) |
|---|---|---|
| **Purpose** | Relative comparison between models | Task-specific suitability judgment |
| **Data** | Fixed datasets | Application-specific, iteratively updated |
| **Evaluation** | Scoreboard, single metrics | Multi-dimensional (accuracy, coherence, safety) |
| **Users** | Model builders, researchers | AI teams, product developers |
| **Limitations** | Saturation, over-generalization | Design cost, subjectivity |

Hoeijmakers identifies a shift in the LLM era: the question moves from "What is the best model?" to "What is the right model for this job?" → [[raw/articles/2025-08-03_hoeijmakers_benchmarks-to-evals-guide]]

---

## 2. Benchmark Catalog

### 2.1 Knowledge & Reasoning

| Benchmark | What It Tests | Notes | Wiki |
|---|---|---|---|
| **MMLU** | Academic knowledge across 57 subjects | Static, broad | — |
| **MMLU Pro** | Improved MMLU (10 choices, 43% new) | Anti-saturation | [[concepts/mmlu-pro]] |
| **GPQA** | Graduate-level science Q&A | Expert-created, Diamond set recommended | [[concepts/gpqa]] |
| **HLE** | Humanity's Last Exam | Hardest MMLU-style, strict filtering | [[concepts/hle]] |
| **SimpleQA** | Factual knowledge check | Detects knowledge loss after RL training | — |
| **TruthfulQA** | Resistance to falsehoods | Oxford & OpenAI | — |
| **ARC** | Commonsense science reasoning | Allen AI | — |
| **ARC-AGI / 2** | Abstract fluid intelligence | Chollet, human-validated | [[concepts/arc-agi-2-benchmark]] |
| **BBQ** | QA bias detection | Demographic bias assessment | — |

### 2.2 Coding & Software Engineering

| Benchmark | What It Tests | Notes | Wiki |
|---|---|---|---|
| **HumanEval** | Python code generation | OpenAI | — |
| **LiveCodeBench** | Rolling problems (LeetCode/AtCoder) | Contamination-free | [[concepts/livecodebench]] |
| **Aider Polyglot** | 6-language coding | Beyond Python | — |
| **SWE-bench / Verified** | Real GitHub issue resolution | First agentic benchmark, plates at 80-85% | [[concepts/swe-bench]] |
| **SWE-bench Agent Scaffolding** | SWE-bench harness design | Agent design impact analysis | [[concepts/swe-bench-agent-scaffolding]] |
| **DeepSWE Benchmark** | Deep SWE evaluation | DataCurve | [[concepts/deepswe-benchmark]] |
| **Frontier SWE Benchmark** | Frontier SWE capability | — | [[concepts/frontier-swe-benchmark]] |
| **FrontierCode** | Code quality (slop avoidance) | — | [[concepts/frontiercode]] |
| **Stack Benchmarking** | Ramp's tech stack evaluation | Production-oriented | [[concepts/stack-benchmarking]] |

### 2.3 Multimodal

| Benchmark | What It Tests | Notes | Wiki |
|---|---|---|---|
| **MMMU** | College-level multimodal understanding | 6 fields, 30 subjects, student-crafted | — |
| **ChartQA** | Chart understanding | Noisy, retirement recommended | — |

### 2.4 Function Calling & Instruction Following

| Benchmark | What It Tests | Notes | Wiki |
|---|---|---|---|
| **BFCL V3** | Berkeley Function Calling | Multi-turn, multi-step | — |
| **IFEval** | Instruction following | Simple, easy to evaluate | [[concepts/ifeval]] |
| **Tau-Bench** | Function calling (LLM simulates users) | Small but powerful | [[concepts/tau-bench]] |
| **Tau-Voice** | Voice agent evaluation | Tau-Bench derivative | [[concepts/tau-voice]] |
| **Tau-Knowledge** | Knowledge-based evaluation | Fintech domain | [[concepts/tau-knowledge]] |

### 2.5 Long Context & Numerical Reasoning

| Benchmark | What It Tests | Notes | Wiki |
|---|---|---|---|
| **MRCR** | Multi-round coreference resolution | Multiple needles, NIAH improvement | — |
| **GSM8K** | Grade-school math reasoning | OpenAI | — |
| **MATH** | Competition mathematics | OpenAI | — |
| **DROP** | Discrete reasoning over paragraphs | Allen AI | — |
| **CountBenchQA** | Counting | Ultra-simple | — |

### 2.6 Agent & Game Environments

| Benchmark | What It Tests | Notes | Wiki |
|---|---|---|---|
| **Factorio LE** | Agent in Factorio-like game environment | Code + REPL, no vision needed | [[concepts/factorio-learning-environment]] |
| **Agent Survival** | Agent survival under PvP pressure | Aggressiveness does not predict victory | [[concepts/agent-survival-benchmark]] |
| **Vending Bench** | Vending machine operation task | — | [[concepts/vending-bench]] |
| **Agent Arena** | Agent comparison via causal tracing | Arena AI, RCT design | [[concepts/agent-arena]] |

### 2.7 Domain-Specific

| Benchmark | What It Tests | Notes | Wiki |
|---|---|---|---|
| **Legal Agent Benchmark** | Legal agent evaluation | Harvey AI | [[concepts/legal-agent-benchmark]] |
| **GAIA** | General AI assistant | — | [[concepts/gaia-benchmark]] |
| **FreshStack** | RAG evaluation | Hamel Husain | [[concepts/freshstack-benchmark]] |
| **EQ-Bench** | Emotional intelligence in dialogue | Hugging Face & LAION | — |

### 2.8 Search & RAG

| Benchmark | What It Tests | Notes | Wiki |
|---|---|---|---|
| **Natural Questions (NQ)** | Real-world Q&A | Google AI | — |
| **NDCG** | Search ranking quality | — | [[concepts/ndcg]] |
| **BEIR / MTEB** | Search & embedding evaluation | — | — |

---

## 3. Evaluation Methodology

### 3.1 Core Frameworks

| Concept | Summary | Wiki |
|---|---|---|
| **AI Evaluation** | 3-layer approach: manual → code-based → LLM-as-Judge | [[concepts/ai-evaluation]] |
| **LLM Evaluation** | Systematic LLM evaluation overview | [[concepts/llm-evaluation]] |
| **LM Evaluation Harness** | EleutherAI's 60+ benchmark unified framework | [[concepts/llm-evaluation-harness]] |
| **Evaluation Flywheel** | Data collection → evaluation → analysis → improvement cycle | [[concepts/evaluation-flywheel]] |
| **Eval Loops** | Automated quality control scoring | [[concepts/eval-loops]] |
| **Offline Evaluation** | Offline evaluation techniques | [[concepts/offline-evaluation]] |

### 3.2 Metrics & Methods

| Concept | Summary | Wiki |
|---|---|---|
| **LLM-as-Judge** | Automated LLM evaluation, requires calibration | [[concepts/llm-as-judge]] |
| **Pass@k** | Code generation success rate | [[concepts/pass-k-metric]] |
| **NDCG** | Search ranking metric | [[concepts/ndcg]] |

### 3.3 Philosophy & Debate

| Concept | Summary | Wiki |
|---|---|---|
| **Evals vs Monitoring Debate** | Offline eval vs production monitoring | [[concepts/evals-vs-monitoring-debate]] |
| **Evaluation Harness Validity** | Harness design determines capability visibility | [[concepts/evaluation-harness-validity]] |
| **Benchmaxxing** | Benchmark over-optimization trap | [[concepts/benchmaxxing]] |
| **AI Benchmarks & Evals Overview** | @xeophon 18-part series | [[concepts/ai-benchmarks-evals-overview]] |
| **AI Resistant Evaluations** | AI-resistant evaluation design | [[concepts/ai-resistant-evaluations]] |

### 3.4 Agent Evaluation

| Concept | Summary | Wiki |
|---|---|---|
| **Agent Evaluation Methodology** | Agent evaluation lifecycle | [[concepts/agent-evaluation-methodology]] |
| **Coding Agent Evaluation** | Coding agent evaluation design | [[concepts/evaluation-coding-agents]] |
| **Evals for AI Agents** | AI agent eval practices | [[concepts/evals-for-ai-agents]] |
| **Evals Skills for Coding Agents** | Coding agent eval skills | [[concepts/evals-skills-for-coding-agents]] |
| **Macro Evals for Agentic Systems** | Large-scale agentic eval | [[concepts/macro-evals-for-agentic-systems]] |
| **Infrastructure Noise in Agent Evals** | Quantifying infra noise impact | [[concepts/infrastructure-noise-agent-evals]] |
| **Process Reward Models** | PRM-based agent evaluation | [[concepts/process-reward-models-agent-eval]] |
| **Harness Design Patterns** | Multi-agent GAN loop etc. | [[concepts/harness-design-multi-agent-gan-loop-context-reset-sprint-contracts-evaluator-pattern]] |
| **Generator-Evaluator Pattern** | Generate-evaluate pattern | [[concepts/generator-evaluator-pattern]] |

---

## 4. Evaluation Tools & Platforms

| Tool/Platform | Summary | Wiki |
|---|---|---|
| **Langfuse Academy** | Trace → Monitor → Dataset → Experiment → Evaluate | [[concepts/ai-evaluation]] |
| **LangSmith / Braintrust / Arize Phoenix** | Evaluation tool comparison | [[concepts/evaluation-tools-langsmith-braintrust-arize-phoenix-inspect-ai]] |
| **Lighteval** | Hugging Face evaluation library | [[concepts/lighteval]] |
| **Galileo Eval Engineer** | Evaluation engineering | [[entities/galileo-eval-engineer]] |
| **Langwatch** | Continuous production evaluation | — |
| **Raindrop** | Agent monitoring | [[concepts/evals-vs-monitoring-debate]] |
| **Braintrust** | Eval platform | [[concepts/evals-vs-monitoring-debate]] |

---

## 5. Industry & Societal Context

### Benchmark Trustworthiness Issues

- **Benchmark Lying**: Fireworks AI on benchmark score manipulation → `raw/articles/2026-05-10_fireworks-ai_ai-benchmark-lying.md`
- **Business Benchmarks**: Cohere's "AI benchmarks for business" → `raw/articles/2026-05-10_cohere_ai-benchmarks-for-business.md`
- **Multilingual Fairness**: Cohere on multilingual/multicultural benchmark fairness → `raw/articles/2026-05-10_cohere_towards-fair-and-comprehensive-multilingual-and-multicultural-llm-benchmarking.md`
- **Benchmark Framing**: Framing effects in benchmark presentation → tag: `benchmark-framing`
- **Mismeasure of Open Source**: Mis-measurement of open-source models → [[concepts/mismeasure-of-open-source]]

### Governance & Regulation

- Regulators referencing benchmarks for compliance frameworks
- Safety, fairness, and bias contexts driving eval adoption

---

## 6. Evolution Timeline

```
2020-2022: Static benchmark golden age (MMLU, GSM8K, HumanEval, HellaSwag)
    ↓
2023: SWE-bench arrives → first agentic benchmark
    ↓
2024: Benchmark saturation becomes visible (MMLU→MMLU Pro, ARC→ARC-AGI 2)
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

## 7. Cross-Reference Links

- [[concepts/ai-benchmarks-evals-overview]] — @xeophon 18-part series
- [[concepts/ai-evaluation]] — Evaluation methodology (Langfuse Academy)
- [[concepts/evals-vs-monitoring-debate]] — Evals vs monitoring debate
- [[concepts/evaluation-harness-validity]] — OpenAI harness design framework
- [[concepts/llm-evaluation-harness]] — EleutherAI lm-eval
- [[concepts/benchmaxxing]] — Benchmark over-optimization
- [[concepts/agent-evaluation-methodology]] — Agent evaluation lifecycle
- [[concepts/swe-bench]] — SWE-bench (origin of agentic benchmarks)
- [[concepts/agent-arena]] — Agent Arena (causal inference-based)
- [[concepts/evals-for-ai-agents]] — Agent eval practices
- [[concepts/evaluation-flywheel]] — Continuous evaluation cycle
