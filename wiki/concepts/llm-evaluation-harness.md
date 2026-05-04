---
title: "LM Evaluation Harness (lm-eval)"
type: concept
created: 2026-04-12
updated: 2026-05-04
tags:
  - evaluation
  - benchmarking
  - reproducibility
  - eleutherai
  - open-source
aliases:
  - lm-evaluation-harness
  - lm-eval
  - LLM Eval Harness
  - EleutherAI LM Evaluation Harness
sources:
  - https://github.com/EleutherAI/lm-evaluation-harness
  - https://arxiv.org/abs/2405.14782v2
  - raw/papers/2024-05-23_2405.14782_lessons-from-the-trenches.md
  - raw/articles/2024-06-11_hailey-schoelkopf-lm-evaluation-deep-dive.md
  - raw/articles/lenny-podcast-ai-evals-hottest-skill-hamel-shreya-2025-09.md
---

# LM Evaluation Harness (lm-eval)

**lm-eval** is the industry-standard open-source framework for reproducible evaluation of Large Language Models, developed and maintained by [[entities/eleutherai|EleutherAI]]. It provides a unified interface for evaluating LLMs across 60+ academic benchmarks (200+ subtasks) and powers the Hugging Face [[concepts/open-llm-leaderboard|Open LLM Leaderboard]].

## Overview

Started in 2021 to reproduce GPT-3's evaluations, lm-eval has grown into a community-driven infrastructure used by NVIDIA, Cohere, Mosaic ML, and hundreds of research labs worldwide. Its core mission is to solve the **orchestration problem**: enabling researchers to run any benchmark on any model with a standardized, versioned, and reproducible API.

## Why Evaluation is Hard

The paper *"Lessons from the Trenches on Reproducible Evaluation of Language Models"* (Biderman, Schoelkopf et al., 2024) identifies the **Key Problem**:

> "When evaluating language models, there can be many semantically equivalent but syntactically different ways of expressing the same idea... our best tools for determining whether two sentences are semantically equivalent are the very models we are seeking to evaluate."

### Common Challenges

| Challenge | Description |
|-----------|-------------|
| **Sensitivity to setup** | Small changes in prompts, few-shot examples, or tokenization drastically change metrics |
| **Lack of comparability** | Research groups use different benchmark versions, making head-to-head comparisons misleading |
| **Transparency issues** | Private evaluation codebases prevent verification and replication |
| **Metric flaws** | BLEU/ROUGE are heuristic; LLM-as-a-judge has reproducibility issues and biases |
| **Closed systems** | API-only models include non-transparent safety filters or personalization |
| **Benchmark obsolescence** | BERT-era benchmarks retrofitted for in-context learning without standardized implementations |
| **API model deprecation** | OpenAI's code-davinci-002 deprecated Jan 2024, making hundreds of studies irreproducible |

## The lm-eval Architecture

### Three Primitive Request Types

lm-eval abstracts all evaluation into three operations:

1. **Loglikelihood** — Probability of a target string conditioned on an input
   - Used for multiple-choice evaluation
   - Significantly cheaper than generation (prefill only, no token-by-token decoding)
   - **Recommendation:** Best for base models (especially smaller ones)
   - **Cons:** Prevents Chain-of-Thought, artificially easy

2. **Perplexity (PPL)** — Average loglikelihood over tokens in a dataset
   - Easy to set up for any distribution
   - Generally meaningless for instruction-tuned models

3. **Generation (generate_until)** — Text generation until a stopping condition
   - Used for free-form evaluation
   - Evaluated via: heuristics/string matching, LLM-as-a-judge, or human annotators

### Key Design Components

- **Task versioning** — Version field incremented whenever a task modification affects scoring
- **Standard error reporting** — Automatic SE via bootstrapping or sample standard deviation
- **Jinja2 templating** — Complex prompt engineering support
- **YAML task configuration** — Modular, version-controlled task definitions
- **Multiple choice normalization** — Three methods to prevent length bias:
  - Token-length normalization `P(T|I) / count(tokens)`
  - Byte-length normalization (`acc_norm`) — removes tokenizer dependence
  - Mutual information (`acc_mutual_info`) — `P(completion|prompt) / P(completion|null_prompt)`

