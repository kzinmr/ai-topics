---
title: "GPQA (Graduate-Level Google-Proof Q&A)"
type: concept
created: 2026-05-08
updated: 2026-05-08
status: active
tags:
  - benchmark
  - evaluation
  - methodology
  - reasoning
aliases:
  - gpqa
  - "GPQA Diamond"
sources:
  - https://arxiv.org/abs/2311.12022
  - https://github.com/idavidrein/gpqa
  - https://artificialanalysis.ai/evaluations/gpqa-diamond
  - wiki/raw/articles/2025-04-29_xeophon-ai-benchmark-eval-series.md
related_entities:
  - entities/florian-brand.md
related_concepts:
  - concepts/ai-benchmarks-and-evals.md
  - concepts/llm-evaluation.md
  - concepts/hle.md
---

# GPQA (Graduate-Level Google-Proof Q&A)

> **Part 1 of @xeophon's 18-part AI Benchmarks & Evals series.** One of the most rigorous knowledge benchmarks — tests PhD-level science reasoning in biology, physics, and chemistry with questions specifically designed to be unanswerable via web search.

**Paper**: [arXiv 2311.12022](https://arxiv.org/abs/2311.12022) (Nov 2023) | **Authors**: David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, Samuel R. Bowman (NYU, Cohere, Anthropic)

---

## What It Measures

GPQA tests **graduate-level scientific reasoning** across three domains:
- **Biology** (e.g., molecular biology, genetics, biochemistry)
- **Physics** (e.g., quantum mechanics, electromagnetism, thermodynamics)
- **Chemistry** (e.g., organic chemistry, physical chemistry, analytical chemistry)

Questions are designed to be **"Google-proof"** — answers cannot be found through web search, requiring genuine domain expertise and reasoning rather than information retrieval. The benchmark was explicitly created to enable **scalable oversight experiments**: testing whether humans can effectively supervise AI systems that may surpass human capabilities in specialized domains.

---

## Data Sourcing Method

GPQA's data creation process is notably sophisticated, similar to HLE (Humanity's Last Exam):

1. **Expert question writing**: Domain experts (PhD holders or PhD candidates) are recruited via Upwork to write challenging multiple-choice questions in their specialty areas
2. **Expert validation**: Each question is validated by another domain expert who must answer correctly, ensuring questions are answerable (not impossible) but genuinely difficult
3. **Non-expert validation**: Highly skilled non-experts (with unrestricted web access and 30+ minutes per question) attempt to answer — questions where they succeed are filtered out
4. **Monetary incentives**: Experts are paid competitive hourly rates; higher incentives in current iterations improve quality further
5. **Diamond set creation**: The 198 questions where experts agree AND non-experts struggle most form the **GPQA Diamond** subset — the most reliable subset

---

## Dataset Structure

| Subset | Questions | Description |
|--------|-----------|-------------|
| **GPQA Main Set** | 448 | Full dataset; some questions have expert disagreement |
| **GPQA Diamond** | 198 | Highest-quality subset; stringent expert agreement + non-expert difficulty filter |
| **GPQA Extended** | 546 | Newer extended set with additional questions |

All questions are **4-option multiple choice** format. The Diamond set is the standard evaluation subset used by most model providers and independent evaluators.

---

## Key Numbers

| Metric | Value |
|--------|-------|
| **Dataset size (Main)** | 448 questions |
| **Dataset size (Diamond)** | 198 questions |
| **Domains** | Biology, Physics, Chemistry only |
| **Random baseline** | 25% (4-choice MC) |
| **PhD expert accuracy** | 65% (74% after error correction) |
| **Skilled non-expert + web** | 34% |
| **GPT-4 baseline (Nov 2023)** | 39% |
| **o1 (Sep 2024)** | ~78% |
| **Human expert (OpenAI test)** | 69.7% |

### Current Leaderboard (GPQA Diamond, 2026)

| Rank | Model | Score | Source |
|------|-------|-------|--------|
| 1 | Claude Mythos Preview | 94.6% | Anthropic self-report |
| 2 | GPT-5.5 Pro | 94.4% | OpenAI self-report |
| 3 | Gemini 3.1 Pro Preview | 94.1% | Artificial Analysis |
| 4 | GPT-5.4 Pro | 94.4% | OpenAI self-report |
| 5 | Claude Opus 4.5 | ~89% | Estimated |
| 6 | o3 | 87.7% | OpenAI self-report |
| 7 | Claude Opus 4 | 83.3% | Anthropic self-report |

