---
title: "Remote Labor Index"
type: concept
created: 2026-06-26
updated: 2026-07-07
tags: [benchmark, evaluation, ai-agents]
sources:
  - title: "Remote Labor Index: Measuring AI Automation of Remote Work"
    arxiv: "2510.26787"
    year: 2025
  - raw/newsletters/2026-07-06-import-ai-464-fables-writes-gpu-kernels-ai-automation-and-analog-computation.md
related_concepts:
  - "[[gdpval]]"
  - "[[theagentcompany]]"
  - "[[crmarena-pro]]"
  - "[[gaia-benchmark]]"
---

# Remote Labor Index

The Remote Labor Index is a benchmark that measures AI's capability to automate remote work. Rather than testing isolated capabilities, the Remote Labor Index tracks how well AI agents can perform the actual jobs that remote workers do — from customer service and data analysis to software development and content creation. The benchmark provides a direct measurement of AI's potential to automate specific remote occupations.

## What It Measures

The Remote Labor Index evaluates AI agents on their ability to:

- **Perform complete remote jobs**: Execute the full range of tasks that constitute a remote worker's job, not just isolated subtasks
- **Handle diverse remote occupations**: Cover the spectrum of remote work including knowledge work, creative work, technical work, and service work
- **Maintain sustained work quality**: Demonstrate consistent performance over extended task sequences that mirror actual workdays
- **Adapt to job-specific requirements**: Understand and follow the specific processes, tools, and standards of different remote occupations
- **Track automation progress**: Provide a longitudinal measure of how AI automation capability improves over time across different job categories

The benchmark is designed to answer the question: "Which remote jobs can AI effectively automate, and to what degree?"

## Data/Methodology

The Remote Labor Index is built around real remote job specifications:

- **Job-derived tasks**: Tasks are derived from actual job descriptions, performance metrics, and work products of remote workers across multiple industries
- **Occupation-level evaluation**: Rather than testing individual skills, the benchmark evaluates performance at the occupation level — can the agent do the job?
- **Work simulation**: Agents are placed in simulated work environments with realistic tools, datasets, and communication channels
- **Multi-metric scoring**: Performance is measured across multiple dimensions including task completion rate, output quality, efficiency, and error rate
- **Economic calibration**: Task difficulty and importance are calibrated to reflect the actual economic value and prevalence of different remote occupations
- **Longitudinal tracking**: The benchmark is designed to be run repeatedly over time, tracking the progression of AI automation capability across occupations

## Key Results

- AI automation capability varies enormously across remote occupations — some jobs are substantially more automatable than others
- Occupations involving structured, repetitive tasks with clear success criteria show the highest automation rates
- Jobs requiring sustained interpersonal interaction, creative judgment, or deep domain expertise remain the most resistant to automation
- The trajectory of automation capability is not uniform across occupations — some are improving rapidly while others show slow progress
- Partial automation (AI assists human workers) is achievable across a much broader range of occupations than full automation
|- The benchmark reveals that the gap between AI capability on standardized tests and real job performance remains significant

## July 2026 Update

CAIS and Scale Labs published the July 2026 Remote Labor Index results, detecting a significant increase in AI automation capability:

| Model | Success Rate |
|-------|-------------|
| **Claude Fable 5** | **16.1%** |
| Opus 4.8 | 8.3% |
| GPT-5.5 | 6.3% |

- The frontier has more than **quadrupled** (from 2.5% at launch in October 2025 to 16.1% in July 2026) in under **eight months**
- Tasks include ring design, advertisement video creation, floor plan & rendering
- Source: raw/newsletters/2026-07-06-import-ai-464-fables-writes-gpu-kernels-ai-automation-and-analog-computation.md

## Related Benchmarks

- **[[gdpval]]**: Evaluates economically valuable tasks; the Remote Labor Index specifically frames evaluation around job automation
- **[[theagentcompany]]**: Simulates company work; the Remote Labor Index evaluates across diverse remote occupations
- **[[crmarena-pro]]**: Tests specific enterprise CRM tasks; the Remote Labor Index covers broader remote work categories
- **[[gaia-benchmark]]**: Tests general agent capabilities; the Remote Labor Index focuses on occupation-level automation potential

## Connections to Other Wiki Concepts

The Remote Labor Index is directly relevant to [[future-of-work]] and [[ai-and-labor]] discussions. The benchmark provides empirical evidence for debates about [[job-displacement]] and [[technological-unemployment]] by measuring which jobs AI can actually perform. It connects to [[remote-work-trends]] and the growing importance of distributed work. The benchmark also relates to [[automation-economics]] — understanding the degree to which specific occupations can be automated informs business strategy, workforce planning, and public policy. The Remote Labor Index contributes to discussions of [[universal-basic-income]] and [[workforce-retraining]] by identifying which occupations face the most significant automation pressure.
