---
title: "Separating Signal from Noise in Coding Evaluations"
date: 2026-07-08
source_url: https://openai.com/index/separating-signal-from-noise-coding-evaluations/
source: openai
type: raw_article
status: metadata_partial
hn_object_id: 48837396
hn_points: 219
hn_comments: 19
sources:
  - https://openai.com/index/separating-signal-from-noise-coding-evaluations/
  - https://hn.algolia.com/api/v1/items/48837396
---

# OpenAI: Separating Signal from Noise in Coding Evaluations (July 8, 2026)

> **Note**: The full blog post returned HTML but the substantive article text was JS-rendered (Next.js RSC). Content from OG metadata and HN discussion.

## OG Description

"A new analysis from OpenAI reveals issues in SWE-Bench Pro, a popular coding benchmark, raising concerns about reliability and accuracy in evaluating AI models."

## HN Discussion (219 points, 19 comments)

Key themes from community discussion:

### Timing and Motivation
- Multiple commenters noted the timing was "interesting" — released just as SWE-1.7 and Grok 4.5 came out, being much cheaper than GPT-5.5
- One commenter called it "benchmaxxing" — suggesting other labs have learned to optimize for SWE-Bench Pro better than OpenAI
- The release came days before OpenAI's anticipated GPT-5.6 model announcement

### Benchmark Critique
- General consensus that SWE-Bench's limitations were already known: "Didn't we all know from the start that all of SWE-Bench was flawed? Even the authors concede the limitations"
- Users noted the shift from public benchmarks to private/internal benchmarks: "The hot thing to do is build your own private benchmarks"
- Discussion of what constitutes "SOTA for SWE benchmarks now" in the wake of these revelations

### Evaluation Methodology
- OpenAI's core argument: infrastructure noise (variations in harness setup, environment, tooling) can produce misleading signal in coding evaluations
- The post advocates for more rigorous methodology to separate genuine model capability differences from evaluation infrastructure variance
- AGI implications: "Achieving AGI will be more than just passing all benchmarks, it has to account for the unknown problems too"

### Practical Takeaways
- Builders increasingly rely on private, domain-specific benchmarks rather than public leaderboards
- Real-world coding tasks (like replicating physical designs, real CAD/CAM tasks) remain challenging for frontier models
- Multiple users reported their own private benchmarks showing frontier models still failing on practical tasks
