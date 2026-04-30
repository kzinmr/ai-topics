---
title: "Skill Retrieval Augmentation (SRA)"
type: concept
created: 2026-04-30
updated: 2026-04-30
tags: [ai-agents, skill-retrieval, information-retrieval, harness-engineering, agent-capabilities, sra]
aliases:
  - sra
  - skill-retrieval-augmentation
  - sra-bench
  - skill-incorporation-bottleneck
sources:
  - raw/papers/2026-04-27_2604.24594_skill-retrieval-augmentation-for-agentic-ai.md
  - https://arxiv.org/abs/2604.24594
  - https://github.com/oneal2000/SR-Agents
status: skeleton
---

# Skill Retrieval Augmentation (SRA)

> SRA is a research paradigm for dynamically retrieving skills from an external corpus on demand, rather than listing all available skills in context. As agent skill libraries grow toward "web scale", SRA addresses the fundamental scalability bottleneck of in-context skill injection.

Coined by Su, Long, Ai et al. (2026, arXiv:2604.24594), SRA defines the three-stage pipeline of **Skill Retrieval → Skill Incorporation → Skill Application** and provides SRA-Bench (5,400 tasks, 26,262 skills) as the first dedicated benchmark for measuring skill retrieval quality in agentic systems.

The paradigm directly connects to [[concepts/harness-engineering]]: as noted by jobergum (Vespa.ai), "progressive disclosure and skill is a big part of agent harness engineering. Effective retrieval over skills is going to be big, might even become 'web scale'."

## Core Paradigm

### The Scalability Problem

Traditional agents rely on **in-context skill injection** — listing all available skills in the system prompt. This fails at scale because:

1. **Context window limits**: Skill libraries now exceed 1M items (e.g., SkillsMP)
2. **Reasoning degradation**: Model accuracy drops sharply when forced to evaluate too many candidates
3. **Attention dilution**: Noise from irrelevant skills competes with relevant ones

SRA replaces this with a **retrieval-first architecture**: skills live in an external corpus and are fetched dynamically only when needed.

### Three-Stage SRA Pipeline

| Stage | Function | Key Challenge |
|-------|----------|---------------|
| **Skill Retrieval** | Identify relevant skills from a massive corpus (26K+ skills) | Neither lexical (BM25) nor dense (BGE) is universal winner; hybrid works best |
| **Skill Incorporation** | Decide which retrieved skills to "load" into active context | **The critical bottleneck** — agents fail to distinguish gold from distractor skills |
| **Skill Application** | Execute the skill to solve the task | Executable payload quality varies; some skills are runnable code, others are descriptions only |

### What Counts as a "Skill"

A modular capability package containing:
- **Name** and **description**
- **Detailed instructions** and invocation conditions
- **Executable payload** (code, tools, or API calls)

## SRA-Bench: The Evaluation Framework

| Metric | Value |
|--------|-------|
| Test instances | 5,400 capability-intensive tasks across 6 domains |
| Total skills | 26,262 (636 gold + ~25K distractor) |
| Domains | TheoremQA, LogicBench, ToolQA, MedCalc-Bench, CHAMP, BigCodeBench |
| Evaluation stages | Retrieval accuracy → Incorporation correctness → End-task execution |

### Key Empirical Results

| Model | Direct (Parametric) | SRA (Selection) | Oracle (Perfect Skill) |
|-------|-------------------|-----------------|----------------------|
| Qwen3-235B | 53.3% | **62.8%** | 67.5% |
| Llama-3.3-70B | 47.8% | **59.2%** | 64.4% |

## The Incorporation Bottleneck

The paper's most significant finding: **current LLMs cannot reliably determine which retrieved skills to actually use**.

> "Current LLM agents tend to load skills at similar rates, regardless of whether a gold skill is retrieved or whether the task actually requires external capabilities."

Two specific failures:
- **Relevance-Awareness Gap**: Agents load skills even when the retrieved set contains no relevant skill (skill-loading hallucination)
- **Need-Awareness Gap**: Agents are no more likely to load a skill for a hard task than an easy one they can solve natively

### Progressive Disclosure vs Full-Skill Injection

SRA confirms that **Progressive Disclosure** (loading skills only after a decision is made) is more robust than listing all candidates upfront — directly validating the approach used in systems like [[concepts/markdown-based-skills]].

## Comparison with Related Concepts

| Aspect | [[concepts/agentic-search]] | [[concepts/skill-architecture-patterns]] | **SRA (this page)** |
|--------|------------------------------|------------------------------------------|---------------------|
| **Scope** | IR strategies for agent queries (web search + tool discovery) | Skill management philosophies (self-authored vs governed) | Academic framework for skill retrieval at scale |
| **Focus** | How agents find *documents/answers* | How agents *organize/govern* their skill corpus | How agents *retrieve* the right *skill* from a growing corpus |
| **Level** | IR layer + harness layer | Harness layer (skill lifecycle) | Retrieval layer (finding the right skill) |
| **Evidence** | Practitioner analysis + IR benchmarks | Source code analysis (Hermes vs OpenClaw) | Academic benchmark (SRA-Bench, 5.4K tasks) |
| **Key Insight** | BM25/lexical outperforms dense for agent queries | Self-authored skills grow faster than consolidation | Incorporation bottleneck — retrieval isn't enough |
| **Scaling Concern** | Query mismatch (agent queries ≠ user queries) | Skill corpus rot (redundant/overlapping skills) | **Corpus size → retrieval quality degradation** |

## Connection to Harness Engineering

jobergum's framing of SRA as a harness engineering problem highlights:

1. **Progressive disclosure** as the architectural principle — not loading skills until the agent commits to using them
2. **Retrieval quality** as the binding constraint — as skill corpora grow, retrieval recall/precision directly determines agent capability
3. **Skill incorporation** as the under-explored frontier — the harness needs explicit logic for deciding when and which skills to load, not just a search API

This aligns with [[concepts/harness-engineering]]'s emphasis on the outer loop: the harness should validate and gate skill selection, not delegate it entirely to the LLM's opaque reasoning.

## Research Agenda (from the paper)

1. **Structured Skill Libraries** — Moving from flat lists to graphs/hierarchies
2. **Utility-Aware Retrieval** — Optimizing retrievers for "helpfulness" rather than semantic similarity
3. **Skill Refinement** — Offline loops to debug and improve skill instructions
4. **Parametric Skill Augmentation** — Converting frequent skills to LoRAs/adapters to save context

## Related Works

- [[concepts/agentic-search]] — Level 2 (skill/tool discovery); BM25 outperforms dense for agent queries — complementary finding
- [[concepts/skill-architecture-patterns]] — Hermes Agent vs OpenClaw; the skill scale explosion SRA addresses
- [[concepts/markdown-based-skills]] — Markdown skills format; progressive disclosure pattern
- [[concepts/harness-engineering]] — Broader harness framework; outer loop gating of skill selection
- [[concepts/harness-engineering/system-architecture/agent-skills]] — Agent skills / SKILL.md bundles

## TODO

- [ ] Enrich with follow-up works: [[2604.15771]] Skill-RAG (failure-aware skill routing), [[2504.06188]] SkillFlow (production skill retrieval system)
- [ ] Track skill incorporation bottleneck research as it develops
- [ ] Monitor real-world SRA implementations (SkillsMP, community skill repositories)
