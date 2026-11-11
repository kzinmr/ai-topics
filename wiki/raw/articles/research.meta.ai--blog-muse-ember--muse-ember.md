---
source_url: https://research.meta.ai/blog/muse-ember
title: "Introducing Our Smallest, Most Efficient Model: Muse Ember"
site: Meta AI Research (Superintelligence Labs)
author: Meta Superintelligence Labs
published: 2026-11-09
fetched: 2026-11-11
capture: partial_html_cleaned (680KB HTML -> cleaned text; chart data present as tabular text)
hn_item: 50429024
hn_points: 330
hn_comments: 140
---

# Introducing Our Smallest, Most Efficient Model: Muse Ember

November 9, 2026 · 4 minute read — research.meta.ai/blog/muse-ember

Today, we're introducing Muse Ember, our smallest and most efficient model designed for complex reasoning execution and the work agents repeat all day: tool calls, coding subtasks, routing, extraction, and long document parsing.

Muse Ember delivers more intelligence per dollar than Claude Haiku 5.5 or GPT-6 Luna at any reasoning setting: it matches Haiku's best score at about a third of the cost and beats every Luna setting. It also sits on the efficiency frontier of the full Artificial Analysis leaderboard: no model scores higher for less per task.

## Intelligence vs. Cost Per Task

Artificial Analysis Intelligence Index against cost per task at each reasoning effort, from the raw Artificial Analysis results. Muse Ember costs are estimates at proposed pricing.

| Model | Cost per task (USD) | Intelligence Index |
|---|---|---|
| Muse Ember | $0.116 | 33.9 |
| Muse Ember | $0.136 | 35.8 |
| Claude Haiku 5.5 | $0.092 | 24.6 |
| Claude Haiku 5.5 | $0.159 | 29.6 |
| Claude Haiku 5.5 | $0.248 | 34.3 |
| Claude Haiku 5.5 | $0.411 | 36.2 |
| GPT-6 Luna | $0.073 | 21.4 |
| GPT-6 Luna | $0.104 | 23.3 |
| GPT-6 Luna | $0.152 | 27.8 |

## Muse Ember evaluation results (max reasoning)

| Eval | Muse Ember | Claude Haiku 5.5 | GPT-6 Luna |
|---|---|---|---|
| AutomationBench-AA (E2E business workflows) | **37.8** | 13.9 | 20.2 |
| Agents' Last Exam (end-to-end agent tasks) | **61.6** | 57.0 | 57.1 |
| Personal Superintelligence Index (internal composite) | **46.8** | 36.1 | 37.0 |
| Terminal-Bench 4.0 (agentic terminal coding, best published harness) | **40.9** | 39.2 | 16.4 |
| Coding Agent Index-AA | **46** | 37 | 31 |
| FrontierCode 2.0-AA (mergeability-judged) | 27.2 | **34.9** | 25.2 |
| GDP.pdf-AA (professional work over long documents) | **22.8** | 20.8 | **22.8** |
| OSWorld 2.1 computer use (partial / binary) | 69.5 / 33.8 | 68.9 / 27.8 | 50.5 / 17.0 |
| PerceptionBench w/ tools | **80.6** | 78.6 | 62.8 |
| Artificial Analysis Index | **36** | 36 | 28 |

AutomationBench-AA is reported as strict pass@1 (Artificial Analysis, Nov 9 2026).
Agents' Last Exam is a Meta internal evaluation, Linux subset.

## Availability

Muse Ember is available today on the Meta Model API, at $0.10 per million input tokens and $0.50 per million output tokens.

## Context / architecture claims

- Positioning: built for "the work agents repeat all day" — tool calls, coding subtasks, routing, extraction, long document parsing.
- 1M-token context window; up to 512K output tokens ("take in a full codebase or document set in a single call").
- Agents spend most of their tokens on many small, structured steps; Muse Ember targets carrying a business workflow end to end (pulling records, calling tools in sequence, updating systems across apps).

## Partner quotes (early testing; vendor-selected)

- **Box** (Yashodha Bhavnani, VP of AI Products): on the Box AI Complex Work Eval — "impressive accuracy, speed and token efficiency. It can score a contract against a company's negotiation playbook clause by clause and land on the right overall risk rating, or screen candidates against a detailed brief and flag the borderline ones who still qualify as alternates."
- **Cline** (Saoud Rizwan, Founder): "incredible seeing Meta release a lightweight model for developers who want a fast, low-cost model they can rely on, and for teams cutting costs by running it as the subagent in their harness. Muse Ember is purpose-built for, and excels at, subagent work like coding and document analysis."
- **Oracle** (Konstantinos Papamiltiadis, SVP Global Partnerships): "encouraging ability to tackle complex engineering tasks in our early testing."
- **Cloudflare** (Dane Knecht, CTO): "What stood out in our testing was speed. Muse Ember ran up to 30% faster at the tail than the comparable model we tested, and it handled broad, multi-repo investigation tasks well. It's a strong fit for fast, high-throughput agentic workloads."
- **You.com** (Chak Pothina, Inference Lead): "completed every coding quest in our testing with the lowest latency of any model we tested: a p95 of 2.2 seconds, about 4x to 13x faster than leading open-weight models, and with 36–48% fewer output tokens."

## Sections in original post

Agents / Coding / Multimodal / Safety / Availability (Safety section body not captured in the cleaned scrape).
