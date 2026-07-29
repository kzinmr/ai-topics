---
title: "CryptanalysisBench"
type: benchmark
created: 2026-07-28
updated: 2026-07-28
tags:
  - benchmark
  - security
  - evaluation
  - crypto
  - anthropic
sources:
  - raw/articles/simonwillison.net--2026-jul-28-discovering-cryptographic-weaknesses-with-claude--6abd4154.md
---

# CryptanalysisBench

**CryptanalysisBench** is an evaluation benchmark for assessing the ability of large language models — specifically frontier models like [[concepts/claude/mythos-preview|Claude Mythos Preview]] — to perform novel mathematical research in cryptography. The benchmark resulted from a 60-hour continuous run of Claude Mythos Preview by Anthropic researchers (in partnership with ETH Zurich, Tel Aviv University, and University of Haifa) that discovered mathematical flaws in two prominent cryptographic targets.

## Overview

In July 2026, Anthropic researchers deployed [[concepts/claude/mythos-preview|Claude Mythos Preview]] autonomously for 60 hours — costing approximately $100,000 in API compute — to search for cryptographic weaknesses. The model succeeded in finding mathematical flaws in both HAWK (a NIST post-quantum cryptographic candidate) and a weakened version of AES. The findings were described by researchers as having "no practical impact on today's computer systems" — they are mathematical proofs of concept demonstrating capability rather than practical attacks.

The results were published in the paper *"CryptanalysisBench: Can LLMs do Cryptanalysis?"* which introduced the benchmark framework for evaluating LLM cryptanalysis capabilities.

## Key Findings

| Target | Type | Result | Practical Impact |
|--------|------|--------|:----------------:|
| **HAWK** | NIST post-quantum cryptography candidate | Mathematical flaw discovered | None — proof of concept |
| **AES (weakened variant)** | Modified/simplified AES | Mathematical weakness found | None — proof of concept |

## Benchmark Design

The CryptanalysisBench evaluation methodology involved:

- **Model**: Claude Mythos Preview running continuously
- **Duration**: 60 hours of uninterrupted autonomous operation
- **Compute cost**: ~$100,000 estimated API cost
- **Human intervention**: Minimal — primarily encouragement prompts such as "not to give up" and "find something worth publishing"
- **Prompt transparency**: Researchers published raw interaction prompts, typos and all (including misspellings like "inteligent" and "agian"), revealing the raw interaction style needed to push frontier models toward novel mathematical research
- **Partnership**: Conducted in collaboration with ETH Zurich, Tel Aviv University, and University of Haifa

## Significance

The CryptanalysisBench results are significant for several reasons:

- **Novel mathematical research**: This marks one of the first demonstrations of a frontier model autonomously conducting novel cryptanalytic research that results in publishable findings
- **Capability demonstration**: Even though the discovered weaknesses have no practical impact, they demonstrate that current frontier models possess a meaningful ability to engage with advanced mathematical reasoning in cryptography
- **Workflow insight**: The need for active encouragement (prompting the model "not to give up") and the high compute cost ($100K) reveal the current frontier of what's possible — and what's required — for LLM-driven cryptanalysis
- **Benchmark for future work**: CryptanalysisBench establishes a framework for measuring progress in LLM cryptanalysis capabilities

### Limitations

- The discovered weaknesses affect HAWK (a candidate algorithm, not yet standardized) and a weakened variant of AES (not standard AES)
- Neither finding has practical security implications for deployed systems
- The approach required substantial human guidance and compute resources, suggesting significant capability gaps remain before fully autonomous cryptanalysis is viable

## Related Pages

- [[concepts/claude/mythos]] — Claude Mythos, the model used in the research
- [[concepts/claude/mythos-preview]] — The Mythos Preview variant deployed for this work
- [[concepts/ai-benchmarks]] — Other AI evaluation benchmarks
- [[entities/simon-willison]] — Simon Willison, who reported on the results
