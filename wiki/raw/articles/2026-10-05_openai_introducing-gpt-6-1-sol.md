---
title: 'Introducing GPT-6.1 Sol | OpenAI'
source: 'openai'
url: 'https://openai.com/index/introducing-gpt-6-1-sol'
date: '2026-10-05'
type: raw_article
tags: [raw, source]
fetched: '2026-10-05'
sha256: 4c85f24863a62a19d08c7b20d6ac4e7a4e20d381015765b3a22fff8396d63b57
description: 'OpenAI introduces GPT-6.1 Sol, an upgrade to GPT-6 Sol that nearly matches GPT-6 Astra on agentic coding, computer use, and professional work at about one-fifth of Astra's token prices.'
---

## Near-Astra intelligence for a fifth of the price

We're introducing **GPT‑6.1 Sol**, an upgrade to GPT‑6 Sol that nearly matches GPT‑6 Astra's intelligence on agentic coding, computer use, and professional work at one-fifth of Astra's standard input and output token prices. Cached input costs just **$0.10 per million tokens**—95% less than standard input pricing and 50% less than GPT‑6 Sol's cached input pricing—giving developers more room to build and run capable agents that reuse context across requests.

## A more capable Sol across tasks

GPT‑6.1 Sol offers a new balance of capability and cost for important everyday work. It delivers substantial improvements over GPT‑6 Sol across complex professional tasks, from writing and debugging code to understanding documents and executing multi-step business workflows. On several of these evaluations, it approaches GPT‑6 Astra's performance at substantially lower cost.

### Coding

On **DeepSWE v1.1**, which evaluates complex software-engineering tasks in real codebases, GPT‑6.1 Sol matches GPT‑6 Astra at roughly one-fifth of the cost, while eclipsing GPT‑6 Sol's best score by 6.4 percentage points at a lower reasoning effort and cost.

### Professional work

On **GDP.pdf**, which measures how accurately models answer professional questions using complex PDF documents (tables, charts, diagrams, fine-print details), GPT‑6.1 Sol scores higher than Opus 5.5 with fallbacks at less than half the cost per task across the tested reasoning settings. It also approaches GPT‑6 Astra's state-of-the-art performance at roughly one-fifth the cost per task.

On **AutomationBench** (1.0.6), which measures whether agents correctly complete multi-step business workflows across 47 tools (sales, marketing, operations, support, finance, HR), GPT‑6.1 Sol scores 2.2 percentage points above Opus 5.5 at medium reasoning effort, at roughly a third of the cost. That score is up 4.8 points from GPT‑6 Sol at the same setting. (The Claude Fable 5.1 datapoint understates its actual cost, omitting the cost of fallbacks, which occurred on ~40% of tasks.)

### Computer use

On **OSWorld 2.0**'s offline set (v2026.08.08 release, partial reward), GPT‑6.1 Sol outperforms GPT‑6 Sol by seven percentage points at maximum reasoning effort at less than half the cost. It comes within 2.1 points of Astra's score at maximum reasoning effort at roughly one-seventh the cost per task.

### Scientific research

On **Terminal-Bench Science 0.1** (data analysis, simulation, theorem proving), GPT‑6.1 Sol more than doubles GPT‑6 Sol's score at maximum reasoning effort at less than half the cost per task. At maximum effort, GPT‑6.1 Sol costs $5.47 per task on average, compared with $23.21 for Opus 5.5 and $23.80 for Astra — over 75% lower cost. GPT‑6 Astra still achieves the highest score (68.1%) and should be used for the most difficult scientific research tasks.

### Factuality

GPT‑6.1 Sol's largest factuality improvement over GPT‑6 Sol comes at low reasoning effort, reducing the share of responses containing a factual error from 11.4% to 7.7% (~32% reduction). Across tested reasoning settings its error rate remains within 1.9 points of GPT‑6 Astra's, at less than one-fifth the cost per task. Evaluated on de-identified ChatGPT conversations where users had flagged a prior model's error — deliberately difficult, not representative of typical usage.

## Deploying GPT‑6.1 Sol safely

GPT‑6.1 Sol shows substantial improvements over GPT‑6 Sol in alignment evaluations, bringing it closer to GPT‑6 Astra. It is more transparent about its limitations and more reliable at respecting user intent and safety constraints — lower failure rates on transparency about broken search tools, respecting explicit restrictions, and avoiding unauthorized outcomes during agentic tasks. No attempts to bypass an automated safety reviewer were observed, matching Astra and Sol. See the GPT‑6.1 Sol system card addendum (deploymentsafety.openai.com/gpt-6-1-sol).

## Pricing and availability

Available starting today to Plus, Pro, Business, Enterprise, and Edu users in ChatGPT Work and Codex. Not yet available in Chat. Developers access it via the OpenAI API as `gpt-6.1-sol`. Standard API prices: **$2 / M input tokens, $0.10 / M cached input, $10 / M output tokens**. In coming days an Ultrafast tier (up to 8x faster token generation) will be offered in Codex.
