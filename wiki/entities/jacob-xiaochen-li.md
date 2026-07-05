---
title: Jacob Xiaochen Li
type: entity
created: 2026-06-17
updated: 2026-07-05
tags:
  - person
  - ai-researcher
  - ai-agents
  - mit
  - context-engineering
aliases: ["Jacob Li", "jacobxli"]
sources:
  - https://jacobxli.com/
  - https://jacobxli.com/blog/2026/machine-studying/
related:
  - entities/omar-khattab
  - entities/rick-battle
  - concepts/machine-studying
  - concepts/context-engineering
---

# Jacob Xiaochen Li

**Affiliation:** MIT CSAIL

Jacob Xiaochen Li is a researcher at **MIT CSAIL** working on AI agent capabilities, specifically on how agents can autonomously develop expertise from document corpora. He is the lead author of the [[concepts/machine-studying|Machine Studying]] framework and [[concepts/machine-studying#studybench-benchmark|StudyBench]] benchmark, co-authored with [[entities/omar-khattab|Omar Khattab]] and Rick Battle.

## Research Focus

Li's research investigates how AI agents can go beyond passive retrieval to actively **study** and develop expertise from corpora — a paradigm at the intersection of context management, self-supervised learning, and agentic information seeking.

## Key Contributions

### Machine Studying (June 2026)
Problem formulation for agents developing expertise from corpora. Defines *expertise* as efficiency of turning inference compute into accuracy. Three paradigms:
1. **Self-supervised objectives** — Agents learn representations directly from unlabeled document corpora
2. **Synthetic data/environments** — Creating practice problems from source material
3. **Amortized context management** — Efficiently managing growing knowledge across inference steps

### StudyBench
A benchmark evaluating agent ability to study novel domains, using DSPy and OpenClaw tasks. Measures how effectively agents can acquire and apply new domain knowledge.

## Affiliation

Li conducts this research at **MIT CSAIL** under the broader research program of [[entities/omar-khattab|Omar Khattab]], whose work spans DSPy, ColBERT, and RLM-based architectures.

## Publications

- "Machine Studying" blog post (June 17, 2026) — with Rick Battle (Broadcom), Omar Khattab (MIT CSAIL)
- StudyBench benchmark — accompanying the Machine Studying framework

## Cross-References

- [[concepts/machine-studying]] — The Machine Studying paradigm
- [[concepts/context-engineering]] — StudyBench evaluates context management strategies
- [[entities/omar-khattab]] — Advisor and research lead
- [[entities/rick-battle]] — Co-author

## Sources

- [Jacob Li's Website](https://jacobxli.com/)
- [Machine Studying Blog Post](https://jacobxli.com/blog/2026/machine-studying/)