## Best Practices (from the paper)

1. **Share exact prompts and code** — Provide links to specific code commits, not stylized descriptions
2. **Avoid copying results** — Don't pull numbers from other papers unless the exact same evaluation code was used
3. **Provide model outputs** — Share raw generations for recalculability and statistical testing
4. **Perform qualitative analysis** — Review small batches before full-scale runs to catch bugs early
5. **Measure and report uncertainty** — Report standard errors, use multiple seeds

## Prompting Style Sensitivity (Case Study)

The paper demonstrates how evaluation setup flips model rankings:

| Model | ARC (Cloze Style) | ARC (MMLU Style) | Difference |
|-------|------------------|------------------|------------|
| **Mistral-7B** | 47.1% | 51.5% | +4.4pp (prefers MMLU-style) |
| **Llama-2-7B** | 43.1% | 40.4% | -2.7pp (prefers Cloze-style) |

**Insight:** If researchers choose different prompting styles and compare results head-to-head, the comparison is "nonsensical."

## Supported Model Backends

| Backend | Command Extras | Key Features |
|---------|---------------|--------------|
| **HuggingFace** | `lm_eval[hf]` | Default, broadest model support |
| **vLLM** | `lm_eval[vllm]` | Continuous batching, tensor/data parallel |
| **SGLang** | Manual install | Fast backend, optimized memory |
| **NVIDIA NeMo** | `nemo_lm` | `.nemo` checkpoints, tensor parallelism |
| **OpenAI/Local API** | `lm_eval[api]` | OpenAI, Anthropic, OAI-compatible servers |
| **Windows ML** | `winml` | ONNX models on NPUs |
| **GGUF** | via `hf` | Quantized models via `gguf_file` arg |
| **Steered HF** | built-in | Steering vectors via PyTorch/CSV configs |

## Recent Updates (2024-2025)

- **CLI Refactor (Dec 2025):** New subcommands (`run`, `ls`, `validate`) and YAML config support via `--config`
- **Lighter installation:** Base package no longer includes `transformers` or `torch`; backends as extras
- **CoT stripping:** Added `think_end_token` to strip reasoning traces from vLLM/SGLang outputs
- **Multimodal prototyping:** Text+image input support (e.g., `mmmu` task)
- **New backends:** SGLang, Windows ML (NPU/GPU/CPU), Steered HF models

## Connection to AI Evals

While lm-eval focuses on **model-level** evaluation (standardized benchmarks, academic metrics), modern [[concepts/ai-evals]] extend to:
- **Application-level:** Real user traces, product-specific failure modes
- **Continuous:** Ongoing monitoring vs. one-time evaluation
- **LLM-as-judge:** Subjective quality assessment

## Related Concepts

- [[concepts/open-llm-leaderboard]] — Primary leaderboard powered by lm-eval
- [[entities/eleutherai]] — Development collective
- [[entities/hailey-schoelkopf]] — Primary maintainer
- [[entities/stella-biderman]] — Co-author and EleutherAI director
- [[concepts/ai-evals]] — Broader evaluation methodology

## Example: YAML Task Configuration

```yaml
task: arc_easy
dataset_path: allenai/ai2_arc
output_type: multiple_choice
doc_to_text: "Question: {{question}}\nAnswer:"
doc_to_target: "{{choices.label.index(answerKey)}}"
doc_to_choice: "{{choices.text}}"
metric_list:
  - metric: acc
    aggregation: mean
```

## Sources

- [GitHub Repository](https://github.com/EleutherAI/lm-evaluation-harness)
- [arXiv Paper: Lessons from the Trenches](https://arxiv.org/abs/2405.14782v2)
- [Hailey Schoelkopf's Deep Dive Presentation](https://docs.google.com/presentation/d/1qTaDYqLCgxkUaTfxQkN1it4tx6_jixwv9ZtsbqQgE4U/edit)
