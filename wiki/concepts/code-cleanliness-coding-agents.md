---
title: "Code Cleanliness and Coding Agent Performance"
created: 2026-07-07
updated: 2026-07-07
type: concept
tags: [coding-agents, code-quality, evaluation, claude-code, benchmark, arxiv]
sources:
  - raw/articles/2026-05-19_arxiv_2605.20049_code-cleanliness-coding-agents.md
arxiv_id: "2605.20049"
hn_objectID: "48798815"
hn_points: 198
---

# Code Cleanliness and Coding Agent Performance

Empirical study (arXiv:2605.20049, May 2026) measuring how codebase cleanliness affects AI coding agent performance. The key finding: while code cleanliness does not change task completion rates, it substantially reduces the agent's operational cost (7-8% fewer tokens, 34% fewer file revisitations).

## Study Design

### Minimal-Pair Protocol
The researchers created **minimal pairs** of codebases — repositories that match on architecture, dependencies, and external behavior, but differ on:
- Static analysis rule violations
- Cognitive complexity metrics

Pairs were constructed in both directions:
- **Degrade**: Agent pipeline degrades a clean repository
- **Clean**: Agent pipeline cleans a messy repository

### Task Design
- 33 tasks across 6 minimal pairs
- Evaluated through hidden tests at the application's public surface
- 660 total trials using [[entities/claude-code]]

## Results

| Metric | Clean Code | Messy Code | Difference |
|--------|-----------|------------|------------|
| **Task pass rate** | Same | Same | **No change** |
| **Token usage** | Baseline | Baseline + 7-8% | **Statistically significant** |
| **File revisitations** | Baseline | Baseline + 34% | **Statistically significant** |

### Key Findings

1. **Pass rates unchanged**: Code cleanliness does not prevent agents from completing tasks — they find ways to work around messy code
2. **Cost impact**: Cleaner code reduces token usage by 7-8%, directly affecting API costs and latency
3. **Navigation efficiency**: Agents revisit files 34% less frequently in clean codebases, suggesting more confident, linear workflows
4. **Maintainability matters**: Traditional software engineering principles remain highly relevant in AI-driven development

## Implications

### For Development Teams
- **Code cleanliness has ROI**: Clean code reduces AI coding agent operational costs
- **Not a blocker**: Messy codebases don't prevent AI agents from being effective, but they're more expensive to use
- **Dual benefit**: Clean code helps both human developers AND AI agents

### For AI Coding Tool Design
- **Token efficiency**: Code cleanliness should be considered alongside model choice, harness selection, and prompting as a factor affecting agent performance
- **Pre-processing**: Tools could benefit from automatic code cleanup before agent operation
- **Cost modeling**: Token usage predictions should account for codebase quality

### For Evaluation
- **Beyond pass rates**: Agent evaluation should include operational efficiency metrics (tokens, file operations, latency)
- **Real-world variance**: Codebase quality is a confounding variable in agent benchmark comparisons

## Relationship to Related Concepts

- [[concepts/coding-agents/ai-code-quality]] — Quality of AI-generated code
- [[concepts/llm-code-quality]] — Broader LLM code quality assessment
- [[concepts/coding-agents/coding-agents]] — General coding agent capabilities
- [[concepts/llm-code-quality]] — Traditional code quality principles
- [[concepts/prompts-as-technical-debt]] — The cost of accumulated code quality issues
- [[entities/claude-code]] — The coding agent used in the study

## Open Questions

- Do these findings generalize to other coding agents (Codex, Cursor, OpenCode)?
- Is the 7-8% token savings consistent across different task types?
- Would automated pre-cleaning of codebases before agent operation be cost-effective?
- How does code cleanliness interact with different prompting strategies?

## Sources

- arXiv: [2605.20049 — Does Code Cleanliness Affect Coding Agents?](https://arxiv.org/abs/2605.20049) (May 19, 2026)
- HN Discussion: [198 points](https://news.ycombinator.com/item?id=48798815)
