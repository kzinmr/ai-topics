---
title: "YourBench"
type: concept
aliases:
  - yourbench
  - YourBench
  - Your Bench
created: 2026-04-25
updated: 2026-11-26
tags:
  - concept
  - benchmark
  - huggingface
  - evaluation
  - llm-evaluation
  - open-source
related:
  - "[[entities/clefourrier]]"
  - "[[concepts/evaluation/llm-evaluation-harness]]"
  - "[[concepts/evaluation/open-llm-leaderboard]]"
sources:
  - https://arxiv.org/abs/2504.01833
  - https://github.com/huggingface/yourbench
  - https://huggingface.co/yourbench
---

# YourBench

**YourBench** is Hugging Face's open-source framework for **dynamic, automated generation of custom LLM evaluation benchmarks directly from user-provided documents** — PDFs, Word docs, HTML, text — without manual annotation. Announced in the paper *"YourBench: Easy Custom Evaluation Sets for Everyone"* (arXiv:2504.01833, Apr 2025; lead engineer Sumuk Shashidhar, from the HF Leaderboard & Evals team that includes [[entities/clefourrier|Clémentine Fourrier]]).

## The Problem It Targets

Static benchmarks suffer from **saturation and contamination**; human evaluation is costly and slow. The result: no timely, domain-specific assessment for real-world deployments. YourBench generates **fresh, domain-tailored, grounded** benchmarks cheaply.

## How It Works

```
documents (PDF/DOCX/HTML/txt)
        │  ingestion → standardized Markdown
        ▼
natural-language brief ──→ plan.json + config.yaml
        │  single-hop + multi-hop question generation
        ▼
custom Pydantic output schemas → QA pairs
        │  citation scores, exact normalized-question dedup
        ▼
local datasets / JSONL  ·  push to HF Hub
```

- **Multi-model pipeline** — different LLMs per stage (generation, revision, validation)
- **Grounding, not parametric recall** — questions must be answerable from the provided corpus (citation-grounding checks)
- CLI: `yourbench create "Test understanding of policy exceptions" --source ./documents --model MODEL --output ./benchmark`; rerun recipes with `yourbench run` / `yourbench inspect`

## Headline Validation (paper)

- Replicated **7 MMLU subsets** from minimal source text for **< $15 total** inference cost
- **Spearman Rho = 1** — perfectly preserved relative model rankings vs the original benchmarks
- **Tempora-0325**: a novel dataset of 7K+ documents published *exclusively after March 2025* to prove generated data is grounded in inputs, not parametric memory
- Validated across **26 SoTA models from 7 families (3–671B params)**; released 150k+ QA pairs + all inference traces

## Position in the Benchmark Ecosystem

| Concern | Your answer |
|---|---|
| General eval harness | [[concepts/evaluation/llm-evaluation-harness]] / lighteval |
| Public leaderboard | [[concepts/evaluation/open-llm-leaderboard]] |
| **Custom, private, domain benchmarks** | **YourBench** |
| Contamination-resistant | Tempora-0325 post-cutoff corpora |

Connects to the wiki's broader benchmark-integrity thread ([[concepts/ai-benchmarks/frontier-swe-benchmark]], data-contamination discussion, benchmaxxing critique): YourBench is the "build your own, on your data, freshly" counter-move to saturated public sets.

## Sources

- [Paper: YourBench (arXiv:2504.01833)](https://arxiv.org/abs/2504.01833)
- [huggingface/yourbench on GitHub](https://github.com/huggingface/yourbench) — README scraped 2026-11-26
- [HF org: yourbench](https://huggingface.co/yourbench) — team incl. clefourrier, Sumuk Shashidhar, Thomas Wolf
