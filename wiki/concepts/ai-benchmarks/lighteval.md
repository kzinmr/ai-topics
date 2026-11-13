---
title: "LightEval"
type: concept
created: 2026-04-25
updated: 2026-11-13
tags:
  - concept
  - evaluation
  - benchmark
  - huggingface
  - open-source
sources:
  - https://github.com/huggingface/lighteval
  - raw/articles/benchflow-awesome-evals-2025.md
aliases:
  - lighteval
  - Hugging Face LightEval
---

# LightEval

**LightEval** is Hugging Face's open-source, all-in-one LLM evaluation toolkit — the successor to the older `evaluate` library for LLM-era benchmarking. Maintained by the evaluation team led by [[entities/clefourrier|Céline Fourrier]], it powers the backend scoring of the [[concepts/evaluation/open-llm-leaderboard|Open LLM Leaderboard]] and covers **1000+ evaluation tasks** across multilingual, math, code, and agent-oriented suites.

## Why It Exists

The pre-LLM HF `evaluate` library was metric-oriented (BLEU, ROUGE, accuracy) and could not express the needs of generative LLM eval: multi-backend inference, chat templates, few-shot prompting harnesses, and judge-based scoring. LightEval was built as a purpose-built **evaluation harness** for that gap, while `evaluate` moved into maintenance mode.

## Key Features

- **Multi-backend inference** — one task definition runs across 🤗 Transformers, vLLM, TGI, and Ollama (and the nanotron stack for large-scale distributed eval), so leaderboard-style runs don't require re-implementing the pipeline per engine.
- **1000+ tasks** — MMLU, MMLU-Pro, BBH, GSM8K, HumanEval/EQ-Bench, HLE, multilingual suites (including the `lighteval` port of the big-bench work), and agent benchmarks such as DABStep.
- **Custom task registry** — add a task in one Python file by implementing dataset loading + prompt construction + a scoring function.
- **Chat-template aware** — few-shot prompts are built through the model's chat template, avoiding the "raw completion vs. chat model" scoring mismatches that plagued early leaderboards.
- **Judge-based scoring** — LLM-as-judge pipelines are first-class citizens (see [[concepts/evaluation/llm-as-judge]]).

## Position in the Harness Landscape

| Harness | Maintainer | Distinguishing trait |
|---|---|---|
| **LightEval** | Hugging Face | Multi-backend (Transformers/vLLM/TGI), leaderboard-grade, chat-template aware |
| lm-evaluation-harness | EleutherAI | Community-standard task zoo, CLI-first |
| OpenAI Evals | OpenAI | Registry of registry-quality evals, YAML-defined |
|Inspect AI | UK AISI | Safety/red-teaming oriented, sandboxed tool use |

## Usage

```bash
pip install lighteval
lighteval nano \
  lighteval|hellaswag|0|0 \
  --model=facebook/opt-125m
```

## Related

- [[entities/clefourrier]] — leads the HF evaluation team
- [[entities/hugging-face]] — hosting organization
- [[concepts/evaluation/open-llm-leaderboard]] — leaderboard built on LightEval
- [[concepts/evaluation/ai-benchmarks-and-evals]] — evaluation landscape
- [[concepts/evaluation/llm-as-judge]] — judge-based scoring pattern
- [[concepts/llm-course-roadmap]] — recommended eval tooling in the LLM curriculum
- [[concepts/vllm]] — one of the supported inference backends
