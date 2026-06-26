---
title: "The Shift to Agentic AI: Evidence from Codex"
type: paper
source: openai
url: https://cdn.openai.com/pdf/5d1e1489-21c0-43e4-9d42-f87efdbf0082/the-shift-to-agentic-ai-evidence-from-codex.pdf
blog_url: https://openai.com/index/how-agents-are-transforming-work/
date: 2026-06-25
authors:
  - Drew Johnston (OpenAI)
  - David Holtz (Columbia Business School / OpenAI)
  - Alex Martin Richmond (OpenAI)
  - Christopher Ong (OpenAI)
  - Prasanna Tambe (Wharton / OpenAI)
  - Aaron Chatterji (Duke Fuqua / OpenAI)
tags:
  - agents
  - codex
  - openai
  - productivity
  - enterprise-ai
  - adoption
  - ai-agents
  - knowledge-work
  - labor-economics
---

# The Shift to Agentic AI: Evidence from Codex

**Authors**: Drew Johnston, David Holtz, Alex Martin Richmond, Christopher Ong, Prasanna Tambe, Aaron Chatterji
**Affiliations**: OpenAI, Columbia Business School, University of Pennsylvania (Wharton), Duke University (Fuqua)
**Published**: June 25, 2026
**PDF**: https://cdn.openai.com/pdf/5d1e1489-21c0-43e4-9d42-f87efdbf0082/the-shift-to-agentic-ai-evidence-from-codex.pdf
**Blog summary**: https://openai.com/index/how-agents-are-transforming-work/

---

## Abstract

Large-scale evidence of how agentic AI technology changes how people work, based on OpenAI Codex usage data across three populations: external personal-account users, external organizational-account users, and OpenAI workers. Uses an automated, privacy-protecting pipeline with classifiers to extract anonymized insights.

## Four Stylized Facts

### 1. The shift to agentic AI is rapid but uneven

- Weekly active Codex usage increased **more than fivefold** in first half of 2026
- Agentic tooling remains much less broadly used than ChatGPT overall
- Shift smallest among individual users, larger among organizational users, largest among OpenAI workers

**Codex share of output tokens (as of June 11, 2026)**:
| User Group | Codex Output Token Share |
|------------|-------------------------|
| OpenAI workers | 99.8% |
| Organizational users | 63.3% |
| Individual users | 16.5% |

- Among individual users, <1% used Codex in last 28 days — but those who adopt are unusually intensive
- Among organizational users, 17.3% used Codex in last 28 days
- Among OpenAI workers, Codex use is nearly universal

### 2. Codex use is strongly oriented toward delegated production

- Users ask Codex to carry out **concrete work tasks**: debugging, refactoring, validating changes, configuring applications, drafting documents, analyzing data
- This is **production, not consultation** — users are asking Codex to do work, not just provide advice
- Task complexity has increased over time: increasing share of users delegating tasks estimated >8 hours for experienced human

### 3. Codex use is anchored in software production but broader where adoption is deepest

- Largest share of tasks tied to software: code implementation, understanding, validation, engineering ops, application management
- But users also delegate: understanding existing systems, configuring environments, validating changes, managing repos, producing documentation
- Among OpenAI workers: usage extends into research, planning, communication, data analysis, product work, recruiting, sales

### 4. Intensive users organize around large, repeatable, parallel workflows

- Heavy users are qualitatively different from occasional users
- More likely to use skills, run longer/complex tasks, operate multiple agents concurrently
- >10% of users manage **3+ concurrent Codex agents** at some point each week
- 26.6% use **skills** (reusable instructions for complex workflows)
- At 99th percentile: users generate **60+ hours of agent turns per day** across parallel agents

## Key Data Points

### Growth Metrics
- Weekly active users grew **>5×** between Jan 1 and Jun 1, 2026
- Since Aug 2025, non-developer individual users grew **137×**, organizational **189×**

### Task Complexity Evolution
- Share of individual users submitting tasks estimated >8 hours: **nearly tenfold increase** since start of 2026
- Share >30 minutes: 80.6% (May 2026)
- Share >1 hour: 70.2% (May 2026)

### Output Token Growth (Nov 2025 → Jun 2026, within OpenAI)
- Research: **50×+ median increase**
- Legal: **13× median increase**
- Every job function: **at least 10× increase**

### Department Adoption Timeline (within OpenAI)
- Engineering: adopted first (gradual, by Dec 2025 majority)
- Legal, Finance, Recruiting: crossed majority ~April 2026
- By June 2026: every department uses Codex as primary AI tool

### Skill and Concurrency Usage
- 26.6% of users invoke skills (reusable workflow instructions)
- >10% manage 3+ concurrent agents weekly
- Among OpenAI collaboration conversations: 50.9% invoke at least one skill

## Methodology

### Three User Populations
1. **Individual users** (personal plans: Free, Go, Plus, Pro) — broad-market early adoption view
2. **Organizational users** (Business, Enterprise plans) — business settings outside OpenAI
3. **OpenAI workers** — frontier usage, minimal adoption frictions

### Classification Pipeline
- Automated, privacy-protecting pipeline
- Request-level classifier for task taxonomy (2 levels)
- Job title classifier (gpt-5-mini) for organizational users
- Persona classifier for individual users
- All on 4% user sample

### Task Taxonomy
**First-level categories**: Code Implementation, Code Understanding, Code Validation, Engineering Ops, Application Management, Documentation, Data Analysis, Research, Planning, Communication, Product Work, Recruiting, Sales, Other

**Second-level categories**: debugging, environment setup, documentation, planning, repository management, code Q&A, bug fixing, configuration, web search, etc.

## Related Literature

Key papers cited:
- Eloundou et al. (2024) — "GPTs Are GPTs" occupational exposure
- Chatterji et al. (2025) — How People Use ChatGPT (NBER 34255)
- Yang et al. (2025) — Perplexity agent adoption (arXiv:2512.07828)
- Yang et al. (2026) — How AI Agents Reshape Knowledge Work (arXiv:2606.07489)
- Sarkar (2026) — AI Agents and Higher-Order Work (SSRN 5713646)
- Baumann et al. (2026) — SWE-chat coding agent interactions (arXiv:2604.20779)
- Hitzig et al. (2026) — Agentic Coding and Persistent Returns to Expertise (Anthropic)
- Brynjolfsson et al. (2019) — AI and Modern Productivity Paradox
- Demirer et al. (2026a) — Chaining Tasks, Redefining Work (NBER 34859)
- Demirer et al. (2026b) — Writing Code vs. Shipping Code (NBER 35275)
- Dillon et al. (2025) — Shifting Work Patterns with Generative AI
- Chen & Stratton (2026) — AI in the Firm

## Implications

### For Productivity Measurement
- Agentic AI shifts unit of analysis from conversation to delegated workflow
- Token usage is a better metric than active user counts for measuring adoption depth
- Task complexity and concurrency are key dimensions of "serious" adoption

### For Job Reorganization
- Work shifts from execution to supervision, verification, coordination
- Organizations may redesign workflows around parallelized agent labor
- Individual workers manage multiple workstreams simultaneously
- Skills in task decomposition and agent orchestration become more valuable

### For Workforce Restructuring
- Non-technical roles can take on technical execution via agents
- Cross-functional work expands — agents lower cost of moving across task boundaries
- Domain expertise becomes more important for supervising delegated work
- Team composition, hiring needs, career ladders may all shift
