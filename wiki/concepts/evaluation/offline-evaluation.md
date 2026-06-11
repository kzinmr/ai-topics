---
title: "Offline Evaluation: Pre-Production Eval Pipelines for LLM Applications"
description: "Offline Evaluation is a pipeline for systematically evaluating LLM applications before deploying to production. It consists of three layers: offline testing, human judgment, and production telemetry."
created: 2026-04-20
updated: 2026-04-20
type: concept
status: complete
depth_tracking:
 created: 2026-04-20
 target_depth: concept-level
tags:
  - evaluation
sources:
 - raw/articles/dspy-rlm-2026-04-20.md
 - raw/articles/llm-as-judge-scoring-bias-2026-04-20.md
related:
 - ai-evals
 - llm-as-judge
 - evaluation-flywheel
 - dspy
---

# Offline Evaluation: Pre-Production Eval Pipeline

**Offline Evaluation** is a pipeline that systematically evaluates LLM applications before deploying to production. The distinction between **model evaluation vs product evaluation** is critical.

## Model Evaluation vs Product Evaluation

| Evaluation Type | Focus | Purpose |
|-----------|------|------|
| **Model Evaluation** | Base model capabilities | Sanity check (e.g., MMLU benchmark) |
| **Product Evaluation** | Full system (prompts, RAG, tools, guardrails, UI) | **The only question that matters** |

> **Key Insight:** Ask not «Is this model good?» but **«Does this system solve the user's task accurately, safely, and consistently?»**

## Three-Layer Evaluation Stack

### Layer 1: Offline Tests
|- **Timing:** Run automatically during development and PRs
|- **Purpose:** Regression detection, fast feedback
|- **Tools:** pytest, beartest, deepset haystack evaluation
|- **Metrics:** BLEU, ROUGE, exact match, regex match

### Layer 2: Human Judgment
|- **Timing:** Pre-release and major changes
|- **Purpose:** Quality assurance, nuance evaluation
|- **Method:** Expert/user evaluation team
|- **Blind spots:** Subjective, slow, scalability issues

### Layer 3: Production Telemetry
|- **Timing:** Continuous post-deployment
|- **Purpose:** Actual performance monitoring, alerts
|- **Metrics:** Error rate, latency, user feedback, task success rate

## Offline Test Design

### Test Types

| Test Type | Description | Example |
|-----------|------|-----|
| **Unit tests** | Single component | Signature output format |
| **Integration tests** | Component interaction | RAG pipeline retrieval→answer |
| **Regression tests** | Detect existing feature breakage | Tests that passed on prior version |
| **Adversarial tests** | Resistance to adversarial input | Injection attacks, prompt evasion |
| **Edge case tests** | Boundary conditions | Empty context, exception inputs |

### Creating Test Data

```
Recommended Golden Dataset (20-50 examples) composition:
├── Happy path (40%) — Standard success cases
├── Edge cases (30%) — Boundary conditions, exception handling
├── Adversarial (20%) — Injections, forced termination
└── Ambiguous (10%) — Multiple valid answers exist
```

### Evaluation Metrics Pyramid

```
        /\
       /  \     Correctness (exact match, regex)
      /----\    ------------
     /      \   Groundedness (attribution to retrieved docs)
    /--------\  ------------
   /          \ Style & Coherence (fluency, consistency)
  /------------\ ------------
 /              \ Task Success (did it solve the user's problem?)
```

## Lexical Metrics (for Regression Testing)

### BLEU/ROUGE
| Pros | Cons |
|------|------|
| Fast, consistent | Misses meaning/nuance |
| Useful for reference-based tasks | Not suitable for absolute quality evaluation |
| Suitable for regression testing |  |

> **Use case:** Confirms the same answer is being generated consistently (regression). Not suitable for measuring quality improvement.

### LLM-based Metrics (for Quality Assessment)
| Pros | Cons |
|------|------|
| Captures meaning | Slow, sometimes subjective |
| High correlation with human evaluation | Prompt-dependent |
| Useful for evaluating new approaches |  |

## Integration with CI/CD

```yaml
# .github/workflows/eval.yml (concept example)
- name: Run Offline Evals
  run: |
    pytest tests/eval/ \
      --metrics=exact_match,groundedness,llm_judge \
      --golden-dataset=tests/eval/golden.jsonl \
      --fail-on-regression
```

## Offline Eval Pipeline Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Evaluation Pipeline                    │
├─────────────────────────────────────────────────────────┤
│  ┌──────────┐    ┌───────────┐    ┌────────────────┐   │
│  │ Test     │───►│ Metric    │───►│ Aggregation    │   │
│  │ Cases    │    │ Compute   │    │ & Reporting    │   │
│  └──────────┘    └───────────┘    └────────────────┘   │
│       │               │                   │             │
│       ▼               ▼                   ▼             │
│  ┌──────────┐    ┌───────────┐    ┌────────────────┐   │
│  │ Golden   │    │ LLM-as-   │    │ Regression     │   │
│  │ Dataset  │    │ Judge     │    │ Comparison     │   │
│  └──────────┘    └───────────┘    └────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

## Relationship to LLM-as-Judge

LLM-as-Judge plays a critical role as the **metric computation layer** in offline evaluation:

| Layer | LLM-as-Judge Role |
|---------|-------------------|
| Unit/Integration tests | Fixed evaluation (BLEU/ROUGE, etc.) sufficient |
| Quality assessment | LLM-as-Judge required (subjective judgment) |
| Regression comparison | Detect differences from previous version |

## Best Practices

1. **Define metrics before building** — Clarify what to measure before starting development
2. **Start with golden dataset** — Create 20-50 representative test cases
3. **Test at multiple levels** — Combine unit/integration/e2e
4. **Automate regression detection** — Automatic execution per PR
5. **Correlate with human judgment** — Verify offline metrics align with human evaluation
6. **Iterate on metrics** — Refine metrics based on actual failure patterns

## See Also

- [[concepts/evaluation/ai-evals]] — AI Evaluation Overview
- [[concepts/evaluation/llm-as-judge]] — LLM-as-Judge Detailed Bias Analysis
- [[concepts/evaluation/evaluation-flywheel]] — Continuous Evaluation Improvement Cycle
- [[concepts/dspy]] — Eval Integration in DSPy