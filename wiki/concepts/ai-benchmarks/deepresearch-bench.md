---
title: "DeepResearch Bench"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags: [benchmark, evaluation, ai-agents, deep-research]
sources:
  - title: "DeepResearch Bench: A Comprehensive Benchmark for Deep Research Agents"
    arxiv: "2506.11763"
    year: 2025
related_concepts:
  - "[[gaia-benchmark]]"
  - "[[scienceagentbench]]"
  - "[[re-bench]]"
  - "[[gaia2-are]]"
---

# DeepResearch Bench

DeepResearch Bench is a comprehensive benchmark designed to evaluate deep research agents — AI systems that conduct multi-step, in-depth research by searching, reading, synthesizing, and reasoning over large bodies of information. The benchmark tests the full research workflow from question formulation through evidence gathering to final synthesis.

## What It Measures

DeepResearch Bench evaluates an agent's ability to:

- **Conduct multi-step research**: Navigate complex research questions that require gathering information from multiple sources over many steps
- **Search and retrieve information**: Effectively use search engines, databases, and document repositories to find relevant information
- **Synthesize across sources**: Integrate findings from diverse sources into coherent, well-supported conclusions
- **Maintain research coherence**: Track progress across long research sessions and avoid redundant or contradictory findings
- **Produce comprehensive reports**: Generate detailed research reports that address all aspects of a complex question
- **Handle ambiguity and uncertainty**: Appropriately qualify claims when evidence is incomplete or contradictory

Unlike simple question-answering benchmarks, DeepResearch Bench tests the sustained, iterative research process that characterizes deep investigation.

## Data/Methodology

DeepResearch Bench is structured around research tasks that require genuine multi-step investigation:

- **Complex research questions**: Questions are designed to require multiple search queries, reading of multiple documents, and synthesis across sources — tasks that cannot be answered from a single retrieval step
- **Multi-step task structure**: Each task specifies a research question along with the expected depth and breadth of investigation
- **Reference-based evaluation**: Agent outputs are compared against expert-written reference reports that identify key findings, sources, and conclusions
- **Coverage metrics**: Evaluation measures how thoroughly the agent covers the relevant landscape of a research topic
- **Quality metrics**: Assessment of writing quality, source credibility, logical coherence, and appropriate hedging of claims
- **Diverse domains**: Tasks span science, technology, policy, history, and other domains requiring deep investigation

## Key Results

- Deep research agents show dramatically better performance than single-shot retrieval-augmented generation (RAG) systems on complex questions
- The quality of research reports improves with the number of search and reading steps agents are allowed to take, up to a point of diminishing returns
- Current frontier agents produce reports that approach expert quality on well-documented topics but struggle with niche or rapidly evolving subjects
- Agent performance is highly sensitive to the quality of the underlying search infrastructure — better retrieval directly improves research quality
- Synthesis and source integration remain the weakest capabilities, with agents often failing to reconcile conflicting information across sources

## Related Benchmarks

- **[[gaia-benchmark]]**: Tests general assistant capabilities including some research tasks; DeepResearch Bench specifically targets deep, multi-step research
- **[[scienceagentbench]]**: Evaluates scientific analysis tasks that may require research but focuses on data-driven workflows
- **[[re-bench]]**: Tests ML research capabilities; DeepResearch Bench covers research across all domains
- **[[gaia2-are]]**: Scales up agent environments and evaluations, including research-heavy tasks

## Connections to Other Wiki Concepts

DeepResearch Bench is closely related to the concept of [[concepts/deep-research]] and [[concepts/retrieval-augmented-generation]] (RAG), pushing beyond simple retrieval to test sustained investigative capability. The benchmark connects to discussions of [[information-synthesis]] and [[knowledge-management]] as core AI capabilities. It also relates to [[ai-as-research-assistant]] paradigms and raises questions about [[epistemic-quality]] — whether AI-generated research reports maintain the rigor expected of human research. DeepResearch Bench has implications for [[journalism]], [[policy-analysis]], and other fields where deep investigation is a core professional skill.
