---
title: "Eval Tools Comparison: LangSmith, Braintrust, Arize Phoenix, Inspect AI"
type: concept
aliases:
  - evaluation-tools-langsmith-braintrust-arize-phoenix-inspect-ai
created: 2026-04-25
updated: 2026-05-02
tags:
  - evaluation
  - tools
  - comparison
  - braintrust
  - langsmith
  - arize-phoenix
  - inspect-ai
status: enrichment
sources:
  - raw/articles/2026-05-02_braintrust-evals-101-why-are-evals-important.md
  - https://www.braintrust.dev/foundations
---

# Eval Tools Comparison: LangSmith, Braintrust, Arize Phoenix, Inspect AI

## Braintrust

**URL:** https://www.braintrust.dev
**GitHub:** https://github.com/braintrustdata
**Course:** https://www.braintrust.dev/foundations

Braintrust provides an AI observability and evaluation platform. Key differentiators:

### Eval-Specific Features
- **LLM-as-Judge scorers** with choice scores (A/B/C → 1.0/0.5/0.0) and Chain-of-Thought reasoning
- **`trial_count` parameter** for multi-run evaluation to reduce scorer variance
- **Online scoring** — rules configured in the UI auto-run on new log data
- **Multi-level trace scoring** — per-turn (individual response) and per-trace (conversation-level)
- **Experiments** — compare prompt variants side-by-side with aggregate scores and per-input diffs
- **Topics** — semantic clustering of production logs across task areas, sentiments, and patterns
- **Playground** — interactive eval builder with dataset upload and scorer configuration
- **Braintrust BTQL API** — query project traces for batch scoring via the insert API

### Evals 101 Course (14 Modules)
A free course teaching practical eval methodology. See [[concepts/ai-evals#Braintrust Evals 101: Practical Eval Methodology]] for full details. Key modules:

| Module | Topic | Key Technique |
|--------|-------|--------------|
| 03 | Build Eval in UI | Dataset upload, prompt variants, LLM-as-Judge scorer |
| 06 | Build Eval in Code | `braintrust.Eval()` API, `autoevals.LLMClassifier` |
| 07 | Nondeterminism | `trial_count=3` for scorer variance reduction |
| 10-11 | Multi-Turn Traces | Per-turn vs per-trace scoring with CoT |
| 12 | Online Scoring | Automatic rule-based scoring on log data |
| 13 | Production Logs | 250 conversations across 5 task areas |
| 14 | Improvement Loop | Hypothesis → test → CoT analysis on failures |

### Comparison with Other Tools

| Dimension | Braintrust | LangSmith | Arize Phoenix | Inspect AI |
|-----------|-----------|-----------|---------------|-----------|
| **Company** | Braintrust Data | LangChain | Arize AI | UK AI Safety Institute (open-source) | 
| **Focus** | Observability + Evals | LLM App Observability | ML Observability + LLM Monitoring | Model Evaluation Framework |
| **Eval Style** | LLM-as-Judge + Experiments | Tracing + HITL | Drift + Performance Monitoring | Benchmark-style evals |
| **OSS Core** | No (proprietary SaaS) | LangSmith SDK (OSS tracing) | Phoenix (OSS, 2M+ monthly downloads) | Yes (Fully OSS) |
| **Code Recipes** | Evals 101 course + Cookbook | LangChain docs + tutorials | Phoenix cookbook + docs | Inspect docs + examples |
| **Eval Scoring** | LLMClassifier, code, online | LangChain evaluators | Phoenix LLM evaluators | Built-in scorers (model-graded, code) |
| **Trial Averaging** | `trial_count` parameter | Not built-in | Not built-in | Configurable per eval |

## Safety & Data Handling
- Braintrust stores scored outputs for experimentation and comparison
- See platform privacy policy for data handling details

## See Also
- [[concepts/ai-evals]] — AI evaluation general concept
- [[concepts/evaluation-flywheel]] — Iterative eval improvement cycle
- [[concepts/eval-tools-comparison]] — Alternative stub comparison page
- [[concepts/ai-eval-tools-comparison]] — Alternative stub comparison page
- [[concepts/arize]] — Arize AI entity page
- [[entities/anthropic]] — Anthropic (Promptfoo)
