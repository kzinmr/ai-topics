---
title: "Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity"
url: "https://substack.com/redirect/99be2d73-6efd-4741-88b9-e9e358b50e74?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E"
fetched_at: 2026-04-17T13:10:22.871777+00:00
source_date: 2026-04-17
tags: [newsletter, auto-ingested]
---

# Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity

Source: https://substack.com/redirect/99be2d73-6efd-4741-88b9-e9e358b50e74?j=eyJ1IjoiMmZseDYifQ.6O_iC1_GWCzChnbrHzSrs1hMpJpoODTUJm_FAk3tf6E

[Submitted on 7 Jun 2025 (
v1
), last revised 20 Nov 2025 (this version, v3)]
Title:
The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity
View a PDF of the paper titled The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity, by Parshin Shojaee and 5 other authors
View PDF
HTML (experimental)
Abstract:
Recent generations of language models have introduced Large Reasoning Models (LRMs) that generate detailed thinking processes before providing answers. While these models demonstrate improved performance on reasoning benchmarks, their fundamental capabilities, scaling properties, and limitations remain insufficiently understood. Current evaluations primarily focus on established math and coding benchmarks, emphasizing final answer accuracy. However, this evaluation paradigm often suffers from contamination and does not provide insights into the reasoning traces. In this work, we systematically investigate these gaps with the help of controllable puzzle environments that allow precise manipulation of complexity while maintaining consistent logical structures. This setup enables the analysis of not only final answers but also the internal reasoning traces, offering insights into how LRMs think. Through extensive experiments, we show that LRMs face a complete accuracy collapse beyond certain complexities. Moreover, they exhibit a counterintuitive scaling limit: their reasoning effort increases with problem complexity up to a point, then declines despite having remaining token budget. By comparing LRMs with their standard LLM counterparts under same inference compute, we identify three performance regimes: (1) low-complexity tasks where standard models outperform LRMs, (2) medium-complexity tasks where LRMs demonstrates advantage, and (3) high-complexity tasks where both models face complete collapse. We found that LRMs have limitations in exact computation: they fail to use explicit algorithms and reason inconsistently across scales. We also investigate the reasoning traces in more depth, studying the patterns of explored solutions and analyzing the models' computational behavior, shedding light on their strengths, limitations, and raising questions about their reasoning capabilities.
Submission history
From: Parshin Shojaee [
view email
]
[v1]
Sat, 7 Jun 2025 22:42:29 UTC (12,102 KB)
[v2]
Fri, 18 Jul 2025 04:14:22 UTC (11,640 KB)
[v3]
Thu, 20 Nov 2025 00:19:24 UTC (11,960 KB)