> **Note**: GPQA Diamond is now approaching saturation at the frontier (~94-95%). Top models significantly exceed PhD expert performance.

---

## @xeophon's Key Insights

From the Part 1 analysis (Apr 29, 2025):

1. **Diamond set > Main set**: The main set contains questions where experts disagree on the answer. Always prefer Diamond subset evaluations for serious comparisons.
2. **Bio/Physics/Chemistry only**: GPQA does NOT cover math, CS, engineering, or any other science. It's a narrow-but-deep benchmark, not a general science test.
3. **Data creation is sophisticated**: Similar pipeline to HLE — expert-written, expert-validated, non-expert filtered. One of the best data sourcing approaches.
4. **Monetary incentives**: The current version pays experts more than the original, contributing to higher quality.
5. **Scalable oversight design**: GPQA isn't just about model capability — it's designed to test whether humans can supervise AI outputs in domains where the AI may be superhuman.

---

## Strengths

- **Genuinely Google-proof**: Questions cannot be solved by web search — tests real understanding
- **Expert-validated quality**: Multi-stage validation with domain experts ensures correctness
- **Clear difficulty signal**: Large gap between experts (65%) and non-experts (34%) validates difficulty
- **Scalable oversight testbed**: Designed for research on human supervision of AI systems
- **Diamond subset**: Curated highest-quality subset provides reliable comparisons
- **Independent verification**: Multiple third-party evaluators (Artificial Analysis, Epoch AI, Vals.ai) independently benchmark

---

## Weaknesses

- **Small dataset**: 448 total (198 Diamond) — limited statistical power for comparing models with similar scores; requires ~10% accuracy difference for 80% statistical power
- **Narrow domains**: Only 3 scientific fields; misses CS, math, engineering, medicine, social sciences
- **Saturation risk**: Frontier models approaching 94-95%, close to ceiling — diminishing ability to discriminate
- **Multiple-choice limitation**: 4-option MC format may allow elimination strategies rather than true understanding
- **Potential sourcing bias**: Experts recruited via Upwork may not represent the full breadth of PhD-level expertise
- **No multimodal**: Text-only; cannot test scientific diagram/chart interpretation

---

## Use Cases

- **Scalable oversight research**: Primary use case — testing human ability to evaluate AI outputs on hard questions
- **Frontier model comparison**: Discriminating top-tier models on genuine scientific reasoning
- **RL training validation**: Detecting whether RL-trained models retain or lose scientific knowledge
- **Pre-deployment safety**: Verifying AI systems don't hallucinate confidently on expert-level science

---

## Variants & Extensions

- **GPQA Extended Set**: 546 questions — expanded version with additional domains
- **GPQA Diamond**: The de facto standard — 198 highest-quality questions
- Not to be confused with **MMLU** (broader, easier, knowledge-recall focused) or **HLE** (harder, broader domains, different creation pipeline)

---

## Related Pages

- [[concepts/ai-benchmarks-and-evals]] — Full 18-part benchmark series overview
- [[entities/florian-brand]] — Florian Brand (@xeophon), series author
- [[concepts/llm-evaluation]] — LLM evaluation landscape
- [[concepts/hle]] — Humanity's Last Exam (similar data creation approach)
- [[concepts/mmlu-pro]] — MMLU Pro (broader knowledge benchmark)

---

## Sources

1. Rein et al., "GPQA: A Graduate-Level Google-Proof Q&A Benchmark," arXiv:2311.12022, Nov 2023. https://arxiv.org/abs/2311.12022
2. GPQA GitHub repository. https://github.com/idavidrein/gpqa
3. Artificial Analysis GPQA Diamond Leaderboard. https://artificialanalysis.ai/evaluations/gpqa-diamond
4. OpenAI, "Learning to Reason with LLMs" (o1 release), Sep 2024. https://openai.com/index/learning-to-reason-with-llms/
5. Epoch AI GPQA Diamond Benchmark. https://epoch.ai/benchmarks/gpqa-diamond
6. @xeophon (Florian Brand), "AI Benchmarks & Evals Series, Part 1: GPQA," Apr 29, 2025. https://x.com/xeophon/status/1917175899948020203
