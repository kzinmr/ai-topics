---
title: "Cursor AI"
created: 2026-05-06
updated: 2026-05-08
type: entity
tags:
  - entity
  - company
  - coding-agents
  - devtools
  - ai-agents
aliases:
  - "Cursor"
  - "cursor.com"
related:
  - [[concepts/programbench]]
  - [[entities/openai]]
  - [[entities/anthropic]]
sources:
  - raw/newsletters/2026-05-06-ainews-silicon-valley-gets-serious-about-services.md
  - https://open.substack.com/pub/swyx/p/ainews-silicon-valley-gets-serious
  - https://www.paraform.com/talent-density-index
  - https://cursor.com/blog/series-d
  - https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html
---

# Cursor AI

**Cursor** is an AI-powered code editor and coding agent platform built by **Anysphere**. Founded by four MIT CS graduates with Olympiad pedigrees, Cursor provides AI-assisted development within an IDE (VS Code fork) and has expanded into automated CI/CD operations with agents that monitor GitHub repositories and autonomously fix CI failures. As of 2026, Cursor has grown to ~400 employees, serves the majority of Fortune 500 companies and over 50,000 teams, and has crossed $1 billion in annualized revenue.

## Overview

| Detail | Value |
|--------|-------|
| **Category** | AI Code Editor / Coding Agent |
| **Product** | Cursor IDE (VS Code fork) + CI-fix agents |
| **Founded** | 2022 (by 4 MIT CS grads: Michael Truell, Aman Sanger, Arvid Lunnemark, Sualeh Asif) |
| **Employees** | ~400 |
| **Revenue** | $1B+ annualized (Nov 2025) |
| **Valuation** | $29.3B (Series D, Nov 2025); in talks for $50B+ (Apr 2026) |
| **Total Funding** | ~$3.4B+ |
| **Key Investors** | a16z, Thrive Capital, Accel, DST Global, Coatue, NVIDIA, Google |
| **Tech Blog** | [cursor.com/blog](https://cursor.com/blog) |
| **SpaceX Interest** | SpaceX holds right to acquire Cursor for $60B or pay $10B for compute credits |
| **Key Differentiator** | IDE-native AI integration + automated CI operations |

## Key Facts

### Founding & Team

Cursor was founded by four MIT computer science graduates — **Michael Truell** (CEO), **Aman Sanger**, **Arvid Lunnemark**, and **Sualeh Asif** — all with competitive programming (Olympiad) backgrounds. The company operates out of San Francisco and has grown to approximately 400 employees while maintaining one of the most selective hiring bars in the industry.

### Hiring Bar

Cursor is infamous for its **brutal hiring process**, which is a key factor in its #4 ranking on the Paraform Talent Density Index (score: 0.799):

- **No AI in first-round interviews**: Candidates are explicitly banned from using AI tools (other than autocomplete) during technical screeners. CEO Michael Truell calls it "a great time-boxed test for skill and intelligence."
- **2-day on-site project**: Finalists spend two days at Cursor's office working on a real project alongside the core team, including meals and a final demo.
- **Aggressive recruiting**: Cursor is known to fly across the world to personally re-recruit candidates who initially declined.
- Despite the bar, Cursor continues to pull engineers from **OpenAI**, **Scale AI**, and top research labs.

### Paraform Talent Density Index

Cursor ranks **#4** on the [Paraform Talent Density Index](https://www.paraform.com/talent-density-index) (April 2026), behind only Thinking Machines Lab, OpenAI, and Anthropic. Paraform's methodology evaluates technical depth, hiring trajectory, caliber of prior employers, domain expertise, and performance signals — not raw headcount or brand recognition. Cursor's headcount of ~400 makes its top-4 ranking particularly notable, as most companies at that scale experience talent dilution.

### Funding & Valuation

| Round | Date | Amount | Valuation |
|-------|------|--------|-----------|
| Series C | Jun 2025 | $900M | — |
| Series D | Nov 2025 | $2.3B | $29.3B post-money |
| Series E (in talks) | Apr 2026 | ~$2B | $50B+ pre-money |

Enterprise revenue grew **100x** in 2025 YTD. Jensen Huang called Cursor his "favorite enterprise AI service" in October 2025.

## CI-Fix Agents (May 2026)

In May 2026, Cursor launched **agents that monitor GitHub repositories and automatically fix CI failures**. This represents a shift from assisting developers during coding to autonomously maintaining codebases in production:

- **GitHub Integration**: Agents watch PRs and CI runs
- **Autonomous Fixes**: When CI fails, the agent analyzes the error, generates a fix, and pushes a commit
- **Review Loop**: Changes go through standard PR review before merge
- **Scope**: Currently focused on common CI failure patterns (type errors, linting, test failures)

### How It Compares

| Tool | Scope | Autonomy |
|------|-------|----------|
| **Cursor IDE** | In-editor code completion and refactoring | Assistive |
| **Cursor CI-fix agents** | Automated CI failure remediation | Autonomous (with review) |
| **Devin for Security** | Vulnerability detection and remediation | Autonomous |
| **Claude Code** | CLI-based multi-file editing | Assistive/Agentic |

## SpaceX-Cursor Connection

In April 2026, it was reported that **SpaceX has the right to acquire Cursor for $60 billion** or alternatively pay $10 billion for collaborative compute credits (likely Colossus H100 equivalents). This signals a broader industry trend: top coding labs need to own both model and product.

## Related Concepts

- [[concepts/programbench]] — Meta's full-repo generation benchmark (0% top accuracy, complementary to Cursor's existing-code focus)
- [[concepts/swe-bench]] — Standard coding benchmark
- [[entities/openai]] — Codex and Agents SDK competitor
- [[entities/anthropic]] — Claude Code competitor

## Sources

- [AINews: Silicon Valley gets Serious about Services](https://open.substack.com/pub/swyx/p/ainews-silicon-valley-gets-serious) — May 6, 2026
- [Cursor Series D Blog Post](https://cursor.com/blog/series-d) — November 2025
- [CNBC: Cursor raises $2.3B at $29.3B valuation](https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html) — November 13, 2025
- [Paraform Talent Density Index](https://www.paraform.com/talent-density-index) — April 2026
- [Business Insider: Inside Cursor's hiring strategy](https://www.businessinsider.com/cursor-interview-process-no-ai-on-site-project-coding-tool-2025-6) — June 2025
