---
title: "Coding Agents & Complexity Budgets"
type: concept
created: 2026-05-09
updated: 2026-05-27
status: L2
tags: [agentic-engineering, coding-agents, developer-tooling, workflow, software-engineering, ai-native]
sources:
  - "[[raw/articles/2025-12-01_leerob_coding-agents-complexity-budgets]]"
related:
  - "[[concepts/ai-native-development]]"
  - "[[concepts/agentic-engineering]]"
  - "[[entities/cursor]]"
---
# Coding Agents & Complexity Budgets

Lee Robinson's (Cursor, ex-Vercel) concept of **abstraction costs** and **complexity budgets** in the age of AI coding agents.

## Core Thesis

**In the era of AI and coding agents, the cost of abstraction has never been higher.**

Traditionally, it was standard to introduce CMS systems so non-developers (marketers, writers) could edit via GUI. But now that agents can manipulate code directly, intermediate abstraction layers (CMS, i18n frameworks, preview systems) hinder agent productivity.

## Case Study: cursor.com CMS → Code Migration

- **Timeline**: Estimated 2 weeks → Actual 3 days
- **Cost**: $260 in tokens (using hundreds of agents)
- **Method**: Generated migration plan with Cursor → agents implemented → humans reviewed

### Eliminated Complexity

1. **Dual account management**: Account management on both CMS and GitHub sides
2. **Preview complexity**: Static site + CMS draft mode → required Vercel authentication
3. **Internationalization (i18n)**: CMS-based translation workflow → managed in codebase
4. **Content migration**: Data export from CMS API + format conversion

## Complexity Budget

Every software system has a limited **capacity for complexity**, and abstractions consume from that budget:

- Before CMS: 30% of complexity budget consumed → 70% remaining for features
- After CMS: 60% of complexity budget consumed → 40% remaining
- AI agent era: **If agents can handle code directly, abstraction is unnecessary** → allocate full complexity budget to features

## Practical Implications

| Before (Pre-AI) | After (AI Agent Era) |
|-----------------|----------------------|
| GUI needed for non-developers | Chatbot is sufficient (marketers submit PRs on GitHub) |
| Abstraction hides complexity | Abstraction itself adds complexity |
| Static site generator + CMS | Static site generator + Markdown |
| Dedicated i18n frameworks | File-based translations |

## References

- [Coding Agents & Complexity Budgets — Lee Robinson](https://leerob.com/agents) (2025-12)
- [cursor.com](https://cursor.com) — Target site of this migration
