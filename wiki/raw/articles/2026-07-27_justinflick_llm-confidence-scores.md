---
title: "Don't ask an LLM for a confidence score"
source: "https://justinflick.com/2026/07/27/llm-confidence-scores.html"
author: "Justin Flick"
date: "2026-07-27"
date_ingested: "2026-07-28"
publication: "justinflick.com"
tags: [llm-reliability, confidence, calibration, evaluation, prompt-engineering]
type: raw_article
---

# Don't ask an LLM for a confidence score

*Article by Justin Flick, published 2026-07-27*

The article argues that asking LLMs for confidence scores on their own outputs is fundamentally unreliable and context-dependent. Key points:

1. **Confidence scores are not absolute** — They only develop meaning when controlling for many other variables (model, prompt, task type, temperature, etc.)
2. **Cross-model comparison is invalid** — Comparing confidence scores across different models or prompts is not meaningful
3. **Calibration varies wildly** — LLM confidence calibration depends heavily on the specific task and context
4. **Alternative approaches** — Instead of raw confidence scores, use approaches like:
   - Training probes that predict LLM correctness (81% accuracy claimed in related work)
   - Using confidence probes to route between models (dumb model → smart model when uncertain)
   - Multi-sample consistency checks
   - Structured output verification

HN Discussion highlights:
- Agreement that confidence scores without controlling for variables are meaningless
- Reference to probe-based approaches for realistic confidence estimation
- Discussion of the fundamental limitations of LLM self-assessment

*Full article content successfully fetched (25,994 chars). See source URL for complete text.*
