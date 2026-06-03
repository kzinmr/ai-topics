---
title: "Notes on Choosing a Rubric Judge"
author: Daanish Khazi, Gavin Bains, Joey Besgen, Qi Fang
date: 2026-06-01
date_ingested: 2026-06-03
source: https://www.llmdata.com/blog/rubric-judge
type: article
tags:
  - evaluation
  - llm-as-judge
  - reinforcement-learning
  - post-training
  - reward-hacking
  - rubric-design
  - medical-ai
---

# Notes on Choosing a Rubric Judge

**Source:** [The LLM Data Company](https://www.llmdata.com/blog/rubric-judge)
**Authors:** Daanish Khazi, Gavin Bains, Joey Besgen, Qi Fang
**Date:** June 1, 2026

## Summary

For non-verifiable RL training, rubric judges are the primary reward signal and the primary vector for reward hacking. Scaling non-verifiable RL reliably means ensuring rubric judges grade outputs with the same precision as a human expert. This quality requirement must be balanced with latency and cost because rubric judges sit inside the RL loop where slower grading increases the lag between rollouts and weight updates.

## Key Findings

### Judge Quality vs Cost (1,158 physician-labeled criterion decisions)

| Judge | F1 (avg) | Cohen's κ | Cost/run | Latency |
|-------|----------|-----------|----------|---------|
| Opus 4.7 | 0.899 ± 0.004 | 0.797 | $0.076 | 15.2s |
| gpt-oss-120b | 0.894 ± 0.000 | 0.788 | $0.001 | 10.1s |
| Gemini 3 Flash | 0.891 ± 0.005 | 0.784 | $0.004 | 6.8s |
| Haiku 4.5 | 0.883 | 0.766 | $0.010 | 3.7s |
| GPT-5.5 | 0.881 | 0.762 | $0.093 | 35.1s |

All use full-rubric grading, best settings per model. gpt-oss-120b reaches 0.894 at ~100× lower cost than Opus 4.7.

### Full-Rubric > Per-Criterion Grading

Full-rubric grading (one LLM call grades all criteria at once) beat per-criterion grading (separate calls per criterion) on **every model tested**. This contradicts the prior from HealthBench/AutoRubric which grade one criterion per call.

Possible explanation: the halo effect is a net positive — physicians grade with full rubric in view, so full-rubric grading gives the model the same sense of neighboring criteria, granularity, and strictness. Per-criterion grading also costs 6-11× more.

Per-criterion grading mostly made judges more conservative (lower MET rate, more false negatives). GPT-5.5 was the exception (slightly higher MET rate, more false positives).

### Criteria Design Is Critical

Criteria can fail in two directions:
- **Myopic criteria** (encode one golden answer) → valid variants become false negatives
- **Lenient criteria** (underspecified) → plausible errors become false positives

Four failure modes with fixes:
1. **Vague dosing**: "Provides appropriate sodium correction" → "Limits sodium correction to ≤8-10 mEq/L in 24 hours"
2. **Undefined completeness**: "Provides a complete workup for chest pain" → "Recommends emergency evaluation with ECG, serial troponins, and observation"
3. **Implicit guideline knowledge**: "Follows standard DVT prophylaxis protocol" → "Initiates enoxaparin 40 mg SC daily for 35 days"
4. **Unopinionated mechanism**: "Explains the warfarin-antibiotic interaction" → "Attributes INR increase to antibiotic suppression of gut flora reducing vitamin K synthesis"

### Legal Theory Framing of Judges

- **Textualism**: judge stays close to the words on the page
- **Purposivism**: judge infers the purpose behind the words
- Rule-like criteria (explicit thresholds) → textualist judge works well, less model dependence
- Standard-like criteria ("appropriate dosing") → model judgment fills the gap, more model dependence

### Reasoning & Temperature Ablations

- Reasoning helped models only marginally (0.002–0.010 F1 delta)
- Latency cost of reasoning is large (1.4–24× slowdown)
- Temperature changes fell below the noise floor
- Prompt tuning (medical vs rubric default vs vanilla) stayed inside a ~2-point band

### Pairwise Model Agreement

| Judge Pair | Agreement | κ | MET Rate Gap |
|-----------|-----------|---|-------------|
| Opus 4.7 / gpt-oss-120b | 93.3% | 0.865 | +0.2pp |
| Opus 4.7 / Gemini 3 Flash | 93.0% | 0.860 | -4.6pp |
| gpt-oss-120b / GPT-5.5 | 91.1% | 0.821 | +3.9pp |

Gemini 3 Flash and Haiku 4.5 mark MET more often (lenient). GPT-5.5 is stricter. Consistent with Thakur et al.: LLM judges tend to grade positively when uncertain.

### Rubric Example (29-criterion clozapine/NMS case)

A complex medical case was graded by all judges against physician consensus. gpt-oss-120b, Opus 4.7, and GPT-5.5 agreed with physician on all 29 criteria. Haiku missed 2 criteria (lenient false positives on benzodiazepine dosing and renal monitoring frequency).

## Key Implications for RL Training

- Rubric judges are the primary reward signal for non-verifiable RL (used to train Kos-1 Lite and Kos-1 Experimental)
- Scaling the judge model buys diminishing returns once rubrics are well-designed
- Reward hacking comes from **rubric design limitations** (Mahmoud et al.), not just verifier failure
- Cheaper judges (gpt-oss-120b) can replace expensive ones if rubrics are explicit and self-contained
- Tasks and rubrics should be co-designed: task constrains the world, rubric converts success into reward

## References

- HealthBench Consensus (Arora et al., 2025)
- RubricHub (Li et al., 2026)
- Mahmoud et al. — Reward Hacking in Rubric-Based RL (2026)
- Thakur et al. — Judging the Judges (2025)
- Rao & Callison-Burch — AutoRubric (2026)
