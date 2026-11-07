---
title: "Hightouch"
created: 2026-11-07
updated: 2026-11-07
type: entity
tags:
  - company
  - enterprise-saas
  - data-science
  - llm-as-judge
  - decision-model
sources:
  - https://hightouch.com/blog/llm-judges-identity-resolution
  - https://news.ycombinator.com/item?id=50397429
confidence: medium
---

# Hightouch

**Hightouch** is a composable customer data platform (CDP) company founded by Tejas Manohar (ex-Segment), positioned as a challenger to the traditional CDP category. Raised **$150M at a $2.75B valuation** led by Goldman Sachs and Bain Capital Ventures (per company blog, Nov 2026). Also ships an AI messaging product ("Yes, Hightouch can send messages now").

## Relevance to the AI/agent wiki

Hightouch has become an unlikely producer of high-quality **decision-model benchmarking** content, because identity resolution (IDR) QA is a natural LLM-judging workload:

- **"A Jev that can ask Opus for help gives Opus accuracy at 4x lower cost"** (Nov 4, 2026, HN 488 pts): compared Claude Opus 5.5, Gemini 3.1 Pro, GPT-6 Sol vs decision models Jev and GPT-6 Luna on grading over-merged identities; introduced the hybrid escalation result documented at [[concepts/calibrated-escalation]] — **calibration, not raw accuracy, is what makes cheap-first cascades work**.
- Stated follow-ups: under-merging detection, and open-weight vs proprietary decision models.

Their methodology notes are refreshingly explicit about limits: synthetic benchmark via pseudopeople (IHME/Univ. of Washington), "no real people appear in any example," costs/latencies self-observed. All reported numbers should be treated as vendor-side instrumentation pending independent replication.

## Related

- [[concepts/calibrated-escalation]] — their flagship finding
- [[concepts/system-one-models]] — the Jev/Luna decision-model class they benchmarked

## Sources

- [LLM Judges for Identity Resolution at 4x Lower Cost](https://hightouch.com/blog/llm-judges-identity-resolution) (Nov 4, 2026)
- [HN](https://news.ycombinator.com/item?id=50397429)
