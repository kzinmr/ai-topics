---
title: Codestral
created: 2026-06-03
updated: 2026-06-03
type: concept
tags: [model, code-model, mistral, open-source, coding-agents, evaluation, benchmark]
sources:
  - raw/articles/2024-05-29_mistral_codestral.md
  - raw/articles/2026-05-10_mistral-ai_codestral.md
  - raw/articles/2026-05-10_mistral-ai_codestral-2501.md
  - raw/articles/2026-05-10_mistral-ai_codestral-25-08.md
  - raw/articles/2026-05-10_mistral-ai_codestral-mamba.md
  - raw/articles/2026-05-10_mistral-ai_codestral-embed.md
---

# Codestral

## Overview

**Codestral** is [[entities/mistral-ai|Mistral AI]]'s family of open-weight code generation models, first introduced in May 2024. The flagship 22B-parameter model is explicitly designed for code generation tasks and supports over 80 programming languages including Python, Java, C, C++, JavaScript, Bash, Swift, and Fortran. It features a 32K context window (later expanded to 256K in newer versions) and excels at fill-in-the-middle (FIM) completion, code completion, test generation, and partial code filling. Codestral is optimized for low-latency, high-frequency coding use cases and is available via Mistral's API (la Plateforme), dedicated IDE endpoints, and self-deployment.

## Model Variants

The Codestral family spans multiple releases with distinct architectures and use cases:

### Codestral (22B, May 2024)
The original release. 22B parameters, 32K context window, open-weight under the Mistral AI Non-Production License. Trained on 80+ programming languages. Integrated with Continue.dev, Tabnine, LlamaIndex, and LangChain at launch. Available via `codestral.mistral.ai` (free beta) and `api.mistral.ai` (token-billed).

### Codestral Mamba (July 2024)
A **Mamba2** architecture variant with 7.3B parameters, released under the **Apache 2.0** license. Unlike transformer-based models, Mamba models offer linear time inference and the theoretical ability to model sequences of infinite length. Tested up to 256K tokens in-context retrieval. Designed with help from Albert Gu and Tri Dao. Available as `codestral-mamba-2407` on la Plateforme. Deployable via `mistral-inference` SDK and TensorRT-LLM.

### Codestral 25.01 (January 2025)
A major upgrade featuring a more efficient architecture and improved tokenizer, generating code approximately **2× faster** than the original. Context window expanded to **256K**. Debuted at #1 on the LMsys Copilot Arena leaderboard. Available as `codestral-latest` on la Plateforme, Google Cloud Vertex AI, and Azure AI Foundry.

### Codestral 25.08 (July 2025)
Further improvements based on production IDE telemetry:
- **+30%** increase in accepted completions
- **+10%** more retained code after suggestion
- **50%** fewer runaway generations
- +5% on IF eval v8, +5% in average MultiplE

Part of the broader **Mistral Coding Stack** alongside Devstral (agentic coding, powered by OpenHands) and Mistral Code (JetBrains/VS Code plugin).

### Codestral Embed (May 2025)
Mistral's first **code-specialized embedding model**, optimized for retrieval use cases on real-world code data. Outperforms Voyage Code 3, Cohere Embed v4.0, and OpenAI's large embedding model. Supports configurable output dimensions (e.g., 256-dim INT8 that still beats competitors). 8,192 token context window. Priced at $0.15/M tokens on API. Key benchmarks: SWE-Bench lite, CodeSearchNet, CommitPack, Spider.

## Performance Benchmarks

### Original Codestral (22B, May 2024)
| Benchmark | Category | Performance |
|---|---|---|
| HumanEval pass@1 | Python code generation | 81.1% |
| MBPP sanitised pass@1 | Python code generation | 78.2% |
| CruxEval | Python output prediction | 51.3% |
| RepoBench EM | Long-range repo completion | 34.0% (best among competitors) |
| Spider | SQL generation | 63.5% |
| HumanEval (avg 7 langs) | Multi-language | 65.6% |

### Codestral 25.01 Benchmarks (vs. original and competitors)
| Benchmark | Codestral 25.01 | Original 22B | DeepSeek Coder 33B | DeepSeek Coder V2 Lite |
|---|---|---|---|---|
| HumanEval Python | **86.6%** | 81.1% | 77.4% | 83.5% |
| MBPP | 80.2% | 78.2% | **80.2%** | 83.2% |
| RepoBench | **38.0%** | 34.0% | 28.4% | 20.0% |
| Spider SQL | 66.5% | 63.5% | 60.0% | **72.0%** |
| HumanEval avg (7 langs) | **71.4%** | 65.6% | 65.1% | 65.9% |

### FIM Performance (Codestral 25.01)
| Model | HumanEvalFIM Python | HumanEvalFIM Java | HumanEvalFIM JS | Avg |
|---|---|---|---|---|
| Codestral 25.01 | 80.2% | **89.6%** | **88.0%** | **85.9%** |
| Original Codestral | 77.0% | 83.2% | 86.1% | 82.1% |
| OpenAI FIM API | 80.0% | 84.8% | 86.5% | 83.7% |
| DeepSeek Coder 33B | 80.1% | 89.0% | 86.8% | 85.3% |

## Fill-in-the-Middle (FIM) Capability

Fill-in-the-middle is a core capability of the Codestral family, enabling the model to complete code given both a prefix and suffix — critical for IDE autocomplete scenarios. The original Codestral (22B) was benchmarked against DeepSeek Coder 33B on HumanEval FIM across Python, JavaScript, and Java, showing strong parity with larger models. Codestral 25.01 further improved FIM, achieving SOTA results in its weight class with **85.9% average** HumanEvalFIM across three languages (single-line exact match) and **95.3% pass@1**, surpassing both the OpenAI FIM API and DeepSeek Coder 33B instruct.

Codestral's FIM performance, combined with its low latency and 256K context (in 25.01+), makes it particularly well-suited for IDE integration via partners like Continue.dev, Tabnine, and Sourcegraph Cody.

## Licensing

- **Codestral (22B, May 2024)**: Released under the **Mistral AI Non-Production License** (MNPL) — free for research and testing, commercial licenses available on demand.
- **Codestral Mamba (July 2024)**: Released under the **Apache 2.0** license — free for all use, modification, and distribution.
- **Codestral 25.01 / 25.08**: Commercial deployment available via Mistral API and enterprise self-deployment; specific license terms available through Mistral.
- **Codestral Embed**: Available via API ($0.15/M tokens) and on-prem via enterprise contact.

## See Also

- [[entities/mistral-ai]] — Mistral AI company overview and model portfolio
- [[concepts/coding-agents/coding-agents]] — AI coding agent tools and workflows
- [[concepts/ai-benchmarks/swe-bench]] — SWE-Bench benchmark for software engineering evaluation
- [[concepts/coding-agents/evaluation-coding-agents]] — Evaluating AI coding agent performance
