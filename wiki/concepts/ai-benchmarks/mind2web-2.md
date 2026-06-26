---
title: "Mind2Web 2"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - ai-agents
  - web-development
  - llm-as-judge
sources:
  - https://arxiv.org/abs/2506.21506
related_concepts:
  - concepts/ai-benchmarks/online-mind2web
  - concepts/ai-benchmarks/browsecomp
  - concepts/ai-benchmarks/webarena
---

# Mind2Web 2

**Mind2Web 2** is a benchmark for evaluating agentic search capabilities using an Agent-as-a-Judge evaluation framework. Introduced by Gou et al. from the OSU NLP Group (NeurIPS 2025 Datasets & Benchmarks track, arXiv 2506.21506), it is the successor to the original Mind2Web benchmark. Mind2Web 2 features 130 long-horizon live-web agentic-search tasks and introduces a novel Agent-as-a-Judge rubric-tree grader designed for time-varying, citation-backed answers.

**Paper**: [arXiv 2506.21506](https://arxiv.org/abs/2506.21506)

## What It Measures

- **Domain**: Agentic search and deep research on the live web
- **Task type**: Long-horizon agentic search tasks requiring sustained browsing, information synthesis, and citation-backed answers
- **Format**: Agents must perform extended web research to answer complex, multi-faceted questions with sourced, verifiable responses
- **Evaluation**: **Agent-as-a-Judge** — a novel rubric-tree grading system where an LLM judge evaluates answers against structured rubrics, handling time-varying information and citation verification
- **Key distinction**: Addresses the Deep Research evaluation gap — previous benchmarks lacked the ability to evaluate long-form, citation-heavy research outputs from browsing agents

## Data/Methodology

Mind2Web 2 comprises **130 long-horizon agentic-search tasks** on live websites:

**Task Design**:
- Tasks require extended web research (not single-page interactions)
- Answers must be citation-backed and verifiable
- Information on live websites may change over time (time-varying answers)

**Agent-as-a-Judge Methodology**:
1. Tasks are posed as complex research questions requiring multi-step web browsing
2. Agents produce long-form, citation-backed answers
3. A **rubric-tree grader** (Agent-as-a-Judge) evaluates answer quality:
   - Structured rubrics define expected answer components
   - The judge handles time-varying information (answers may change as websites update)
   - Citation accuracy is verified against actual sources
4. The evaluation framework is designed to scale beyond simple factoid verification

## Key Results

- **Scale**: 130 long-horizon agentic search tasks
- **NeurIPS 2025 D&B**: Published at a top ML venue's Datasets & Benchmarks track
- **Agent-as-a-Judge innovation**: Novel evaluation framework for complex, time-varying research outputs
- **Deep Research evaluation**: Fills a critical gap in evaluating browsing agents that produce long-form research reports

## Related Benchmarks

- [[concepts/ai-benchmarks/online-mind2web|Online-Mind2Web]] — Companion benchmark by the same OSU NLP Group challenging optimistic web agent results (300 tasks)
- [[concepts/ai-benchmarks/browsecomp|BrowseComp]] — OpenAI's benchmark for deep-research browsing with deterministic grading (1,266 questions)
- [[concepts/ai-benchmarks/webarena|WebArena]] — Multi-step web tasks with functional correctness verification (812 tasks)

## Connections to Other Wiki Concepts

- [[concepts/evaluation/agent-evaluation-methodology|Agent Evaluation Methodology]] — Mind2Web 2's Agent-as-a-Judge approach represents a significant advance in evaluating complex, time-varying agent outputs where simple pass/fail verification is insufficient
- [[concepts/ai-benchmarks/tau-bench|τ-bench]] — Both tackle the challenge of evaluating agents in dynamic environments; τ-bench uses simulated users with verifiable DB states, while Mind2Web 2 uses rubric-tree judges on live web content
