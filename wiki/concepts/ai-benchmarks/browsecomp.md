---
title: "BrowseComp"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - ai-agents
  - web-development
sources:
  - https://openai.com/index/browsecomp/
  - https://arxiv.org/abs/2504.12516
related_concepts:
  - concepts/ai-benchmarks/webarena
  - concepts/ai-benchmarks/mind2web-2
  - concepts/ai-benchmarks/online-mind2web
---

# BrowseComp

**BrowseComp** is a simple yet challenging benchmark for evaluating browsing agents, released by OpenAI (Wei et al., 2025). It tests an agent's ability to find specific, hard-to-locate information on the web through deep research browsing. The benchmark uses 1,266 "inverted" questions — queries that are difficult to find but easy to verify — making it ideal for evaluating deep-research browsing capabilities with deterministic grading.

**Paper**: [arXiv 2504.12516](https://arxiv.org/abs/2504.12516) | **Blog**: [OpenAI announcement](https://openai.com/index/browsecomp/)

## What It Measures

- **Domain**: Deep-research web browsing and information retrieval
- **Task type**: Finding specific, hard-to-locate factual information through web browsing
- **Format**: 1,266 "inverted" questions where the answer is hard to find but easy to verify — e.g., questions about obscure facts buried deep in websites
- **Evaluation**: Short verifiable answers enable **deterministic grading** — answers are either correct or incorrect, removing subjective evaluation
- **Key distinction**: Designed specifically for deep-research browsing agents like OpenAI's Deep Research product, testing the ability to persist through complex search chains

## Data/Methodology

BrowseComp consists of **1,266 questions** with the following design principles:

**Inverted Question Design**:
- Questions are crafted so the information is deliberately hard to locate on the web
- Answers are short, specific, and objectively verifiable
- This "hard-to-find / easy-to-verify" asymmetry is the core design principle

**Methodology**:
1. Questions require multiple search queries and deep browsing to answer
2. Agents must navigate through multiple web pages, following leads and cross-referencing information
3. The benchmark tests persistence, search strategy, and information synthesis
4. Grading is deterministic — no LLM judge required for answer verification

## Key Results

- **Scale**: 1,266 inverted browsing questions
- **Standard for browsing agents**: Now the standard evaluation for browsing-agent products (Deep Research, Operator)
- **Deterministic evaluation**: Unlike many agent benchmarks, BrowseComp uses simple string matching for grading, avoiding LLM-judge calibration issues
- **Training signal**: Used as a verifiable reward target for training OpenAI's deep-research agents via RL

## Related Benchmarks

- [[concepts/ai-benchmarks/webarena|WebArena]] — Tests web agents on realistic interactive website tasks (812 tasks)
- [[concepts/ai-benchmarks/mind2web-2|Mind2Web 2]] — Evaluates agentic search with Agent-as-a-Judge on 130 long-horizon live-web tasks
- [[concepts/ai-benchmarks/online-mind2web|Online-Mind2Web]] — Challenges optimistic web agent results with online evaluation on 300 live websites
- [[concepts/ai-benchmarks/webvoyager|WebVoyager]] — Tests end-to-end web navigation on 15 real websites with multimodal models

## Connections to Other Wiki Concepts

- [[concepts/evaluation/agent-evaluation-methodology|Agent Evaluation Methodology]] — BrowseComp exemplifies the verifiable-answer approach to agent evaluation, where deterministic grading avoids the biases of LLM-as-judge
- [[concepts/ai-benchmarks/tau-bench|τ-bench]] — Both benchmarks emphasize verifiable evaluation: BrowseComp through factual answer verification, τ-bench through database state checks
